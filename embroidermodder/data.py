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

"""

# LineEdits
ARC_CENTER_X                   0
ARC_CENTER_Y                   1
ARC_RADIUS                     2
ARC_START_ANGLE                3
ARC_END_ANGLE                  4
ARC_START_X                    5
ARC_START_Y                    6
ARC_END_X                      7
ARC_END_Y                      8
ARC_AREA                       9
ARC_LENGTH                    10
ARC_CHORD                     11
ARC_INC_ANGLE                 12
TEXT_SINGLE_CONTENTS          13
TEXT_SINGLE_HEIGHT            14
TEXT_SINGLE_ROTATION          15
TEXT_SINGLE_X                 16
TEXT_SINGLE_Y                 17
CIRCLE_CENTER_X               18
CIRCLE_CENTER_Y               19
CIRCLE_RADIUS                 20
CIRCLE_DIAMETER               21
CIRCLE_AREA                   22
CIRCLE_CIRCUMFERENCE          23
ELLIPSE_CENTER_X              24
ELLIPSE_CENTER_Y              25
ELLIPSE_RADIUS_MAJOR          26
ELLIPSE_RADIUS_MINOR          27
ELLIPSE_DIAMETER_MAJOR        28
ELLIPSE_DIAMETER_MINOR        29
IMAGE_X                       30
IMAGE_Y                       31
IMAGE_WIDTH                   32
IMAGE_HEIGHT                  33
IMAGE_NAME                    34
IMAGE_PATH                    35
INFINITE_LINE_X1              36
INFINITE_LINE_Y1              37
INFINITE_LINE_X2              38
INFINITE_LINE_Y2              39
INFINITE_LINE_VECTOR_X        40
INFINITE_LINE_VECTOR_Y        41
BLOCK_X                       42
BLOCK_Y                       43
LINE_START_X                  44
LINE_START_Y                  45
LINE_END_X                    46
LINE_END_Y                    47
LINE_DELTA_X                  48
LINE_DELTA_Y                  49
LINE_ANGLE                    50
LINE_LENGTH                   51
POLYGON_CENTER_X              52
POLYGON_CENTER_Y              53
POLYGON_RADIUS_VERTEX         54
POLYGON_RADIUS_SIDE           55
POLYGON_DIAMETER_VERTEX       56
POLYGON_DIAMETER_SIDE         57
POLYGON_INTERIOR_ANGLE        58
RECT_CORNER_X1                59
RECT_CORNER_Y1                60
RECT_CORNER_X2                61
RECT_CORNER_Y2                62
RECT_CORNER_X3                63
RECT_CORNER_Y3                64
RECT_CORNER_X4                65
RECT_CORNER_Y4                66
RECT_HEIGHT                   67
RECT_WIDTH                    68
RECT_AREA                     69
POINT_X                       70
POINT_Y                       71
LINEEDIT_PROPERTY_EDITORS     72

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


"""

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
ACTION_exit                =   7
ACTION_cut                 =   8
ACTION_copy                =   9
ACTION_paste               =  10
ACTION_undo                =  11
ACTION_redo                =  12
# Window Menu */
ACTION_windowclose         =  13
ACTION_windowcloseall      =  14
ACTION_windowcascade       =  15
ACTION_windowtile          =  16
ACTION_windownext          =  17
ACTION_windowprevious      =  18
# Help Menu */
ACTION_help                =  19
ACTION_changelog           =  20
ACTION_tipoftheday         =  21
ACTION_about               =  22
ACTION_whatsthis           =  23
# Icons */
ACTION_icon16              =  24
ACTION_icon24              =  25
ACTION_icon32              =  26
ACTION_icon48              =  27
ACTION_icon64              =  28
ACTION_icon128             =  29
ACTION_settingsdialog      =  30
# Layer ToolBar */
ACTION_makelayercurrent    =  31
ACTION_layers              =  32
ACTION_layerselector       =  33
ACTION_layerprevious       =  34
ACTION_colorselector       =  35
ACTION_linetypeselector    =  36
ACTION_lineweightselector  =  37
ACTION_hidealllayers       =  38
ACTION_showalllayers       =  39
ACTION_freezealllayers     =  40
ACTION_thawalllayers       =  41
ACTION_lockalllayers       =  42
ACTION_unlockalllayers     =  43
# Text ToolBar */
ACTION_textbold            =  44
ACTION_textitalic          =  45
ACTION_textunderline       =  46
ACTION_textstrikeout       =  47
ACTION_textoverline        =  48
# Zoom ToolBar */
ACTION_zoomrealtime        =  49
ACTION_zoomprevious        =  50
ACTION_zoomwindow          =  51
ACTION_zoomdynamic         =  52
ACTION_zoomscale           =  53
ACTION_zoomcenter          =  54
ACTION_zoomin              =  55
ACTION_zoomout             =  56
ACTION_zoomselected        =  57
ACTION_zoomall             =  58
ACTION_zoomextents         =  59
# Pan SubMenu */
ACTION_panrealtime         =  60
ACTION_panpoint            =  61
ACTION_panleft             =  62
ACTION_panright            =  63
ACTION_panup               =  64
ACTION_pandown             =  65
# View */
ACTION_day                 =  66
ACTION_night               =  67

