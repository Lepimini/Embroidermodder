/* This file is part of Embroidermodder 2.
 * ------------------------------------------------------------
 * Copyright 2021 The Embroidermodder Team
 * Embroidermodder 2 is Open Source Software.
 * See LICENSE.txt for licensing terms.
 * ------------------------------------------------------------
 * This file is only for data and declarations that
 * are compiled into the source.
 */

#include "embroidermodder.h"

const char* _appName_ = "Embroidermodder";
const char* _appVer_ = "v2.0 alpha";
int exitApp = 0;

char *tips[] = {
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
    "\0"
};

char *details_label_text[] = {
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
};

char *obj_names[] = {
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
};

int file_toolbar[] = {
    ACTION_new,
    ACTION_open,
    ACTION_save,
    ACTION_saveas,
    ACTION_print,
    ACTION_designdetails,
    -1,
    ACTION_undo,
    ACTION_redo,
    -1,
    ACTION_help,
    -2
};

int edit_toolbar[] = {
    ACTION_cut,
    ACTION_copy,
    ACTION_paste,
    -2
};

int view_toolbar[] = {
    ACTION_day,
    ACTION_night,
    -2
};

int pan_toolbar[] = {
    ACTION_panrealtime,
    ACTION_panpoint,
    -1,
    ACTION_panleft,
    ACTION_panright,
    ACTION_panup,
    ACTION_pandown,
    -2
};

int icon_toolbar[] = {
    ACTION_icon16,
    ACTION_icon24,
    ACTION_icon32,
    ACTION_icon48,
    ACTION_icon64,
    ACTION_icon128,
    -2
};

int help_toolbar[] = {
    ACTION_help,
    -1,
    ACTION_changelog,
    -1,
    ACTION_about,
    -1,
    ACTION_whatsthis,
    -2
};

int zoom_toolbar[] = {
    ACTION_zoomwindow,
    ACTION_zoomdynamic,
    ACTION_zoomscale,
    -1,
    ACTION_zoomcenter,
    ACTION_zoomin,
    ACTION_zoomout,
    -1,
    ACTION_zoomselected,
    ACTION_zoomall,
    ACTION_zoomextents,
    -2
};

int layer_toolbar[] = {
    -2
};

int text_toolbar[] = {
    -2
};

int properties_toolbar[] = {
    -2
};

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
};


int file_menu[] = {
    ACTION_new,
    ACTION_open,
    ACTION_save,
    ACTION_saveas,
    ACTION_print,
    ACTION_designdetails,
    -1,
    ACTION_help,
    -1,
    ACTION_exit,
    -2
};

int edit_menu[] = {
    ACTION_undo,
    ACTION_redo,
    -1,
    ACTION_cut,
    ACTION_copy,
    ACTION_paste,
    -2
};

int view_menu[] = {
    ACTION_day,
    ACTION_night,
    -2
};

int pan_menu[] = {
    ACTION_panrealtime,
    ACTION_panpoint,
    -1,
    ACTION_panleft,
    ACTION_panright,
    ACTION_panup,
    ACTION_pandown,
    -2
};

int icon_menu[] = {
    ACTION_icon16,
    ACTION_icon24,
    ACTION_icon32,
    ACTION_icon48,
    ACTION_icon64,
    ACTION_icon128,
    -2
};

int help_menu[] = {
    ACTION_help,
    -1,
    ACTION_changelog,
    -1,
    ACTION_tipoftheday,
    -1,
    ACTION_about,
    -1,
    ACTION_whatsthis,
    -2
};

int zoom_menu[] = {
    ACTION_zoomwindow,
    ACTION_zoomdynamic,
    ACTION_zoomscale,
    -1,
    ACTION_zoomcenter,
    ACTION_zoomin,
    ACTION_zoomout,
    -1,
    ACTION_zoomselected,
    ACTION_zoomall,
    ACTION_zoomextents,
    -2
};

int settings_menu[] = {
    ACTION_settingsdialog,
    -1,
    -2
};

int recent_menu[] = {
    -1,
    -2
};

int window_menu[] = {
    -1,
    -2
};

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
};

char *toolbar_label[] = {
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
};

char *menu_label[] = {
    "&File",
    "&Edit",
    "&View",
    "&Settings",
    "&Window",
    "&Help",
    "Open &Recent",
    "&Zoom",
    "&Pan"
};

char *status_bar_labels[] = {
    "SNAP",
    "GRID",
    "RULER",
    "ORTHO",
    "POLAR",
    "QSNAP",
    "QTRACK",
    "LWT"
};

char *folders[] = {
    "",
    "commands",
    "help",
    "icons",
    "images",
    "samples",
    "translations"
};

int n_toolbars = 10;
int n_menus = 8;

path_symbol icon_zero[] = {
    /* path.addEllipse(QPointF(x+0.25*xScale, y-0.50*yScale), 0.25*xScale, 0.50*yScale);*/
    {PATHS_MOVETO, {0.0, -0.75}},
    {PATHS_LINETO, {0.0, -0.25}},
    {PATHS_ARCTO, {0.0, -0.5, 0.5, 0.5, 180.0, 180.0}},
    {PATHS_LINETO, {0.5, -0.75}},
    {PATHS_ARCTO, {0.0, -1.0, 0.5, 0.5, 0.0, 180.0}},
    {PATHS_END, {0.0, 0.0}}
};

path_symbol icon_one[] = {
    {PATHS_MOVETO, {0.05, 0.00}},
    {PATHS_LINETO, {0.45, 0.00}},
    {PATHS_MOVETO, {0.0, -0.75}},
    {PATHS_LINETO, {0.25, -1.00}},
    {PATHS_LINETO, {0.25, 0.00}},
    {PATHS_END, {0.0, 0.0}}
};

path_symbol icon_two[] = {
    {PATHS_MOVETO, {0.0, -0.75}},
    {PATHS_ARCTO, {0.45, 1.00, 0.50, 180.00, -216.87}},
    {PATHS_LINETO, {0.0, 0.0}},
    {PATHS_LINETO, {0.50, 0.0}},
    {PATHS_END, {0.0, 0.0}}
};

path_symbol icon_three[] = {
    {PATHS_ARCMOVETO, {0.0, -0.50, 0.50, 0.50, 195.00}},
    {PATHS_ARCTO, {0.0, -0.50, 0.50, 195.00, 255.00}},
    {PATHS_ARCTO, {0.0, -0.50, 0.50, 270.00, 255.00}},
    {PATHS_END, {0.0, 0.0}}
};

path_symbol icon_four[] = {
    {PATHS_MOVETO, {0.50, 0.0}},
    {PATHS_LINETO, {0.50, -1.00}},
    {PATHS_LINETO, {0.0, -0.50}},
    {PATHS_LINETO, {0.50, -0.50}},
    {PATHS_END, {0.0, 0.0}}
};

