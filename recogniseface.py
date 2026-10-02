import cv2
from database import mark_attendance


# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")


# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


# Open camera
cap = cv2.VideoCapture(0)


# Map labels to names
names = {
    1: "Student 1",
    2: "Student 2"
}


# Keep track of students already marked
marked_students = set()


while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera not detected")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )


    for (x, y, w, h) in faces:

        # Crop face
        face = gray[y:y+h, x:x+w]


        # Predict identity
        label, confidence = recognizer.predict(face)


        # Decide whether person is known
        if confidence < 70:

            name = names.get(label, "Unknown")

            # Mark attendance only once during this camera session
            if label not in marked_students:

                mark_attendance(label)

                marked_students.add(label)

        else:

            name = "Unknown"


        # Draw rectangle
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )


        # Display name
        cv2.putText(
            frame,
            name,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )


        print(name, "Score:", round(confidence, 2))


    cv2.imshow("Face Recognition", frame)


    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()