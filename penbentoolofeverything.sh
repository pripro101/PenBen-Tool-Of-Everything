#!/bin/bash

# PenBen Tool - Shell Script Version

# Update system and install dependencies
echo "Updating system and installing dependencies..."
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip curl git sudo apt-transport-https python3-requests python3-psutil python3-pygame

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install requests pygame psutil

# Function to read a file
read_file() {
    echo "Enter the file path to read:"
    read file_path
    if [ -f "$file_path" ]; then
        cat "$file_path"
    else
        echo "File not found."
    fi
}

# Function to write to a file
write_file() {
    echo "Enter the file path to write to:"
    read file_path
    echo "Enter the content to write:"
    read content
    echo "$content" > "$file_path"
    echo "Content written to $file_path"
}

# Function to get public IP
get_public_ip() {
    echo "Fetching public IP..."
    curl -s https://api.ipify.org?format=json | jq -r '.ip'
}

# Function to check internet connectivity
check_internet_connectivity() {
    echo "Checking internet connectivity..."
    if curl -s --head http://www.google.com | grep "200 OK" > /dev/null; then
        echo "Internet is connected."
    else
        echo "No internet connection."
    fi
}

# Function to get system info
get_system_info() {
    echo "System Info:"
    uname -a
    free -h
    df -h
    lscpu
}

# Function to manage drives
manage_drives() {
    echo "Displaying available drives..."
    lsblk
}

# Function to manage apps
manage_apps() {
    echo "Listing installed applications..."
    dpkg --get-selections
}

# Function to install apps
install_apps() {
    echo "Enter the app name to install:"
    read app
    sudo apt install -y "$app"
}

# Function to install games
install_games() {
    echo "Simulating game installation..."
    echo "Enter the game name:"
    read game
    echo "Installing $game... (Simulated)"
}

# Function to uninstall games
uninstall_games() {
    echo "Enter the game name to uninstall:"
    read game
    echo "Uninstalling $game... (Simulated)"
}

# Function to send Rickroll
send_rickroll() {
    echo "Enter the recipient's email:"
    read email
    echo "Sending Rickroll to $email... (Simulated)"
}

# Function to perform pranks
pranks() {
    echo "Pranking... (Simulated)"
}

# Function to clone repositories (ALHacking and HackingTool)
clone_repositories() {
    echo "Cloning repositories..."
    git clone https://github.com/4lbH4cker/ALHacking.git ~/pripro_tools/ALHacking
    git clone https://github.com/Z4nzu/hackingtool.git ~/pripro_tools/hackingtool
}

# Function to run ALHack menu
run_alhck_menu() {
    echo "Running ALHack menu..."
    bash ~/pripro_tools/ALHacking/alhack.sh
}

# Function to display the main menu
display_menu() {
    echo "PenBen Tool of Everything!"
    echo "1. Read a file"
    echo "2. Write to a file"
    echo "3. Get Public IP"
    echo "4. Check Internet Connectivity"
    echo "5. Get System Info"
    echo "6. Drive Management"
    echo "7. Apps Management"
    echo "8. Install Apps"
    echo "9. Install Games"
    echo "10. Uninstall Games"
    echo "11. Send Rickroll"
    echo "12. Pranks"
    echo "13. Clone Repositories"
    echo "14. Run ALHack Menu"
    echo "15. Exit"
    echo "Enter your choice:"
    read choice
}

# Main loop
while true; do
    display_menu
    case $choice in
        1)
            read_file
            ;;
        2)
            write_file
            ;;
        3)
            get_public_ip
            ;;
        4)
            check_internet_connectivity
            ;;
        5)
            get_system_info
            ;;
        6)
            manage_drives
            ;;
        7)
            manage_apps
            ;;
        8)
            install_apps
            ;;
        9)
            install_games
            ;;
        10)
            uninstall_games
            ;;
        11)
            send_rickroll
            ;;
        12)
            pranks
            ;;
        13)
            clone_repositories
            ;;
        14)
            run_alhck_menu
            ;;
        15)
            echo "Exiting..."
            break
            ;;
        *)
            echo "Invalid option. Try again."
            ;;
    esac
done

