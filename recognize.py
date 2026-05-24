import face_recognition
import cv2
import numpy as np
import pickle
from datetime import datetime

# Load trained encodings
with open("encodings.pickle", "rb") as file:
    data = pickle.load(file)

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Keep track of recognized names to avoid duplicate attendance
recognized_names = []

def mark_attendance(name):
    with open("attendance.csv", "a") as f:
        now = datetime.now()
        time_string = now.strftime("%H:%M:%S")
        date_string = now.strftime("%Y-%m-%d")
        f.write(f"{name},{date_string},{time_string}\n")

print("⏳ Starting face recognition. Press 'q' to quit.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("❌ Failed to grab frame from webcam.")
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(data["encodings"], face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(data["encodings"], face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = data["names"][best_match_index]

            if name not in recognized_names:
                recognized_names.append(name)
                mark_attendance(name)
                print(f"✅ Attendance marked for {name}")

        # Draw rectangle and label
        top, right, bottom, left = face_location
        top *= 4; right *= 4; bottom *= 4; left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
print("🛑 Face recognition stopped.")
