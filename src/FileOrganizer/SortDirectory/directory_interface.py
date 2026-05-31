import os
from src.FileOrganizer.SortDirectory import sort_directory
from src.FileOrganizer.Helper import inputting_directories

if __name__ == "__main__":

    print("Input a directory to check: \n")
    print("Which method would you like to pick?")
    print("1. Partial Input?\n2. Full Input?\n")
    print("Input: ")
    user_input = input()

    target_directory = ""
    while user_input != 1 or user_input != 2:
        match user_input:
            case "1":
                target_directory = inputting_directories.partial_input()
            case "2":
                target_directory = inputting_directories.full_input()
            case _:
                print("Invalid")
    target_directory = os.getcwd() + f"\\{target_directory}"
    sort_directory.sort_directory(os.getcwd(), target_directory)
