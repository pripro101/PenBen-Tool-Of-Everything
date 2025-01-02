import subprocess
import sys
import time
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import os

# Constants
KEY_FILE_PATH = Path.home() / ".penben_drive_keys.json"
GAMES_DIR = Path.home() / "pripropythonscripts" / "games"
GITHUB_API_URL = "https://api.github.com/repos"
ITCH_IO_URL = "https://itch.io/api/1/your_api_key_here"
GAME_JOLT_URL = "https://api.gamejolt.com/v1/games"

# Ensure the games directory exists
GAMES_DIR.mkdir(parents=True, exist_ok=True)

def install_dependencies():
    """Automatically installs missing dependencies."""
    required_modules = ['requests', 'pygame', 'psutil']
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"Module '{module}' is already installed.")
        except ImportError:
            print(f"Module '{module}' is not installed. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

def run_alha_script():
    """Runs the alha.sh script in a separate terminal"""
    try:
        subprocess.Popen(["gnome-terminal", "--", "bash", "-c", "sudo bash /home/pripro/pripropythonscripts/alha/alha.sh; exec bash"])
        messagebox.showinfo("Success", "alha.sh script has been launched!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error running alha.sh: {str(e)}")

def run_prhacktool():
    """Runs the PrHacktool script or command."""
    try:
        subprocess.check_call(["python3", "/home/pripro/hackingtool/hackingtool.py"])
        messagebox.showinfo("Success", "PrHacktool executed successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error running PrHacktool: {str(e)}")

def install_game():
    """Download and install a game"""
    # Example installation process
    messagebox.showinfo("Install Game", "This will install a game (Feature under construction).")

def uninstall_game():
    """Uninstall a game"""
    # Example uninstallation process
    messagebox.showinfo("Uninstall Game", "This will uninstall a game (Feature under construction).")

def display_menu():
    """Displays the menu with all tool options"""
    print("\nPenBen Tool Of Everything!")
    print("1. Run alha.sh")
    print("2. Run PrHacktool")
    print("3. Install Game")
    print("4. Uninstall Game")
    print("5. Exit")

# Tkinter Window Setup
root = tk.Tk()
root.title("Pripro App")
root.geometry("300x350")  # Window size

# Button to run alha.sh script
alha_button = tk.Button(root, text="Run alha.sh Script", command=run_alha_script, height=2, width=20)
alha_button.pack(pady=10)

# Button to run PrHacktool
prhacktool_button = tk.Button(root, text="Run PrHacktool", command=run_prhacktool, height=2, width=20)
prhacktool_button.pack(pady=10)

# Button to install a game
install_game_button = tk.Button(root, text="Install Game", command=install_game, height=2, width=20)
install_game_button.pack(pady=10)

# Button to uninstall a game
uninstall_game_button = tk.Button(root, text="Uninstall Game", command=uninstall_game, height=2, width=20)
uninstall_game_button.pack(pady=10)

# Button to exit the application
exit_button = tk.Button(root, text="Exit", command=root.quit, height=2, width=20)
exit_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
