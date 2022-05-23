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
; Configuration and data specific to the GUI.
;

(define (title) "Embroidermodder")
(define (version) "2.0.0-alpha")
(define (git-build-hash) "92403820fc2c6be46b884b6500e01a239363fc82")
(define (interface-font) "assets/fonts/source-sans/TTF/SourceSans3-Regular.ttf")
(define (text-font) "assets/fonts/source-sans/TTF/SourceSans3-Regular.ttf")
(define (real-render) 0)
(define (max-string-length) 500)
(define (debug-mode) 1)
(define (window-position) (vector 100 100))
(define (window-dimensions) (vector 640 480))
(define (max-distance) 1000000.0)
(define (general-icon-size) 16)
(define (background-color) "446688")
(define (interface-color) "6688AA")
(define (button-background-color) "88AAFF")
(define (color-mode) 0)
(define (general-mdi-bg-use-logo) 0)
(define (general-mdi-bg-use-texture) 0)
(define (general-mdi-bg-use-color) 0)
(define (selection-coolgrip-color) "FFFFFF")
(define (selection-hotgrip-color) "FFFFFF")

(define (general-language) "default")
(define (general-icon-theme) "default")
(define (general-mdi-bg-logo) "assets/icons/logo.png")
(define (general-mdi-bg-texture) "assets/icons/texture.png")
(define (general-mdi-bg-color) "FFFFFF")
(define (general-current-tip) 0)
(define (general-tip-of-the-day) 0)
(define (general-system-help-browser) 1)
(define (general-check-for-updates) 0)

; QSnap Properties
(define (qsnap-locator-color) "FFFFFF")
(define (qsnap-endpoint) 0)
(define (qsnap-midpoint) 0)
(define (qsnap-center) 0)
(define (qsnap-node) 0)
(define (qsnap-quadrant) 0)
(define (qsnap-intersection) 0)
(define (qsnap-extension) 0)
(define (qsnap-insertion) 0)
(define (qsnap-perpendicular) 0)
(define (qsnap-tangent) 0)
(define (qsnap-nearest) 0)
(define (qsnap-apparent) 0)
(define (qsnap-parallel) 0)
(define (qsnap-enabled) 0)
(define (qsnap-locator-size) 16)
(define (qsnap-aperture-size) 16)
(define (qsnap-active) 0)
(define (qsnap-toggle) 0)

; Text Settings
(define (text-style-bold) 0)
(define (text-style-italic) 0)
(define (text-style-underline) 0)
(define (text-style-strikethrough) 0)

; Line Weight Settings
(define (lwt-show-lwt) 0)
(define (lwt-real-render) 0)
(define (lwt-default-lwt) 1.0)

; Ruler Settings
(define (ruler-metric) 1)
(define (ruler-show-on-load) 1)
(define (ruler-pixel-size) 30)

(define (tab-index) 0)

; Grid Settings
(define (grid-size-radius) 10.0)
(define (grid-center-on-origin) 0)
(define (grid-center) (vector 0.5 0.5))
(define (grid-size) (vector 10.0 10.0))
(define (grid-spacing) (vector 10.0 10.0))
(define (grid-size-radius) 10.0)
(define (grid-spacing-radius) 10.0)
(define (grid-spacing-angle) 10.0)
(define (grid-show-on-load) 0)
(define (grid-show-origin) 1)
(define (grid-color-match-crosshair) 1)
(define (grid-load-from-file) 1)
(define (grid-color) "FFFFFF")

(define (symbol-scale) 0.01)

(define (display-use-opengl) 1)
(define (display-renderhint-aa) 1)
(define (display-renderhint-text-aa) 1)
(define (display-renderhint-smooth-pix) 1)
(define (display-renderhint-high-aa) 1)
(define (display-renderhint-noncosmetic) 1)
(define (display-show-scrollbars) 1)
(define (display-scrollbar-widget-num) 1)
(define (display-zoomscale-in) 1)
(define (display-zoomscale-out) 1)
(define (display-selectbox-alpha) 1)
(define (display-crosshair-percent) 10)

(define (opensave-open-thumbnail) "assets/icon/open_file_16.png")
(define (opensave-save-thumbnail) "assets/icon/save_file_16.png")
(define (opensave-recent-max-files) 10)
(define (opensave-trim-dst-num-jumps) 6)

(define (printing-use-last-device) 0)
(define (printing-disable-bg) 0)

; Selection Settings
(define (selection-mode-pickfirst) 0)
(define (selection-mode-pickadd) 0)
(define (selection-mode-pickdrag) 0)
(define (selection-grip-size) 16)
(define (selection-pickbox-size) 16)

(define (grip-size) 16)
(define (pick-box-size) 40)
(define (crosshair-size) 16)
(define (shift-key-pressed-state) 0)
(define (gripping-active) 0)
(define (rapid-move-active) 0)
(define (previewActive) 0)
(define (pastingActive) 0)
(define (movingActive) 0)
(define (selectingActive) 0)
(define (zoomWindowActive) 0)

