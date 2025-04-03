"""
Button Coordinate Recorder for Gmail Spam Blocking
This module helps record screen coordinates for buttons needed to block spam in Gmail.
It guides the user through positioning their cursor over specific buttons and records
their coordinates, which can later be used for automation scripts.
The recorded buttons include:
- menu: The menu button for spam emails
- block: The option to block the sender
- block_confirm: The confirmation button for blocking
- next: The button to move to the next email
All coordinates are saved to a JSON file in the assets directory for later use
by automation scripts.
Dependencies:
- pyautogui: For detecting cursor position
- tkinter: For creating guidance dialogs
Usage:
    python block_by_coords.py
The script will guide you through the process of recording each button position.
Simply follow the on-screen instructions, positioning your cursor and pressing Enter
for each button when prompted.

"""

import json
import os
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import pyautogui


def record_button_position(button_name):
    """
    Guide the user to position their cursor over a button and record coordinates.
    """
    # Create a simple Tkinter window for the instruction
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Create a small dialog window
    dialog = tk.Toplevel(root)
    dialog.title(f"Record '{button_name}' Position")
    dialog.geometry("300x100")
    dialog.lift()  # Bring window to front
    dialog.focus_force()  # Force focus
    
    label = ttk.Label(dialog, text=f"Position your cursor over the '{button_name}' button\nthen press Enter to record.")
    label.pack(pady=20)
    
    # Array to store coordinates
    pos = [0, 0]
    
    # Function to record position and close dialog
    def record_position(event=None):
        pos[0], pos[1] = pyautogui.position()
        dialog.destroy()
    
    # Bind Enter key to record_position function
    dialog.bind("<Return>", record_position)
    
    # Wait for dialog to close
    root.wait_window(dialog)
    
    return pos

def main():
    """
    Record the coordinates of four buttons and save them to a JSON file.
    """
    # Buttons to record
    button_names = ["menu", "block", "block_confirm", "next"]
    
    # Dictionary to store coordinates
    coords = {}
    
    # Greeting message
    print("Welcome to the button coordinate recorder!")
    print("You will be guided to record the position of each button.")
    
    # Record coordinates for each button
    for button_name in button_names:
        # Wait 4 seconds before recording each button to allow user to prepare
        time.sleep(4)
        coords[button_name] = record_button_position(button_name)
        print(f"Recorded '{button_name}' button at coordinates: {coords[button_name]}")
    
    # Ensure the assets directory exists
    assets_dir = "assets"
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
    
    # Save coordinates to JSON file
    coords_file = os.path.join(assets_dir, "coords.json")
    with open(coords_file, "w") as f:
        json.dump(coords, f, indent=4)
    
    print(f"\nAll coordinates saved to {coords_file}")
    print("Recorded button coordinates:")
    for button_name, coordinates in coords.items():
        print(f"- {button_name}: {coordinates}")

if __name__ == "__main__":
    main()