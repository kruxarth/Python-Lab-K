import cv2
import numpy as np

# Load Haar cascades for detecting face and eyes
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# -------------------------------------------------------------------
# 🌙 Helper Function: Auto brightness + contrast for low light
# -------------------------------------------------------------------
def enhance_brightness(image):
    """Enhances brightness and contrast automatically for low-light frames."""
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    enhanced = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    # Gamma correction
    gamma = 1.6
    inv_gamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** inv_gamma * 255 for i in np.arange(256)]).astype("uint8")
    return cv2.LUT(enhanced, table)


# -------------------------------------------------------------------
# 👁️ Face Liveness Detection (Anti-Spoof + Low-Light Tolerant)
# -------------------------------------------------------------------
def detect_liveness(frame1, frame2):
    """
    Detects live human faces using motion, depth, texture, and reflection analysis.
    ✅ Works in natural or low light.
    ❌ Rejects mobile or printed images.
    """
    try:
        # Auto brightness correction
        frame1 = enhance_brightness(frame1)
        frame2 = enhance_brightness(frame2)

        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        # 1️⃣ Motion between frames
        diff = cv2.absdiff(gray1, gray2)
        motion_score = np.mean(diff)

        # 2️⃣ Brightness variation
        brightness_diff = abs(np.mean(gray1) - np.mean(gray2))

        # 3️⃣ Sharpness (texture)
        lap_var = cv2.Laplacian(gray1, cv2.CV_64F).var()

        # 4️⃣ Saturation
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        saturation = np.mean(hsv[:, :, 1])

        # 5️⃣ Reflection (white/glare pixels)
        bright_spots = np.sum(gray1 > 230)
        reflection_ratio = bright_spots / gray1.size * 100

        # 6️⃣ Depth variation (3D edges)
        sobelx = cv2.Sobel(gray1, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray1, cv2.CV_64F, 0, 1, ksize=3)
        depth_variation = np.mean(np.sqrt(sobelx**2 + sobely**2))

        print(
            f"🧠 Motion={motion_score:.2f}, BrightnessΔ={brightness_diff:.2f}, "
            f"Sharpness={lap_var:.2f}, Saturation={saturation:.2f}, "
            f"Reflection={reflection_ratio:.2f}%, Depth={depth_variation:.2f}"
        )

        # 🚫 Smart Anti-Spoof Filters (Balanced for Natural Light)
        if lap_var < 15:
            print("⚠️ Low texture — allowing due to low light.")
            if motion_score < 0.5:
                return False

        # 💡 Reflection tolerance: allow up to 8%
        if reflection_ratio > 8.0:
            print("❌ Excessive glare — likely mobile or glossy surface.")
            return False
        elif reflection_ratio > 4.0:
            print("⚠️ Mild glare detected — tolerating as natural reflection.")

        if saturation > 130:
            print("❌ Oversaturated colors — possible phone screen.")
            return False

        if motion_score < 0.3 and brightness_diff < 0.3:
            print("⚠️ Minimal movement — please blink or move slightly.")
            return False

        if depth_variation < 5:
            print("❌ Very low depth — likely a flat photo.")
            return False

        # ✅ Optional: Detect eyes for blink/liveness
        faces = face_cascade.detectMultiScale(gray1, 1.3, 5)
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                roi_gray = gray1[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                if len(eyes) >= 1:
                    print("✅ Eyes detected — real human confirmed.")
                    return True

        # ✅ Backup validation (strong motion + depth)
        if motion_score > 2.0 and depth_variation > 8:
            print("✅ Liveness confirmed by motion + 3D depth.")
            return True

        print("❌ Liveness check failed — spoof or still image.")
        return False

    except Exception as e:
        print(f"⚠️ Liveness check error: {e}")
        return False


# -------------------------------------------------------------------
# 🪪 ID Card Verification (Detect real vs digital)
# -------------------------------------------------------------------
def verify_real_idcard(frame):
    """Detects whether the ID card is real (physical) or fake (digital/screen)."""
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        lap_var = cv2.Laplacian(gray, cv2.CV_64F).var()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        saturation = np.mean(hsv[:, :, 1])
        bright_spots = np.sum(gray > 240)
        reflection_ratio = bright_spots / gray.size * 100

        print(f"🪪 ID Check → Sharpness={lap_var:.2f}, Saturation={saturation:.2f}, Reflection={reflection_ratio:.2f}%")

        # 🚫 Spoof detection rules
        if lap_var < 15:
            print("⚠️ Flat surface — possible printed ID.")
            return False
        if reflection_ratio > 8:
            print("❌ Reflection/glare — digital or phone screen ID detected.")
            return False
        if saturation > 140:
            print("❌ Oversaturated colors — likely mobile screen.")
            return False

        print("✅ Verified physical ID card.")
        return True

    except Exception as e:
        print(f"⚠️ ID card verification error: {e}")
        return False
