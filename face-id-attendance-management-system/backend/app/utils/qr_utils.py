import qrcode
import jwt
import time
from pathlib import Path

SECRET_KEY = "vedika_qr_secret"
QR_FOLDER = Path("qrs")
QR_FOLDER.mkdir(exist_ok=True)

def generate_qr_token(session_id: str, subject: str):
    payload = {
        "session_id": session_id,
        "subject": subject,
        "timestamp": time.time(),
        "exp": time.time() + 120  # valid for 2 minutes
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verify_qr_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def create_qr_image(token: str, session_id: str):
    img = qrcode.make(token)
    qr_path = QR_FOLDER / f"{session_id}.png"
    img.save(qr_path)
    return qr_path
