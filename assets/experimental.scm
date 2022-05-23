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
; Experimental
;
; Unlike "unsorted.scm" this will parse correctly but may not
; run and could cause crashes.
;
; Use 3 space indentation and stack up trailing parentheses.


(define (usage)
   (debug-message "Usage Message"))

(define (rgb red green blue)
   (+
     blue
     (* 256 green)
     (* 256 256 red)))


; These toggle functions could be made by a macro.
(define (toggle-polar)
   (let*
      (debug-message "StatusBarButton togglePolar()")
      (define (show-polar) (not show-polar))))

(define (toggle-snap)
   (let*
      (debug-message "StatusBarButton toggleQSnap()")
      (define (snap-mode) (not snap-mode))))))