path_symbol icon_five[] = {
    {PATHS_MOVETO, {0.50, -1.0}},
    {PATHS_LINETO, {0.0, -1.00}},
    {PATHS_LINETO, {0.0, -0.50}},
    {PATHS_LINETO, {0.25, -0.50}},
    {PATHS_LINETO, {0.0, -0.5, 0.5, 0.5, 90.0, -180.0}},
    {PATHS_LINETO, {0.0, 0.0}},
    {PATHS_END, {0.0, 0.0}}
};

path_symbol icon_six[] = {
    /*
    path.addEllipse(QPointF(x+0.25*xScale, y-0.25*yScale), 0.25*xScale, 0.25*yScale);
    path.moveTo(x+0.00*xScale, y-0.25*yScale);
    path.lineTo(x+0.00*xScale, y-0.75*yScale);
    path.arcTo(x+0.00*xScale, y-1.00*yScale, 0.50*xScale, 0.50*yScale, 180.00, -140.00);
    */
    {PATHS_END, {0.0, 0.0}}
};

path_symbol icon_seven[] = {
    {PATHS_MOVETO, {0.0, -1.0}},
    /*
    path.moveTo(x+0.00*xScale, y-1.00*yScale);
    path.lineTo(x+0.50*xScale, y-1.00*yScale);
    path.lineTo(x+0.25*xScale, y-0.25*yScale);
    path.lineTo(x+0.25*xScale, y-0.00*yScale);
    */
    {PATHS_END, {0.0, 0.0}}
};

path_symbol icon_eight[] = {
    /*
    path.addEllipse(QPointF(x+0.25*xScale, y-0.25*yScale), 0.25*xScale, 0.25*yScale);
    path.addEllipse(QPointF(x+0.25*xScale, y-0.75*yScale), 0.25*xScale, 0.25*yScale);
    */
    {PATHS_END, {0.0, 0.0}}
};

path_symbol icon_nine[] = {
    /*
    path.addEllipse(QPointF(x+0.25*xScale, y-0.75*yScale), 0.25*xScale, 0.25*yScale);
    path.moveTo(x+0.50*xScale, y-0.75*yScale);
    path.lineTo(x+0.50*xScale, y-0.25*yScale);
    path.arcTo(x+0.00*xScale, y-0.50*yScale, 0.50*xScale, 0.50*yScale, 0.00, -140.00);
    */
    {PATHS_END, {0.0, 0.0}}
};

path_symbol icon_minus[] = {
    /*
    path.moveTo(x+0.00*xScale, y-0.50*yScale);
    path.lineTo(x+0.50*xScale, y-0.50*yScale);
    */
    {PATHS_END, {0.0, 0.0}}
};

path_symbol icon_apostrophe[] = {
    /*
    path.moveTo(x+0.25*xScale, y-1.00*yScale);
    path.lineTo(x+0.25*xScale, y-0.75*yScale);
    */
    {PATHS_END, {0.0, 0.0}}
};

path_symbol icon_quote[] = {
    /*
    path.moveTo(x+0.10*xScale, y-1.00*yScale);
    path.lineTo(x+0.10*xScale, y-0.75*yScale);
    path.moveTo(x+0.40*xScale, y-1.00*yScale);
    path.lineTo(x+0.40*xScale, y-0.75*yScale);
    */
    {PATHS_END, {0.0, 0.0}}
};

path_symbol *symbol_list[] = {
    icon_zero,
    icon_one,
    icon_two,
    icon_three,
    icon_four,
    icon_five,
    icon_six,
    icon_seven,
    icon_eight,
    icon_nine,
    icon_minus,
    icon_apostrophe,
    icon_quote
};

int n_actions = 68;

