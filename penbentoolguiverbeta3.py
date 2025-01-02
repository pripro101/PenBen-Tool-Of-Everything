import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import requests
import zipfile
import tarfile

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

# Functions for other menu options
def list_snap_apps():
    show_message("Snap Apps", "Listing available Snap apps...")

def list_flatpak_apps():
    show_message("Flatpak Apps", "Listing available Flatpak apps...")

def list_apt_apps():
    show_message("APT Apps", "Listing available APT apps...")

def install_apps():
    show_message("Install Apps", "You can install apps here.")

def install_games():
    show_message("Install Games", "You can install games here.")

def uninstall_games():
    show_message("Uninstall Games", "You can uninstall games here.")

# Main menu function with Tkinter buttons
def display_menu():
    def on_prhacktool_click():
        run_prhacktool()

    def on_alhck_click():
        alhck_menu()

    def on_snap_apps_click():
        list_snap_apps()

    def on_flatpak_apps_click():
        list_flatpak_apps()

    def on_apt_apps_click():
        list_apt_apps()

    def on_install_apps_click():
        install_apps()

    def on_install_games_click():
        install_games()

    def on_uninstall_games_click():
        uninstall_games()

    # Create the main window
    window = tk.Tk()
    window.title("PenBen Tool Of Everything")

    # Create buttons for each option
    button_prhacktool = tk.Button(window, text="Run PrHacktool", command=on_prhacktool_click)
    button_prhacktool.pack(pady=10)

    button_alhck = tk.Button(window, text="Open Alhck Menu", command=on_alhck_click)
    button_alhck.pack(pady=10)

    button_snap_apps = tk.Button(window, text="List Snap Apps", command=on_snap_apps_click)
    button_snap_apps.pack(pady=10)

    button_flatpak_apps = tk.Button(window, text="List Flatpak Apps", command=on_flatpak_apps_click)
    button_flatpak_apps.pack(pady=10)

    button_apt_apps = tk.Button(window, text="List APT Apps", command=on_apt_apps_click)
    button_apt_apps.pack(pady=10)

    button_install_apps = tk.Button(window, text="Install Apps", command=on_install_apps_click)
    button_install_apps.pack(pady=10)

    button_install_games = tk.Button(window, text="Install Games", command=on_install_games_click)
    button_install_games.pack(pady=10)

    button_uninstall_games = tk.Button(window, text="Uninstall Games", command=on_uninstall_games_click)
    button_uninstall_games.pack(pady=10)

    button_exit = tk.Button(window, text="Exit", command=window.quit)
    button_exit.pack(pady=10)

    window.mainloop()

# Main function to initialize and start the application
def main():
    install_dependencies()  # Install required dependencies
    display_menu()  # Show the GUI menu

if __name__ == "__main__":
    main()
