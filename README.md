import os
import subprocess
import sys
import time
import platform
import psutil
import requests
from pathlib import Path
import zipfile
import tarfile
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import webbrowser
import sched
import threading

# Constants
KEY_FILE_PATH = Path.home() / ".penben_drive_keys.json"
GAMES_DIR = Path.home() / "pripropythonscripts" / "games"
TOOLS_DIR = Path.home() / "pripro_tools"
HACKING_TOOL_REPO = "https://github.com/Z4nzu/hackingtool.git"
ALHACK_REPO = "https://github.com/4lbH4cker/ALHacking.git"

# Ensure the tools directory and games directory exist
TOOLS_DIR.mkdir(parents=True, exist_ok=True)
GAMES_DIR.mkdir(parents=True, exist_ok=True)

# Initialize scheduler for timed tasks
scheduler = sched.scheduler(time.time, time.sleep)

# Function to install dependencies
def install_dependencies():
    """Automatically installs missing Python dependencies and system tools."""
    required_modules = ['requests', 'pygame', 'psutil']
    for module in required_modules:
        try:
            __import__(module)
            print(f"Module '{module}' is already installed.")
        except ImportError:
            print(f"Module '{module}' is not installed. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

    # Update system apps and install missing system packages
    system_deps = ['curl', 'git', 'sudo', 'apt-transport-https']
    for dep in system_deps:
        try:
            subprocess.check_call(['sudo', 'apt', 'install', '-y', dep])
            print(f"System tool '{dep}' installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Error installing system package {dep}. You may need to install it manually.")
    
    # Update system packages
    print("Updating system packages...")
    subprocess.check_call(['sudo', 'apt', 'update'])
    subprocess.check_call(['sudo', 'apt', 'upgrade', '-y'])
    print("System updated successfully!")

# Function to print rainbow-colored text
def print_rainbow_text(text):
    """Prints text in rainbow colors."""
    colors = [
        "\033[91m",  # Red
        "\033[93m",  # Yellow
        "\033[92m",  # Green
        "\033[96m",  # Cyan
        "\033[94m",  # Blue
        "\033[95m"   # Magenta
    ]
    reset = "\033[0m"
    for i, char in enumerate(text):
        print(colors[i % len(colors)] + char, end="")
    print(reset)

# Display intro with loading
def display_intro():
    """Displays the rainbow intro text and initialization animation."""
    print_rainbow_text("Pripro Corp (PenBen)")
    print("\nInitializing...........")
    update_screen()  # Update the system and apps during initialization
    time.sleep(2)
    print("\nInitialization complete!")

def update_screen():
    """Update the system apps and overall system."""
    print("Updating system and apps...")
    
    # Perform system update
    try:
        subprocess.check_call(['sudo', 'apt', 'update'])
        subprocess.check_call(['sudo', 'apt', 'upgrade', '-y'])
        print("System apps updated successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error updating system: {e}")
    
    # Perform Python dependency update
    install_dependencies()
    
    # Perform additional cleanup or updates (e.g., removing unused packages)
    try:
        subprocess.check_call(['sudo', 'apt', 'autoremove', '-y'])
        print("Unused packages removed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error removing unused packages: {e}")
    
    print("Update process complete!")

# Clone repositories
def clone_repositories():
    """Clone the hackingtool and ALHacking repositories."""
    try:
        print(f"Cloning {HACKING_TOOL_REPO} into {TOOLS_DIR}...")
        subprocess.check_call(["git", "clone", HACKING_TOOL_REPO, str(TOOLS_DIR / "hackingtool")])

        print(f"Cloning {ALHACK_REPO} into {TOOLS_DIR}...")
        subprocess.check_call(["git", "clone", ALHACK_REPO, str(TOOLS_DIR / "ALHacking")])

        print("Repositories cloned successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repositories: {e}")

# Read a file
def read_file():
    """Reads content from a file."""
    file_path = input("Enter the file path: ")
    if Path(file_path).exists():
        with open(file_path, 'r') as file:
            print(f"File content:\n{file.read()}")
    else:
        print(f"File '{file_path}' does not exist.")

# Write to a file
def write_file():
    """Writes content to a file."""
    file_path = input("Enter the file path: ")
    content = input("Enter the content to write: ")
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Content written to {file_path}")

# Get public IP
def get_public_ip():
    """Fetches the public IP address."""
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip = response.json()['ip']
        print(f"Your public IP address is: {ip}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching public IP: {e}")

# Check internet connectivity
def check_internet_connectivity():
    """Checks if the internet is reachable."""
    try:
        response = requests.get('https://www.google.com', timeout=5)
        if response.status_code == 200:
            print("Internet is connected.")
        else:
            print("Internet is not connected.")
    except requests.exceptions.RequestException:
        print("No internet connection.")

# Get system info
def get_system_info():
    """Fetches and prints system information."""
    print(f"System Info:\nOS: {platform.system()} {platform.version()}\nPlatform: {platform.platform()}")
    print(f"Processor: {platform.processor()}")
    print(f"Memory: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
    print(f"Disk: {psutil.disk_usage('/').total / (1024 ** 3):.2f} GB")

# Manage drives
def manage_drives():
    """Displays available disk drives."""
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"Device: {partition.device}, Mountpoint: {partition.mountpoint}, Filesystem: {partition.fstype}")

# Manage apps
def manage_apps():
    """Lists installed applications."""
    if platform.system() == 'Linux':
        subprocess.run(['dpkg', '--get-selections'], check=True)
    elif platform.system() == 'Windows':
        subprocess.run(['wmic', 'product', 'get', 'name'], check=True)
    elif platform.system() == 'Darwin':
        subprocess.run(['brew', 'list'], check=True)

# Install apps
def install_apps():
    """Installs a new application (example: curl)."""
    app = input("Enter the name of the app to install: ")
    if platform.system() == 'Linux':
        subprocess.run(['sudo', 'apt', 'install', app], check=True)
    elif platform.system() == 'Windows':
        subprocess.run(['choco', 'install', app], check=True)
    elif platform.system() == 'Darwin':
        subprocess.run(['brew', 'install', app], check=True)

# Install games
def install_games():
    """Simulates installing a game."""
    game = input("Enter the name of the game to install: ")
    print(f"Installing {game}... (Simulated)")

# Uninstall games
def uninstall_games():
    """Simulates uninstalling a game."""
    game = input("Enter the name of the game to uninstall: ")
    print(f"Uninstalling {game}... (Simulated)")

# Send Rickroll
def send_rickroll():
    """Sends a Rickroll via email (mock)."""
    email = input("Enter the recipient's email: ")
    subject = "Rickroll!"
    body = "Never gonna give you up, never gonna let you down, never gonna run around and desert you!"
    print(f"Sending Rickroll to {email}... (Simulated)")

# Pranks
def pranks():
    """Simulate pranks."""
    print("Pranking... (Simulated)")

# Run ALHck menu
def run_alhck_menu():
    """Launches the ALHck menu using alhack.sh script."""
    alhack_script = TOOLS_DIR / "ALHacking" / "alhack.sh"
    
    if alhack_script.exists():
        try:
            # Try to run the script in a new terminal
            print("Running ALHck Menu in a new terminal...")
            subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"sudo bash {alhack_script}; exec bash"])
        except Exception as e:
            # Fallback to running the script in the current terminal if the new terminal fails
            print(f"Error running in a new terminal: {e}. Running in the current terminal...")
            subprocess.check_call(["sudo", "bash", str(alhack_script)])
    else:
        print("alhack.sh not found. Please install ALHck first.")

