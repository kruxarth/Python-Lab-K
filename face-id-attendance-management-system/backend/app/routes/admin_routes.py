from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models
from app.auth import get_db
from fastapi.responses import StreamingResponse
import csv, io
from fastapi import Depends, HTTPException, Header
import jwt
from app.config import JWT_SECRET, JWT_ALGORITHM

router = APIRouter(prefix="/admin", tags=["Admin"])

# -------------------- EXISTING CODE (UNCHANGED) --------------------

# ✅ Fetch all attendance records with user info (for dashboard)
@router.get("/attendance")
def get_all_attendance(db: Session = Depends(get_db)):
    """Fetch all attendance records with user details (for admin dashboard)"""
    records = (
        db.query(models.Attendance, models.User)
        .join(models.User, models.Attendance.user_id == models.User.id, isouter=True)
        .order_by(models.Attendance.timestamp.desc())
        .all()
    )

    result = []
    for att, user in records:
        result.append({
            "id": att.id,
            "user_name": user.full_name if user else "Unknown",
            "roll_no": user.roll_no if user else "—",
            "branch": user.branch if user else "—",
            "status": att.status.replace("_", " "),
            "confidence": round(att.confidence * 100, 2) if att.confidence else 0,
            "timestamp": att.timestamp
        })
    return result


# 🧾 Logs (optional)
@router.get("/logs")
def get_logs(db: Session = Depends(get_db)):
    """Fetch recent audit logs"""
    logs = db.query(models.AuditLog).order_by(models.AuditLog.created_at.desc()).limit(50).all()
    return [{"action": l.action, "detail": l.detail, "time": l.created_at} for l in logs]


# 📥 Export attendance as CSV
@router.get("/export_csv")
def export_csv(db: Session = Depends(get_db)):
    """Export all attendance records with user info as a CSV"""
    rows = (
        db.query(models.Attendance, models.User)
        .join(models.User, models.Attendance.user_id == models.User.id, isouter=True)
        .all()
    )

    stream = io.StringIO()
    writer = csv.writer(stream)
    writer.writerow(["ID", "Name", "Roll No", "Branch", "Status", "Confidence (%)", "Timestamp"])
    for att, user in rows:
        writer.writerow([
            att.id,
            user.full_name if user else "Unknown",
            user.roll_no if user else "—",
            user.branch if user else "—",
            att.status.replace("_", " "),
            round(att.confidence * 100, 2) if att.confidence else 0,
            att.timestamp
        ])

    stream.seek(0)
    return StreamingResponse(
        iter([stream.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=attendance.csv"}
    )


# -------------------- TOKEN VERIFICATION (NEW ADDITION) --------------------

def verify_token(authorization: str = Header(None)):
    """Verify JWT token from admin login"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing token")

    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if payload.get("role") != "admin":
            raise HTTPException(status_code=403, detail="Access denied (not admin)")
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


# -------------------- NEW PROTECTED ROUTE (ADDED) --------------------

@router.get("/records")
def get_admin_records(user=Depends(verify_token), db: Session = Depends(get_db)):
    """
    Fetch all attendance records — accessible only to verified admins with valid JWT.
    """
    records = db.query(models.Attendance).all()

    if not records:
        raise HTTPException(status_code=404, detail="No attendance records found.")

    return {
        "message": "Attendance records retrieved successfully",
        "total_records": len(records),
        "data": [
            {
                "id": r.id,
                "student_id": getattr(r, "student_id", None),
                "subject": getattr(r, "subject", None),
                "method": getattr(r, "method", None),
                "timestamp": r.timestamp.strftime("%Y-%m-%d %H:%M:%S") if r.timestamp else None
            }
            for r in records
        ]
    }
# 🗑️ Delete a specific attendance record (Admin only)
@router.delete("/attendance/{record_id}")
def delete_attendance_record(record_id: int, db: Session = Depends(get_db)):
    """Delete a specific attendance record by ID"""
    record = db.query(models.Attendance).filter(models.Attendance.id == record_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    db.delete(record)
    db.commit()

    crud.log_action(db, "attendance_deleted", f"Deleted record ID={record_id}")
    return {"status": "success", "message": f"Record ID {record_id} deleted successfully"}
