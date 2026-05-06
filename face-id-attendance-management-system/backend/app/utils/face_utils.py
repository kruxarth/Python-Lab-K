from deepface import DeepFace
import numpy as np
import base64
from io import BytesIO
from PIL import Image
import cv2

# -------------------------------------------------------------
# ✅ EXISTING FUNCTIONS
# -------------------------------------------------------------

def b64_to_image(b64str: str):
    """Convert base64-encoded image string to NumPy array."""
    header, data = (b64str.split(",", 1) if "," in b64str else (None, b64str))
    img_bytes = base64.b64decode(data)
    img = Image.open(BytesIO(img_bytes)).convert("RGB")
    return np.array(img)

def get_face_embedding(img_np):
    """Extract face embedding using DeepFace with OpenCV backend (no TensorFlow)."""
    try:
        result = DeepFace.represent(
            img_path=img_np,
            model_name="Facenet",
            detector_backend="opencv",  # avoids tf-keras dependency
            enforce_detection=False
        )
        if not result:
            return None
        return np.array(result[0]["embedding"], dtype=np.float32)
    except Exception as e:
        print("⚠️ Face embedding error:", e)
        return None

def cosine_similarity(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def compare_encodings(known_encoding, candidate_encoding):
    similarity = cosine_similarity(known_encoding, candidate_encoding)
    distance = 1 - similarity
    return similarity, distance

def preprocess_for_ocr_cv2(img_np):
    """Preprocess image for better OCR (binarization, resizing)."""
    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
    h, w = gray.shape
    if h < 500:
        gray = cv2.resize(gray, (int(w * 2), int(h * 2)))
    return cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 11, 2)

# -------------------------------------------------------------
# 👁️‍🗨️ NEW FUNCTION — LIVENESS DETECTION (Blink / Movement)
# -------------------------------------------------------------

def detect_liveness(frame1, frame2, threshold=5000):
    """
    Detects basic liveness by checking movement between two frames.
    If there is enough pixel change, assume the person is real (not a photo).
    """
    try:
        # Convert both frames to grayscale
        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        # Calculate absolute difference
        diff = cv2.absdiff(gray1, gray2)
        _, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

        # Count changed pixels
        motion_score = np.sum(diff) / 255

        print(f"🧠 Liveness motion score: {motion_score:.2f}")
        return motion_score > threshold
    except Exception as e:
        print("⚠️ Liveness check error:", e)
        return False
