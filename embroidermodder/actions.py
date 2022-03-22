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


action_map = {
    "donothing": do_nothing,
    "new": new_file,
    "open": open_file,
    "save": save_file,
    "saveas": save_as_file,
    "print": main_print,
    "details": design_details,
    "exit": exit_program,
    "copy": copy_object,
    "cut": cut_object,
    "paste": paste_object,
    "old_code": """
        "statustip": "&Do Nothing",
        "tooltip": "Does nothing.",
        "function": do_nothing
        "function": open_file
        "statustip": "&Save",
        "tooltip": "Save the design to disk.",
        "function": save_file
        "statustip": "Save &As",
        "tooltip": "Save the design under a new name.",
        "function": save_as_file
        "statustip": "&Print",
        "tooltip": "Print the design.",
        "function": main_print
        "statustip": "&Details",
        "tooltip": "Details of the current design.",
        "function": design_details
        "statustip": "E&xit",
        "tooltip": "Exit the application.",
        "function": exit_program
    
    {
        cut_xpm,
        "statustip": "Cu&t",
        "Cut the current selection's contents to the clipboard.",
        main_cut
    },
    "copy": {
        copy_xpm,
        "statustip": "&Copy",
        "Copy the current selection's contents to the clipboard.",
        main_copy
    },
    "paste": {
        paste_xpm,
        "statustip": "&Paste",
        "Paste the clipboard's contents into the current selection.",
        main_paste
    },
    "undo": {
        undo_xpm,
        "statustip": "&Undo",
        "Reverses the most recent action.",
        main_undo
    },
    {
        redo_xpm,
        "redo",
        "statustip": "&Redo",
        "Reverses the effects of the previous undo action.",
        "Ctrl+Shift+Z",
        main_redo
    },
    {
        windowclose_xpm,
        "windowclose",
        "statustip": "Cl&ose",
        "Close the active window.",
        windowClose
    },
    {
        windowcloseall_xpm,
        "windowcloseall",
        "statustip": "Close &All",
        "Close all the windows.",
        windowCloseAll
    },
    {
        windowcascade_xpm,
        "windowcascade",
        "&Cascade",
        "Cascade the windows.",
        windowCascade
    },
    {
        windowtile_xpm,
        "windowtile",
        "&Tile",
        "Tile the windows.",
        windowTile
    },
    "windownext": {
        "icon": windownext_xpm,
        "Ne&xt",
        "Move the focus to the next window.",
        windowNext
    },
    "windowprevious": {
        windowprevious_xpm,
        "Pre&vious",
        "Move the focus to the previous window.",
        windowPrevious
    },
    "help": {
        "icon": help_xpm,
        "statustip": "&Help",
        "tooltip": "Displays help.",
        "function": main_help
    },
    "changelog": {
        "icon": changelog_xpm,
        "statustip": "&Changelog",
        "tooltip": "Describes new features in this product.",
        changelog
    },
    "tipoftheday": {
        "icon": tipoftheday_xpm,
        "&Tip Of The Day",
        "Displays a dialog with useful tips",
        tipOfTheDay
    },
    "about": {
        "icon": about_xpm,
        "&About Embroidermodder 2",
        "Displays information about this product.",
        main_about
    },
    "whatsthis": {
        "icon": whatsthis_xpm,
        "&What's This?",
        "What's This? Context Help!",
        whatsthisContextHelp
    },
    "icon16": {
        "icon": icon16_xpm,
        "Icon&16",
        "Sets the toolbar icon size to 16x16.",
        icon16
    },
    "icon24": {
        "icon": icon24_xpm,
        "statustip": "Icon&24",
        "tooltip": "Sets the toolbar icon size to 24x24.",
        "function": icon24
    },
    {
        icon32_xpm,
        "icon32",
        "Icon&32",
        "Sets the toolbar icon size to 32x32.",
        icon32
    },
    {
        icon48_xpm,
        "icon48",
        "Icon&48",
        "Sets the toolbar icon size to 48x48.",
        icon48
    },
    {
        icon64_xpm,
        "icon64",
        "Icon&64",
        "Sets the toolbar icon size to 64x64.",
        icon64
    },
    {
        icon128_xpm,
        "icon128",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128.",
        icon128
    },
    {
        settingsdialog_xpm,
        "settingsdialog",
        "&Settings",
        "Configure settings specific to this product.",
        settingsDialog
    },
    {
        makelayercurrent_xpm,
        "makelayercurrent",
        "&Make Layer Active",
        "Makes the layer of a selected object the active layer",
        makeLayerCurrent
    },
    {
        layers_xpm,
        "layers",
        "&Layers",
        "Manages layers and layer properties:  LAYER",
        layerManager
    },
    {
        layerselector_xpm,
        "layerselector",
        "&Layer Selector",
        "Dropdown selector for changing the current layer",
        layerSelector
    },
    {
        layerprevious_xpm,
        "layerprevious",
        "&Layer Previous",
        "Restores the previous layer settings:  LAYERP",
        layerPrevious
    },
    {
        colorselector_xpm,
        "colorselector",
        "&Color Selector",
        "Dropdown selector for changing the current thread color",
        colorSelector
    },
    {
        linetypeselector_xpm,
        "linetypeselector",
        "&Stitchtype Selector",
        "Dropdown selector for changing the current stitch type",
        lineTypeSelector
    },
    {
        lineweightselector_xpm,
        "lineweightselector",
        "&Threadweight Selector",
        "Dropdown selector for changing the current thread weight",
        lineWeightSelector
    },
    {
        hidealllayers_xpm,
        "hidealllayers",
        "&Hide All Layers",
        "Turns the visibility off for all layers in the current drawing:  HIDEALL",
        hideAllLayers
    },
    {
        showalllayers_xpm,
        "showalllayers",
        "&Show All Layers",
        "Turns the visibility on for all layers in the current drawing:  SHOWALL",
        showAllLayers
    },
    {
        freezealllayers_xpm,
        "freezealllayers",
        "&Freeze All Layers",
        "Freezes all layers in the current drawing:  FREEZEALL",
        freezeAllLayers
    },
    {
        thawalllayers_xpm,
        "thawalllayers",
        "&Thaw All Layers",
        "Thaws all layers in the current drawing:  THAWALL",
        thawAllLayers
    },
    {
        lockalllayers_xpm,
        "lockalllayers",
        "&Lock All Layers",
        "Locks all layers in the current drawing:  LOCKALL",
        lockAllLayers
    },
    {
        unlockalllayers_xpm,
        "unlockalllayers",
        "&Unlock All Layers",
        "Unlocks all layers in the current drawing:  UNLOCKALL",
        unlockAllLayers
    },
    {
        textbold_xpm,
        "textbold",
        "&Bold Text",
        "Sets text to be bold.",
        textBold
    },
    {
        textitalic_xpm,
        "textitalic",
        "&Italic Text",
        "Sets text to be italic.",
        textItalic
    },
    {
        textoverline_xpm,
        "textunderline",
        "&Underline Text",
        "Sets text to be underlined.",
        textOverline
    },
    {
        textstrikeout_xpm,
        "textstrikeout",
        "&StrikeOut Text",
        "Sets text to be striked out.",
        textStrikeout
    },
    {
        textoverline_xpm,
        "textoverline",
        "&Overline Text",
        "Sets text to be overlined.",
        textOverline
    },
    {
        zoomrealtime_xpm,
        "zoomrealtime",
        "Zoom &Realtime",
        "Zooms to increase or decrease the apparent size of objects in the current viewport.",
        zoomRealtime
    },
    {
        zoomprevious_xpm,
        "zoomprevious",
        "Zoom &Previous",
        "Zooms to display the previous view.",
        zoomPrevious
    },
    {
        zoomwindow_xpm,
        "zoomwindow",
        "Zoom &Window",
        "Zooms to display an area specified by a rectangular window.",
        zoomWindow
    },
    {
        zoomdynamic_xpm,
        "zoomdynamic",
        "Zoom &Dynamic",
        "Zooms to display the generated portion of the drawing.",
        zoomDynamic
    },
    {
        zoomscale_xpm,
        "zoomscale",
        "Zoom &Scale",
        "Zooms the display using a specified scale factor.",
        zoomScale
    },
    {
        zoomcenter_xpm,
        "zoomcenter",
        "Zoom &Center",
        "Zooms to display a view specified by a center point and magnification or height.",
        zoomCenter
    },
    {
        zoomin_xpm,
        "zoomin",
        "Zoom &In",
        "Zooms to increase the apparent size of objects.",
        zoomIn
    },
    {
        zoomout_xpm,
        "zoomout",
        "Zoom &Out",
        "Zooms to decrease the apparent size of objects.",
        zoomOut
    },
    {
        zoomselected_xpm,
        "zoomselected",
        "Zoom Selec&ted",
        "Zooms to display the selected objects.",
        zoomSelected
    },
    "zoomall": {
        "icon": zoomall_xpm,
        "Zoom &All",
        "Zooms to display the drawing extents or the grid limits.",
        zoomAll
    },
    "zoomextents": {
        "icon": zoomextents_xpm,
        
        "Zoom &Extents",
        "Zooms to display the drawing extents.",
        zoomExtents
    },
    {
        "icon": panrealtime_xpm,
        "panrealtime",
        "&Pan Realtime",
        "Moves the view in the current viewport.",
        panrealtime
    },
    {
        panpoint_xpm,
        "panpoint",
        "&Pan Point",
        "Moves the view by the specified distance.",
        panpoint
    },
    {
        panleft_xpm,
        "panleft",
        "&Pan Left",
        "Moves the view to the left.",
        panLeft
    },
    {
        panright_xpm,
        "panright",
        "&Pan Right",
        "Moves the view to the right.",
        panRight
    },
    {
        panup_xpm,
        "panup",
        "&Pan Up",
        "Moves the view up.",
        panUp
    },
    {
        pandown_xpm,
        "pandown",
        "&Pan Down",
        "Moves the view down.",
        panDown
    },
    {
        day_xpm,
        "day",
        "&Day",
        "Updates the current view using day vision settings.",
        dayVision
    },
    {
        night_xpm,
        "night",
        "&Night",
        "Updates the current view using night vision settings.",
        nightVision
    },
    {
        circle_xpm,
        "circle",
        "&Circle",
        "Creates a circle:  CIRCLE",
        doNothing
    },
    {
        line_xpm,
        "line",
        "&Line",
        "Creates straight line segments:  LINE",
        doNothing
    },
    {
        distance_xpm,
        "distance",
        "&Distance",
        "Measures the distance and angle between two points:  DIST",
        doNothing
    },
    {
        dolphin_xpm,
        "dolphin",
        "&Dolphin",
        "Creates a dolphin:  DOLPHIN",
        doNothing
    },
    {
        ellipse_xpm,
        "ellipse",
        "&Ellipse",
        "Creates a ellipse:  ELLIPSE",
        doNothing
    },
    {
        erase_xpm,
        "delete",
        "D&elete",
        "Removes objects from a drawing:  DELETE",
        doNothing
    },
    {
        heart_xpm,
        "heart",
        "&Heart",
        "Creates a heart:  HEART",
        doNothing
    },
    {
        locatepoint_xpm,
        "locatepoint",
        "&Locate Point",
        "Displays the coordinate values of a location:  ID",
        doNothing
    },
    {
        donothing_xpm,
        "trebleclef",
        "TrebleClef",
        "Creates a treble clef:  TREBLECLEF",
        doNothing
    },
    {
        path_xpm,
        "path",
        "&Path",
        "Creates a 2D path:  PATH",
        doNothing
    },
    {
        donothing_xpm,
        "platform",
        "&Platform",
        "List which platform is in use:  PLATFORM",
        doNothing
    },
    {
        point_xpm,
        "point",
        "&Point",
        "Creates multiple points:  POINT",
        doNothing
    },
    {
        polygon_xpm,
        "polygon",
        "Pol&ygon",
        "Creates a regular polygon:  POLYGON",
        "function": doNothing
    },
    {
        polyline_xpm,
        "polyline",
        "&Polyline",
        "Creates a 2D polyline:  PLINE",
        "function": doNothing
    },
    {
        quickleader_xpm,
        "quickleader",
        "&QuickLeader",
        "Creates a leader and annotation:  QUICKLEADER",
        "function": doNothing
    },
    {
        rectangle_xpm,
        "rectangle",
        "&Rectangle",
        "Creates a rectangular polyline: RECTANGLE",
        "function": doNothing
    },
    {
        rgb_xpm,
        "rgb",
        "&RGB",
        "Updates the current view colors:  RGB",
        "function": doNothing
    },
    {
        move_xpm,
        "move",
        "&Move",
        "Displaces objects a specified distance in a specified direction: MOVE",
        "function": doNothing
    },
    {
        rotate_xpm,
        "rotate",
        "&Rotate",
        "Rotates objects about a base point:  ROTATE",
        "function": doNothing
    },
    "sandbox": {
        "icon": sandbox_xpm,
        "statustip": "Sandbox",
        "tooltip": "A sandbox to play in:  SANDBOX",
        "function": doNothing
    },
    "scale": {
        "icon": scale_xpm,
        "statustip": "Sca&le",
        "tooltip": "Enlarges or reduces objects proportionally in the X, Y, and Z directions: SCALE",
        "function": doNothing
    },
    {
        donothing_xpm,
        "selectall",
        "&Select All",
        "Selects all objects:  SELECTALL",
        "function": doNothing
    },
    {
        singlelinetext_xpm,
        "singlelinetext",
        "&Single Line Text",
        "Creates single-line text objects:  TEXT",
        "function": doNothing
    },
    "snowflake": {
        "icon": snowflake_xpm,
        "&Snowflake",
        "Creates a snowflake:  SNOWFLAKE",
        "function": doNothing
    },
    {
        star_xpm,
        "star",
        "&Star",
        "Creates a star:  STAR",
        doNothing
    }"""
}


def build_menubar(root, menu_layout):
    r"""
    """
    menubar = tk.Menu(root)
    for m in menu_layout["order"]:
        menu_ = tk.Menu(menubar, tearoff=0)
        for item in menu_layout[m].keys():
            cmd = menu_layout[m][item]
            menu_.add_command(label=item, command=action_map[cmd])
        menubar.add_cascade(label=m, menu=menu_)
    root.config(menu=menubar)


def build_buttongrid(root, button_layout):
    r"""
    Create the toolbars in the order given by the "order" list.
    """
    for toolbar in button_layout["order"]:
        for button in button_layout[toolbar].keys():
            B = button_layout[toolbar][button]
            cmd = action_map[B["command"]]
            button_ = tk.Button(root, text=button, command=cmd)
            button_.grid(row=B["row"], column=B["column"])

