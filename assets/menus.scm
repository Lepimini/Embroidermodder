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
; Menus

(define (menu-item-height) 15)
(define (menu-width) 100)

; FILE MENU
; ---------
(define (x-offset) 10)
(create-label (x-offset) 5 100 100 "File" "file-menu")
(if (= (menu-state) (file-menu))
    (begin
      (create-label (x-offset) (+ 5 (* (menu-item-height) 1))
        (menu-width) (menu-item-height)
        "New" "new")
      ; (horizontal-rule )
      (create-label (x-offset) (+ 5 (* (menu-item-height) 2))
        (menu-width) (menu-item-height)
        "Open" "open")
      ; (horizontal-rule )
      (create-label (x-offset) (+ 5 (* (menu-item-height) 3))
        (menu-width) (menu-item-height)
        "Save" "save")
      (create-label (x-offset) (+ 5 (* (menu-item-height) 4))
        (menu-width) (menu-item-height)
        "Save as..." "save-as")
      (create-label (x-offset) (+ 5 (* (menu-item-height) 5))
        (menu-width) (menu-item-height)
        "Export" "export")
      ; (horizontal-rule )
      (create-label (x-offset) (+ 5 (* (menu-item-height) 6))
        (menu-width) (menu-item-height)
        "Print" "print")
      ; (horizontal-rule )
      (create-label (x-offset) (+ 5 (* (menu-item-height) 7))
        (menu-width) (menu-item-height)
        "Design Details" "design-details")
      ; (horizontal-rule )
      (create-label (x-offset) (+ 5 (* (menu-item-height) 8))
        (menu-width) (menu-item-height)
        "Exit" "exit-program")))

; EDIT MENU
; ---------
(define (x-offset) 60)

(create-label (x-offset) 5 100 100 "Edit" "edit-menu")

(if (= (menu-state) (edit-menu))
    (begin
      (create-ui-rect (x-offset) 20 (menu-width)
        (* (menu-item-height) 5)
        255 255 255)
      (create-label (x-offset) (+ 5 (* (menu-item-height) 1))
        (menu-width) (menu-item-height)
        "Undo" "undo")
      (create-label (x-offset) (+ 5 (* (menu-item-height) 2))
        (menu-width) (menu-item-height)
        "Redo" "redo")
      (create-label (x-offset) (+ 5 (* (menu-item-height) 3))
        (menu-width) (menu-item-height)
        "Cut" "cut")
      (create-label (x-offset) 65 (menu-width) (menu-item-height) "Copy")
      (create-label (x-offset) 80 (menu-width) (menu-item-height) "Paste")
      (horizontal-rule (x-offset) (+ 5 (* (menu-item-height) 3)) (menu-width))
      (horizontal-rule (x-offset) (+ 5 (* (menu-item-height) 6)) (menu-width))
      (vertical-rule (x-offset) 20
        (* (menu-item-height) 5))
      (vertical-rule (+ (x-offset) (menu-width)) 20
        (* (menu-item-height) 5))))

; VIEW MENU
; ---------
(define (x-offset) 110)
(create-label (x-offset) 5 100 100 "View" "view-menu")

(if (= (menu-state) (view-menu))
  (begin
    (create-ui-rect (x-offset) 20 50 100 255 255 255)
    (create-label
     (x-offset) 20 (menu-width) (menu-item-height) "Day")
    (create-label (x-offset) 35 (menu-width) (menu-item-height) "Night")
    ; (horizontal-rule )
    (create-label (x-offset) 50 (menu-width) (menu-item-height) "Icon 16")
    (create-label (x-offset) 65 (menu-width) (menu-item-height) "Icon 24")
    (create-label (x-offset) 80 (menu-width) (menu-item-height) "Icon 32")
    (create-label (x-offset) 95 (menu-width) (menu-item-height) "Icon 48")
    (create-label (x-offset) 110 (menu-width) (menu-item-height) "Icon 64")
    (create-label (x-offset) 135 (menu-width) (menu-item-height) "Icon 128")
    (horizontal-rule (x-offset) (+ 5 (* (menu-item-height) 3)) (menu-width))
    (horizontal-rule (x-offset) (+ 5 (* (menu-item-height) 8)) (menu-width))
    (vertical-rule (x-offset) 5 200)
    (vertical-rule 110 5 200)))

