import os

from src.FileOrganizer.SortDirectory import sort_controller
from src.FileOrganizer.LinkDirectory import link_controller
def option_decoder(option, user_options):
    if option in user_options:
        return -1
    else:
        print(user_options.get(option)[1])

def options():
    option = {
        1: ["Sort Directory", sort_controller],
        2: ["Link Directory", link_controller],
        3: ["Repeat Options", options()],
        4: "Quit"
    }
    for key, option in option.items():
        if len(option)==2:
            print(key,": ", option[0])
        else:
            print(key, ": ", option)
    return option

#User's Loop (Main)

def main():
    option_decoder("yep")

    user_input = 999
    opening_message = "What would you like to do?"
    print(opening_message)
    user_options = options()
    while user_input == 999:

        user_input = input()
        option_decoder(user_input, user_options)
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

