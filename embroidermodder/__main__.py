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

debug_mode = False

def debug_message(s):
    r"""
    Guards against debug messages coming up during normal operation.
    
    Just change debug_mode to True to activate it. We could have a toggle
    in the program to turn it on during operation for when something starts
    acting weird.
    """
    if debug_mode:
        print(s)


def doNothing():
    r""" This function intentionally does nothing. """
    debug_message("doNothing()")    


def new_file():
    " Creates a new file using the standard dialog. "
    debug_message("New File")


def open_file():
    " Opens a file using the standard dialog. "
    debug_message("Open File")


def save_file():
    " Saves a file using the standard dialog. "
    debug_message("Save File")


def save_as_file():
    " Saves an existing file as a new format using the standard dialog. "
    debug_message("Save file as...")


def exit_program():
    r"""
    Instead of closing using exit() this allows us to chain any checks,
    like the confirmation of the close, to the action.
    """
    debug_message("Closing Embroidermodder 2.0.")
    exit()


def cut_object():
    r"""
    Cut acts on objects selected before the action is called.
    
    If no objects are selected an error is returned.
    """
    debug_message("cut")


def copy_object():
    r"""
    Copy acts on objects selected before the action is called.
    
    If no objects are selected an error is returned.
    """
    debug_message("copy")


def paste_object():
    debug_message("paste")


def icon16():
    debug_message("icon16()")


def icon24():
    debug_message("icon24()")


def icon32():
    debug_message("icon32()")


def icon48():
    debug_message("icon48()")


def icon64():
    debug_message("icon64()")


def icon128():
    r"""
    """
    debug_message("icon128()")


def main_print():
    r"""
    """
    debug_message("print()")


def whatsthisContextHelp():
    r"""
    """
    debug_message("main_exit()")


def makeLayerCurrent():
    r"""
    """
    debug_message("main_exit()")


def layerSelector():
    r"""
    """
    debug_message("main_exit()")


def main_help():
    r"""
    """
    debug_message("main_help")


def settings_dialog():
    r"""
    """
    debug_message("settings_dialog()")


def designDetails():
    r"""
    """
    debug_message("main_exit()")


def main_cut():
    r"""
    """
    debug_message("cut()")
    
    #gview = _mainWin->activeView()
    #if gview:
    #    gview->cut()


def main_copy():
    r"""
    """
    debug_message("copy()")
    #gview = _mainWin->activeView()
    #if gview:
    #    gview->copy()


def main_paste():
    r"""
    """
    debug_message("main_paste()")
    #gview = _mainWin->activeView()
    #if gview:
    #    gview->paste()


def main_redo():
    r"""
    """
    debug_message("copy()")
    #gview = _mainWin->activeView()
    #if gview:
    #    gview->copy()


def main_undo():
    r"""
    """
    debug_message("main_paste()")
    #gview = _mainWin->activeView()
    #if gview:
    #    gview->paste()
    

def tipOfTheDay():
    r"""
    """
    debug_message("main_exit()")


def changelog():
    r"""
    """
    debug_message("changelog()")

    # display in a custom widget instead
    # QUrl changelogURL("help/changelog.html")
    # QDesktopServices::openUrl(changelogURL)


def showAllLayers():
    r"""
    """
    debug_message("main_exit()")


def freezeAllLayers():
    r"""
    """
    debug_message("main_exit()")


def thawAllLayers():
    r"""
    """
    debug_message("main_exit()")


def lockAllLayers():
    r"""
    """
    debug_message("main_exit()")


def unlockAllLayers():
    r"""
    """
    debug_message("main_exit()")


def hideAllLayers():
    r"""
    """
    debug_message("main_exit()")


def lineWeightSelector():
    r"""
    """
    debug_message("main_exit()")


def lineTypeSelector():
    r"""
    """
    debug_message("main_exit()")


def colorSelector():
    r"""
    """
    debug_message("main_exit()")


def windowClose():
    r"""
    """
    debug_message("main_exit()")


def windowTile():
    r"""
    """
    debug_message("main_exit()")


def windowCloseAll():
    r"""
    """
    debug_message("main_exit()")


def windowCascade():
    r"""
    """
    debug_message("main_exit()")


