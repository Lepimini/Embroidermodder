#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENCE for licensing terms.

    ------------------------------------------------------------

    Another attempt at a graphical user interface that runs on
    lots of machines without a complex build or fragile dependencies.
    
    This is a translation of some of the ideas we came up with for other
    attempts.
"""

import tkinter as tk
import json

def new_file():
    print("New File")

def open_file():
    print("Open File")

def save_file():
    print("Save File")

def saveas_file():
    print("Save file as...")

def exit_program():
    print("Closing Embroidermodder 2.0.")
    exit()

def cut_object():
    print("cut")

def copy_object():
    print("copy")

def paste_object():
    print("paste")

function_map = {
    "new_file": new_file,
    "open_file": open_file,
    "save_file": save_file,
    "saveas_file": saveas_file,
    "exit_program": exit_program,
    "cut_object": cut_object,
    "copy_object": copy_object,
    "paste_object": paste_object
}

def build_menubar(root, menu_layout):
    menubar = tk.Menu(root)
    for m in menu_layout.keys():
        menu_ = tk.Menu(menubar, tearoff=0)
        for item in menu_layout[m].keys():
            cmd = menu_layout[m][item]
            menu_.add_command(label=item, command=function_map[cmd])
        menubar.add_cascade(label=m, menu=menu_)
    root.config(menu=menubar)

def build_buttongrid(root, button_layout):
    new_button = tk.Button(root, text="New", command=new_file)
    open_button = tk.Button(root, text="Open", command=open_file)
    new_button.grid(row=1, column=0)
    open_button.grid(row=1, column=1)

f = open("embroidermodder_layout.json", "r")
layout = json.loads(f.read())
f.close()
root = tk.Tk()
root.title(layout["title"])
root.minsize(layout["width"], layout["height"])
build_menubar(root, layout["menubar"])
build_buttongrid(root, layout["buttongrid"])
root.mainloop()


