import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox,ttk

def add_list_to_screen(text_list, list_box : tk.Listbox, screen):
    for row in range(len(text_list)):
        list_box.insert(tk.END,text_list[row])

def clear_list(target:tk.Listbox):
    target.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Screen")

    frame = tk.Frame()
    frame.grid(row = 0, column = 0)
    text_test_name = "Default"
    text_directory_List = tk.Listbox()
    text_test_list = ( "Rat", "Ox", "Tiger", "Rabbit")
    text_directory_name = tk.Label(root, text = text_test_name)
    text_directory_name.grid( row= 0, column = 0)
    text_directory_List.grid( row = 1, column = 0)
    button = tk.Button(root, text = "Clear", command = lambda: clear_list(text_directory_List))
    add_list_to_screen(text_test_list, text_directory_List, root)
    button.grid(row = 1, column = 1)
    root.mainloop()
    root.frame()

