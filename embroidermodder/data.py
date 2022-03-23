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

from .icons import *

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


file_toolbar = [
    "new_file",
    "open",
    "save",
    "saveas",
    "print",
    "designdetails",
    "---",
    "help"
]
edit_toolbar = [
    "undo",
    "redo",
    "---",
    "cut",
    "copy",
    "paste"
]
view_toolbar = [
    "day",
    "night"
]
pan_toolbar = [
    "panrealtime",
    "panpoint",
    "---",
    "panleft",
    "panright",
    "panup",
    "pandown"
]

"""
int icon_toolbar[] = {
    "icon16,
    "icon24,
    "icon32,
    "icon48,
    "icon64,
    "icon128,
    -2
]

int help_toolbar[] = {
    "help,
    -1,
    "changelog,
    -1,
    "about,
    -1,
    "whatsthis,
    -2
]

int zoom_toolbar[] = {
    "zoomwindow,
    "zoomdynamic,
    "zoomscale,
    -1,
    "zoomcenter,
    "zoomin,
    "zoomout,
    -1,
    "zoomselected,
    "zoomall,
    "zoomextents,
    -2
]

layer_toolbar = [

]

text_toolbar = [

]

properties_toolbar = [

]

int *toolbars[] = {
    file_toolbar,
    edit_toolbar,
    view_toolbar,
    zoom_toolbar,
    pan_toolbar,
    icon_toolbar,
    help_toolbar,
    layer_toolbar,
    text_toolbar,
    properties_toolbar
]


int file_menu[] = {
    "new",
    "open",
    "save",
    "saveas",
    "print",
    "designdetails",
    -1,
    "help,
    -1,
    "exit,
    -2
]

int edit_menu[] = {
    "undo,
    "redo,
    -1,
    "cut,
    "copy,
    "paste,
    -2
]

int view_menu[] = {
    "day,
    "night,
    -2
]

int pan_menu[] = {
    "panrealtime,
    "panpoint,
    -1,
    "panleft,
    "panright,
    "panup,
    "pandown,
    -2
]
icon_menu = [
    "icon16",
    "icon24",
    "icon32",
    "icon48",
    "icon64",
    "icon128",
]
help_menu = [
    "help",
    "---",
    "changelog",
    "---",
    "tipoftheday",
    "---",
    "about",
    "---",
    "whatsthis"
]

int zoom_menu[] = {
    "zoomwindow",
    "zoomdynamic",
    "zoomscale",
    "---",
    "zoomcenter,
    "zoomin,
    "zoomout,
    "---",
    "zoomselected,
    "zoomall,
    "zoomextents,
]

int settings_menu[] = {
    "settingsdialog,
    -1,
    -2
]

int recent_menu[] = {
    -1,
    -2
]

int window_menu[] = {
    -1,
    -2
]

int *menus[] = {
    file_menu,
    edit_menu,
    view_menu,
    settings_menu,
    window_menu,
    help_menu,
    recent_menu,
    zoom_menu,
    pan_menu
]

float symbol_scale = 0.01

/* Symbols use the SVG path syntax.
 *
 * In theory, we could combine the icons and symbols systems,
 * since they could be rendered once and stored as icons in Qt.
 * (Or as textures in FreeGLUT.)
 *
 * Also we want to render the patterns themselves using SVG
 * syntax, so it would save on repeated work overall.
 */
symbol_list[] = {
    /* 0 */ "icon 0",
    /* 1 */ "M 5 100 L 45 100 M 0 25 L 25 0 L 25 100",
    /* 2 */ "icon 2",
    /* 3 */ "icon 3",
    /* 4 */ "M 50 100 L 50 0 L 0 50 L 50 50",
    /* 5 */ "icon 5",
    /* 6 */ "icon 6",
    /* 7 */ "M 0 0 L 50 0 L 25 75 L 25 100",
    /* 8 */ "icon 8",
    /* 9 */ "icon 9",
    /* - */ "M 0 50 L 50 50",
    /* ' */ "M 25 100 L 25 25",
    /* " */ "M 10 0 L 10 25 M 40 0 L 40 25"
]

path_symbol icon_zero[] = {
    /* path.addEllipse(QPointF(x+0.25*xScale, y-0.50*yScale), 0.25*xScale, 0.50*yScale);*/
    M 0 -0.75
    L 0 -0.25
    A 0 -0.5 0.5 0.5 180.0 180.0
    L 0.5, -0.75
    A 0 -1.0, 0.5, 0.5, 0.0, 180.0
]

path_symbol icon_two[] = {
    {PATHS_MOVETO, 0 -0.75
    A {0.45, 1.00, 0.50, 180.00, -216.87
    L 0 0.0
    L {0.50, 0.0
]

path_symbol icon_three[] = {
    {PATHS_ARCMOVETO, 0 -0.50, 0.50, 0.50, 195.00
    A 0 -0.50, 0.50, 195.00, 255.00
    A 0 -0.50, 0.50, 270.00, 255.00
]

path_symbol icon_five[] = {
    M 50 0 L 0 0 L 0 50 L 25 50 A 0.0, -0.5 0.5 0.5 90.0 -180.0 L 0 0
]

path_symbol icon_six[] = {
    path.addEllipse(QPointF(x+0.25*xScale, y-0.25*yScale), 0.25*xScale, 0.25*yScale)
    M 0 75 L 0 25
    path.arcTo(x+0.00*xScale, y-1.00*yScale, 0.50*xScale, 0.50*yScale, 180.00, -140.00)
]

path_symbol icon_eight[] = {
    path.addEllipse(QPointF(x+0.25*xScale, y-0.25*yScale), 0.25*xScale, 0.25*yScale)
    path.addEllipse(QPointF(x+0.25*xScale, y-0.75*yScale), 0.25*xScale, 0.25*yScale)
]

path_symbol icon_nine[] = {
    path.addEllipse(QPointF(x+0.25*xScale, y-0.75*yScale), 0.25*xScale, 0.25*yScale)
    M 0.50*xScale, y-0.75*yScale)
    L x+0.50*xScale, y-0.25*yScale)
    path.arcTo(x+0.00*xScale, y-0.50*yScale, 0.50*xScale, 0.50*yScale, 0.00, -140.00)
]

# Comboboxes */
# --------------------------------- */
ARC_CLOCKWISE                 0
GENERAL_LAYER                 1
GENERAL_COLOR                 2
GENERAL_LINE_TYPE             3
GENERAL_LINE_WEIGHT           4
TEXT_SINGLE_FONT              5
TEXT_SINGLE_JUSTIFY           6
COMBOBOX_PROPERTY_EDITORS     7

PROPERTY_EDITORS \
    ( LINEEDIT_PROPERTY_EDITORS + COMBOBOX_PROPERTY_EDITORS )

LINE_EDIT_DOUBLE               0
LINE_EDIT_INT                  1
LINE_EDIT_STR                  2
COMBO_BOX_TYPE                 3

# Keys */
# ---- */
# value type - int: See OBJ_TYPE_VALUES */
OBJ_TYPE                      0
# value type - str: See OBJ_NAME_VALUES */
OBJ_NAME                      1
# value type - str: "USER", "DEFINED", "STRINGS", etc... */
OBJ_LAYER                     2
# value type - int: 0-255
  TODO: Use color chart in formats/format-dxf.h for this */
OBJ_COLOR                     3
#value type - int: See OBJ_LTYPE_VALUES*/
OBJ_LTYPE                     4
 #value type - int: 0-27*/
OBJ_LWT                       5
# value type - int: See OBJ_RUBBER_VALUES */
OBJ_RUBBER                    6

# Values */
# ------ */
# NOTE: Allow this enum to evaluate false */
OBJ_TYPE_NULL                 0
# NOTE: Values >= 65536 ensure compatibility with qgraphicsitem_cast() */
OBJ_TYPE_BASE            100000
OBJ_TYPE_ARC             100001
OBJ_TYPE_BLOCK           100002
OBJ_TYPE_CIRCLE          100003
OBJ_TYPE_DIMALIGNED      100004
OBJ_TYPE_DIMANGULAR      100005
OBJ_TYPE_DIMARCLENGTH    100006
OBJ_TYPE_DIMDIAMETER     100007
OBJ_TYPE_DIMLEADER       100008
OBJ_TYPE_DIMLINEAR       100009
OBJ_TYPE_DIMORDINATE     100010
OBJ_TYPE_DIMRADIUS       100011
OBJ_TYPE_ELLIPSE         100012
OBJ_TYPE_ELLIPSEARC      100013
OBJ_TYPE_RUBBER          100014
OBJ_TYPE_GRID            100015
OBJ_TYPE_HATCH           100016
OBJ_TYPE_IMAGE           100017
OBJ_TYPE_INFINITELINE    100018
OBJ_TYPE_LINE            100019
OBJ_TYPE_PATH            100020
OBJ_TYPE_POINT           100021
OBJ_TYPE_POLYGON         100022
OBJ_TYPE_POLYLINE        100023
OBJ_TYPE_RAY             100024
OBJ_TYPE_RECTANGLE       100025
OBJ_TYPE_SLOT            100026
OBJ_TYPE_SPLINE          100027
OBJ_TYPE_TEXTMULTI       100028
OBJ_TYPE_TEXTSINGLE      100029
OBJ_TYPE_UNKNOWN         100030


# CAD Linetypes */
OBJ_LTYPE_CONT                0
OBJ_LTYPE_CENTER              1
OBJ_LTYPE_DOT                 2
OBJ_LTYPE_HIDDEN              3
OBJ_LTYPE_PHANTOM             4
OBJ_LTYPE_ZIGZAG              5
# Embroidery Stitchtypes */
# __________ */
OBJ_LTYPE_RUNNING             6
# vvvvvvvvvv */
OBJ_LTYPE_SATIN               7
# >>>>>>>>>> */
OBJ_LTYPE_FISHBONE            8

# OBJ_LWT_VALUES
 * --------------
 */
OBJ_LWT_BYLAYER             (-2)
OBJ_LWT_BYBLOCK             (-1)
OBJ_LWT_DEFAULT                0
OBJ_LWT_01                     1
OBJ_LWT_02                     2
OBJ_LWT_03                     3
OBJ_LWT_04                     4
OBJ_LWT_05                     5
OBJ_LWT_06                     6
OBJ_LWT_07                     7
OBJ_LWT_08                     8
OBJ_LWT_09                     9
OBJ_LWT_10                    10
OBJ_LWT_11                    11
OBJ_LWT_12                    12
OBJ_LWT_13                    13
OBJ_LWT_14                    14
OBJ_LWT_15                    15
OBJ_LWT_16                    16
OBJ_LWT_17                    17
OBJ_LWT_18                    18
OBJ_LWT_19                    19
OBJ_LWT_20                    20
OBJ_LWT_21                    21
OBJ_LWT_22                    22
OBJ_LWT_23                    23
OBJ_LWT_24                    24


# OBJ_SNAP_VALUES */
# --------------- */
# NOTE: Allow this enum to evaluate false */
OBJ_SNAP_NULL                  0
OBJ_SNAP_ENDPOINT              1
OBJ_SNAP_MIDPOINT              2
OBJ_SNAP_CENTER                3
OBJ_SNAP_NODE                  4
OBJ_SNAP_QUADRANT              5
OBJ_SNAP_INTERSECTION          6
OBJ_SNAP_EXTENSION             7
OBJ_SNAP_INSERTION             8
OBJ_SNAP_PERPENDICULAR         9
OBJ_SNAP_TANGENT              10
OBJ_SNAP_NEAREST              11
OBJ_SNAP_APPINTERSECTION      12
OBJ_SNAP_PARALLEL             13


# OBJ_RUBBER_VALUES
 * -----------------
 * NOTE: Allow this enum to evaluate false and true */
OBJ_RUBBER_OFF                 0
OBJ_RUBBER_ON                  1
OBJ_RUBBER_CIRCLE_1P_RAD       2
OBJ_RUBBER_CIRCLE_1P_DIA       3
OBJ_RUBBER_CIRCLE_2P           4
OBJ_RUBBER_CIRCLE_3P           5
OBJ_RUBBER_CIRCLE_TTR          6
OBJ_RUBBER_CIRCLE_TTT          7
OBJ_RUBBER_DIMLEADER_LINE      8
OBJ_RUBBER_ELLIPSE_LINE        9
OBJ_RUBBER_ELLIPSE_MAJORDIAMETER_MINORRADIUS 10
OBJ_RUBBER_ELLIPSE_MAJORRADIUS_MINORRADIUS 11
OBJ_RUBBER_ELLIPSE_ROTATION   12
OBJ_RUBBER_GRIP               13
OBJ_RUBBER_LINE               14
OBJ_RUBBER_POLYGON            15
OBJ_RUBBER_POLYGON_INSCRIBE   16
OBJ_RUBBER_POLYGON_CIRCUMSCRIBE 17
OBJ_RUBBER_POLYLINE           18
OBJ_RUBBER_IMAGE              19
OBJ_RUBBER_RECTANGLE          20
OBJ_RUBBER_TEXTSINGLE         21


# SPARE_RUBBER_VALUES
 * -------------------
 * NOTE: Allow this enum to evaluate false */
SPARE_RUBBER_OFF               0
SPARE_RUBBER_PATH              1
SPARE_RUBBER_POLYGON           2
SPARE_RUBBER_POLYLINE          3


# PREVIEW_CLONE_VALUES
 * --------------------
 * NOTE: Allow this enum to evaluate false */
PREVIEW_CLONE_NULL            0
PREVIEW_CLONE_SELECTED        1
PREVIEW_CLONE_RUBBER          2

# PREVIEW_MODE_VALUES
# -------------------
# NOTE: Allow this enum to evaluate false
preview_modes = [
    "null",
    "move",
    "rotate",
    "scale"
]

# COMMAND ACTIONS
# ---------------
actions = [
    "donothing",
    "new",
    "open",
    "save",
    "saveas",
    "print",
    "designdetails"
]
"exit                =   7
"cut                 =   8
"copy                =   9
"paste               =  10
"undo                =  11
"redo                =  12
# Window Menu */
"windowclose         =  13
"windowcloseall      =  14
"windowcascade       =  15
"windowtile          =  16
"windownext          =  17
"windowprevious      =  18
# Help Menu */
"help                =  19
"changelog           =  20
"tipoftheday         =  21
"about               =  22
"whatsthis           =  23
# Icons */
"icon16              =  24
"icon24              =  25
"icon32              =  26
"icon48              =  27
"icon64              =  28
"icon128             =  29
"settingsdialog      =  30
# Layer ToolBar */
"makelayercurrent    =  31
"layers              =  32
"layerselector       =  33
"layerprevious       =  34
"colorselector       =  35
"linetypeselector    =  36
"lineweightselector  =  37
"hidealllayers       =  38
"showalllayers       =  39
"freezealllayers     =  40
"thawalllayers       =  41
"lockalllayers       =  42
"unlockalllayers     =  43
# Text ToolBar */
"textbold            =  44
"textitalic          =  45
"textunderline       =  46
"textstrikeout       =  47
"textoverline        =  48
# Zoom ToolBar */
"zoomrealtime        =  49
"zoomprevious        =  50
"zoomwindow          =  51
"zoomdynamic         =  52
"zoomscale           =  53
"zoomcenter          =  54
"zoomin              =  55
"zoomout             =  56
"zoomselected        =  57
"zoomall             =  58
"zoomextents         =  59
# Pan SubMenu */
"panrealtime         =  60
"panpoint            =  61
"panleft             =  62
"panright            =  63
"panup               =  64
"pandown             =  65
# View */
"day                 =  66
"night               =  67

# Just added */
"trebleclef          =  68
"path                =  69
"circle              =  70
"line                =  71
"distance            =  72
"dolphin             =  73
"ellipse             =  74
"delete              =  75
"heart               =  76
"locatepoint         =  77
N_ACTIONS                  =  78

    "save": save_file,
        "statustip": "&Save",
        "tooltip": "Save the design to disk.",
        "function": save_file
    "saveas": save_as_file,
        "statustip": "Save &As",
        "tooltip": "Save the design under a new name.",
        "function": save_as_file
    "print": main_print,
        "statustip": "&Print",
        "tooltip": "Print the design.",
    "details": design_details,
        "statustip": "&Details",
        "tooltip": "Details of the current design.",
        "function": design_details
    "exit": exit_program,
        "statustip": "E&xit",
        "tooltip": "Exit the application.",
        "function": exit_program
    
    "cut": cut_object,
    {
        "icon": cut_xpm,
        "statustip": "Cu&t",
        "tooltip": "Cut the current selection's contents to the clipboard.",
        main_cut
    },
    "copy": copy_object,
    "copy": {
        "icon": "copy",
        "statustip": "&Copy",
        "tooltip": "Copy the current selection's contents to the clipboard.",
        main_copy
    },
    "paste": paste_object,
    "paste": {
        paste_xpm,
        "statustip": "&Paste",
        "tooltip": "Paste the clipboard's contents into the current selection.",
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
    }
}
"""


