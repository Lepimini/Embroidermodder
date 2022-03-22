#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENCE for licensing terms.

    ------------------------------------------------------------
    
    Main entry point for the program.

    This is the heart of the program, we're working on replacing
    the Qt reliance, so these functions and data represent the eventual core
    of the program.

    The widget system is created here, but it is built on top of the
    SVG system created in libembroidery. So a widget is an svg drawing,
    with a position to draw it in relative to its parent. The widgets
    form a tree rooted at the global variable called root.
"""

import tkinter as tk
from .data import layout
from .actions import build_buttongrid, build_menubar

MAX_DISTANCE = 10000000.0

circle_modes = [
    "1P_RAD", "1P_DIA", "2P", "3P", "TTR"
]

folders = {
    "app": "",
    "commands": "",
    "help": "",
    "images": "",
    "samples": "",
    "translations": ""
}

path_types = [
    "MOVETO",
    "LINETO",
    "ARCTO",
    "ARCMOVETO",
    "ELLIPSE",
    "END"
]

permissions = [
    "USER", "SYSTEM"
]

def translate(s):
    r"""
    To support other languages we use a simple nested dictionary,
    the first layer for what the message is and the second for
    the list of translations.
    
    In order to deal with incomplete translations calling the
    table falls back to returning the string supplied in English.
    """
    lang = settings["general_language"] 
    if s in translation_table.keys():
        if lang in translation_table[s].keys():
            return translation_table[s][lang]
    return s

root = tk.Tk()
root.title(layout["title"])
root.minsize(layout["width"], layout["height"])
build_menubar(root, layout["menubar"])
build_buttongrid(root, layout["toolbar"])
root.mainloop()

