from sqlalchemy.orm import Session
from app import models
from app.auth import get_password_hash
import pickle
from datetime import datetime, timedelta, timezone  # ✅ added

# 🧍 Create New User
def create_user(db: Session, full_name: str, email: str, password: str):
    user = models.User(
        full_name=full_name,
        email=email,
        password_hash=get_password_hash(password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# 📩 Fetch a Single User by Email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# 🧠 Get All Face Encodings (for recognition)
def get_all_user_encodings(db: Session):
    users = db.query(models.User).all()
    data = []
    for u in users:
        if u.face_encoding:
            data.append((u.id, u.full_name, pickle.loads(u.face_encoding)))
    return data

# 💾 Save User’s Face Encoding
def save_face_encoding(db: Session, user_id: int, encoding):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.face_encoding = pickle.dumps(encoding)
        db.commit()

# 💾 Save Extracted ID OCR Text
def save_id_ocr(db: Session, user_id: int, text: str):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.id_ocr_text = text
        db.commit()

# 🧾 ✅ Create Attendance Entry (with real IST timestamp)
def create_attendance(db: Session, user_id, status, confidence):
    # Set Indian Standard Time (UTC +5:30)
    IST = timezone(timedelta(hours=5, minutes=30))
    current_time_ist = datetime.now(IST)

    att = models.Attendance(
        user_id=user_id,
        status=status,
        confidence=confidence,
        timestamp=current_time_ist  # ✅ saves true current IST
    )
    db.add(att)
    db.commit()
    db.refresh(att)
    return att

# 🧮 Log System Events (like enrollments, attendance)
def log_action(db: Session, action, detail):
    log = models.AuditLog(action=action, detail=detail)
    db.add(log)
    db.commit()

# 🪪 ✅ Get All Registered Users (for OCR-based ID Attendance)
def get_all_users(db: Session):
    return db.query(models.User).all()

from datetime import datetime, date
from app import models

def get_user_by_roll(db, roll_no):
    return db.query(models.User).filter(models.User.roll_no == roll_no).first()

def get_attendance_today(db, user_id):
    today = date.today()
    return db.query(models.Attendance).filter(
        models.Attendance.user_id == user_id,
        models.Attendance.timestamp >= datetime.combine(today, datetime.min.time()),
        models.Attendance.timestamp <= datetime.combine(today, datetime.max.time())
    ).first()
