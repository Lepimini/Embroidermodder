;
; Embroidermodder 2.
;
; ------------------------------------------------------------
;
; Copyright 2013-2022 The Embroidermodder Team
; Embroidermodder 2 is Open Source Software.
; See LICENSE for licensing terms.
;
; ------------------------------------------------------------
;
; Things that run after foreign functions have been
; initialised.
;
;void
;make_toolbar(SDL_Rect rect, char **actions)
;{
;    int i;
;    create_widget(rect, "do_nothing");
;    rect.x += padding;
;    rect.y += padding;
;    rect.w = button_size;;
;    rect.h = button_size;
;    for (i=0; actions[i][0]!='E'; i++) {
;        /* char *icon = action_list[index].icon; */
;        /*  icon, "button_background_color", */
;        create_widget(rect, actions[i]);
;        rect.x += padding+button_size;
;    }
;}
;
;    /*
;    Background 
;    make_rectangle(&rect, 0, 0, 640, 480);
;      NULL, "background_color", 
;    create_widget(rect, "do_nothing");
;    Menubar
;    debug_message("menubar");
;    make_rectangle(&rect, 0, 0, 640, 40);
;    NULL, "interface_color",
;    create_widget(rect, "do_nothing");
;
;    File Toolbar
;    debug_message("file");
;    make_rectangle(&rect, 0, 45, padding*6+button_size*5, padding*2+button_size);
;    
;    make_toolbar(rect, (char**)toolbar_entries[0]);
 ;   
;
;    Edit Toolbar
;    debug_message("edit");
;    make_rectangle(&rect, padding*7+button_size*5, 45, padding*6+button_size*5, padding*2+button_size);
;    make_toolbar(rect, (char**)toolbar_entries[1]);
;
;    Window Toolbar
;    make_rectangle(&rect, padding*14+button_size*10, 45, padding*7+button_size*6, padding*2+button_size);
;    make_toolbar(rect, (char**)toolbar_entries[3]);
;
;    Statusbar
;    make_rectangle(&rect, 0, 455, 640, 25);;
;     NULL, "interface_color",
;    create_widget(rect, "do_nothing");
;    */

(create-ui-rect 0 0 640 480 140 190 200)

(create-widget 10 10 24 24 "new")
(create-widget 40 10 24 24 "open")
(create-widget 70 10 24 24 "save")
(create-widget 100 10 24 24 "save-as")

(create-widget 130 10 24 24 "do-nothing")
(create-widget 160 10 24 24 "debug-message")
(create-widget 190 10 24 24 "new-file")
(create-widget 220 10 24 24 "open-file")
(create-widget 250 10 24 24 "save-file")
(create-widget 280 10 24 24 "save-file-as")
(create-widget 310 10 24 24 "check-for-updates")
(create-widget 340 10 24 24 "select-all")
(create-widget 370 10 24 24 "whats-this")
(create-widget 400 10 24 24 "design-details")
(create-widget 430 10 24 24 "print-pattern")
(create-widget 460 10 24 24 "exit-program")

(create-widget 10 40 24 24 "cut-object")
(create-widget 40 40 24 24 "copy-object")
(create-widget 70 40 24 24 "paste-object")
(create-widget 100 40 24 24 "delete-object")

(create-widget 130 40 24 24 "undo")
(create-widget 160 40 24 24 "redo")
(create-widget 190 40 24 24 "window-close")
(create-widget 220 40 24 24 "window-close-all")
(create-widget 250 40 24 24 "window-cascade")
(create-widget 280 40 24 24 "window-tile")
(create-widget 310 40 24 24 "window-next")
(create-widget 340 40 24 24 "window-previous")
(create-widget 370 40 24 24 "help")
(create-widget 400 40 24 24 "changelog-dialog")
(create-widget 290 40 24 24 "tip-of-the-day-dialog")
(create-widget 310 40 24 24 "about-dialog")

