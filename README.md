# Simulate F1 Key Press

This Python script simulates pressing the "F1" key every 5 seconds for a specific Windows program, even if the program is minimized. The script can run in the background and includes functionality to stop the simulation using the "esc" key.

## Features

- Simulates pressing the "F1" key to a specified Windows program.
- Works even if the program is minimized.
- Runs in the background.
- Stops the simulation when the "esc" key is pressed.
- Automatically requests elevated privileges to ensure the script can interact with programs running with higher privileges.

## Requirements

- Python 3.x
- `pyautogui` library
- `keyboard` library
- `pywin32` library

## Installation

1. Install the required Python libraries:
   ```bash
   pip install pyautogui keyboard pywin32

author: ammar naji

email: aynaji@outlook.com