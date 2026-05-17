import os

from src.main.python.org.SortDirectory import directory_sorter

#User's Loop
if __name__ == "__main__":
    user_input = 999
    opening_message = "What would you like to do?"
    while user_input == 999:
        print(opening_message)
        user_input = input()
        match user_input:
            case  "1":
                print("Input a directory to check: \n")
                target_directory = input()
                target_directory = os.getcwd() + f"\\{target_directory}"
                directory_sorter.sort_directory(os.getcwd(), target_directory)
                break
            case "2":
                break
            case _:
                print("Invalid Answer")
                user_input = 999





def options():
    option = {
        1: "Sort Directory",
        2: "Quit"
    }
    return option




'''
Framework:
    1. Define File Directories
    2. Verify Integrity
    3. Insert Directory to sort through
    4. Check/Split Files to check their extensions
    5. Sort based on their extensions
    6. Insert Sorted files into their dedicated Directory
    
'''
'''
Improvements:
    -UI Implementation (Pytinker?)-
    -Customization:

        -Allowing the User to customize Directories (Old/New)
        -Allow the User to customize their folder names
        -Allow User to specify Certain files
            -Via Keywords ,etc.
'''

