import os
import subprocess
import sys
import time
import tkinter as tk
from tkinter import messagebox
import requests
import zipfile
import tarfile
from pathlib import Path

# Constants
GAMES_DIR = Path.home() / "pripropythonscripts" / "games"

# Ensure the games directory exists
GAMES_DIR.mkdir(parents=True, exist_ok=True)

# Install missing dependencies function
def install_dependencies():
    required_modules = ['requests', 'pygame', 'psutil']
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

# Function for displaying a message box
def show_message(title, message):
    messagebox.showinfo(title, message)

# Function to run PrHacktool
def run_prhacktool():
    try:
        subprocess.check_call(["python3", "/home/pripro/hackingtool/hackingtool.py"])
        show_message("Success", "PrHacktool executed successfully!")
    except subprocess.CalledProcessError as e:
        show_message("Error", f"Error running PrHacktool: {str(e)}")

# Function for Alhck Menu
def alhck_menu():
    show_message("Alhck Menu", "Launching Alhck menu...")

# Function for displaying menu
def display_menu():
    def on_prhacktool_click():
        run_prhacktool()

    def on_alhck_click():
        alhck_menu()

    window = tk.Tk()
    window.title("PenBen Tool Of Everything")

    # Create and pack buttons
    button_prhacktool = tk.Button(window, text="Run PrHacktool", command=on_prhacktool_click)
    button_prhacktool.pack(pady=10)

    button_alhck = tk.Button(window, text="Open Alhck Menu", command=on_alhck_click)
    button_alhck.pack(pady=10)

    # Add more buttons as needed
    button_exit = tk.Button(window, text="Exit", command=window.quit)
    button_exit.pack(pady=10)

    window.mainloop()

# Main function to initialize and start the application
def main():
    install_dependencies()  # Install required dependencies
    display_menu()  # Show the GUI menu

if __name__ == "__main__":
    main()
