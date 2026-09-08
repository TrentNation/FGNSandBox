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
def switch_window():
    None

def add_task(event = None):
    task = entry_task.get().strip()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        pass # Do "Nothing" if no item is selected





if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Screen")
    #root.geometry("100x100")

    frame_main = tk.Frame(root)
    frame_main.pack(padx=10, pady=10, fill="x")

    entry_task = tk.Entry(frame_main, font=("Arial", 12))
    entry_task.pack(side="left", fill="x", expand=True, padx= (0, 5))
    entry_task.bind("<Return>", add_task) #Pressing Enter adds the task

    button_add = tk.Button(frame_main, text ="Add", command=add_task, width=8)
    button_add.pack(side="right")

    #Options Section
    option_list = tk.Frame(root)
    option_list.pack(side="right",padx=10,expand=True, pady=10,fill="both")
    option_list.config(highlightthickness=0.5, highlightbackground="black")

    button_add = tk.Button(option_list, text="Sort Folders" ,command = switch_window, font=("Arial", 20))
    button_add.pack(side="left",expand = True)



    # Viewing Folders Section
    frame_list = tk.Frame(root)
    frame_list.pack(fill="both", expand=True, padx=10, pady=5)

    scrollbar = tk.Scrollbar(frame_list)
    scrollbar.pack(side="right", fill="y")

    text_test_name = "Default"
    listbox_tasks = tk.Listbox(frame_list, yscrollcommand=scrollbar.set, font = ("Arial", 12), selectbackground="gray")
    listbox_tasks.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=listbox_tasks.yview)

    button_delete = tk.Button(root, text="Delete Selected Task", command = delete_task, background = "tomato", fg = "white")
    button_delete.pack(fill = "x", padx=10, pady=10)
    #default_path = "C:\Coding\Coding Projects\Python Projects\Practice\FileOrganizer\src\FileOrganizer"
    #text_test_list =  os.listdir(default_path)


    root.mainloop()

