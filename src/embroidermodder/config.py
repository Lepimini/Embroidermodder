#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENSE for licensing terms.

    ------------------------------------------------------------

    This folder is for the configuration for Embroidermodder 2.
    There is no code, only data in this folder.

    So we don't have to load this from file on the first run
    the settings are all laid out in a single JSON style dict.
    This dict called "settings" is constructed from smaller
    data structures in the other files of this folder.

    It makes specific pieces of config easier to find while
    allowing the program to run without installing.

    ------------------------------------------------------------

    Configuration: so we don't have to load this from file on
    the first run. It makes packaging more straight-forward.

    Also this means that we can run without installing.
"""

from embroidermodder.icons import icons

settings = {
    "welcome_message": r"""
     ___ _____ ___  ___   __  _ ___  ___ ___   _____  __  ___  ___  ___ ___    ___ 
    | __|     | _ \| _ \ /  \| |   \| __| _ \ |     |/  \|   \|   \| __| _ \  |__ \
    | __| | | | _ <|   /| () | | |) | __|   / | | | | () | |) | |) | __|   /  / __/
    |___|_|_|_|___/|_|\_\\__/|_|___/|___|_|\_\|_|_|_|\__/|___/|___/|___|_|\_\ |___|
    _____________________________________________________________________________ 
    |                                                                             |
    |                         http://embroidermodder.org                          |
    |_____________________________________________________________________________|

    Usage: embroidermodder [options] files ...

    Options:
    -d, --debug      Print lots of debugging information.
    -h, --help       Print self message and exit.
    -v, --version    Print the version number of embroidermodder and exit.
    """,
    "to_add_to_property_editor": """
    
    toolbar = ToolBar[10]
    menu = Menu[10]
    status_bar = toolButton = [
        tk.Button() for i in range(8)
    ]
    toolButton = [
        tk.Button() for i in range(PROPERTY_EDITORS)
    ]
    lineEdit = [
        tk.LineEdit() for i in range(LINEEDIT_PROPERTY_EDITORS)
    ]
    comboBox =  [
        tk.ComboBox() for i in range(COMBOBOX_PROPERTY_EDITORS)
    ]

    opensave_recent_list_of_files = []
    opensave_custom_filter = ""

    toolButtonTextSingleHeight =
    toolButtonTextSingleRotation = tk.Button()

    text_single_editors = {
        "contents": {
            "entry": tk.LineEdit(),
            "toolbutton": tk.Button()
        },
        "font": [tk.FontComboBox(), tk.Button()],
        "justify": [tk.ComboBox(), tk.Button()],
        "height": [tk.LineEdit(), tk.Button()],
        "rotation": [tk.LineEdit(), tk.Button()]
    }

    ToolButton toolButtonGeneralLayer
    ToolButton toolButtonGeneralColor
    ToolButton toolButtonGeneralLineType
    ToolButton toolButtonGeneralLineWeight

    ComboBox comboBoxGeneralLayer
    ComboBox comboBoxGeneralColor
    ComboBox comboBoxGeneralLineType
    ComboBox comboBoxGeneralLineWeight

    ToolButton toolButtonImageX
    ToolButton toolButtonImageY
    ToolButton toolButtonImageWidth
    ToolButton toolButtonImageHeight

    LineEdit lineEditImageX
    LineEdit lineEditImageY
    LineEdit lineEditImageWidth
    LineEdit lineEditImageHeight

    GroupBox groupBoxMiscImage

    ToolButton toolButtonImageName
    ToolButton toolButtonImagePath

    LineEdit lineEditImageName
    LineEdit lineEditImagePath

    ToolButton toolButtonPolygonCenterX
    ToolButton toolButtonPolygonCenterY
    ToolButton toolButtonPolygonRadiusVertex
    ToolButton toolButtonPolygonRadiusSide
    ToolButton toolButtonPolygonDiameterVertex
    ToolButton toolButtonPolygonDiameterSide
    ToolButton toolButtonPolygonInteriorAngle

    LineEdit lineEditPolygonCenterX
    LineEdit lineEditPolygonCenterY
    LineEdit lineEditPolygonRadiusVertex
    LineEdit lineEditPolygonRadiusSide
    LineEdit lineEditPolygonDiameterVertex
    LineEdit lineEditPolygonDiameterSide
    LineEdit lineEditPolygonInteriorAngle

    EmbVector pasteDelta
    Vector scenePressPoint
    Point pressPoint
    Vector sceneMovePoint
    Point movePoint
    Vector sceneReleasePoint
    Point releasePoint
    Vector sceneGripPoint

    Color rulerColor

    Point  viewMousePoint
    EmbVector sceneMousePoint
    unsigned int snapLocatorColor
    unsigned int gripColorCool
    unsigned int gripColorHot
    unsigned int crosshairColor
    int precisionAngle
    int precisionLength

    Label status_bar_mouse_coord

    ToolButton toolButtonInfiniteLineX1
    ToolButton toolButtonInfiniteLineY1
    ToolButton toolButtonInfiniteLineX2
    ToolButton toolButtonInfiniteLineY2
    ToolButton toolButtonInfiniteLineVectorX
    ToolButton toolButtonInfiniteLineVectorY

    LineEdit lineEditInfiniteLineX1
    LineEdit lineEditInfiniteLineY1
    LineEdit lineEditInfiniteLineX2
    LineEdit lineEditInfiniteLineY2
    LineEdit lineEditInfiniteLineVectorX
    LineEdit lineEditInfiniteLineVectorY

    #Used when checking if fields vary
    fieldOldText = ""
    fieldNewText = ""
    fieldVariesText = ""
    fieldYesText = ""
    fieldNoText = ""
    fieldOnText = ""
    fieldOffText = ""

    ToolButton toolButtonArcClockwise
    ComboBox comboBoxArcClockwise

    GroupBox groupBoxGeometry[32]
    GroupBox groupBoxGeneral
    GroupBox groupBoxMiscArc
    GroupBox groupBoxMiscPath
    GroupBox groupBoxMiscPolyline
    GroupBox groupBoxTextTextSingle
    GroupBox groupBoxMiscTextSingle

    ToolButton toolButtonBlockX
    ToolButton toolButtonBlockY

    LineEdit lineEditBlockX
    LineEdit lineEditBlockY

    ToolButton toolButtonPathVertexNum
    ToolButton toolButtonPathVertexX
    ToolButton toolButtonPathVertexY
    ToolButton toolButtonPathArea
    ToolButton toolButtonPathLength

    ComboBox comboBoxPathVertexNum
    LineEdit lineEditPathVertexX
    LineEdit lineEditPathVertexY
    LineEdit lineEditPathArea
    LineEdit lineEditPathLength

    ToolButton toolButtonPathClosed

    ComboBox comboBoxPathClosed

    ToolButton toolButtonPolylineVertexNum
    ToolButton toolButtonPolylineVertexX
    ToolButton toolButtonPolylineVertexY
    ToolButton toolButtonPolylineArea
    ToolButton toolButtonPolylineLength

    ComboBox comboBoxPolylineVertexNum
    LineEdit lineEditPolylineVertexX
    LineEdit lineEditPolylineVertexY
    LineEdit lineEditPolylineArea
    LineEdit lineEditPolylineLength

    ToolButton toolButtonPolylineClosed

    ComboBox comboBoxPolylineClosed

    ToolButton toolButtonRayX1
    ToolButton toolButtonRayY1
    ToolButton toolButtonRayX2
    ToolButton toolButtonRayY2
    ToolButton toolButtonRayVectorX
    ToolButton toolButtonRayVectorY

    LineEdit lineEditRayX1
    LineEdit lineEditRayY1
    LineEdit lineEditRayX2
    LineEdit lineEditRayY2
    LineEdit lineEditRayVectorX
    LineEdit lineEditRayVectorY

    ToolButton toolButtonTextMultiX
    ToolButton toolButtonTextMultiY

    lineEditTextMultiX = LineEdit()
    lineEditTextMultiY = LineEdit()

    ToolButton toolButtonTextSingleX
    ToolButton toolButtonTextSingleY

    LineEdit lineEditTextSingleX
    LineEdit lineEditTextSingleY

    ToolButton toolButtonTextSingleBackward
    ToolButton toolButtonTextSingleUpsideDown

    ComboBox comboBoxTextSingleBackward
    ComboBox comboBoxTextSingleUpsideDown
    """,
    "title": "Embroidermodder",
    "version": "2.0-alpha-2",
    "DEBUG_MODE": 0,
    "width": 640,
    "height": 480,
    "MAX_STRING_LENGTH": 500,
    "MAX_DISTANCE": 1000000.0,
    "window_width": 640,
    "window_height": 480,
    "window_x": 100,
    "window_y": 100,
    "general_icon_size": 16,
    "general_mdi_bg_use_logo": 0,
    "general_mdi_bg_use_texture": 0,
    "general_mdi_bg_use_color": 0,
    "qsnap_endpoint": 0,
    "qsnap_midpoint": 0,
    "qsnap_center": 0,
    "qsnap_node": 0,
    "qsnap_quadrant": 0,
    "qsnap_intersection": 0,
    "qsnap_extension": 0,
    "qsnap_insertion": 0,
    "qsnap_perpendicular": 0,
    "qsnap_tangent": 0,
    "qsnap_nearest": 0,
    "qsnap_apparent": 0,
    "qsnap_parallel": 0,
    "grid_center_on_origin": 0,
    "grid_center": [0.5, 0.5],
    "grid_size": [10.0, 10.0],
    "grid_spacing": [10.0, 10.0],
    "grid_size_radius": 10.0,
    "grid_spacing_radius": "",
    "grid_spacing_angle": "",
    "ruler_show_on_load": "",
    "ruler_metric": "",
    "general_tip_of_the_day": "",
    "general_system_help_browser": "",
    "general_check_for_updates": "",
    "display_use_opengl": "",
    "display_renderhint_aa": "",
    "display_renderhint_text_aa": "",
    "display_renderhint_smooth_pix": "",
    "display_renderhint_high_aa": "",
    "display_renderhint_noncosmetic": "",
    "display_show_scrollbars": "",
    "display_scrollbar_widget_num": "",
    "display_zoomscale_in": "",
    "display_zoomscale_out": "",
    "display_selectbox_alpha": "",
    "display_crosshair_percent": "",
    "opensave_open_thumbnail": "",
    "opensave_save_thumbnail": "",
    "opensave_recent_max_files": "",
    "opensave_trim_dst_num_jumps": "",
    "printing_use_last_device": "",
    "printing_disable_bg": "",
    "grid_show_on_load": "",
    "grid_show_origin": "",
    "grid_color_match_crosshair": "",
    "grid_load_from_file": "",
    "ruler_pixel_size": "",
    "qsnap_enabled": "",
    "qsnap_locator_size": "",
    "qsnap_aperture_size": "",
    "lwt_show_lwt": 0,
    "lwt_real_render": 0,
    "lwt_default_lwt": 1.0,
    "selection_mode_pickfirst": "",
    "selection_mode_pickadd": "",
    "selection_mode_pickdrag": "",
    "selection_grip_size": "",
    "selection_pickbox_size": "",
    "text_style_bold": 0,
    "text_style_italic": 0,
    "text_style_underline": 0,
    "text_style_strikethrough": 0,
    "rulerPixelSize": "",
    "gripSize": "",
    "pickBoxSize": "",
    "crosshairSize": "",
    "shiftKeyPressedState": "",
    "grippingActive": "",
    "rapidMoveActive": "",
    "previewActive": "",
    "pastingActive": "",
    "movingActive": "",
    "selectingActive": "",
    "zoomWindowActive": "",
    "panningRealTimeActive": "",
    "panningPointActive": "",
    "panningActive": "",
    "qSnapActive": 0,
    "qSnapToggle": 0,
    "rulerMetric": 1,
    "general_language": "default",
    "general_icon_theme": "default",
    "general_mdi_bg_logo": "",
    "general_mdi_bg_texture": "",
    "general_mdi_bg_color": "",
    "general_current_tip": "",
    "display_crosshair_color": "",
    "display_bg_color": "",
    "display_selectbox_left_color": "",
    "display_selectbox_left_fill": "",
    "display_selectbox_right_color": "",
    "display_selectbox_right_fill": "",
    "display_units": "",
    "opensave_open_format": "",
    "opensave_save_format": "",
    "opensave_recent_directory": "",
    "printing_default_device": "",
    "grid_color": "",
    "ruler_color": "",
    "qsnap_locator_color": "#FFFFFF",
    "grid_type": "cartesian",
    "selection_coolgrip_color": "#FFFFFF",
    "selection_hotgrip_color": "#FFFFFF",
    "text_font": "arial",
    "BUILD_GIT_HASH": "92403820fc2c6be46b884b6500e01a239363fc82",
    "translation_table": {
        "?": {
            "French": "?",
            "German": "?",
            "Spanish": "?"
        }
    },
    "circle_modes": [
        "1P_RAD",
        "1P_DIA",
        "2P",
        "3P",
        "TTR"
    ],
    "folders": [
        "",
        "commands",
        "help",
        "icons",
        "images",
        "samples",
        "translations"
    ],
    "todo_actions": [
        "ACTION_spellcheck",
        "ACTION_quickselect"
    ],
    "dolphin_modes": [
        "NUM_POINTS",
        "XSCALE",
        "YSCALE"
    ],
    "ellipse_modes": [
        "MAJORDIAMETER_MINORRADIUS",
        "MAJORRADIUS_MINORRADIUS",
        "ROTATION"
    ],
    "polygon_modes": [
        "NUM_SIDES",
        "CENTER_PT",
        "POLYTYPE",
        "INSCRIBE",
        "CIRCUMSCRIBE",
        "DISTANCE",
        "SIDE_LEN"
    ],
    "treble_clef_modes": [
        "NUM_POINTS",
        "XSCALE",
        "YSCALE"
    ],
    "path_types": [
        "MOVETO",
        "LINETO",
        "ARCTO",
        "ARCMOVETO",
        "ELLIPSE",
        "END"
    ],
    "permissions": [
        "USER",
        "PROGRAM",
        "ADMIN"
    ],
    "symbol_scale": 0.01,
    "symbols_docstring": [
        "Symbols use the SVG path syntax.",
        "",
        "In theory, we could combine the icons and symbols systems,",
        "since they could be rendered once and stored as icons in Qt.",
        "(Or as textures in FreeGLUT.)",
        "",
        "Also we want to render the patterns themselves using SVG",
        "syntax, so it would save on repeated work overall."
    ],
    "symbol_list": {
        "0": [
            "/* path.addEllipse(Vector(x+0.25*xs, y-0.50*ys),",
            "    0.25*xs, 0.50*ys);*/",
            "M 0 -0.75",
            "L 0 -0.25",
            "A 0 -0.5 0.5 0.5 180.0 180.0",
            "L 0.5, -0.75",
            "A 0 -1.0, 0.5, 0.5, 0.0, 180.0"
        ],
        "1": "M 5 100 L 45 100 M 0 25 L 25 0 L 25 100",
        "2": "icon 2",
        "3": "icon 3",
        "4": "M 50 100 L 50 0 L 0 50 L 50 50",
        "5": "icon 5",
        "6": "icon 6",
        "7": "M 0 0 L 50 0 L 25 75 L 25 100",
        "8": "icon 8",
        "9": "icon 9",
        "-": "M 0 50 L 50 50",
        "'": "M 25 100 L 25 25",
        "\"": "M 10 0 L 10 25 M 40 0 L 40 25"
    },
    "preview_modes": [
        "null",
        "move",
        "rotate",
        "scale"
    ],
    "thread_weights": [
        ["lineweightbylayer.png", "ByLayer", -2.00],
        ["lineweightbyblock.png", "ByBlock", -1.00],
        ["lineweightdefault.png", "Default", 0.00],
        ["lineweight01.png", "0.00 mm", 0.00],
        ["lineweight02.png", "0.05 mm", 0.05],
        ["lineweight03.png", "0.15 mm", 0.15],
        ["lineweight04.png", "0.20 mm", 0.20],
        ["lineweight05.png", "0.25 mm", 0.25],
        ["lineweight06.png", "0.30 mm", 0.30],
        ["lineweight07.png", "0.35 mm", 0.35],
        ["lineweight08.png", "0.40 mm", 0.40],
        ["lineweight09.png", "0.45 mm", 0.45],
        ["lineweight10.png", "0.50 mm", 0.50],
        ["lineweight11.png", "0.55 mm", 0.55],
        ["lineweight12.png", "0.60 mm", 0.60],
        ["lineweight13.png", "0.65 mm", 0.65],
        ["lineweight14.png", "0.70 mm", 0.70],
        ["lineweight15.png", "0.75 mm", 0.75],
        ["lineweight16.png", "0.80 mm", 0.80],
        ["lineweight17.png", "0.85 mm", 0.85],
        ["lineweight18.png", "0.90 mm", 0.90],
        ["lineweight19.png", "0.95 mm", 0.95],
        ["lineweight20.png", "1.00 mm", 1.00],
        ["lineweight21.png", "1.05 mm", 1.05],
        ["lineweight22.png", "1.10 mm", 1.10],
        ["lineweight23_xpm", "1.15 mm", 1.15],
        ["lineweight24_png", "1.20 mm", 1.20]
    ],
    "actions": [
        "do_nothing",
        "new_file",
        "open_file",
        "save_file",
        "save_as_file",
        "print",
        "design_details",
        "exit_program",
        "cut",
        "copy",
        "paste",
        "undo",
        "redo",
        "window_close",
        "window_close_all",
        "windowCascade",
        "windowtile",
        "windownext",
        "windowprevious",
        "help",
        "changelog",
        "tipoftheday",
        "about",
        "whatsthis",
        "icon16",
        "icon24",
        "icon32",
        "icon48",
        "icon64",
        "icon128",
        "settingsdialog",
        "makelayercurrent",
        "layers",
        "layerselector",
        "layerprevious",
        "colorselector",
        "linetypeselector",
        "lineweightselector",
        "hidealllayers",
        "showalllayers",
        "freezealllayers",
        "thawalllayers",
        "lockalllayers",
        "unlockalllayers",
        "textbold",
        "textitalic",
        "textunderline",
        "textstrikeout",
        "textoverline",
        "zoomrealtime",
        "zoomprevious",
        "zoomwindow",
        "zoomdynamic",
        "zoomscale",
        "zoomcenter",
        "zoomin",
        "zoomout",
        "zoomselected",
        "zoomall",
        "zoomextents",
        "panrealtime",
        "panpoint",
        "panleft",
        "panright",
        "panup",
        "pandown",
        "day",
        "night",
        "trebleclef",
        "path",
        "circle",
        "line",
        "distance",
        "dolphin",
        "ellipse",
        "delete",
        "heart",
        "locatepoint"
    ],
    "menu_bar": {
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
            "order": [
                "New",
                "---",
                "Open...",
                "---",
                "Save...",
                "Save As...",
                "---",
                "Print",
                "---",
                "Design Details",
                "---",
                "Exit"
            ],
            "tearoff": 0,
            "---": "do_nothing",
            "New": "new_file",
            "Open...": "open_file",
            "Save...": "save_file",
            "Save As...": "save_as_file",
            "Print": "main_print",
            "Design Details": "design_details",
            "Help": "main_help",
            "Exit": "exit_program"
        },
        "Edit": {
            "order": [
                "Undo",
                "Redo",
                "---",
                "Cut",
                "Copy",
                "Paste"
            ],
            "tearoff": 1,
            "---": "do_nothing",
            "Undo": "main_undo",
            "Redo": "main_redo",
            "Cut": "cut_object",
            "Copy": "copy_object",
            "Paste": "paste_object"
        },
        "View": {
            "order": [
                "Day",
                "Night",
                "---",
                "Icon 16",
                "Icon 24",
                "Icon 32",
                "Icon 48",
                "Icon 64",
                "Icon 128"
            ],
            "tearoff": 1,
            "---": "do_nothing",
            "Day": "day_vision",
            "Night": "night_vision",
            "Icon 16": "icon16",
            "Icon 24": "icon24",
            "Icon 32": "icon32",
            "Icon 48": "icon48",
            "Icon 64": "icon64",
            "Icon 128": "icon128"
        },
        "Settings": {
            "order": [
                "Preferences..."
            ],
            "tearoff": 1,
            "Preferences...": "settings_dialog"
        },
        "Window": {
            "order": [],
            "tearoff": 1
        },
        "Help": {
            "order": [
                "Help",
                "---",
                "Changelog",
                "---",
                "Tip of the Day",
                "---",
                "About",
                "---",
                "What's This?"
            ],
            "tearoff": 1,
            "---": "do_nothing",
            "Help": "do_nothing",
            "Changelog": "do_nothing",
            "Tip of the Day": "do_nothing",
            "About": "do_nothing",
            "What's This?": "do_nothing"
        },
        "Recent": {
            "order": [],
            "tearoff": 1,
            "---": "do_nothing"
        },
        "Zoom": {
            "order": [
                "Zoom Real Time",
                "Zoom Previous",
                "---",
                "Zoom Window",
                "Zoom Dynamic",
                "Zoom Scale",
                "Zoom Center",
                "---",
                "Zoom In",
                "Zoom Out",
                "---",
                "Zoom Selected",
                "Zoom All",
                "Zoom Extents"
            ],
            "tearoff": 1,
            "icon": "zoom-16.png",
            "---": "do_nothing",
            "Zoom Real Time": "do_nothing",
            "Zoom Previous": "do_nothing",
            "Zoom Window": "do_nothing",
            "Zoom Dynamic": "do_nothing",
            "Zoom Scale": "do_nothing",
            "Zoom Center": "do_nothing",
            "Zoom In": "do_nothing",
            "Zoom Out": "do_nothing",
            "Zoom Selected": "do_nothing",
            "Zoom All": "do_nothing",
            "Zoom Extents": "do_nothing"
        },
        "Pan": {
            "order": [
                "Pan Real Time",
                "Pan Point",
                "---",
                "Pan Left",
                "Pan Right",
                "Pan Up",
                "Pan Down"
            ],
            "tearoff": 1,
            "---": "do_nothing",
            "Pan Real Time": "do_nothing",
            "Pan Point": "do_nothing",
            "Pan Left": "do_nothing",
            "Pan Right": "do_nothing",
            "Pan Up": "do_nothing",
            "Pan Down": "do_nothing"
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
                "Open",
                "Save",
                "Save as",
                "Print",
                "Design Details",
                "Help"
            ],
            "New": {
                "icon": "new-16.png",
                "command": "newFile",
                "row": 1,
                "column": 0,
                "statustip": "&New",
                "tooltip": "Create a new file."
            },
            "Open": {
                "icon": "open-16.png",
                "command": "openFile",
                "row": 1,
                "column": 1,
                "statustip": "&Open",
                "tooltip": "Open an existing file."
            },
            "Save": {
                "icon": "save-16.png",
                "command": "saveFile",
                "row": 1,
                "column": 2,
                "statustip": "&Save",
                "tooltip": "Save the design to disk."
            },
            "Save as": {
                "icon": "saveas-16.png",
                "command": "saveAsFile",
                "row": 1,
                "column": 3,
                "statustip": "Save &As",
                "tooltip": "Save the design under a new name."
            },
            "Print": {
                "icon": "print-16.png",
                "command": "mainPrint",
                "row": 1,
                "column": 4,
                "statustip": "&Print",
                "tooltip": "Print the design."
            },
            "Design Details": {
                "icon": "histogram-16.png",
                "command": "designDetails",
                "row": 1,
                "column": 5,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Help": {
                "icon": "help-16.png",
                "command": "mainHelp",
                "row": 1,
                "column": 6,
                "statustip": "&Help",
                "tooltip": "Details of the current design."
            }
        },
        "Edit": {
            "order": [
                "Undo",
                "Redo",
                "Cut",
                "Copy",
                "Paste"
            ],
            "Undo": {
                "icon": "undo-16.png",
                "command": "mainUndo",
                "row": 1,
                "column": 7,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Redo": {
                "icon": "redo-16.png",
                "command": "designDetails",
                "row": 1,
                "column": 8,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Cut": {
                "icon": "cut-16.png",
                "command": "designDetails",
                "row": 1,
                "column": 9,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Copy": {
                "icon": "copy-16.png",
                "command": "designDetails",
                "row": 1,
                "column": 10,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Paste": {
                "icon": "paste-16.png",
                "command": "designDetails",
                "row": 1,
                "column": 11,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            }
        },
        "View": {
            "order": [
                "Day",
                "Night"
            ],
            "Day": {
                "icon": "day-16.png",
                "command": "dayVision",
                "row": 1,
                "column": 12,
                "statustip": "&Day",
                "tooltip": "Updates the current view using day vision settings."
            },
            "Night": {
                "icon": "night-16.png",
                "command": "nightVision",
                "row": 1,
                "column": 13,
                "statustip": "&Night",
                "tooltip": "Updates the current view using night vision settings."
            }
        },
        "Zoom": {
            "order": [
                "Zoom Window",
                "Zoom Dynamic",
                "Zoom Scale",
                "Zoom Center",
                "Zoom In",
                "Zoom Out",
                "Zoom Selected",
                "Zoom All",
                "Zoom Extents"
            ],
            "Zoom Window": {
                "icon": "icon16-16.png",
                "command": "icon16",
                "row": 2,
                "column": 0,
                "statustip": "Zoom Window",
                "tooltip": "Sets the toolbar icon size to 16x16."
            },
            "Zoom Dynamic": {
                "icon": "icon24-16.png",
                "command": "zoom_dynamic",
                "row": 2,
                "column": 1,
                "statustip": "Zoom Dynamic",
                "tooltip": "Sets the toolbar icon size to 24x24."
            },
            "Zoom Scale": {
                "icon": "zoom-16.png",
                "command": "zoom_scale",
                "row": 2,
                "column": 2,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Zoom Center": {
                "icon": "zoom-16.png",
                "command": "zoom_center",
                "row": 2,
                "column": 3,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Zoom In": {
                "icon": "zoom-16.png",
                "command": "icon64",
                "row": 2,
                "column": 4,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Zoom Out": {
                "icon": "icon128-16.png",
                "command": "icon128",
                "row": 2,
                "column": 5,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Zoom Selected": {
                "icon": "icon48-16.png",
                "command": "icon48",
                "row": 2,
                "column": 3,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Zoom All": {
                "icon": "icon64-16.png",
                "command": "icon64",
                "row": 2,
                "column": 4,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Zoom Extents": {
                "icon": "icon128-16.png",
                "command": "icon128",
                "row": 2,
                "column": 5,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            }
        },
        "Pan": {
            "order": [
                "Pan Real Time",
                "Pan Point",
                "Pan Left",
                "Pan Right",
                "Pan Up",
                "Pan Down"
            ],
            "Pan Real Time": {
                "icon": "icon16-16.png",
                "command": "icon16",
                "row": 2,
                "column": 0,
                "statustip": "Icon&16",
                "tooltip": "Sets the toolbar icon size to 16x16."
            },
            "Pan Point": {
                "icon": "icon24-16.png",
                "command": "icon24",
                "row": 2,
                "column": 1,
                "statustip": "Icon&24",
                "tooltip": "Sets the toolbar icon size to 24x24."
            },
            "Pan Left": {
                "icon": "icon32-16.png",
                "command": "icon32",
                "row": 2,
                "column": 2,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Pan Right": {
                "icon": "icon48-16.png",
                "command": "icon48",
                "row": 2,
                "column": 3,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Pan Up": {
                "icon": "icon64-16.png",
                "command": "icon64",
                "row": 2,
                "column": 4,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Pan Down": {
                "icon": "icon128-16.png",
                "command": "icon128",
                "row": 2,
                "column": 5,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            }
        },
        "Icon": {
            "order": [
                "Icon 16",
                "Icon 24",
                "Icon 32",
                "Icon 48",
                "Icon 64",
                "Icon 128"
            ],
            "Icon 16": {
                "icon": "icon16-16.png",
                "command": "icon16",
                "row": 2,
                "column": 0,
                "statustip": "Icon&16",
                "tooltip": "Sets the toolbar icon size to 16x16."
            },
            "Icon 24": {
                "icon": "icon24-16.png",
                "command": "icon24",
                "row": 2,
                "column": 1,
                "statustip": "Icon&24",
                "tooltip": "Sets the toolbar icon size to 24x24."
            },
            "Icon 32": {
                "icon": "icon32-16.png",
                "command": "icon32",
                "row": 2,
                "column": 2,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Icon 48": {
                "icon": "icon48-16.png",
                "command": "icon48",
                "row": 2,
                "column": 3,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Icon 64": {
                "icon": "icon64-16.png",
                "command": "icon64",
                "row": 2,
                "column": 4,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            },
            "Icon 128": {
                "icon": "icon128-16.png",
                "command": "icon128",
                "row": 2,
                "column": 5,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            }
        },
        "Help": {
            "order": [
                "Help",
                "Changelog",
                "About",
                "What's This?"
            ],
            "Help": {
                "icon": "help-16.png",
                "command": "help",
                "row": 2,
                "column": 0,
                "statustip": "&Help",
                "tooltip": "Opens the packaged help."
            },
            "Changelog": {
                "icon": "changelog-16.png",
                "command": "changelog",
                "row": 2,
                "column": 1,
                "statustip": "Changelog",
                "tooltip": "Opens a log of what has recently changed."
            },
            "About": {
                "icon": "about-16.png",
                "command": "about",
                "row": 2,
                "column": 4,
                "statustip": "&About",
                "tooltip": "Opens the about this software dialog."
            },
            "What's This?": {
                "icon": "icon128-16.png",
                "command": "icon128",
                "row": 2,
                "column": 5,
                "statustip": "&Details",
                "tooltip": "Details of the current design."
            }
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
        "arc_center_x": {
            "object": "arc",
            "label": "Center X",
            "type": "double",
            "permissions": "user"
        },
        "arc_center_y": {
            "object": "arc",
            "label": "Center Y",
            "type": "double",
            "permissions": "user"
        },
        "arc_radius": {
            "object": "arc",
            "label": "Radius",
            "type": "double",
            "permissions": "user"
        },
        "arc_start_angle": {
            "object": "arc",
            "label": "Start Angle",
            "type": "double",
            "permissions": "user"
        },
        "arc_end_angle": {
            "object": "arc",
            "label": "End Angle",
            "type": "double",
            "permissions": "user"
        },
        "arc_start_x": {
            "object": "arc",
            "label": "Start X",
            "type": "double",
            "permissions": "program"
        },
        "arc_start_y": {
            "object": "arc",
            "label": "Start Y",
            "type": "double",
            "permissions": "program"
        },
        "arc_end_x": {
            "object": "arc",
            "label": "End X",
            "type": "double",
            "permissions": "program"
        },
        "arc_end_y": {
            "object": "arc",
            "label": "End Y",
            "type": "double",
            "permissions": "program"
        },
        "arc_area": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "ARC_LENGTH": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "ARC_CHORD": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "arc_inc_angle": {
            "object": "arc",
            "label": "Included Angle",
            "type": "double",
            "permissions": "program"
        },
        "TEXT_SINGLE_CONTENTS": {
            "object": "text-single",
            "label": "Contents",
            "type": "double",
            "permissions": "program"
        },
        "TEXT_SINGLE_HEIGHT": {
            "object": "text-single",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "TEXT_SINGLE_ROTATION": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "TEXT_SINGLE_X": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "TEXT_SINGLE_Y": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "CIRCLE_CENTER_X": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "CIRCLE_CENTER_Y": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "CIRCLE_RADIUS": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "CIRCLE_DIAMETER": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "CIRCLE_AREA": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "CIRCLE_CIRCUMFERENCE": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "ELLIPSE_CENTER_X": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "ELLIPSE_CENTER_Y": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "ELLIPSE_RADIUS_MAJOR": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "ELLIPSE_RADIUS_MINOR": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "ELLIPSE_DIAMETER_MAJOR": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "ELLIPSE_DIAMETER_MINOR": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "IMAGE_X": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "IMAGE_Y": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "IMAGE_WIDTH": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "IMAGE_HEIGHT": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "IMAGE_NAME": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "IMAGE_PATH": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "INFINITE_LINE_X1": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "INFINITE_LINE_Y1": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "INFINITE_LINE_X2": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "INFINITE_LINE_Y2": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "INFINITE_LINE_VECTOR_X": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "INFINITE_LINE_VECTOR_Y": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "BLOCK_X": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "BLOCK_Y": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "LINE_START_X": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "LINE_START_Y": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "LINE_END_X": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "LINE_END_Y": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "LINE_DELTA_X": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "LINE_DELTA_Y": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "LINE_ANGLE": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "LINE_LENGTH": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "POLYGON_CENTER_X": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "POLYGON_CENTER_Y": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "POLYGON_RADIUS_VERTEX": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "POLYGON_RADIUS_SIDE": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "POLYGON_DIAMETER_VERTEX": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "POLYGON_DIAMETER_SIDE": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "POLYGON_INTERIOR_ANGLE": {
            "object": "arc",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "RECT_CORNER_X1": {
            "object": "rect",
            "label": "Corner X1",
            "type": "double",
            "permissions": "user"
        },
        "RECT_CORNER_Y1": {
            "object": "rect",
            "label": "Corner Y1",
            "type": "double",
            "permissions": "user"
        },
        "RECT_CORNER_X2": {
            "object": "rect",
            "label": "Corner X2",
            "type": "double",
            "permissions": "user"
        },
        "RECT_CORNER_Y2": {
            "object": "rect",
            "label": "Corner Y2",
            "type": "double",
            "permissions": "user"
        },
        "RECT_CORNER_X3": {
            "object": "rect",
            "label": "Corner X3",
            "type": "double",
            "permissions": "user"
        },
        "rect_corner_y3": {
            "object": "rect",
            "label": "Corner Y3",
            "type": "double",
            "permissions": "user"
        },
        "RECT_CORNER_x4": {
            "object": "rect",
            "label": "Corner X4",
            "type": "double",
            "permissions": "user"
        },
        "RECT_CORNER_y4": {
            "object": "rect",
            "label": "Corner Y4",
            "type": "double",
            "permissions": "user"
        },
        "RECT_HEIGHT": {
            "object": "rect",
            "label": "Height",
            "type": "double",
            "permissions": "user"
        },
        "RECT_WIDTH": {
            "object": "rect",
            "label": "Width",
            "type": "double",
            "permissions": "user"
        },
        "RECT_AREA": {
            "object": "rect",
            "label": "Area",
            "type": "double",
            "permissions": "program"
        },
        "POINT_X": {
            "object": "point",
            "label": "Point X",
            "type": "double",
            "permissions": "user"
        },
        "POINT_Y": {
            "object": "point",
            "label": "Point Y",
            "type": "double",
            "permissions": "user"
        }
    },
    "comboboxes": [
        "ARC_CLOCKWISE",
        "GENERAL_LAYER",
        "GENERAL_COLOR",
        "GENERAL_LINE_TYPE",
        "GENERAL_LINE_WEIGHT",
        "TEXT_SINGLE_FONT",
        "TEXT_SINGLE_JUSTIFY"
    ],
    "editor_types": [
        "line edit double",
        "line edit int",
        "line edit str",
        "combo box"
    ],
    "keys": {
        "obj_type": "int: See OBJ_TYPE_VALUES",
        "obj_name": "str: \"USER\", \"DEFINED\", \"STRINGS\", etc...",
        "OBJ_LAYER": "value type - int: 0-255",
        "OBJ_COLOR": "TODO: Use color chart in formats/format-dxf.h for this",
        "OBJ_LTYPE": "int: See OBJ_LTYPE_VALUES",
        "OBJ_LWT": "int: [-2, 27]",
        "OBJ_RUBBER": "int: See OBJ_RUBBER_VALUES"
    },
    "CAD Linetypes": [
        "LTYPE_CONT",
        "LTYPE_CENTER",
        "LTYPE_DOT",
        "LTYPE_HIDDEN",
        "LTYPE_PHANTOM",
        "LTYPE_ZIGZAG",
        "LTYPE_RUNNING",
        "LTYPE_SATIN",
        "LTYPE_FISHBONE"
    ],
    "LWT_VALUES": {
        "LWT_BYLAYER": -2,
        "LWT_BYBLOCK": -1,
        "LWT_DEFAULT": 0,
        "LWT_01": 1,
        "LWT_02": 2,
        "LWT_03": 3,
        "LWT_04": 4,
        "LWT_05": 5,
        "LWT_06": 6,
        "LWT_07": 7,
        "LWT_08": 8,
        "LWT_09": 9,
        "LWT_10": 10,
        "LWT_11": 11,
        "LWT_12": 12,
        "LWT_13": 13,
        "LWT_14": 14,
        "LWT_15": 15,
        "LWT_16": 16,
        "LWT_17": 17,
        "LWT_18": 18,
        "LWT_19": 19,
        "LWT_20": 20,
        "LWT_21": 21,
        "LWT_22": 22,
        "LWT_23": 23,
        "LWT_24": 24
    },
    "shortcuts": {
        "Ctrl+N": "newFile",
        "Ctrl+O": "openFile",
        "Ctrl+S": "saveFile",
        "Ctrl+Shift+S": "saveAsFile",
        "Ctrl+P": "mainPrint",
        "Ctrl+D": "designDetails",
        "Ctrl+Q": "exitProgram",
        "Ctrl+X": "cutObject",
        "Ctrl+C": "copyObject",
        "Ctrl+V": "pasteObject",
        "Ctrl+Z": "mainUndo",
        "Ctrl+Shift+Z": "mainRedo",
        "F1": "mainHelp",
        "F2": "mainAbout"
    },
    "tips": [
        "we need more tips?",
        "you can change the color of the display through settings?",
        "you can hide the scrollbars to increase the viewable area through settings?",
        "you can change the icon size for increased visibility?",
        "you can toggle the grid on and off by pressing the button in the statusbar?",
        "the grid size can be changed to match your hoop size through settings?",
        "the crosshair size is based on a percentage of your screen size? "
        + "Setting it to 100 may help you visually line things up better.",
        "you can pan by pressing the middle mouse button and dragging your"
        + " mouse across the screen?",
        "you can open and edit multiple designs simultaneously?",
        "that many embroidery machines support the .dst format?",
        "that you can zoom in and out using your mouse wheel?",
        "that you can use circular and isometric grids?",
        "about our command line format converter?",
        "that you can use the 'DAY' and 'NIGHT' commands to quickly switch the "
        + " view colors to commonly used white or black?",
        "that you can quickly change the background, crosshair and grid colors "
        + "using the 'RGB' command?"
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
        "Null",
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
    ],
    "tosort": {
        "to_translate": [
            "path_symbol icon_two[] = {",
            "    {PATHS_MOVETO, 0 -0.75",
            "    A {0.45, 1.00, 0.50, 180.00, -216.87",
            "    L 0 0.0",
            "    L {0.50, 0.0",
            "]",
            "",
            "path_symbol icon_three[] = {",
            "    {PATHS_ARCMOVETO, 0 -0.50, 0.50, 0.50, 195.00",
            "    A 0 -0.50, 0.50, 195.00, 255.00",
            "    A 0 -0.50, 0.50, 270.00, 255.00",
            "]",
            "",
            "path_symbol icon_five[] = {",
            "    M 50 0 L 0 0 L 0 50 L 25 50 A 0.0, -0.5 0.5 0.5 90.0 -180.0 L 0 0",
            "]",
            "",
            "path_symbol icon_six[] = {",
            "    path.addEllipse(Vector(x+0.25*xs, y-0.25*ys), 0.25*xs, 0.25*ys)",
            "    M 0 75 L 0 25",
            "    path.arcTo(x+0.00*xs, y-1.00*ys, 0.50*xs, 0.50*ys, 180.00, -140.00)",
            "]",
            "",
            "path_symbol icon_eight[] = {",
            "    path.addEllipse(Vector(x+0.25*xs, y-0.25*ys), 0.25*xs, 0.25*ys)",
            "    path.addEllipse(Vector(x+0.25*xs, y-0.75*ys), 0.25*xs, 0.25*ys)",
            "]",
            "",
            "path_symbol icon_nine[] = {",
            "    path.addEllipse(Vector(x+0.25*xs, y-0.75*ys), 0.25*xs, 0.25*ys)",
            "    M 0.50*xs, y-0.75*ys)",
            "    L x+0.50*xs, y-0.25*ys)",
            "    path.arcTo(x+0.00*xs, y-0.50*ys, 0.50*xs, 0.50*ys, 0.00, -140.00)",
            "]",
            "# OBJ_SNAP_VALUES",
            "# ---------------",
            "# NOTE: Allow this enum to evaluate false",
            "OBJ_SNAP_NULL                  0",
            "OBJ_SNAP_ENDPOINT              1",
            "OBJ_SNAP_MIDPOINT              2",
            "OBJ_SNAP_CENTER                3",
            "OBJ_SNAP_NODE                  4",
            "OBJ_SNAP_QUADRANT              5",
            "OBJ_SNAP_INTERSECTION          6",
            "OBJ_SNAP_EXTENSION             7",
            "OBJ_SNAP_INSERTION             8",
            "OBJ_SNAP_PERPENDICULAR         9",
            "OBJ_SNAP_TANGENT              10",
            "OBJ_SNAP_NEAREST              11",
            "OBJ_SNAP_APPINTERSECTION      12",
            "OBJ_SNAP_PARALLEL             13",
            "",
            "# OBJ_RUBBER_VALUES",
            "# -----------------",
            "# NOTE: Allow this enum to evaluate false and true",
            "OBJ_RUBBER_OFF",
            "OBJ_RUBBER_ON                  1",
            "OBJ_RUBBER_CIRCLE_1P_RAD       2",
            "OBJ_RUBBER_CIRCLE_1P_DIA       3",
            "OBJ_RUBBER_CIRCLE_2P           4",
            "OBJ_RUBBER_CIRCLE_3P           5",
            "OBJ_RUBBER_CIRCLE_TTR          6",
            "OBJ_RUBBER_CIRCLE_TTT          7",
            "OBJ_RUBBER_DIMLEADER_LINE      8",
            "OBJ_RUBBER_ELLIPSE_LINE        9",
            "OBJ_RUBBER_ELLIPSE_MAJORDIAMETER_MINORRADIUS 10",
            "OBJ_RUBBER_ELLIPSE_MAJORRADIUS_MINORRADIUS 11",
            "OBJ_RUBBER_ELLIPSE_ROTATION   12",
            "OBJ_RUBBER_GRIP               13",
            "OBJ_RUBBER_LINE               14",
            "OBJ_RUBBER_POLYGON            15",
            "OBJ_RUBBER_POLYGON_INSCRIBE   16",
            "OBJ_RUBBER_POLYGON_CIRCUMSCRIBE 17",
            "OBJ_RUBBER_POLYLINE           18",
            "OBJ_RUBBER_IMAGE              19",
            "OBJ_RUBBER_RECTANGLE          20",
            "OBJ_RUBBER_TEXTSINGLE         21",
            "",
            "",
            "# SPARE_RUBBER_VALUES",
            "# -------------------",
            "# NOTE: Allow this enum to evaluate false",
            "SPARE_RUBBER_OFF               0",
            "SPARE_RUBBER_PATH              1",
            "SPARE_RUBBER_POLYGON           2",
            "SPARE_RUBBER_POLYLINE          3",
            "",
            "",
            "# PREVIEW_CLONE_VALUES",
            "# --------------------",
            "# NOTE: Allow this enum to evaluate false",
            "PREVIEW_CLONE_NULL            0",
            "PREVIEW_CLONE_SELECTED        1",
            "PREVIEW_CLONE_RUBBER          2"
        ],
        "quickleader": {
            "icon": "quickleader-16.png",
            "function": "quickleader",
            "tooltip": "&QuickLeader",
            "statustip": "Creates a leader and annotation: QUICKLEADER"
        },
        "rectangle": {
            "icon": "rectangle-16.png",
            "function": "rectangle",
            "tooltip": "&Rectangle",
            "statustip": "Creates a rectangular polyline: RECTANGLE"
        },
        "rgb": {
            "icon": "rgb-16.png",
            "function": "rgb",
            "tooltip": "&RGB",
            "statustip": "Updates the current view colors: RGB"
        },
        "move": {
            "icon": "move-16.png",
            "function": "move",
            "tooltip": "&Move",
            "statustip":
                "Displaces objects a specified distance in a specified direction: MOVE"
        },
        "rotate": {
            "icon": "rotate-16.png",
            "function": "rotate",
            "statustip": "&Rotate",
            "tooltip": "Rotates objects about a base point: ROTATE"
        },
        "sandbox": {
            "icon": "sandbox-16.png",
            "function": "sandbox",
            "statustip": "&Sandbox",
            "tooltip": "A sandbox to play in: SANDBOX"
        },
        "scale": {
            "icon": "scale-16.png",
            "function": "scale",
            "statustip": "Sca&le",
            "tooltip":
                "Enlarges or reduces objects proportionally in "
                + "the X, Y, and Z directions: SCALE"
        },
        "select all": {
            "icon": "selectall-16.png",
            "function": "select_all",
            "tooltip": "&Select All",
            "statustip": "Selects all objects: SELECTALL"
        },
        "single line text": {
            "icon": "singlelinetext-16.png",
            "function": "single_line_text",
            "tooltip": "&Single Line Text",
            "statustip": "Creates single-line text objects: TEXT"
        },
        "snowflake": {
            "icon": "snowflake-16.png",
            "function": "snowflake",
            "tooltip": "&Snowflake",
            "statustip": "Creates a snowflake: SNOWFLAKE"
        },
        "star": {
            "icon": "star-16.png",
            "command": "star",
            "tooltip": "&Star",
            "statustip": "Creates a star: STAR"
        },
        "arc length": {
            "object": "arc",
            "type": "double",
            "label": "Length",
            "permissions": "program"
        },
        "arc chord": {
            "object": "arc",
            "type": "double",
            "label": "Chord",
            "permissions": "program"
        },
        "arc included angle": {
            "object": "arc",
            "type": "double",
            "label": "Included Angle",
            "permissions": "program"
        },
        "arc clockwise": {
            "object": "arc",
            "label": "Clockwise",
            "type": "int",
            "permissions": "program"
        },
        "Ellipse Center X": {
            "object": "ellipse",
            "label": "Center X",
            "type": "double",
            "permissions": "user"
        },
        "Ellipse Center Y": {
            "object": "ellipse",
            "label": "Center Y",
            "type": "double",
            "permissions": "user"
        },
        "Ellipse Radius Major": {
            "object": "ellipse",
            "label": "Radius Major",
            "type": "double",
            "permissions": "user"
        },
        "Ellipse Radius Minor": {
            "object": "ellipse",
            "label": "Radius Minor",
            "type": "double",
            "permissions": "user"
        },
        "Ellipse Diameter Major": {
            "object": "ellipse",
            "label": "Diameter Major",
            "type": "double",
            "permissions": "user"
        },
        "Ellipse Diameter Minor": {
            "object": "ellipse",
            "label": "Diameter Minor",
            "type": "double",
            "permissions": "user"
        },
        "Block X": {
            "object": "block",
            "label": "Position X",
            "permissions": "user",
            "type": "double"
        },
        "Block Y": {
            "object": "block",
            "label": "Position Y",
            "permissions": "user",
            "type": "double"
        },
        "exit": {
            "icon": "exit-16.png",
            "function": "exit_program",
            "tooltip": "E&xit",
            "statustip": "Exit the application."
        },
        "cut": {
            "function": "cut_object",
            "icon": "cut-16.png",
            "tooltip": "Cu&t",
            "statustip": "Cut the current selection's contents to the clipboard."
        },
        "copy": {
            "function": "copy_object",
            "icon": "copy-16.png",
            "tooltip": "&Copy",
            "statustip": "Copy the current selection's contents to the clipboard."
        },
        "paste": {
            "function": "paste_object",
            "icon": "paste-16.png",
            "tooltip": "&Paste",
            "statustip": "Paste the clipboard's contents into the current selection."
        },
        "undo": {
            "function": "main_undo",
            "icon": "undo-16.png",
            "tooltip": "&Undo",
            "statustip": "Reverses the most recent action."
        },
        "redo": {
            "icon": "redo-16.png",
            "function": "mainRedo",
            "tooltip": "&Redo",
            "statustip": "Reverses the effects of the previous undo action."
        },
        "windowclose": {
            "icon": "windowclose-16.png",
            "function": "windowClose",
            "tooltip": "Cl&ose",
            "statustip": "Close the active window."
        },
        "windowcloseall": {
            "icon": "windowcloseall-16.png",
            "function": "windowCloseAll",
            "tooltip": "Close &All",
            "statustip": "Close all the windows."
        },
        "window_casacade": {
            "icon": "windowcascade-16.png",
            "function": "window_cascade",
            "tooltip": "&Cascade",
            "statustip": "Cascade the windows."
        },
        "window_tile": {
            "icon": "windowtile-16.png",
            "function": "window_tile",
            "tooltip": "&Tile",
            "statustip": "Tile the windows."
        },
        "windownext": {
            "icon": "windownext-16.png",
            "function": "window_next",
            "tooltip": "Ne&xt",
            "statustip": "Move the focus to the next window."
        },
        "windowprevious": {
            "icon": "windowprevious-16.png",
            "function": "window_previous",
            "tooltip": "Pre&vious",
            "statustip": "Move the focus to the previous window."
        },
        "help": {
            "icon": "help-16.png",
            "statustip": "&Help",
            "tooltip": "Displays help.",
            "function": "main_help"
        },
        "changelog": {
            "icon": "changelog-16.png",
            "statustip": "&Changelog",
            "tooltip": "Describes new features in this product.",
            "function": "changelog"
        },
        "tipoftheday": {
            "icon": "tipoftheday-16.png",
            "tooltip": "&Tip Of The Day",
            "statustip": "Displays a dialog with useful tips",
            "function": "tipOfTheDay"
        },
        "about": {
            "icon": "about-16.png",
            "tooltip": "&About Embroidermodder 2",
            "statustip": "Displays information about this product.",
            "function": "main_about"
        },
        "whatsthis": {
            "icon": "whatsthis-16.png",
            "tooltip": "&What's This?",
            "statustip": "What's This? Context Help!",
            "function": "whatsthisContextHelp"
        },
        "icon32": {
            "icon": "icon32-16.png",
            "function": "icon32",
            "tooltip": "Icon&32",
            "statustip": "Sets the toolbar icon size to 32x32."
        },
        "icon48": {
            "icon": "icon48-16.png",
            "function": "icon48",
            "tooltip": "Icon&48",
            "statustip": "Sets the toolbar icon size to 48x48."
        },
        "icon64": {
            "icon": "icon64-16.png",
            "function": "icon64",
            "tooltip": "Icon&64",
            "statustip": "Sets the toolbar icon size to 64x64."
        },
        "icon128": {
            "icon": "icon128-16.png",
            "function": "icon128",
            "tooltip": "Icon12&8",
            "statustip": "Sets the toolbar icon size to 128x128."
        },
        "settings_dialog": {
            "icon": "settingsdialog-16.png",
            "function": "settings_dialog",
            "tooltip": "&Settings",
            "statustip": "Configure settings specific to this product."
        },
        "make_layer_current": {
            "icon": "makelayercurrent-16.png",
            "function": "make_layer_current",
            "tooltip": "&Make Layer Active",
            "statustip": "Makes the layer of a selected object the active layer"
        },
        "layers": {
            "icon": "layers-16.png",
            "function": "layers",
            "tooltip": "&Layers",
            "statustip": "Manages layers and layer properties: LAYER"
        },
        "layer_selector": {
            "icon": "layerselector-16.png",
            "function": "layerselector",
            "tooltip": "&Layer Selector",
            "statustip": "Dropdown selector for changing the current layer"
        },
        "layerprevious": {
            "icon": "layerprevious-16.png",
            "function": "layerprevious",
            "tooltip": "&Layer Previous",
            "statustip": "Restores the previous layer settings: LAYERP"
        },
        "colorselector": {
            "icon": "colorselector-16.png",
            "function": "colorselector",
            "tooltip": "&Color Selector",
            "statustip": "Dropdown selector for changing the current thread color"
        },
        "linetypeselector": {
            "icon": "linetypeselector-16.png",
            "function": "linetypeselector",
            "tooltip": "&Stitchtype Selector",
            "statustip": "Dropdown selector for changing the current stitch type"
        },
        "lineweightselector": {
            "icon": "lineweightselector-16.png",
            "function": "lineweightselector",
            "tooltip": "&Threadweight Selector",
            "statustip": "Dropdown selector for changing the current thread weight"
        },
        "hidealllayers": {
            "icon": "hidealllayers-16.png",
            "function": "hidealllayers",
            "tooltip": "&Hide All Layers",
            "statustip":
            "Turns the visibility off for all layers in the current drawing: HIDEALL"
        },
        "showalllayers": {
            "icon": "showalllayers-16.png",
            "function": "showalllayers",
            "tooltip": "&Show All Layers",
            "statustip":
            "Turns the visibility on for all layers in the current drawing: SHOWALL"
        },
        "freezealllayers": {
            "icon": "freezealllayers-16.png",
            "function": "freezealllayers",
            "tooltip": "&Freeze All Layers",
            "statustip": "Freezes all layers in the current drawing:  FREEZEALL"
        },
        "thawalllayers": {
            "icon": "thawalllayers-16.png",
            "function": "thawalllayers",
            "tooltip": "&Thaw All Layers",
            "statustip": "Thaws all layers in the current drawing: THAWALL"
        },
        "lockalllayers": {
            "icon": "lockalllayers-16.png",
            "function": "lockalllayers",
            "tooltip": "&Lock All Layers",
            "statustip": "Locks all layers in the current drawing: LOCKALL"
        },
        "unlockalllayers": {
            "icon": "unlockalllayers-16.png",
            "function": "unlockalllayers",
            "tooltip": "&Unlock All Layers",
            "statustip": "Unlocks all layers in the current drawing:  UNLOCKALL"
        },
        "textbold": {
            "icon": "textbold-16.png",
            "function": "textbold",
            "tooltip": "&Bold Text",
            "statustip": "Sets text to be bold."
        },
        "textitalic": {
            "icon": "textitalic-16.png",
            "function": "textitalic",
            "tooltip": "&Italic Text",
            "statustip": "Sets text to be italic."
        },
        "textunderline": {
            "icon": "textoverline-16.png",
            "function": "textunderline",
            "tooltip": "&Underline Text",
            "statustip": "Sets text to be underlined."
        },
        "textstrikeout": {
            "icon": "textstrikeout-16.png",
            "function": "textstrikeout",
            "tooltip": "&StrikeOut Text",
            "statustip": "Sets text to be striked out."
        },
        "textoverline": {
            "icon": "textoverline-16.png",
            "function": "textoverline",
            "tooltip": "&Overline Text",
            "statustip": "Sets text to be overlined."
        },
        "zoomrealtime": {
            "icon": "zoomrealtime-16.png",
            "function": "zoomrealtime",
            "tooltip": "Zoom &Realtime",
            "statustip":
            "Zooms to increase or decrease the apparent size of "
            + "objects in the current viewport."
        },
        "zoomprevious": {
            "icon": "zoomprevious-16.png",
            "function": "zoomprevious",
            "tooltip": "Zoom &Previous",
            "statustip": "Zooms to display the previous view."
        },
        "zoomwindow": {
            "icon": "zoomwindow-16.png",
            "function": "zoomwindow",
            "tooltip": "Zoom &Window",
            "statustip": "Zooms to display an area specified by a rectangular window."
        },
        "zoomdynamic": {
            "icon": "zoomdynamic-16.png",
            "function": "zoomdynamic",
            "tooltip": "Zoom &Dynamic",
            "statustip": "Zooms to display the generated portion of the drawing."
        },
        "zoomscale": {
            "icon": "zoomscale-16.png",
            "function": "zoomscale",
            "tooltip": "Zoom &Scale",
            "statustip": "Zooms the display using a specified scale factor."
        },
        "zoomcenter": {
            "icon": "zoomcenter-16.png",
            "function": "zoomcenter",
            "tooltip": "Zoom &Center",
            "statustip":
            "Zooms to display a view specified by a center point and"
            + " magnification or height."
        },
        "zoomin": {
            "icon": "zoomin-16.png",
            "function": "zoomin",
            "tooltip": "Zoom &In",
            "statustip": "Zooms to increase the apparent size of objects."
        },
        "zoomout": {
            "icon": "zoomout-16.png",
            "function": "zoomout",
            "tooltip": "Zoom &Out",
            "statustip": "Zooms to decrease the apparent size of objects."
        },
        "zoom_selected": {
            "icon": "zoomselected-16.png",
            "function": "zoomselected",
            "tooltip": "Zoom Selec&ted",
            "statustip": "Zooms to display the selected objects."
        },
        "zoom_all": {
            "icon": "zoomall-16.png",
            "function": "zoomall",
            "tooltip": "Zoom &All",
            "statustip": "Zooms to display the drawing extents or the grid limits."
        },
        "zoom_extents": {
            "icon": "zoomextents-16.png",
            "tooltip": "Zoom &Extents",
            "statustip": "Zooms to display the drawing extents.",
            "function": "zoom_extents"
        },
        "panrealtime": {
            "icon": "panrealtime-16.png",
            "function": "panrealtime",
            "tooltip": "&Pan Realtime",
            "statustip": "Moves the view in the current viewport."
        },
        "panpoint": {
            "icon": "panpoint-16.png",
            "function": "panpoint",
            "tooltip": "&Pan Point",
            "statustip": "Moves the view by the specified distance."
        },
        "panleft": {
            "icon": "panleft-16.png",
            "function": "panleft",
            "tooltip": "&Pan Left",
            "statustip": "Moves the view to the left."
        },
        "panright": {
            "icon": "panright-16.png",
            "function": "panright",
            "tooltip": "&Pan Right",
            "statustip": "Moves the view to the right."
        },
        "panup": {
            "icon": "panup-16.png",
            "function": "panup",
            "tooltip": "&Pan Up",
            "statustip": "Moves the view up."
        },
        "pandown": {
            "icon": "pandown-16.png",
            "function": "pandown",
            "tooltip": "&Pan Down",
            "statustip": "Moves the view down."
        },
        "circle": {
            "icon": "circle-16.png",
            "function": "circle",
            "tooltip": "&Circle",
            "statustip": "Creates a circle: CIRCLE"
        },
        "line": {
            "icon": "line-16.png",
            "function": "line",
            "tooltip": "&Line",
            "statustip": "Creates straight line segments: LINE"
        },
        "distance": {
            "icon": "distance-16.png",
            "function": "distance",
            "tooltip": "&Distance",
            "statustip": "Measures the distance and angle between two points: DIST"
        },
        "dolphin": {
            "icon": "dolphin-16.png",
            "function": "dolphin",
            "tooltip": "&Dolphin",
            "statustip": "Creates a dolphin:  DOLPHIN"
        },
        "ellipse": {
            "icon": "ellipse-16.png",
            "function": "ellipse",
            "tooltip": "&Ellipse",
            "statustip": "Creates a ellipse: ELLIPSE"
        },
        "erase": {
            "icon": "erase-16.png",
            "function": "delete",
            "tooltip": "D&elete",
            "statustip": "Removes objects from a drawing: DELETE"
        },
        "heart": {
            "icon": "heart-16.png",
            "function": "heart",
            "tooltip": "&Heart",
            "statustip": "Creates a heart: HEART"
        },
        "locatepoint": {
            "icon": "locatepoint-16.png",
            "function": "locatepoint",
            "tooltip": "&Locate Point",
            "statustip": "Displays the coordinate values of a location:  ID"
        },
        "trebleclef": {
            "icon": "donothing-16.png",
            "function": "trebleclef",
            "tooltip": "TrebleClef",
            "statustip": "Creates a treble clef: TREBLECLEF"
        },
        "path": {
            "icon": "path-16.png",
            "function": "path",
            "tooltip": "&Path",
            "statustip": "Creates a 2D path: PATH"
        },
        "platform": {
            "icon": "donothing-16.png",
            "function": "platform",
            "tooltip": "&Platform",
            "statustip": "List which platform is in use: PLATFORM"
        },
        "point": {
            "icon": "point-16.png",
            "function": "point",
            "tooltip": "&Point",
            "statustip": "Creates multiple points: POINT"
        },
        "polygon": {
            "icon": "polygon-16.png",
            "function": "polygon",
            "tooltip": "Pol&ygon",
            "statustip": "Creates a regular polygon: POLYGON"
        },
        "polyline": {
            "icon": "polyline-16.png",
            "function": "polyline",
            "tooltip": "&Polyline",
            "statustip": "Creates a 2D polyline: PLINE"
        }
    },
    "icons": icons
}