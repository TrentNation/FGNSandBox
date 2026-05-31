import os
from src.FileOrganizer.SortDirectory import sort_directory

#Input each Directory separately
def partial_input():
    loop = 0
    filepath = ""
    while loop != 2:
        current_filepath = ""
        print("current_path: ", current_filepath)
        print("Input: ")
        user_input = input()
        index = user_input.find(r'"\"')
        if index != -1:
            user_input = user_input[0:index+1] #Good chance to cause an error due to max depth
        print(user_input)
        if check_if_valid(user_input):
            current_filepath += user_input
            print("Begin here?")
            print("\n1. Yes?\n2. No?")
            loop = input()
        else:
            print("Invalid option")
    return filepath




#Input the entire Directory at once
def full_input():
    current_filepath = ""
    loop = 0
    filepath = ""
    while loop != 2:
        current_filepath = ""
        print("Input: ")
        user_input = input()
        print(user_input)
        if check_if_valid(user_input):
            current_filepath = user_input
            print("Begin here?")
            print("\n1. Yes?\n2. No?")
            loop = input()
        else:
            closest_valid_path(user_input)
            print("Invalid option")
    return filepath

# Loops through directories and finds the last valid directory in the path
#Example: "C:User\Code\Python\Ascascasd" Should revert to "C:User\Code\Python"
def closest_valid_path(filepath):
    valid_path = ""
    filepath.split("\\")
    for directory in filepath:
        checking_path = valid_path + directory
        if check_if_valid(checking_path):
            valid_path += f"{checking_path}\\"
        else:
            print(f"That sadly is not a valid path. The closest we could find is{valid_path}. Would you like to use this one?")
            print("1. Yes. \n 2. No")
            user_input = ""
            while user_input != "1" and user_input != 2:
                user_input = input()
                match user_input:
                    case 1:
                        return valid_path
                    case 2:
                        return 0
                    case _:
                        print("Invalid")


    return valid_path
#Checks if File is Valid
def check_if_valid(path):
    return os.path.exists(path)




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
                target_directory = partial_input()
            case "2":
                target_directory = full_input()
            case _:
                print("Invalid")
    target_directory = os.getcwd() + f"\\{target_directory}"
    sort_directory.sort_directory(os.getcwd(), target_directory)