# Just added */
ACTION_trebleclef          =  68
ACTION_path                =  69
ACTION_circle              =  70
ACTION_line                =  71
ACTION_distance            =  72
ACTION_dolphin             =  73
ACTION_ellipse             =  74
ACTION_delete              =  75
ACTION_heart               =  76
ACTION_locatepoint         =  77
N_ACTIONS                  =  78

layout = {
    "title": "Embroidermodder 2.0",
    "width": 640,
    "height": 480,
    "MAX_STRING_LENGTH": 500,
    "menubar": {
        "order": [
            "File", "Edit", "View", "Settings", "Window", "Help", "Recent",
            "Zoom", "Pan"
        ],
        "File": {
            "New": "new",
            "Open...": "open",
            "Save...": "save",
            "Save As...": "saveas",
            "Exit": "exit"
        },
        "Edit": {
            "Cut": "cut",
            "Copy": "copy",
            "Paste": "paste"
        },
        "View": {
        },
        "Settings": {
        },
        "Window": {
        },
        "Help": {
        },
        "Recent": {
        },
        "Zoom": {
        },
        "Pan": {
        }
    },
    "toolbar": {
        "File": {
            "New": {
                "icon": new_xpm,
                "command": "new",
                "row": 1,
                "column": 0,
                "statustip": "&New",
                "tooltip": "Create a new file."
            },
            "Open": {
                "command": "open",
                "row": 1,
                "column": 1,
                "statustip": "&Open",
                "tooltip": "Open an existing file."
            }
        },
        "Edit": {
        },
        "View": {
        },
        "Zoom": {
        },
        "Pan": {
        },
        "Icon": {
        },
        "Help": {
        },
        "Layer": {
        },
        "Text": {
        },
        "Properties": {
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
        "arc_center_y": ""
    },
    "shortcuts": {
        "Ctrl+N": "new",
        "Ctrl+O": "open",
        "Ctrl+S": "save",
        "Ctrl+Shift+S": "saveas",
        "Ctrl+P": "print",
        "Ctrl+D": "details",
        "Ctrl+Q": "exit",
        "Ctrl+X": "cut",
        "Ctrl+C": "copy",
        "Ctrl+V": "paste",
        "Ctrl+Z": "undo",
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
    
    }
}


details_label_text = [
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
]


obj_names = [
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
]

status_bar_label = [
    "SNAP",
    "GRID",
    "RULER",
    "ORTHO",
    "POLAR",
    "QSNAP",
    "QTRACK",
    "LWT"
]


folders = [
    "",
    "commands",
    "help",
    "icons",
    "images",
    "samples",
    "translations"
]


settings_tab_label = [
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
]


origin_string = [
    "M 0.0 0.5",
    "A -0.5 -0.5 1.0 1.0 90.0 360.0",
    "A -0.5 -0.5 1.0 1.0 90.0 -360.0",
    "L 0.0 -0.5",
    "A -0.5 -0.5 1.0 1.0 270.0 90.0",
    "L -0.5 0.0",
    "A -0.5 -0.5 1.0 1.0 180.0 -90.0",
    "Z",
    "\0"
]

