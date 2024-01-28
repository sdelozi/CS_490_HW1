#!/bin/bash

# Check for both args
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <source_folder> <destination_folder>"
    exit 1
fi

source_folder="$1"
destination_folder="$2"

# Check if source folder exists
if [ ! -d "$source_folder" ]; then
    echo "Error: Source folder '$source_folder' not found."
    exit 1
fi

# Check if destination folder exists, create if not
if [ ! -d "$destination_folder" ]; then
    echo "Creating destination folder: $destination_folder"
    mkdir -p "$destination_folder"
fi

# Copy files from source to destination
cp -r "$source_folder"/* "$destination_folder"

echo "Files copied from '$source_folder' to '$destination_folder'."