action_hash_data action_list[] = {
    {
        /* 0 */
        ACTION_donothing,
        icon_donothing,
        "donothing",
        "&Do Nothing",
        "Does nothing.",
        "\0",
        doNothing
    },
    {
        /* 1 */
        ACTION_new,
        icon__new,
        "new",
        "&New",
        "Create a new file.",
        "Ctrl+N",
        newFile
    },
    {
        /* 2 */
        ACTION_open,
        icon_open,
        "open",
        "&Open",
        "Open an existing file.",
        "Ctrl+O",
        openFile
    },
    {
        /* 3 */
        ACTION_save,
        icon_save,
        "save",
        "&Save",
        "Save the design to disk.",
        "Ctrl+S",
        saveFile
    },
    {
        /* 4 */
        ACTION_saveas,
        icon_saveas,
        "saveas",
        "Save &As",
        "Save the design under a new name.",
        "Ctrl+Shift+S",
        saveAsFile
    },
    {
        /* 5 */
        ACTION_print,
        icon_print,
        "print",
        "&Print",
        "Print the design.",
        "Ctrl+P",
        main_print
    },
    {
        /* 6 */
        ACTION_designdetails,
        icon_designdetails,
        "designdetails",
        "&Details",
        "Details of the current design.",
        "Ctrl+D",
        designDetails
    },
    {
        /* 7 */
        ACTION_exit,
        icon_exit,
        "exit",
        "E&xit",
        "Exit the application.",
        "Ctrl+Q",
        main_exit
    },
    {
        /* 8 */
        ACTION_cut,
        icon_cut,
        "cut",
        "Cu&t",
        "Cut the current selection's contents to the clipboard.",
        "Ctrl+X",
        main_cut
    },
    {
        /* 9 */
        ACTION_copy,
        icon_copy,
        "copy",
        "&Copy",
        "Copy the current selection's contents to the clipboard.",
        "Ctrl+C",
        main_copy
    },
    {
        /* 10 */
        ACTION_paste,
        icon_paste,
        "paste",
        "&Paste",
        "Paste the clipboard's contents into the current selection.",
        "Ctrl+V",
        main_paste
    },
    {
        ACTION_windowcascade,
        icon_windowcascade,
        "windowcascade",
        "&Cascade",
        "Cascade the windows.",
        "\0",
        windowCascade
    },
    {
        ACTION_windowtile,
        icon_windowtile,
        "windowtile",
        "&Tile",
        "Tile the windows.",
        "\0",
        windowTile
    },
    {
        ACTION_windowclose,
        icon_windowclose,
        "windowclose",
        "Cl&ose",
        "Close the active window.",
        "\0",
        windowClose
    },
    {
        ACTION_windowcloseall,
        icon_windowcloseall,
        "windowcloseall",
        "Close &All",
        "Close all the windows.",
        "\0",
        windowCloseAll
    },
    {
        ACTION_windownext,
        icon_windownext,
        "windownext",
        "Ne&xt",
        "Move the focus to the next window.",
        "\0",
        windowNext
    },
    {
        ACTION_windowprevious,
        icon_windowprevious,
        "windowprevious",
        "Pre&vious",
        "Move the focus to the previous window.",
        "\0",
        windowPrevious
    },
    {
        ACTION_help,
        icon_help,
        "help",
        "&Help",
        "Displays help.",
        "F1",
        main_help
    },
    {
        ACTION_changelog,
        icon_changelog,
        "changelog",
        "&Changelog",
        "Describes new features in this product.",
        "\0",
        changelog
    },
    {
        ACTION_tipoftheday,
        icon_tipoftheday,
        "tipoftheday",
        "&Tip Of The Day",
        "Displays a dialog with useful tips",
        "\0",
        tipOfTheDay
    },
    {
        ACTION_about,
        icon_about,
        "about",
        "&About Embroidermodder 2",
        "Displays information about this product.",
        "F2",
        main_about
    },
    {
        ACTION_whatsthis,
        icon_whatsthis,
        "whatsthis",
        "&What's This?",
        "What's This? Context Help!",
        "\0",
        whatsthisContextHelp
    },
    {
        ACTION_undo,
        icon_undo,
        "undo",
        "&Undo",
        "Reverses the most recent action.",
        "Ctrl+Z",
        main_undo
    },
    {
        ACTION_redo,
        icon_redo,
        "redo",
        "&Redo",
        "Reverses the effects of the previous undo action.",
        "Ctrl+Shift+Z",
        main_redo
    },
    {
        ACTION_icon16,
        icon_icon16,
        "icon16",
        "Icon&16",
        "Sets the toolbar icon size to 16x16.",
        "\0",
        icon16
    },
    {
        ACTION_icon24,
        icon_icon24,
        "icon24",
        "Icon&24",
        "Sets the toolbar icon size to 24x24.",
        "\0",
        icon24
    },
    {
        ACTION_icon32,
        icon_icon32,
        "icon32",
        "Icon&32",
        "Sets the toolbar icon size to 32x32.",
        "\0",
        icon32
    },
    {
        ACTION_icon48,
        icon_icon48,
        "icon48",
        "Icon&48",
        "Sets the toolbar icon size to 48x48.",
        "\0",
        icon48
    },
    {
        ACTION_icon64,
        icon_icon64,
        "icon64",
        "Icon&64",
        "Sets the toolbar icon size to 64x64.",
        "\0",
        icon64
    },
    {
        ACTION_icon128,
        icon_icon128,
        "icon128",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128.",
        "\0",
        icon128
    },
    {
        ACTION_settingsdialog,
        icon_settingsdialog,
        "settingsdialog",
        "&Settings",
        "Configure settings specific to this product.",
        "\0",
        settingsDialog
    },
    {
       ACTION_makelayercurrent,
       icon_makelayercurrent,
       "makelayercurrent",
       "&Make Layer Active",
       "Makes the layer of a selected object the active layer",
        "\0",
        makeLayerCurrent
    },
    {
        ACTION_layers,
        icon_layers,
        "layers",
        "&Layers",
        "Manages layers and layer properties:  LAYER",
        "\0",
        layerManager
    },
    {
        ACTION_layerselector,
        icon_layerselector,
        "layerselector",
        "&Layer Selector",
        "Dropdown selector for changing the current layer",
        "\0",
        layerSelector
    },
    {
        ACTION_layerprevious,
        icon_layerprevious,
        "layerprevious",
        "&Layer Previous",
        "Restores the previous layer settings:  LAYERP",
        "\0",
        layerPrevious
    },
    {
        ACTION_colorselector,
        icon_colorselector,
        "colorselector",
        "&Color Selector",
        "Dropdown selector for changing the current thread color",
        "\0",
        colorSelector
    },
    {
        ACTION_linetypeselector,
        icon_linetypeselector,
        "linetypeselector",
        "&Stitchtype Selector",
        "Dropdown selector for changing the current stitch type",
        "\0",
        lineTypeSelector
    },
    {
        ACTION_lineweightselector,
        icon_lineweightselector,
        "lineweightselector",
        "&Threadweight Selector",
        "Dropdown selector for changing the current thread weight",
        "\0",
        lineWeightSelector
    },
    {
        ACTION_hidealllayers,
        icon_hidealllayers,
        "hidealllayers",
        "&Hide All Layers",
        "Turns the visibility off for all layers in the current drawing:  HIDEALL",
        "\0",
        hideAllLayers
    },
    {
        ACTION_showalllayers,
        icon_showalllayers,
        "showalllayers",
        "&Show All Layers",
        "Turns the visibility on for all layers in the current drawing:  SHOWALL",
        "\0",
        showAllLayers
    },
    {
        ACTION_freezealllayers,
        icon_freezealllayers,
        "freezealllayers",
        "&Freeze All Layers",
        "Freezes all layers in the current drawing:  FREEZEALL",
        "\0",
        freezeAllLayers
    },
    {
        ACTION_thawalllayers,
        icon_thawalllayers,
        "thawalllayers",
        "&Thaw All Layers",
        "Thaws all layers in the current drawing:  THAWALL",
        "\0",
        thawAllLayers
    },
    {
        ACTION_lockalllayers,
        icon_lockalllayers,
        "lockalllayers",
        "&Lock All Layers",
        "Locks all layers in the current drawing:  LOCKALL",
        "\0",
        lockAllLayers
    },
    {
        ACTION_unlockalllayers,
        icon_unlockalllayers,
        "unlockalllayers",
        "&Unlock All Layers",
        "Unlocks all layers in the current drawing:  UNLOCKALL",
        "\0",
        unlockAllLayers
    },
    {
        ACTION_textbold,
        icon_textbold,
        "textbold",
        "&Bold Text",
        "Sets text to be bold.",
        "\0",
        textBold
    },
    {
        ACTION_textitalic,
        icon_textitalic,
        "textitalic",
        "&Italic Text",
        "Sets text to be italic.",
        "\0",
        textItalic
    },
    {
        ACTION_textoverline,
        icon_textoverline,
        "textunderline",
        "&Underline Text",
        "Sets text to be underlined.",
        "\0",
        textOverline
    },
    {
        ACTION_textstrikeout,
        icon_textstrikeout,
        "textstrikeout",
        "&StrikeOut Text",
        "Sets text to be striked out.",
        "\0",
        textStrikeout
    },
    {
        ACTION_textoverline,
        icon_textoverline,
        "textoverline",
        "&Overline Text",
        "Sets text to be overlined.",
        "\0",
        textOverline
    },
    {
        ACTION_zoomrealtime,
        icon_zoomrealtime,
        "zoomrealtime",
        "Zoom &Realtime",
        "Zooms to increase or decrease the apparent size of objects in the current viewport.",
        "\0",
        zoomRealtime
    },
    {
        ACTION_zoomprevious,
        icon_zoomprevious,
        "zoomprevious",
        "Zoom &Previous",
        "Zooms to display the previous view.",
        "\0",
        zoomPrevious
    },
    {
        ACTION_zoomwindow,
        icon_zoomwindow,
        "zoomwindow",
        "Zoom &Window",
        "Zooms to display an area specified by a rectangular window.",
        "\0",
        zoomWindow
    },
    {
        ACTION_zoomdynamic,
        icon_zoomdynamic,
        "zoomdynamic",
        "Zoom &Dynamic",
        "Zooms to display the generated portion of the drawing.",
        "\0",
        zoomDynamic
    },
    {
        ACTION_zoomscale,
        icon_zoomscale,
        "zoomscale",
        "Zoom &Scale",
        "Zooms the display using a specified scale factor.",
        "\0",
        zoomScale
    },
    {
        ACTION_zoomcenter,
        icon_zoomcenter,
        "zoomcenter",
        "Zoom &Center",
        "Zooms to display a view specified by a center point and magnification or height.",
        "\0",
        zoomCenter
    },
    {
        ACTION_zoomin,
        icon_zoomin,
        "zoomin",
        "Zoom &In",
        "Zooms to increase the apparent size of objects.",
        "\0",
        zoomIn
    },
    {
        ACTION_zoomout,
        icon_zoomout,
        "zoomout",
        "Zoom &Out",
        "Zooms to decrease the apparent size of objects.",
        "\0",
        zoomOut
    },
    {
        ACTION_zoomselected,
        icon_zoomselected,
        "zoomselected",
        "Zoom Selec&ted",
        "Zooms to display the selected objects.",
        "\0",
        zoomSelected
    },
    {
        ACTION_zoomall,
        icon_zoomall,
        "zoomall",
        "Zoom &All",
        "Zooms to display the drawing extents or the grid limits.",
        "\0",
        zoomAll
    },
    {
        ACTION_zoomextents,
        icon_zoomextents,
        "zoomextents",
        "Zoom &Extents",
        "Zooms to display the drawing extents.",
        "\0",
        zoomExtents
    },
    {
        ACTION_panrealtime,
        icon_panrealtime,
        "panrealtime",
        "&Pan Realtime",
        "Moves the view in the current viewport.",
        "\0",
        panrealtime
    },
    {
        ACTION_panpoint,
        icon_panpoint,
        "panpoint",
        "&Pan Point",
        "Moves the view by the specified distance.",
        "\0",
        panpoint
    },
    {
        ACTION_panleft,
        icon_panleft,
        "panleft",
        "&Pan Left",
        "Moves the view to the left.",
        "\0",
        panLeft
    },
    {
        ACTION_panright,
        icon_panright,
        "panright",
        "&Pan Right",
        "Moves the view to the right.",
        "\0",
        panRight
    },
    {
        ACTION_panup,
        icon_panup,
        "panup",
        "&Pan Up",
        "Moves the view up.",
        "\0",
        panUp
    },
    {
        ACTION_pandown,
        icon_pandown,
        "pandown",
        "&Pan Down",
        "Moves the view down.",
        "\0",
        panDown
    },
    {
        ACTION_day,
        icon_day,
        "day",
        "&Day",
        "Updates the current view using day vision settings.",
        "\0",
        dayVision
    },
    {
        ACTION_night,
        icon_night,
        "night",
        "&Night",
        "Updates the current view using night vision settings.",
        "\0",
        nightVision
    }
};

