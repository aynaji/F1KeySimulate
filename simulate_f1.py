"""
simulate_f1.py

This script simulates pressing the "F1" key every 5 seconds for a specific Windows program, even if the program is minimized.
The script can run in the background and includes functionality to stop the simulation using the "esc" key.

Author: AMMAR NAJI
Date: 2024-11-24
"""

import time
import keyboard
import win32api
import win32con
import win32gui

# Replace with the title of your specific program window
window_title = "Your Program Window Title"

def send_f1_to_window(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F1, 0)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_F1, 0)

def simulate_f1_to_minimized_window(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    if not hwnd:
        print(f"Window with title '{window_title}' not found.")
        return

    while not keyboard.is_pressed('esc'):
        send_f1_to_window(hwnd)
        time.sleep(5)

print("Starting script...")
print("Press 'esc' to stop the script.")

simulate_f1_to_minimized_window(window_title)
