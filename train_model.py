import os
import cv2
import face_recognition
import pickle

dataset_dir = 'faces'        # Folder where all images are saved
encoding_file = 'encodings.pickle'  # This file will store trained face data

known_encodings = []
known_names = []

# Loop through all folders (names) inside faces/
for person_name in os.listdir(dataset_dir):
    person_folder = os.path.join(dataset_dir, person_name)
    
    if not os.path.isdir(person_folder):
        continue

    # Loop through all images of this person
    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)
        
        # Load image with OpenCV
        image = cv2.imread(image_path)

        if image is None:
            print(f"⚠️ Could not load image: {image_name}")
            continue

        # Convert BGR (OpenCV default) → RGB (needed for face_recognition)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Get face encodings
        encodings = face_recognition.face_encodings(rgb)

        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(person_name)
            print(f"✅ Encoded: {person_name} ({image_name})")
        else:
            print(f"⚠️ No face found in: {image_name}")

# Save encodings to a file
print("\n✅ Training complete. Saving encodings...")
data = {"encodings": known_encodings, "names": known_names}

with open(encoding_file, "wb") as f:
    pickle.dump(data, f)

print(f"✅ Model saved as: {encoding_file}")
