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

(define (icon-size) 24)
(define (menubar-height) 24)
(define (menubar-padding) 2)
(define (toolbar-offset) (+ (menubar-height) (menubar-padding)))
(define (toolbar-padding) 4)
(define (toolbar-width) 632)
(define (toolbar-height) (+ (icon-size) (toolbar-padding)))
(define (icon-padding) 4)

(define (background-rect x y w h)
  (create-ui-rect x y w h 100 150 210))

(create-ui-rect 0 0 640 480 50 50 50)

; Menubar
(create-ui-rect
  0 0
  640 (menubar-height)
  200 200 250)

; Toolbars
(background-rect
  (toolbar-padding) (toolbar-offset)
  (toolbar-width) (toolbar-height))

(background-rect
  (toolbar-padding)
  (+ (toolbar-padding) (toolbar-height) (toolbar-offset))
  (toolbar-width) (toolbar-height))

(background-rect
  (toolbar-padding)
  (+ (* 2 (+ (toolbar-padding) (toolbar-height)))
    (toolbar-offset))
  (toolbar-width) (toolbar-height))

(background-rect
  (toolbar-padding)
  (+ (* 3 (+ (toolbar-padding) (toolbar-height)))
    (toolbar-offset))
  (toolbar-width) (toolbar-height))

(define (horizontal-rule x y w)
  (create-ui-rect x y w 2 0 0 0))
(define (vertical-rule x y h)
  (create-ui-rect x y 2 h 0 0 0))

(horizontal-rule 4 170 300)
(horizontal-rule 4 200 300)
(horizontal-rule 4 230 300)
(horizontal-rule 4 260 300)
(vertical-rule 170 170 300)
(vertical-rule 200 170 300)
(vertical-rule 230 170 300)
(vertical-rule 260 170 300)

; For menubars:
(create-label 0 0 100 10 "File")
(create-label 0 100 100 10 "Edit")

(define (icon-offset n)
  (+ (* n (icon-padding))
     (* (- n 1) (+ (icon-size) (toolbar-padding)))))

(define (create-icon n m s)
  (create-widget
    (icon-offset n) (+ (icon-offset m) (menubar-height))
    (icon-size) (icon-size) s))

(create-icon 1 1 "new")
(create-icon 2 1 "open")
(create-icon 3 1 "save")
(create-icon 4 1 "save-as")

(create-icon 5 1 "cut")
(create-icon 6 1 "copy")
(create-icon 7 1 "paste")
(create-icon 8 1 "delete")

(create-icon 9 1 "undo")
(create-icon 10 1 "redo")
(create-icon 11 1 "check-for-updates")
(create-icon 12 1 "select-all")
(create-icon 13 1 "whats-this")
(create-icon 14 1 "design-details")
(create-icon 15 1 "print-pattern")
(create-icon 16 1 "exit-program")

(create-icon 1 2 "window-close")
(create-icon 2 2 "window-close-all")
(create-icon 3 2 "window-cascade")
(create-icon 4 2 "window-tile")
(create-icon 5 2 "window-next")
(create-icon 6 2 "window-previous")

(create-icon 7 2 "help")
(create-icon 8 2 "changelog-dialog")
(create-icon 9 2 "tip-of-the-day-dialog")
(create-icon 10 2 "about-dialog")

(create-icon 11 2 "icon-16")
(create-icon 12 2 "icon-24")
(create-icon 13 2 "icon-32")
(create-icon 14 2 "icon-48")
(create-icon 15 2 "icon-64")
(create-icon 16 2 "icon-128")

(create-icon 17 2 "settings-dialog")
(create-icon 18 2 "make-layer-current")

(create-icon 19 2 "pan-real-time")
(create-icon 20 2 "pan-point")
(create-icon 21 2 "pan-left")
(create-icon 22 2 "pan-right")
(create-icon 23 2 "pan-up")
(create-icon 24 2 "pan-down")

(create-icon 25 2 "day")
(create-icon 26 2 "night")

(create-icon 1 3 "layers")
(create-icon 2 3 "layer-selector")
(create-icon 3 3 "layer-previous")
(create-icon 4 3 "color-selector")
(create-icon 5 3 "line-type-selector")
(create-icon 6 3 "line-weight-selector")
(create-icon 7 3 "hide-all-layers")
(create-icon 8 3 "show-all-layers")
(create-icon 9 3 "freeze-all-layers")
(create-icon 10 3 "thaw-all-layers")
(create-icon 11 3 "lock-all-layers")
(create-icon 12 3 "unlock-all-layers")

(create-icon 13 3 "text-bold")
(create-icon 14 3 "text-italic")
(create-icon 15 3 "text-underline")
(create-icon 16 3 "text-strikeout")
(create-icon 17 3 "text-overline")

(create-icon 18 3 "zoom-real-time")
(create-icon 19 3 "zoom-previous")
(create-icon 20 3 "zoom-window")
(create-icon 21 3 "zoom-dynamic")
(create-icon 22 3 "zoom-scale")
(create-icon 23 3 "zoom-center")
(create-icon 24 3 "zoom-in")
(create-icon 25 3 "zoom-out")
(create-icon 26 3 "zoom-selected")
(create-icon 27 3 "zoom-all")
(create-icon 28 3 "zoom-extents")

(create-icon 9 4 "treble-clef")
(create-icon 10 4 "path")
(create-icon 11 4 "circle")
(create-icon 12 4 "line")
(create-icon 13 4 "distance")
(create-icon 14 4 "dolphin")
(create-icon 15 4 "ellipse")

(create-icon 16 4 "heart")
(create-icon 17 4 "locate-point")
(create-icon 18 4 "move")
(create-icon 19 4 "export")
(create-icon 20 4 "heart4")
(create-icon 21 4 "heart5")
(create-icon 22 4 "single-line-text")
(create-icon 23 4 "spell-check"
(create-icon 24 4 "quick-select")
(create-icon 25 4 "rectangle")
(create-icon 26 4 "rgb")
(create-icon 27 4 "rotate")
(create-icon 28 4 "sandbox")
(create-icon 29 4 "quickleader")
(create-icon 1 4 "snowflake")
(create-icon 1 4 "star")
(create-icon 1 4 "platform")
(create-icon 1 4 "point")
(create-icon 1 4 "polygon")
(create-icon 1 4 "polyline")
(create-icon 1 4 "settings-dialog")
(create-icon 1 4 "quickleader")
(create-icon 1 4 "locate-point")
(create-icon 1 4 "point")

; Statusbar
(create-ui-rect
  0 454
  640 (menubar-height)
  100 100 100)

