import cv2
from database import mark_attendance


# Student ID → Student Name
names = {
    1: "Student 1",
    2: "Student 2"
}


# Load trained face recognition model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")


# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)


# Open laptop camera
cap = cv2.VideoCapture(0)


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


    # Process every detected face
    for (x, y, w, h) in faces:

        # Crop face
        face = gray[y:y+h, x:x+w]


        # Recognize face
        label, confidence = recognizer.predict(face)


        # Check confidence
        if confidence < 70:

            name = names.get(label, "Unknown")

            if name != "Unknown":

                # Mark attendance in PostgreSQL
                mark_attendance(label)

        else:

            name = "Unknown"


        # Draw rectangle around face
        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (255, 0, 0),
            2
        )


        # Display name
        cv2.putText(
            frame,
            name,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )


    # Display camera
    cv2.imshow("Attendance System - PostgreSQL", frame)


    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# Release camera
cap.release()
cv2.destroyAllWindows()
