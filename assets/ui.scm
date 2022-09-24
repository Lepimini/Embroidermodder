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
; Generate the user interface.
;
; Menubar
; make_rectangle(&rect, 0, 0, 640, 40);
;    NULL, "interface_color",
; create_widget(rect, "do_nothing");
;
; File Toolbar
; make_rectangle(&rect, 0, 45, padding*6+button_size*5, padding*2+button_size);
; make_toolbar(rect, (char**)toolbar_entries[0]);
;
; Edit Toolbar
; make_rectangle(&rect, padding*7+button_size*5, 45, padding*6+button_size*5, padding*2+button_size);
; make_toolbar(rect, (char**)toolbar_entries[1]);
;
; Window Toolbar
;    make_rectangle(&rect, padding*14+button_size*10, 45, padding*7+button_size*6, padding*2+button_size);
;    make_toolbar(rect, (char**)toolbar_entries[3]);
;
; Statusbar
;    make_rectangle(&rect, 0, 455, 640, 25);;
;     NULL, "interface_color",
;    create_widget(rect, "do_nothing");

(define (icon-size) 24)
(define (window-width) 640)
(define (window-height) 480)
(define (menubar-height) 24)
(define (menubar-padding) 2)
(define (toolbar-offset) (+ (menubar-height) (menubar-padding)))
(define (toolbar-padding) 4)
(define (toolbar-width) 632)
(define (toolbar-height) (+ (icon-size) (toolbar-padding)))
(define (icon-padding) 4)

(define (background-rect x y w h)
  (create-ui-rect x y w h 100 150 210))

(create-ui-rect 0 0 (window-width) (window-height) 50 50 50)

; Toolbar background
(create-ui-rect
  0 0
  640 (+ (* 3 (+ (toolbar-padding) (toolbar-height)))
    (toolbar-offset))
  240 240 250)

; Menubar
(create-ui-rect
  0 0
  (window-width) (menubar-height)
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

(horizontal-rule 10 170 350)
(horizontal-rule 10 240 350)
(horizontal-rule 10 310 350)
(horizontal-rule 10 380 350)
(horizontal-rule 10 450 350)
(vertical-rule 10 150 300)
(vertical-rule 80 150 300)
(vertical-rule 150 150 300)
(vertical-rule 220 150 300)
(vertical-rule 290 150 300)
(vertical-rule 360 150 300)

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

(create-icon 17 1 "window-close")
(create-icon 18 1 "window-close-all")
(create-icon 19 1 "window-cascade")
(create-icon 20 1 "window-tile")
(create-icon 21 1 "window-next")
(create-icon 22 1 "window-previous")

(create-icon 1 2 "help")
(create-icon 2 2 "changelog-dialog")
(create-icon 3 2 "tip-of-the-day-dialog")
(create-icon 4 2 "about-dialog")

(create-icon 5 2 "icon-16")
(create-icon 6 2 "icon-24")
(create-icon 7 2 "icon-32")
(create-icon 8 2 "icon-48")
(create-icon 9 2 "icon-64")
(create-icon 10 2 "icon-128")

(create-icon 11 2 "settings-dialog")
(create-icon 12 2 "make-layer-current")

(create-icon 13 2 "pan-real-time")
(create-icon 14 2 "pan-point")
(create-icon 15 2 "pan-left")
(create-icon 16 2 "pan-right")
(create-icon 17 2 "pan-up")
(create-icon 18 2 "pan-down")

(create-icon 19 2 "day")
(create-icon 20 2 "night")

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

(create-icon 1 4 "treble-clef")
(create-icon 2 4 "path")
(create-icon 3 4 "circle")
(create-icon 4 4 "line")
(create-icon 5 4 "distance")
(create-icon 6 4 "dolphin")
(create-icon 7 4 "ellipse")

(create-icon 8 4 "heart")
(create-icon 9 4 "locate-point")
(create-icon 10 4 "move")
;(create-icon 11 4 "export")
;(create-icon 12 4 "heart4")
;(create-icon 13 4 "heart5")
;(create-icon 14 4 "single-line-text")
;(create-icon 15 4 "spell-check"
;(create-icon 16 4 "quick-select")
;(create-icon 17 4 "rectangle")
;(create-icon 18 4 "rgb")
;(create-icon 19 4 "rotate")
;(create-icon 20 4 "sandbox")
;(create-icon 21 4 "quickleader")
;(create-icon 22 4 "snowflake")
;(create-icon 23 4 "star")
;(create-icon 24 4 "platform")
;(create-icon 25 4 "point")
;(create-icon 26 4 "polygon")
;(create-icon 27 4 "polyline")
;(create-icon 28 4 "settings-dialog")
;(create-icon 29 4 "quickleader")
;(create-icon 30 4 "locate-point")
;(create-icon 31 4 "point")

; For menubars:
(create-label 10 5 100 100 "File")
(create-label 60 5 100 100 "Edit")

; Statusbar
(create-ui-rect
  0 (- (window-height) (menubar-height))
  (window-width) (menubar-height)
  100 100 100)