layout = {
    "title": "Embroidermodder 2.0",
    "width": 640,
    "height": 480,
    "MAX_STRING_LENGTH": 500,
    "menubar": {
        "order": [
            "File",
            "Edit",
            "View",
            "Settings",
            "Window",
            "Help",
            "Recent",
            "Zoom",
            "Pan"
        ],
        "File": {
            "order": [],
            "New": "new_file",
            "Open...": "open_file",
            "Save...": "save_file",
            "Save As...": "save_as_file",
            "Exit": "exit_program"
        },
        "Edit": {
            "order": [],
            "Cut": "cut_object",
            "Copy": "copy_object",
            "Paste": "paste_object"
        },
        "View": {
            "order": []
        },
        "Settings": {
            "order": []
        },
        "Window": {
            "order": []
        },
        "Help": {
            "order": []
        },
        "Recent": {
            "order": []
        },
        "Zoom": {
            "order": []
        },
        "Pan": {
            "order": []
        }
    },
    "toolbar": {
        "order": [
            "File",
            "Edit",
            "View",
            "Zoom",
            "Pan",
            "Icon",
            "Help",
            "Layer",
            "Text",
            "Properties"
        ],
        "File": {
            "order": [
                "New",
                "Open"
            ],
            "New": {
                "icon": "new",
                "command": "new_file",
                "row": 1,
                "column": 0,
                "statustip": "&New",
                "tooltip": "Create a new file."
            },
            "Open": {
                "icon": "open",
                "command": "open_file",
                "row": 1,
                "column": 1,
                "statustip": "&Open",
                "tooltip": "Open an existing file."
            }
        },
        "Edit": {
            "order": []
        },
        "View": {
            "order": []
        },
        "Zoom": {
            "order": []
        },
        "Pan": {
            "order": []
        },
        "Icon": {
            "order": []
        },
        "Help": {
            "order": []
        },
        "Layer": {
            "order": []
        },
        "Text": {
            "order": []
        },
        "Properties": {
            "order": []
        },
        "Other": {
            "order": []
        
        }
    },
    "symbols": {
        "zero": "",
        "one": "",
        "two": "",
        "three": "",
        "four": "",
        "five": "",
        "six": "",
        "seven": "",
        "eight": "",
        "nine": "",
        "minus": "",
        "apostrophe": "",
        "quote": ""
    },
    "toggles": {
        "snap": 0,
        "grid": 0,
        "ruler": 0,
        "ortho": 0,
        "polar": 0,
        "qsnap": 0,
        "qtrack": 0,
        "lwt": 0
    },
    "line_edits": {
        "arc_center_x": "",
        "arc_center_y": "",
        "arc_radius": "",
        "arc_start_angle": "",
        "arc_end_angle": "",
        "arc_start_x": "",
        "arc_start_y": "",
        "arc_end_x": "",
        "arc_end_y": "",
        "arc_area": "",
        "ARC_LENGTH": "",
        "ARC_CHORD": "",
        "ARC_INC_ANGLE": "",
        "TEXT_SINGLE_CONTENTS": "",
        "TEXT_SINGLE_HEIGHT": "",
        "TEXT_SINGLE_ROTATION": "",
        "TEXT_SINGLE_X": "",
        "TEXT_SINGLE_Y": "",
        "CIRCLE_CENTER_X": "",
        "CIRCLE_CENTER_Y": "",
        "CIRCLE_RADIUS": "",
        "CIRCLE_DIAMETER": "",
        "CIRCLE_AREA": "",
        "CIRCLE_CIRCUMFERENCE": "",
        "ELLIPSE_CENTER_X": "",
        "ELLIPSE_CENTER_Y": "",
        "ELLIPSE_RADIUS_MAJOR": "",
        "ELLIPSE_RADIUS_MINOR": "",
        "ELLIPSE_DIAMETER_MAJOR": "",
        "ELLIPSE_DIAMETER_MINOR": "",
        "IMAGE_X": "",
        "IMAGE_Y": "",
        "IMAGE_WIDTH": "",
        "IMAGE_HEIGHT": "",
        "IMAGE_NAME": "",
        "IMAGE_PATH": "",
        "INFINITE_LINE_X1": "",
        "INFINITE_LINE_Y1": "",
        "INFINITE_LINE_X2": "",
        "INFINITE_LINE_Y2": "",
        "INFINITE_LINE_VECTOR_X": "",
        "INFINITE_LINE_VECTOR_Y": "",
        "BLOCK_X": "",
        "BLOCK_Y": "",
        "LINE_START_X": "",
        "LINE_START_Y": "",
        "LINE_END_X": "",
        "LINE_END_Y": "",
        "LINE_DELTA_X": "",
        "LINE_DELTA_Y": "",
        "LINE_ANGLE": "",
        "LINE_LENGTH": "",
        "POLYGON_CENTER_X": "",
        "POLYGON_CENTER_Y": "",
        "POLYGON_RADIUS_VERTEX": "",
        "POLYGON_RADIUS_SIDE": "",
        "POLYGON_DIAMETER_VERTEX": "",
        "POLYGON_DIAMETER_SIDE": "",
        "POLYGON_INTERIOR_ANGLE": "",
        "RECT_CORNER_X1": "",
        "RECT_CORNER_Y1": "",
        "RECT_CORNER_X2": "",
        "RECT_CORNER_Y2": "",
        "RECT_CORNER_X3": "",
        "RECT_CORNER_Y3": "",
        "RECT_CORNER_X4": "",
        "RECT_CORNER_Y4": "",
        "RECT_HEIGHT": "",
        "RECT_WIDTH": "",
        "RECT_AREA": "",
        "POINT_X": "",
        "POINT_Y": ""
    },
    "shortcuts": {
        "Ctrl+N": "new_file",
        "Ctrl+O": "open_file",
        "Ctrl+S": "save_file",
        "Ctrl+Shift+S": "save_as_file",
        "Ctrl+P": "print",
        "Ctrl+D": "design_details",
        "Ctrl+Q": "exit_program",
        "Ctrl+X": "cut_object",
        "Ctrl+C": "copy_object",
        "Ctrl+V": "paste_object",
        "Ctrl+Z": "undo",
        "Ctrl+Shift+Z": "redo",
        "F1": "help",
        "F2": "about"
    },
    "tips": [
        "we need more tips?",
        "you can change the color of the display through settings?",
        "you can hide the scrollbars to increase the viewable area through settings?",
        "you can change the icon size for increased visibility?",
        "you can toggle the grid on and off by pressing the button in the statusbar?",
        "the grid size can be changed to match your hoop size through settings?",
        "the crosshair size is based on a percentage of your screen size? Setting it to 100 may help you visually line things up better.",
        "you can pan by pressing the middle mouse button and dragging your mouse across the screen?",
        "you can open and edit multiple designs simultaneously?",
        "that many embroidery machines support the .dst format?",
        "that you can zoom in and out using your mouse wheel?",
        "that you can use circular and isometric grids?",
        "about our command line format converter?",
        "that you can use the 'DAY' and 'NIGHT' commands to quickly switch the view colors to commonly used white or black?",
        "that you can quickly change the background, crosshair and grid colors using the 'RGB' command?",
    ],
    "translation_table": {
    
    },
    "folders": [
        "",
        "commands",
        "help",
        "icons",
        "images",
        "samples",
        "translations"
    ],
    "details_label_text": [
        "Total Stitches:",
        "Real Stitches:",
        "Jump Stitches:",
        "Trim Stitches:",
        "Total Colors:",
        "Color Changes:",
        "Left:",
        "Top:",
        "Right:",
        "Bottom:",
        "Width:",
        "Height:"
    ],
    "obj_names": [
        "Unknown",
        "Base",
        "Arc",
        "Block",
        "Circle",
        "Aligned Dimension",
        "Angular Dimension",
        "Arc Length Dimension",
        "Diameter Dimension",
        "Leader Dimension",
        "Linear Dimension",
        "Ordinate Dimension",
        "Radius Dimension",
        "Ellipse",
        "Elliptical Arc",
        "Rubber",
        "Grid",
        "Hatch",
        "Image",
        "Infinite Line",
        "Line",
        "Path",
        "Point",
        "Polygon",
        "Polyline",
        "Ray",
        "Rectangle",
        "Slot",
        "Spline",
        "Multi Line Text",
        "Single Line Text",
        "Unknown"
    ],
    "status_bar_label": [
        "SNAP",
        "GRID",
        "RULER",
        "ORTHO",
        "POLAR",
        "QSNAP",
        "QTRACK",
        "LWT"
    ],
    "settings_tabs": [
        "General",
        "Files/Path",
        "Display",
        "Open/Save",
        "Printing",
        "Snap",
        "Grid/Ruler",
        "Ortho/Polar",
        "QuickSnap",
        "QuickTrack",
        "LineWeight",
        "Selection"
    ],
    "origin_string": [
        "M 0.0 0.5",
        "A -0.5 -0.5 1.0 1.0 90.0 360.0",
        "A -0.5 -0.5 1.0 1.0 90.0 -360.0",
        "L 0.0 -0.5",
        "A -0.5 -0.5 1.0 1.0 270.0 90.0",
        "L -0.5 0.0",
        "A -0.5 -0.5 1.0 1.0 180.0 -90.0",
        "Z"
    ]
}


