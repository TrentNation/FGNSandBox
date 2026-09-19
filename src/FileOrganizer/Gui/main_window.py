import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox,ttk
from tkinter.constants import HORIZONTAL, VERTICAL
import os

from src.FileOrganizer.Helper.inputting_directories import partial_input
from src.FileOrganizer.SortDirectory import extension_directory

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
    frame_files_directory = tk.Frame(frame_sort)
    frame_files_directory.pack(side = "left", ipadx = 10, ipady = 10, expand=True,fill="both")
    frame_files_directory.config(highlightthickness=0.5, highlightbackground="blue", width=100)


    scrollbar_directory = tk.Scrollbar(frame_files_directory)
    scrollbar_directory.pack(side="right", fill="y")
    listbox_directory_files = tk.Listbox(frame_files_directory, yscrollcommand=scrollbar_directory.set)
    scrollbar_directory.config(command=listbox_directory_files.yview)
    listbox_directory_files.pack(side = "left",expand = True, fill="both")
    for current_file in os.listdir(current_directory):
        for _ in range(20):
            listbox_directory_files.insert(tk.END, current_file)




#Current Directory Name
    '''
    Missing :
        -Updatable Directory Name
    '''
    frame_directory_name = tk.LabelFrame(frame_sort)
    frame_directory_name.config(highlightthickness=0.5, highlightbackground="red", height=50, width = 100, text="Current Directory:")
    frame_directory_name.pack( fill="both", expand=True)
    text_directory_name = tk.Label(frame_directory_name,font=("Arial", 20), text=current_directory.split('\\')[-1], wraplength=200)
    text_directory_name.pack(expand=True, fill="both")
    #text_directory_name.config(text= ("<Return>", popup_bonus))

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
    '''
    Opens Popup Window for Changing Directory
    '''
    button_change_directory = tk.Button(frame_options, text="Change Current Directory", font = ("Arial", 20))
    button_output_change = tk.Button(frame_options, text = "Change Output Folders", font = ("Arial", 20))
    button_sort_folder.grid(row = 0,column=0, sticky="nsew")
    button_change_directory.grid(row=1,column=0, sticky="nsew")
    button_output_change.grid(row=2,column=0, sticky="nsew")

'''
Purpose: popup_bonus should create a popup window for the user to input a valid directory address. Once it's validated, it should return the value to update the previous's window
current_directory value & tk.Label box.
'''
class Popup(tk.Toplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master,kwargs)
        label_entry_help = tk.Label(self, text="Input New Directory")
        label_entry_help.pack()

        self.entry = tk.Entry(self)
        self.entry.insert(0, "Hello World")
        self.entry.pack()

        button_enter = tk.Button(self, text="OK", command= self.button_submit)
        button_enter.pack()

        ##To keep Popup Window on Top + Pause Previous Windows
        self.transient(master)   #Set window to be top of main Window

        self.grab_set()          #Hijacks the commands from Main Window(Prevents any inputs on main window)
        master.wait_window(self) #Pauses The Main Window Until Destroyed(Finished
    def button_submit(self):
        self.result = self.entry.get()
        self.destroy()

'''
def popup_bonus():
    def input_directory(event = None):
        query_directory = event.get().strip()
        if os.path.isdir(query_directory):
            current_directory = query_directory
            win.destroy()
        else:
            tk.Label(win, text="ERROR: INVALID", highlightcolor="red", font=("Arial", 8)).pack()
    win = tk.Toplevel()
    win.wm_title("Enter New Directory")

    label_entry_help = tk.Label(win, text="Input New Directory")
    label_entry_help.pack()
    entry_directory = tk.Entry(win, font=("Arial", 12))
    entry_directory.pack()
    button_enter = tk.Button(win, text="Enter", command= lambda : input_directory(entry_directory))
    entry_directory.bind("<Return>", input_directory)
    button_enter.pack()
    button_exit = tk.Button(win, text="Exit", command = win.destroy)
    button_exit.pack()
    return entry_directory
'''