def windowNext():
    r"""
    """
    debug_message("main_exit()")


def windowPrevious():
    r"""
    """
    debug_message("main_exit()")


def textItalic():
    r"""
    """
    debug_message("main_exit()")

    settings.text_style.italic = not settings.text_style.italic


def textBold():
    r"""
    """
    debug_message("main_exit()")

    settings.text_style.bold = not settings.text_style.bold


def textStrikeout():
    r"""
    """
    debug_message("main_exit()")

    settings.text_style.strikeout = not settings.text_style.strikeout


def textUnderline():
    r"""
    """
    debug_message("main_exit()")

    settings.text_style.underline = not settings.text_style.underline


def textOverline():
    r"""
    """
    debug_message("main_exit()")

    settings.text_style.overline = not settings.text_style.overline


def makeLayerActive():
    r"""
    """
    debug_message("makeLayerActive()")
    debug_message("Implement makeLayerActive.")


def layerManager():
    r"""
    """
    debug_message("layerManager()")
    debug_message("Implement layerManager.")
    #/*LayerManager layman( _mainWin,  _mainWin)
    #layman.exec()
    #*/


def layerPrevious():
    r"""
    """
    debug_message("layerPrevious()")
    debug_message("Implement layerPrevious.")


def zoomRealtime():
    r"""
    """
    debug_message("zoomRealtime()")
    debug_message("Implement zoomRealtime.")


def zoomPrevious():
    r"""
    """
    debug_message("zoomPrevious()")
    debug_message("Implement zoomPrevious.")


def zoomWindow():
    r"""
    """
    debug_message("zoomWindow()")
    #/*View* gview = _mainWin->activeView()
    #if (gview) 
    #    gview->zoomWindow()


def zoomDynamic():
    r"""
    """
    debug_message("zoomDynamic()")
    debug_message("Implement zoomDynamic.")


def zoomScale():
    r"""
    """
    debug_message("zoomScale()")
    debug_message("Implement zoomScale.")


def zoomCenter():
    r"""
    """
    debug_message("zoomCenter()")
    debug_message("Implement zoomCenter.")


def zoomIn():
    r"""
    """
    debug_message("zoomIn()")


def zoomOut():
    r"""
    """
    debug_message("zoomOut()")


def zoomSelected():
    r"""
    """
    debug_message("zoomSelected()")


def zoomAll():
    r"""
    """
    debug_message("zoomAll()")
    debug_message("Implement zoomAll.")


def zoomExtents():
    r"""
    """
    debug_message("zoomExtents()")


def panrealtime():
    r"""
    """
    debug_message("panrealtime()")


def panpoint():
    r"""
    """
    debug_message("panpoint()")


def panLeft():
    r"""
    """
    debug_message("panLeft()")


def panRight():
    r"""
    """
    debug_message("panRight()")


def panUp():
    r"""
    """
    debug_message("panUp()")


def panDown():
    r"""
    """
    debug_message("panDown()")


function_map = {
    "new_file": new_file,
    "open_file": open_file,
    "save_file": save_file,
    "save_as_file": save_as_file,
    "exit_program": exit_program,
    "cut_object": cut_object,
    "copy_object": copy_object,
    "paste_object": paste_object
}

def build_menubar(root, menu_layout):
    r"""
    """
    menubar = tk.Menu(root)
    for m in menu_layout.keys():
        menu_ = tk.Menu(menubar, tearoff=0)
        for item in menu_layout[m].keys():
            cmd = menu_layout[m][item]
            menu_.add_command(label=item, command=function_map[cmd])
        menubar.add_cascade(label=m, menu=menu_)
    root.config(menu=menubar)


def build_buttongrid(root, button_layout):
    r"""
    """
    new_button = tk.Button(root, text="New", command=new_file)
    open_button = tk.Button(root, text="Open", command=open_file)
    new_button.grid(row=1, column=0)
    open_button.grid(row=1, column=1)


root = tk.Tk()
root.title(layout["title"])
root.minsize(layout["width"], layout["height"])
build_menubar(root, layout["menubar"])
build_buttongrid(root, layout["toolbar"])
root.mainloop()

