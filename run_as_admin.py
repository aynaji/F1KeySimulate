"""
run_as_admin.py

This script requests elevated privileges and runs the simulate_f1.py script to simulate pressing the "F1" key every 5 seconds
for a specific Windows program, even if the program is minimized.

Author: AMMAR NAJI
Date: 2024-11-24
"""

import ctypes
import sys
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    import simulate_f1
else:
    # Re-run the script with admin privileges
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, os.path.abspath(__file__), None, 1
    )