'''
Purpose:
Class object representing the Main Gui

'''

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
class SortScreen(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        #frame_main = tk.Frame(self)
        #frame_main.pack(padx=10, pady=10, fill="x")
        self.title("Sorting Screen")
        #self.geometry("500x400")
        self.config(background="#907948")
        current_directory = os.getcwd()

        frame_sort = tk.Frame(self)
        frame_sort.pack(padx = 10, pady = 10, fill="both",expand=True)
        frame_sort.config(highlightthickness=0.5, highlightbackground="black")

        #Listing off Directory's Files
        frame_files_directory = tk.Frame(frame_sort)
        frame_files_directory.pack(side = "left", ipadx = 10, ipady = 10, expand=True,fill="both")
        frame_files_directory.config(highlightthickness=0.5, highlightbackground="blue", width=100)

        '''
        Priority One:
            COMPLETE THIS SECTION
                -Needs Directory Extension Grouping Implemented
                -(Effectively, if the file is recognized by the sorter, it will be classified and shown to the user
                    -Example:
                    _________________________
                    |     Document1.pdf     |
                    |    Document2.docx     |  <----- Documents
                    |    Document3.txt      |
                    |_______________________|
                        File1.py              <------ Unknown?
                        File2.py
                        ...
        '''
        scrollbar_directory = tk.Scrollbar(frame_files_directory)
        scrollbar_directory.pack(side="left", fill="y")
        #listbox_directory_files = tk.Listbox(frame_files_directory, yscrollcommand=scrollbar_directory.set)
        canvas_directory_files = tk.Canvas(frame_files_directory,highlightthickness=0)
        canvas_directory_files.pack(fill="both")
        frame_directory_files = tk.Frame(canvas_directory_files, highlightthickness=1, highlightcolor="black")
        canvas_directory_files.create_window((0,0), window=frame_directory_files, anchor="nw")
        frame_directory_files.bind("<Configure>", lambda e: canvas_directory_files.configure(scrollregion=canvas_directory_files.bbox("all")))
        #frame_directory_files.pack(side="left", fill="both")

        scrollbar_directory.config(command=canvas_directory_files.yview, highlightthickness=1)
        canvas_directory_files.config(yscrollcommand=scrollbar_directory.set)

        #Collecting...
        list_directory_files = list()
        temp_dir = extension_directory.extension_directory()
        list_extension = temp_dir.get_directory()
        for current_file in os.listdir(current_directory):
            extension = os.path.splitext(current_file)[1][1:]
            list_directory_files.append([current_file,list_extension.get(extension)])

        #Displaying...
        while len(list_directory_files) != 0:
            frame_files_group = tk.Frame(frame_directory_files, highlightthickness=2, highlightcolor="red", padx=2,pady=2)
            text_group_directories = tk.Text(frame_files_group,height=2,width=20, background=frame_files_group.cget("background"))
            list_text = list()
            list_text.append(list_directory_files[0])
            current_extension = list_directory_files[0][1]

            #Turn this into a single for Loop
            list_text = [file[0] for file in list_directory_files if file[1] == list_text[0][1]]
            for file in list_text:
                text_group_directories.insert(tk.END, f'{file}\n')

            list_directory_files = list(filter(lambda x: x[0][1] == current_extension, list_directory_files))
            #frame_files_group.config(text=f"{current_extension}")
            label_extension = tk.Label(frame_files_group,text = f"<---- {current_extension}")
            label_extension.pack(side="right")
            frame_files_group.pack()
            text_group_directories.pack()
        #Current Directory Name
        frame_directory_name = tk.LabelFrame(frame_sort)
        frame_directory_name.config(highlightthickness=0.5, highlightbackground="red", height=50, width = 100, text="Current Directory:")
        frame_directory_name.pack( fill="both", expand=True)
        text_directory_name = tk.Label(frame_directory_name,font=("Arial", 20), text=current_directory.split('\\')[-1], wraplength=200)
        text_directory_name.pack(expand=True, fill="both")

        #Action Options
        frame_options = tk.Frame(frame_sort)
        frame_options.pack(ipadx=10, ipady=300, expand = True, fill="both")
        frame_options.config(highlightthickness=0.5, highlightbackground="green", width=100)

        button_sort_folder = tk.Button(frame_options, text="Sort Folders", font = ("Arial", 20))
        '''
        Opens Popup Window for Changing Directory
        '''
        button_change_directory = tk.Button(frame_options, text="Change Current Directory", font = ("Arial", 20))
        button_output_change = tk.Button(frame_options, text = "Change Output Folders", font = ("Arial", 20))
        button_sort_folder.grid(row = 0,column=0, sticky="nsew")
        button_change_directory.grid(row=1,column=0, sticky="nsew")
        button_output_change.grid(row=2,column=0, sticky="nsew")




class Main(tk.Frame):
    def __init__(self, master = None, **kwargs):
        super().__init__(master, **kwargs)
        frame_main = tk.Frame(self)
        frame_main.pack(padx=10,pady=10, fill="x")

        #Options Section
        frame_options = tk.Frame(self)
        frame_options.pack(side="right",padx=10,expand=True, pady=10,fill="both")
        frame_options.config(highlightthickness=0.5, highlightbackground="black")

        button_sort = tk.Button(frame_options, text="Sort Folders" ,command = self.switch_sort, font=("Arial", 20))
        button_sort.grid(row=0, column = 0, padx = 5, pady = 5)

        button_link = tk.Button(frame_options, text ="Link Folders", command = switch_window, font=("Arial",20))
        button_link.grid(row=1, column=0, padx = 5, pady = 5)

        ## Viewing Folders Section
        frame_list = tk.Frame(self)
        frame_list.pack(fill="both", expand=True, padx=10, pady=5)

        scrollbar = tk.Scrollbar(frame_list)
        scrollbar.pack(side="right", fill="y")

        text_test_name = "Default"
        listbox_tasks = tk.Listbox(frame_list, yscrollcommand=scrollbar.set, font = ("Arial", 12), selectbackground="gray")
        listbox_tasks.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=listbox_tasks.yview)
    def switch_sort(self):
        s = SortScreen(self)

    def switch_link(self):
        None
        # l = LinkScreen(self)



if __name__ == "__main__":
    root = tk.Tk()
    main = Main(root)
    main.pack()
    root.mainloop()

    #default_path = "C:\Coding\Coding Projects\Python Projects\Practice\FileOrganizer\src\FileOrganizer"
    #text_test_list =  os.listdir(default_path)


    root.mainloop()

