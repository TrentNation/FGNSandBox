import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox,ttk
from tkinter.constants import HORIZONTAL, VERTICAL


def add_list_to_screen(text_list, list_box : tk.PanedWindow, screen):
    for row in range(len(text_list)):
        list_box.add(tk.Button(text = f"{text_list[row]}",
                               ))

def change_list_to_list(list_box: tk.Listbox):
    clear_list(list_box)


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
    #text_directory_List.grid( row = 1, column = 0)

    button = tk.Button(root, text = "Clear", command = lambda: clear_list(text_directory_List))

    panel_main = tk.PanedWindow(root, orient=HORIZONTAL)
    panel_main.grid(row = 1, column =0)
    panel_window = tk.PanedWindow(panel_main, orient=VERTICAL, bd=5)
    panel_main.add(panel_window)

    add_list_to_screen(text_test_list,panel_window, root)

    #add_list_to_screen(text_test_list, text_directory_List, root)
    button.grid(row = 1, column = 1)




    root.mainloop()

    root.frame()

