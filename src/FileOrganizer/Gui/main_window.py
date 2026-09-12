import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox,ttk
from tkinter.constants import HORIZONTAL, VERTICAL
import os


'''
Saving the Current Directory's place is becoming a hassle.
Consider Storing it as a value to a class Object
'''

'''
Main Idea:
"Screen showcases current directory Files"
"Each File is showcased as a button"
"Clicking on them switches to their directory"
"You can back up a file via another button"
'''
def switch_window(screen=None):
    None

def sort_screen():
    new_window = tk.Toplevel()
    new_window.title("Sorting Screen")
    new_window.geometry("500x400")
    new_window.config(background="#907948")

    current_directory = os.getcwd()
    frame_sort = tk.Frame(new_window)
    frame_sort.pack(padx = 10, pady = 10, fill="both",expand=True)
    frame_sort.config(highlightthickness=0.5, highlightbackground="black")

    #Listing off Directory's Files
    frame_current_directory = tk.Frame(frame_sort)
    frame_current_directory.pack(side = "left", ipadx = 10, ipady = 10, expand=True,fill="both")
    frame_current_directory.config(highlightthickness=0.5, highlightbackground="blue", width=100)

    listbox_directory_files = tk.Listbox(frame_current_directory)
    listbox_directory_files.pack(side = "left",expand = True, fill="both")
    for current_file in os.listdir(current_directory):
        listbox_directory_files.insert(tk.END, current_file)

    #Current Directory Name
    '''
    Missing :
        -Updatable Directory Name
    '''
    frame_directory_name = tk.LabelFrame(frame_sort)
    frame_directory_name.config(highlightthickness=0.5, highlightbackground="red", height=50, width = 100, text="Current Directory:")
    frame_directory_name.pack( fill="both", expand=True)
    text_directory_name = tk.Label(frame_directory_name,font=("Arial", 14), text=current_directory.split('\\')[-1], wraplength=200)
    text_directory_name.pack(expand=True, fill="both")

    #Action Options
    '''
    Missing:
        -Wrapping Around Options
        -Actionable Buttons
    '''
    frame_options = tk.Frame(frame_sort)
    frame_options.pack(ipadx=10, ipady=300, expand = True, fill="both")
    frame_options.config(highlightthickness=0.5, highlightbackground="green", width=100)

    button_sort_folder = tk.Button(frame_options, text="Sort Folders", font = ("Arial", 20))
    button_change_directory = tk.Button(frame_options, text="Change Current Directory", font = ("Arial", 20))
    button_output_change = tk.Button(frame_options, text = "Change Output Folders", font = ("Arial", 20))
    button_sort_folder.grid(row = 0,column=0, sticky="nsew")
    button_change_directory.grid(row=1,column=0, sticky="nsew")
    button_output_change.grid(row=2,column=0, sticky="nsew")


'''

def add_task(event = None):
    task = entry_task.get().strip()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
'''
'''
def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        pass # Do "Nothing" if no item is selected
'''




if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Screen")
    #root.geometry("100x100")

    frame_main = tk.Frame(root)
    frame_main.pack(padx=10, pady=10, fill="x")
    '''
    entry_task = tk.Entry(frame_main, font=("Arial", 12))
    entry_task.pack(side="left", fill="x", expand=True, padx= (0, 5))
    entry_task.bind("<Return>", add_task) #Pressing Enter adds the task

    button_add = tk.Button(frame_main, text ="Add", command=add_task, width=8)
    button_add.pack(side="right")
    '''

    #Options Section
    option_list = tk.Frame(root)
    option_list.pack(side="right",padx=10,expand=True, pady=10,fill="both")
    option_list.config(highlightthickness=0.5, highlightbackground="black")

    button_Sort = tk.Button(option_list, text="Sort Folders" ,command = sort_screen, font=("Arial", 20))
    button_Sort.grid(row=0, column = 0, padx = 5, pady = 5)

    button_Link = tk.Button(option_list, text ="Link Folders", command = switch_window, font=("Arial",20))
    button_Link.grid(row=1, column=0, padx = 5, pady = 5)


    # Viewing Folders Section
    frame_list = tk.Frame(root)
    frame_list.pack(fill="both", expand=True, padx=10, pady=5)

    scrollbar = tk.Scrollbar(frame_list)
    scrollbar.pack(side="right", fill="y")

    text_test_name = "Default"
    listbox_tasks = tk.Listbox(frame_list, yscrollcommand=scrollbar.set, font = ("Arial", 12), selectbackground="gray")
    listbox_tasks.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=listbox_tasks.yview)

    #button_delete = tk.Button(root, text="Delete Selected Task", command = delete_task, background = "tomato", fg = "white")
    #button_delete.pack(fill = "x", padx=10, pady=10)

    #default_path = "C:\Coding\Coding Projects\Python Projects\Practice\FileOrganizer\src\FileOrganizer"
    #text_test_list =  os.listdir(default_path)


    root.mainloop()

