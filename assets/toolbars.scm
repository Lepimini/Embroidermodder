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
; Toolbars


; Toolbars
; ------------------------------------------------------------------------------
(define (file-toolbar)
  (vector
    "new"
    "open"
    "save"
    "save_as"
    "print"
    "design_details"
    "help"
    "END"
  )
)

(define (edit-toolbar)
  (vector
    "undo"
    "redo"
    "cut"
    "copy"
    "paste"
    "END"
  )
)

(define (view-toolbar)
  (vector
    "day"
    "night"
    "END"
  )
)

(define (zoom-toolbar)
  (vector
    "zoom_window"
    "zoom_dynamic"
    "zoom_scale"
    "zoom_center"
    "zoom_in"
    "zoom_out"
    "zoom_selected"
    "zoom_all"
    "zoom_extents"
    "END"
  )
)

(define (pan-toolbar)
  (vector
    "pan_real_time"
    "pan_point"
    "pan_left"
    "pan_right"
    "pan_up"
    "pan_down"
    "END"
  )
)

(define (icon-toolbar)
  (vector
    "icon16"
    "icon24"
    "icon32"
    "icon48"
    "icon64"
    "icon128"
    "END"
  )
)

(define (help-toolbar)
  (vector
    "help"
    "changelog"
    "about"
    "whats_this"
    "END"
  )
)

(define (layer-toolbar)
  (vector
    "END"
  )
)

(define (text-toolbar)
  (vector
    "END"
  )
)

(define (propertes-toolbar)
  (vector
    "END"
  )
)

(define (other-toolbar)
  (vector
    "END"
  )
)

