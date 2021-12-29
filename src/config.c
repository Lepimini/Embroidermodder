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
    ACTION_undo,
    ACTION_redo,
    -1,
    ACTION_help,
    -2
};

int edit_menu[] = {
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

int layer_menu[] = {
    -2
};

int text_menu[] = {
    -2
};

int properties_menu[] = {
    -2
};

int *menus[] = {
    file_menu,
    edit_menu,
    view_menu,
    zoom_menu,
    pan_menu,
    icon_menu,
    help_menu,
    layer_menu,
    text_menu,
    properties_menu
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

int n_toolbars = 10;
int n_menus = 10;

path_symbol icon_zero[] = {
    /* path.addEllipse(QPointF(x+0.25*xScale, y-0.50*yScale), 0.25*xScale, 0.50*yScale); */
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
        ACTION_donothing,
        icon_donothing,
        "donothing",
        "&Do Nothing",
        "Does nothing."
    },
    {
        ACTION_windowcascade,
        icon_windowcascade,
        "windowcascade",
        "&Cascade",
        "Cascade the windows."
    },
    {
         ACTION_windowtile,
         icon_windowtile,
         "windowtile",
         "&Tile",
         "Tile the windows."
    },
    {
        ACTION_windowclose,
        icon_windowclose,
        "windowclose",
        "Cl&ose",
        "Close the active window."
    },
    {
        ACTION_windowcloseall,
        icon_windowcloseall,
        "windowcloseall",
        "Close &All",
        "Close all the windows."
    },
    {
        ACTION_windownext,
        icon_windownext,
        "windownext",
        "Ne&xt",
        "Move the focus to the next window."
    },
    {
        ACTION_windowprevious,
        icon_windowprevious,
        "windowprevious",
        "Pre&vious",
        "Move the focus to the previous window."
    },
    {
        ACTION_new,
        icon__new,
        "new",
        "&New",
        "Create a new file."
    },
    {
        ACTION_open,
        icon_open,
        "open",
        "&Open",
        "Open an existing file."
    },
    {
        ACTION_save,
        icon_save,
        "save",
        "&Save",
        "Save the design to disk."
    },
    {
        ACTION_saveas,
        icon_saveas,
        "saveas",
        "Save &As",
        "Save the design under a new name."
    },
    {
        ACTION_print,
        icon_print,
        "print",
        "&Print",
        "Print the design."
    },
    {
        ACTION_designdetails,
        icon_designdetails,
        "designdetails",
        "&Details",
        "Details of the current design."
    },
    {
        ACTION_exit,
        icon_exit,
        "exit",
        "E&xit",
        "Exit the application."
    },
    {
        ACTION_cut,
        icon_cut,
        "cut",
        "Cu&t",
        "Cut the current selection's contents to the clipboard."
    },
    {
        ACTION_copy,
        icon_copy,
        "copy",
        "&Copy",
        "Copy the current selection's contents to the clipboard."
    },
    {
        ACTION_paste,
        icon_paste,
        "paste",
        "&Paste",
        "Paste the clipboard's contents into the current selection."
    },
    {
        ACTION_help,
        icon_help,
        "help",
        "&Help",
        "Displays help."
    },
    {
        ACTION_changelog,
        icon_changelog,
        "changelog",
        "&Changelog",
        "Describes new features in this product."
    },
    {
        ACTION_tipoftheday,
        icon_tipoftheday,
        "tipoftheday",
        "&Tip Of The Day",
        "Displays a dialog with useful tips"
    },
    {
        ACTION_about,
        icon_about,
        "about",
        "&About Embroidermodder 2",
        "Displays information about this product."
    },
    {
        ACTION_whatsthis,
        icon_whatsthis,
        "whatsthis",
        "&What's This?",
        "What's This? Context Help!"
    },
    {
        ACTION_undo,
        icon_undo,
        "undo",
        "&Undo",
        "Reverses the most recent action."
    },
    {
        ACTION_redo,
        icon_redo,
        "redo",
        "&Redo",
        "Reverses the effects of the previous undo action."
    },
    {
        ACTION_icon16,
        icon_icon16,
        "icon16",
        "Icon&16",
        "Sets the toolbar icon size to 16x16."
    },
    {
        ACTION_icon24,
        icon_icon24,
        "icon24",
        "Icon&24",
        "Sets the toolbar icon size to 24x24."
    },
    {
        ACTION_icon32,
        icon_icon32,
        "icon32",
        "Icon&32",
        "Sets the toolbar icon size to 32x32."
    },
    {
        ACTION_icon48,
        icon_icon48,
        "icon48",
        "Icon&48",
        "Sets the toolbar icon size to 48x48."
    },
    {
        ACTION_icon64,
        icon_icon64,
        "icon64",
        "Icon&64",
        "Sets the toolbar icon size to 64x64."
    },
    {
        ACTION_icon128,
        icon_icon128,
        "icon128",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128."
    },
    {
        ACTION_settingsdialog,
        icon_settingsdialog,
        "settingsdialog",
        "&Settings",
        "Configure settings specific to this product."
    },
    {
       ACTION_makelayercurrent,
       icon_makelayercurrent,
       "makelayercurrent",
       "&Make Layer Active",
       "Makes the layer of a selected object the active layer"
    },
    {
        ACTION_layers,
        icon_layers,
        "layers",
        "&Layers",
        "Manages layers and layer properties:  LAYER"
    },
    {
        ACTION_layerselector,
        icon_layerselector,
        "layerselector",
        "&Layer Selector",
        "Dropdown selector for changing the current layer"
    },
    {
        ACTION_layerprevious,
        icon_layerprevious,
        "layerprevious",
        "&Layer Previous",
        "Restores the previous layer settings:  LAYERP"
    },
    {
        ACTION_colorselector,
        icon_colorselector,
        "colorselector",
        "&Color Selector",
        "Dropdown selector for changing the current thread color"
    },
    {
        ACTION_linetypeselector,
        icon_linetypeselector,
        "linetypeselector",
        "&Stitchtype Selector",
        "Dropdown selector for changing the current stitch type"
    },
    {
        ACTION_lineweightselector,
        icon_lineweightselector,
        "lineweightselector",
        "&Threadweight Selector",
        "Dropdown selector for changing the current thread weight"
    },
    {
        ACTION_hidealllayers,
        icon_hidealllayers,
        "hidealllayers",
        "&Hide All Layers",
        "Turns the visibility off for all layers in the current drawing:  HIDEALL"
    },
    {
        ACTION_showalllayers,
        icon_showalllayers,
        "showalllayers",
        "&Show All Layers",
        "Turns the visibility on for all layers in the current drawing:  SHOWALL"
    },
    {
        ACTION_freezealllayers,
        icon_freezealllayers,
        "freezealllayers",
        "&Freeze All Layers",
        "Freezes all layers in the current drawing:  FREEZEALL"
    },
    {
        ACTION_thawalllayers,
        icon_thawalllayers,
        "thawalllayers",
        "&Thaw All Layers",
        "Thaws all layers in the current drawing:  THAWALL"
    },
    {
        ACTION_lockalllayers,
        icon_lockalllayers,
        "lockalllayers",
        "&Lock All Layers",
        "Locks all layers in the current drawing:  LOCKALL"
    },
    {
        ACTION_unlockalllayers,
        icon_unlockalllayers,
        "unlockalllayers",
        "&Unlock All Layers",
        "Unlocks all layers in the current drawing:  UNLOCKALL"
    },
    {
        ACTION_textbold,
        icon_textbold,
        "textbold",
        "&Bold Text",
        "Sets text to be bold."
    },
    {
        ACTION_textitalic,
        icon_textitalic,
        "textitalic",
        "&Italic Text",
        "Sets text to be italic."
    },
    {
        ACTION_textoverline,
        icon_textoverline,
        "textunderline",
        "&Underline Text",
        "Sets text to be underlined."
    },
    {
        ACTION_textstrikeout,
        icon_textstrikeout,
        "textstrikeout",
        "&StrikeOut Text",
        "Sets text to be striked out."
    },
    {
        ACTION_textoverline,
        icon_textoverline,
        "textoverline",
        "&Overline Text",
        "Sets text to be overlined."
    },
    {
        ACTION_zoomrealtime,
        icon_zoomrealtime,
        "zoomrealtime",
        "Zoom &Realtime",
        "Zooms to increase or decrease the apparent size of objects in the current viewport."
    },
    {
        ACTION_zoomprevious,
        icon_zoomprevious,
        "zoomprevious",
        "Zoom &Previous",
        "Zooms to display the previous view."
    },
    {
        ACTION_zoomwindow,
        icon_zoomwindow,
        "zoomwindow",
        "Zoom &Window",
        "Zooms to display an area specified by a rectangular window."
    },
    {
        ACTION_zoomdynamic,
        icon_zoomdynamic,
        "zoomdynamic",
        "Zoom &Dynamic",
        "Zooms to display the generated portion of the drawing."
    },
    {
        ACTION_zoomscale,
        icon_zoomscale,
        "zoomscale",
        "Zoom &Scale",
        "Zooms the display using a specified scale factor."
    },
    {
        ACTION_zoomcenter,
        icon_zoomcenter,
        "zoomcenter",
        "Zoom &Center",
        "Zooms to display a view specified by a center point and magnification or height."
    },
    {
        ACTION_zoomin,
        icon_zoomin,
        "zoomin",
        "Zoom &In",
        "Zooms to increase the apparent size of objects."
    },
    {
        ACTION_zoomout,
        icon_zoomout,
        "zoomout",
        "Zoom &Out",
        "Zooms to decrease the apparent size of objects."
    },
    {
        ACTION_zoomselected,
        icon_zoomselected,
        "zoomselected",
        "Zoom Selec&ted",
        "Zooms to display the selected objects."
    },
    {
        ACTION_zoomall,
        icon_zoomall,
        "zoomall",
        "Zoom &All",
        "Zooms to display the drawing extents or the grid limits."
    },
    {
        ACTION_zoomextents,
        icon_zoomextents,
        "zoomextents",
        "Zoom &Extents",
        "Zooms to display the drawing extents."
    },
    {
        ACTION_panrealtime,
        icon_panrealtime,
        "panrealtime",
        "&Pan Realtime",
        "Moves the view in the current viewport."
    },
    {
        ACTION_panpoint,
        icon_panpoint,
        "panpoint",
        "&Pan Point",
        "Moves the view by the specified distance."
    },
    {
        ACTION_panleft,
        icon_panleft,
        "panleft",
        "&Pan Left",
        "Moves the view to the left."
    },
    {
        ACTION_panright,
        icon_panright,
        "panright",
        "&Pan Right",
        "Moves the view to the right."
    },
    {
        ACTION_panup,
        icon_panup,
        "panup",
        "&Pan Up",
        "Moves the view up."
    },
    {
        ACTION_pandown,
        icon_pandown,
        "pandown",
        "&Pan Down",
        "Moves the view down."
    },
    {
        ACTION_day,
        icon_day,
        "day",
        "&Day",
        "Updates the current view using day vision settings."
    },
    {
        ACTION_night,
        icon_night,
        "night",
        "&Night",
        "Updates the current view using night vision settings."
    }
};

