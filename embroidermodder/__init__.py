#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENSE for licensing terms.

    ------------------------------------------------------------

    The __init__ file is for anyone that needs access to the data of
    embroidermodder for another application without booting the program.
    
    So when you import embroidermodder as a module it uses this file.
    But when the program is booted it's the equivalent of this program:
    
        import embroidermodder
        embroidermodder.main()

    You could have the clause `if __name__ == "__main__"` but in this
    case the embroidermodder command calls the function directly.
"""

import libembroidery
from .data import layout, config
from .actions import build_buttongrid, build_menubar
import tkinter as tk

def translate(message):
    r"""
    To support other languages we use a simple nested dictionary,
    the first layer for what the message is and the second for
    the list of translations.

    In order to deal with incomplete translations calling the
    table falls back to returning the string supplied in English.
    """
    lang = settings["general_language"] 
    if message in translation_table.keys():
        if lang in translation_table[message].keys():
            return translation_table[message][lang]
    return message

def main():
    """
    Main entry point for the program.

    This is the heart of the program, we're working on replacing
    the Qt reliance, so these functions and data represent the eventual core
    of the program.

    The widget system is created here, but it is built on top of the
    SVG system created in libembroidery. So a widget is an svg drawing,
    with a position to draw it in relative to its parent. The widgets
    form a tree rooted at the global variable called root.
    """
    root = tk.Tk()
    root.title(layout["title"])
    root.minsize(layout["width"], layout["height"])
    build_menubar(root, layout["menubar"])
    build_buttongrid(root, layout["toolbar"])
    root.mainloop()
