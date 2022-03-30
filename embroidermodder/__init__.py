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
from .data import *
from .actions import *
import tkinter as tk

# For some reason this is causing bugs so I've overridden it.
settings["translation_table"] = {
    "?": {
        "French": "?",
        "German": "?",
        "Spanish": "?"
    }
}

def translate(message):
    r"""
    To support other languages we use a simple nested dictionary,
    the first layer for what the message is and the second for
    the list of translations.

    In order to deal with incomplete translations calling the
    table falls back to returning the string supplied in English.
    """
    lang = settings["general_language"]
    translation = settings["translation_table"]
    if message in translation.keys():
        if lang in translation[message].keys():
            return translation[message][lang]
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
    buildMenubar(root, layout["menubar"])
    buildButtonGrid(root, layout["toolbar"])
    root.mainloop()
