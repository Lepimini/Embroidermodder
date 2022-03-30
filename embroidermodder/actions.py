#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENSE for licensing terms.

    ------------------------------------------------------------

    To make the undo history easier to manage we use a dict for
    keeping all the action information together.
"""

import tkinter as tk
from PIL import Image, ImageTk
from .data import load_image

debug_mode = True

def debugMessage(s):
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
    debugMessage("doNothing()")    


def newFile():
    " Creates a new file using the standard dialog. "
    debugMessage("New File")


def openFile():
    " Opens a file using the standard dialog. "
    debugMessage("Open File")


def saveFile():
    " Saves a file using the standard dialog. "
    debugMessage("Save File")


def saveAsFile():
    " Saves an existing file as a new format using the standard dialog. "
    debugMessage("Save file as...")


def exitProgram():
    r"""
    Instead of closing using exit() this allows us to chain any checks,
    like the confirmation of the close, to the action.
    """
    debugMessage("Closing Embroidermodder 2.0.")
    exit()


def cutObject():
    r"""
    Cut acts on objects selected before the action is called.
    
    If no objects are selected an error is returned.
    """
    debugMessage("cut")


def copyObject():
    r"""
    Copy acts on objects selected before the action is called.
    
    If no objects are selected an error is returned.
    """
    debugMessage("copy")


def pasteObject():
    r"""
    """
    debugMessage("paste")


def icon16():
    r"""
    """
    debugMessage("icon16()")


def icon24():
    r"""
    """
    debugMessage("icon24()")


def icon32():
    r"""
    """
    debugMessage("icon32()")


def icon48():
    r"""
    """
    debugMessage("icon48()")


def icon64():
    r"""
    """
    debugMessage("icon64()")


def icon128():
    r"""
    """
    debugMessage("icon128()")


def mainPrint():
    r"""
    """
    debugMessage("print()")


def mainRedo():
    r"""
    """
    debugMessage("copy()")
    #View* gview = _mainWin->activeView()
    #if (gview) {
    #    gview->copy()


def mainUndo():
    r"""
    """
    debugMessage("main_paste()")
    #View* gview = _mainWin->activeView()
    #if gview:
    #    gview->paste()


def tipOfTheDay():
    r"""
    """
    debugMessage("main_paste()")


def changelog():
    r"""
    """
    debugMessage("changelog()")

    # display in a custom widget instead
    #
    # QUrl changelogURL("help/changelog.html")
    # QDesktopServices::openUrl(changelogURL)


def showAllLayers():
    r"""
    """
    debugMessage("showAllLayers()")


def freezeAllLayers():
    r"""
    """
    debugMessage("freezeAllLayers()")


def thawAllLayers():
    r"""
    """
    debugMessage("thawAllLayers()")


def lockAllLayers():
    r"""
    """
    debugMessage("lockAllLayers()")


def windowNext():
    r"""
    """
    debugMessage("windowNext()")


def windowPrevious():
    r"""
    """
    debugMessage("windowPrevious()")


def textItalic():
    r"""
    """
    settings["text_style_italic"] = not settings["text_style_italic"]


def textBold():
    r"""
    """
    settings["text_style_bold"] = not settings["text_style_bold"]


def textStrikeout():
    r"""
    """
    settings.text_style.strikeout = not settings.text_style.strikeout


def textUnderline():
    r"""
    """
    settings.text_style.underline = not settings.text_style.underline


def textOverline():
    r"""
    """
    settings.text_style.overline = not settings.text_style.overline


def layerManager():
    r"""
    """
    debugMessage("layerManager()")
    debugMessage("Implement layerManager.")
    #LayerManager layman( _mainWin,  _mainWin)
    #layman.exec()


def layerPrevious():
    r"""
    """
    debugMessage("layerPrevious()")
    debugMessage("Implement layerPrevious.")


def zoomRealtime():
    r"""
    """
    debugMessage("zoomRealtime()")
    debugMessage("Implement zoomRealtime.")


def zoomPrevious():
    r"""
    """
    debugMessage("zoomPrevious()")
    debugMessage("Implement zoomPrevious.")


def zoomWindow():
    r"""
    """
    debugMessage("zoomWindow()")
    #gview = _mainWin->activeView()
    #if gview:
    #    gview->zoomWindow()


def zoomDynamic():
    r"""
    """
    debugMessage("zoomDynamic()")
    debugMessage("Implement zoomDynamic.")


def zoomScale():
    r"""
    """
    debugMessage("zoomScale()")
    debugMessage("Implement zoomScale.")


def zoomCenter():
    r"""
    """
    debugMessage("zoomCenter()")
    debugMessage("Implement zoomCenter.")


def zoomIn():
    r"""
    """
    debugMessage("zoomIn()")


def zoomOut():
    ""
    debugMessage("zoomOut()")


def zoomSelected():
    ""
    debugMessage("zoomSelected()")


def zoomAll():
    ""
    debugMessage("zoomAll()")
    debugMessage("Implement zoomAll.")


def zoomExtents():
    ""
    debugMessage("zoomExtents()")


def panrealtime():
    ""
    debugMessage("panrealtime()")


def panpoint():
    ""
    debugMessage("panpoint()")


def panLeft():
    ""
    debugMessage("panLeft()")


def panRight():
    ""
    debugMessage("panRight()")


def panUp():
    ""
    debugMessage("panUp()")


def panDown():
    ""
    debugMessage("panDown()")


def dayVision():
    r""" TODO: Make day vision color settings.
    gview = _mainWin->activeView()
    if gview:
        gview->setBackgroundColor("#FFFFFF")
        gview->setCrossHairColor("#000000")
        gview->setGridColor("#000000")
        """
    debugMessage("day_vision()")


def nightVision():
    r""" TODO: Make night vision color settings.
    gview = _mainWin->activeView()
    if gview:
        gview->setBackgroundColor("#000000")
        gview->setCrossHairColor("#FFFFFF")
        gview->setGridColor("#FFFFFF")
        """
    debugMessage("night_vision()")


def whatsthisContextHelp():
    r"""
    """
    debugMessage("whatsthisContextHelp()")


def makeLayerCurrent():
    r"""
    """
    debugMessage("makeLayerCurrent()")


def layerSelector():
    r"""
    """
    debugMessage("main_exit()")


def mainHelp():
    r"""
    """
    debugMessage("main_help")


def settingsDialog():
    r"""
    """
    debugMessage("settings_dialog()")


def designDetails():
    r"""
    """
    debugMessage("main_exit()")


def mainCut():
    r"""
    """
    debugMessage("cut()")
    
    #gview = _mainWin->activeView()
    #if gview:
    #    gview->cut()


def mainCopy():
    r"""
    """
    debugMessage("copy()")
    #gview = _mainWin->activeView()
    #if gview:
    #    gview->copy()


def mainPaste():
    r"""
    """
    debugMessage("main_paste()")
    #gview = _mainWin->activeView()
    #if gview:
    #    gview->paste()


def showAllLayers():
    r"""
    """
    debugMessage("main_exit()")


def freezeAllLayers():
    r"""
    """
    debugMessage("freezeAllLayers()")


def thawAllLayers():
    r"""
    """
    debugMessage("main_exit()")


def lockAllLayers():
    r"""
    """
    debugMessage("main_exit()")


def unlockAllLayers():
    r"""
    """
    debugMessage("main_exit()")


def hideAllLayers():
    r"""
    """
    debugMessage("main_exit()")


def lineWeightSelector():
    r"""
    """
    debugMessage("main_exit()")


def lineTypeSelector():
    r"""
    """
    debugMessage("main_exit()")


def colorSelector():
    r"""
    """
    debugMessage("main_exit()")


def windowClose():
    r"""
    """
    debugMessage("main_exit()")


def windowTile():
    r"""
    """
    debugMessage("main_exit()")


def windowCloseAll():
    r"""
    """
    debugMessage("windowCloseAll()")


def windowCascade():
    r"""
    """
    debugMessage("windowCascade()")


def windowNext():
    r"""
    """
    debugMessage("main_exit()")


def windowPrevious():
    r"""
    """
    debugMessage("main_exit()")


def textItalic():
    r"""
    """
    debugMessage("main_exit()")

    settings.text_style.italic = not settings.text_style.italic


def textBold():
    r"""
    """
    debugMessage("main_exit()")

    settings.text_style.bold = not settings.text_style.bold


def textStrikeout():
    r"""
    """
    debugMessage("main_exit()")

    settings.text_style.strikeout = not settings.text_style.strikeout


def textUnderline():
    r"""
    """
    debugMessage("main_exit()")

    settings.text_style.underline = not settings.text_style.underline


def textOverline():
    r"""
    """
    debugMessage("main_exit()")

    settings.text_style.overline = not settings.text_style.overline


def makeLayerActive():
    r"""
    """
    debugMessage("makeLayerActive()")
    debugMessage("Implement makeLayerActive.")


def layerManager():
    r"""
    """
    debugMessage("layerManager()")
    debugMessage("Implement layerManager.")
    #/*LayerManager layman( _mainWin,  _mainWin)
    #layman.exec()
    #*/


def layerPrevious():
    r"""
    """
    debugMessage("layerPrevious()")
    debugMessage("Implement layerPrevious.")


def zoomRealtime():
    r"""
    """
    debugMessage("zoomRealtime()")
    debugMessage("Implement zoomRealtime.")


def zoomPrevious():
    r"""
    """
    debugMessage("zoomPrevious()")
    debugMessage("Implement zoomPrevious.")


def zoomWindow():
    r"""
    """
    debugMessage("zoomWindow()")
    #/*View* gview = _mainWin->activeView()
    #if (gview) 
    #    gview->zoomWindow()


def zoomDynamic():
    r"""
    """
    debugMessage("zoomDynamic()")
    debugMessage("Implement zoomDynamic.")


def zoomScale():
    r"""
    """
    debugMessage("zoomScale()")
    debugMessage("Implement zoomScale.")


def zoomCenter():
    r"""
    """
    debugMessage("zoomCenter()")
    debugMessage("Implement zoomCenter.")


def zoomIn():
    r"""
    """
    debugMessage("zoomIn()")


def zoomOut():
    r"""
    """
    debugMessage("zoomOut()")


def zoomSelected():
    r"""
    """
    debugMessage("zoomSelected()")


def zoomAll():
    r"""
    """
    debugMessage("zoomAll()")
    debugMessage("Implement zoomAll.")


def zoomExtents():
    r"""
    """
    debugMessage("zoomExtents()")


def panrealtime():
    r"""
    """
    debugMessage("panrealtime()")


def panpoint():
    r"""
    """
    debugMessage("panpoint()")


def panLeft():
    r"""
    """
    debugMessage("panLeft()")


def panRight():
    r"""
    """
    debugMessage("panRight()")


def panUp():
    r"""
    """
    debugMessage("panUp()")


def panDown():
    r"""
    """
    debugMessage("panDown()")


def settingsSnap():
    r"""
    """
    debugMessage("stub")


def settingsGrid():
    r"""
    """
    debugMessage("stub")


def settingsRuler():
    r"""
    """
    debugMessage("stub")


def settingsOrtho():
    r"""
    """
    debugMessage("stub")


def settingsPolar():
    r"""
    """
    debugMessage("stub")


def settingsQSnap():
    r"""
    """
    debugMessage("stub")


def settingsQTrack():
    r"""
    """
    debugMessage("stub")


def settingsLwt():
    r"""
    """
    debugMessage("stub")


def toggleSnap(on):
    r"""
    """
    debugMessage("StatusBarButton toggleSnap()")


def toggleGrid(on):
    r"""
    """
    debugMessage("StatusBarButton toggleGrid()")


def toggleRuler(on):
    r"""
    """
    debugMessage("StatusBarButton toggleRuler()")


def toggleOrtho(on):
    r"""
    """
    debugMessage("StatusBarButton toggleOrtho()")


def togglePolar(on):
    debugMessage("StatusBarButton togglePolar()")


def toggleQSnap(on):
    debugMessage("StatusBarButton toggleQSnap()")


def toggleQTrack(on):
    debugMessage("StatusBarButton toggleQTrack()")


def toggleLwt(on):
    debugMessage("StatusBarButton toggleLwt()")


def enableLwt():
    debugMessage("StatusBarButton enableLwt()")


def disableLwt():
    debugMessage("StatusBarButton disableLwt()")


def enableReal():
    debugMessage("StatusBarButton enableReal()")


def disableReal():
    debugMessage("StatusBarButton disableReal()")


def buildMenubar(root, menu_layout):
    r"""
    """
    debugMessage("build_menubar")
    menubar = tk.Menu(root)
    for m in menu_layout["order"]:
        debugMessage(m)
        menu_ = tk.Menu(menubar, tearoff=0)
        for item in menu_layout[m]["order"]:
            debugMessage(item)
            cmd = menu_layout[m][item]
            menu_.add_command(label=item, command=globals()[cmd])
        menubar.add_cascade(label=m, menu=menu_)
    root.config(menu=menubar)

# to stop the garbage collector stealing it
tkimg = {}

def buildButtonGrid(root, button_layout):
    r"""
    Create the toolbars in the order given by the "order" list.
    """
    global tkimg
    debugMessage("build_buttongrid")
    for toolbar in button_layout["order"]:
        debugMessage(toolbar)
        for button in button_layout[toolbar]["order"]:
            debugMessage(button)
            B = button_layout[toolbar][button]
            cmd = globals()[B["command"]]
            tkimg[button] = load_image(B["icon"])
            button_ = tk.Button(
                root,
                command=cmd,
                image=tkimg[button]
            )
            button_.grid(row=B["row"], column=B["column"])

