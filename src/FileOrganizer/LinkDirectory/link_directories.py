#Import os Library
import os
import subprocess


# Source file path
# source_directory : The primary directory to serve as base
# target_directory : The directory we want to link with the base (Secondary)
def create_symbolic(source_directory, target_directory):
    os.link(source_directory, target_directory)
    return

#Creates A Junction Link folder connected to the source Directory
#source_directory : The primary directory to serve as base
#target_directory : The Location of where the new Junction folder will be located
def create_junction(source_directory, target_directory):
    cmd = f'mklink /j "{target_directory + f"\\junction_folder\\"}" "{source_directory}"'
    print("command: ", cmd)
    result = subprocess.run(cmd,shell=True,capture_output=True,text=True) #This is REALLY dangerous and exposes the system


    if result.returncode != 0:
        raise OSError("Failed to create Junction: ", result.stderr.strip())
    else:
        print(f"{target_directory[-10:]}'sJunction Folder Created at: {source_directory[-10:]} ")


