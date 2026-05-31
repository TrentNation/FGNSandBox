from src.FileOrganizer.LinkDirectory import link_directories
from pathlib import Path
import os

def check_relationship_of(directory):
    #Checks for children
    num_of_children = len(os.listdir(directory))
    print("Number of Folders: ", num_of_children)
    directory_path = Path(os.path.abspath(directory))
    if directory_path.is_symlink() and directory_path.is_dir():
        print("This directory contains a symbolic link with another")
    if directory_path.is_symlink() and directory_path.is_file():
        print("This file contains a symbolic link")

def recursive_checking_files(directory):
    num_of_files = 0
    print(f"list of {directory}'s directs: ", len(os.listdir(directory)))
    if os.path.isdir(directory):
        for file in os.listdir(directory):
            if os.path.isdir(file):
                num_of_files+=recursive_checking_files(file)
            else:
                num_of_files+=1
    return num_of_files


if __name__ == "__main__":
    placeholder = ""
    while placeholder != 4:
        print("Insert the Directory you want as primary:")
        primary_directory = input()
        print("Insert the Directory you want as secondary")
        secondary_directory = input()

