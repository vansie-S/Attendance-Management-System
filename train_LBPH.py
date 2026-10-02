import cv2
import os
import numpy as np

# Create LBPH recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []

# Student folders and their labels
students = {
    "student_1": 1,
    "student_3": 2
}

# Read images from each student folder
for student, label in students.items():

    folder = f"dataset/{student}"

    for filename in os.listdir(folder):

        image_path = os.path.join(folder, filename)

        # Read image in grayscale
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is not None:
            faces.append(image)
            labels.append(label)

# Convert labels to NumPy array
labels = np.array(labels)

# Train model
recognizer.train(faces, labels)

# Save model
recognizer.save("face_model.yml")

print("Training completed!")
print("Total images:", len(faces))