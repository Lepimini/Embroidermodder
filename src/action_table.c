/* 
 *  Embroidermodder 2.
 *
 *  ------------------------------------------------------------
 *
 *  Copyright 2013-2022 The Embroidermodder Team
 *  Embroidermodder 2 is Open Source Software.
 *  See LICENSE for licensing terms.
 *
 *  ------------------------------------------------------------
 *
 *  The action table.
 */

#include "em2.h"

Action action_list[] = {
    {
        "do-nothing",
        scm_do_nothing,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "Do &Nothing",
        "An action that intensionally does nothing."
    },
    {
        "debug-message",
        scm_debug_message,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "Debug &Message",
        "Prints to the console (that the program is launched from) any debugging information."
    },
    {
        "new-file",
        scm_new_file,
        "Null",
        "user",
        0,
        "assets/icons/new.png",
        "&New",
        "Create a new file in a new tab."
    },
    {
        "open-file",
        scm_open_file,
        "Null",
        "user",
        0,
        "assets/icons/open.png",
        "&Open",
        "Open an existing file."
    },
    {
        "save-file",
        scm_save_file,
        "Null",
        "user",
        0,
        "assets/icons/save.png",
        "&Save",
        "Save the design to disk."
    },
    {
        "save-file-as",
        scm_save_file_as,
        "Null",
        "user",
        0,
        "assets/icons/save_as.png",
        "&Save File As...",
        "Save the design under a new name and/or format."
    },
    {
        "check-for-updates",
        scm_check_for_updates,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "Check for &Updates",
        "NULL"
    },
    {
        "select-all",
        scm_select_all,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "Select &All",
        "NULL"
    },
    {
        "whats-this",
        scm_whats_this,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "design-details",
        scm_design_details,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "print-pattern",
        scm_print_pattern,
        "Null",
        "user",
        0,
        "assets/icons/print.png",
        "&Print",
        "Opens the print dialog to print pattern information and images."
    },
    {
        "exit-program",
        scm_exit_program,
        "Null",
        "user",
        0,
        "assets/icons/exit.png",
        "E&xit",
        "Exit the application."
    },
    {
        "cut-object",
        scm_cut,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "copy-object",
        scm_copy,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "paste-object",
        scm_paste,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "undo",
        scm_undo,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "redo",
        scm_redo,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "window-close",
        scm_window_close,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "window-close-all",
        scm_window_close_all,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "window-cascade",
        scm_window_cascade,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "window-tile",
        scm_window_tile,
        "Null",
        "user",
        0,
        "NULL",
        "NULL",
        "Tiles the windows"
    },
    {
        "window-next",
        scm_window_next,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "window-previous",
        scm_window_previous,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "help",
        scm_help,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "changelog-dialog",
        scm_changelog,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "tip-of-the-day-dialog",
        scm_tip_of_the_day,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "about-dialog",
        scm_about,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "icon-16",
        scm_icon_16,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "icon-24",
        scm_icon_24,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "icon-32",
        scm_icon_32,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "icon-48",
        scm_icon_48,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "icon-64",
        scm_icon_64,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "icon-128",
        scm_icon_128,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "settings-dialog",
        scm_settings_dialog,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "make-layer-current",
        scm_make_layer_current,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "layers",
        scm_layers,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "layer-selector",
        scm_layer_selector,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "layer-previous",
        scm_layer_previous,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "color-selector",
        scm_color_selector,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "line-type-selector",
        scm_line_type_selector,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_line_weight_selector,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_hide_all_layers,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_show_all_layers,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_freeze_all_layers,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_thaw_all_layers,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_lock_all_layers,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_unlock_all_layers,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_text_bold,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_text_italic,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_text_underline,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "text-strikeout",
        scm_text_strikeout,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "text-overline",
        scm_text_overline,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_zoom_real_time,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_zoom_previous,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_zoom_window,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_zoom_dynamic,
        "Null",
        "user",
        0,
        "assets/icons/do_nothing.png",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_zoom_scale,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_zoom_center,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_zoom_in,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_zoom_out,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_zoom_selected,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_zoom_all,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "zoom-extents",
        scm_zoom_extents,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "pan-real-time",
        scm_pan_real_time,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "pan-point",
        scm_pan_point,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "pan-left",
        scm_pan_left,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_pan_right,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_pan_up,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "pan-down",
        scm_pan_down,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "day-vision",
        scm_day_vision,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "night-vision",
        scm_night_vision,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_treble_clef,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_path,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_circle,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "",
        scm_line,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "distance",
        scm_distance,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "dolphin",
        scm_dolphin,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "ellipse",
        scm_ellipse,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "delete-object",
        scm_delete_object,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "heart",
        scm_heart,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "locate-point",
        scm_locate_point,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    },
    {
        "END",
        NULL,
        "NULL",
        "NULL",
        0,
        "NULL",
        "NULL",
        "NULL"
    }
};

