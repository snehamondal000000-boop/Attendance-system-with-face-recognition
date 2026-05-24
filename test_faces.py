import face_recognition
import os

# Path to your test images folder
path = r"C:\Users\Sneha - Personal\Desktop\FaceAttendance\test face"

# Step 1: Load known images and create encodings
known_encodings = []
known_names = []

for file in os.listdir(path):
    if file.endswith(".jpg") or file.endswith(".png"):  # only images
        img_path = os.path.join(path, file)
        img = face_recognition.load_image_file(img_path)
        
        # Find face encodings (face landmarks as numbers)
        encodings = face_recognition.face_encodings(img)
        if len(encodings) > 0:
            encoding = encodings[0]
            known_encodings.append(encoding)
            name = os.path.splitext(file)[0]  # take filename as name
            known_names.append(name)

print("✅ Encoded faces:", known_names)

# Step 2: Test with one known image (Sneha Mondal.jpg)
test_image = face_recognition.load_image_file(os.path.join(path, "Sneha Mondal.jpg"))
test_encoding = face_recognition.face_encodings(test_image)[0]

# Step 3: Compare test image with all known faces
results = face_recognition.compare_faces(known_encodings, test_encoding)

for i, match in enumerate(results):
    if match:
        print(f"✅ Match found: {known_names[i]}")
    else:
        print(f"❌ No match with {known_names[i]}")
