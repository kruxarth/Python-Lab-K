from datetime import datetime, date
from sqlalchemy import and_
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app.auth import get_db
from app.utils.liveness_utils import detect_liveness, verify_real_idcard
from app.schemas import AttendanceIn, AttendanceOut, LivenessAttendanceIn
from app.utils.face_utils import (
    b64_to_image,
    get_face_embedding,
    compare_encodings
)
import pytesseract
from difflib import SequenceMatcher
import cv2
import numpy as np
import re

# ✅ Configure Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

router = APIRouter(prefix="/attendance", tags=["Attendance"])


# -------------------------------------------------------------------
# 🧩 Helper Function: Text Normalizer for OCR Cleanup
# -------------------------------------------------------------------
def normalize_text(text):
    """Cleans OCR text: removes symbols, fixes common misreads."""
    text = text.lower()
    replacements = {
        'o': '0', 'i': '1', 'l': '1',
        's': '5', 'b': '8', 'g': '6',
        'z': '2', 'q': '9'
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r'[^a-z0-9]', '', text)
    return text


# -------------------------------------------------------------------
# 🎯 1️⃣ Face Attendance Route (with Liveness Detection)
# -------------------------------------------------------------------
@router.post("/recognize", response_model=AttendanceOut)
def recognize_face(payload: LivenessAttendanceIn, db: Session = Depends(get_db)):
    """Marks attendance using face recognition + liveness verification"""
    if not payload.image_b64_1 or not payload.image_b64_2:
        raise HTTPException(status_code=400, detail="Missing one or both image frames")

    frame1 = b64_to_image(payload.image_b64_1)
    frame2 = b64_to_image(payload.image_b64_2)
    if frame1 is None or frame2 is None:
        raise HTTPException(status_code=400, detail="Invalid frames for liveness check")

    # 🧠 Step 1: Liveness detection
    if not detect_liveness(frame1, frame2):
        raise HTTPException(status_code=400, detail="Liveness check failed (please blink or move slightly)")

    # 🧩 Step 2: Get embedding for recognition
    embedding = get_face_embedding(frame1)
    if embedding is None:
        raise HTTPException(status_code=400, detail="No face detected in frame")

    # 🧠 Step 3: Compare with stored encodings
    known_faces = crud.get_all_user_encodings(db)
    best_user, best_sim = None, 0.0

    for uid, name, known_enc in known_faces:
        sim, _ = compare_encodings(known_enc, embedding)
        if sim > best_sim:
            best_user, best_sim = uid, sim

    # ✅ Step 4: Threshold check + once-per-day validation
    threshold = 0.5
    if best_sim >= threshold and best_user:
        today = date.today()
        existing_attendance = db.query(crud.models.Attendance).filter(
            and_(
                crud.models.Attendance.user_id == best_user,
                crud.models.Attendance.timestamp >= datetime.combine(today, datetime.min.time()),
                crud.models.Attendance.timestamp <= datetime.combine(today, datetime.max.time())
            )
        ).first()

        if existing_attendance:
            raise HTTPException(status_code=400, detail="Attendance already marked for today ")

        att = crud.create_attendance(db, best_user, "present_via_face", best_sim)
        crud.log_action(db, "attendance_marked_face", f"user_id={best_user}, sim={best_sim:.2f}")
        return att

    crud.log_action(db, "attendance_unknown_face", f"best_sim={best_sim:.2f}")
    raise HTTPException(status_code=404, detail="Face not recognized")


# -------------------------------------------------------------------
# 🪪 2️⃣ ID Card Attendance Route (OCR-based + Anti-spoof + Smart Crop)
# -------------------------------------------------------------------
def is_similar(a, b, threshold=0.7):
    """Fuzzy string similarity for OCR matching"""
    return SequenceMatcher(None, a, b).ratio() >= threshold


