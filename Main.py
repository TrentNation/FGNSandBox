import os
import shutil


#Specify the target Directory
directory = os.getcwd()
test_folder = "my_directory\\"

test_directory = directory +f"\\{test_folder}"



file_directory = {
    "txt" : "Document",
    "Doc" : "Document",
    "Docx" : "Document",
    "Epub" : "Document",
    "HTML" : "Document",
    "Mobi" : "Document",
    "PDF" : "Document",
    "7Z" : "Archives",
    "Tar" : "Archives",
    "War" : "Archives",
    "Zip" : "Archives",
    "Jar" : "Application",
    "Py" : "Application",
    "exe" : "Application",
    "mp3" : "Videos",
    "mp4" : "Videos"
}

for current_file in os.listdir(test_directory):
    extension = os.path.splitext(current_file)[1][1:]
    new_location = (directory + f"\\{file_directory.get(extension)}\\")
    old_location = f"{test_directory}" + f"{current_file}"
    try:
        os.mkdir(new_location)
        new_location += current_file
        os.rename(old_location, new_location)
    except FileExistsError:
        new_location += current_file
        os.rename(old_location, new_location)


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

