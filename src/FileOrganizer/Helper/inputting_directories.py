import os

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
            current_filepath += user_input
            print("Begin here?")
            print("\n1. Yes?\n2. No?")
            loop = input()
        else:
            print("Invalid option")
    return filepath

def closest_valid_path(filepath):
    return # Loops through directories and finds the last valid directory in the path
    #Example: "C:User\Code\Python\Ascascasd" Should revert to "C:User\Code\Python"
def check_if_valid(path):
    return os.path.exists(path)