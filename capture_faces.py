import cv2
import os

def capture_images(name):
    cam = cv2.VideoCapture(0)
    count = 0
    folder = f"faces/{name}"
    os.makedirs(folder, exist_ok=True)

    print("Press 's' to save image, 'q' to quit")
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        cv2.imshow("Capture Faces", frame)

        key = cv2.waitKey(1)
        if key == ord('s'):
            img_path = f"{folder}/{count}.jpg"
            cv2.imwrite(img_path, frame)
            print(f"Saved: {img_path}")
            count += 1
        elif key == ord('q') or count >= 20:
            break

    cam.release()
    cv2.destroyAllWindows()

# Ask for student name
name = input("Enter Student Name: ")
capture_images(name)
