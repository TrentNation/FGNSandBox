import os
from src.FileOrganizer.SortDirectory import sort_directory

#Input each Directory separately
def partial_input():
    loop = 0
    file_path = ""
    while loop != "1":
        current_file_path = ""
        print("current_path: ", file_path)
        print("Input: ")
        user_input = input()
        index = user_input.rfind(r'"\"')
        if index != -1:
            user_input = user_input[0:index+1] #Good chance to cause an error due to max depth
        print(user_input)
        if check_if_valid(file_path + user_input):  #SHOULD work?
            file_path += f"{user_input}\\"
            print("Begin here?")
            print("\n1. Yes?\n2. No?")
            loop = input()
        else:
            print("Invalid option")
    return file_path

#Input the entire Directory at once
def full_input():
    loop = 0
    file_path = ""
    print("Please insert the desired directory")
    while loop != "1":
        print("Input: ")
        user_input = input()
        print(user_input)
        if check_if_valid(user_input):
            file_path = user_input
            print("Valid Directory: ", file_path)
            print("Begin here?")
            print("1. Yes?\n2. No?")
            print("Input: ")
            loop = input()
            match loop:
                case "1":
                    print(f"Will be using {file_path[:10]}... ")
                    return file_path
                case "2":
                    print("Input a New File Path")

        else:
            file_path = closest_valid_path(user_input)
            #print("Invalid option")
    return file_path

# Loops through directories and finds the last valid directory in the path
#Example: "C:User\Code\Python\Ascascasd" Should revert to "C:User\Code\Python"
def closest_valid_path(file_path):
    valid_path = ""
    directories_folder = file_path.split("\\")
    for directory in directories_folder:
        checking_path = valid_path + directory

        if check_if_valid(checking_path):
            valid_path += f"{directory}\\"
        else:
            if check_if_valid(valid_path):
                print(f"That sadly is not a valid path. The closest we could find is {valid_path}. Would you like to use this one?")
                print("1. Yes. \n2. No.")
                user_input = ""
                while user_input != "1" and user_input != "2":
                    user_input = input()
                    match user_input:
                        case "1":
                            return valid_path
                        case "2":
                            return 0
                        case _:
                            print("Invalid")
            else:
                print("Not a valid path")
    #Returns The Full-Inputted File Path
    return valid_path

#Checks if File is Valid
def check_if_valid(path):
    return os.path.exists(path)






#if __name__ == "__main__":

def input_interface():

    print("Which method would you like to input your path?")
    print("1. Partial Input?\n2. Full Input?\n")
    print("Input: ")
    user_input = ""

    target_directory = ""
    while user_input not in ("1", "2"):
        user_input = input()
        match user_input:
            case "1":
                target_directory = partial_input()
                break
            case "2":
                target_directory = full_input()
                break
            case _:
                print("Invalid")
                user_input = input()
    return target_directory