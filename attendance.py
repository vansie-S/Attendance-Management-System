print("PROGRAM STARTED")
import os
import cv2
import csv
from datetime import datetime
os.environ["OPENCV_OPENCL_RUNTIME"] = "disabled"


# -----------------------------
# STUDENT INFORMATION
# -----------------------------

names = {
    1: "Student 1",
    2: "Student 2"
}

# -----------------------------
# LOAD FACE RECOGNIZER
# -----------------------------

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")

# -----------------------------
# LOAD FACE DETECTOR
# -----------------------------

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# -----------------------------
# CSV FILE
# -----------------------------

csv_file = "attendance.csv"

# Create CSV if it doesn't exist
if not os.path.exists(csv_file):

    with open(csv_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Student_ID",
            "Name",
            "Date",
            "Time",
            "Status"
        ])

# -----------------------------
# ATTENDANCE FUNCTION
# -----------------------------
def mark_attendance(student_id, name):
    today = datetime.now().strftime("%Y-%m-%d")

    # Read existing attendance
    with open(csv_file, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if (row["Student_ID"].strip() == str(student_id)
                    and row["Date"].strip() == today):
                return False

    # Add attendance only if not already present
    current_time = datetime.now().strftime("%H:%M:%S")

    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            student_id,
            name,
            today,
            current_time,
            "Present"
        ])

    print(name, "marked PRESENT")
    return True
# -----------------------------
# OPEN CAMERA
# -----------------------------

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera not detected")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    # -----------------------------
    # RECOGNIZE EACH FACE
    # -----------------------------

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]

        label, confidence = recognizer.predict(face)

        # Accept only good matches
        if confidence < 70:

            name = names.get(
                label,
                "Unknown"
            )

            # Mark attendance
            mark_attendance(
                label,
                name
            )

        else:

            name = "Unknown"

        # Draw rectangle
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

    # Show camera
    cv2.imshow(
        "Attendance System",
        frame
    )

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release camera
cap.release()

cv2.destroyAllWindows()