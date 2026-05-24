import os
from src.FileOrganizer.SortDirectory import directory_sorter
if __name__ == "__main__":

    print("Input a directory to check: \n")
    target_directory = input()
    target_directory = os.getcwd() + f"\\{target_directory}"
    directory_sorter.sort_directory(os.getcwd(), target_directory)

def partial_input():
    current_filepath = ""
    print("current_path: ", current_filepath)
    print("Input: ")
    user_input = input()


def full_input():
    current_filepath = ""
def check_if_valid(path):
    return os.path.exists(path)