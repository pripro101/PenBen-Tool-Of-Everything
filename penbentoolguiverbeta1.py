import os
import subprocess
import sys
import time
import platform
import psutil
import json
from pathlib import Path
import requests
import zipfile
import tarfile
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import webbrowser
import sched
import threading
import tkinter as tk
from tkinter import messagebox

# Constants
KEY_FILE_PATH = Path.home() / ".penben_drive_keys.json"
GAMES_DIR = Path.home() / "pripropythonscripts" / "games"
GITHUB_API_URL = "https://api.github.com/repos"
ITCH_IO_URL = "https://itch.io/api/1/your_api_key_here"
GAME_JOLT_URL = "https://api.gamejolt.com/v1/games"

# Ensure the games directory exists
GAMES_DIR.mkdir(parents=True, exist_ok=True)

# Initialize scheduler for timed tasks
scheduler = sched.scheduler(time.time, time.sleep)

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

    # Ensure system tools are installed
    system_deps = ['sudo', 'curl', 'git']
    for dep in system_deps:
        try:
            subprocess.check_call(['sudo', 'apt', 'install', '-y', dep])
            print(f"System package {dep} installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Error installing system package {dep}. You may need to install it manually.")

def show_message(message, title="Message"):
    """Display a message box with the given message."""
    messagebox.showinfo(title, message)

def on_install_dependencies():
    """Callback for the install dependencies button."""
    install_dependencies()
    show_message("Dependencies installed successfully!")

def on_run_prhacktool():
    """Callback to run PrHacktool."""
    try:
        subprocess.check_call(["python3", "/home/pripro/hackingtool/hackingtool.py"])
        show_message("PrHacktool executed successfully!")
    except subprocess.CalledProcessError as e:
        show_message(f"Error running PrHacktool: {str(e)}", title="Error")

def on_download_game():
    """Callback for downloading a game."""
    game_url = game_url_entry.get()
    game_name = game_name_entry.get()
    download_game(game_url, game_name)
    show_message(f"Game {game_name} downloaded successfully!")

def download_game(game_url, game_name):
    """Download game files, extract them, and delete the archive after extraction."""
    game_dir = GAMES_DIR / game_name
    game_dir.mkdir(parents=True, exist_ok=True)

    print(f"Downloading {game_name} to {game_dir}...")
    try:
        if game_url.endswith(".zip"):
            game_file = game_dir / f"{game_name}.zip"
            with requests.get(game_url, stream=True) as r:
                with open(game_file, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            with zipfile.ZipFile(game_file, 'r') as zip_ref:
                zip_ref.extractall(game_dir)
            os.remove(game_file)

        elif game_url.endswith(".tar.gz"):
            game_file = game_dir / f"{game_name}.tar.gz"
            with requests.get(game_url, stream=True) as r:
                with open(game_file, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            with tarfile.open(game_file, 'r:gz') as tar_ref:
                tar_ref.extractall(game_dir)
            os.remove(game_file)

        elif game_url.endswith(".tar"):
            game_file = game_dir / f"{game_name}.tar"
            with requests.get(game_url, stream=True) as r:
                with open(game_file, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            with tarfile.open(game_file, 'r') as tar_ref:
                tar_ref.extractall(game_dir)
            os.remove(game_file)

        else:
            print("Unsupported download format! Please provide a valid .zip, .tar.gz, or .tar URL.")
            return

    except Exception as e:
        print(f"Error downloading and extracting game: {e}")
        show_message(f"Error downloading the game: {e}", title="Error")

# GUI Setup
root = tk.Tk()
root.title("PenBen Tool Of Everything")

# Install Dependencies Button
install_button = tk.Button(root, text="Install Dependencies", command=on_install_dependencies)
install_button.pack(pady=10)

# PrHacktool Button
prhacktool_button = tk.Button(root, text="Run PrHacktool", command=on_run_prhacktool)
prhacktool_button.pack(pady=10)

# Game Download Section
game_url_label = tk.Label(root, text="Enter Game URL:")
game_url_label.pack(pady=5)
game_url_entry = tk.Entry(root)
game_url_entry.pack(pady=5)

game_name_label = tk.Label(root, text="Enter Game Name:")
game_name_label.pack(pady=5)
game_name_entry = tk.Entry(root)
game_name_entry.pack(pady=5)

download_button = tk.Button(root, text="Download Game", command=on_download_game)
download_button.pack(pady=10)

# Mainloop
root.mainloop()
