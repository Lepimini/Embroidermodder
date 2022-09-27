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
;
; Since ui.scm is reloaded periodically,
; we don't want anything to be downstream of it if it
; doesn't have some reason to be.

(load "assets/init.scm")
(load "assets/config.scm")

