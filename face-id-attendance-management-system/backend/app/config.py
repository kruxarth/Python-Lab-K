import os

# ✅ Store DB in backend folder (not inside app/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_URL = f"sqlite:///{os.path.join(BASE_DIR, 'attendance.db')}"

JWT_SECRET = "supersecretkey"
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
FACE_CONFIDENCE_THRESHOLD = 0.5
