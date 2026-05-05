from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.auth import get_db
from app import crud
import qrcode
import os, json, time, uuid
from datetime import datetime

router = APIRouter(prefix="/qr", tags=["QR Attendance"])

# ------------------------------
# ✅ Absolute folder for QR images
# ------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QR_FOLDER = os.path.join(BASE_DIR, "generated_qr")
os.makedirs(QR_FOLDER, exist_ok=True)

# Active sessions
active_qr_tokens = {}
recently_used_qr = {}

# -------------------------------------------------------------------
# 📦 Generate QR Code (Teacher Side)
# -------------------------------------------------------------------
@router.post("/generate")
async def generate_qr(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    subject = data.get("subject")
    if not subject:
        raise HTTPException(status_code=400, detail="Subject or lab not provided")

    # Unique session for this QR
    session_id = str(uuid.uuid4())

    payload = {
        "session_id": session_id,
        "subject": subject,
        "timestamp": time.time(),
        "expires_in": 300  # 5 minutes validity
    }

    # Save QR to file
    qr_img = qrcode.make(json.dumps(payload))
    qr_path = os.path.join(QR_FOLDER, f"{session_id}.png")
    qr_img.save(qr_path)

    # Keep active session
    active_qr_tokens[session_id] = payload
    print(f"✅ QR generated for: {subject} ({session_id})")

    # Dynamically detect the host IP instead of hardcoding
    host_ip = request.client.host or "localhost"
    if host_ip.startswith("127.") or host_ip == "localhost":
        # If running locally, replace with your LAN IP
        host_ip = "192.168.33.136"

    qr_url = f"http://{host_ip}:8000/qr/image/{session_id}"

    return {
        "qr_url": qr_url,
        "subject": subject,
        "expires_in": 300
    }

# -------------------------------------------------------------------
# 🖼️ Serve the generated QR image
# -------------------------------------------------------------------
@router.get("/image/{session_id}")
def get_qr_image(session_id: str):
    path = os.path.join(QR_FOLDER, f"{session_id}.png")
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="QR not found or expired")
    return FileResponse(path, media_type="image/png")

# -------------------------------------------------------------------
# 📱 Verify QR Scan (Student Side)
# -------------------------------------------------------------------
@router.post("/verify")
def verify_qr(data: dict, request: Request, db: Session = Depends(get_db)):
    """Verifies scanned QR and marks attendance for a student."""
    try:
        # Parse the QR token
        session_data = json.loads(data.get("token", ""))
        session_id = session_data["session_id"]
        subject = session_data.get("subject")

        # Validate session existence
        if session_id not in active_qr_tokens:
            raise HTTPException(status_code=400, detail="QR expired or invalid")

        # Check expiry
        now = time.time()
        if now - active_qr_tokens[session_id]["timestamp"] > 300:
            del active_qr_tokens[session_id]
            raise HTTPException(status_code=400, detail="QR expired, please scan a new one")

        # Prevent re-scan from same device
        device_ip = request.client.host
        if device_ip in recently_used_qr and recently_used_qr[device_ip] == session_id:
            raise HTTPException(status_code=400, detail="QR already used from this device")

        recently_used_qr[device_ip] = session_id

        # Validate student by roll number
        roll_no = data.get("roll_no")
        user = crud.get_user_by_roll(db, roll_no)
        if not user:
            raise HTTPException(status_code=404, detail="Student not found")

        # Prevent duplicate attendance same day
        today = datetime.now().date()
        existing = crud.get_attendance_today(db, user.id)
        if existing:
            raise HTTPException(status_code=400, detail="Attendance already marked for today ✅")

        # Create attendance entry
        crud.create_attendance(db, user.id, f"present_via_qr ({subject})", 1.0)
        crud.log_action(db, "attendance_qr", f"{user.full_name} marked via QR ({subject})")

        return {
            "status": "success",
            "message": f"Attendance marked for {user.full_name}",
            "subject": subject
        }

    except Exception as e:
        print(f"⚠️ QR Verify Error: {e}")
        raise HTTPException(status_code=400, detail="Invalid or corrupted QR data")
