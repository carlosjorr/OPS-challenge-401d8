#!/usr/bin/env python3

import os
import subprocess

def encrypt_folder(folder_path):
    # Encrypt the folder
    subprocess.run(['manage-bde', '-on', folder_path])

def decrypt_folder(folder_path):
    # Decrypt the folder
    subprocess.run(['manage-bde', '-off', folder_path])

# Begin recursive directory crawl
for root, dirs, files in os.walk(".", topdown=False):
    # For each hit, concatenate the current directory pathing to the left of the result
    for file in files:
        file_path = os.path.join(root, file)
        # Encrypt the file
        encrypt_folder(file_path)
        print(f'File encrypted: {file_path}')
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        # Encrypt the directory
        encrypt_folder(dir_path)
        print(f'Directory encrypted: {dir_path}')