#if 0
New for toolbars: modify and draw. Inquiry toolbar?

#define ACTION_circle      70
#define ACTION_line        71
#define ACTION_distance    72
#define ACTION_dolphin     73
#define ACTION_ellipse     74
#define ACTION_delete      75
#define ACTION_heart       76
#define ACTION_locatepoint 77

    {
        ACTION_circle,
        icon_circle,
        "circle",
        "&Circle",
        "Creates a circle:  CIRCLE",
        "\0",
        doNothing
    },
    {
        ACTION_line,
        icon_line,
        "line",
        "&Line",
        "Creates straight line segments:  LINE",
        "\0",
        doNothing
    },
    {
        ACTION_distance,
        icon_distance,
        "distance",
        "&Distance",
        "Measures the distance and angle between two points:  DIST",
        "\0",
        doNothing
    },
    {
        ACTION_dolphin,
        icon_dolphin,
        "dolphin",
        "&Dolphin",
        "Creates a dolphin:  DOLPHIN",
        "\0",
        doNothing
    },
    {
        ACTION_ellipse,
        icon_ellipse,
        "ellipse",
        "&Ellipse",
        "Creates a ellipse:  ELLIPSE",
        "\0",
        doNothing
    },
    {
        ACTION_delete,
        icon_erase,
        "delete",
        "D&elete",
        "Removes objects from a drawing:  DELETE",
        "\0",
        doNothing
    },
    {
        ACTION_heart,
        icon_heart,
        "&Heart",
        "Creates a heart:  HEART",
        "\0",
        doNothing
    },
    {
        ACTION_locatepoint,
        icon_locatepoint,
        "&Locate Point",
        "Displays the coordinate values of a location:  ID",
        "\0",
        doNothing
    },
    {
        ACTION_trebleclef,
        icon_trebleclef,
        "TrebleClef",
        "Creates a treble clef:  TREBLECLEF",
        "\0",
        doNothing
    },
    {
        ACTION_path,
        icon_path,
        "&Path",
        "Creates a 2D path:  PATH",
        "\0",
        doNothing
    },
    {
        ACTION_platform,
        icon_platform,
        "&Platform",
        "List which platform is in use:  PLATFORM",
        "\0",
        doNothing
    },
    {
        ACTION_point,
        icon_point,
        "&Point",
        "Creates multiple points:  POINT",
        "\0",
        doNothing
    },
    {
        ACTION_polygon,
        icon_polygon,
        "Pol&ygon",
        "Creates a regular polygon:  POLYGON",
        "\0",
        doNothing
    },
    {
        ACTION_polyline,
        icon_polyline,
        "&Polyline",
        "Creates a 2D polyline:  PLINE",
        "\0",
        doNothing
    },
    {
        ACTION_quickleader,
        icon_quickleader,
        "&QuickLeader",
        "Creates a leader and annotation:  QUICKLEADER",
        "\0",
        doNothing
    },
    {
        ACTION_rectangle,
        icon_rectangle,
        "&Rectangle",
        "Creates a rectangular polyline: RECTANGLE",
        "\0",
        doNothing
    },
    {
        ACTION_rgb,
        icon_rgb,
        "&RGB",
        "Updates the current view colors:  RGB",
        "\0",
        doNothing
    },
    {
        ACTION_move,
        icon_move,
        "&Move",
        "Displaces objects a specified distance in a specified direction: MOVE",
        "\0",
        doNothing
    },
    {
        ACTION_rotate,
        icon_rotate,
        "&Rotate",
        "Rotates objects about a base point:  ROTATE",
        "\0",
        doNothing
    },
    {
        ACTION_sandbox,
        icon_sandbox,
        "Sandbox",
        "A sandbox to play in:  SANDBOX",
        "\0",
        doNothing
    },
    {
        ACTION_scale,
        icon_scale,
        "Sca&le",
        "Enlarges or reduces objects proportionally in the X, Y, and Z directions:  SCALE",
        "\0",
        doNothing
    },
    {
        ACTION_selectall,
        icon_selectall,
        "&Select All",
        "Selects all objects:  SELECTALL",
        "\0",
        doNothing
    },
    {
        ACTION_singlelinetext,
        icon_singlelinetext,
        "&Single Line Text",
        "Creates single-line text objects:  TEXT",
        "\0",
        doNothing
    },
    {
        ACTION_snowflake,
        icon_snowflake,
        "&Snowflake",
        "Creates a snowflake:  SNOWFLAKE",
        "\0",
        doNothing
    },
    {
        ACTION_star,
        icon_star,
        "&Star",
        "Creates a star:  STAR",
        "\0",
        doNothing
    },