/*
    {
        "Null", "user", "0",
        "assets/icons/histogram.png",
        "design_details",
        "&Design Details",
        "Show the design details dialog for the current design."
    },
    {
        "Null", "user", "0",
        "assets/icons/cut.png",
        "cut",
        "Cu&t",
        "Cut the current selection's contents to the clipboard."
    },
    {
        "Null", "user", "0",
        "assets/icons/copy.png",
        "copy",
        "&Copy",
        "Copy the current selection's contents to the clipboard."
    },
    {
        "Null", "user", "0",
        "assets/icons/paste.png",
        "paste",
        "&Paste",
        "Paste the clipboard contents into the selection within the scene."
    },
    {
        "Null", "user", "0",
        "assets/icons/undo.png",
        "undo",
        "&Undo",
        "Reverses the most recent action."
    },
    {
        "Null", "user", "0",
        "assets/icons/redo.png",
        "redo",
        "&Redo",
        "Reverses the effects of the previous undo action."
    },
    {
        "Null", "user", "0",
        "assets/icons/windowclose.png",
        "window_close",
        "Cl&ose",
        "Close the active window."
    },
    {
        "Null", "user", "0",
        "assets/icons/windowcloseall.png",
        "window_close_all",
        "Close &All",
        "Close all the windows."
    },
    {
        "Null", "user", "0",
        "assets/icons/windowcascade.png",
        "window_cascade",
        "&Cascade",
        "Cascade the windows."
    },
    {
        "Null", "user", "0",
        "assets/icons/windowtile.png",
        "window_tile",
        "&Tile",
        "Tile the windows."
    },
    {
        "Null", "user", "0",
        "assets/icons/windownext.png",
        "window_next",
        "Ne&xt",
        "Move the focus to the next window."
    },
    {
        "Null", "user", "0",
        "assets/icons/windowprevious.png",
        "window_previous",
        "Pre&vious",
        "Move the focus to the previous window."
    },
    {
        "Null", "user", "0",
        "assets/icons/help.png",
        "help",
        "&Help",
        "Displays help."
    },
    {
        "Null", "user", "0",
        "assets/icons/changelog.png",
        "changelog",
        "&Changelog",
        "Opens a log of recent, new features in this product."
    },
    {
        "Null", "user", "0",
        "assets/icons/tipoftheday.png",
        "tip of the day",
        "&Tip Of The Day",
        "Displays a dialog with useful tips."
    },
    {
        "Null", "user", "0",
        "assets/icons/about.png",
        "about",
        "&About Embroidermodder 2",
        "Displays information about this product."
    },
    {
        "Null", "user", "0",
        "assets/icons/whatsthis.png",
        "what's this",
        "&What's This?",
        "What's This? Context Help!"
    },
    {
        "Null", "user", "0",
        "assets/icons/icon16.png",
        "icon_16",
        "Icon&16",
        "Sets the toolbar icon size to 16x16."
    },
    {
        "Null", "user", "0",
        "assets/icons/help.png",
        "icon24",
        "Icon&24",
        "."
    },
    {
        "Null", "user", "0",
        "assets/icons/icon32.png",
        "icon32"
        "Icon&32"
        "Sets the toolbar icon size to 32x32."
    },
    {
        "Null", "user", "0",
        "assets/icons/icon48.png"
        "icon48"
        "Icon&48"
        "Sets the toolbar icon size to 48x48."
    },
    {
        "Null", "user", "0",
        "assets/icons/icon64.png",
        "icon64",
        "Icon&64",
        "Sets the toolbar icon size to 64x64."
    },
    {
        "Null", "user", "0",
        "assets/icons/icon128.png",
        "icon128"
        "Icon12&8"
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "icon128.png",
        "icon128",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "assets/icons/icon128.png",
        "make_layer_current",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "assets/icons/icon128.png",
        "layers",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "assets/icons/icon128.png",
        "layer_selector",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "assets/icons/icon128.png",
        "layer_previous",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "icon128.png",
        "color_selector",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "assets/icons/icon128.png",
        "linetype_selector",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "assets/icons/icon128.png",
        "lineweight_selector",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "assets/icons/icon128.png",
        "hide_all_layers",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "assets/icons/icon128.png",
        "show_all_layers",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "assets/icons/freezealllayers.png",
        "freeze_all_layers",
        "&Freeze All Layers",
        "Freezes all layers in the current drawing: freeze_all_layers"
    },
    {
        "Null", "user", "0",
        "assets/icons/thawalllayers.png",
        "thaw_all_layers",
        "&Thaw All Layers",
        "Thaws all layers in the current drawing: thaw_all_layers"
    },
    {
        "Null", "user", "0",
        "assets/icons/lockalllayers.png",
        "lock_all_layers",
        "&Lock All Layers",
        "Locks all layers in the current drawing: LOCKALL"
    },
    {
        "Null", "user", "0",
        "assets/icons/textbold.png",
        "text_bold",
        "Text &Bold",
        "Sets the text to be bold."
    },
    {
        "Null", "user", "0",
        "assets/icons/textitalic.png",
        "text_italic",
        "&Italic Text",
        "Sets text to be italic."
    },
    {
        "Null", "user",
        "0",
        "assets/icons/textoverline.png",
        "text_underline",
        "&Underline Text",
        "Sets text to be underlined."
    },
    {
        "Null", "user",
        "0",
        "assets/icons/textstrikeout.png",
        "text_strikeout",
        "&StrikeOut Text",
        "Sets text to be striked out."
    },
    {
        "Null", "user", "0",
        "assets/icons/textoverline.png",
        "text_overline",
        "&Overline Text",
        "Sets text to be overlined."
    },
    {
        "Null", "user", "0",
        "assets/icons/zoomrealtime.png",
        "zoom_real_time",
        "Zoom &Realtime",
        "Zooms to increase or decrease the apparent size of objects in the current viewport."
    },
    {
        "Null", "user", "0",
        "assets/icons/zoomprevious.png",
        "zoom_previous",
        "Zoom &Previous",
        "Zooms to display the previous view."
    },
    {
        "Null", "user", "0",
        "assets/icons/zoomwindow.png",
        "zoom_window",
        "Zoom &Window",
        "Zooms to display an area specified by a rectangular window."
    },
    {
        "Null", "user", "0",
        "assets/icons/zoomdynamic.png",
        "zoom_dynamic",
        "Zoom &Dynamic",
        "Zooms to display the generated portion of the drawing."
    },
    {
        "Null", "user", "0",
        "assets/icons/scale.png",
        "zoom_scale",
        "Zoom Sca&le",
        "Enlarges or reduces objects proportionally in the X, Y, and Z directions: SCALE"
    },
    {
        "Null", "user", "0",
        "assets/icons/zoomcenter.png",
        "zoom_center",
        "Zoom &Center",
        "Zooms to display a view specified by a center point and  magnification or height."
    },
    {
        "Null", "user", "0",
        "assets/icons/zoomin.png",
        "zoom_in",
        "Zoom &In",
        "Zooms to increase the apparent size of objects."
    },
    {
        "Null", "user", "0",
        "assets/icons/zoomout.png",
        "zoom_out",
        "Zoom &Out",
        "Zoom to decrease the apparent size of object."
    },
    {
        "Null", "user", "0",
        "assets/icons/zoomselected.png",
        "zoom_selected",
        "Zoom Selec&ted",
        "Zooms to display the selected objects."
    },
    {
        "Null", "user", "0",
        "assets/icon/zoomall.png",
        "zoom_all",
        "Zoom &All",
        "Zooms to display the drawing extents or the grid limits."
    },
    {
        "Null", "user", "0",
        "assets/icons/zoomextents.png",
        "zoom_extents",
        "Zoom &Extents",
        "Zooms to display the drawing extents."
    },
    {
        "Null", "user", "0",
        "assets/icons/panrealtime.png",
        "pan_real_time",
        "&Pan Realtime",
        "Moves the view in the current viewport."
    },
    {
        "Null", "user", "0",
        "assets/icons/panpoint.png",
        "pan_point",
        "Pan &Point",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "assets/icons/panleft.png",
        "pan_left",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user",
        "0",
        "assets/icons/panright.png",
        "pan_right",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user",
        "0",
        "assets/icons/panup.png",
        "pan_up",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "assets/icons/pandown.png",
        "pan_down",
        "Pan &Down",
        "Move current view down."
    },
    {
        "Null", "user", "0",
        "assets/icons/day.png",
        "day",
        "Icon12&8",
        "Updates the current view using day vision settings."
    },
    {
        "Null", "user", "0",
        "assets/icons/night.png",
        "night",
        "Icon12&8",
         "Updates the current view using night vision settings."
    },
    {
        "Null", "user", "0",
        "icon128.png",
        "treble_clef",
        "&Treble Clef",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "icon128.png",
        "path",
        "&Path",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "circle.png",
        "circle", "&Circle",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "icon128.png",
        "line", "&Line",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "icon128.png",
        "distance",
        "&Distance",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "assets/icons/dolphin.png",
        "dolphin", "&Dolphin",
        "Creates a dolphin: dolphin"
    },
    {
        "Null", "user", "0",
        "assets/icons/ellipse.png",
        "ellipse", "&Ellipse",
        "Add an ellipse to the vector layer."
    },
    {
        "Null", "user", "0",
        "assets/icons/erase.png",
        "delete", "D&elete",
        "Removes objects from a drawing: delete"
    },
    {
        "Null", "user", "0",
        "assets/icons/heart.png",
        "heart", "&Heart",
        "Creates a heart: HEART"
    },
    {
        "Null", "user", "0",
        "assets/icons/locate_point.png",
        "locate_point", "&Locate Point",
        "Find a point that is near the indicated region."
    },
    {
        "Null", "user", "0",
        "spellcheck.png",
        "spell_check", "S&pell Check",
        "."
    },
    {
        "Null", "user", "0",
        "icon128.png",
        "quick_select", "Icon12&8",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "rectangle.png",
        "rectangle",
        "&Rectangle",
        "Creates a rectangular polyline: RECTANGLE"
    },
    {
        "Null", "user", "0",
        "rgb.png",
        "rgb",
        "&RGB",
        "Updates the current view colors: RGB"
    },
    {
        "Null", "user", "0",
        "rotate.png",
        "rotate",
        "&Rotate",
        "Rotates objects about a base point: ROTATE"
    },
    {
        "Null", "user", "0",
        "sandbox.png",
        "sandbox",
        "&Sandbox",
        "A sandbox to play in: SANDBOX"
    },
    {
        "Null", "user", "0",
        "assets/icons/export.png",
        "export",
        "&Export",
        "Export the current tab as a non-stitch format that will lose more data."
    },
    {
        "Null", "user", "0",
        "assets/icons/move.png",
        "move",
        "&Move",
        "Move the selected object(s) by the offset given as a vector."
    },
    {
        "Null", "user", "0",
        "assets/icons/quickleader.png",
        "quickleader",
        "&QuickLeader",
        "Creates a leader and annotation: QUICKLEADER"
    },
    {
        "Null", "user", "0",
        "assets/icons/selectall.png",
        "select_all",
        "&Select All",
        "Selects all objects: SELECTALL"
    },
    {
        "Null", "user", "0",
        "singlelinetext.png",
        "single_line_text",
        "&Single Line Text",
        "Creates single-line text objects: TEXT"
    },
    {
        "Null", "user", "0",
        "assets/icons/snowflake.png",
        "snowflake",
        "&Snowflake",
        "Creates a snowflake: SNOWFLAKE"
    },
    {
        "Null", "user", "0",
        "assets/icons/star.png",
        "star",
        "&Star",
        "Creates a star: STAR"
    },
    {
        "Null", "user", "0",
        "assets/icons/path.png",
        "path",
        "&Path",
        "Creates a 2D path: PATH"
    },
    {
        "Null", "user", "0",
        "assets/icons/donothing.png",
        "platform",
        "&Platform",
        "List which platform is in use: PLATFORM"
    },
    {
        "Null", "user", "0",
        "assets/icons/point.png",
        "point",
        "&Point",
        "Creates multiple points: POINT"
    },
    {
        "Null", "user", "0",
        "assets/icons/polygon.png",
        "polygon",
        "Pol&ygon",
        "Creates a regular polygon: POLYGON"
    },
    {
        "Null", "user", "0",
        "assets/icons/polyline.png",
        "polyline",
        "&Polyline",
        "Creates a 2D polyline: PLINE"
    },
    {
        "Null", "user", "0",
        "assets/icons/settingsdialog.png",
        "settings_dialog",
        "&Settings",
        "Configure settings specific to this product."
    },
    {
        "Null", "user", "0",
        "assets/icons/makelayercurrent.png",
        "make_layer_current",
        "&Make Layer Active",
        "Makes the layer of a selected object the active layer"
    },
    {
        "Null", "user", "0",
        "assets/icons/layers.png",
        "layers",
        "&Layers",
        "Manages layers and layer properties: LAYER"
    },
    {
        "Null", "user", "0",
        "assets/icons/layerselector.png",
        "layerselector",
        "&Layer Selector",
        "Dropdown selector for changing the current layer"
    },
    {
        "Null", "user", "0",
        "assets/icons/layerprevious.png",
        "layerprevious",
        "&Layer Previous",
        "Restores the previous layer settings: LAYERP"
    },
    {
        "Null", "user", "0",
        "assets/icons/colorselector.png",
        "colorselector",
        "&Color Selector",
        "Dropdown selector for changing the current thread color"
    },
    {
        "Null", "user", "0",
        "assets/icons/linetypeselector.png",
        "line type selector",
        "&Stitchtype Selector",
        "Dropdown selector for changing the current stitch type"
    },
    {
        "Null", "user", "0",
        "assets/icons/lineweightselector.png",
        "line weight selector",
        "&Threadweight Selector",
        "Dropdown selector for changing the current thread weight"
    },
    {
        "Null", "user", "0",
        "assets/icons/hidealllayers.png",
        "hide all layers",
        "&Hide All Layers",
        "Turns the visibility off for all layers in the current drawing: HIDEALL"
    },
    {
        "Null", "user", "0",
        "assets/icons/showalllayers.png",
        "showalllayers",
        "&Show All Layers",
        "Turns the visibility on for all layers in the current drawing: SHOWALL"
    },
    {
        "Null", "user", "0",
        "textbold.png",
        "textbold",
        "&Bold Text",
        "Sets text to be bold."
    },
    {
        "Null", "user", "0",
        "assets/icons/zoomscale.png",
        "zoomscale",
        "Zoom &Scale",
        "Zooms the display using a specified scale factor."
    },
    {
        "Null", "user", "0",
        "assets/icons/quickleader.png",
        "quickleader",
        "&QuickLeader",
        "Creates a leader and annotation: QUICKLEADER"
    },
    {
        "Null", "user", "0",
        "assets/icons/move.png",
        "move",
        "&Move",
        "Displaces objects a specified distance in a specified direction: MOVE"
    },
	{
    	"Null",
		"user",
		0,
		"assets/icons/circle.png",
        "circle",
        "&Circle",
        "Adds a circle to the vector layer."
    },
    {
		"Null",
		"user",
		0,
		"assets/icons/dolphin.png",
		"dolphin",
		"Dolphin",
		"Create a dolphin design in the vector layer."
		"assets/objects/dolphin/dolphin.scm",
		num_points=512
		scale_x=0.04
		scale_y=0.04
	},
	{
		"Null",
		"user",
		0,
		"assets/icons/heart.png",
		"heart4",
		"&Heart4",
		"Adds a heart to the vector layer."
		"assets/scripts/heart4.scm"
    },
    {
		"Null",
		"user",
		0,
		"assets/icons/heart.png",
		"heart5",
		"&Heart5",
		"Adds a heart to the vector layer."
		"assets/scripts/heart5.scm"
	},
	{
		"Null",
		"user",
		0,
		"assets/icons/path.png",
		"path",
		"&Path",
		"Add a path object to the current view."
	},
    {
        "Null", "user", "0",
        "assets/icons/icon128.png",
        "icon128",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128."
    },
    {
        "Null", "user", "0",
        "assets/icons/freezealllayers.png",
        "freezealllayers",
        "_Freeze All Layers",
        "Freezes all layers in the current drawing:  FREEZEALL"
    },
    {
        "Null", "user", "0",
        "assets/icons/panpoint.png",
        "panpoint",
        "&Pan Point",
        "Moves the view by the specified distance."
    },
    {
        "Null", "user", "0",
        "assets/icons/panleft.png",
        "panleft",
        "&Pan Left",
        "Moves the view to the left."
    },
    {
        "Null", "user", "0",
        "assets/icons/panright.png",
        "panright",
        "&Pan Right",
        "Moves the view to the right."
    },
    {
        "Null", "user", "0",
        "assets/icons/panup.png",
        "pan up",
        "&Pan Up",
        "Moves the view up."
    },
    {
        "Null", "user", "0",
        "assets/icons/pandown.png",
        "pan down",
        "&Pan Down",
        "Moves the view down."
    },
    {
        "Null", "user", "0",
        "assets/icons/line.png",
        "line",
        "&Line",
        "Creates straight line segments: LINE"
    },
    {
        "Null", "user", "0",
        "assets/icons/distance.png",
        "distance",
        "&Distance",
        "Measures the distance and angle between two points: DIST"
    },
    {
        "Null", "user", "0",
        "assets/icons/locatepoint.png",
        "locate point",
        "&Locate Point",
        "Displays the coordinate values of a location: ID"
    },
    {
        "Null", "user", "0",
        "assets/icons/donothing.png",
        "trebleclef",
        "TrebleClef",
        "Creates a treble clef: TREBLECLEF"
    },
    {
        "Null", "user", "0",
        "assets/icons/path.png",
        "path",
        "&Path",
        "Creates a 2D path: PATH"
    },
    {
        "Null", "user", "0",
        "assets/icons/donothing.png",
        "platform",
        "&Platform",
        "List which platform is in use: PLATFORM"
    },
    {
        "Null", "user", "0",
        "assets/icons/point.png",
        "point",
        "&Point",
        "Creates multiple points: POINT"
    },
    {
        "Null", "user", "0",
        "assets/icons/polygon.png",
        "polygon",
        "Pol&ygon",
        "Creates a regular polygon: POLYGON"
    },
    {
        "Null", "user", "0",
        "assets/icons/polyline.png",
        "polyline",
        "&Polyline",
        "Creates a 2D polyline: PLINE"
    }
*/
