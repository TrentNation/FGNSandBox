import os
import subprocess
from src.FileOrganizer.SortDirectory import sort_controller
from src.FileOrganizer.LinkDirectory import link_controller
def option_decoder(option, user_options):
    if option in user_options:
        return -1
    else:
        print(user_options.get(option))

def print_dict(dictionary : dict):
    for key, option in dictionary.items():
        if len(option)>1:
            print(key,": ", option)
        else:
            print(key, ": ", option)
def options(picked = None):
    option = {
        1: "Sort Directory",
        2: "Link Directory",
        3: "Repeat Options",
        4: "Quit"
    }
    if picked is None:
        print_dict(option)
    else:
        match picked:
            case "1":
                subprocess.run(["python", "C:\Coding\Coding Projects\Python Projects\Practice\FileOrganizer\src\FileOrganizer\SortDirectory\\sort_controller.py"])
            case "2":
                subprocess.run(["python", "C:\Coding\Coding Projects\Python Projects\Practice\FileOrganizer\src\FileOrganizer\LinkDirectory\\link_controller.py"])
            case "3":
                print_dict(option)
            case "4":
                return 4

#User's Loop (Main)

def main():
    # option_decoder("yep")

    user_input = 999
    opening_message = "What would you like to do?"
    options()
    while user_input != "4":
        print(opening_message)
        user_input = input()
        user_options = options(user_input)

        # option_decoder(user_input, user_options)
        '''
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

#Entry Point
if __name__ == "__main__":
    main()



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
    -UI Implementation (Pytinker?)
    -Customization:

        -Allowing the User to customize Directories (Old/New)
        -Allow the User to customize their folder names
        -Allow User to specify Certain files
            -Via Keywords ,etc.
'''