#endif

int n_property_editors = 8;

property_editor_row property_editors[] = {
/*
    create_lineedit_row(formLayout, ARC_AREA, "double", true, "blank", "Area");
    create_lineedit_row(formLayout, ARC_LENGTH, "double", true, "blank", "Length");
    create_lineedit_row(formLayout, ARC_CHORD, "double", true, "blank", "Chord");
    create_lineedit_row(formLayout, ARC_INC_ANGLE, "double", true, "blank", "Included Angle");
    ARC_CLOCKWISE, "int", true, "blank", "Clockwise", 



QGroupBox* PropertyEditor::createGroupBoxGeometryCircle()
{
    groupBoxGeometryCircle = new QGroupBox(tr("Geometry"), this);

    toolButtonCircleCenterX = createToolButton("blank", tr("Center X"));
    toolButtonCircleCenterY = createToolButton("blank", tr("Center Y"));
    toolButtonCircleRadius = createToolButton("blank", tr("Radius"));
    toolButtonCircleDiameter = createToolButton("blank", tr("Diameter"));
    toolButtonCircleArea = createToolButton("blank", tr("Area"));
    toolButtonCircleCircumference = createToolButton("blank", tr("Circumference"));

    lineEditCircleCenterX = createLineEdit("double", 0);
    lineEditCircleCenterY = createLineEdit("double", 0);
    lineEditCircleRadius = createLineEdit("double", 0);
    lineEditCircleDiameter = createLineEdit("double", 0);
    lineEditCircleArea = createLineEdit("double", 0);
    lineEditCircleCircumference = createLineEdit("double", 0);

    mapSignal(lineEditCircleCenterX, "lineEditCircleCenterX", OBJ_TYPE_CIRCLE);
    mapSignal(lineEditCircleCenterY, "lineEditCircleCenterY", OBJ_TYPE_CIRCLE);
    mapSignal(lineEditCircleRadius, "lineEditCircleRadius", OBJ_TYPE_CIRCLE);
    mapSignal(lineEditCircleDiameter, "lineEditCircleDiameter", OBJ_TYPE_CIRCLE);
    mapSignal(lineEditCircleArea, "lineEditCircleArea", OBJ_TYPE_CIRCLE);
    mapSignal(lineEditCircleCircumference, "lineEditCircleCircumference", OBJ_TYPE_CIRCLE);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonCircleCenterX, lineEditCircleCenterX);
    formLayout->addRow(toolButtonCircleCenterY, lineEditCircleCenterY);
    formLayout->addRow(toolButtonCircleRadius, lineEditCircleRadius);
    formLayout->addRow(toolButtonCircleDiameter, lineEditCircleDiameter);
    formLayout->addRow(toolButtonCircleArea, lineEditCircleArea);
    formLayout->addRow(toolButtonCircleCircumference, lineEditCircleCircumference);
    groupBoxGeometryCircle->setLayout(formLayout);

    return groupBoxGeometryCircle;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryDimAligned()
{
    groupBoxGeometryDimAligned = new QGroupBox(tr("Geometry"), this);

    //TODO: toolButtons and lineEdits for DimAligned

    return groupBoxGeometryDimAligned;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryDimAngular()
{
    groupBoxGeometryDimAngular = new QGroupBox(tr("Geometry"), this);

    //TODO: toolButtons and lineEdits for DimAngular

    return groupBoxGeometryDimAngular;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryDimArcLength()
{
    groupBoxGeometryDimArcLength = new QGroupBox(tr("Geometry"), this);

    //TODO: toolButtons and lineEdits for DimArcLength

    return groupBoxGeometryDimArcLength;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryDimDiameter()
{
    groupBoxGeometryDimDiameter = new QGroupBox(tr("Geometry"), this);

    //TODO: toolButtons and lineEdits for DimDiameter

    return groupBoxGeometryDimDiameter;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryDimLeader()
{
    groupBoxGeometryDimLeader = new QGroupBox(tr("Geometry"), this);

    //TODO: toolButtons and lineEdits for DimLeader

    return groupBoxGeometryDimLeader;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryDimLinear()
{
    groupBoxGeometryDimLinear = new QGroupBox(tr("Geometry"), this);

    //TODO: toolButtons and lineEdits for DimLinear

    return groupBoxGeometryDimLinear;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryDimOrdinate()
{
    groupBoxGeometryDimOrdinate = new QGroupBox(tr("Geometry"), this);

    //TODO: toolButtons and lineEdits for DimOrdinate

    return groupBoxGeometryDimOrdinate;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryDimRadius()
{
    groupBoxGeometryDimRadius = new QGroupBox(tr("Geometry"), this);

    //TODO: toolButtons and lineEdits for DimRadius

    return groupBoxGeometryDimRadius;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryImage()
{
    groupBoxGeometryImage = new QGroupBox(tr("Geometry"), this);

    toolButtonImageX = createToolButton("blank", tr("Position X"));
    toolButtonImageY = createToolButton("blank", tr("Position Y"));
    toolButtonImageWidth = createToolButton("blank", tr("Width"));
    toolButtonImageHeight = createToolButton("blank", tr("Height"));

    lineEditImageX = createLineEdit("double", 0);
    lineEditImageY = createLineEdit("double", 0);
    lineEditImageWidth = createLineEdit("double", 0);
    lineEditImageHeight = createLineEdit("double", 0);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonImageX, lineEditImageX);
    formLayout->addRow(toolButtonImageY, lineEditImageY);
    formLayout->addRow(toolButtonImageWidth, lineEditImageWidth);
    formLayout->addRow(toolButtonImageHeight, lineEditImageHeight);
    groupBoxGeometryImage->setLayout(formLayout);

    return groupBoxGeometryImage;
}

QGroupBox* PropertyEditor::createGroupBoxMiscImage()
{
    groupBoxMiscImage = new QGroupBox(tr("Misc"), this);

    toolButtonImageName = createToolButton("blank", tr("Name"));
    toolButtonImagePath = createToolButton("blank", tr("Path"));

    lineEditImageName = createLineEdit("double", 1);
    lineEditImagePath = createLineEdit("double", 1);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonImageName, lineEditImageName);
    formLayout->addRow(toolButtonImagePath, lineEditImagePath);
    groupBoxMiscImage->setLayout(formLayout);

    return groupBoxMiscImage;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryInfiniteLine()
{
    groupBoxGeometryInfiniteLine = new QGroupBox(tr("Geometry"), this);

    toolButtonInfiniteLineX1 = createToolButton("blank", tr("Start X"));
    toolButtonInfiniteLineY1 = createToolButton("blank", tr("Start Y"));
    toolButtonInfiniteLineX2 = createToolButton("blank", tr("2nd X"));
    toolButtonInfiniteLineY2 = createToolButton("blank", tr("2nd Y"));
    toolButtonInfiniteLineVectorX = createToolButton("blank", tr("Vector X"));
    toolButtonInfiniteLineVectorY = createToolButton("blank", tr("Vector Y"));

    lineEditInfiniteLineX1 = createLineEdit("double", 0);
    lineEditInfiniteLineY1 = createLineEdit("double", 0);
    lineEditInfiniteLineX2 = createLineEdit("double", 0);
    lineEditInfiniteLineY2 = createLineEdit("double", 0);
    lineEditInfiniteLineVectorX = createLineEdit("double", 1);
    lineEditInfiniteLineVectorY = createLineEdit("double", 1);

    //TODO: mapSignal for infinite lines

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonInfiniteLineX1, lineEditInfiniteLineX1);
    formLayout->addRow(toolButtonInfiniteLineY1, lineEditInfiniteLineY1);
    formLayout->addRow(toolButtonInfiniteLineX2, lineEditInfiniteLineX2);
    formLayout->addRow(toolButtonInfiniteLineY2, lineEditInfiniteLineY2);
    formLayout->addRow(toolButtonInfiniteLineVectorX, lineEditInfiniteLineVectorX);
    formLayout->addRow(toolButtonInfiniteLineVectorY, lineEditInfiniteLineVectorY);
    groupBoxGeometryInfiniteLine->setLayout(formLayout);

    return groupBoxGeometryInfiniteLine;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryLine()
{
    groupBoxGeometryLine = new QGroupBox(tr("Geometry"), this);

    toolButtonLineStartX = createToolButton("blank", tr("Start X"));
    toolButtonLineStartY = createToolButton("blank", tr("Start Y"));
    toolButtonLineEndX = createToolButton("blank", tr("End X"));
    toolButtonLineEndY = createToolButton("blank", tr("End Y"));
    toolButtonLineDeltaX = createToolButton("blank", tr("Delta X"));
    toolButtonLineDeltaY = createToolButton("blank", tr("Delta Y"));
    toolButtonLineAngle = createToolButton("blank", tr("Angle"));
    toolButtonLineLength = createToolButton("blank", tr("Length"));

    lineEditLineStartX = createLineEdit("double", 0);
    lineEditLineStartY = createLineEdit("double", 0);
    lineEditLineEndX = createLineEdit("double", 0);
    lineEditLineEndY = createLineEdit("double", 0);
    lineEditLineDeltaX = createLineEdit("double", 1);
    lineEditLineDeltaY = createLineEdit("double", 1);
    lineEditLineAngle = createLineEdit("double", 1);
    lineEditLineLength = createLineEdit("double", 1);

    mapSignal(lineEditLineStartX, "lineEditLineStartX", OBJ_TYPE_LINE);
    mapSignal(lineEditLineStartY, "lineEditLineStartY", OBJ_TYPE_LINE);
    mapSignal(lineEditLineEndX, "lineEditLineEndX", OBJ_TYPE_LINE);
    mapSignal(lineEditLineEndY, "lineEditLineEndY", OBJ_TYPE_LINE);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonLineStartX, lineEditLineStartX);
    formLayout->addRow(toolButtonLineStartY, lineEditLineStartY);
    formLayout->addRow(toolButtonLineEndX, lineEditLineEndX);
    formLayout->addRow(toolButtonLineEndY, lineEditLineEndY);
    formLayout->addRow(toolButtonLineDeltaX, lineEditLineDeltaX);
    formLayout->addRow(toolButtonLineDeltaY, lineEditLineDeltaY);
    formLayout->addRow(toolButtonLineAngle, lineEditLineAngle);
    formLayout->addRow(toolButtonLineLength, lineEditLineLength);
    groupBoxGeometryLine->setLayout(formLayout);

    return groupBoxGeometryLine;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryPath()
{
    groupBoxGeometryPath = new QGroupBox(tr("Geometry"), this);

    toolButtonPathVertexNum = createToolButton("blank", tr("Vertex #"));
    toolButtonPathVertexX = createToolButton("blank", tr("Vertex X"));
    toolButtonPathVertexY = createToolButton("blank", tr("Vertex Y"));
    toolButtonPathArea = createToolButton("blank", tr("Area"));
    toolButtonPathLength = createToolButton("blank", tr("Length"));

    comboBoxPathVertexNum = createComboBox(0);
    lineEditPathVertexX = createLineEdit("double", 0);
    lineEditPathVertexY = createLineEdit("double", 0);
    lineEditPathArea = createLineEdit("double", 1);
    lineEditPathLength = createLineEdit("double", 1);

    //TODO: mapSignal for paths

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonPathVertexNum, comboBoxPathVertexNum);
    formLayout->addRow(toolButtonPathVertexX, lineEditPathVertexX);
    formLayout->addRow(toolButtonPathVertexY, lineEditPathVertexY);
    formLayout->addRow(toolButtonPathArea, lineEditPathArea);
    formLayout->addRow(toolButtonPathLength, lineEditPathLength);
    groupBoxGeometryPath->setLayout(formLayout);

    return groupBoxGeometryPath;
}

QGroupBox* PropertyEditor::createGroupBoxMiscPath()
{
    groupBoxMiscPath = new QGroupBox(tr("Misc"), this);

    toolButtonPathClosed = createToolButton("blank", tr("Closed"));

    comboBoxPathClosed = createComboBox(0);

    //TODO: mapSignal for paths

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonPathClosed, comboBoxPathClosed);
    groupBoxMiscPath->setLayout(formLayout);

    return groupBoxMiscPath;
}


QGroupBox* PropertyEditor::createGroupBoxGeometryPolygon()
{
    groupBoxGeometryPolygon = new QGroupBox(tr("Geometry"), this);

    {
        OBJ_TYPE_POLYGON, POLYGON_CENTER_X,
        "double", 0, "blank", "Center X", LINE_EDIT_MODE, "lineEditPolygonCenterX"
    },
    {
        OBJ_TYPE_POLYGON, POLYGON_CENTER_Y,
        "double", 0, "blank", "Center Y", LINE_EDIT_MODE, "lineEditPolygonCenterY"
    },
    {
        OBJ_TYPE_POLYGON, POLYGON_VERTEX_RADIUS,
        "double", 0, "blank", "Vertex Radius", LINE_EDIT_MODE, "lineEditPolygonVertexRadius"
    }

    toolButtonPolygonRadiusSide = createToolButton("blank", tr("Side Radius"));
    toolButtonPolygonDiameterVertex = createToolButton("blank", tr("Vertex Diameter"));
    toolButtonPolygonDiameterSide = createToolButton("blank", tr("Side Diameter"));
    toolButtonPolygonInteriorAngle = createToolButton("blank", tr("Interior Angle"));

    lineEditPolygonRadiusSide = createLineEdit("double", 0);
    lineEditPolygonDiameterVertex = createLineEdit("double", 0);
    lineEditPolygonDiameterSide = createLineEdit("double", 0);
    lineEditPolygonInteriorAngle = createLineEdit("double", 1);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonPolygonRadiusSide, lineEditPolygonRadiusSide);
    formLayout->addRow(toolButtonPolygonDiameterVertex, lineEditPolygonDiameterVertex);
    formLayout->addRow(toolButtonPolygonDiameterSide, lineEditPolygonDiameterSide);
    formLayout->addRow(toolButtonPolygonInteriorAngle, lineEditPolygonInteriorAngle);
    groupBoxGeometryPolygon->setLayout(formLayout);

    return groupBoxGeometryPolygon;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryPolyline()
{
    groupBoxGeometryPolyline = new QGroupBox(tr("Geometry"), this);

    toolButtonPolylineVertexNum = createToolButton("blank", tr("Vertex #"));
    toolButtonPolylineVertexX = createToolButton("blank", tr("Vertex X"));
    toolButtonPolylineVertexY = createToolButton("blank", tr("Vertex Y"));
    toolButtonPolylineArea = createToolButton("blank", tr("Area"));
    toolButtonPolylineLength = createToolButton("blank", tr("Length"));

    comboBoxPolylineVertexNum = createComboBox(0);
    lineEditPolylineVertexX = createLineEdit("double", 0);
    lineEditPolylineVertexY = createLineEdit("double", 0);
    lineEditPolylineArea = createLineEdit("double", 1);
    lineEditPolylineLength = createLineEdit("double", 1);

    //TODO: mapSignal for polylines

    QFormLayout* formLayout = new QFormLayout(this);
    "comboBoxPolylineVertexNum"
    "lineEditPolylineVertexX"
    "lineEditPolylineVertexY"
    "lineEditPolylineArea"
    "lineEditPolylineLength"
    groupBoxGeometryPolyline->setLayout(formLayout);

    return groupBoxGeometryPolyline;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryRay()
{
    toolButtonRayX2 = createToolButton();
    toolButtonRayY2 = createToolButton("blank", tr("2nd Y"));
    toolButtonRayVectorX = createToolButton("blank", tr("Vector X"));
    toolButtonRayVectorY = createToolButton("blank", tr("Vector Y"));

    "blank", "Start X", "double", 0, "lineEditRayX1"
    "blank", "Start Y", "double", 0, "lineEditRayY1"
    "blank", "2nd X", "double", 0, "lineEditRayX2"
    "blank", "2nd Y", "double", 0, "lineEditRayY2"
    "blank", "Vector X", "double", 1, "lineEditRayVectorX"
    "double", 1, "lineEditRayVectorY"
}

QGroupBox* PropertyEditor::createGroupBoxGeometryTextMulti()
{
    groupBoxGeometryTextMulti = new QGroupBox(tr("Geometry"), this);

    toolButtonTextMultiX = createToolButton("blank", tr("Position X"));
    toolButtonTextMultiY = createToolButton("blank", tr("Position Y"));

    lineEditTextMultiX = createLineEdit("double", 0);
    lineEditTextMultiY = createLineEdit("double", 0);


    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonTextMultiX, lineEditTextMultiX);
    formLayout->addRow(toolButtonTextMultiY, lineEditTextMultiY);
    groupBoxGeometryTextMulti->setLayout(formLayout);

    return groupBoxGeometryTextMulti;
}

QGroupBox* PropertyEditor::createGroupBoxTextTextSingle()
{
    groupBoxTextTextSingle = new QGroupBox(tr("Text"), this);

    {
        "blank",
        "Contents",
        "toolButtonTextSingleContents"
    },
    toolButtonTextSingleFont = createToolButton("blank", tr("Font"));
    toolButtonTextSingleJustify = createToolButton("blank", tr("Justify"));
    toolButtonTextSingleHeight = createToolButton("blank", tr("Height"));
    toolButtonTextSingleRotation = createToolButton("blank", tr("Rotation"));

    lineEditTextSingleContents = createLineEdit("string", 0);
    comboBoxTextSingleFont = createFontComboBox(0);
    comboBoxTextSingleJustify = createComboBox(0);
    lineEditTextSingleHeight = createLineEdit("double", 0);
    lineEditTextSingleRotation = createLineEdit("double", 0);

    mapSignal(lineEditTextSingleContents, "lineEditTextSingleContents", OBJ_TYPE_TEXTSINGLE);
    mapSignal(comboBoxTextSingleFont, "comboBoxTextSingleFont", OBJ_TYPE_TEXTSINGLE);
    mapSignal(comboBoxTextSingleJustify, "comboBoxTextSingleJustify", OBJ_TYPE_TEXTSINGLE);
    mapSignal(lineEditTextSingleHeight, "lineEditTextSingleHeight", OBJ_TYPE_TEXTSINGLE);
    mapSignal(lineEditTextSingleRotation, "lineEditTextSingleRotation", OBJ_TYPE_TEXTSINGLE);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonTextSingleContents, lineEditTextSingleContents);
    formLayout->addRow(toolButtonTextSingleFont, comboBoxTextSingleFont);
    formLayout->addRow(toolButtonTextSingleJustify, comboBoxTextSingleJustify);
    formLayout->addRow(toolButtonTextSingleHeight, lineEditTextSingleHeight);
    formLayout->addRow(toolButtonTextSingleRotation, lineEditTextSingleRotation);
    groupBoxTextTextSingle->setLayout(formLayout);

    return groupBoxTextTextSingle;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryTextSingle()
{
    groupBoxGeometryTextSingle = new QGroupBox(tr("Geometry"), this);

    toolButtonTextSingleX = createToolButton("blank", tr("Position X"));
    toolButtonTextSingleY = createToolButton("blank", tr("Position Y"));

    lineEditTextSingleX = createLineEdit("double", 0);
    lineEditTextSingleY = createLineEdit("double", 0);

    mapSignal(lineEditTextSingleX, "lineEditTextSingleX", OBJ_TYPE_TEXTSINGLE);
    mapSignal(lineEditTextSingleY, "lineEditTextSingleY", OBJ_TYPE_TEXTSINGLE);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonTextSingleX, lineEditTextSingleX);
    formLayout->addRow(toolButtonTextSingleY, lineEditTextSingleY);
    groupBoxGeometryTextSingle->setLayout(formLayout);

    return groupBoxGeometryTextSingle;
}

QGroupBox* PropertyEditor::createGroupBoxMiscTextSingle()
{
    groupBoxMiscTextSingle = new QGroupBox(tr("Misc"), this);

    toolButtonTextSingleBackward = createToolButton("blank", tr("Backward"));
    toolButtonTextSingleUpsideDown = createToolButton("blank", tr("UpsideDown"));

    comboBoxTextSingleBackward = createComboBox(0);
    comboBoxTextSingleUpsideDown = createComboBox(0);

    mapSignal(comboBoxTextSingleBackward, "comboBoxTextSingleBackward", OBJ_TYPE_TEXTSINGLE);
    mapSignal(comboBoxTextSingleUpsideDown, "comboBoxTextSingleUpsideDown", OBJ_TYPE_TEXTSINGLE);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonTextSingleBackward, comboBoxTextSingleBackward);
    formLayout->addRow(toolButtonTextSingleUpsideDown, comboBoxTextSingleUpsideDown);
    groupBoxMiscTextSingle->setLayout(formLayout);

    return groupBoxMiscTextSingle;
}

*/
    {
        /* 0 */
        OBJ_TYPE_ARC, ARC_CENTER_X,
        "double", 0, "blank", "Center X", LINE_EDIT_TYPE, "lineEditArcCenterX"
    },
    {
        /* 1 */
        OBJ_TYPE_ARC, ARC_CENTER_Y,
        "double", 0, "blank", "Center Y", LINE_EDIT_TYPE, "lineEditArcCenterY"
    },
    {
        /* 2 */
        OBJ_TYPE_ARC, ARC_RADIUS,
        "double", 0, "blank", "Radius", LINE_EDIT_TYPE, "lineEditArcRadius"
    },
    {
        /* 3 */
        OBJ_TYPE_ARC, ARC_START_ANGLE,
        "double", 0, "blank", "Start Angle", LINE_EDIT_TYPE, "lineEditArcStartAngle"
    },
    {
        /* 4 */
        OBJ_TYPE_ARC, ARC_END_ANGLE,
        "double", 0, "blank", "End Angle", LINE_EDIT_TYPE, "lineEditArcEndAngle"
    },
    {
        /* 5 */
        OBJ_TYPE_ARC, ARC_START_X,
        "double", 1, "blank", "Start X", LINE_EDIT_TYPE, "lineEditArcStartX"
    },
    {
        /* 6 */
        OBJ_TYPE_ARC, ARC_START_Y,
        "double", 1, "blank", "Start Y", LINE_EDIT_TYPE, "lineEditArcStartY"
    },
    {
        /* 7 */
        OBJ_TYPE_ARC, ARC_END_X,
        "double", 1, "blank", "End X", LINE_EDIT_TYPE, "lineEditArcEndX"
    },
    {
        /* 8 */
        OBJ_TYPE_ARC, ARC_END_Y,
        "double", 1, "blank", "End Y", LINE_EDIT_TYPE, "lineEditArcEndY"
    },
    {
        /* 9 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_CENTER_X,
        "double", 0, "blank", "Center X", LINE_EDIT_TYPE, "lineEditEllipseCenterX"
    },
    {
        /* 10 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_CENTER_Y,
        "double", 0, "blank", "Center Y", LINE_EDIT_TYPE, "lineEditEllipseCenterY"
    },
    {
        /* 11 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_RADIUS_MAJOR,
        "double", 0, "blank", "Radius Major", LINE_EDIT_TYPE, "lineEditEllipseRadiusMajor"
    },
    {
        /* 12 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_RADIUS_MINOR,
        "double", 0, "blank", "Radius Minor", LINE_EDIT_TYPE, "lineEditEllipseRadiusMinor"
    },
    {
        /* 13 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_DIAMETER_MAJOR,
        "double", 0, "blank", "Diameter Major", LINE_EDIT_TYPE, "lineEditEllipseDiameterMajor"
    },
    {
        /* 14 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_DIAMETER_MINOR,
        "double", 0, "blank", "Diameter Minor", LINE_EDIT_TYPE, "lineEditEllipseDiameterMinor"
    },
    {
        /* 15 */
        OBJ_TYPE_BLOCK, BLOCK_X,
        "double", 0, "blank", "Position X", LINE_EDIT_TYPE, "lineEditBlockX"
    },
    {
        /* 16 */
        OBJ_TYPE_BLOCK, BLOCK_Y,
        "double", 0, "blank", "Position Y", LINE_EDIT_TYPE, "lineEditBlockY"
    },
    {
        /* 17 */
        OBJ_TYPE_POINT, POINT_X,
        "double", 0, "blank", "Position X", LINE_EDIT_TYPE, "lineEditPointX"
    },
    {
        /* 18 */
        OBJ_TYPE_POINT, POINT_Y,
        "double", 0, "blank", "Position Y", LINE_EDIT_TYPE, "lineEditPointY"
    },
    {
        /* 19 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_X1,
        "double", 0, "blank", "Corner 1 X", LINE_EDIT_TYPE, "lineEditRectangleCorner1X"
    },
    {
        /* 20 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_Y1,
        "double", 0, "blank", "Corner 1 Y", LINE_EDIT_TYPE, "lineEditRectangleCorner1Y"
    },
    {
        /* 21 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_X2,
        "double", 0, "blank", "Corner 2 X", LINE_EDIT_TYPE, "lineEditRectangleCorner2X"
    },
    {
        /* 22 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_Y2,
        "double", 0, "blank", "Corner 2 Y", LINE_EDIT_TYPE, "lineEditRectangleCorner2Y"
    },
    {
        /* 23 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_X3,
        "double", 0, "blank", "Corner 3 X", LINE_EDIT_TYPE, "lineEditRectangleCorner3X"
    },
    {
        /* 24 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_Y3,
        "double", 0, "blank", "Corner 3 Y", LINE_EDIT_TYPE, "lineEditRectangleCorner3Y"
    },
    {
        /* 25 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_X4,
        "double", 0, "blank", "Corner 4 X", LINE_EDIT_TYPE, "lineEditRectangleCorner4X"
    },
    {
        /* 26 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_Y4,
        "double", 0, "blank", "Corner 4 Y", LINE_EDIT_TYPE, "lineEditRectangleCorner4Y"
    },
    {
        /* 27 */
        OBJ_TYPE_RECTANGLE, RECT_WIDTH,
        "double", 0, "blank", "Width", LINE_EDIT_TYPE, "lineEditRectangleWidth"
    },
    {
        /* 28 */
        OBJ_TYPE_RECTANGLE, RECT_HEIGHT,
        "double", 0, "blank", "Height", LINE_EDIT_TYPE, "lineEditRectangleHeight"
    },
    {
        /* 29 */
        OBJ_TYPE_RECTANGLE, RECT_AREA,
        "double", 1, "blank", "Area", LINE_EDIT_TYPE, "lineEditRectangleArea"
    },
    {
        /* END */
        OBJ_TYPE_UNKNOWN, 0,
        "NULL", 0, "NULL", "NULL", 0, "NULL"
    }
};

