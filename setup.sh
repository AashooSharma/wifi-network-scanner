#!/bin/bash

# Update and upgrade Termux packages
echo "Updating and upgrading Termux packages..."
pkg update && pkg upgrade -y

# Install Python
echo "Installing Python..."
pkg install python -y

# Install Nmap
echo "Installing Nmap..."
pkg install nmap -y

# Install net-tools
echo "Installing net-tools..."
pkg install net-tools -y

# Check if requirements.txt exists and install Python packages
if [ -f requirements.txt ]; then
    echo "Installing Python packages from requirements.txt..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping Python package installation."
fi

echo "Setup completed successfully!"
