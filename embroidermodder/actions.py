#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENCE for licensing terms.

    ------------------------------------------------------------

    To make the undo history easier to manage we use a dict for
    keeping all the action information together.
"""

import tkinter as tk
import pkg_resources
import tempfile


debug_mode = True

def load_image(path):
    r"""
    For safe packaging, and to reduce the risk of program
    crashing errors the resources are loaded via a temporary
    file.
    """
    file_data = pkg_resources.resource_string(__name__, path)
    file = tempfile.NamedTemporaryFile()
    file.write(file_data)
    return tk.PhotoImage(file=file.name)


def debug_message(s):
    r"""
    Guards against debug messages coming up during normal operation.

    Just change debug_mode to True to activate it. We could have a toggle
    in the program to turn it on during operation for when something starts
    acting weird.
    """
    if debug_mode:
        print(s)


def do_nothing():
    r""" This function intentionally does nothing. """
    debug_message("do_nothing()")    


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
    r"""
    """
    debug_message("paste")


def icon16():
    r"""
    """
    debug_message("icon16()")


def icon24():
    r"""
    """
    debug_message("icon24()")


def icon32():
    r"""
    """
    debug_message("icon32()")


def icon48():
    r"""
    """
    debug_message("icon48()")


def icon64():
    r"""
    """
    debug_message("icon64()")


def icon128():
    r"""
    """
    debug_message("icon128()")


def main_print():
    r"""
    """
    debug_message("print()")


def main_redo():
    r"""
    """
    debug_message("copy()")
    #View* gview = _mainWin->activeView()
    #if (gview) {
    #    gview->copy()


def main_undo():
    r"""
    """
    debug_message("main_paste()")
    #View* gview = _mainWin->activeView()
    #if gview:
    #    gview->paste()


def tipOfTheDay():
    r"""
    """
    debug_message("main_paste()")


def changelog():
    r"""
    """
    debug_message("changelog()")

    # display in a custom widget instead
    #
    # QUrl changelogURL("help/changelog.html")
    # QDesktopServices::openUrl(changelogURL)


def show_all_layers():
    r"""
    """
    return


def freezeAllLayers():
    r"""
    """
    return


def thawAllLayers():
    r"""
    """
    debug_message("thawAllLayers()")


def lockAllLayers():
    r"""
    """
    debug_message("lockAllLayers()")


def windowNext():
    r"""
    """
    debug_message("windowNext()")


def windowPrevious():
    debug_message(".")


def textItalic():
    settings["text_style_italic"] = not settings["text_style_italic"]


def textBold():
    settings["text_style_bold"] = not settings["text_style_bold"]


def textStrikeout():
    settings.text_style.strikeout = not settings.text_style.strikeout


def textUnderline():
    settings.text_style.underline = not settings.text_style.underline


def textOverline():
    settings.text_style.overline = not settings.text_style.overline


def layerManager():
    debug_message("layerManager()")
    debug_message("Implement layerManager.")
    #LayerManager layman( _mainWin,  _mainWin)
    #layman.exec()


def layerPrevious():
    debug_message("layerPrevious()")
    debug_message("Implement layerPrevious.")


def zoomRealtime():
    debug_message("zoomRealtime()")
    debug_message("Implement zoomRealtime.")


def zoomPrevious():
    ""
    debug_message("zoomPrevious()")
    debug_message("Implement zoomPrevious.")


def zoomWindow():
    ""
    debug_message("zoomWindow()")
    #gview = _mainWin->activeView()
    #if gview:
    #    gview->zoomWindow()


def zoomDynamic():
    ""
    debug_message("zoomDynamic()")
    debug_message("Implement zoomDynamic.")


def zoomScale():
    ""
    debug_message("zoomScale()")
    debug_message("Implement zoomScale.")


def zoomCenter():
    ""
    debug_message("zoomCenter()")
    debug_message("Implement zoomCenter.")


def zoomIn():
    ""
    debug_message("zoomIn()")


def zoomOut():
    ""
    debug_message("zoomOut()")


def zoomSelected():
    ""
    debug_message("zoomSelected()")


def zoomAll():
    ""
    debug_message("zoomAll()")
    debug_message("Implement zoomAll.")


def zoomExtents():
    ""
    debug_message("zoomExtents()")


def panrealtime():
    ""
    debug_message("panrealtime()")


def panpoint():
    ""
    debug_message("panpoint()")


def panLeft():
    ""
    debug_message("panLeft()")


def panRight():
    ""
    debug_message("panRight()")


def panUp():
    ""
    debug_message("panUp()")


def panDown():
    ""
    debug_message("panDown()")


def day_vision():
    r""" TODO: Make day vision color settings.
    gview = _mainWin->activeView()
    if gview:
        gview->setBackgroundColor("#FFFFFF")
        gview->setCrossHairColor("#000000")
        gview->setGridColor("#000000")
        """
    debug_message("day_vision()")


def night_vision():
    r""" TODO: Make night vision color settings.
    gview = _mainWin->activeView()
    if gview:
        gview->setBackgroundColor("#000000")
        gview->setCrossHairColor("#FFFFFF")
        gview->setGridColor("#FFFFFF")
        """
    debug_message("night_vision()")


def whatsthisContextHelp():
    r"""
    """
    debug_message("whatsthisContextHelp()")


def makeLayerCurrent():
    r"""
    """
    debug_message("makeLayerCurrent()")


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


def design_details():
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
    debug_message("main_redo()")
    #gview = _mainWin->activeView()
    #if gview:
    #    gview->copy()


def main_undo():
    r"""
    """
    debug_message("main_undo()")
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


def show_all_layers():
    r"""
    """
    debug_message("main_exit()")


def freeze_all_layers():
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


def settingsSnap():
    r"""
    """
    debug_message("stub")


def settingsGrid():
    r"""
    """
    debug_message("stub")


def settingsRuler():
    r"""
    """
    debug_message("stub")


def settingsOrtho():
    r"""
    """
    debug_message("stub")


def settingsPolar():
    r"""
    """
    debug_message("stub")


def settingsQSnap():
    r"""
    """
    debug_message("stub")


def settingsQTrack():
    r"""
    """
    debug_message("stub")


def settingsLwt():
    r"""
    """
    debug_message("stub")


def toggleSnap(on):
    r"""
    """
    debug_message("StatusBarButton toggleSnap()")


def toggleGrid(on):
    r"""
    """
    debug_message("StatusBarButton toggleGrid()")


def toggleRuler(on):
    r"""
    """
    debug_message("StatusBarButton toggleRuler()")


def toggleOrtho(on):
    r"""
    """
    debug_message("StatusBarButton toggleOrtho()")


def togglePolar(on):
    debug_message("StatusBarButton togglePolar()")


def toggleQSnap(on):
    debug_message("StatusBarButton toggleQSnap()")


def toggleQTrack(on):
    debug_message("StatusBarButton toggleQTrack()")


def toggleLwt(on):
    debug_message("StatusBarButton toggleLwt()")


def enableLwt():
    debug_message("StatusBarButton enableLwt()")


def disableLwt():
    debug_message("StatusBarButton disableLwt()")


def enableReal():
    debug_message("StatusBarButton enableReal()")


def disableReal():
    debug_message("StatusBarButton disableReal()")


def build_menubar(root, menu_layout):
    r"""
    """
    debug_message("build_menubar")
    menubar = tk.Menu(root)
    for m in menu_layout["order"]:
        debug_message(m)
        menu_ = tk.Menu(menubar, tearoff=0)
        for item in menu_layout[m]["order"]:
            debug_message(item)
            cmd = menu_layout[m][item]
            menu_.add_command(label=item, command=globals()[cmd])
        menubar.add_cascade(label=m, menu=menu_)
    root.config(menu=menubar)


def build_buttongrid(root, button_layout):
    r"""
    Create the toolbars in the order given by the "order" list.
    """
    debug_message("build_buttongrid")
    for toolbar in button_layout["order"]:
        debug_message(toolbar)
        for button in button_layout[toolbar]["order"]:
            debug_message(button)
            B = button_layout[toolbar][button]
            cmd = globals()[B["command"]]
            button_ = tk.Button(
                root,
                text=button,
                command=cmd,
                image=load_image('icons/default/dolphin.png')
            )
            button_.grid(row=B["row"], column=B["column"])

