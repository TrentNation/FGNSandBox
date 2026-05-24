import os

from src.FileOrganizer.SortDirectory import directory_sorter

def options():
    option = {
        1: "Sort Directory",
        2: "Repeat Options",
        3: "Quit"
    }
    for key, option in option.items():
        print(key,": ", option)
    return

#User's Loop (Main)
if __name__ == "__main__":
    user_input = 999
    opening_message = "What would you like to do?"
    print(opening_message)
    print(options())
    while user_input == 999:

        user_input = input()
        match user_input:
            case  "1":

                print(opening_message)
                print(options())
                user_input = 999

            case "2":
                print(options())
                user_input = 999

            case _:
                print("Invalid Answer")
                user_input = 999










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

