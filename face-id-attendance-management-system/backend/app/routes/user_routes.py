from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from app import crud
from app.auth import get_db, get_current_user
from app.utils.face_utils import b64_to_image, get_face_embedding, preprocess_for_ocr_cv2
import pytesseract

# ✅ Configure Tesseract for OCR (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

router = APIRouter(prefix="/users", tags=["User"])

# -------------------------------------------------------------------
# 🧍 User Enrollment (Face + ID Card)
# -------------------------------------------------------------------
@router.post("/enroll")
def enroll_user(
    full_name: str = Form(...),
    roll_no: str = Form(...),
    branch: str = Form(...),
    face_image_b64: str = Form(...),
    id_image_b64: str = Form(...),
    db: Session = Depends(get_db)
):
    print(f"📩 Enrollment request received for: {roll_no} ({branch})")

    # ✅ Check if Roll Number already exists
    existing = db.query(crud.models.User).filter_by(roll_no=roll_no).first()
    if existing:
        raise HTTPException(status_code=400, detail="Roll Number already registered")

    # ✅ Create new user
    user = crud.models.User(
        full_name=full_name,
        roll_no=roll_no,
        branch=branch
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # ✅ Process face image → generate embedding
    try:
        face_img = b64_to_image(face_image_b64)
        embedding = get_face_embedding(face_img)
        if embedding is None:
            raise HTTPException(status_code=400, detail="No face detected in the face image")
        crud.save_face_encoding(db, user.id, embedding)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Face processing failed: {str(e)}")

    # ✅ Process ID card → OCR extraction
    try:
        id_img = b64_to_image(id_image_b64)
        id_proc = preprocess_for_ocr_cv2(id_img)
        text = pytesseract.image_to_string(id_proc, lang="eng")
        crud.save_id_ocr(db, user.id, text)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"OCR failed: {str(e)}")

    # ✅ Log user enrollment
    crud.log_action(db, "user_enrolled", f"Roll No: {roll_no}, Branch: {branch}")

    return {"status": "enrolled", "user_id": user.id, "roll_no": roll_no, "branch": branch}


# -------------------------------------------------------------------
# 👤 Current User Info (if auth enabled later)
# -------------------------------------------------------------------
@router.get("/me")
def current_user(user=Depends(get_current_user)):
    return {"id": user.id, "roll_no": user.roll_no, "full_name": user.full_name, "branch": user.branch}


# -------------------------------------------------------------------
# ❌ Delete User by ID (for admin use)
# -------------------------------------------------------------------
@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    from app import models
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    crud.log_action(db, "user_deleted", f"Deleted user {user_id}")
    return {"status": "deleted"}
