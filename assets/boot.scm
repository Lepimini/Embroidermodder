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
; Chaining all our configuration and ui data and functions.

(define (files-to-load)
  (vector
    "assets/init.scm"
    "assets/config.scm"
    "assets/objects.scm"
    "assets/menus.scm"
    "assets/toolbars.scm"
    "assets/experimental.scm"
    "END"
  )
)

(create-widget 10 100 10 100 "erase")
