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

(define (menu-labels)
  (vector
    "File"
    "Edit"
    "View"
    "Settings"
    "Window"
    "Help"
    "Recent"
    "Zoom"
    "Pan"
    "END"
  )
)

(define (file-menu)
  (vector
    "new"
    "---"
    "open"
    "---"
    "save"
    "save_as"
    "---"
    "print"
    "---"
    "design_details"
    "---"
    "exit"
    "END"
  )
)

(define (edit-menu)
  (vector
    "undo"
    "redo"
    "---"
    "cut"
    "copy"
    "paste"
    "END"
  )
)

(define (view-menu)
  (vector
    "day"
    "night"
    "---"
    "icon16"
    "icon24"
    "icon32"
    "icon48"
    "icon64"
    "icon128"
    "END"
  )
)

(define (settings-menu)
  (vector
    "settings_dialog"
    "END"
  )
)

(define (window-menu)
  (vector
    "END"
  )
)

(define (help-menu)
  (vector
    "help"
    "---"
    "changelog"
    "---"
    "tip_of_the_day"
    "---"
    "about"
    "---"
    "whats_this"
    "END"
  )
)

(define (recent-menu)
  (vector
    "END"
  )
)

(define (zoom-menu)
  (vector
    "zoom_real_time"
    "zoom_previous"
    "---"
    "zoom_window"
    "zoom_dynamic"
    "zoom_scale"
    "zoom_center"
    "---"
    "zoom_in"
    "zoom_out"
    "---"
    "zoom_selected"
    "zoom_all"
    "zoom_extents"
    "END"
  )
)

(define (pan-menu)
  (vector
    "pan_real_time"
    "pan_point"
    "---"
    "pan_left"
    "pan_right"
    "pan_up"
    "pan_down"
    "END"
  )
)