(create-widget 10 70 24 24 "icon-16")
(create-widget 30 70 24 24 "icon-24")
(create-widget 50 70 24 24 "icon-32")
(create-widget 70 70 24 24 "icon-48")
(create-widget 90 70 24 24 "icon-64")
(create-widget 110 70 24 24 "icon-128")

(create-widget 130 70 24 24 "settings-dialog")
(create-widget 150 70 24 24 "make-layer-current")

(create-widget 170 70 24 24 "layers")
(create-widget 190 70 24 24 "layer-selector")
(create-widget 210 70 24 24 "layer-previous")
(create-widget 230 70 24 24 "color-selector")
(create-widget 250 70 24 24 "line-type-selector")
(create-widget 270 70 24 24 "line-weight-selector")
(create-widget 290 70 24 24 "hide-all-layers")
(create-widget 310 70 24 24 "show-all-layers")
(create-widget 330 70 24 24 "freeze-all-layers")
(create-widget 350 70 24 24 "thaw-all-layers")
(create-widget 370 70 24 24 "lock-all-layers")
(create-widget 390 70 24 24 "unlock-all-layers")

(create-widget 410 70 24 24 "text-bold")
(create-widget 430 70 24 24 "text-italic")
(create-widget 450 70 24 24 "text-underline")
(create-widget 470 70 24 24 "text-strikeout")
(create-widget 70 70 24 24 "text-overline")

(create-widget 70 70 24 24 "zoom-real-time")
(create-widget 70 70 24 24 "zoom-previous")
(create-widget 70 70 24 24 "zoom-window")
(create-widget 70 70 24 24 "zoom-dynamic")
(create-widget 70 70 24 24 "zoom-scale")
(create-widget 70 70 24 24 "zoom-center")
(create-widget 70 70 24 24 "zoom-in")
(create-widget 70 70 24 24 "zoom-out")
(create-widget 70 70 24 24 "zoom-selected")
(create-widget 70 70 24 24 "zoom-all")
(create-widget 70 70 24 24 "zoom-extents")

(create-widget 10 100 24 24 "pan-real-time")
(create-widget 40 100 24 24 "pan-point")
(create-widget 70 100 24 24 "pan-left")
(create-widget 100 100 24 24 "pan-right")
(create-widget 130 100 24 24 "pan-up")
(create-widget 160 100 24 24 "pan-down")

(create-widget 190 100 24 24 "day-vision")
(create-widget 220 100 24 24 "night-vision")

(create-widget 250 100 24 24 "treble-clef")
(create-widget 280 100 24 24 "path")
(create-widget 310 100 24 24 "circle")
(create-widget 340 100 24 24 "line")
(create-widget 370 100 24 24 "distance")
(create-widget 400 100 24 24 "dolphin")
(create-widget 430 100 24 24 "ellipse")

(create-widget 10 130 24 24 "heart")
(create-widget 40 130 24 24 "locate-point")
(create-widget 70 130 24 24 "move")
(create-widget 100 130 24 24 "export")
(create-widget 130 130 24 24 "create-widget")
(create-widget 160 130 24 24 "heart4")
(create-widget 190 130 24 24 "heart5")
(create-widget 220 130 24 24 "single-line-text")
(create-widget 250 130 24 24 "spell-check"
(create-widget 280 130 24 24 "quick-select")
(create-widget 310 130 24 24 "rectangle")
(create-widget 340 130 24 24 "rgb")
(create-widget 370 130 24 24 "rotate")
(create-widget 270 130 24 24 "sandbox")
(create-widget 290 130 24 24 "quickleader")
(create-widget 310 130 24 24 "snowflake")
(create-widget 330 130 24 24 "star")
(create-widget 350 130 24 24 "platform")
(create-widget 370 130 24 24 "point")
(create-widget 390 130 24 24 "polygon")
(create-widget 410 130 24 24 "polyline")
(create-widget 430 130 24 24 "settings-dialog")
(create-widget 450 130 24 24 "quickleader")
(create-widget 470 130 24 24 "locate-point")
(create-widget 490 130 24 24 "point"