# Display ALHck menu
def display_alhck_menu():
    """ALHck Menu with options."""
    print("\nALHck Menu!")
    print("1. Run ALHck Menu (alhack.sh)")
    print("2. Go Back")
    choice = input("Enter your choice: ")
    return choice

# Display menu with all options
def display_menu():
    """Main menu with all options."""
    print("\nPenBen Tool Of Everything!")
    print("1. Read a file")
    print("2. Write to a file")
    print("3. Get Public IP")
    print("4. Check Internet Connectivity")
    print("5. Get System Info")
    print("6. Drive Management")
    print("7. Apps Management")
    print("8. Install Apps")
    print("9. Install Games")
    print("10. Pygame Tests")
    print("11. Uninstall Games")
    print("12. Send Rickroll")
    print("13. Pranks")
    print("14. Run PrHacktool")
    print("15. ALHck Menu")  # New option for ALHck Menu
    print("16. Setup Tools (Clone and Install)")
    print("17. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    """Main function to handle user inputs and execute functions."""
    display_intro()
    install_dependencies()  # Ensure all dependencies are installed and system is updated

    while True:
        choice = display_menu()

        if choice == "1":
            read_file()
        elif choice == "2":
            write_file()
        elif choice == "3":
            get_public_ip()
        elif choice == "4":
            check_internet_connectivity()
        elif choice == "5":
            get_system_info()
        elif choice == "6":
            manage_drives()
        elif choice == "7":
            manage_apps()
        elif choice == "8":
            install_apps()
        elif choice == "9":
            install_games()
        elif choice == "10":
            print("Running Pygame tests...")
        elif choice == "11":
            uninstall_games()
        elif choice == "12":
            send_rickroll()
        elif choice == "13":
            pranks()
        elif choice == "14":
            print("Running PrHacktool...")
        elif choice == "15":
            # ALHck menu
            while True:
                alhck_choice = display_alhck_menu()
                if alhck_choice == "1":
                    run_alhck_menu()
                elif alhck_choice == "2":
                    break  # Go back to the main menu
                else:
                    print("Invalid choice! Please try again.")
        elif choice == "16":
            clone_repositories()
        elif choice == "17":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
