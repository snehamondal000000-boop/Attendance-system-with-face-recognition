import tkinter as tk
from tkinter import messagebox
import subprocess

# FULL PATH to your project folder
PROJECT_PATH = r"C:/Users/SNEHA MONDAL/OneDrive/Desktop/FaceAttendance/"

# ---- Button Functions ----
def capture_faces():
    try:
        subprocess.run(["python", PROJECT_PATH + "capture_faces.py"])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def train_model():
    try:
        subprocess.run(["python", PROJECT_PATH + "train_model.py"])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def recognize_faces():
    try:
        subprocess.run(["python", PROJECT_PATH + "recognize.py"])
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---- GUI Window ----
root = tk.Tk()
root.title("Face Attendance System")
root.geometry("450x350")
root.configure(bg="#1e1e1e")  # Dark theme background

# Title
title = tk.Label(
    root,
    text="Face Attendance System",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title.pack(pady=20)

# BUTTON STYLE
BTN_BG = "#0078D4"   # Windows blue
BTN_FG = "white"

def create_button(text, command):
    return tk.Button(
        root,
        text=text,
        font=("Arial", 14, "bold"),
        bg=BTN_BG,
        fg=BTN_FG,
        activebackground="#005fa3",
        activeforeground="white",
        width=20,
        height=1,
        relief="flat",
        command=command
    )

btn1 = create_button("📸  Capture Faces", capture_faces)
btn1.pack(pady=10)

btn2 = create_button("🧠  Train Model", train_model)
btn2.pack(pady=10)

btn3 = create_button("👁️  Recognize Faces", recognize_faces)
btn3.pack(pady=10)

root.mainloop()