; Panning Settings
(define (panning-real-time-active) 0)
(define (panning-point-active) 0)
(define (panning-active) 0)

(define (display-crosshair-color) "FFFFFF")
(define (display-bg-color) "FFFFFF")
(define (display-selectbox-left-color) "FFFFFF")
(define (display-selectbox-left-fill) "FFFFFF")
(define (display-selectbox-right-color) "FFFFFF")
(define (display-selectbox-right-fill) "FFFFFF")
(define (display-units) "Scientific")
(define (tips-length) 15)


(define (shortcuts)
  (vector
    (vector "new_file" "Ctrl+N")
    (vector "open_file" "Ctrl+O")
    (vector "save_file" "Ctrl+S")
    (vector "save_file_as" "Ctrl+Shift+S")
    (vector "print" "Ctrl+P")
    (vector "design_details" "Ctrl+D")
    (vector "exit" "Ctrl+Q")
    (vector "cut" "Ctrl+X")
    (vector "copy" "Ctrl+C")
    (vector "paste" "Ctrl+V")
    (vector "undo" "Ctrl+Z")
    (vector "redo" "Ctrl+Shift+Z")
    (vector "help" "F1")
    (vector "about" "F2")
    (vector "fullscreen" "F11")
  )
)

(define (tips)
  (vector
    "we need more tips?"
    "you can change the color of the display through settings?"
    "you can hide the scrollbars to increase the viewable area through settings?"
    "you can change the icon size for increased visibility?"
    "you can toggle the grid on and off by pressing the button in the statusbar?"
    "the grid size can be changed to match your hoop size through settings?"
    "the crosshair size is based on a percentage of your screen size? Setting it to 100 may help you visually line things up better."
    "you can pan by pressing the middle mouse button and dragging your mouse across the screen?"
    "you can open and edit multiple designs simultaneously?"
    "that many embroidery machines support the .dst format?"
    "that you can zoom in and out using your mouse wheel?"
    "that you can use circular and isometric grids?"
    "about our command line format converter?"
    "that you can use the 'DAY' and 'NIGHT' commands to quickly switch the  view colors to commonly used white or black?"
    "that you can quickly change the background, crosshair and grid colors using the 'RGB' command?"
    "END"
  )
)

(define (welcome-message)
  (vector
    " _____________________________________________________________________________"
    "|                                                                             |"
    "|                         EMBROIDERMODDER 2.0.0-alpha                         |"
    "|                         http://embroidermodder.org                          |"
    "|_____________________________________________________________________________|"
    "Usage: embroidermodder [options] files ..."
    ""
    "Options:"
    "-d, --debug      Print lots of debugging information."
    "-h, --help       Print self message and exit."
    "-v, --version    Print the version number of embroidermodder and exit."
  )
)

; In the order (icons, labels, value)
(define (thread_weights)
  (vector
    (vector "assets/icons/lineweightbylayer.png" "ByLayer" -2.0)
    (vector "assets/icons/lineweightbyblock.png" "ByBlock" -1.0)
    (vector "assets/icons/lineweightdefault.png" "Default" 0.0)
    (vector "assets/icons/lineweight01.png" "0.00 mm" 0.0)
    (vector "assets/icons/lineweight02.png" "0.05 mm" 0.05)
    (vector "assets/icons/lineweight03.png" "0.15 mm" 0.15)
    (vector "assets/icons/lineweight04.png" "0.20 mm" 0.2)
    (vector "assets/icons/lineweight05.png" "0.25 mm" 0.25)
    (vector "assets/icons/lineweight06.png" "0.30 mm" 0.3)
    (vector "assets/icons/lineweight07.png" "0.35 mm" 0.35)
    (vector "assets/icons/lineweight08.png" "0.40 mm" 0.4)
    (vector "assets/icons/lineweight09.png" "0.45 mm" 0.45)
    (vector "assets/icons/lineweight10.png" "0.50 mm" 0.5)
    (vector "assets/icons/lineweight11.png" "0.55 mm" 0.55)
    (vector "assets/icons/lineweight12.png" "0.60 mm" 0.6)
    (vector "assets/icons/lineweight13.png" "0.65 mm" 0.65)
    (vector "assets/icons/lineweight14.png" "0.70 mm" 0.7)
    (vector "assets/icons/lineweight15.png" "0.75 mm" 0.75)
    (vector "assets/icons/lineweight16.png" "0.80 mm" 0.8)
    (vector "assets/icons/lineweight17.png" "0.85 mm" 0.85)
    (vector "assets/icons/lineweight18.png" "0.90 mm" 0.9)
    (vector "assets/icons/lineweight19.png" "0.95 mm" 0.95)
    (vector "assets/icons/lineweight20.png" "1.00 mm" 1.0)
    (vector "assets/icons/lineweight21.png" "1.05 mm" 1.05)
    (vector "assets/icons/lineweight22.png" "1.10 mm" 1.1)
    (vector "assets/icons/lineweight23.png" "1.15 mm" 1.15)
    (vector "assets/icons/lineweight24.png" "1.20 mm" 1.2}
  )
)

