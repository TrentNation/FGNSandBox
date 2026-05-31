from src.FileOrganizer.Helper import inputting_directories
from src.FileOrganizer.LinkDirectory import link_directories
from pathlib import Path
import os

def check_relationship_of(directory):
    #Checks for children
    num_of_children = len(os.listdir(directory))
    print("Number of Folders: ", num_of_children)
    directory_path = Path(directory).resolve()
    if (directory_path.is_symlink()):
        if directory_path.is_dir():
            print("This directory contains a symbolic link with another")
        else:
            print("This file contains a symbolic link")
    else:
        print("There is no symbolic link.")

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
        inputdir = inputting_directories
        print("Insert the Directory you want as primary:")
        primary_directory = inputdir.input_interface()
        check_relationship_of(primary_directory)
        print("Insert the Directory you want as secondary")
        secondary_directory = inputdir.input_interface()
        check_relationship_of(secondary_directory)

