import os

from src.main.python.org.SortDirectory import extension_directory


def sort_directory(directory,target_directory):
    file_directory = extension_directory.extension_directory().get_directory()
    if os.path.isdir(target_directory):
        for current_file in os.listdir(target_directory):
            extension = os.path.splitext(current_file)[1][1:]
            new_location = (directory + f"\\{file_directory.get(extension)}\\") #Destination based on extension
            old_location = f"{target_directory}" + f"\\{current_file}"            #Grabs current File

            #Checks if Directory Exists
            if not os.path.isdir(new_location):
                os.mkdir(new_location)
                new_location += current_file
                os.rename(old_location, new_location)
            else:
                new_location += current_file
                os.rename(old_location, new_location)
            continue
    else:
        print(f"{target_directory} is not a valid directory" )
    return