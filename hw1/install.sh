#!/bin/bash

# Update the system
sudo apt update
sudo apt upgrade -y

# Install htop and screen
sudo apt install htop -y
sudo apt install screen -y

# Install Miniconda
MINICONDA_PATH="$HOME/miniconda3"
mkdir -p "$MINICONDA_PATH"
wget "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh" -O "$MINICONDA_PATH/miniconda.sh"
bash "$MINICONDA_PATH/miniconda.sh" -b -u -p "$MINICONDA_PATH"
rm -rf "$MINICONDA_PATH/miniconda.sh"

# Check if conda executable exists
if [ -x "$MINICONDA_PATH/bin/conda" ]; then
    # Run conda init
    "$MINICONDA_PATH/bin/conda" init bash
    echo "Miniconda installation completed and initialized."
else
    echo "Error: Conda executable not found. Miniconda installation may have failed."
fi

echo "Installation completed: htop, screen, and Miniconda"
