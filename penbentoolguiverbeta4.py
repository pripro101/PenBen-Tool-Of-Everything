import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

# Constants
GAMES_DIR = os.path.expanduser("~/pripropythonscripts/games")

# Ensure the games directory exists
if not os.path.exists(GAMES_DIR):
    os.makedirs(GAMES_DIR)

# Install missing dependencies function
def install_dependencies():
    required_modules = ['requests', 'pygame', 'psutil']
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

# Function to show message boxes
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

# Function to list Snap Apps
def list_snap_apps():
    show_message("Snap Apps", "Listing available Snap apps...")

# Function to list Flatpak Apps
def list_flatpak_apps():
    show_message("Flatpak Apps", "Listing available Flatpak apps...")

# Function to list APT Apps
def list_apt_apps():
    show_message("APT Apps", "Listing available APT apps...")

# Function to install apps
def install_apps():
    show_message("Install Apps", "You can install apps here.")

# Function to install games
def install_games():
    show_message("Install Games", "You can install games here.")

# Function to uninstall games
def uninstall_games():
    show_message("Uninstall Games", "You can uninstall games here.")

# Function to run the main menu GUI
def display_menu():
    # Create the main window
    window = tk.Tk()
    window.title("PenBen Tool Of Everything")

    # Define button actions
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

    # Create buttons for each menu item
    button_prhacktool = tk.Button(window, text="Run PrHacktool", command=on_prhacktool_click)
    button_prhacktool.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    button_alhck = tk.Button(window, text="Open Alhck Menu", command=on_alhck_click)
    button_alhck.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    button_snap_apps = tk.Button(window, text="List Snap Apps", command=on_snap_apps_click)
    button_snap_apps.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    button_flatpak_apps = tk.Button(window, text="List Flatpak Apps", command=on_flatpak_apps_click)
    button_flatpak_apps.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    button_apt_apps = tk.Button(window, text="List APT Apps", command=on_apt_apps_click)
    button_apt_apps.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    button_install_apps = tk.Button(window, text="Install Apps", command=on_install_apps_click)
    button_install_apps.grid(row=5, column=0, padx=10, pady=10, sticky="w")

    button_install_games = tk.Button(window, text="Install Games", command=on_install_games_click)
    button_install_games.grid(row=6, column=0, padx=10, pady=10, sticky="w")

    button_uninstall_games = tk.Button(window, text="Uninstall Games", command=on_uninstall_games_click)
    button_uninstall_games.grid(row=7, column=0, padx=10, pady=10, sticky="w")

    # Exit button
    button_exit = tk.Button(window, text="Exit", command=window.quit)
    button_exit.grid(row=8, column=0, padx=10, pady=10, sticky="w")

    window.mainloop()

# Main function to initialize and start the application
def main():
    install_dependencies()  # Install required dependencies
    display_menu()  # Show the GUI menu

if __name__ == "__main__":
    main()