; SETTINGS MENU
; -------------
(define (x-offset) 160)
(create-label (x-offset) 5 100 100 "Settings" "settings-menu")

(if (= (menu-state) (settings-menu))
  (begin
    (create-ui-rect 160 20 50 100 255 255 255)
    (create-label 160 20 (menu-width) (menu-item-height)
      "Settings Dialog" "settings-dialog")))

; WINDOW MENU
; -----------
(define (x-offset) 210)
(create-label (x-offset) 5 100 100 "Window")

(if (= (menu-state) (window-menu))
  (begin
    (create-ui-rect 210 20 50 100 255 255 255)
    (create-label 210 20 (menu-width) (menu-item-height) "Window Cascade")))

; HELP MENU
; ---------
(define (x-offset) 260)
(create-label (x-offset) 5 (menu-width) (menu-item-height) "Help")

(if (= (menu-state) (help-menu))
  (begin
    (create-ui-rect (x-offset) 20 50 100 255 255 255)
    (create-label (x-offset) 20 (menu-width) (menu-item-height) "Help")
    ; (horizontal-rule )
    (create-label (x-offset) 35 (menu-width) (menu-item-height) "Changelog")
    ; (horizontal-rule )
    (create-label (x-offset) 50 (menu-width) (menu-item-height) "Tip of the Day")
    ; (horizontal-rule )
    (create-label (x-offset) 65 (menu-width) (menu-item-height) "About")
    ; (horizontal-rule )
    (create-label (x-offset) 80 (menu-width) (menu-item-height) "What's This?")
    ; (horizontal-rule )
    (vertical-rule (x-offset) 5 200)
    (vertical-rule 110 5 200)))

; RECENT MENU
; -----------
(define (x-offset) 310)
(create-label (x-offset) 5 100 100 "Recent")

(if (= (menu-state) (recent-menu))
  (begin
    (create-ui-rect (x-offset) 20 50 100 255 255 255)))

; ZOOM MENU
; ---------
(define (x-offset) 360)
(create-label (x-offset) 5 100 100 "Zoom")

(if (= (menu-state) (zoom-menu))
  (begin
    (create-ui-rect (x-offset) 20 50 100 255 255 255)
    (create-label (x-offset) 20 (menu-width) (menu-item-height) "Zoom Real Time")
    (create-label (x-offset) 20 (menu-width) (menu-item-height) "Zoom Previous")
    ; (horizontal-rule )
    (create-label (x-offset) 35 (menu-width) (menu-item-height) "Zoom Window")
    (create-label (x-offset) 35 (menu-width) (menu-item-height) "Zoom Dynamic")
    (create-label (x-offset) 35 (menu-width) (menu-item-height) "Zoom Scale")
    (create-label (x-offset) 35 (menu-width) (menu-item-height) "Zoom Center")
    ; (horizontal-rule )
    (create-label (x-offset) 50 (menu-width) (menu-item-height) "Zoom In")
    (create-label (x-offset) 50 (menu-width) (menu-item-height) "Zoom Out")
    ; (horizontal-rule )
    (create-label (x-offset) 65 (menu-width) (menu-item-height) "Zoom Selected")
    (create-label (x-offset) 65 (menu-width) (menu-item-height) "Zoom All")
    (create-label (x-offset) 65 (menu-width) (menu-item-height) "Zoom Extents")
    ; (horizontal-rule )
    (vertical-rule (x-offset) 5 200)
    (vertical-rule 110 5 200)))

; PAN MENU
; --------
(define (x-offset) 410)
(create-label (x-offset) 5 100 100 "Pan")

(if (= (menu-state) (pan-menu))
  (begin
    (create-ui-rect (x-offset) 20 50 100 255 255 255)
    (create-label (x-offset) 20 (menu-width) (menu-item-height) "Pan Real Time")
    (create-label (x-offset) 20 (menu-width) (menu-item-height) "Pan Point")
    ; (horizontal-rule )
    (create-label (x-offset) 35 (menu-width) (menu-item-height) "Pan Left")
    (create-label (x-offset) 35 (menu-width) (menu-item-height) "Pan Right")
    (create-label (x-offset) 35 (menu-width) (menu-item-height) "Pan Up")
    (create-label (x-offset) 35 (menu-width) (menu-item-height) "Pan Down")
    ; (horizontal-rule )
    (vertical-rule (x-offset) 5 200)
    (vertical-rule 110 5 200)))