@router.post("/id_recognize")
def recognize_id_card(payload: AttendanceIn, db: Session = Depends(get_db)):
    """Marks attendance using ID card OCR (Name + Roll No + Branch)"""
    if not payload.image_b64:
        raise HTTPException(status_code=400, detail="No ID image received")

    img_np = b64_to_image(payload.image_b64)

    # ✅ Step 0: Verify real physical ID card
    if not verify_real_idcard(img_np):
        raise HTTPException(
            status_code=400,
            detail="Fake or digital ID detected — please show a real physical ID card."
        )

    # ✅ Step 1: Try ROI (bottom 30%) and full ID fallback
    height, width, _ = img_np.shape
    roi = img_np[int(height * 0.6):int(height * 0.9), int(width * 0.05):int(width * 0.95)]
    images_to_try = [roi, img_np]
    extracted_text, clean_text = "", ""
    text_found = False

    for idx, img in enumerate(images_to_try):
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        gray = cv2.bilateralFilter(gray, 9, 75, 75)
        gray = cv2.convertScaleAbs(gray, alpha=2.0, beta=25)
        gray = cv2.medianBlur(gray, 3)
        gray = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 11
        )

        if np.mean(gray) < 130:
            gray = cv2.bitwise_not(gray)

        custom_config = (
            r'--oem 3 --psm 7 '
            r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'
        )

        text_try = pytesseract.image_to_string(gray, lang="eng", config=custom_config).lower().strip()

        if text_try:
            extracted_text = text_try
            clean_text = normalize_text(extracted_text)
            print(f"✅ Text found on attempt {idx + 1}: {extracted_text}")
            text_found = True
            break

    if not text_found or not extracted_text.strip():
        raise HTTPException(status_code=400, detail="No readable text found on ID card")

    # ✅ Step 2: Detect Roll No pattern
    roll_matches = re.findall(r"[a-z]{1,3}\d{2,6}[a-z0-9]{0,4}", extracted_text)
    detected_roll = roll_matches[0].replace(" ", "").replace("-", "") if roll_matches else None
    if detected_roll:
        print(f"🎯 Detected Roll No (Pattern Match): {detected_roll}")

    # ✅ Step 3: Match with Database
    users = crud.get_all_users(db)
    matched_user = None

    for u in users:
        full_name = u.full_name.lower() if getattr(u, "full_name", None) else ""
        roll_no = str(u.roll_no).lower().replace(" ", "").replace("-", "") if getattr(u, "roll_no", None) else ""
        branch = u.branch.lower() if getattr(u, "branch", None) else ""

        if roll_no and roll_no in clean_text:
            matched_user = u
            print(f"✅ Roll No matched directly: {roll_no}")
            break

        if detected_roll and roll_no and (detected_roll in roll_no or roll_no in detected_roll):
            matched_user = u
            print(f"✅ Roll No matched (pattern): {roll_no}")
            break

        if SequenceMatcher(None, roll_no, clean_text).ratio() > 0.65:
            matched_user = u
            print(f"✅ Fuzzy Roll No match for: {roll_no}")
            break

        if is_similar(full_name, extracted_text, 0.4) or is_similar(branch, extracted_text, 0.4):
            matched_user = u
            print(f"✅ Matched by name/branch: {u.full_name}")
            break

    # ✅ Step 4: Mark attendance (once per day)
    if matched_user:
        today = date.today()
        existing_attendance = db.query(crud.models.Attendance).filter(
            and_(
                crud.models.Attendance.user_id == matched_user.id,
                crud.models.Attendance.timestamp >= datetime.combine(today, datetime.min.time()),
                crud.models.Attendance.timestamp <= datetime.combine(today, datetime.max.time())
            )
        ).first()

        if existing_attendance:
            raise HTTPException(status_code=400, detail="Attendance already marked for today ✅")

        att = crud.create_attendance(db, matched_user.id, "present_via_id", 1.0)
        crud.log_action(db, "attendance_marked_id", f"{matched_user.roll_no} recognized via ID")
        return {
            "status": "present_via_id",
            "full_name": matched_user.full_name,
            "roll_no": matched_user.roll_no,
            "branch": matched_user.branch
        }

    crud.log_action(db, "attendance_unknown_id", f"text={extracted_text[:80]}...")
    raise HTTPException(status_code=404, detail="ID not recognized. Try better lighting or ensure Roll No is visible.")
