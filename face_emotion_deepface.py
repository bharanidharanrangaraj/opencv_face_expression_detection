import cv2
from deepface import DeepFace

# ----------------------------------------
# Haar Cascade for face detection
# ----------------------------------------
face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Webcam not accessible")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(80, 80)
    )

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]

        try:
            result = DeepFace.analyze(
                face_img,
                actions=["emotion"],
                enforce_detection=False
            )

            dominant_emotion = result[0]["dominant_emotion"]
            confidence = result[0]["emotion"][dominant_emotion]

            label = f"{dominant_emotion} ({confidence:.1f}%)"

        except Exception:
            label = "Detecting..."

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            label,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Emotion Detection - DeepFace", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
