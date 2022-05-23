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
; Unsorted

;preview-modes:
;    null
;    move
;    rotate
;    scale

;comboboxes:
;    ARC-CLOCKWISE
;    GENERAL-LAYER
;    GENERAL-COLOR
;    GENERAL-LINE-TYPE
;    GENERAL-LINE-WEIGHT
;    TEXT-SINGLE-FONT
;    TEXT-SINGLE-JUSTIFY

;keys:
;    obj-type=int=See OBJ-TYPE-VALUES
;    obj-name=str=\USER\, \DEFINED\, \STRINGS\, etc...
;    OBJ-LAYER=value type {int=0-255
;    OBJ-COLOR=TODO=Use color chart in formats/format-dxf.h for this
;    OBJ-LTYPE=int=See OBJ-LTYPE-VALUES
;    OBJ-LWT=int=[-2, 27]
;    OBJ-RUBBER=int=See OBJ-RUBBER-VALUES


; This is different for each user, so we're leaving it out of
; the settings dict.
; =str(Path.home()) + os.sep + .embroidermodder2

; application-folder[500]

;opensave-open-format=
;opensave-save-format=
;opensave-recent-directory=
;printing-default-device=
;ruler-color=FFFFFF
;qsnap-locator-color=FFFFFF
;grid-type=cartesian
;selection-coolgrip-color=FFFFFF
;selection-hotgrip-color=FFFFFF
;translation-table:
;    {default=?
;      French=?
;      German=?
;      Spanish=?

;symbols-docstring=|
;    Symbols use the SVG path syntax.

;    In theory, we could combine the icons and symbols systems,
;    since they could be rendered once and stored as icons in Qt.
;    (Or as textures in FreeGLUT.)

;    Also we want to render the patterns themselves using SVG
;    syntax, so it would save on repeated work overall.

;symbol-list:
;    s0=|
;        path.addEllipse(Vector(x+0.25*xs, y-0.50*ys),
;            0.25*xs, 0.50*ys)
;        M 0 -0.75
;        L 0 -0.25
;        A 0 -0.5 0.5 0.5 180.0 180.0
;        L 0.5, -0.75
;        A 0 -1.0, 0.5, 0.5, 0.0, 180.0
;    s1=M 5 100 L 45 100 M 0 25 L 25 0 L 25 100
;    s2=icon 2
;    s3=icon 3
;    s4=M 50 100 L 50 0 L 0 50 L 50 50
;    s5=icon 5
;    s6=icon 6
;    s7=M 0 0 L 50 0 L 25 75 L 25 100
;    s8=icon 8
;    s9=icon 9
;    s-=M 0 50 L 50 50
;    s'=M 25 100 L 25 25
;    s\=M 10 0 L 10 25 M 40 0 L 40 25


;origin-string=|
;    M 0.0 0.5
;    A -0.5 -0.5 1.0 1.0 90.0 360.0
;    A -0.5 -0.5 1.0 1.0 90.0 -360.0
;    L 0.0 -0.5
;    A -0.5 -0.5 1.0 1.0 270.0 90.0
;    L -0.5 0.0
;    A -0.5 -0.5 1.0 1.0 180.0 -90.0
;    Z
;tosort:
;    to-translate=|
;        path-symbol icon-two[] = {
;            {PATHS-MOVETO, 0 -0.75
;            A {0.45, 1.00, 0.50, 180.00, -216.87
;            L 0 0.0
;            L {0.50, 0.0
;        ]
;        
;        path-symbol icon-three[] = {
;            {PATHS-ARCMOVETO, 0 -0.50, 0.50, 0.50, 195.00
;            A 0 -0.50, 0.50, 195.00, 255.00
;            A 0 -0.50, 0.50, 270.00, 255.00
;        ]
;        
;        path-symbol icon-five[] = {
;            M 50 0 L 0 0 L 0 50 L 25 50 A 0.0, -0.5 0.5 0.5 90.0 -180.0 L 0 0
;        ]
;        
;        path-symbol icon-six[] = {
;            path.addEllipse(Vector(x+0.25*xs, y-0.25*ys), 0.25*xs, 0.25*ys)
;            M 0 75 L 0 25
;            path.arcTo(x+0.00*xs, y-1.00*ys, 0.50*xs, 0.50*ys, 180.00, -140.00)
;        ]
;        
;        path-symbol icon-eight[] = {
;            path.add-ellipse(Vector(x+0.25*xs, y-0.25*ys), 0.25*xs, 0.25*ys)
;            path.add-ellipse(Vector(x+0.25*xs, y-0.75*ys), 0.25*xs, 0.25*ys)
;        ]
;        
;        path-symbol icon-nine[] = {
;            path.add-ellipse(Vector(x+0.25*xs, y-0.75*ys), 0.25*xs, 0.25*ys)
;            M 0.50*xs, y-0.75*ys)
;            L x+0.50*xs, y-0.25*ys)
;            path.arcTo(x+0.00*xs, y-0.50*ys, 0.50*xs, 0.50*ys, 0.00, -140.00)
;        ]

;settings[to-add-to-property-editor] = 
;    
;    toolbar = ToolBar[10]
;    menu = Menu[10]
;    status-bar = toolButton = [
;        tk.Button() for i in range(8)
;    ]
;    toolButton = [
;        tk.Button() for i in range(PROPERTY-EDITORS)
;    ]
;    lineEdit = [
;        tk.LineEdit() for i in range(LINEEDIT-PROPERTY-EDITORS)
;    ]
;    comboBox = [
;        tk.ComboBox() for i in range(COMBOBOX-PROPERTY-EDITORS)
;    ]

;    opensave-recent-list-of-files = []
;    opensave-custom-filter = 

;    toolButtonTextSingleHeight =
;    toolButtonTextSingleRotation = tk.Button()

;    text-single-editors = {
;        contents={
;            entry=tk.LineEdit(),
;            toolbutton=tk.Button()
;    },
;        font=[tk.FontComboBox(), tk.Button()],
;        justify=[tk.ComboBox(), tk.Button()],
;        height=[tk.LineEdit(), tk.Button()],
;        rotation=[tk.LineEdit(), tk.Button()]
;    }

;    EmbVector pasteDelta
;    Vector scenePressPoint
;    Point pressPoint
;    Vector sceneMovePoint
;    Point movePoint
;    Vector sceneReleasePoint
;    Point releasePoint
;    Vector sceneGripPoint

;    Color rulerColor

;    Point  viewMousePoint
;    EmbVector sceneMousePoint
;    unsigned int snapLocatorColor
;    unsigned int gripColorCool
;    unsigned int gripColorHot
;    unsigned int crosshairColor
;    int precisionAngle
;    int precisionLength

;    Label status-bar-mouse-coord

;    #Used when checking if fields vary
;    fieldOldText = 
;    fieldNewText = 
;    fieldVariesText = 
;    fieldYesText = 
;    fieldNoText = 
;    fieldOnText = 
;    fieldOffText = 

;    ToolButton toolButtonArcClockwise
;    ComboBox comboBoxArcClockwise

;    GroupBox groupBoxGeometry[32]
;    GroupBox groupBoxGeneral
;    GroupBox groupBoxMiscArc
;    GroupBox groupBoxMiscPath
;    GroupBox groupBoxMiscPolyline
;    GroupBox groupBoxTextTextSingle
;    GroupBox groupBoxMiscTextSingle

;    Help {
;        Help
;        Opens the packaged help.

;        Changelog
;        Opens a log of what has recently changed.

;        About
;        Opens the about this software dialog.

;        What's This?
;        Details of the current design.
;    }

;mdi-window

;    QToolBar* toolbar[10]
;    QMenu* menu[10]
;    StatusBarButton* status-bar[8]
;    QToolButton* toolButton[PROPERTY-EDITORS]
;    QLineEdit* lineEdit[LINEEDIT-PROPERTY-EDITORS]
;    QComboBox* comboBox[COMBOBOX-PROPERTY-EDITORS]

;    QStringList opensave-recent-list-of-files
;    QString opensave-custom-filter


;    pasteDelta
;    Vector scenePressPoint
;    QPoint pressPoint
;    Vector sceneMovePoint
;    QPoint movePoint
;    Vector sceneReleasePoint
;    QPoint releasePoint
;    Vector sceneGripPoint

;    Color rulerColor

;    QPoint  viewMousePoint
;    sceneMousePoint
;    unsigned int qsnapLocatorColor
;    unsigned int gripColorCool
;    unsigned int gripColorHot
;    unsigned int crosshairColor
;    int precisionAngle
;    int precisionLength

;    QLabel* statusBarMouseCoord


;    #Used when checking if fields vary
;    QString fieldOldText
;    QString fieldNewText
;    QString fieldVariesText
;    QString fieldYesText
;    QString fieldNoText
;    QString fieldOnText
;    QString fieldOffText

;    QToolButton* toolButtonArcClockwise
;    QComboBox* comboBoxArcClockwise

;    QGroupBox* groupBoxGeometry[32]
;    QGroupBox* groupBoxGeneral
;    QGroupBox* groupBoxMiscArc
;    QGroupBox* groupBoxMiscPath
;    QGroupBox* groupBoxMiscPolyline
;    QGroupBox* groupBoxTextTextSingle
;    QGroupBox* groupBoxMiscTextSingle


;/*

(define ()
;draw-background(self, painter, rect)
;    painter.fill-rect(rect, backgroundBrush())

;    # HACK a = rect.intersects(grid-path.controlPointRect()
;    a = 1
;    if (self.gscene.property("ENABLE-GRID") and a) {
;        grid-pen = Pen (grid-color)
;        grid-pen.set-join-style("MiterJoin")
;        grid-pen.set-cosmetic(1)
;        painter.set-pen(grid-pen)
;        painter.draw-path(grid-path)
;        painter.draw-path(self.origin-path)
;        painter.fill-path(self.origin-path, grid-color)
;    }
)

(define ()
;horizontal-ruler-ticks(position, ruler-vert,
;            feet=False, little=0.20, medium=0.40, fraction=1.0)
;    " Returns an array of lines for the ticks part of the horizontal ruler. "
;    ticks = []
;    ruler-size = ruler-vert.subtract(position)
;    if settings["ruler-metric"]:
;        for i in range(10)
;            height = position.y
;            if i==5:
;                height -= ruler-size.y*medium
;            else:
;                height -= ruler-size.y*little
;            ticks += [Line(position.x, position.y+fraction*i,
;                            height, position.y+fraction*i)]
;    else:
;        if feet:
;            for i in range(12)
;                height = position.y - ruler-size.y*medium
;                ticks += [Line(ruler-vert.x, y+fraction*i, height, y+fraction*i)]
;        else:
;            for i in range(16)
;                if i==0:
;                    height = oy
;                elif i==5:
;                    height = ruler-horiz.y - ruler-size.y*medium
;                else:
;                    height = ruler-horiz.y - ruler-size.y*little
;                ticks += [Line(ruler-vert.x, y+fraction*i, height, y+fraction*i)]

;    return ticks
)

(define ()
;vertical-ruler-ticks(position, ruler-horiz,
;            feet=False, little=0.20, medium=0.40, fraction=1.0)
;    " Returns an array of lines for the ticks part of the vertical ruler. "
;    ticks = []
;    ruler-size = ruler-horiz.subtract(position)
;    if settings["ruler-metric"]:
;        for i in range(10)
;            height = ruler-horiz.y
;            if i==0:
;                height = origin.y
;            elif i==5:
;                height -= ruler-size.y*medium
;            else:
;                height -= ruler-size.y*little
;            ticks += [Line(x+fraction*i, ruler-horiz.y, x+fraction*i, height)]
;    else:
;        if feet:
;            for i in range(12)
;                height = position.y - ruler-size.y*medium
;                ticks += [Line(ruler-vert.x, y+fraction*i, height, y+fraction*i)]
;        else:
;            for i in range(16)
;                height = ruler-horiz.y
;                if i==0:
;                    height = oy
;                elif i==5:
;                    height -= ruler-size.y*medium
;                else:
;                    height -= ruler-size.y*little
;                ticks += [Line(ruler-vert.x, y+fraction*i, height, y+fraction*i)]

;    return ticks
)

; Draw horizontal and vertical rulers.
;
(define (draw-rulers view)
;
;    vw = self.width()
;    vh = self.height()
;    origin = map-to-scene(0,0)
;    ruler-horiz = map-to-scene(vw, settings["ruler-pixel-size"])
;    ruler-vert = map-to-scene(settings["ruler-pixel-size"], vh)

;    horizontal-ruler-size = ruler-horiz.subtract(origin)
;    vertical-ruler-size = ruler-vert.subtract(origin)

; NOTE:
; Drawing ruler if zoomed out too far will cause an assertion failure.
; We will limit the maximum size the ruler can be shown at.

;    maxSize = -1
;    # Intentional underflow
;    if horizontal-ruler-size.x >= maxSize or vertical-ruler-size.y >= maxSize:
;        return

;    distance = map-to-scene(settings.rulerPixelSize*3, 0).x() - origin.x
;    dist-str = str(distance)
;    dist-str-size = len(dist-str)
;    msd = int(dist-str[0]) # Most Significant Digit

;    if msd != -1:
;        return

;    msd += 1
;    if msd == 10:
;        msd = 1
;        dist-str.resize(dist-str-size+1)
;        dist-str-size += 1

;    dist-str.replace(0, 1, str(msd))
;    for i in range(1, dist-str-size)
;        dist-str.replace(i, 1, '0')

;    unit = dist-str.toInt()
;    fraction = 1.0
;    feet = 1
;    if settings["ruler-metric"]:
;        if unit < 10:
;            unit = 10
;        fraction = unit/10

;    else:
;        if unit <= 1:
;            (define (unit) 1)
;            feet = 0
;            fraction = (float)(unit/16)

;        else:
;            unit = round-to-multiple(1, unit, 12)
;            fraction = unit/12

;    little = 0.20
;    medium = 0.40
;    rh-text-offset = map-to-scene(3, 0).x() - origin.x
;    rv-text-offset = map-to-scene(0, 3).y() - origin.y
;    text-height = horizontal-ruler-size.y*medium

;    lines = [
;        Line(Vector(origin.x, ruler-horiz.y), Vector(ruler-horiz.x, ruler-horiz.y)),
;        Line(Vector(ruler-vert.x, origin.y), Vector(ruler-vert.x, ruler-vert.y)),
;        Line(Vector(scene-mouse-point.x, ruler-horiz.y), Vector(scene-mouse-point.x, origin.y)),
;        Line(Vector(ruler-vert.x, scene-mouse-point.y), Vector(origin.x, scene-mouse-point.y))
;    ]

;    transform = 0
;    ruler-pen = QPen(Color(0,0,0))
;    ruler-pen.set-cosmetic(1)
;    painter.set-pen(ruler-pen)
;    rect = Rect(origin.x, origin.y, horizontal-ruler-size.x, horizontal-ruler-size.y)
;    painter.fill-rect(rect, ruler-color)
;    rect = Rect(origin.x, origin.y, vertical-ruler-size.x, vertical-ruler-size.y)
;    painter.fill-rect(rect, ruler-color)

;    if origin.x - unit < -1e10:
;        return
;    x-flow = round-to-multiple(0, origin.x, unit)

;    if x-flow - unit < -1e10:
;        return

;    if origin.y - unit < -1e10:
;        return
;    y-flow = round-to-multiple(0, origin.y, unit)

;    if y-flow - unit < -1e10:
;        return

;    x-start = x-flow - unit
;    y-start = y-flow - unit

;    x = x-start
;    while x < ruler-horiz.x:
;        transform.translate(x+rh-text-offset, ruler-horiz.y-horizontal-ruler-size.y/2)
;        ruler-text-path = Path()
;        text-path = Path()
;        if settings["ruler-metric"]:
;            text-path = create-ruler-text-path(0, 0, str(x), text-height)
;        else:
;            if feet:
;                s = str(x/12) + "'"
;                text-path = create-ruler-text-path(0, 0, s, text-height)
;            else:
;                s = str(x) + "\""
;                text-path = create-ruler-text-path(0, 0, s, text-height)

;        ruler-text-path = transform.map(text-path)
;        transform.reset()
;        painter.draw-path(ruler-text-path)

;        lines += self.horizontal-ruler-ticks()
;        x += unit

;    y = y-start
;    while y < ruler-vert.y:
;        transform.translate(ruler-vert.x-vertical-ruler-size.x/2, y-rv-text-offset)
;        transform.rotate(-90)
;        ruler-text-path = Path()
;        text-path = Path()
;        if settings["ruler-metric"]:
;            text-path = create-ruler-text-path(0, 0, str(-y), text-height)
;        else:
;            if feet:
;                text-path = create-ruler-text-path(0, 0, str(-y/12)+"'", text-height)
;            else:
;                text-path = create-ruler-text-path(0, 0, str(-y)+"\"", text-height)

;        ruler-text-path = transform.map(text-path)
;        transform.reset()
;        painter.draw-path(ruler-text-path)

;        lines += self.vertical-ruler-ticks()
;        y += unit

;    painter.draw-lines(lines)
;    painter.fill-rect(Rect(origin.x, origin.y, vertical-ruler-size.x, horizontal-ruler-size.y), ruler-color)
)

(define (draw-crosshair)
  (let*
;    # painter.setBrush(Qt-NoBrush)
;    crosshairPen = QPen (Color-fromRgb(crosshair-color))
;    crosshairPen.set-cosmetic(1)
;    painter.set-pen(crosshairPen)

;    start = map-to-scene(view-mouse-point.x(), view-mouse-point.y()-settings.crosshair-size)
;    end = map-to-scene(view-mouse-point.x(), view-mouse-point.y()+settings.crosshair-size)
;    painter.draw-line(Line(start, end))

;    start = map-to-scene(view-mouse-point.x()-settings.crosshair-size, view-mouse-point.y())
;    end = map-to-scene(view-mouse-point.x()+settings.crosshair-size, view-mouse-point.y())
;    painter.drawLine(Line(start, end))

;    top-left = map-to-scene(view-mouse-point.x()-settings.selection-pickbox-size,
;        view-mouse-point.y()-settings.selection-pickbox-size)
;    bottom-right = map-to-scene(view-mouse-point.x()+settings.selection-pickbox-size,
;        view-mouse-point.y()+settings.selection-pickbox-size)
;    painter.drawRect(Rect(top-left, bottom-right))

;    p = QPixmap-grabWindow(winId())
;    p.save(QString("test.bmp"), "bmp")
  )
)

; TODO: and findClosestSnapPoint == 1
;
(define (draw-closest-qsnap view)
;    qsnap-pen = Pen(Color(qsnapLocator-color))
;    qsnap-pen.set-width(2)
;    qsnap-pen.set-join-style(Qt-MiterJoin)
;    qsnap-pen.set-cosmetic(1)
;    painter.set-pen(qsnap-pen)
;    qsnap-offset = Vector(settings["qsnap-locator-size"], settings["qsnap-locator-size"])

;    apertureSnapPoints = []
;    apertureitem-list = items(
;        view-mouse-point.x()-settings["qsnap-aperture-size"],
;        view-mouse-point.y()-settings["qsnap-aperture-size"],
;        settings["qsnap-aperture-size"]*2,
;        settings["qsnap-aperture-size"]*2)
;    for item in apertureitem-list:
;        if item.type != "Unknown":
;            tempitem-obj = item
;            if tempitem-obj:
;                aperture-snap-points += [ tempitem-obj.mouseSnapPoint(scene-mouse-point) ]


;    #TODO: Check for intersection snap points and add them to the list
;    for asp in aperture-snap-points:
;        p1 = map-from-scene(asp) - qsnap-offset
;        q1 = map-from-scene(asp) + qsnap-offset
;        painter.drawRect(Rect(map-to-scene(p1), map-to-scene(q1)))
)

; Draw grip points for all selected objects.
;
(define (draw-foreground view painter rect)
  (let*
;    grip-pen = Pen(rgb=grip-color-cool)
;    grip-pen.set-width(2)
;    grip-pen.set-join-style("MiterJoin")
;    grip-pen.set-cosmetic(1)
;    painter.set-pen(grip-pen)
;    grip-offset = Vector(
;        settings["selection-grip-size"], settings["selection-grip-size"]
;    )

;    selected-grip-points = []
;    selecteditem-list = self.gscene.selected-items()
;    if selecteditem-list.size() <= 100:
;        for item in selecteditem-list:
;            if item.type != "Unknown":
;                tempBase-obj = item
;                if tempBase-obj:
;                    selected-grip-points = tempBase-obj.all-grip-points()

;                for ssp in selected-grip-points:
;                    p1 = map-from-scene(ssp) - grip-offset
;                    q1 = map-from-scene(ssp) + grip-offset
;                    rect = Rect(map-to-scene(p1), map-to-scene(q1))

;                    if ssp == sceneGripPoint:
;                        painter.fill-rect(rect, rgb=grip-color-hot)
;                    else:
;                        painter.draw-rect(rect)
;                    }
;                }
;            }
;        }
;    }

;    if (!selecting-active) {
;        self.draw-closest-qsnap()
;        self.draw-crosshair()
;    }

    (if (enable-ruler) (draw-rulers))))

(define (create-ruler-text-path position str height)
;    int i
;    path = Path()

;    x-scale = height
;    y-scale = height
;    pos = Vector(x, y)
;    scale = Vector(0.01*height, 0.01*height)

;    for (i=0; i<strlen(str); i++) {
;        if (str[i] == '1') {
;            path.add-to-path(symbol-list["SYMBOL-one"], pos, scale)
;        }
;        if (str[i] == '2') {
;            position = Vector(x+0.00*x-scale, y-0.75*y-scale)
;            path.move-to(position)
;            path.arc-to(x+0.00*x-scale, y-1.00*y-scale, 0.50*x-scale, 0.50*y-scale, 180.00, -216.87)
;            path.line-to(x+0.00*x-scale, y-0.00*y-scale)
;            path.line-to(x+0.50*x-scale, y-0.00*y-scale)
;        }
;        if (str[i] == '3') {
;            path.arcmove-to(x+0.00*x-scale, y-0.50*y-scale, 0.50*x-scale, 0.50*y-scale, 195.00)
;            path.arc-to(x+0.00*x-scale, y-0.50*y-scale, 0.50*x-scale, 0.50*y-scale, 195.00, 255.00)
;            path.arc-to(x+0.00*x-scale, y-1.00*y-scale, 0.50*x-scale, 0.50*y-scale, 270.00, 255.00)
;        }
;        if (str[i] == '4') {
;            path.move-to(x+0.50*x-scale, y-0.00*y-scale)
;            path.line-to(x+0.50*x-scale, y-1.00*y-scale)
;            path.line-to(x+0.00*x-scale, y-0.50*y-scale)
;            path.line-to(x+0.50*x-scale, y-0.50*y-scale)
;        }
;        if (str[i] == '5') {
;            path.move-to(x+0.50*x-scale, y-1.00*y-scale)
;            path.line-to(x+0.00*x-scale, y-1.00*y-scale)
;            path.line-to(x+0.00*x-scale, y-0.50*y-scale)
;            path.line-to(x+0.25*x-scale, y-0.50*y-scale)
;            path.arc-to(x+0.00*x-scale, y-0.50*y-scale, 0.50*x-scale, 0.50*y-scale, 90.00, -180.00)
;            path.line-to(x+0.00*x-scale, y-0.00*y-scale)
;        }
;        if (str[i] == '6') {
;            path.addEllipse(Vector(x+0.25*x-scale, y-0.25*y-scale), 0.25*x-scale, 0.25*y-scale)
;            path.move-to(x+0.00*x-scale, y-0.25*y-scale)
;            path.line-to(x+0.00*x-scale, y-0.75*y-scale)
;            path.arc-to(x+0.00*x-scale, y-1.00*y-scale, 0.50*x-scale, 0.50*y-scale, 180.00, -140.00)
;        }
;        if (str[i] == '7') {
;            path.move-to(x+0.00*x-scale, y-1.00*y-scale)
;            path.line-to(x+0.50*x-scale, y-1.00*y-scale)
;            path.line-to(x+0.25*x-scale, y-0.25*y-scale)
;            path.line-to(x+0.25*x-scale, y-0.00*y-scale)
;        }
;        if (str[i] == '8') {
;            path.addEllipse(Vector(x+0.25*x-scale, y-0.25*y-scale), 0.25*x-scale, 0.25*y-scale)
;            path.addEllipse(Vector(x+0.25*x-scale, y-0.75*y-scale), 0.25*x-scale, 0.25*y-scale)
;        }
;        if (str[i] == '9') {
;            path.addEllipse(Vector(x+0.25*x-scale, y-0.75*y-scale), 0.25*x-scale, 0.25*y-scale)
;            path.move-to(x+0.50*x-scale, y-0.75*y-scale)
;            path.line-to(x+0.50*x-scale, y-0.25*y-scale)
;            path.arc-to(x+0.00*x-scale, y-0.50*y-scale, 0.50*x-scale, 0.50*y-scale, 0.00, -140.00)
;        }
;        if (str[i] == '0') {
;            #path.addEllipse(Vector(x+0.25*x-scale, y-0.50*y-scale), 0.25*x-scale, 0.50*y-scale)

;            path.move-to(x+0.00*x-scale, y-0.75*y-scale)
;            path.line-to(x+0.00*x-scale, y-0.25*y-scale)
;            path.arc-to(x+0.00*x-scale, y-0.50*y-scale, 0.50*x-scale, 0.50*y-scale, 180.00, 180.00)
;            path.line-to(x+0.50*x-scale, y-0.75*y-scale)
;            path.arc-to(x+0.00*x-scale, y-1.00*y-scale, 0.50*x-scale, 0.50*y-scale, 0.00, 180.00)
;        }
;        if (str[i] == '-') {
;            path.move-to(x+0.00*x-scale, y-0.50*y-scale)
;            path.line-to(x+0.50*x-scale, y-0.50*y-scale)
;        }
;        if (str[i] == '\'') {
;            path.move-to(x+0.25*x-scale, y-1.00*y-scale)
;            path.line-to(x+0.25*x-scale, y-0.75*y-scale)
;        }
;        if (str[i] == '"') {
;            path.move-to(x+0.10*x-scale, y-1.00*y-scale)
;            path.line-to(x+0.10*x-scale, y-0.75*y-scale)
;            path.move-to(x+0.40*x-scale, y-1.00*y-scale)
;            path.line-to(x+0.40*x-scale, y-0.75*y-scale)
;        }

;        x += 0.75*x-scale
;        pos[0] = x
;    }
;    return path
)

(define rectangular-grid 1)
(define circular-grid 2)
(define isometric-grid 3)

(define (create-grid gridType)
  (let*
    (define grid-path (Path))
    (define enable-grid 1)
    (if (= gridType rectangular-grid)
      (create-grid-rect)
      (if (= gridType circular-grid)
        (create-grid-polar)
        (if (= gridType isometric-grid)
          (create-grid-iso)
          (define enable-grid 0)))) 
    (create-origin)
    
    ; EXPERIMENT
    ; Tagging experiments with the path system to the origin.
    (define origin-position (vector 10.0 0.0))
    (define origin-scale (vector 1.0 1.0))
;    self.origin-path.add-list-to-path(origin-string, position, scale)
    (update-current-scene)))

(define (create-origin)
    ; TODO: Make Origin Customizable.
;    self.origin-path = Path()

;    if settings["grid-show-origin"]) {
;        # self.origin-path.addEllipse(Vector(0,0), 0.5, 0.5)
      ; TODO: Make Origin Customizable.
;        position = [0.0, 0.0]
;        scale = [1.0, 1.0]
;        self.origin-path.add-list-to-path(origin-string, position, scale)
;    }
)

(define (create-grid-rect)
;    x-spacing = settings["grid-spacing"]["x"]
;    y-spacing = settings["grid-spacing"]["y"]

;    gr = Rect(0, 0,
;                settings["grid-size"]["x"],
;                -settings["grid-size"]["y"])
;    # Ensure the loop will work correctly with negative numbers
;    point1-x = min(gr.left(), gr.right())
;    point1-y = min(gr.top(), gr.bottom())
;    point2-x = max(gr.left(), gr.right())
;    point2-y = max(gr.top(), gr.bottom())

;    grid-path = Path()
;    grid-path.add-rect(gr)
;    gx = point1-x
;    while gx < point2-x:
;        gy = point1-y
;        while gy < point2-y:
;            grid-path.move-to(point1-x, gy)
;            grid-path.line-to(point2-x, gy)
;            grid-path.move-to(gx, point1-y)
;            grid-path.line-to(gx, point2-y)
;            gy += y-spacing
;        gx += x-spacing

;    # Center the Grid
;    grid-rect = grid-path.bounding-rect()
;    bx = grid-rect.width() / 2.0
;    by = -grid-rect.height() / 2.0
;    center = Vector(settings["grid-center"]["x"], -settings["grid-center"]["y"])
;    delta-x = center.x - bx
;    delta-y = center.y - by

;    if settings["grid-center-on-origin"]:
;        grid-path.translate(-bx, -by)
;    else:
;        grid-path.translate(delta-x, delta-y)
;    */
)

(define (create-grid-polar)
;    double r, ang
;    /*
;    rad-spacing = settings["grid-spacing-radius"]
;    ang-spacing = settings["grid-spacing-angle"]

;    rad = settings["grid-size-radius"]

;    grid-path = Path()
;    grid-path.addEllipse(Vector(0,0), rad, rad)
;    for (r=0.0; r < rad; r+=rad-spacing) {
;        grid-path.addEllipse(Vector(0,0), r, r)
;    }

;    for (ang=0.0; ang<360.0; ang+=ang-spacing) {
;        grid-path.move-to(0,0)
;        grid-path.line-to(Line-from-polar(rad, ang).p2())
;    }

;    if (not settings["grid-center-on-origin"]) {
;        grid-path.translate(settings.grid-center.x, -settings.grid-center.y)
;    }
;    */
)

(define (create-grid-iso)
   ; Ensure the loop will work correctly with negative numbers
;    isoW = abs(settings["grid-size"]["x"])
;    isoH = abs(settings["grid-size"]["y"])

;    p1 = Vector(0,0)
;    p2 = Line-from-polar(isoW, 30).p2()
;    p3 = Line-from-polar(isoH, 150).p2()
;    p4 = p2 + p3

;    grid-path = Path()
;    grid-path.move-to(p1)
;    grid-path.line-to(p2)
;    grid-path.line-to(p4)
;    grid-path.line-to(p3)
;    grid-path.line-to(p1)

;    x = 0.0
;    while x < isoW:
;        y = 0.0
;        while y < isoH:
;            px = Line-from-polar(x, 30).p2()
;            py = Line-from-polar(y, 150).p2()

;            grid-path.move-to(px)
;            grid-path.line-to(px+p3)
;            grid-path.move-to(py)
;            grid-path.line-to(py+p2)
;            y += settings["grid-spacing"]["y"]
;        x += settings["grid-spacing"]["x"]

;    #Center the Grid
;    grid-rect = grid-path.bounding-rect()
;    # bx is unused
;    by = -grid-rect.height()/2.0
;    cx = settings["grid-center"]["x"]
;    cy = -settings["grid-center"]["y"]

;    if settings["grid-center-on-origin"]:
;        grid-path.translate(0, -by)
;    else:
;        grid-path.translate(0, -by)
;        grid-path.translate(cx, cy)
)

(define (native-add-text-single str position rot fill rubber-mode)
   (let*
      (define (gview) (active-view))
      (define (gscene) (scene gview))
      (if (and gview gscene)
;        obj = TextSingle(str, x, -y, get-current-color())
;        obj.objTextFont = settings["text-font"]
;        obj.obj-text = settings["text-style"]
;        obj.set-object-text(obj.objText)
;        obj.set-rotation(-rot); */
;        /* TODO: single line text fill. */ /*
;        obj.set-object-rubber-mode(rubber-mode)
;        (if (rubber-mode)
;            gview.add-to-rubber-room(obj)
;            gscene.add-item(obj)
;            gscene.update()
;        )
     )))

(define (native-add-line line rot rubber-mode)
;    /* gview = active-view()
;    gscene = gview.scene()
;    if gview and gscene:
;        obj = Line(x1, -y1, x2, -y2, get-current-color())
;        obj.set-rotation(-rot)
;        obj.set-object-rubber-mode(rubber-mode)
;        if rubber-mode:
;            gview.add-to-rubber-room(obj)
;            gscene.add-item(obj)
;            gscene.update(); */
)

; x (double)
; y (double)
; w (double)
; h (double)
; rot (double)
; fill (EmbColor)
; rubber-mode (int)
;
(define (native-add-rectangle x y w h rot fill rubber-mode)
;    gview = active-view()
;    gscene = gview.scene()
;    if (gview && gscene) {
;        obj = Rect(x, -y, w, -h, get-current-color())
;        obj.set-rotation(-rot)
;        obj.set-object-rubber-mode(rubber-mode)
; TODO: rect fill
;        if (rubber-mode) {
;            gview.add-to-rubber-room(obj)
;            gscene.add-item(obj)
;            gscene.update()
;        }
;    }
)

; start (EmbVector)
; mid (EmbVector)
; end (EmbVector)
; rubber-mode (int)
;
(define (add-arc start mid end rubber-mode)
;    /*gview = active-view()
;    scene = active-scene()
;    if (gview && scene) {
;        arc-obj = Arc(start.x, -start.y, mid.x, -mid.y, end.x, -end.y, get-current-color())
;        arc-obj.set-object-rubber-mode(rubber-mode)
;        if rubber-mode:
;            gview.add-to-rubber-room(arc-obj)
;        scene.add-item(arc-obj)
;        scene.update()
;    }
)

(define ()
;add-circle(EmbVector center, double radius, EmbColor fill, int rubber-mode)
;    /*gview = active-view()
;    gscene = gview.scene()
;    if (gview && gscene) {
;        obj = Circle(center.x, -center.y, radius, get-current-color())
;        obj.set-object-rubber-mode(rubber-mode)
;        #TODO: circle fill
;        if (rubber-mode) {
;            gview.add-to-rubber-room(obj)
;            gscene.add-item(obj)
;            gscene.update()
;        }
;    } */
)

(define ()
;add-ellipse(
;    EmbEllipse ellipse, double rot, EmbColor fill,
;    int rubber-mode)
;    /* gview = active-view()
;    gscene = gview.scene()
;    if (gview && gscene) {
;        obj = Ellipse(center.x, -center.y, width, height, get-current-color())
;        obj.set-rotation(-rot)
;        obj.set-object-rubber-mode(rubber-mode); */
;        /* TODO: ellipse fill */ /*
;        if (rubber-mode) {
;            gview.add-to-rubber-room(obj)
;            gscene.add-item(obj)
;            gscene.update()
;        }
;    } */
)

(define (add-point)
; (x, y)
;    gview = active-view()
;    if (gview) {
;        obj = Point(x, -y, get-current-color())
;    }
)

; NOTE:
; This native is different than the rest in that the Y+ is down
; (scripters need not worry about this).
;
(define (add-polygon)
;(EmbVector start, EmbVector p, int rubber-mode)
;    gview = active-view()
;    gscene = gview.scene()
;    if (gview && gscene) {
;        obj = Polygon(start, p, get-current-color())
;        obj.set-object-rubber-mode(rubber-mode)
;        if (rubber-mode) {
;            gview.add-to-rubber-room(obj)
;            gscene.add-item(obj)
;            gscene.update()
;        }
;    }
)

; NOTE:
; This native is different than the rest in that the Y+ is
; down (scripters need not worry about this).
;
(define (add-polyline)
;(EmbVector start, EmbVector p, int rubber-mode)
;    /* gview = active-view()
;    gscene = gview.scene()
;    if (gview and gscene) {
;        obj = Polyline(start, p, get-current-color())
;        obj.set-object-rubber-mode(rubber-mode)
;        if (rubber-mode) {
;            gview.add-to-rubber-room(obj)
;            gscene.add-item(obj)
;            gscene.update()
;        }
;    } */
)


(define (add-dim-leader)
;(EmbDimLeader dim-leader double rot, int rubber-mode)
;    /*gview = active-view()
;    gscene = gview.scene()
;    if (gview and gscene) {
;        obj = DimLeader(x1, -y1, x2, -y2, get-current-color())
;        obj.set-rotation(-rot)
;        obj.set-object-rubber-mode(rubber-mode)
;        if (rubber-mode) {
;            gview.add-to-rubber-room(obj)
;            gscene.add-item(obj)
;            gscene.update()
;        }
;    }
)


;/*
; * TODO: Save a Brother PEL image (An 8bpp, 130x113 pixel
; *     monochromatic? bitmap image) Why 8bpp when only 1bpp is needed?
; *
; * TODO: Should BMC be limited to ~32KB or is this a mix up with Bitmap Cache?
; * TODO: Is there/should there be other embedded data in the bitmap
; *     besides the image itself?
; * NOTE: Can save a Singer BMC image (An 8bpp, 130x113 pixel colored
; *     bitmap image)
; * TODO: figure out how to center the image, right now it just plops
; *     it to the left side.
;*/
(define ()
;saveBMC(void/* MdiWindow *subwindow */)
;    /*  
;    img = QImage(150, 150, "QImage-Format-ARGB32-Premultiplied")
;    img.fill(qRgb(255,255,255))
;    extents = gscene.itemsBoundingRect()

;    painter = QPainter(img)
;    targetRect = Rect(0,0,150,150)
;    if (printing-disable-bg) { */
;        /* TODO: Make BMC background into it's own setting? */ /*
;        brush = gscene.backgroundBrush()
;        gscene.setBackgroundBrush(Qt-NoBrush)
;        gscene.update()
;        gscene.render(painter, targetRect, extents, "Qt-KeepAspectRatio")
;        gscene.setBackgroundBrush(brush)
;    }
;    else {
;        gscene.update()
;        gscene.render(painter, targetRect, extents, "Qt-KeepAspectRatio")
;    }
;    img.convertToFormat(QImage-Format-Indexed8, Qt-ThresholdDither|Qt-AvoidDither).save("test.bmc", "BMP")
;    */
)

; SETTINGS

(define (settings-snap)
;    (debug-message "snap settings tab")
)

(define (settings-grid)
;    (debug-message "grid settings tab")
)

(define (settings-ruler)
;    (debug-message "ruler settings tab")
)

(define (settings-ortho)
;    (debug-message "settings ortho")
)

;void
;settings-polar(void)
;    (debug-message "stub")
)

;void
;settings-qsnap(void)
;    (debug-message "stub")
)

;void
;settings-qtrack(void)
;    (debug-message "stub")
)

;void
;settings-lwt(void)
;    (debug-message "stub")
)

;void
;toggle-grid(void)
;    (debug-message "StatusBarButton toggleGrid()")
;    /* show-grid = !show-grid; */
)

;void
;toggle-ruler(void)
;    (debug-message "StatusBarButton toggleRuler()")
;    /* show-ruler = !show-ruler; */
)

;void
;toggle-ortho(void)
;    (debug-message "StatusBarButton toggleOrtho()")
;    /* show-ortho = !show-ortho; */
)


(define (set-snap active)
;    (debug-message "View toggle-snap()")
;    set-override-cursor("WaitCursor")
;    #  TODO: finish this.
;    gscene.set-property("ENABLE-SNAP", active)
;    gscene.update()
;    restore-override-cursor()
)

;void
;toggle-track(void)
;    (debug-message "StatusBarButton toggleQTrack()")
;    /* track-mode = !track-mode; */
)

;void
;toggle-lwt(void)
;    (debug-message "StatusBarButton toggleLwt()")
;    /* show-lwt = !show-lwt; */
)

;/*
; * Switch to rendering all line weights more accurately, so the effect
; * of different thread weights can be understood.
; */
;void
;enable-lwt(void)
;    (debug-message "StatusBarButton enableLwt()")
;    /* show-lwt = 1; */
)

;/*
; * Switch to rendering all line weights the same, so the effect
; * of different thread weights can be ignored.
; */
;void
;disable-lwt(void)
;    (debug-message "StatusBarButton disableLwt()")
;    /* show-lwt = 0; */
)

;/*
; * Turn real rendering on and see the pattern as an approximation of
; * what the stitched embroidery will look like.
; */
(define (enable-real)
;    (debug-message "StatusBarButton enableReal()")
;    (define (real-render) 1)
)

;/*
; * Turn real rendering off and see the pattern as collection of
; * geometric primatives.
; */
(define (disable-real)
;    (debug-message "StatusBarButton disableReal()")
;    real-render = 0
)

(define (create-settings-widget setting)
;    /* translate(setting.description),
;        int-dialog[setting.index] = int-setting[setting.index]; */
;    if (setting.type[0] == 'i') { /* Int */
;        return
;    }
;    if (setting.type[1] == 'o') { /* dOuble */
;        return
;    }
;    if (setting.type[1] == 'r') { /* dRopdown */
;        return
;    }
;    if (setting.type[0] == 's') { /* String */
;        return
;    }
;    /* Error. */
)

(define (create-settings-box box)
;    int i
;    (debug-message box.title)
;    for (i=0; box.settings[i].type >= 0; i++) {
;        create-settings-widget(box.settings[i])
;    }
)

(define (create-settings-tab tab)
;    int i
;    (debug-message tab.title)
;    for (i=0; i<tab.n-boxes; i++) {
;        create-settings-box(tab.box[i])
;    }
)


;/* 
;class settings-dialog-action()
;    tab-widget* tab-widget
;    dialogButtonBox* buttonBox
;*/

;/* showTab is the tab index, use the TAB-GENERAL style defines.
; */
(define (settings-dialog-init showTab)
;    /* mw = mw
;    accept = copy()
;    dialog = copy()
;    preview = copy()

;    window = tk.Tk()
;    window.size(750,550)
;    tab-widget = tk.tab-widget(window); */

;    /* TODO: Add icons to tabs */
;    /* tab-widget.add-tab(create-tab-general(), translate("General"))
;    tab-widget.add-tab(createTabFilesPaths(), translate("Files/Paths"))
;    tab-widget.add-tab(createTabDisplay(), translate("Display"))
;    tab-widget.add-tab(createTabOpenSave(), translate("Open/Save"))
;    tab-widget.add-tab(createTabPrinting(), translate("Printing"))
;    tab-widget.add-tab(createTabSnap(), translate("Snap"))
;    tab-widget.add-tab(createTabGridRuler(), translate("Grid/Ruler"))
;    tab-widget.add-tab(createTabOrthoPolar(), translate("Ortho/Polar"))
;    tab-widget.add-tab(createTabQuickSnap(), translate("QuickSnap"))
;    tab-widget.add-tab(createTabQuickTrack(), translate("QuickTrack"))
;    tab-widget.add-tab(createTabLineWeight(), translate("LineWeight"))
;    tab-widget.add-tab(createTabSelection(), translate("Selection"))

;    for i in range(12)
;        if showTab == settings-tab-label[i]:
;            tab-widget.setCurrentIndex(i)

;    buttonBox = tk.DialogButtonBox(QDialogButtonBox-Ok | tk.DialogButtonBox-Cancel)

;    # connect(buttonBox, SIGNAL(accepted()), this, SLOT(acceptChanges()))
;    # connect(buttonBox, SIGNAL(rejected()), this, SLOT(rejectChanges()))

;    vbox-layout-main = tk.VBoxLayout()
;    vbox-layout-main.add-widget(tab-widget)
;    vbox-layout-main.add-widget(buttonBox)
;    setLayout(vbox-layout-main)

;    window.title(translate("Settings"))
;    window.setOverrideCursor("ArrowCursor"); */
)

(define ()
;create-tab-general(void)
;    /* widget = tk.Widget(window)

;    #Language
;    groupBoxLanguage = tk.GroupBox(translate("Language"), widget)

;    labelLanguage = tk.Label(translate("Language (Requires Restart)"), groupBoxLanguage)
;    combo-boxLanguage = tk.combo-box(groupBoxLanguage)
;    to-lower(dialog-general-language, general-language)
;    combo-boxLanguage.add-item("Default")
;    combo-boxLanguage.add-item("System")
;    combo-boxLanguage.insertSeparator(2)
;    trDir = tk.App.applicationDirPath()
;    trDir.cd("translations")
;    for dirName in trDir.entryList(QDir-Dirs | tk.Dir-NoDotAndDotDot)
;        dirName[0] = dirName[0].toUpper()
;        combo-boxLanguage.add-item(dirName)

;    current = dialog-general-language
;    current[0] = current[0].toUpper()
;    combo-boxLanguage.setCurrentIndex(combo-boxLanguage.findText(current))
;    #connect(combo-boxLanguage, SIGNAL(current-index-changed("")), this, SLOT(combo-boxLanguageCurrent-index-changed("")))

;    vboxLayoutLanguage = tk.VBoxLayout(groupBoxLanguage)
;    vboxLayoutLanguage.add-widget(labelLanguage)
;    vboxLayoutLanguage.add-widget(combo-boxLanguage)
;    groupBoxLanguage.setLayout(vboxLayoutLanguage)

;    #Icons
;    groupBoxIcon = tk.GroupBox(translate("Icons"), widget)

;    labelIconTheme = tk.Label(translate("Icon Theme"), groupBoxIcon)
;    combo-boxIconTheme = tk.combo-box(groupBoxIcon)
;    dir = tk.App.applicationDirPath()
;    dir.cd("icons")
;    dialog-general-icon-theme = general-icon-theme
;    for dirName in dir.entryList(QDir-Dirs | tk.Dir-NoDotAndDotDot)
;        combo-boxIconTheme.add-item(load-icon(theme-xpm), dirName)

;    combo-boxIconTheme.setCurrentIndex(combo-boxIconTheme.findText(dialog-general-icon-theme))
;    #connect(combo-boxIconTheme, SIGNAL(current-index-changed("")), this, SLOT(combo-boxIconThemeCurrent-index-changed("")))

;    labelIconSize = tk.Label(translate("Icon Size"), groupBoxIcon)
;    combo-box-icon-size = tk.combo-box(groupBoxIcon)
;    combo-box-icon-size.add-item(load-icon("icon16-xpm"), "Very Small", 16)
;    combo-box-icon-size.add-item(load-icon("icon24-xpm"), "Small", 24)
;    combo-box-icon-size.add-item(load-icon("icon32-xpm"), "Medium", 32)
;    combo-box-icon-size.add-item(load-icon("icon48-xpm"), "Large", 48)
;    combo-box-icon-size.add-item(load-icon("icon64-xpm"), "Very Large", 64)
;    combo-box-icon-size.add-item(load-icon("icon128-xpm"), "I'm Blind", 128)
;    dialog-general-icon-size = general-icon-size
;    combo-box-icon-size.setCurrentIndex(combo-box-icon-size.findData(dialog-general-icon-size))
;    #connect(combo-box-icon-size, SIGNAL(current-index-changed(int)), this, SLOT(combo-box-icon-sizeCurrent-index-changed(int)))

;    vbox-layout-icon = tk.QVBoxLayout(groupBoxIcon)
;    vbox-layout-icon.add-widget(labelIconTheme)
;    vbox-layout-icon.add-widget(combo-boxIconTheme)
;    vbox-layout-icon.add-widget(labelIconSize)
;    vbox-layout-icon.add-widget(combo-box-icon-size)
;    groupBoxIcon.setLayout(vbox-layout-icon)

;    #Mdi Background
;    groupBoxMdiBG = tk.GroupBox(window, text=translate("Background"))

;    check-box-mdi-bg-use-logo = tk.check-box(groupBoxMdiBG, text=translate("Use Logo"))
;    dialog-general-mdi-bg-use-logo = general-mdi-bg-use-logo
;    preview["general-mdi-bg-use-logo = dialog-general-mdi-bg-use-logo
;    check-box-mdi-bg-use-logo.setChecked(preview["general-mdi-bg-use-logo)
;    #connect(check-box-mdi-bg-use-logo, SIGNAL(-state-changed(int)), this, SLOT(check-boxGeneralMdiBGUseLogo-state-changed(int)))

;    button-mdi-bg-logo = tk.Button(groupBoxMdiBG, text=translate("Choose"))
;    button-mdi-bg-logo.set-enabled(dialog-general-mdi-bg-use-logo)
;    dialog-general-mdi-bg-logo = general-mdi-bg-logo
;    accept["general-mdi-bg-logo = dialog-general-mdi-bg-logo
;    #connect(button-mdi-bg-logo, SIGNAL(clicked()), this, SLOT(chooseGeneralMdiBackgroundLogo()))
;    #connect(check-box-mdi-bg-use-logo, SIGNAL(toggled(int)), button-mdi-bg-logo, SLOT(set-enabled(int)))

;    check-box-mdi-bg-use-texture = tk.check-box(translate("Use Texture"), groupBoxMdiBG)
;    dialog-general-mdi-bg-use-texture = general-mdi-bg-use-texture
;    preview["general-mdi-bg-use-texture = dialog-general-mdi-bg-use-texture
;    check-box-mdi-bg-use-texture.setChecked(preview["general-mdi-bg-use-texture)
;    #connect(check-box-mdi-bg-use-texture, SIGNAL(-state-changed(int)), this, SLOT(check-boxGeneralMdiBGUseTexture-state-changed(int)))

;    buttonMdiBGTexture = tk.Button(groupBoxMdiBG, text=translate("Choose"))
;    buttonMdiBGTexture.set-enabled(dialog-general-mdi-bg-use-texture)
;    dialog-general-mdi-bg-texture = general-mdi-bg-texture
;    accept["general-mdi-bg-texture = dialog-general-mdi-bg-texture
;    #connect(buttonMdiBGTexture, SIGNAL(clicked()), this, SLOT(chooseGeneralMdiBackgroundTexture()))
;    #connect(check-box-mdi-bg-use-texture, SIGNAL(toggled(int)), buttonMdiBGTexture, SLOT(set-enabled(int)))

;    check-boxMdiBGUseColor = tk.check-box(translate("Use Color"), groupBoxMdiBG)
;    dialog-general-mdi-bg-use-color = general-mdi-bg-use-color
;    preview["general-mdi-bg-use-color = dialog-general-mdi-bg-use-color
;    check-boxMdiBGUseColor.setChecked(preview.general-mdi-bg-use-color)
;    #connect(check-boxMdiBGUseColor, SIGNAL(-state-changed(int)), this, SLOT(check-boxGeneralMdiBGUseColor-state-changed(int)))

;    buttonMdiBGColor = PushButton(translate("Choose"), groupBoxMdiBG)
;    buttonMdiBGColor.set-enabled(dialog-general-mdi-bg-use-color)
;    dialog-general-mdi-bg-color = general-mdi-bg-color
;    preview["general-mdi-bg-color = dialog-general-mdi-bg-color
;    accept["general-mdi-bg-color = dialog-general-mdi-bg-color
;    mdiBGPix = Image(16,16)
;    mdiBGPix.fill(Color(preview.general-mdi-bg-color))
;    buttonMdiBGColor.setIcon(QIcon(mdiBGPix))
;    #connect(buttonMdiBGColor, SIGNAL(clicked()), this, SLOT(chooseGeneralMdiBackgroundColor()))
;    #connect(check-boxMdiBGUseColor, SIGNAL(toggled(int)), buttonMdiBGColor, SLOT(set-enabled(int)))

;    gridLayoutMdiBG = tk.GridLayout(widget)
;    gridLayoutMdiBG.add-widget(check-box-mdi-bg-use-logo, 0, 0, "Align Left")
;    gridLayoutMdiBG.add-widget(button-mdi-bg-logo, 0, 1, "Align Right")
;    gridLayoutMdiBG.add-widget(check-box-mdi-bg-use-texture, 1, 0, "Align Left")
;    gridLayoutMdiBG.add-widget(buttonMdiBGTexture, 1, 1, "Align Right")
;    gridLayoutMdiBG.add-widget(check-boxMdiBGUseColor, 2, 0, "Align Left")
;    gridLayoutMdiBG.add-widget(buttonMdiBGColor, 2, 1, "Align Right")
;    groupBoxMdiBG.setLayout(gridLayoutMdiBG)

;    #Tips
;    groupBoxTips = tk.GroupBox(translate("Tips"), widget)

;    check-boxTipOfTheDay = tk.check-box(translate("Show Tip of the Day on startup"), groupBoxTips)
;    dialog-general-tip-of-the-day = general-tip-of-the-day
;    check-boxTipOfTheDay.setChecked(dialog-general-tip-of-the-day)
;    #connect(check-boxTipOfTheDay, SIGNAL(-state-changed(int)), this, SLOT(check-boxTipOfTheDay-state-changed(int)))

;    vboxLayoutTips = tk.VBoxLayout(groupBoxTips)
;    vboxLayoutTips.add-widget(check-boxTipOfTheDay)
;    groupBoxTips.setLayout(vboxLayoutTips)

;    #Help Browser
;    groupBoxHelpBrowser = tk.GroupBox(translate("Help Browser"), widget)

;    radio-button-system-help-browser = tk.RadioButton(translate("System"), groupBoxHelpBrowser)
;    radio-button-system-help-browser.setChecked(general-system-help-browser)
;    radio-button-custom-help-browser = tk.RadioButton(translate("Custom"), groupBoxHelpBrowser)
;    radio-button-custom-help-browser.setChecked(!general-system-help-browser)
;    radio-button-custom-help-browser.set-enabled(0); TODO: finish this */

;    /*
;    vboxLayoutHelpBrowser = tk.VBoxLayout(groupBoxHelpBrowser)
;    vboxLayoutHelpBrowser.add-widget(radio-button-system-help-browser)
;    vboxLayoutHelpBrowser.add-widget(radio-button-custom-help-browser)
;    groupBoxHelpBrowser.setLayout(vboxLayoutHelpBrowser)
;*/
;    /* Widget Layout */ /*
;    vbox-layout-main = tk.VBoxLayout(widget)
;    vbox-layout-main.add-widget(groupBoxLanguage)
;    vbox-layout-main.add-widget(groupBoxIcon)
;    vbox-layout-main.add-widget(groupBoxMdiBG)
;    vbox-layout-main.add-widget(groupBoxTips)
;    vbox-layout-main.add-widget(groupBoxHelpBrowser)
;    vbox-layout-main.addStretch(1)
;    widget.setLayout(vbox-layout-main)

;    scroll-area = tk.scroll-area(this)
;    scroll-area.setWidgetResizable(1)
;    scroll-area.setWidget(widget)
;    return scroll-area; */
)

(define ()
;create-tab-files-paths(void)
;    /* widget = tk.Widget(this)

;    scroll-area = tk.scroll-area(this)
;    scroll-area.setWidgetResizable(1)
;    scroll-area.setWidget(widget)
;    return scroll-area; */
)

(define ()
;create-tab-display(void)
;    /*
;    widget = tk.Widget(this)

;    #Rendering
;    #TODO: Review OpenGL and Rendering settings for future inclusion
;    #
;    groupBoxRender = tk.GroupBox(translate("Rendering"), widget)

;    check-boxUseOpenGL = tk.check-box(translate("Use OpenGL"), groupBoxRender)
;    int-dialog[INT-DISPLAY-USE-OPENGL] = int-setting[INT-DISPLAY-USE-OPENGL]
;    check-boxUseOpenGL.setChecked(int-dialog[INT-DISPLAY-USE-OPENGL)
;    #connect(check-boxUseOpenGL, SIGNAL(-state-changed(int)), this, SLOT(check-boxUseOpenGL-state-changed(int)))

;    check-boxRenderHintAA = tk.check-box(translate("Antialias"), groupBoxRender)
;    dialog-display-renderhint-aa = display-render-hint-aa
;    check-boxRenderHintAA.setChecked(dialog-display-renderhint-aa)
;    #connect(check-boxRenderHintAA, SIGNAL(-state-changed(int)), this, SLOT(check-boxRenderHintAA-state-changed(int)))

;    check-boxRenderHintTextAA = tk.check-box(translate("Antialias Text"), groupBoxRender)
;    dialog-display-renderhint-text-aa = display-render-hint-text-aa
;    check-boxRenderHintTextAA.setChecked(dialog-display-renderhint-text-aa)
;    #connect(check-boxRenderHintTextAA, SIGNAL(-state-changed(int)), this, SLOT(check-boxRenderHintTextAA-state-changed(int)))

;    check-boxRenderHintSmoothPix = tk.check-box(translate("Smooth Pixmap"), groupBoxRender)
;    dialog-display-renderhint-smooth-pix = display-render-hint-smooth-pix
;    check-boxRenderHintSmoothPix.setChecked(dialog-display-renderhint-smooth-pix)
;    #connect(check-boxRenderHintSmoothPix, SIGNAL(-state-changed(int)), this, SLOT(check-boxRenderHintSmoothPix-state-changed(int)))

;    check-boxRenderHintHighAA = tk.check-box(translate("High Quality Antialiasing (OpenGL)"), groupBoxRender)
;    dialog-display-renderhint-high-aa = display-render-hint-high-aa
;    check-boxRenderHintHighAA.setChecked(dialog-display-renderhint-high-aa)
;    #connect(check-boxRenderHintHighAA, SIGNAL(-state-changed(int)), this, SLOT(check-boxRenderHintHighAA-state-changed(int)))

;    check-boxRenderHintNonCosmetic = tk.check-box(translate("Non Cosmetic"), groupBoxRender)
;    dialog-display-renderhint-noncosmetic = display-render-hint-non-cosmetic
;    check-boxRenderHintNonCosmetic.setChecked(dialog-display-renderhint-noncosmetic)
;    #connect(check-boxRenderHintNonCosmetic, SIGNAL(-state-changed(int)), this, SLOT(check-boxRenderHintNonCosmetic-state-changed(int)))

;    vboxLayoutRender = tk.VBoxLayout(groupBoxRender)
;    vboxLayoutRender.add-widget(check-boxUseOpenGL)
;    vboxLayoutRender.add-widget(check-boxRenderHintAA)
;    vboxLayoutRender.add-widget(check-boxRenderHintTextAA)
;    vboxLayoutRender.add-widget(check-boxRenderHintSmoothPix)
;    vboxLayoutRender.add-widget(check-boxRenderHintHighAA)
;    vboxLayoutRender.add-widget(check-boxRenderHintNonCosmetic)
;    groupBoxRender.setLayout(vboxLayoutRender)

;    #ScrollBars
;    groupBoxScrollBars = tk.GroupBox(translate("ScrollBars"), widget)

;    check-boxShowScrollBars = tk.check-box(translate("Show ScrollBars"), groupBoxScrollBars)
;    dialog-display-show-scrollbars = display-show-scrollbars
;    preview.display-show-scrollbars = dialog-display-show-scrollbars
;    check-boxShowScrollBars.setChecked(preview.display-show-scrollbars)
;    #connect(check-boxShowScrollBars, SIGNAL(-state-changed(int)), this, SLOT(check-boxShowScrollBars-state-changed(int)))

;    labelScrollBarWidget = tk.Label(translate("Perform action when clicking corner widget"), groupBoxScrollBars)
;    combo-boxScrollBarWidget = tk.combo-box(groupBoxScrollBars)
;    dialog-display-scrollbar-widget-num = display-scrollbar-widget-num
;    numActions = actionHash.size()
;    for i in range(numActions)
;        action = actionHash.value(i)
;        if action:
;            combo-boxScrollBarWidget.add-item(action.icon(), action.text().replace("&", ""))

;    combo-boxScrollBarWidget.setCurrentIndex(dialog-display-scrollbar-widget-num)
;    #connect(combo-boxScrollBarWidget, SIGNAL(current-index-changed(int)), this, SLOT(combo-boxScrollBarWidgetCurrent-index-changed(int)))

;    vboxLayoutScrollBars = tk.VBoxLayout(groupBoxScrollBars)
;    vboxLayoutScrollBars.add-widget(check-boxShowScrollBars)
;    vboxLayoutScrollBars.add-widget(labelScrollBarWidget)
;    vboxLayoutScrollBars.add-widget(combo-boxScrollBarWidget)
;    groupBoxScrollBars.setLayout(vboxLayoutScrollBars)

;    #Colors
;    groupBoxColor = tk.GroupBox(translate("Colors"), widget)

;    labelCrossHairColor = tk.Label(translate("Crosshair Color"), groupBoxColor)
;    buttonCrossHairColor = PushButton(translate("Choose"), groupBoxColor)
;    dialog-display-crosshair-color = display-crosshair-color
;    preview.display-crosshair-color = dialog-display-crosshair-color
;    accept.display-crosshair-color = dialog-display-crosshair-color
;    crosshairPix = (16,16)
;    crosshairPix.fill(Color(preview.display-crosshair-color))
;    buttonCrossHairColor.setIcon(QIcon(crosshairPix))
;    #connect(buttonCrossHairColor, SIGNAL(clicked()), this, SLOT(chooseDisplayCrossHairColor()))

;    labelBGColor = tk.Label(translate("Background Color"), groupBoxColor)
;    buttonBGColor = PushButton(translate("Choose"), groupBoxColor)
;    dialog-display-bg-color = display-bg-color
;    preview.display-bg-color = dialog-display-bg-color
;    accept.display-bg-color = dialog-display-bg-color
;    bgPix = Image(16,16)
;    bgPix.fill(Color(preview.display-bg-color))
;    buttonBGColor.setIcon(QIcon(bgPix))
;    #connect(buttonBGColor, SIGNAL(clicked()), this, SLOT(chooseDisplayBackgroundColor()))

;    labelSelectBoxLeftColor = tk.Label(translate("Selection Box Color (Crossing)"), groupBoxColor)
;    buttonSelectBoxLeftColor = PushButton(translate("Choose"), groupBoxColor)
;    dialog-display-selectbox-left-color = display-selectbox-left-color
;    preview["display-selectbox-left-color = dialog-display-selectbox-left-color
;    accept["display-selectbox-left-color = dialog-display-selectbox-left-color
;    sBoxLCPix = Image(16,16)
;    sBoxLCPix.fill(Color(preview["display-selectbox-left-color))
;    buttonSelectBoxLeftColor.setIcon(QIcon(sBoxLCPix))
;    #connect(buttonSelectBoxLeftColor, SIGNAL(clicked()), this, SLOT(chooseDisplaySelectBoxLeftColor()))

;    labelSelectBoxLeftFill = tk.Label(translate("Selection Box Fill (Crossing)"), groupBoxColor)
;    buttonSelectBoxLeftFill = PushButton(translate("Choose"), groupBoxColor)
;    dialog-display-selectbox-left-fill = display-selectbox-left-fill
;    preview["display-selectbox-left-fill = dialog-display-selectbox-left-fill
;    accept["display-selectbox-left-fill = dialog-display-selectbox-left-fill
;    sBoxLFPix = Image(16,16)
;    sBoxLFPix.fill(Color(preview["display-selectbox-left-fill))
;    buttonSelectBoxLeftFill.setIcon(QIcon(sBoxLFPix))
;    #connect(buttonSelectBoxLeftFill, SIGNAL(clicked()), this, SLOT(chooseDisplaySelectBoxLeftFill()))

;    labelSelectBoxRightColor = tk.Label(translate("Selection Box Color (Window)"), groupBoxColor)
;    buttonSelectBoxRightColor = tk.PushButton(translate("Choose"), groupBoxColor)
;    dialog-display-selectbox-right-color = display-selectbox-right-color
;    preview["display-selectbox-right-color = dialog-display-selectbox-right-color
;    accept["display-selectbox-right-color = dialog-display-selectbox-right-color
;    sBoxRCPix = Image(16,16)
;    sBoxRCPix.fill(Color(preview["display-selectbox-right-color))
;    buttonSelectBoxRightColor.setIcon(QIcon(sBoxRCPix))
;    #connect(buttonSelectBoxRightColor, SIGNAL(clicked()), this, SLOT(chooseDisplaySelectBoxRightColor()))

;    labelSelectBoxRightFill = tk.Label(translate("Selection Box Fill (Window)"), groupBoxColor)
;    buttonSelectBoxRightFill = PushButton(translate("Choose"), groupBoxColor)
;    dialog-display-selectbox-right-fill = display-selectbox-right-fill
;    preview.display-selectbox-right-fill = dialog-display-selectbox-right-fill
;    accept.display-selectbox-right-fill = dialog-display-selectbox-right-fill
;    sBoxRFPix = Image(16,16)
;    sBoxRFPix.fill(Color(preview.display-selectbox-right-fill))
;    buttonSelectBoxRightFill.setIcon(QIcon(sBoxRFPix))
;    #connect(buttonSelectBoxRightFill, SIGNAL(clicked()), this, SLOT(chooseDisplaySelectBoxRightFill()))

;    labelSelectBoxAlpha = tk.Label(translate("Selection Box Fill Alpha"), groupBoxColor)
;    spin-boxSelectBoxAlpha = tk.spin-box(groupBoxColor)
;    spin-boxSelectBoxAlpha.setRange(0, 255)
;    dialog-display-selectbox-alpha = display-selectbox-alpha
;    preview.display-selectbox-alpha = dialog-display-selectbox-alpha
;    spin-boxSelectBoxAlpha.setValue(preview.display-selectbox-alpha)
;    #connect(spin-boxSelectBoxAlpha, SIGNAL(-value-changed(int)), this, SLOT(spin-boxDisplaySelectBoxAlpha-value-changed(int)))

;    gridLayoutColor = tk.GridLayout(widget)
;    gridLayoutColor.add-widget(labelCrossHairColor, 0, 0, "Align Left")
;    gridLayoutColor.add-widget(buttonCrossHairColor, 0, 1, "Align Right")
;    gridLayoutColor.add-widget(labelBGColor, 1, 0, "Align Left")
;    gridLayoutColor.add-widget(buttonBGColor, 1, 1, "Align Right")
;    gridLayoutColor.add-widget(labelSelectBoxLeftColor, 2, 0, "Align Left")
;    gridLayoutColor.add-widget(buttonSelectBoxLeftColor, 2, 1, "Align Right")
;    gridLayoutColor.add-widget(labelSelectBoxLeftFill, 3, 0, "Align Left")
;    gridLayoutColor.add-widget(buttonSelectBoxLeftFill, 3, 1, "Align Right")
;    gridLayoutColor.add-widget(labelSelectBoxRightColor, 4, 0, "Align Left")
;    gridLayoutColor.add-widget(buttonSelectBoxRightColor, 4, 1, "Align Right")
;    gridLayoutColor.add-widget(labelSelectBoxRightFill, 5, 0, "Align Left")
;    gridLayoutColor.add-widget(buttonSelectBoxRightFill, 5, 1, "Align Right")
;    gridLayoutColor.add-widget(labelSelectBoxAlpha, 6, 0, "Align Left")
;    gridLayoutColor.add-widget(spin-boxSelectBoxAlpha, 6, 1, "Align Right")
;    groupBoxColor.setLayout(gridLayoutColor)

;    #Zoom
;    groupBoxZoom = tk.GroupBox(translate("Zoom"), widget)

;    labelzoom-scale-actionIn = tk.Label(translate("Zoom In Scale"), groupBoxZoom)
;    spin-boxzoom-scale-actionIn = tk.Doublespin-box(groupBoxZoom)
;    dialog-display-zoom-scale-action-in = display-zoom-scale-action-in
;    spin-boxzoom-scale-actionIn.setValue(dialog-display-zoom-scale-action-in)
;    spin-boxzoom-scale-actionIn.setSingleStep(0.01)
;    spin-boxzoom-scale-actionIn.setRange(1.01, 10.00)
;    #connect(spin-boxzoom-scale-actionIn, SIGNAL(-value-changed(double)), this, SLOT(spin-boxzoom-scale-actionIn-value-changed(double)))

;    labelzoom-scale-actionOut = tk.Label(translate("Zoom Out Scale"), groupBoxZoom)
;    spin-boxzoom-scale-actionOut = tk.Doublespin-box(groupBoxZoom)
;    dialog-display-zoom-scale-action-out = display-zoom-scale-action-out
;    spin-boxzoom-scale-actionOut.setValue(dialog-display-zoom-scale-action-out)
;    spin-boxzoom-scale-actionOut.setSingleStep(0.01)
;    spin-boxzoom-scale-actionOut.setRange(0.01, 0.99)
;    #connect(spin-boxzoom-scale-actionOut, SIGNAL(-value-changed(double)), this, SLOT(spin-boxzoom-scale-actionOut-value-changed(double)))

;    gridLayoutZoom = tk.GridLayout(groupBoxZoom)
;    gridLayoutZoom.add-widget(labelzoom-scale-actionIn, 0, 0, "Align Left")
;    gridLayoutZoom.add-widget(spin-boxzoom-scale-actionIn, 0, 1, "Align Right")
;    gridLayoutZoom.add-widget(labelzoom-scale-actionOut, 1, 0, "Align Left")
;    gridLayoutZoom.add-widget(spin-boxzoom-scale-actionOut, 1, 1, "Align Right")
;    groupBoxZoom.setLayout(gridLayoutZoom)

;    #Widget Layout
;    vbox-layout-main = tk.VBoxLayout(widget)
;    #vbox-layout-main.add-widget(groupBoxRender)
;    # TODO: Review OpenGL and Rendering settings for future inclusion
;    vbox-layout-main.add-widget(groupBoxScrollBars)
;    vbox-layout-main.add-widget(groupBoxColor)
;    vbox-layout-main.add-widget(groupBoxZoom)
;    vbox-layout-main.addStretch(1)
;    widget.setLayout(vbox-layout-main)

;    scroll-area = tk.scroll-area(this)
;    scroll-area.setWidgetResizable(1)
;    scroll-area.setWidget(widget)
;    return scroll-area
;    */
)

;/* TODO: finish open/save options */
(define ()
;createTabOpenSave(void)
;    /*
;    widget = tk.Widget(this)

;    #Custom Filter
;    groupBoxCustomFilter = tk.GroupBox(translate("Custom Filter"), widget)
;    groupBoxCustomFilter.set-enabled(0); #TODO: Fixup custom filter

;    buttonCustomFilterSelectAll = PushButton(translate("Select All"), groupBoxCustomFilter)
;    #connect(buttonCustomFilterSelectAll, SIGNAL(clicked()), this, SLOT(buttonCustomFilterSelectAllClicked()))
;    buttonCustomFilterClearAll = PushButton("Clear All", groupBoxCustomFilter)
;    #connect(buttonCustomFilterClearAll, SIGNAL(clicked()), this, SLOT(buttonCustomFilterClearAllClicked()))
;    gridLayoutCustomFilter = tk.GridLayout(groupBoxCustomFilter)

;    for i in range(numberOfFormats)
;        c = check-box(formatTable[i].extension, groupBoxCustomFilter)
;        c.setChecked(opensave-custom-filter.contains(QString("*") + formatTable[i].extension, tk.t-CaseInsensitive))
;        #connect(c, SIGNAL(-state-changed(int)), this, SLOT(check-boxCustomFilter-state-changed(int)))
;        #connect(this, SIGNAL(buttonCustomFilterSelectAll(int)), c, SLOT(setChecked(int)))
;        #connect(this, SIGNAL(buttonCustomFilterClearAll(int)), c, SLOT(setChecked(int)))
;        gridLayoutCustomFilter.add-widget(c, i%10, i/10, "Align Left")

;    gridLayoutCustomFilter.add-widget(buttonCustomFilterSelectAll, 0, 7, "Align Left")
;    gridLayoutCustomFilter.add-widget(buttonCustomFilterClearAll, 1, 7, "Align Left")
;    gridLayoutCustomFilter.setColumnStretch(7,1)
;    groupBoxCustomFilter.setLayout(gridLayoutCustomFilter)

;    if opensave-custom-filter.contains("supported", tk.t-CaseInsensitive)
;        buttonCustomFilterSelectAllClicked()

;    # Opening
;    groupBoxOpening = tk.GroupBox(translate("File Open"), widget)

;    combo-boxOpenFormat = tk.combo-box(groupBoxOpening)

;    check-boxOpenThumbnail = tk.check-box(translate("Preview Thumbnails"), groupBoxOpening)
;    check-boxOpenThumbnail.setChecked(0)

;    # TODO: Add a button to clear the recent history.

;    labelRecentMaxFiles = tk.Label(translate("Number of recently accessed files to show"), groupBoxOpening)
;    spin-boxRecentMaxFiles = tk.spin-box(groupBoxOpening)
;    spin-boxRecentMaxFiles.setRange(0, 10)
;    dialog-opensave-recent-max-files = opensave-recent-max-files
;    spin-boxRecentMaxFiles.setValue(dialog-opensave-recent-max-files)
;    #connect(spin-boxRecentMaxFiles, SIGNAL(-value-changed(int)), this, SLOT(spin-boxRecentMaxFiles-value-changed(int)))

;    frameRecent = tk.Frame(groupBoxOpening)
;    gridLayoutRecent = tk.GridLayout(frameRecent)
;    gridLayoutRecent.add-widget(labelRecentMaxFiles, 0, 0, "AlignLeft")
;    gridLayoutRecent.add-widget(spin-boxRecentMaxFiles, 0, 1, "Align Right")
;    frameRecent.setLayout(gridLayoutRecent)

;    vboxLayoutOpening = tk.VBoxLayout(groupBoxOpening)
;    vboxLayoutOpening.add-widget(combo-boxOpenFormat)
;    vboxLayoutOpening.add-widget(check-boxOpenThumbnail)
;    vboxLayoutOpening.add-widget(frameRecent)
;    groupBoxOpening.setLayout(vboxLayoutOpening)

;    #Saving
;    groupBoxSaving = tk.GroupBox(translate("File Save"), widget)

;    combo-boxSaveFormat = tk.combo-box(groupBoxSaving)

;    check-boxSaveThumbnail = tk.check-box(translate("Save Thumbnails"), groupBoxSaving)
;    check-boxSaveThumbnail.setChecked(0)

;    check-boxAutoSave = tk.check-box(translate("AutoSave"), groupBoxSaving)
;    check-boxAutoSave.setChecked(0)

;    vboxLayoutSaving = tk.VBoxLayout(groupBoxSaving)
;    vboxLayoutSaving.add-widget(combo-boxSaveFormat)
;    vboxLayoutSaving.add-widget(check-boxSaveThumbnail)
;    vboxLayoutSaving.add-widget(check-boxAutoSave)
;    groupBoxSaving.setLayout(vboxLayoutSaving)

;    #Trimming
;    groupBoxTrim = tk.GroupBox(translate("Trimming"), widget)

;    labelTrimDstNumJumps = tk.Label(translate("DST Only: Minimum number of jumps to trim"), groupBoxTrim)
;    spin-boxTrimDstNumJumps = tk.spin-box(groupBoxTrim)
;    spin-boxTrimDstNumJumps.setRange(1, 20)
;    dialog-opensave-trim-dst-num-jumps = opensave-trim-dst-num-jumps
;    spin-boxTrimDstNumJumps.setValue(dialog-opensave-trim-dst-num-jumps)
;    #connect(spin-boxTrimDstNumJumps, SIGNAL(-value-changed(int)), this, SLOT(spin-boxTrimDstNumJumps-value-changed(int)))

;    frameTrimDstNumJumps = tk.Frame(groupBoxTrim)
;    gridLayoutTrimDstNumJumps = tk.GridLayout(frameTrimDstNumJumps)
;    gridLayoutTrimDstNumJumps.add-widget(labelTrimDstNumJumps, 0, 0, "Align Left")
;    gridLayoutTrimDstNumJumps.add-widget(spin-boxTrimDstNumJumps, 0, 1, "Align Right")
;    frameTrimDstNumJumps.setLayout(gridLayoutTrimDstNumJumps)

;    vboxLayoutTrim = tk.VBoxLayout(groupBoxTrim)
;    vboxLayoutTrim.add-widget(frameTrimDstNumJumps)
;    groupBoxTrim.setLayout(vboxLayoutTrim)

;    #Widget Layout
;    vbox-layout-main = tk.VBoxLayout(widget)
;    vbox-layout-main.add-widget(groupBoxCustomFilter)
;    vbox-layout-main.add-widget(groupBoxOpening)
;    vbox-layout-main.add-widget(groupBoxSaving)
;    vbox-layout-main.add-widget(groupBoxTrim)
;    vbox-layout-main.addStretch(1)
;    widget.setLayout(vbox-layout-main)

;    scroll-area = tk.scroll-area(this)
;    scroll-area.setWidgetResizable(1)
;    scroll-area.setWidget(widget)
;    return scroll-area
;    */
)

(define ()
;create-tab-printing(void)
;/*
;    widget = tk.Widget(this)

;    # Default Printer
;    groupBoxDefaultPrinter = tk.GroupBox(translate("Default Printer"), widget)

;    radioButtonUseSame = tk.RadioButton(translate("Use as default device"), groupBoxDefaultPrinter)
;    radioButtonUseSame.setChecked(!printing-use-last-device)
;    radioButtonUseLast = tk.RadioButton(translate("Use last used device"), groupBoxDefaultPrinter)
;    radioButtonUseLast.setChecked(printing-use-last-device)

;    combo-boxDefaultDevice = tk.combo-box(groupBoxDefaultPrinter)
;    listAvailPrinters = tk.PrinterInfo-availablePrinters()
;    for info in listAvailPrinters:
;        combo-boxDefaultDevice.add-item(load-icon(print-xpm), info.printerName())

;    vboxLayoutDefaultPrinter = tk.VBoxLayout(groupBoxDefaultPrinter)
;    vboxLayoutDefaultPrinter.add-widget(radioButtonUseSame)
;    vboxLayoutDefaultPrinter.add-widget(combo-boxDefaultDevice)
;    vboxLayoutDefaultPrinter.add-widget(radioButtonUseLast)
;    groupBoxDefaultPrinter.setLayout(vboxLayoutDefaultPrinter)

;    # Save Ink
;    groupBoxSaveInk = tk.GroupBox(translate("Save Ink"), widget)

;    check-boxDisableBG = tk.check-box(translate("Disable Background"), groupBoxSaveInk)
;    dialog-printing-disable-bg = printing-disable-bg
;    check-boxDisableBG.setChecked(dialog-printing-disable-bg)
;    #connect(check-boxDisableBG, SIGNAL(-state-changed(int)), this, SLOT(check-boxDisableBG-state-changed(int)))

;    vboxLayoutSaveInk = tk.VBoxLayout(groupBoxSaveInk)
;    vboxLayoutSaveInk.add-widget(check-boxDisableBG)
;    groupBoxSaveInk.setLayout(vboxLayoutSaveInk)

;    #Widget Layout
;    vbox-layout-main = tk.VBoxLayout(widget)
;    vbox-layout-main.add-widget(groupBoxDefaultPrinter)
;    vbox-layout-main.add-widget(groupBoxSaveInk)
;    vbox-layout-main.addStretch(1)
;    widget.setLayout(vbox-layout-main)

;    scroll-area = tk.scroll-area(this)
;    #scroll-area.setWidgetResizable(1)
;    scroll-area.setWidget(widget)
;    return scroll-area
;    */
)

(define ()
;create-tab-snap(void)
;    /*
;    widget = tk.Widget(this)

;    #TODO: finish this

;    scroll-area = tk.scroll-area(this)
;    scroll-area.setWidgetResizable(1)
;    scroll-area.setWidget(widget)
;    return scroll-area
;    */
)

(define ()
;createTabGridRuler(void)
;    create-settings-tab(grid-ruler-settings)
;    /*
;    widget = tk.Widget(this)

;    #Grid Color
;    groupBoxGridColor = tk.GroupBox(translate("Grid Color"), widget)

;    labelGridColor = tk.Label(translate("Grid Color"), groupBoxGridColor)
;    labelGridColor.setObjectName("labelGridColor")
;    buttonGridColor = PushButton(translate("Choose"), groupBoxGridColor)
;    buttonGridColor.setObjectName("buttonGridColor")
;    if dialog-grid-color-match-crosshair:
;        dialog-grid-color = display-crosshair-color
;    else {
;        dialog-grid-color = grid-color
;    preview.grid-color = dialog-grid-color
;    accept.grid-color = dialog-grid-color
;    gridPix = Image(16,16)
;    gridPix.fill(Color(preview.grid-color))
;    buttonGridColor.setIcon(QIcon(gridPix))
;    #connect(buttonGridColor, SIGNAL(clicked()), this, SLOT(chooseGridColor()))

;    labelGridColor.set-enabled(!dialog-grid-color-match-crosshair)
;    buttonGridColor.set-enabled(!dialog-grid-color-match-crosshair)

;    gridLayoutGridColor = tk.GridLayout(widget)
;    gridLayoutGridColor.add-widget(check-boxGridColorMatchCrossHair, 0, 0, "Align Left")
;    gridLayoutGridColor.add-widget(labelGridColor, 1, 0, "Align Left")
;    gridLayoutGridColor.add-widget(buttonGridColor, 1, 1, "Align Right")
;    groupBoxGridColor.setLayout(gridLayoutGridColor)

;    #Grid Geometry
;    groupBoxGridGeom = tk.GroupBox(translate("Grid Geometry"), widget)

;    check-box-grid-load-from-file = tk.check-box(translate("Set grid size from opened file"), groupBoxGridGeom)
;    dialog-grid-load-from-file = grid-load-from-file
;    check-box-grid-load-from-file.setChecked(dialog-grid-load-from-file)
;    #connect(check-box-grid-load-from-file, SIGNAL(-state-changed(int)), this, SLOT(check-box-grid-load-from-file-state-changed(int)))

;    label-grid-type = tk.Label(translate("Grid Type"), groupBoxGridGeom)
;    label-grid-type.setObjectName("label-grid-type")
;    combo-box-grid-type = tk.combo-box(groupBoxGridGeom)
;    combo-box-grid-type.setObjectName("combo-box-grid-type")
;    combo-box-grid-type.add-item("Rectangular")
;    combo-box-grid-type.add-item("Circular")
;    combo-box-grid-type.add-item("Isometric")
;    strcpy(dialog-grid-type, grid-type)
;    combo-box-grid-type.setCurrentIndex(combo-box-grid-type.findText(dialog-grid-type))
;    # #connect(combo-box-grid-type, SIGNAL(current-index-changed("")), this, SLOT(combo-box-grid-typeCurrent-index-changed("")))

;    check-box-grid-center-on-origin = tk.check-box(translate("Center the grid on the origin"), groupBoxGridGeom)
;    check-box-grid-center-on-origin.setObjectName("check-box-grid-center-on-origin")
;    dialog-grid-center-on-origin = grid-center-on-origin
;    check-box-grid-center-on-origin.setChecked(dialog-grid-center-on-origin)
;    #connect(check-box-grid-center-on-origin, SIGNAL(-state-changed(int)), this, SLOT(check-box-grid-center-on-origin-state-changed(int)))

;    label-grid-center-x = tk.Label(translate("Grid Center X"), groupBoxGridGeom)
;    label-grid-center-x.setObjectName("label-grid-center-x")
;    spin-boxGridCenterX = tk.Doublespin-box(groupBoxGridGeom)
;    spin-boxGridCenterX.setObjectName("spin-boxGridCenterX")
;    dialog-grid-center.x = grid-center.x
;    spin-boxGridCenterX.setSingleStep(1.000)
;    spin-boxGridCenterX.setRange(-1000.000, 1000.000)
;    spin-boxGridCenterX.setValue(dialog-grid-center.x)
;    #connect(spin-boxGridCenterX, SIGNAL(-value-changed(double)), this, SLOT(spin-boxGridCenterX-value-changed(double)))

;    label-grid-center-y = tk.Label(translate("Grid Center Y"), groupBoxGridGeom)
;    label-grid-center-y.setObjectName("label-grid-center-y")
;    spin-box-grid-center-y = tk.Doublespin-box(groupBoxGridGeom)
;    spin-box-grid-center-y.setObjectName("spin-box-grid-center-y")
;    dialog-grid-center.y = grid-center.y
;    spin-box-grid-center-y.setSingleStep(1.000)
;    spin-box-grid-center-y.setRange(-1000.000, 1000.000)
;    spin-box-grid-center-y.setValue(dialog-grid-center.y)
;    #connect(spin-box-grid-center-y, SIGNAL(-value-changed(double)), this, SLOT(spin-box-grid-center-y-value-changed(double)))

;    label-grid-sizeX = tk.Label(translate("Grid Size X"), groupBoxGridGeom)
;    label-grid-sizeX.setObjectName("label-grid-sizeX")
;    spin-box-grid-sizeX = tk.Doublespin-box(groupBoxGridGeom)
;    spin-box-grid-sizeX.setObjectName("spin-box-grid-sizeX")
;    dialog-grid-size.x = grid-size.x
;    spin-box-grid-sizeX.setSingleStep(1.000)
;    spin-box-grid-sizeX.setRange(1.000, 1000.000)
;    spin-box-grid-sizeX.setValue(dialog-grid-size.x)
;    #connect(spin-box-grid-sizeX, SIGNAL(-value-changed(double)), this, SLOT(spin-box-grid-sizeX-value-changed(double)))

;    label-grid-sizeY = tk.Label(translate("Grid Size Y"), groupBoxGridGeom)
;    label-grid-sizeY.setObjectName("label-grid-sizeY")
;    spin-box-grid-sizeY = tk.Doublespin-box(groupBoxGridGeom)
;    spin-box-grid-sizeY.setObjectName("spin-box-grid-sizeY")
;    dialog-grid-size.y = grid-size.y
;    spin-box-grid-sizeY.setSingleStep(1.000)
;    spin-box-grid-sizeY.setRange(1.000, 1000.000)
;    spin-box-grid-sizeY.setValue(dialog-grid-size.y)
;    #connect(spin-box-grid-sizeY, SIGNAL(-value-changed(double)), this, SLOT(spin-box-grid-sizeY-value-changed(double)))

;    labelGridSpacingX = tk.Label(translate("Grid Spacing X"), groupBoxGridGeom)
;    labelGridSpacingX.setObjectName("labelGridSpacingX")
;    spin-boxGridSpacingX = tk.Doublespin-box(groupBoxGridGeom)
;    spin-boxGridSpacingX.setObjectName("spin-boxGridSpacingX")
;    dialog-grid-spacing.x = grid-spacing.x
;    spin-boxGridSpacingX.setSingleStep(1.000)
;    spin-boxGridSpacingX.setRange(0.001, 1000.000)
;    spin-boxGridSpacingX.setValue(dialog-grid-spacing.x)
;    #connect(spin-boxGridSpacingX, SIGNAL(-value-changed(double)), this, SLOT(spin-boxGridSpacingX-value-changed(double)))

;    labelGridSpacingY = tk.Label(translate("Grid Spacing Y"), groupBoxGridGeom)
;    labelGridSpacingY.setObjectName("labelGridSpacingY")
;    spin-boxGridSpacingY = tk.Doublespin-box(groupBoxGridGeom)
;    spin-boxGridSpacingY.setObjectName("spin-boxGridSpacingY")
;    dialog-grid-spacing.y = grid-spacing.y
;    spin-boxGridSpacingY.setSingleStep(1.000)
;    spin-boxGridSpacingY.setRange(0.001, 1000.000)
;    spin-boxGridSpacingY.setValue(dialog-grid-spacing.y)
;    #connect(spin-boxGridSpacingY, SIGNAL(-value-changed(double)), this, SLOT(spin-boxGridSpacingY-value-changed(double)))

;    label-grid-sizeRadius = tk.Label(translate("Grid Size Radius"), groupBoxGridGeom)
;    label-grid-sizeRadius.setObjectName("label-grid-sizeRadius")
;    spin-box-grid-sizeRadius = tk.Doublespin-box(groupBoxGridGeom)
;    spin-box-grid-sizeRadius.setObjectName("spin-box-grid-sizeRadius")
;    dialog-grid-size-radius = grid-size-radius
;    spin-box-grid-sizeRadius.setSingleStep(1.000)
;    spin-box-grid-sizeRadius.setRange(1.000, 1000.000)
;    spin-box-grid-sizeRadius.setValue(dialog-grid-size-radius)
;    #connect(spin-box-grid-sizeRadius, SIGNAL(-value-changed(double)), this, SLOT(spin-box-grid-sizeRadius-value-changed(double)))

;    labelGridSpacingRadius = tk.Label(translate("Grid Spacing Radius"), groupBoxGridGeom)
;    labelGridSpacingRadius.setObjectName("labelGridSpacingRadius")
;    spin-boxGridSpacingRadius = tk.Doublespin-box(groupBoxGridGeom)
;    spin-boxGridSpacingRadius.setObjectName("spin-boxGridSpacingRadius")
;    dialog-grid-spacing-radius = grid-spacing-radius
;    spin-boxGridSpacingRadius.setSingleStep(1.000)
;    spin-boxGridSpacingRadius.setRange(0.001, 1000.000)
;    spin-boxGridSpacingRadius.setValue(dialog-grid-spacing-radius)
;    #connect(spin-boxGridSpacingRadius, SIGNAL(-value-changed(double)), this, SLOT(spin-boxGridSpacingRadius-value-changed(double)))

;    labelGridSpacingAngle = tk.Label(translate("Grid Spacing Angle"), groupBoxGridGeom)
;    labelGridSpacingAngle.setObjectName("labelGridSpacingAngle")
;    spin-boxGridSpacingAngle = tk.Doublespin-box(groupBoxGridGeom)
;    spin-boxGridSpacingAngle.setObjectName("spin-boxGridSpacingAngle")
;    dialog-grid-spacing-angle = grid-spacing-angle
;    spin-boxGridSpacingAngle.setSingleStep(1.000)
;    spin-boxGridSpacingAngle.setRange(0.001, 1000.000)
;    spin-boxGridSpacingAngle.setValue(dialog-grid-spacing-angle)
;    #connect(spin-boxGridSpacingAngle, SIGNAL(-value-changed(double)), this, SLOT(spin-boxGridSpacingAngle-value-changed(double)))

;    label-grid-type.set-enabled(!dialog-grid-load-from-file)
;    combo-box-grid-type.set-enabled(!dialog-grid-load-from-file)
;    check-box-grid-center-on-origin.set-enabled(!dialog-grid-load-from-file)
;    label-grid-center-x.set-enabled(!dialog-grid-load-from-file)
;    spin-boxGridCenterX.set-enabled(!dialog-grid-load-from-file)
;    label-grid-center-y.set-enabled(!dialog-grid-load-from-file)
;    spin-box-grid-center-y.set-enabled(!dialog-grid-load-from-file)
;    label-grid-sizeX.set-enabled(!dialog-grid-load-from-file)
;    spin-box-grid-sizeX.set-enabled(!dialog-grid-load-from-file)
;    label-grid-sizeY.set-enabled(!dialog-grid-load-from-file)
;    spin-box-grid-sizeY.set-enabled(!dialog-grid-load-from-file)
;    labelGridSpacingX.set-enabled(!dialog-grid-load-from-file)
;    spin-boxGridSpacingX.set-enabled(!dialog-grid-load-from-file)
;    labelGridSpacingY.set-enabled(!dialog-grid-load-from-file)
;    spin-boxGridSpacingY.set-enabled(!dialog-grid-load-from-file)
;    label-grid-sizeRadius.set-enabled(!dialog-grid-load-from-file)
;    spin-box-grid-sizeRadius.set-enabled(!dialog-grid-load-from-file)
;    labelGridSpacingRadius.set-enabled(!dialog-grid-load-from-file)
;    spin-boxGridSpacingRadius.set-enabled(!dialog-grid-load-from-file)
;    labelGridSpacingAngle.set-enabled(!dialog-grid-load-from-file)
;    spin-boxGridSpacingAngle.set-enabled(!dialog-grid-load-from-file)

;    visibility = 0
;    if dialog-grid-type == "Circular":
;        visibility = 1
;    label-grid-sizeX.set-visible(!visibility)
;    spin-box-grid-sizeX.set-visible(!visibility)
;    label-grid-sizeY.set-visible(!visibility)
;    spin-box-grid-sizeY.set-visible(!visibility)
;    labelGridSpacingX.set-visible(!visibility)
;    spin-boxGridSpacingX.set-visible(!visibility)
;    labelGridSpacingY.set-visible(!visibility)
;    spin-boxGridSpacingY.set-visible(!visibility)
;    label-grid-sizeRadius.set-visible(visibility)
;    spin-box-grid-sizeRadius.set-visible(visibility)
;    labelGridSpacingRadius.set-visible(visibility)
;    spin-boxGridSpacingRadius.set-visible(visibility)
;    labelGridSpacingAngle.set-visible(visibility)
;    spin-boxGridSpacingAngle.set-visible(visibility)

;    gridLayoutGridGeom = tk.GridLayout(groupBoxGridGeom)
;    gridLayoutGridGeom.add-widget(check-box-grid-load-from-file, 0, 0, "Align Left")
;    gridLayoutGridGeom.add-widget(label-grid-type, 1, 0, "Align Left")
;    gridLayoutGridGeom.add-widget(combo-box-grid-type, 1, 1, "Align Right")
;    gridLayoutGridGeom.add-widget(check-box-grid-center-on-origin, 2, 0, "Align Left")
;    gridLayoutGridGeom.add-widget(label-grid-center-x, 3, 0, "Align Left")
;    gridLayoutGridGeom.add-widget(spin-boxGridCenterX, 3, 1, "Align Right")
;    gridLayoutGridGeom.add-widget(label-grid-center-y, 4, 0, "Align Left")
;    gridLayoutGridGeom.add-widget(spin-box-grid-center-y, 4, 1, "Align Right")
;    gridLayoutGridGeom.add-widget(label-grid-sizeX, 5, 0, "Align Left")
;    gridLayoutGridGeom.add-widget(spin-box-grid-sizeX, 5, 1, "Align Right")
;    gridLayoutGridGeom.add-widget(label-grid-sizeY, 6, 0, "Align Left")
;    gridLayoutGridGeom.add-widget(spin-box-grid-sizeY, 6, 1, "Align Right")
;    gridLayoutGridGeom.add-widget(labelGridSpacingX, 7, 0, "Align Left")
;    gridLayoutGridGeom.add-widget(spin-boxGridSpacingX, 7, 1, "Align Right")
;    gridLayoutGridGeom.add-widget(labelGridSpacingY, 8, 0, "Align Left")
;    gridLayoutGridGeom.add-widget(spin-boxGridSpacingY, 8, 1, "Align Right")
;    gridLayoutGridGeom.add-widget(label-grid-sizeRadius, 9, 0, "Align Left")
;    gridLayoutGridGeom.add-widget(spin-box-grid-sizeRadius, 9, 1, "Align Right")
;    gridLayoutGridGeom.add-widget(labelGridSpacingRadius, 10, 0, "Align Left")
;    gridLayoutGridGeom.add-widget(spin-boxGridSpacingRadius, 10, 1, "Align Right")
;    gridLayoutGridGeom.add-widget(labelGridSpacingAngle, 11, 0, "Align Left")
;    gridLayoutGridGeom.add-widget(spin-boxGridSpacingAngle, 11, 1, "Align Right")
;    groupBoxGridGeom.setLayout(gridLayoutGridGeom)

;    #Ruler Misc
;    groupBoxRulerMisc = tk.GroupBox(translate("Ruler Misc"), widget)

;    check-boxRulerShowOnLoad = tk.check-box(translate("Initially show ruler when loading a file"), groupBoxRulerMisc)
;    dialog-ruler-show-on-load = ruler-show-on-load
;    check-boxRulerShowOnLoad.setChecked(dialog-ruler-show-on-load)
;    #connect(check-boxRulerShowOnLoad, SIGNAL(-state-changed(int)), this, SLOT(check-boxRulerShowOnLoad-state-changed(int)))

;    labelRulerMetric = tk.Label(translate("Ruler Units"), groupBoxRulerMisc)
;    combo-boxRulerMetric = tk.combo-box(groupBoxRulerMisc)
;    combo-boxRulerMetric.add-item("Imperial", 0)
;    combo-boxRulerMetric.add-item("Metric", 1)
;    dialog-ruler-metric = ruler-metric
;    combo-boxRulerMetric.setCurrentIndex(combo-boxRulerMetric.findData(dialog-ruler-metric))
;    #connect(combo-boxRulerMetric, SIGNAL(current-index-changed(int)), this, SLOT(combo-boxRulerMetricCurrent-index-changed(int)))

;    gridLayoutRulerMisc = tk.GridLayout(widget)
;    gridLayoutRulerMisc.add-widget(check-boxRulerShowOnLoad, 0, 0, "Align Left")
;    gridLayoutRulerMisc.add-widget(labelRulerMetric, 1, 0, "Align Left")
;    gridLayoutRulerMisc.add-widget(combo-boxRulerMetric, 1, 1, "Align Right")
;    groupBoxRulerMisc.setLayout(gridLayoutRulerMisc)

;    #Ruler Color
;    groupBoxRulerColor = tk.GroupBox(translate("Ruler Color"), widget)

;    labelRulerColor = tk.Label(translate("Ruler Color"), groupBoxRulerColor)
;    labelRulerColor.setObjectName("labelRulerColor")
;    buttonRulerColor = PushButton(translate("Choose"), groupBoxRulerColor)
;    buttonRulerColor.setObjectName("buttonRulerColor")
;    dialog-ruler-color = ruler-color
;    preview.ruler-color = dialog-ruler-color
;    accept.ruler-color = dialog-ruler-color
;    rulerPix = Image(16,16)
;    rulerPix.fill(Color(preview.ruler-color))
;    buttonRulerColor.setIcon(QIcon(rulerPix))
;    #connect(buttonRulerColor, SIGNAL(clicked()), this, SLOT(chooseRulerColor()))

;    gridLayoutRulerColor = tk.GridLayout(widget)
;    gridLayoutRulerColor.add-widget(labelRulerColor, 1, 0, "Align Left")
;    gridLayoutRulerColor.add-widget(buttonRulerColor, 1, 1, "Align Right")
;    groupBoxRulerColor.setLayout(gridLayoutRulerColor)

;    #Ruler Geometry
;    groupBoxRulerGeom = tk.GroupBox(translate("Ruler Geometry"), widget)

;    labelRulerPixelSize = tk.Label(translate("Ruler Pixel Size"), groupBoxRulerGeom)
;    labelRulerPixelSize.setObjectName("labelRulerPixelSize")
;    spin-boxRulerPixelSize = tk.Doublespin-box(groupBoxRulerGeom)
;    spin-boxRulerPixelSize.setObjectName("spin-boxRulerPixelSize")
;    dialog-ruler-pixel-size = ruler-pixel-size
;    spin-boxRulerPixelSize.setSingleStep(1.000)
;    spin-boxRulerPixelSize.setRange(20.000, 100.000)
;    spin-boxRulerPixelSize.setValue(dialog-ruler-pixel-size)
;    #connect(spin-boxRulerPixelSize, SIGNAL(-value-changed(double)), this, SLOT(spin-boxRulerPixelSize-value-changed(double)))

;    gridLayoutRulerGeom = tk.GridLayout(groupBoxRulerGeom)
;    gridLayoutRulerGeom.add-widget(labelRulerPixelSize, 0, 0, "Align Left")
;    gridLayoutRulerGeom.add-widget(spin-boxRulerPixelSize, 0, 1, "Align Right")
;    groupBoxRulerGeom.setLayout(gridLayoutRulerGeom)

;    #Widget Layout
;    vbox-layout-main = tk.VBoxLayout(widget)
;    vbox-layout-main.add-widget(groupBoxGridMisc)
;    vbox-layout-main.add-widget(groupBoxGridColor)
;    vbox-layout-main.add-widget(groupBoxGridGeom)
;    vbox-layout-main.add-widget(groupBoxRulerMisc)
;    vbox-layout-main.add-widget(groupBoxRulerColor)
;    vbox-layout-main.add-widget(groupBoxRulerGeom)
;    vbox-layout-main.addStretch(1)
;    widget.setLayout(vbox-layout-main)

;    scroll-area = tk.scroll-area(this)
;    scroll-area.setWidgetResizable(1)
;    scroll-area.setWidget(widget)
;    return scroll-area*/
)

(define ()
;createTabOrthoPolar()
;/*
;    widget = tk.Widget(this)

;    #TODO: finish this

;    scroll-area = tk.scroll-area(this)
;    scroll-area.setWidgetResizable(1)
;    scroll-area.setWidget(widget)
;    return scroll-area
;    */
)

;/* Originally a macro for constructing tk.t check-boxes.
; */
;/*static void
;make-check-box(label, checked, icon, f, x, y)

;    c = tk.check-box(translate(label), groupBoxQSnapLoc)
;    c.setChecked(checked)
;    c.setIcon(load-icon(icon))
;    #connect(c, SIGNAL(-state-changed(int)), this, SLOT(f(int)))
;    #connect(this, SIGNAL(buttonQSnapSelectAll(int)), c, SLOT(setChecked(int)))
;    #connect(this, SIGNAL(buttonQSnapClearAll(int)), c, SLOT(setChecked(int)))
;    gridLayoutQSnap.add-widget(c, x, y, "Align Left")
;    dialog-checked = checked
)

(define ()
;createTabQuickSnap()
;    widget = tk.Widget(this)

;    #QSnap Locators
;    groupBoxQSnapLoc = tk.GroupBox(translate("Locators Used"), widget)
;    buttonQSnapSelectAll = PushButton(translate("Select All"), groupBoxQSnapLoc)
;    buttonQSnapClearAll = PushButton(translate("Clear All"), groupBoxQSnapLoc)
;    gridLayoutQSnap = tk.GridLayout(groupBoxQSnapLoc)

;    #connect(buttonQSnapSelectAll, SIGNAL(clicked()), this, SLOT(buttonQSnapSelectAllClicked()))
;    #connect(buttonQSnapClearAll, SIGNAL(clicked()), this, SLOT(buttonQSnapClearAllClicked()))

;    make-check-box("Endpoint", tk.snap-endpoint, locator-snaptoendpoint-xpm, check-boxQSnapEndPoint-state-changed, 0, 0)
;    make-check-box("Midpoint", tk.snap-midpoint, locator-snaptomidpoint-xpm, check-boxQSnapMidPoint-state-changed, 1, 0)
;    make-check-box("Center", tk.snap-center, locator-snaptocenter-xpm, check-boxQSnapCenter-state-changed, 2, 0)
;    make-check-box("Node", tk.snap-node, locator-snaptonode-xpm, check-boxQSnapNode-state-changed, 3, 0)
;    make-check-box("Quadrant", tk.snap-quadrant, locator-snaptoquadrant-xpm, check-boxQSnapQuadrant-state-changed, 4, 0)
;    make-check-box("Intersection", tk.snap-intersection, locator-snaptointersection-xpm, check-boxQSnapIntersection-state-changed, 5, 0)
;    make-check-box("Extension", tk.snap-extension, locator-snaptoextension-xpm, check-boxQSnapExtension-state-changed, 6, 0)
;    make-check-box("Insertion", tk.snap-insertion, locator-snaptoinsert-xpm, check-boxQSnapInsertion-state-changed, 0, 1)
;    make-check-box("Perpendicular", tk.snap-perpendicular, locator-snaptoperpendicular-xpm, check-boxQSnapPerpendicular-state-changed, 1, 1)
;    make-check-box("Tangent", tk.snap-tangent, locator-snaptotangent-xpm, check-boxQSnapTangent-state-changed, 2, 1)
;    make-check-box("Nearest", tk.snap-nearest, locator-snaptonearest-xpm, check-boxQSnapNearest-state-changed, 3, 1)
;    make-check-box("Apparent Intersection", tk.snap-apparent, locator-snaptoapparentintersection-xpm, check-boxQSnapApparentIntersection-state-changed, 4, 1)
;    make-check-box("Parallel", tk.snap-parallel, locator-snaptoparallel-xpm, check-boxQSnapParallel-state-changed, 5, 1)

;    gridLayoutQSnap.add-widget(buttonQSnapSelectAll, 0, 2, "Align Left")
;    gridLayoutQSnap.add-widget(buttonQSnapClearAll, 1, 2, "Align Left")
;    gridLayoutQSnap.setColumnStretch(2,1)
;    groupBoxQSnapLoc.setLayout(gridLayoutQSnap)

;    #QSnap Visual Config
;    groupBoxQSnapVisual = tk.GroupBox(translate("Visual Configuration"), widget)

;    labelQSnapLocColor = tk.Label(translate("Locator Color"), groupBoxQSnapVisual)
;    combo-boxQSnapLocColor = tk.combo-box(groupBoxQSnapVisual)
;    addColorsTocombo-box(combo-boxQSnapLocColor)
;    dialog-qsnap-locator-color = qsnap-locator-color
;    combo-boxQSnapLocColor.setCurrentIndex(combo-boxQSnapLocColor.findData(dialog-qsnap-locator-color))
;    #connect(combo-boxQSnapLocColor, SIGNAL(current-index-changed(int)), this, SLOT(combo-boxQSnapLocatorColorCurrent-index-changed(int)))

;    labelQSnapLocSize = tk.Label(translate("Locator Size"), groupBoxQSnapVisual)
;    sliderQSnapLocSize = tk.Slider(Qt-Horizontal, groupBoxQSnapVisual)
;    sliderQSnapLocSize.setRange(1,20)
;    dialog-qsnap-locator-size = qsnap-locator-size
;    sliderQSnapLocSize.setValue(dialog-qsnap-locator-size)
;    #connect(sliderQSnapLocSize, SIGNAL(-value-changed(int)), this, SLOT(sliderQSnapLocatorSize-value-changed(int)))

;    vboxLayoutQSnapVisual = tk.VBoxLayout(groupBoxQSnapVisual)
;    vboxLayoutQSnapVisual.add-widget(labelQSnapLocColor)
;    vboxLayoutQSnapVisual.add-widget(combo-boxQSnapLocColor)
;    vboxLayoutQSnapVisual.add-widget(labelQSnapLocSize)
;    vboxLayoutQSnapVisual.add-widget(sliderQSnapLocSize)
;    groupBoxQSnapVisual.setLayout(vboxLayoutQSnapVisual)

;    #QSnap Sensitivity Config
;    groupBoxQSnapSensitivity = tk.GroupBox(translate("Sensitivity"), widget)

;    labelQSnapApertureSize = tk.Label(translate("Aperture Size"), groupBoxQSnapSensitivity)
;    sliderQSnapApertureSize = tk.Slider(Qt-Horizontal, groupBoxQSnapSensitivity)
;    sliderQSnapApertureSize.setRange(1,20)
;    dialog-qsnap-aperture-size = qsnap-aperture-size
;    sliderQSnapApertureSize.setValue(dialog-qsnap-aperture-size)
;    #connect(sliderQSnapApertureSize, SIGNAL(-value-changed(int)), this, SLOT(sliderQSnapApertureSize-value-changed(int)))

;    vboxLayoutQSnapSensitivity = tk.VBoxLayout(groupBoxQSnapSensitivity)
;    vboxLayoutQSnapSensitivity.add-widget(labelQSnapApertureSize)
;    vboxLayoutQSnapSensitivity.add-widget(sliderQSnapApertureSize)
;    groupBoxQSnapSensitivity.setLayout(vboxLayoutQSnapSensitivity)

;    #Widget Layout
;    vbox-layout-main = tk.VBoxLayout(widget)
;    vbox-layout-main.add-widget(groupBoxQSnapLoc)
;    vbox-layout-main.add-widget(groupBoxQSnapVisual)
;    vbox-layout-main.add-widget(groupBoxQSnapSensitivity)
;    vbox-layout-main.addStretch(1)
;    widget.setLayout(vbox-layout-main)

;    scroll-area = tk.scroll-area(this)
;    scroll-area.setWidgetResizable(1)
;    scroll-area.setWidget(widget)
;    return scroll-area
)*/

(define ()
;createTabQuickTrack()
;/*
;    widget = tk.Widget(this)

;    # TODO: finish this

;    scroll-area = tk.scroll-area(this)
;    scroll-area.setWidgetResizable(1)
;    scroll-area.setWidget(widget)
;    return scroll-area
;    */
)
 /*
(define ()
;createTabLineWeight()
;    widget = tk.Widget(this)

;    # TODO: finish this

;    # Misc
;    groupBoxLwtMisc = tk.GroupBox(translate("LineWeight Misc"), widget)

;    s = activeScene()

;    check-boxShowLwt = tk.check-box(translate("Show LineWeight"), groupBoxLwtMisc)
;    if s:
;        dialog-lwt-show-lwt = s.property("ENABLE-LWT")
;    else {
;        dialog-lwt-show-lwt = lwt-show-lwt

;    preview.lwt-show-lwt = dialog-lwt-show-lwt
;    check-boxShowLwt.setChecked(preview.lwt-show-lwt)
;    #connect(check-boxShowLwt, SIGNAL(-state-changed(int)), this, SLOT(check-boxLwtShowLwt-state-changed(int)))

;    check-boxRealRender = tk.check-box(translate("RealRender"), groupBoxLwtMisc)
;    check-boxRealRender.setObjectName("check-boxRealRender")
;    if s:
;        dialog-lwt-real-render = s.property("ENABLE-REAL")
;    else {
;        dialog-lwt-real-render = lwt-real-render

;    preview.lwt-real-render = dialog-lwt-real-render
;    check-boxRealRender.setChecked(preview.lwt-real-render)
;    #connect(check-boxRealRender, SIGNAL(-state-changed(int)), this, SLOT(check-boxLwtRealRender-state-changed(int)))
;    check-boxRealRender.set-enabled(dialog-lwt-show-lwt)

;    labelDefaultLwt = tk.Label(translate("Default weight"), groupBoxLwtMisc)
;    labelDefaultLwt.set-enabled(0); # TODO: remove later
;    combo-boxDefaultLwt = tk.combo-box(groupBoxLwtMisc)
;    dialog-lwt-default-lwt = lwt-default-lwt
;    # TODO: populate the combo-box and set the initial value
;    combo-boxDefaultLwt.add-item("".setNum(dialog-lwt-default-lwt, 'F', 2).append(" mm"), dialog-lwt-default-lwt)
;    combo-boxDefaultLwt.set-enabled(0); # TODO: remove later

;    vboxLayoutLwtMisc = tk.VBoxLayout(groupBoxLwtMisc)
;    vboxLayoutLwtMisc.add-widget(check-boxShowLwt)
;    vboxLayoutLwtMisc.add-widget(check-boxRealRender)
;    vboxLayoutLwtMisc.add-widget(labelDefaultLwt)
;    vboxLayoutLwtMisc.add-widget(combo-boxDefaultLwt)
;    groupBoxLwtMisc.setLayout(vboxLayoutLwtMisc)

;    #Widget Layout
;    vbox-layout-main = tk.VBoxLayout(widget)
;    vbox-layout-main.add-widget(groupBoxLwtMisc)
;    vbox-layout-main.addStretch(1)
;    widget.setLayout(vbox-layout-main)

;    scroll-area = tk.scroll-area(this)
;    scroll-area.setWidgetResizable(1)
;    scroll-area.setWidget(widget)
;    return scroll-area
)
;*/

(define ()
;createTabSelection(void)
;/*
;    widget = tk.Widget(this)

;    # Selection Modes
;    groupBoxSelectionModes = tk.GroupBox(translate("Modes"), widget)

;    check-boxSelectionModePickFirst = tk.check-box(translate("Allow Preselection (PickFirst)"), groupBoxSelectionModes)
;    dialog-selection-mode-pickfirst = selection-mode-pickfirst
;    check-boxSelectionModePickFirst.setChecked(dialog-selection-mode-pickfirst)
;    check-boxSelectionModePickFirst.setChecked(1); check-boxSelectionModePickFirst.set-enabled(0); # TODO: Remove this line when Post-selection is available
;    #connect(check-boxSelectionModePickFirst, SIGNAL(-state-changed(int)), this, SLOT(check-boxSelectionModePickFirst-state-changed(int)))

;    check-boxSelectionModePickAdd = tk.check-box(translate("Add to Selection (PickAdd)"), groupBoxSelectionModes)
;    dialog-selection-mode-pickadd = selection-mode-pickadd
;    check-boxSelectionModePickAdd.setChecked(dialog-selection-mode-pickadd)
;    #connect(check-boxSelectionModePickAdd, SIGNAL(-state-changed(int)), this, SLOT(check-boxSelectionModePickAdd-state-changed(int)))

;    check-boxSelectionModePickDrag = tk.check-box(translate("Drag to Select (PickDrag)"), groupBoxSelectionModes)
;    dialog-selection-mode-pickdrag = selection-mode-pickdrag
;    check-boxSelectionModePickDrag.setChecked(dialog-selection-mode-pickdrag)
;    check-boxSelectionModePickDrag.setChecked(0); check-boxSelectionModePickDrag.set-enabled(0); #TODO: Remove this line when this functionality is available
;    #connect(check-boxSelectionModePickDrag, SIGNAL(-state-changed(int)), this, SLOT(check-boxSelectionModePickDrag-state-changed(int)))

;    vboxLayoutSelectionModes = tk.VBoxLayout(groupBoxSelectionModes)
;    vboxLayoutSelectionModes.add-widget(check-boxSelectionModePickFirst)
;    vboxLayoutSelectionModes.add-widget(check-boxSelectionModePickAdd)
;    vboxLayoutSelectionModes.add-widget(check-boxSelectionModePickDrag)
;    groupBoxSelectionModes.setLayout(vboxLayoutSelectionModes)

;    #Selection Colors
;    groupBoxSelectionColors = tk.GroupBox(translate("Colors"), widget)

;    labelCoolGripColor = tk.Label(translate("Cool Grip (Unselected)"), groupBoxSelectionColors)
;    combo-boxCoolGripColor = tk.combo-box(groupBoxSelectionColors)
;    addColorsTocombo-box(combo-boxCoolGripColor)
;    dialog-selection-coolgrip-color = selection-coolgrip-color
;    combo-boxCoolGripColor.setCurrentIndex(combo-boxCoolGripColor.findData(dialog-selection-coolgrip-color))
;    #connect(combo-boxCoolGripColor, SIGNAL(current-index-changed(int)), this, SLOT(combo-boxSelectionCoolGripColorCurrent-index-changed(int)))

;    labelHotGripColor = tk.Label(translate("Hot Grip (Selected)"), groupBoxSelectionColors)
;    combo-boxHotGripColor = tk.combo-box(groupBoxSelectionColors)
;    addColorsTocombo-box(combo-boxHotGripColor)
;    dialog-selection-hotgrip-color = selection-hotgrip-color
;    combo-boxHotGripColor.setCurrentIndex(combo-boxHotGripColor.findData(dialog-selection-hotgrip-color))
;    #connect(combo-boxHotGripColor, SIGNAL(current-index-changed(int)), this, SLOT(combo-boxSelectionHotGripColorCurrent-index-changed(int)))

;    vboxLayoutSelectionColors = tk.VBoxLayout(groupBoxSelectionColors)
;    vboxLayoutSelectionColors.add-widget(labelCoolGripColor)
;    vboxLayoutSelectionColors.add-widget(combo-boxCoolGripColor)
;    vboxLayoutSelectionColors.add-widget(labelHotGripColor)
;    vboxLayoutSelectionColors.add-widget(combo-boxHotGripColor)
;    groupBoxSelectionColors.setLayout(vboxLayoutSelectionColors)

;    #Selection Sizes
;    groupBoxSelectionSizes = tk.GroupBox(translate("Sizes"), widget)

;    labelSelectionGripSize = tk.Label(translate("Grip Size"), groupBoxSelectionSizes)
;    sliderSelectionGripSize = tk.Slider(Qt-Horizontal, groupBoxSelectionSizes)
;    sliderSelectionGripSize.setRange(1,20)
;    dialog-selection-grip-size = selection-grip-size
;    sliderSelectionGripSize.setValue(dialog-selection-grip-size)
;    #connect(sliderSelectionGripSize, SIGNAL(-value-changed(int)), this, SLOT(sliderSelectionGripSize-value-changed(int)))

;    labelSelectionPickBoxSize = tk.Label(translate("Pickbox Size"), groupBoxSelectionSizes)
;    sliderSelectionPickBoxSize = tk.Slider(Qt-Horizontal, groupBoxSelectionSizes)
;    sliderSelectionPickBoxSize.setRange(1,20)
;    dialog-selection-pickbox-size = selection-pickbox-size
;    sliderSelectionPickBoxSize.setValue(dialog-selection-pickbox-size)
;    #connect(sliderSelectionPickBoxSize, SIGNAL(-value-changed(int)), this, SLOT(sliderSelectionPickBoxSize-value-changed(int)))

;    vboxLayoutSelectionSizes = tk.VBoxLayout(groupBoxSelectionSizes)
;    vboxLayoutSelectionSizes.add-widget(labelSelectionGripSize)
;    vboxLayoutSelectionSizes.add-widget(sliderSelectionGripSize)
;    vboxLayoutSelectionSizes.add-widget(labelSelectionPickBoxSize)
;    vboxLayoutSelectionSizes.add-widget(sliderSelectionPickBoxSize)
;    groupBoxSelectionSizes.setLayout(vboxLayoutSelectionSizes)

;    #Widget Layout
;    vbox-layout-main = tk.VBoxLayout(widget)
;    vbox-layout-main.add-widget(groupBoxSelectionModes)
;    vbox-layout-main.add-widget(groupBoxSelectionColors)
;    vbox-layout-main.add-widget(groupBoxSelectionSizes)
;    vbox-layout-main.addStretch(1)
;    widget.setLayout(vbox-layout-main)

;    scroll-area = tk.scroll-area(this)
;    scroll-area.setWidgetResizable(1)
;    scroll-area.setWidget(widget)
;    return scroll-area
;    */
)

;/* 
; *  Action functions.
; */

(define ()
;create-line-edit(int type, int user-editable)
;    (debug-message "create-tool-button({type}, {user-editable})")
)

(define ()
;create-tool-button(int type, char *label)
;    (debug-message "create-tool-button({type}, {label})")
)

(define ()
;line-action(void)
;    (debug-message "line-action()")
)

(define ()
;distance-action(void)
;    (debug-message "distance-action()")
)

(define ()
;dolphin-action(void)
;    (debug-message "dolphin-action()")
)

(define ()
;ellipse-action(void)
;    (debug-message "ellipse-action()")
)

;void
;pan-real-time-action(void)
;    (debug-message "pan-real-time-action()")
;    /* panning-real-time-active = 1; */
)

;void
;pan-point-action(void)
;    (debug-message "pan-point-action()")
;    /* panning-point-active = 1; */
)

;void
;pan-left-action(void)
;    (debug-message "pan-left-action()")
;    /*
;    horizontal-scroll-bar().set-value(horizontal-scroll-bar().value() + pan-distance)
;    update-mouse-coords(view-mouse-point.x(), view-mouse-point.y())
;    gscene.update()
;    */
)

;void
;pan-right-action(void)
;    (debug-message "pan-right-action()")
;    /*
;    horizontal-scroll-bar().set-value(horizontal-scroll-bar().value() - pan-distance)
;    update-mouse-coords(view-mouse-point.x(), view-mouse-point.y())
;    gscene.update()
;    */
)

(define ()
;pan-up-action(void)
;    (debug-message "pan-up-action()")
;    /*
;    vertical-scroll-bar().set-value(vertical-scroll-bar().value() + pan-distance)
;    update-mouse-coords(view-mouse-point.x(), view-mouse-point.y())
;    gscene.update()
;    */
)

(define ()
;pan-down-action(void)
;    (debug-message "pan-down-action()")
;    /*
;    vertical-scroll-bar().set-value(vertical-scroll-bar().value() - pan-distance)
;    update-mouse-coords(view-mouse-point.x(), view-mouse-point.y())
;    gscene.update()
;    */
)



;/* .
;*/
(define ()
;delete-selected(void)
;    /*
;    item-list = gscene.selected-items()
;    numSelected = item-list.size()

;    for (i in range(len(item-list))) {
;        if (item-list[i].data(OBJ-TYPE) != OBJ-TYPE-NULL) {
;            base = item-list[i]
;            if (base) {
;                (debug-message ".")
;            }
;        }
;    } */
)

(define ()
;create-object-list(int *list-)
;    /*copy-list = []

;    for (item in list-) {
;        if (!item) {
;            continue
;        }

;        if (item.type in -Arc", "Circle", "DimLeader", "Ellipse", "Line",
;                            "Path", "Point", "Polygon", "Polyline", "Rect", "Text Single) {
;            copy-list += [item.copy()]

;        else {
;            if (item.type in -Block", "DimAligned", "DimAngular", "DimArcLength",
;                            "DimDiameter", "DimLinear", "DimOrdinate", "DimRadius",
;                            "Ellipse Arc", "Image", "Infinite Line", "Ray) {
;                (debug-message "TODO: %s" % item.type)
;            }
;        }
;    }

;    return copy-list; */
)

(define ()
;move-selected(EmbVector delta)
;    /* item-list = gscene.selected-items()
;    num-selected = item-list.size()

;    for (item in item-list) {
;        if (item) {
;            (debug-message " . ")
;        }
;    } */

;    /* Always clear the selection after a move. */
;    /* gscene.clear-selection(); */
)

(define ()
;move-action(void)
;    (debug-message " . ")
)


;/*
; *  To make the undo history easier to manage we use a dict for
; *  keeping all the action information together.
; */

;/*
;settings = load-data("config.json")
;icons = load-data("icons.json")
;designs = load-data("designs.json")
;*/

(define ()
;settings-dialog(int showTab)
;    /*  dialog = settings-dialog-action(showTab)
;    dialog-mainloop(); */
)

(define ()
;draw-icon(void)
;    /*
;    Would work on lists like self:

;    "about": [
;        "arc 0 0 128 128 1 -1 black 3",
;        "arc 0 0 128 128 -2 2 black 3",
;        "arc 20 20 108 108 40 -40 black 3"
;    ]
;    out = Image.new("RGB", (128, 128), (255, 255, 255))
;    draw = ImageDraw.Draw(out)
;    for (line in code) {
;        cmd = line.split(" ")
;        if (cmd[0] == "arc") {
;            box = (int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4]))
;            start = int(cmd[5])
;            end = int(cmd[6])
;            draw.arc(box, start, end, fill=cmd[7], width=int(cmd[8]))
;        }
;    }
;    return out
;    */
;    /*  return "self function is overridden."; */
)

(define ()
;check-for-updates(void)
;    /* (debug-message "check-for-updates()")
;    #TODO: Check website for versions, commands, etc... */
)

(define ()
;select-all(void)
;    (debug-message "selectAll()")
;    /*
;    gview = active-view()
;    if gview:
;        gview.selectAll()

;    allPath = Path()
;    allPath.add-rect(gscene.scene-rect())
;    gscene.setSelectionArea(allPath, "ReplaceSelection", "intersects-item-shape", transform())
;    */
)

(define ()
;design-details(void)
;    /*  scene = active-scene()
;    if (scene) {
;        dialog = details-dialog-init(scene, self)
;        dialog-exec()
;    }*/
)



;void
;button-tip-of-the-day-clicked(int button)
;    (debug-message "button-tip-of-the-day-clicked()")
;    if (button == 0) {
;        if (general-current-tip > 0) {
;            general-current-tip--
;        }
;        else {
;            general-current-tip = n-tips-1
;        }
;        /* setText(tips[general-current-tip]); */
;        return
;    }
;    if (button == 1) {
;        general-current-tip++
;        if (general-current-tip >= n-tips) {
;            general-current-tip = 0
;        }
;        /* setText(tips[general-current-tip]); */
;        return
;    }
;    /* close dialog */
)


(define ()
;icon-resize(int icon-size)
;    /*
;    seticon-size(icon-size, icon-size)
;    layer-selector.seticon-size(icon-size*4, icon-size)
;    color-selector.seticon-size(icon-size, icon-size)
;    linetype-selector.seticon-size(icon-size*4, icon-size)
;    lineweightSelector.seticon-size(icon-size*4, icon-size)
;    #set the minimum combobox width so the text is always readable
;    layer-selector.set-minimum-width(icon-size*4)
;    color-selector.set-minimum-width(icon-size*2)
;    linetype-selector.set-minimum-width(icon-size*4)
;    lineweightSelector.set-minimum-width(icon-size*4)

;    #TODO: low-priority:
;    #open app with icon-size set to 128. resize the icons to a smaller size.

;    general-icon-size = icon-size */
)

(define ()
;active-mdi-window(void)
;    /* (debug-message "activemdi-window()")
;    mdi-win = mdi-area.active-sub-window()
;    return mdi-win */
)


;/*
; * Missing function from Qt.
; *
; * Might need to be in View scope not Window.
; */
;void
;set-pen(void)
;    (debug-message "set-pen")
)

;/* This may need to be a method of Main Window. */
;void
;clear-selection(void)
;    (debug-message "clear-selection")
;    /* gscene.clear-selection()
;    prompt = ""; */
)

;/* This function intentionally does nothing. */
;void
;do-nothing(void)
;    (debug-message "do-nothing()")
)

;void
;close-toolbar(int action)
;    /*
;    if (action.object-name() == "toolbarclose") {
;        tb = sender()
;        if (tb) {
;            (debug-message "%s closed.", str(tb.object-name()))
;            tb.hide()
;        }
;    }
;    */
)

;void
;layer-manager-action(void)
;    (debug-message "layerManager()")
;    (debug-message "Implement layerManager.")
;    /* #LayerManager layman( self,  self)
;     * #layman.exec()
)

;void
;layer-previous-action(void)
;    (debug-message "layerPrevious()")
;    (debug-message "Implement layerPrevious.")
)

;void
;layer-selector(void)
;    (debug-message "exit-action()")
)

;void
;line-weight-selector(void)
;    (debug-message "line-weight-selector-action()")
)

;/* Open line type selector dialog-
; */
;void
;line-type-selector(void)
;    (debug-message "line-type-selector-action()")
)

;/* Open color selector dialog-
; */
;void
;color-selector(void)
;    (debug-message "color-selector-action()")
)

(define ()
;layer-selector-action(void)

)

(define ()
;setBackgroundColor(void)

)

(define ()
;setGridColor(void)
;    
)

(define ()
;setCrossHairColor(void)
;    
)

;/*  Whenever the code happens across a todo call, write it in a log file.
; */
(define ()
;alert(char *title, char *message)
;    if (debug-mode) {
;        FILE *f
;        f = fopen("alert.txt", "a")
;        fprintf(f, "%s\n%s\n", title, message)
;        fclose(f)
;    }
)

;/* Should we need to add this to an error report.
; */
(define ()
;report-platform(void)
;    /* print(os.uname()); */
)

(define ()
;scale-action(void)
;    (debug-message ".")
)

;/* . */
(define ()
;get-file-separator(void)
;    (debug-message "getFileSeparator()")
;    /* return my-file-separator */
)


(define ()
;active-view(void)
;    (debug-message "active-view()")
;    /* mdi-win = mdi-area.active-sub-window()
;    if (mdi-win) {
;        v = mdi-win.getView()
;        return v
;    } */
)

(define ()
;active-scene(void)
;    (debug-message "active-scene()")
;    /* mdi-win = mdi-area.active-sub-window()
;    if (mdi-win) {
;        return mdi-win.getScene()
;    } */
)

(define ()
;update-all-view-scroll-bars(int val)
;    /* windowList = mdi-area.sub-window-list()
;    for (mdi-win in windowList) {
;        mdi-win.showViewScrollBars(val)
;    } */
)

(define ()
;update-all-view-cross-hair-colors(EmbColor color)
;    /*windowList = mdi-area.sub-window-list()
;    for (mdi-win in windowList) {
;        mdi-win.setViewCrossHairColor(color)
;    } */
)

(define ()
;updateAllViewBackgroundColors(EmbColor color)
;    /*windowList = mdi-area.sub-window-list()
;    for (mdi-win in windowList) {
;        mdi-win.setViewBackgroundColor(color)
;    } */
)

(define ()
;check-box(int setting, int checked)
;    dialog-setting-int[setting] = checked
)

(define ()
;spin-box(int setting, double value)
;    dialog-setting-double[setting] = value
)

;/*
; * This is the heart of the program, we're working on replacing
; * the Qt reliance, so these functions and data represent the eventual core
; * of the program.
; *
; * The widget system is created here, but it is built on top of the
; * SVG system created in libembroidery. So a widget is an svg drawing,
; * with a position to draw it in relative to its parent. The widgets
; * form a tree rooted at the global variable called root.
; *
; * TODO: Set What's self Context Help to statusTip for now so there
; * is some infos there.
; *
; * Make custom What's self Context Help popup with more descriptive help
; * than just the status bar/tip one liner(short but not real long) with a
; * hyperlink in the custom popup at the bottom to open full help file
; * description. Ex: like wxPython AGW's SuperToolTip.
; */
(define ()
;main-window-init(void)
;    /* To stop the garbage collector stealing our icons. */
;    /* tkimg = {}

;    root = tk.Tk()
;    root.title(title)
;    root.minsize(width, height)
;    build-menu-bar()
;    build-button-grid()
;    undo-history = []
;    undo-history-position = 0
;    opensave-recent-list-of-files = []
;    opensave-custom-filter = ""
;    current-path = ""

;    num-docs = 0
;    tab-index = 0

;    lang = general-language
;    (debug-message "language: %s" % lang)
;    */
;    /* This is a View() instance. */
;    /* canvas = tk.Canvas(root, bg="#FFFFFF",
;                            width=500, height=400)
;    canvas.grid(row=4, column=0, columnspan=20, rowspan=2, sticky="W")
;*/
;    /* Use PropertyEditor
;     * need to make a tk.Entry test
;     */
;   /* property-editor = tk.Label(root, text="Property Editor",
;                                    bg="#FFFFFF")
;    property-editor.grid(row=4, column=21, columnspan=5, sticky="NE")

;    undo-history-editor = tk.Label(root, text="Undo History",
;                                        bg="#FFFFFF")
;    undo-history-editor.grid(row=5, column=21, columnspan=5, 
;                                  sticky="NE")

;    message-bar = tk.Label(root,
;                                text=time.strftime("%d %B %Y"),
;                                bg="#BBBBBB")
;    message-bar.set-text("test")
;    message-bar.grid(row=6, column=0, columnspan=20, sticky="SW")
;    message-bar-tip = Tooltip(
;        message-bar,
;        "*Message Bar*\nShows current state of the program, useful for bug checking information.")

;    return

;    for i in range(nFolders) {
;        current-path = application-folder + folders[i]
;        if (!exists(current-path) {
;            critical(translate("Path Error"), translate("Cannot locate: ") + current-path)

;    if (lang == "system") {
;        lang = QLocale-system().languageToString(QLocale-system().language()).lower()
;    }
; */
;    /* Load translations provided by Qt - self covers dialog buttons and other common things. */ /*
;    translatorQt = ""
;    translatorQt.load("" + QLocale-system().name(), QLibraryInfo-location(QLibraryInfo-TranslationsPath)); */
;    /* TODO: ensure self always loads, ship a copy of self with the app. */
;    /* qApp.installTranslator(translatorQt); */

;    /* Selectors */ /*
;    layer-selector = ComboBox()
;    color-selector = ComboBox()
;    linetype-selector = ComboBox()
;    lineweightSelector = ComboBox()
;    textFontSelector = FontComboBox()
;    text-size-selector = ComboBox()

;    shiftKeyPressedState = 0

;    set-windowIcon(app.png); */
;    /* Require Minimum WVGA */ /*
;    set-minimum-size(800, 480)

;    load-formats()
;    */
;    /* create the mdi-area */ /*
;    vbox = Frame(void)
;    layout = VBoxLayout(vbox)
;    layout.setContentsMargins(Margins())
;    vbox.setFrameStyle(Frame-StyledPanel | Frame-Sunken)
;    mdi-area = mdi-area(vbox)
;    mdi-area.useBackgroundLogo(general-mdi-bg-use-logo)
;    mdi-area.useBackgroundTexture(general-mdi-bg-use-texture)
;    mdi-area.useBackgroundColor(general-mdi-bg-use-color)
;    mdi-area.setBackgroundLogo(general-mdi-bg-logo)
;    mdi-area.setBackgroundTexture(general-mdi-bg-texture)
;    mdi-area.setBackgroundColor(Color(general-mdi-bg-color))
;    mdi-area.setViewMode("TabbedView")
;    mdi-area.setHorizontalScrollBarPolicy("ScrollBarAsNeeded")
;    mdi-area.setVerticalScrollBarPolicy("ScrollBarAsNeeded")
;    mdi-area.setActivationOrder("ActivationHistoryOrder")
;    layout.add-widget(mdi-area)
;    setCentralWidget(vbox)
;    */
;    /*
;    setDockOptions(QAnimatedDocks | QAllowTabbedDocks | QVerticalTabs)
  ; TODO: Load these from settings
;    tabifyDockWidget(dockPropEdit, dockUndoEdit)
  ; TODO: load this from settings
;
;
;    statusbar = StatusBar(root)
;    setStatusBar(statusbar)

;    for (i=0; i<action-list.keys(void); i++)
;        Icon = action-list[i].icon
;        ACTION = Action(Icon, action-list[i].menu-name, self)

;        if len(action-list[i].shortcut)>0:
;            ACTION.setShortcut(QKeySequence(action-list[i].shortcut))

;        ACTION.set-status-tip(action-list[i].description)
;        ACTION.set-object-name(action-list[i].abbreviation)
;        ACTION.setWhatsself(action-list[i].description)
;
;        connect(ACTION, SIGNAL(triggered()), self, SLOT(actions()))
;        action-hash.insert(i, ACTION);

;    action-hash.value("window-close").set-enabled(n-docs > 0)
;    action-hash.value("design-details").set-enabled(n-docs > 0)

;    menu-FILE.add-menu(menu[RECENT-MENU])
;    Do not allow the Recent Menu to be torn off. It's a pain in the ass to maintain.
;    menu[RECENT-MENU].set-tear-off-enabled(0);

;    (debug-message "createWindowMenu()")
;    menu-bar().add-menu(menu-WINDOW)
;    connect(menu-WINDOW, SIGNAL(aboutToShow()), self, SLOT(window-menu-about-to-show())); */
  ; Do not allow the Window Menu to be torn off.
  ; It's a pain in the ass to maintain.
;    menu-WINDOW.set-tear-off-enabled(0)

;    for i in range(N-TOOLBARS) {
;        message = "creating %s\n" % toolbar-label[i]
;        (debug-message message)

;        toolbar[i].set-object-name(toolbar-label[i])

;        for j in toolbars[i]:
;            if toolbars[i][j] >= 0:
;                toolbar[i].add-action(action-hash.value(toolbars[i][j]))
;            else {
;                toolbar[i].add-separator()
;        */
;        /*  connect(toolbar[i], SIGNAL(topLevelChanged(int)), self, SLOT(floating-changed-toolbar(int)));

;    (debug-message "createLayerToolbar()")

;    toolbar-LAYER.set-object-name("toolbarLayer")
;    toolbar-LAYER.add-action(action-hash.value("make-layer-current"))
;    toolbar-LAYER.add-action(action-hash.value("layers"))

;    #TODO: Create layer pixmaps by concatenating several icons
;    layer-selector.add-item("linetypebylayer.png", "0")
;    layer-selector.add-item("linetypebylayer.png", "1")
;    layer-selector.add-item("linetypebylayer.png", "2")
;    layer-selector.add-item("linetypebylayer.png", "3")
;    layer-selector.add-item("linetypebylayer.png", "4")
;    layer-selector.add-item("linetypebylayer.png", "5")
;    layer-selector.add-item("linetypebylayer.png", "6")
;    layer-selector.add-item("linetypebylayer.png", "7")
;    layer-selector.add-item("linetypebylayer.png", "8")
;    layer-selector.add-item("linetypebylayer.png", "9")
;    toolbar-LAYER.add-widget(layer-selector)
;    #connect(layer-selector, SIGNAL(currentIndexChanged(int)), self, SLOT(layer-selectorIndexChanged(int)))

;    toolbar-LAYER.add-action(action-hash.value("layer-previous"))

;    #connect(toolbar-LAYER, SIGNAL(topLevelChanged(int)), self, SLOT(floating-changed-toolbar(int)))

;    (debug-message "createPropertiesToolbar()")

;    toolbar-PROPERTIES.set-object-name("toolbar-properties")

;    color-selector.set-focusProxy(menu-FILE)
;    #NOTE: Qt4.7 wont load icons without an extension...
;    color-selector.add-item("colorbylayer.png", "ByLayer")
;    color-selector.add-item("colorbyblock.png", "ByBlock")
;    color-selector.add-item("colorred.png", translate("Red"), (255, 0, 0))
;    color-selector.add-item("coloryellow.png", translate("Yellow"), (255,255, 0))
;    color-selector.add-item("colorgreen.png", translate("Green"), (0, 255, 0))
;    color-selector.add-item("colorcyan.png", translate("Cyan"), (0,255,255))
;    color-selector.add-item("colorblue.png", translate("Blue"), (0, 0,255))
;    color-selector.add-item("colormagenta.png", translate("Magenta"), (255, 0,255))
;    color-selector.add-item("colorwhite.png", translate("White"), (255,255,255))
;    color-selector.add-item("colorother.png", translate("Other..."))
;    toolbar-PROPERTIES.add-widget(color-selector)
;    #connect(color-selector, SIGNAL(currentIndexChanged(int)), self, SLOT(color-selectorIndexChanged(int)))

;    toolbar-PROPERTIES.add-separator()
;    linetype-selector.set-focusProxy(menu-FILE)
;    linetype-selector.add-item("linetypebylayer.png", "ByLayer")
;    linetype-selector.add-item("linetypebyblock.png", "ByBlock")
;    linetype-selector.add-item("linetypecontinuous.png", "Continuous")
;    linetype-selector.add-item("linetypehidden.png", "Hidden")
;    linetype-selector.add-item("linetypecenter.png", "Center")
;    linetype-selector.add-item("linetypeother.png", "Other...")
;    toolbar-PROPERTIES.add-widget(linetype-selector)
;    #connect(linetype-selector, SIGNAL(currentIndexChanged(int)), self, SLOT(linetype-selectorIndexChanged(int)))

;    toolbar-PROPERTIES.add-separator()
;    lineweightSelector.set-focusProxy(menu-FILE)
;    #NOTE: Qt4.7 wont load icons without an extension...
;    #TODO: Thread weight is weird. See http://en.wikipedia.org/wiki/Thread-(yarn)#Weight
;    for line in thread-weights:
;        lineweightSelector.add-item(line[0], line[1], line[2])
;    lineweightSelector.setMinimumContentsLength(8)
;    #Prevent dropdown text readability being squish...d.
;    toolbar-PROPERTIES.add-widget(lineweightSelector)
;    #connect(lineweightSelector, SIGNAL(currentIndexChanged(int)), self, SLOT(lineweightSelectorIndexChanged(int)))

;    #connect(toolbar-PROPERTIES, SIGNAL(topLevelChanged()), self, SLOT(floating-changed-toolbar()))

;    (debug-message "createTextToolbar()")
;    toolbar-TEXT.set-object-name("toolbarText")
;    toolbar-TEXT.add-widget(textFontSelector)
;    textFontSelector.setCurrentFont(Font(text-font))
;    #connect(textFontSelector, SIGNAL(currentFontChanged()), self, SLOT(textFontSelectorCurrentFontChanged()))

;    #TODO: SEGFAULTING FOR SOME REASON
;    toolbar-TEXT.add-action(action-hash.value("text-bold"))
;    action-hash.value("text-bold").set-checked(text-style-bold)
;    toolbar-TEXT.add-action(action-hash.value("text-italic"))
;    action-hash.value("text-italic").set-checked(text-style-italic)
;    toolbar-TEXT.add-action(action-hash.value("text-underline"))
;    action-hash.value("text-underline").set-checked(text-style-underline)
;    toolbar-TEXT.add-action(action-hash.value("text-strikeout"))
;    action-hash.value("text-strikeout").set-checked(text-style-strikeout)
;    toolbar-TEXT.add-action(action-hash.value("text-overline"))
;    action-hash.value("text-overline").set-checked(text-style-overline)

;    text-size-selector.set-focusProxy(menu-FILE)
;    sizes = [6, 8, 9, 10, 11, 12, 14, 18, 24, 30, 36, 48, 60, 72]
;    for size in sizes:
;        text-size-selector.add-item(str(size)+" pt", size)
;    setTextSize(text-size)
;    toolbar-TEXT.add-widget(text-size-selector)
;    #connect(text-size-selector, SIGNAL(currentIndexChanged(int)), self, SLOT(text-size-selectorIndexChanged(int)))

;    #connect(toolbar-TEXT, SIGNAL(topLevelChanged(int)), self, SLOT(floating-changed-toolbar(int)))

;    #Horizontal
;    toolbar-VIEW.set-orientation("Horizontal")
;    toolbar-ZOOM.set-orientation("Horizontal")
;    toolbar-LAYER.set-orientation("Horizontal")
;    toolbar-PROPERTIES.set-orientation("Horizontal")
;    toolbar-TEXT.set-orientation("Horizontal")
;    #Top
;    add-toolbar-break("TopToolBarArea")
;    add-toolbar("TopToolBarArea", toolbar-FILE)
;    add-toolbar("Top toolbar area", toolbar-EDIT)
;    add-toolbar("Top toolbar area", toolbar-HELP)
;    add-toolbar("Top toolbar area", toolbar-ICON)
;    add-toolbar-break("TopToolBarArea")
;    add-toolbar("Top toolbar area", toolbar-ZOOM)
;    add-toolbar("Top toolbar area", toolbar-PAN)
;    add-toolbar("Top toolbar area", toolbar-VIEW)
;    add-toolbar-break("TopToolBarArea")
;    add-toolbar("Top toolbar area", toolbar-LAYER)
;    add-toolbar("Top toolbar area", toolbar-PROPERTIES)
;    add-toolbar-break("TopToolBarArea")
;    add-toolbar("Top toolbar area", toolbar-TEXT)

;    #zoomToolBar.setToolButtonStyle("ToolButtonTextOnly")

;    icon-resize(get-int(main-window, "general-icon-size"))
;    update-menu-toolbar-statusbar()

;    #Show date in statusbar after it has been updated
;    #TODO: Switch to ISO dates.

;    date = time.currentDate()
;    datestr = date.toString("MMMM d, yyyy")
;    statusbar.showMessage(datestr)

;    showNormal()

;    if general-tip-of-the-day:
;        tip-of-the-day-action(); */
)

(define ()
;read-settings(void)
;    /*   (debug-message "Reading settings...")

;    #self file needs to be read from the users home directory to ensure it is writable.
;    pos = Vector(window-x, window-y)
;    size = (window-width, window-height)

;    #
;    layoutState = settings-file.value("LayoutState").toByteArray()
;    if ! restoreState(layoutState) {
;        (debug-message "LayoutState NOT restored! Setting Default Layout...")
;        #someToolBar.setVisible(1)

;    settings = load-data("config.json")

;    #Sanitise data here
;    window-x = clamp(0, window-x, 1000)
;    window-y = clamp(0, window-y, 1000)

;    move(pos)
;    resize(size); */
)

(define ()
;rotate-action(void)
;    (debug-message "TODO")
)

(define ()
;rotate-selected(EmbVector pos, double rot)
;    /* item-list = gscene.selected-items()
;    num-selected = item-list.size()
;    for (item in item-list) {
;        if (item) {
;            (debug-message ".")
;        }
;    } */
;    /* Always clear the selection after a rotate. */
;    /* gscene.clear-selection(); */
)

(define ()
;mirror-selected(EmbVector point1, EmbVector point2)
;    /* item-list = gscene.selected-items()
;    num-selected = item-list.size()
;    for (item in item-list) {
;        if (item) {
;            (debug-message ".")
;        }
;    } */
;    /*  Always clear the selection after a mirror. */
;    /* gscene.clear-selection(); */
)

(define ()
;scale-selected(EmbVector v, double factor)
;    /* item-list = gscene.selected-items()
;    num-selected = item-list.size()
;    for (item in item-list) {
;        if (item) {
;            (debug-message ".")
;        }
;    } */
;    /*  Always clear the selection after a scale. */
;    /* gscene.clear-selection(); */
)

;static int
;num-selected(void)
;    /* return gscene.selected-items().size(); */
;    return 0
)

(define ()
;show-scroll-bars(int val)
;    if (val) {
;        /* set-horizontal-scroll-bar-policy("ScrollBarAlwaysOn")
;        set-vertical-scroll-bar-policy("ScrollBarAlwaysOn"); */
;    }
;    else {
;        /* set-horizontal-scroll-bar-policy("ScrollBarAlwaysOff")
;        set-vertical-scroll-bar-policy("ScrollBarAlwaysOff"); */
;    }
)

(define ()
;set-cross-hair-color(MdiArea *mdi-area, EmbColor color)
;    /* crosshair-color = color
;    gscene.set-property("VIEW-COLOR-CROSSHAIR", color)
;    gscene.update()
;    */
)

(define ()
;set-background-color(MdiArea *mdi-area, EmbColor color)
;    /* set-background-brush(Color(color))
;    gscene.set-property("VIEW-COLOR-BACKGROUND", color)
;    gscene.update()
;    */
)

(define ()
;set-select-box-colors(
;    MdiArea *mdi-area,
;    EmbColor color-left,
;    EmbColor fill-left,
;    EmbColor color-right,
;    EmbColor fill-right,
;    double alpha)
;    /* select-box.set-colors(color-left, fill-left, color-right, fill-right, alpha); */
)

(define ()
;update-all-view-select-box-colors(
;    EmbColor colorL, EmbColor fillL, EmbColor colorR, EmbColor fillR,
;    double alpha)
;    /* windowList = mdi-area.sub-window-list()
;    for (mdi-win in windowList) {
;        mdi-win.setViewSelectBoxColors(colorL, fillL, colorR, fillR, alpha)
;    } */
)

(define ()
;update-all-view-grid-colors(EmbColor color)
;    /*
;    windowList = mdi-area.sub-window-list()
;    for (mdi-win in windowList) {
;        mdi-win.setViewGridColor(color)
;    }
;    */
)

(define ()
;update-all-view-ruler-colors(EmbColor color)
;    /*
;    windowList = mdi-area.sub-window-list()
;    for (mdi-win in windowList) {
;        mdi-win.set-view-ruler-color(color)
;    }
;    */
)

(define ()
;update-pick-add-mode(int val)
;    /*
;    selection-mode-pickadd = val
;    dockPropEdit.update-pick-add-mode-button(val)
;    */
)

(define ()
;pick-add-mode-toggled(void)
;    /*
;    val = !selection-mode-pickadd
;    updatePickAddMode(val)
;    */
)

(define ()
;layer-selector-index-changed(int index)
;    printf("layer-selectorIndexChanged(%d)", index)
)


;/* Color selector index changed.
; */
(define ()
;color-selector-index-changed(int index)
;    printf("color-selectorIndexChanged(%d)", index)
;    /*
;    comboBox = sender()
;    newColor = Color()
;    if comboBox:
;        ok = 0
;        #TODO: Handle ByLayer and ByBlock and Other...
;        newColor, ok = comboBox.itemData(index).toUInt()
;        if ! ok:
;            warning(translate("Color Selector Conversion Error"), translate("<b>An error has occurred while changing colors.</b>"))

;    else {
;        warning(translate("Color Selector Pointer Error"), translate("<b>An error has occurred while changing colors.</b>"))

;    mdi-win = mdi-area.active-sub-window()
;    if (mdi-win) {
;        mdi-win.currentColorChanged(newColor)
;    }
;    */
)

(define ()
;linetype-selector-index-changed(int index)
;    printf("linetype-selectorIndexChanged(%d)", index)
;    actuator(ACTION-DO-NOTHING)
)

(define ()
;lineweight-selector-index-changed(int index)
;    printf("lineweightSelectorIndexChanged(%d)", index)
;    actuator(ACTION-DO-NOTHING)
)

;/* Text font selector current font changed.
; */
(define ()
;text-fontSelectorCurrentFontChanged(char *font)
;   /*  (debug-message "textFontSelectorCurrentFontChanged()")
;    textFontSelector.setCurrentFont(Font(font.family()))
;    text-font = font.family().toLocal8Bit().constData(); */
)

;/* TODO: check that the toReal() conversion is ok.
; */
(define ()
;text-size-selectorIndexChanged(int index)
;    /* (debug-message "text-size-selectorIndexChanged(%d)", index)
;    text-style.size = abs(text-size-selector.itemData(index).toReal()); */
)

(define ()
;text-font(void)
;    /*return text-font; */
)

(define ()
;setTextSize(int num)
;    int index
;    /*
;    text-style.size = abs(num)
;    index = text-size-selector.find-text("Custom", "MatchContains")
;    if (index != -1) {
;        text-size-selector.remove-item(index)
;    }
;    text-size-selector.add-item("Custom " + "".set-num(num, 'f', 2) + " pt", num)
;    index = text-size-selector.find-text("Custom", "MatchContains")
;    if (index != -1) {
;        text-size-selector.setCurrentIndex(index)
;    }*/
)

;static int
;getCurrentLayer(void)
;    (debug-message "getCurrentLayer")
;    if (window == NULL) {
;        (debug-message "called without window initialised.")
;        return -2
;    }
;    /*
;    (debug-message (char*)title)
;    mdi-win = mdi-area.active-sub-window()
;    if (mdi-win) {
;        return mdi-win.getCurrentLayer()
;    }
;    */
;    return 0
)

;/* TODO: return color ByLayer.
; */
;static int
;get-current-color(void)
;    (debug-message "get-current-color")
;    if (window == NULL) {
;        (debug-message "called without window initialised.")
;        return -2
;    }
;    /*
;    (debug-message (char*)title)
;    mdi-win = mdi-area.active-sub-window()
;    if mdi-win:
;        return mdi-win.get-current-color()
;    */
;    return 0
)

;static int
;get-current-line-type(void)
;    (debug-message "get-current-line-type")
;    if (window == NULL) {
;        (debug-message "called without window initialised.")
;        return -2
;    }
;    /*
;    (debug-message (char*)title)
;    mdi-win = mdi-area.active-sub-window()
;    if (mdi-win) {
;        return mdi-win.get-current-line-type()
;    }
;    */
;    return OBJ-LWT-BYLAYER
)

;static int
;get-current-line-weight(void)
;    (debug-message "get-current-line-weight")
;    if (window == NULL) {
;        (debug-message "called without window initialised.")
;        return -2
;    }
;    /*
;    (debug-message (char*)title)
;    mdi-win = mdi-area.active-sub-window()
;    if (mdi-win) {
;        return mdi-win.get-current-line-weight()
;    }
;    */
;    return OBJ-LWT-BYLAYER
)

(define ()
;calculate-angle(EmbVector point1, EmbVector point2)
;    /*return Line(x1, -y1, x2, -y2).angle(); */
)

(define ()
;calculate-distance(EmbVector point1, EmbVector point2)
;    /* return Line(x1, y1, x2, y2).length(); */
)

(define ()
;fill-menu(int menu-id)
;    /*
;    (debug-message "MainWindow creating %s", menu-label[menu-id])
;    menu-bar().add-menu(menu[menu-id])
;    for (menu in menus[menu-id]) {
;        if (menus[menu-id][i] >= 0) {
;            menu[menu-id].add-action(action-hash.value(menus[menu-id][i]))
;        }
;        else {
;            menu[menu-id].add-separator()
;        }
;    }
;    */
)

;/*
; * This is currently causing a bug and is going to be replaced
; * with a libembroidery function.
; */
;static double
;native-perpendicular-distance(void)
;    EmbLine line
;    EmbVector norm
;    /*
;    line = Line(x1, y1, x2, y2)
;    norm = line.normal()
;    delta.x = point.x-x1
;    delta.y = point.y-y1
;    norm.translate(delta)
;    iPoint = norm.intersects(line)
;    return Line(point, iPoint).length(); */
)

(define ()
;recent-menu-about-to-show(void)
;    (debug-message "recentMenuAboutToShow()")
;    /*
;    menu[RECENT-MENU].clear()

;    recent-file-info = ""
;    recent-value = ""
;    for i in range(len(opensave-recent-list-of-files)) { */
;        /* If less than the max amount of entries add to menu */ /*
;        if i < opensave-recent-max-files:
;            recent-file-info = FileInfo(opensave-recent-list-of-files.at(i))
;            if recent-file-info.exists() and valid-file-format(recent-file-info.fileName()) {
;                recent-value.set-num(i+1)
;                rAction = 0
;                if recent-value.toInt() >= 1 and recent-value.toInt() <= 9:
;                    rAction = Action("&" + recent-value + " " + recent-file-info.fileName(), self)
;                elif recent-value.toInt() == 10:
;                    rAction = Action("1&0 "                  + recent-file-info.fileName(), self)
;                else {
;                    rAction = Action(recent-value + " " + recent-file-info.fileName(), self)
;                rAction.set-checkable(0)
;                rAction.set-data(opensave-recent-list-of-files.at(i))
;                menu[RECENT-MENU].add-action(rAction)
;                #connect(rAction, SIGNAL(triggered()), self, SLOT(openrecentfile()))

;    #Ensure the list only has max amount of entries
;    while opensave-recent-list-of-files.size() > opensave-recent-max-files:
;        opensave-recent-list-of-files.removeLast();*/
)

(define (window-menu-about-to-show)
;    (debug-message "window-menu-about-to-show()")
;    /*
;    menu-WINDOW.clear()
;    menu-WINDOW.add-action(action-hash.value("window-close"))
;    menu-WINDOW.add-action(action-hash.value("window-close-all"))
;    menu-WINDOW.add-separator()
;    menu-WINDOW.add-action(action-hash.value("window-cascade"))
;    menu-WINDOW.add-action(action-hash.value("window-tile"))
;    menu-WINDOW.add-separator()
;    menu-WINDOW.add-action(action-hash.value("window-next"))
;    menu-WINDOW.add-action(action-hash.value("window-previous"))

;    menu-WINDOW.add-separator()
;    windows = mdi-area.sub-window-list()
;    for i in range(len(windows)) {
;        an-action = Action(windows[i].window-title(), self)
;        an-action.set-checkable(1)
;        an-action.set-data(i)
;        menu-WINDOW.add-action(an-action)
;        #connect(an-action, SIGNAL(toggled(int)), self, SLOT(windowMenuActivated(int)))
;        an-action.set-checked(mdi-area.active-sub-window() == windows[i])
;        */
)

(define (window-menu-activated)
;(int *checked)
;    int a-sender
;    (debug-message "windowMenuActivated()")
;    a-sender = sender()
;    if (!a-sender) {
;        return
;    }
;    w = mdi-area.sub-window-list().at[a-sender.data().toInt()]
;    if (w and checked) {
;        w.set-focus()
;    }
)

(define (close-event event)
;    (debug-message "MdiWindow closeEvent()")
;    mdi-area.close-all-sub-windows()
;    write-settings()
;    event.accept()

;    sendCloseMdiWin()
)

(define (on-close-window)
;    (debug-message "onCloseWindow()")
;    mdi-win = mdi-area.active-sub-window()
;    if (mdi-win) {
;        onClosemdi-win(mdi-win)
;    }
)

(define (on-close-mdi-win)
;    int keep-maximized
;    (debug-message "onClosemdi-win()")
;    n-docs--
;    keep-maximized = 0
;    if (the-mdi-win) {
;        keep-maximized = the-mdi-win.is-maximized()
;    }

;    mdi-area.remove-sub-window(the-mdi-win)
;    the-mdi-win.delete-later()

;    update-menu-toolbar-statusbar()
;    window-menu-about-to-show()

;    if (keep-maximized) {
;        mdi-win = mdi-area.active-sub-window()
;        if (mdi-win) {
;            mdi-win.show-maximized()
;        }
;    }
)

(define (resize-event e)
;    (debug-message "resizeEvent()")
;    /* resizeEvent(e)
;    statusBar().setSizeGripEnabled(!isMaximized()); */
)

(define (update-menu-toolbar-statusbar)
;    (debug-message "updateMenuToolbarStatusbar()")
;    /*
;    action-enabled[ACTION-PRINT] = n-docs
;    action-enabled[ACTION-WINDOW-CLOSE] = n-docs
;    action-enabled[ACTION-DESIGN-DETAILS] = n-docs
;    */

;    if (n-docs) {
;        /*
;        #Toolbars
;        for key in toolbar.keys() {
;            toolbar[key].show()

;        #DockWidgets
;        dock-prop-edit.show()
;        dock-undo-edit.show()

;        #Menus
;        menu-bar().clear()
;        menu-bar().add-menu(menu-FILE)
;        menu-bar().add-menu(menu-EDIT)
;        menu-bar().add-menu(menu-VIEW)

;        for (menu- in menuHash) {
;            menu-bar().add-menu(menu-)
;        }

;        menu-bar().add-menu(menu-SETTINGS)
;        menu-bar().add-menu(menu-WINDOW)
;        menu-bar().add-menu(menu-HELP)

;        menu-WINDOW.set-enabled(1)

;        #Statusbar
;        statusbar.clear-message()
;        status-bar-mouse-coord.show()
;        status-bar-SNAP.show()
;        status-bar-GRID.show()
;        status-bar-RULER.show()
;        status-bar-ORTHO.show()
;        status-bar-POLAR.show()
;        status-bar-QSNAP.show()
;        status-bar-QTRACK.show()
;        status-bar-LWT.show()
;        */
;    }
;    else {
;        int i
;        int toolbars-to-hide[] = {
;            TOOLBAR-VIEW,
;            TOOLBAR-ZOOM,
;            TOOLBAR-PAN,
;            TOOLBAR-ICON,
;            TOOLBAR-HELP,
;            TOOLBAR-LAYER,
;            TOOLBAR-TEXT,
;            TOOLBAR-PROPERTIES,
;            -1
;        }
;        /*
;        for (i=0; toolbars-to-hide[i]>=0; i++) {
;            hide-toolbar(toolbars-to-hide[i])
;        }

;        #DockWidgets
;        dockPropEdit.hide()
;        dockUndoEdit.hide()

;        #Menus
;        menu-bar().clear()
;        menu-bar().add-menu(menu-FILE)
;        menu-bar().add-menu(menu-EDIT)
;        menu-bar().add-menu(menu-MENU)
;        menu-bar().add-menu(menu-WINDOW)
;        menu-bar().add-menu(menu-HELP)

;        menu-WINDOW.set-enabled(0)

;        #Statusbar
;        statusbar.clear-message()
;        status-bar-mouse-coord.hide()
;        for (k=0; k<status-bar-n-keys; k++) {
;            status-bar[k].hide()
;        }
;        */
;    }
)

(define ()
;load-formats(void)
;    int i, curFormat
;    char stable, unstable
;    char supported-readers[MAX-STRING-LENGTH]
;    char individual-readers[MAX-STRING-LENGTH]
;    char supported-writers[MAX-STRING-LENGTH]
;    char individual-writers[MAX-STRING-LENGTH]

;    supported-readers[0] = 0
;    individual-readers[0] = 0
;    supported-writers[0] = 0
;    individual-writers[0] = 0

;    strcat(supported-readers, "All Supported Files (")
;    strcat(individual-readers, "All Files (*);;")
;    strcat(supported-writers, "All Supported Files (")
;    strcat(individual-writers, "All Files (*);;")

;    /*
;    supported-str = ""
;    individual-str = ""

;    #TODO: Stable Only (Settings Option)
;    #stable = 'S'
;    #unstable = 'S'

;    #Stable + Unstable
;    stable = 'S'
;    unstable = 'U'

;    */
;    curFormat = 0
;    for (i=0; i<numberOfFormats; i++) {
;        /*
;        extension = format-table[i].extension
;        description = format-table[i].description
;        readerState = format-table[i].reader-state
;        writerState = format-table[i].writer-state

;        upper-ext = extension.upper()
;        supported-str = "*" + upper-ext + " "
;        individual-str = upper-ext.replace(".", "") + " - " + description + " (*" + extension + ");;"
;        if(readerState == stable or readerState == unstable) {
;            #Exclude color file formats from open dialogs
;            if(upper-ext != "COL" and upper-ext != "EDR" and upper-ext != "INF" and upper-ext != "RGB") {
;                supported-readers.append(supported-str)
;                individual-readers.append(individual-str)
;            }
;        }

;        if (writerState == stable or writerState == unstable) {
;            supported-writers.append(supported-str)
;            individual-writers.append(individual-str)
;        }
;        */
;    }

;    strcat(supported-readers, ");;")
;    strcat(supported-writers, ");;")

;    /*
;    format-filter-open = supported-readers + individual-readers
;    format-filter-save = supported-writers + individual-writers
;    */
;    /* TODO: Fixup custom filter. */
;    /*custom = custom-filter
;    if custom.contains("supported", "CaseInsensitive") { */
;        /* This will hide it. */ /*
;        custom = ""
;    }
;    elif ! custom.contains("*", "CaseInsensitive") { */
;        /* This will hide it. */ /*
;        custom = ""
;    }
;    else {
;        custom = "Custom Filter(" + custom + ");;"
;    }

;    return translate(custom + supported + all); */
)

(define ()
;floating-changed-toolbar(int isFloating)
;    /* tb = sender()
;    if (tb) {
;        if (isFloating) { */
;            /* #TODO: Determine best suited close button on various platforms.
;            #Style-SP-DockWidgetCloseButton
;            #Style-SP-TitleBarCloseButton
;            #Style-SP-DialogCloseButton */
;/*
;            ACTION = Action(tb.style().standard-icon;("Style-SP-DialogCloseButton"), "Close", self)
;            ACTION.set-status-tip("Close the " + tb.window-title() + " Toolbar")
;            ACTION.set-object-name("toolbarclose")
;            tb.add-action(ACTION)
;            #connect(tb, SIGNAL(actionTriggered()), self, SLOT(close-toolbar()))
;        }
;        else {
;            for (action in tb.actions()) {
;                if (action.object-name() == "toolbarclose") {
;                    tb.remove-action(action)
;                    #disconnect(tb, SIGNAL(actionTriggered()), self, SLOT(close-toolbar()))
;                    del action
;                }
;            }
;        }
;    } */
)


;/*
; * Build the classic UI dropdown menus using the layout defined
; * on file in our 'layout.json'.
; */
(define ()
;build-menu-bar(void)
;    (debug-message "build-menu-bar")
;    /*
;    menu-layout = menu-bar
;    menu-bar = tk.Menu(root)
;    for (menu in menu-layout-order) {
;        (debug-message menu)
;        menu- = tk.Menu(menu-bar, tearoff=0)
;        for (item in menu-layout[menu]-order) {
;            (debug-message item)
;            cmd = menu-layout[menu][item]
;            menu-.add-command(
;                label=translate(item),
;                command=lambda: actuator(cmd)
;            )
;        }
;        menu-bar.add-cascade(label=translate(menu), menu=menu-)
;    }
;    root.config(menu=menu-bar)
;    */
)

;/*
; * Create the toolbars in the order given by the "order" list.
; */
(define ()
;build-button-grid(void)
;    (debug-message "build-buttongrid")
;    /* button-layout = toolbar
;    for (toolbar in button-layout-order) {
;        (debug-message toolbar)
;        for (button in button-layout[toolbar]-order) {
;            (debug-message button)
;            B = button-layout[toolbar][button]
;            tkimg[button] = load-image(B-icon)
;            button = tk.Button(
;                root,
;                command=lambda: actuator(B-command),
;                image=tkimg[button]
;            )
;            button.grid(row=B-row, column=B-column)
;        }
;    }
;    */
)

(define ()
;application-event(SDL-Event event)
;    /*
;    if (event.type() == FileOpen) {
;        open-files-selected(event.file())
;        return 1
;    }
;    Fall through
;    return application-event(event)
;    */
)


(define ()
;mdi-area-init(MdiArea *area)
;    area->tabs-closeable = 1
;    area->use-logo = 0
;    area->use-texture = 0
;    area->use-color = 0
;    area->bg-logo = 0
;    area->bg-texture = 0
;    area->bg-color = 0
)

(define ()
;mdi-area-use-background-logo(MdiArea *area, int use)
;    area->use-logo = use
;    /* force-repaint(); */
)

(define ()
;mdi-area-use-background-texture(MdiArea *area, int use)
;    area->use-texture = use
;    /* force-repaint(); */
)

(define ()
;mdi-area-use-background-color(MdiArea *area, int use)
;    area->use-color = use
;    /* force-repaint(); */
)

(define ()
;mdi-area-set-background-logo(MdiArea *area, char *file-name)
;    /*
;    bg-logo.load(file-name)
;    force-repaint()
;    */
)

(define ()
;mdi-area-set-background-texture(MdiArea *area, char *file-name)
;    /*
;    bg-texture.load(file-name)
;    force-repaint()
;    */
)

(define ()
;mdi-area-set-background-color(MdiArea *area, EmbColor color)
;    /*
;    if (!color.is-valid()) {
;        bg-color = background().color()
;    }
;    else {
;        bg-color = color
;    }

;    force-repaint()
;    */
)

(define ()
;mdi-area-mouse-double-click-event(MdiArea *area, SDL-Event e)
;    /*
;    mw.open-file-action()
;    */
)

(define ()
;mdi-area-paint-event(MdiArea *area, SDL-Event e)
;    /* vport = viewport()
;    rect = vport.rect()

;    painter = Painter(vport)
;    painter.setRenderHint(QPainter-SmoothPixmapTransform); */

;    /* Always fill with a solid color first. */
;    /* if (use-color) {
;        painter.fillRect(rect, bg-color)
;    }
;    else {
;        painter.fillRect(rect, background())
;    } */

;    /* Then overlay the texture. */
;    /* if (use-texture) {
;        bgBrush = QBrush(bg-texture)
;        painter.fillRect(rect, bgBrush)
;    } */

;    /* Overlay the logo last. */
;    /* if (use-logo) { */
;        /* Center the pixmap */
;        /* dx = (rect.width()-bg-logo.width())/2
;        dy = (rect.height()-bg-logo.height())/2
;        painter.drawPixmap(dx, dy, bg-logo.width(), bg-logo.height(), bg-logo)
;    } */
)

(define ()
;mdi-area-cascade(void)
;    /*
;    cascadeSubWindows()
;    zoom-extents-actionAllSubWindows()
;    */
)

(define (mdi-area-tile)
;    tileSubWindows()
;    zoom-extents-actionAllSubWindows()
)

(define (mdi-area-zoom-extents-actionAllSubWindows)
;    for (window in subWindowList()) {
;        if (window) {
;            v = window.getView()
;            if (v) {
;                v.recalculateLimits()
;                v.zoom-extents-action()
;            }
;        }
;    }
)

; HACK: Take that QMdiArea!
(define (mdi-area-force-repaint)
;    hack = size()
;    resize(hack + QSize(1,1))
;    resize(hack)
)

; NOTE: This function should be used to interpret various
; object types and save them as polylines for stitchOnly formats.
;
(define ()
;to-polyline(
;    EmbPattern *pattern,
;    EmbVector obj-pos,
;    /*
;    obj-path,
;    layer,
;    */
;    EmbColor color,
;    int line-type,
;    double line-weight)
;    /*
;    startX = obj-pos.x()
;    startY = obj-pos.y()
;    point-list = []
;    for i in range(obj-path.element-count()) {
;        element = obj-path.element-at(i)
;        a = Vector(0.0, 0.0)
;        a.point.x = element.x + startX
;        a.point.y = -(element.y + startY)
;        point-list += [a]
;    }

;    poly-object = Polyline()
;    poly-object.point-list = point-list
;    poly-object.color = color
;    poly-object.line-type = "solid"
;    pattern.add-polyline(poly-object)
)


;/*
;class MdiWindow()*/
;    /*
;    MdiWindow(theIndex, mw, parent, wflags)
;    ~MdiWindow()

;    virtual QSize  sizeHint() const

;    static void getCurrentFile()
;    static void getShortCurrentFile()
;    static void getView()
;    static void getScene()
;    static void getCurrentLayer()
;    static void getCurrentColor()
;    static void getCurrentline-type()
;    static void getCurrentline-weight()
;    static void setCurrentLayer(layer)
;    static void set-current-color(color)
;    static void setCurrentline-type(line-type)
;    static void setCurrentline-weight(line-weight)
;    static void design-details-action()
;    static void sendCloseMdiWin(MdiWindow*)

;    mwdow*    mw
;    QGraphicsScene*    gscene
;    QMdiArea*  mdiArea
;    View*  gview
;    int fileWasLoaded

;    # QPrinter printer

;    QString curFile
(define () setCurrentFile(file-name)
;    QString fileExtension(file-name)

;    int myIndex

;    QString curLayer
;    unsigned int curColor
;    QString curline-type
;    QString curline-weight

(define () closeEvent(e)
(define () mdi-onWindowActivated()
(define () mdi-currentLayerChanged(layer)
(define () mdi-currentColorChanged(color)
(define () mdi-currentline-typeChanged(type)
(define () mdi-currentline-weightChanged(weight)
(define () mdi-updateColorline-typeline-weight()
(define () mdi-showViewScrollBars(int val)
(define () mdi-setViewCrossHairColor(color)
(define () setViewBackgroundColor(color)
(define () setViewSelectBoxColors(unsigned int colorL, unsigned int fillL, unsigned int colorR, unsigned int fillR, int alpha)
(define () setViewGridColor(unsigned int color)
(define () set-view-ruler-color(unsigned int color)
(define () print()

(define () showViewScrollBars(int val)
(define () setViewCrossHairColor(color)
;        return
(define () setViewBackgroundColor(color)
;        return
(define () setViewSelectBoxColors(unsigned int colorL, unsigned int fillL, unsigned int colorR, unsigned int fillR, int alpha)
(define () setViewGridColor(unsigned int color)
(define () set-view-ruler-color(unsigned int color)

(define () print()
;    */

;/*
(define ()
;mdi-window-init(self, theIndex, mw, parent, wflags)
;    mw = mw
;    mdiArea = parent
;    myIndex = theIndex
;    fileWasLoaded = 0

;    setAttribute(Qt-WA-DeleteOnClose)

;    aName = ""
;    curFile = aName.asprintf("Untitled%d.dst", myIndex)
;    setWindowTitle(curFile)
;    setWindowIcon(QIcon("icons/app.png"))

;    gscene = QGraphicsScene(0,0,0,0, this)
;    gview = View(mw, gscene, this)

;    setWidget(gview)
)
;*/

(define ()
;load-file-action(char *file-name)
;    FILE *file
;    EmbPattern *p
;    (debug-message "MdiWindow load-file()")
;    /*
;    tmpColor = get-current-color()

;    file = open(file-name, "r")
;    if (!file) {
;        warning(translate("Error reading file"),
;                translate("Cannot read file %1:\n%2.")
;                .arg(file-name).arg(file.errorString()))
;        return 0
;    }

;    mw.set-override-cursor(Qt-WaitCursor)

;    ext = fileExtension(file-name)
;    (debug-message "ext: %s", qPrintable(ext))

;    p = embPattern-create()
;    if (!p) {
;        printf("Could not allocate memory for embroidery pattern\n")
;        exit(1)
;    }

;    if (!p.readAuto(file-name)) {
;        (debug-message "Reading file was unsuccessful: %s\n", file-name)
;        mw.restore-override-cursor()
;        message = translate("Reading file was unsuccessful: ") + file-name
;        warning(this, translate("Error reading pattern"), message)
;    }
;    else {
;        p.move-stitch-list-to-polylines()
;        # TODO: Test more
;        stitchCount = p.stitch-list.count
;        path = Path()

;        if (p.circles) {
;            for i in range(len(p.circles))
;                c = p.circles.circle[i].circle
;                this-color = p.circles.circle[i].color
;                set-current-color(qRgb(this-color.r, this-color.g, this-color.b))
;                # NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed.
;                mw.nativeAddCircle(c.center.x, c.center.y, c.radius, 0, "RUBBER-OFF")
;                # TODO: fill

;        if p.ellipses:
;            for i in range(len(p.ellipses))
;                e = p.ellipses.ellipse[i].ellipse
;                this-color = p.ellipses.ellipse[i].color
;                set-current-color(qRgb(this-color.r, this-color.g, this-color.b))
;                # NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed.
;                mw.nativeAddEllipse(e.centerX, e.centerY, e.radiusX, e.radiusY, 0, 0, OBJ-RUBBER-OFF)
;                #TODO: rotation and fill

;        if p.lines:
;            for i in range(len(p.lines))
;                li = p.lines.line[i].line
;                this-color = p.lines.line[i].color
;                set-current-color(qRgb(this-color.r, this-color.g, this-color.b))
;                # NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed.
;                mw.nativeAddLine(li.start.x, li.start.y, li.end.x, li.end.y, 0, OBJ-RUBBER-OFF)
;                #TODO: rotation

;        if p.paths:
;            # TODO: This is unfinished. It needs more work
;            for i in range(p.paths.count)
;                curpoint-list = p.paths.path[i].point-list
;                pathPath = Path()
;                this-color = p.paths.path[i].color
;                if curpoint-list.count > 0:
;                    pp = curpoint-list[0].point.point
;                    pathPath.move-to(pp.x, -pp.y)
;                    #NOTE: Qt Y+ is down and libembroidery Y+ is up, so inverting the Y is needed.

;                for j in range(curpoint-list.count)
;                    pp = curpoint-list[j].point.point
;                    pathPath.line-to(pp.x, -pp.y)
;                    #NOTE: Qt Y+ is down and libembroidery Y+ is up, so inverting the Y is needed.

;                loadPen = Pen(qRgb(this-color.r, this-color.g, this-color.b))
;                loadPen.set-widthF(0.35)
;                loadPen.set-cap-style(Qt-RoundCap)
;                loadPen.set-join-style(Qt-RoundJoin)

;                obj = Path(0, 0, pathPath, loadPen.color().rgb())
;                item.setObjectRubberMode(OBJ-RUBBER-OFF)
;                mw.activeScene().addItem(obj)

;        if p.points:
;            for i in range(p.points.count)
;                po = p.points.point[i].point
;                this-color = p.points.point[i].color
;                set-current-color(qRgb(this-color.r, this-color.g, this-color.b))
;                # NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed.
;                mw.nativeAddPoint(po.x, po.y)

;        if p.polygons:
;            for i in range(p.polygons.count)
;                curpoint-list = p.polygons.polygon[i].point-list
;                polygonPath = Path()
;                firstPo= 0
;                startX = 0
;                startY = 0
;                x = 0
;                y = 0
;                this-color = p.polygons.polygon[i].color
;                set-current-color(qRgb(this-color.r, this-color.g, this-color.b))
;                for j in range(curpoint-list.count)
;                    pp = curpoint-list.point[j].point
;                    x = pp.x
;                    y = -pp.y
;                    #NOTE: Qt Y+ is down and libembroidery Y+ is up, so inverting the Y is needed.

;                    if first-point:
;                        polygonPath.lineTo(x,y)
;                    else {
;                        polygonPath.move-to(x,y)
;                        firstPo= 1
;                        startX = x
;                        startY = y

;                polygonPath.translate(-startX, -startY)
;                mw.nativeAddPolygon(startX, startY, polygonPath, OBJ-RUBBER-OFF)

;        # NOTE: Polylines should only contain NORMAL stitches.
;        if p.polylines:
;            for i in range(len(p.polylines))
;                curpoint-list = p.polylines.polyline[i].point-list
;                polylinePath = Path()
;                firstPo = 0
;                startX = 0
;                startY = 0
;                x = 0
;                y = 0
;                this-color = p.polylines.polyline[i].color
;                set-current-color(qRgb(this-color.r, this-color.g, this-color.b))
;                for j in range(curpoint-list.count)
;                    pp = curpoint-list.point[j].point
;                    x = pp.x
;                    y = -pp.y
;                    # NOTE: Qt Y+ is down and libembroidery Y+ is up, so inverting the Y is needed.
;                    if first-point:
;                        polylinePath.line-to(x,y)
;                    else {
;                        polylinePath.move-to(x,y)
;                        firstPo= 1
;                        startX = x
;                        startY = y

;                polylinePath.translate(-startX, -startY)
;                mw.nativeAddPolyline(startX, startY, polylinePath, OBJ-RUBBER-OFF)

;        if p.rects:
;            for i in range(len(p.rects))
;                r = p.rects.rect[i].rect
;                this-color = p.rects.rect[i].color
;                set-current-color(qRgb(this-color.r, this-color.g, this-color.b))
;                # NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed.
;                mw.nativeAddRectangle(embRect-x(r), embRect-y(r), embRect-width(r), embRect-height(r), 0, 0, OBJ-RUBBER-OFF)
;                # TODO: rotation and fill

;        set-current-file(file-name)
;        mw.statusbar.showMessage("File loaded.")
;        stitches = ""
;        stitches.setNum(stitchCount)

;        if grid-load-from-file:
;            #TODO: Josh, provide me a hoop size and/or grid spacing from the pattern.
;            (debug-message ".")

;        mw.restore-override-cursor()

;    p.free()

;    # Clear the undo stack so it is not possible to undo past this point.
;    undo-history-length = 0

;    set-current-color(tmpColor)
;    return 1
;    */
)


(define ()
;set-current-file(char *file-name)
;    /*
;    curFile = QFileInfo(file-name).canonicalFilePath()
;    setWindowModified(0)
;    setWindowTitle(getShortCurrentFile())
;    */
)

(define ()
;get-short-current-file(void)
;    /*
;    return QFileInfo(curFile).file-name(); */
)

(define ()
;file-extension(char *file-name)
;    /*
;    return QFileInfo(file-name).suffix().toLower()
;    */
)

(define ()
;on-window-activated(void/* mdi-window *subwindow */)
;    (debug-message "MdiWindow onWindowActivated()")
;    /*
;    mdi-win = w.mdi-window()
;    if (mdi-win) {
;        mdi-win.on-window-activated()
;    }
;    status-bar-SNAP.setChecked(gscene.property("ENABLE-SNAP"))
;    status-bar-GRID.setChecked(gscene.property("ENABLE-GRID"))
;    status-bar-RULER.setChecked(gscene.property("ENABLE-RULER"))
;    status-bar[STATUS-ORTHO].setChecked(gscene.property("ENABLE-ORTHO"))
;    status-bar[STATUS-POLAR].setChecked(gscene.property("ENABLE-POLAR"))
;    status-bar[STATUS-QSNAP].setChecked(gscene.property("ENABLE-QSNAP"))
;    status-bar[STATUS-QTRACK].setChecked(gscene.property("ENABLE-QTRACK"))
;    status-bar[STATUS-LWT].setChecked(gscene.property("ENABLE-LWT"))
;    #mw.prompt.setHistory(promptHistory)
;    */
)

(define ()
;sizeHint()
;    /*
;    (debug-message "MdiWindow sizeHint()")
;    return QSize(450, 300)
;    */
)

(define ()
;current-layer-changed(/*layer */)
;    /* curLayer = layer; */
)

(define ()
;current-color-changed(EmbColor color)
;    /*
;    curColor = color
;    */
)

(define ()
;current-line-type-changed(int type)
;     /*
;    curline-type = type
;    */
)

(define ()
;current-line-weight-changed(double weight)
;    /*
;    curline-weight = weight
;    */
)

(define ()
;update-color-line-type-line-weight(void)
;     /*
;    (debug-message "update color line type weight")
;    */
)

(define ()
;show-view-scroll-bars(double val)
;    /* gview.showScrollBars(val); */
)

(define ()
;set-view-cross-hair-color(EmbColor color)
;    /* gview.setCrossHairColor(color); */
)

(define ()
;set-view-background-color(EmbColor color)
;    /* gview.setBackgroundColor(color); */
)

(define ()
;set-view-select-box-colors(
;    EmbColor colorL,
;    EmbColor fillL,
;    EmbColor colorR,
;    EmbColor fillR,
;    double alpha
;)
;     /* gview.setSelectBoxColors(colorL, fillL, colorR, fillR, alpha); */
)

(define ()
;set-view-grid-color(EmbColor color)
;    /* gview.setGridColor(color); */
)

(define ()
;set-view-ruler-color(EmbColor color)
;    /* gview.setRulerColor(color); */
)

;/*
; *  Property editor.
; *  Uses the configuration to define what data should be presented
; *  to the user and what can be edited by the user.
; *
; * for toolbars: modify and draw. Inquiry toolbar?
; *
; * TODO: associate the property editor with the function callbacks using
; * a function pointer.
; *
; */

;/*
;# property-editor-row property-editors[] = {

;class PropertyEditor()
;  */  /*
;    PropertyEditor(iconDirectory = "", int pickAddMode = 1, QWidget* widgetToFocus = 0, QWidget* parent = 0, Qt-WindowFlags flags = Qt-Widget)
;    ~PropertyEditor()

;    QGroupBox* creategroup-box-geometry(int obj-type)
;    QGroupBox*   createGroupBoxMiscImage()
;    QGroupBox*   createGroupBoxGeneral()
;    QGroupBox*   createGroupBoxMiscArc()
;    QGroupBox*   createGroupBoxMiscPath()
;    QGroupBox*   createGroupBoxMiscPolyline()
;    QGroupBox*   createGroupBoxTextTextSingle()
;    QGroupBox*   createGroupBoxMiscTextSingle()

;    QWidget* focusWidget

;    QString  iconDir
;    int  iconSize
;    Qt-ToolButtonStyle propertyEditorButtonStyle

;    int pickAdd

;    QList<QGraphicsItem*> selectedItemList

;    #Helper functions
;    QToolButton*   createToolButton(const QString& iconName, const QString& txt)
;    QLineEdit* createLineEdit(const QString& validatorType = "", int readOnly = false)
;    QComboBox* create-combo-box(int disable = false)
;    Qfont-combo-box* createfont-combo-box(int disable = false)

(define ()
;updateLineEditStrIfVaries(QLineEdit* lineEdit, const QString& str)

(define ()
;updateLineEditNumIfVaries(QLineEdit* lineEdit, num, int useAnglePrecision)

(define ()
;updatefont-combo-boxStrIfVaries(Qfont-combo-box* font-combo-box, const QString& str)

(define ()
;updateComboBoxStrIfVaries(QComboBox* comboBox, const QString& str, const QStringList& strList)

(define ()
;updateComboBoxintIfVaries(QComboBox* comboBox, int val, int yesOrNoText)

;    QSignalMapper* signalMapper
(define ()
;mapSignal(QObject* fieldObj, const QString& name, QVariant value)

;    QComboBox*   create-combo-boxSelected()
;    QToolButton* createToolButtonQSelect()
;    QToolButton* createToolButtonPickAdd()

;    #TODO: Alphabetic/Categorized TabWidget
;    bool eventFilter(QObject *obj, QEvent *event)

(define ()
;pickAddModeToggled()

(define ()
;setSelectedItems(QList<QGraphicsItem*> itemList)

(define ()
;updatePickAddModeButton(int pickAddMode)

(define ()
;fieldEdited(QObject* fieldObj)

(define ()
;showGroups(int obj-type)

(define ()
;showOneType(int index)

(define ()
;hideAllGroups()

(define ()
;clear-all-fields()

(define ()
;togglePickAddMode(

;*/
;/*
(define ()
;property-editor-init(self, iconDirectory, pickAddMode, widgetToFocus, parent, flags)
;{ */
;    /* . */ /*
;    iconDir = iconDirectory
;    iconSize = 16
;    propertyEditorButtonStyle = Qt-button-TextBesideIcon; */
;    /* TODO: Make customizable. */ /*
;    setMinimumSize(100,100)

;    pickAdd = pickAddMode

;    precisionAngle = 0; */
;    /* TODO: Load this from settings and provide function for updating from settings */ /*
;    precisionLength = 4
;    # TODO: Load this from settings and provide function for updating from settings

;    signalMapper = tk.SignalMapper(root)

;    field-old-text = ""
;    field-new-text = ""
;    field-varies-text = "*Varies*"
;    fieldYesText = "Yes"
;    fieldNoText = "No"
;    fieldOnText = "On"
;    fieldOffText = "Off"

;    widgetMain = tk.Widget(root)

;    widgetSelection = tk.Widget(root)
;    hboxLayoutSelection = tk.HBoxLayout(this)
;    hboxLayoutSelection.add-widget(create-combo-boxSelected())
;    hboxLayoutSelection.add-widget(createbutton-QSelect())
;    hboxLayoutSelection.add-widget(createbutton-PickAdd())
;    widgetSelection.setLayout(hboxLayoutSelection)

;    for i in range(1, UNKNOWN-BASE)
;        group-box-geometry[i] = creategroup-box-geometry(i+BASE)

;    scrollProperties = QScrollArea(this)
;    widgetProperties = QWidget(this)
;    vboxLayoutProperties = QVBoxLayout(this)
;    vboxLayoutProperties.add-widget(createGroupBoxGeneral())
;    for i in range(1, UNKNOWN-BASE)
;        vboxLayoutProperties.add-widget(group-box-geometry[i+BASE])

;    vboxLayoutProperties.add-widget(createGroupBoxMiscArc())
;    vboxLayoutProperties.add-widget(createGroupBoxMiscImage())
;    vboxLayoutProperties.add-widget(createGroupBoxMiscPath())
;    vboxLayoutProperties.add-widget(createGroupBoxMiscPolyline())
;    vboxLayoutProperties.add-widget(createGroupBoxTextTextSingle())
;    vboxLayoutProperties.add-widget(createGroupBoxMiscTextSingle())
;    vboxLayoutProperties.addStretch(1)
;    widgetProperties.setLayout(vboxLayoutProperties)
;    scrollProperties.setWidget(widgetProperties)
;    scrollProperties.setWidgetResizable(1)

;    vboxLayoutMain = QVBoxLayout(this)
;    vboxLayoutMain.add-widget(widgetSelection)
;    vboxLayoutMain.add-widget(scrollProperties)
;    widgetMain.setLayout(vboxLayoutMain)

;    setWidget(widgetMain)
;    setWindowTitle(translate("Properties"))
;    setAllowedAreas(Qt-LeftDockWidgetArea | Qt-RightDockWidgetArea)

;    hideAllGroups()

;    connect(signalMapper, SIGNAL(mapped()), this, SLOT(fieldEdited()))

;    focusWidget = widgetToFocus
;    this.installEventFilter(this)
)
;*/

(define ()
;create-group-box(int data)
;    /*
;    for (i=0; ; i++) {
;        button = create-tool-button("blank", translate(label[i]))
;        edit = create-line-edit("double", 0)
;        add-to-form(button, edit)
;    }
;    */
)

(define ()
;event-filter(int obj, SDL-Event event)
;    /*
;    if (event.type() == "KeyPress") {
;        key = event.key()
;        if (Qt-Key-Escape) {
;            if focusWidget:
;                focusWidget.setFocus(Qt-OtherFocusReason)
;            return 1
;        }
;        else {
;            event.ignore()
;        }
;    }
;    return QObject-eventFilter(obj, event)
;    */
)

(define ()
;create-combo-box-selected(void)
;    /*
;    comboBoxSelected = tk.ComboBox(this)
;    comboBoxSelected.addItem(translate("No Selection"))
;    return comboBoxSelected
;    */
)

(define ()
;createbutton-QSelect(void)
;    /*
;    button-QSelect = tk.Button-(this)
;    button-QSelect.setIcon(load-icon(quickselect-xpm))
;    button-QSelect.setIconSize(QSize(iconSize, iconSize))
;    button-QSelect.setText("QSelect")
;    button-QSelect.setToolTip("QSelect"); #TODO: Better Description
;    button-QSelect.setbutton-Style(Qt-button-IconOnly)
;    return button-QSelect
;    */
)

(define ()
;createbutton-PickAdd(void)
;/*
;    #TODO: Set as PickAdd or PickNew based on settings
;    button-PickAdd = Qbutton-(this)
;    updatePickAddModeButton(pickAdd)
;    connect(button-PickAdd, SIGNAL(clicked(int)), this, SLOT(togglePickAddMode()))
;    return button-PickAdd */
)

(define ()
;updatePickAddModeButton(int pickAddMode)
;/*
;    pickAdd = pickAddMode
;    if (pickAdd)
;        button-PickAdd.setIcon(load-icon(pickadd-xpm))
;        button-PickAdd.setIconSize(QSize(iconSize, iconSize))
;        button-PickAdd.setText("PickAdd")
;        button-PickAdd.setToolTip("PickAdd Mode - Add to current selection.\nClick to switch to PickNew Mode.")
;        button-PickAdd.setbutton-Style(Qt-button-IconOnly)

;    else {
;        button-PickAdd.setIcon(load-icon(picknew-xpm))
;        button-PickAdd.setIconSize(QSize(iconSize, iconSize))
;        button-PickAdd.setText("PickNew")
;        button-PickAdd.setToolTip("PickNew Mode - Replace current selection.\nClick to switch to PickAdd Mode.")
;        button-PickAdd.setbutton-Style(Qt-button-IconOnly)
;        */
)

(define ()
;toggle-pick-add-mode(void)
;/*
;    #emit pickAddModeToggled()
;    (debug-message "not sure how to deal with emit yet")
)

(define ()
;set-selected-items(int *itemList)
;/*
;    selectedItemList = itemList
;    #Hide all the groups initially, then decide which ones to show
;    hideAllGroups()
;    comboBoxSelected.clear()

;    if itemList.isEmpty()
;        comboBoxSelected.addItem(translate("No Selection"))
;        return

;    typeSet = {}
;    numAll = itemList.size()
;    numObjects = [0 for i in range(31)]
;    numTypes = 0

;    for item in itemList:
;        if (!item:
;            continue

;        obj-type = item.type()
;        typeSet.insert(obj-type)

;        if obj-type > BASE and obj-type < UNKNOWN:
;            if numObjects[obj-type-BASE] == 0:
;                numTypes += 1
;            numObjects[obj-type-BASE] += 1
;        else {
;            numObjects[UNKNOWN-BASE] += 1
;*/
;    /* Populate the selection comboBox
;     * ==================================================
;     */ /*
;    if numTypes > 1:
;        comboBoxSelected.addItem(translate("Varies") + " (" + "".setNum(numAll) + ")")
;        connect(comboBoxSelected, SIGNAL(currentIndexChanged(int)), this, SLOT(showOneType(int)))

;    for (i=0; i<31; i++) {
;        if (numObjects[i] > 0) {
;            combo-box-str = translate(obj-names[i])
;            combo-box-str += " (" + "".setNum(numObjects[i]) + ")"
;            comboBoxSelected.addItem(combo-box-str, BASE+i)
;        }
;    } */

;    /* Load Data into the fields
;     * ==================================================
;     * Clear fields first so if the selected data varies,
;     * the comparison is simple.
;     */ /*
;    clear-all-fields()

;    for item in itemList:
;        if (!item:
;            continue

;        # TODO: load data into the General field
;        if item.type == "Arc":
;            p = obj.objectCenter()
;            update-edit-NumIfVaries(edit-[ARC-CENTER-X], p.x(), 0)
;            update-edit-NumIfVaries(edit-[ARC-CENTER-Y], -p.y(), 0)
;            update-edit-NumIfVaries(edit-[ARC-RADIUS], obj.objectRadius(), 0)
;            update-edit-NumIfVaries(edit-[ARC-START-ANGLE], obj.objectStartAngle(), 1)
;            update-edit-NumIfVaries(edit-[ARC-END-ANGLE], obj.objectEndAngle(), 1)
;            update-edit-NumIfVaries(edit-[ARC-START-X], obj.objectStartPoint().x(), 0)
;            update-edit-NumIfVaries(edit-[ARC-START-Y], -obj.objectStartPoint().y(), 0)
;            update-edit-NumIfVaries(edit-[ARC-END-X], obj.objectEndPoint().x(), 0)
;            update-edit-NumIfVaries(edit-[ARC-END-Y], -obj.objectEndPoint().y(), 0)
;            update-edit-NumIfVaries(edit-[ARC-AREA], obj.objectArea(), 0)
;            update-edit-NumIfVaries(edit-[ARC-LENGTH], obj.objectArcLength(), 0)
;            update-edit-NumIfVaries(edit-[ARC-CHORD], obj.objectChord(), 0)
;            update-edit-NumIfVaries(edit-[ARC-INC-ANGLE], obj.objectIncludedAngle(), 1)
;            updateComboBoxintIfVaries(comboBox[ARC-CLOCKWISE], obj.objectClockwise(), 1)

;        elif item.type == "Block":
;            (debug-message "TODO: load block data")

;        elif item.type == "Circle":
;            p = obj.objectCenter()
;            update-edit-NumIfVaries(edit-[CIRCLE-CENTER-X], p.x(), 0)
;            update-edit-NumIfVaries(edit-[CIRCLE-CENTER-Y], -p.y(), 0)
;            update-edit-NumIfVaries(edit-[CIRCLE-RADIUS], obj.objectRadius(), 0)
;            update-edit-NumIfVaries(edit-[CIRCLE-DIAMETER], obj.objectDiameter(), 0)
;            update-edit-NumIfVaries(edit-[CIRCLE-AREA], obj.objectArea(), 0)
;            update-edit-NumIfVaries(edit-[CIRCLE-CIRCUMFERENCE], obj.objectCircumference(), 0)

;        elif item.type == "DimAligned":
;            (debug-message "TODO: load aligned dimension data")

;        elif item.type == "DimAngular":
;            (debug-message "TODO: load angular dimension data")

;        elif item.type == "DimArcLength":
;            (debug-message "TODO: load arclength dimension data")

;        elif item.type == DIMDIAMETER:
;            (debug-message "TODO: load diameter dimension data")

;        elif item.type == DIMLEADER:
;            (debug-message "TODO: load leader dimension data")

;        elif item.type == DIMLINEAR:
;            (debug-message "TODO: load linear dimension data")

;        elif item.type == DIMORDINATE:
;            (debug-message "TODO: load ordinate dimension data")

;        elif item.type == "DimRadius":
;            (debug-message "TODO: load radius dimension data")

;        elif item.type == "Ellipse":
;            p = obj.objectCenter()
;            update-edit-NumIfVaries(edit-[ELLIPSE-CENTER-X], p.x(), 0)
;            update-edit-NumIfVaries(edit-[ELLIPSE-CENTER-Y], -p.y(), 0)
;            update-edit-NumIfVaries(edit-[ELLIPSE-RADIUS-MAJOR], obj.objectRadiusMajor(), 0)
;            update-edit-NumIfVaries(edit-[ELLIPSE-RADIUS-MINOR], obj.objectRadiusMinor(), 0)
;            update-edit-NumIfVaries(edit-[ELLIPSE-DIAMETER-MAJOR], obj.objectDiameterMajor(), 0)
;            update-edit-NumIfVaries(edit-[ELLIPSE-DIAMETER-MINOR], obj.objectDiameterMinor(), 0)

;        elif item.type == "Image":
;            (debug-message "TODO: load image data")

;        elif item.type == "Infinite Line":
;            (debug-message "TODO: load infinite line data")

;        elif item.type == "Line":
;            update-edit-NumIfVaries(edit-[LINE-START-X], obj.objectEndPoint1().x(), 0)
;            update-edit-NumIfVaries(edit-[LINE-START-Y], -obj.objectEndPoint1().y(), 0)
;            update-edit-NumIfVaries(edit-[LINE-END-X], obj.objectEndPoint2().x(), 0)
;            update-edit-NumIfVaries(edit-[LINE-END-Y], -obj.objectEndPoint2().y(), 0)
;            update-edit-NumIfVaries(edit-[LINE-DELTA-X], obj.objectDeltaX(), 0)
;            update-edit-NumIfVaries(edit-[LINE-DELTA-Y], -obj.objectDeltaY(), 0)
;            update-edit-NumIfVaries(edit-[LINE-ANGLE], obj.objectAngle(), 1)
;            update-edit-NumIfVaries(edit-[LINE-LENGTH], obj.objectLength(), 0)

;        elif item.type == "Path":
;            (debug-message ".")

;        elif item.type == "Point":
;            update-edit-NumIfVaries(edit-[POINT-X], obj.objectX(), 0)
;            update-edit-NumIfVaries(edit-[POINT-Y], -obj.objectY(), 0)

;        elif item.type == "Polygon":
;            (debug-message ".")

;        elif item.type == "Polyline":
;            (debug-message ".")

;        elif item.type == "Ray":
;            (debug-message ".")

;        elif item.type == RECTANGLE:
;            corn1 = obj.objectTopLeft()
;            corn2 = obj.objectTopRight()
;            corn3 = obj.objectBottomLeft()
;            corn4 = obj.objectBottomRight()

;            update-edit-NumIfVaries(edit-[RECT-CORNER-X1], corn1.x(), 0)
;            update-edit-NumIfVaries(edit-[RECT-CORNER-Y1], -corn1.y(), 0)
;            update-edit-NumIfVaries(edit-[RECT-CORNER-X2], corn2.x(), 0)
;            update-edit-NumIfVaries(edit-[RECT-CORNER-Y2], -corn2.y(), 0)
;            update-edit-NumIfVaries(edit-[RECT-CORNER-X3], corn3.x(), 0)
;            update-edit-NumIfVaries(edit-[RECT-CORNER-Y3], -corn3.y(), 0)
;            update-edit-NumIfVaries(edit-[RECT-CORNER-X4], corn4.x(), 0)
;            update-edit-NumIfVaries(edit-[RECT-CORNER-Y4], -corn4.y(), 0)
;            update-edit-NumIfVaries(edit-[RECT-WIDTH], obj.objectWidth(), 0)
;            update-edit-NumIfVaries(edit-[RECT-HEIGHT], -obj.objectHeight(), 0)
;            update-edit-NumIfVaries(edit-[RECT-AREA], obj.objectArea(), 0)

;        elif item.type == TEXTMULTI:
;            (debug-message ".")

;        elif item.type == TEXTSINGLE:
;            update-edit-StrIfVaries(edit-TextSingleContents, obj.objText)
;            updatefont-combo-boxStrIfVaries(comboBoxTextSingleFont, obj.objTextFont)
;            updateComboBoxStrIfVaries(comboBoxTextSingleJustify, obj.objTextJustify, obj.objectTextJustifyList())
;            update-edit-NumIfVaries(edit-TextSingleHeight, obj.obj-text.size, 0)
;            update-edit-NumIfVaries(edit-TextSingleRotation, -obj.rotation(), 1)
;            update-edit-NumIfVaries(edit-TextSingleX, obj.objectX(), 0)
;            update-edit-NumIfVaries(edit-TextSingleY, -obj.objectY(), 0)
;            updateComboBoxintIfVaries(comboBoxTextSingleBackward, obj.obj-text.backward, 1)
;            updateComboBoxintIfVaries(comboBoxTextSingleUpsideDown, obj.obj-text.upsidedown, 1)

;    # Only show fields if all objects are the same type
;    #==================================================
;    if numTypes == 1:
;        for obj-type in typeSet:
;            showGroups(obj-type)
;            */
)

(define ()
;update-edit-StrIfVaries(int edit-, char *str)
;/*
;    field-old-text = edit-.text()
;    field-new-text = str

;    if field-old-text.isEmpty()
;        edit-.setText(field-new-text)
;    elif field-old-text != field-new-text:
;        edit-.setText(field-varies-text)
;        */
)

(define ()
;update-edit-NumIfVaries(int edit-, int num, int useAnglePrecision)
;/*
;    precision = 0
;    if useAnglePrecision:
;        precision = precisionAngle
;    else {
;        precision = precisionLength

;    field-old-text = edit-.text()
;    field-new-text.setNum(num, 'f', precision)

;    # Prevent negative zero :D
;    negative-zero = "-0."
;    for i in range(precision)
;        negative-zero += '0'
;    if field-new-text == negative-zero:
;        field-new-text = negative-zero.replace("-", "")

;    if field-old-text.isEmpty()
;        edit-.setText(field-new-text)
;    elif field-old-text != field-new-text:
;        edit-.setText(field-varies-text)*/
)

;/*
(define ()
;updatefont-combo-boxStrIfVaries(self, font-combo-box, str)
;    field-old-text = font-combo-box.property("FontFamily").toString()
;    field-new-text = str
;    #(debug-message "old: %d %s, new: %d %s", oldIndex, qPrintable(font-combo-box.currentText()), newIndex, qPrintable(str))
;    if field-old-text.isEmpty()
;        font-combo-box.setCurrentFont(QFont(field-new-text))
;        font-combo-box.setProperty("FontFamily", field-new-text)
;    elif field-old-text != field-new-text:
;        if font-combo-box.findText(field-varies-text) == -1:
;            # Prevent multiple entries
;            font-combo-box.addItem(field-varies-text)
;        font-combo-box.setCurrentIndex(font-combo-box.findText(field-varies-text))
)

(define ()
;updateComboBoxStrIfVaries(self, comboBox, str, strList)
;    field-old-text = comboBox.currentText()
;    field-new-text = str

;    if field-old-text.isEmpty()
;        for s in strList:
;            comboBox.addItem(s, s)
;        comboBox.setCurrentIndex(comboBox.findText(field-new-text))

;    elif field-old-text != field-new-text:
;        if comboBox.findText(field-varies-text) == -1:
;            # Prevent multiple entries
;            comboBox.addItem(field-varies-text)
;        comboBox.setCurrentIndex(comboBox.findText(field-varies-text))
)

(define (update-combo-box-int-if-varies)
;(self, comboBox, val, yesOrNoText)
;    field-old-text = comboBox.currentText()
;    if yesOrNoText:
;        if val:
;            field-new-text = fieldYesText
;        else {
;            field-new-text = fieldNoText

;    else {
;        if val:
;            field-new-text = fieldOnText
;        else {
;            field-new-text = fieldOffText

;    if field-old-text.isEmpty()
;        if yesOrNoText:
;            comboBox.addItem(fieldYesText, 1)
;            comboBox.addItem(fieldNoText, 0)

;        else {
;            comboBox.addItem(fieldOnText, 1)
;            comboBox.addItem(fieldOffText, 0)

;        comboBox.setCurrentIndex(comboBox.findText(field-new-text))

;    elif field-old-text != field-new-text:
;        # Prevent multiple entries
;        if comboBox.findText(field-varies-text) == -1:
;            comboBox.addItem(field-varies-text)
;        comboBox.setCurrentIndex(comboBox.findText(field-varies-text))
)

(define ()
;showGroups(self, obj-type)
;    if (obj-type in obj-types) {
;        group-box-geometry[obj-type-BASE].show()
;    }
;    if obj-type == "Arc":
;        groupBoxMiscArc.show()
;    elif obj-type == "Image":
;        groupBoxMiscImage.show()
;    elif obj-type == "PATH":
;        groupBoxMiscPath.show()
;    elif obj-type == "POLYLINE":
;        groupBoxMiscPolyline.show()
;    elif obj-type == "Text Single":
;        groupBoxTextTextSingle.show()
;        groupBoxMiscTextSingle.show()
)

(define (show-one-type self index)
;    (hide-all-groups)
;    showGroups(comboBoxSelected.itemData(index).toInt())
)

; NOTE: General group will never be hidden.
;
(define (hide-all-groups)
;    for i in obj-types:
;        group-box-geometry[i].hide()
;    groupBoxMiscArc.hide()
;    groupBoxMiscImage.hide()
;    groupBoxMiscPath.hide()
;    groupBoxMiscPolyline.hide()
;    groupBoxTextTextSingle.hide()
;    groupBoxMiscTextSingle.hide()
)

(define (clear-all-fields)
;    for i in range(COMBOBOX-PROPERTY-EDITORS) {
;        comboBox[i].clear()
;    }
;    for i in range(edit--PROPERTY-EDITORS) {
;        edit-[i].clear()
;    }
     ; Text Single
;    comboBoxTextSingleFont.removeItem(comboBoxTextSingleFont.findText(field-varies-text))
;    # NOTE: Do not clear comboBoxTextSingleFont
;    comboBoxTextSingleFont.setProperty("FontFamily", "")
)


(define (create-group-box-geometry self obj-type)
;    gb = QGroupBox(translate("Geometry"), this)

;    # TODO: use proper icons
;    form-layout = tk.form-layout(this)
;    for i in obj-types:
;        if property-editors[i].object == obj-type:
;            index = property-editors[i].id
;            button-[index] = createbutton-(property-editors[i].icon, translate(property-editors[i].label))
;            edit-[index] = createedit-(property-editors[i].type, property-editors[i].read-only)
;            form-layout.add-row(button-[index], edit-[index])
;            mapSignal(edit-[index], property-editors[i].signal, obj-type)

;    gb.setLayout(form-layout)

;    return gb
)

(define ()
;createbutton-(self, char *iconName, char *txt)
;    tb = Qbutton-(this)
;    tb.setIcon(load-icon(blank-xpm))
;    tb.setIconSize(QSize(iconSize, iconSize))
;    tb.setText(txt)
;    tb.setbutton-Style(propertyEditorButtonStyle)
;    tb.setStyleSheet("border:none;")
;    return tb
)

(define ()
;create-edit-(int validatorType, int readOnly)
;    le = Qedit-(this)
;    if validatorType == "int":
;        le.setValidator(QIntValidator(le))
;    elif validatorType == "double":
;        le.setValidator(QDoubleValidator(le))
;    le.setReadOnly(readOnly)
;    return le
)

(define ()
;create-combo-box(self, disable)
;    cb = QComboBox(this)
;    cb.setDisabled(disable)
;    return cb
)

(define ()
;createfont-combo-box(self, disable)
;    fcb = Qfont-combo-box(this)
;    fcb.setDisabled(disable)
;    return fcb
)

(define ()
;map-signal(self, fieldObj, name, value)
;    fieldObj.setObjectName(name)
;    fieldObj.setProperty(qPrintable(name), value)

;    if name.startsWith("edit-")
;        connect(fieldObj, SIGNAL(editingFinished()), signalMapper, SLOT(map()))
;    elif name.startsWith("comboBox")
;        connect(fieldObj, SIGNAL(activated(str)), signalMapper, SLOT(map()))

;    signalMapper.setMapping(fieldObj, fieldObj)
)

(define ()
;fieldEdited(self, fieldObj)
;    blockSignals = 0
;    if blockSignals:
;        return

;    (debug-message "==========Field was Edited==========")
;    objName = fieldObj.objectName()
;    obj-type = fieldObj.property(qPrintable(objName)).toInt()

;    for item in selectedItemList:
;        if item.type() != obj-type:
;            continue

;        if item.type == "Arc":
;            if objName == "edit-ArcCenterX":
;                tempArcObj = item
;                if tempArcObj:
;                    p = tempArcObj.objectCenter()
;                    p.setX(edit-[ARC-CENTER-X].text().toDouble())
;                    tempArcObj.setPos(p)

;            if objName == "edit-ArcCenterY":
;                tempArcObj = item
;                if tempArcObj:
;                    p = tempArcObj.objectCenter()
;                    p.setY(edit-[ARC-CENTER-Y].text().toDouble())
;                    tempArcObj.setPos(p)

;            if objName == "edit-ArcRadius":
;                tempArcObj = item
;                if tempArcObj:
;                    tempArcObj.setObjectRadius(edit-[ARC-RADIUS].text().toDouble())

;            if objName == "edit-ArcStartAngle":
;                tempArcObj = item
;                if tempArcObj:
;                    tempArcObj.setObjectStartAngle(edit-[ARC-START-ANGLE].text().toDouble())

;            if objName == "edit-ArcEndAngle":
;                tempArcObj = item
;                if tempArcObj:
;                    tempArcObj.setObjectEndAngle(edit-[ARC-END-ANGLE].text().toDouble())

;        elif item.type == "Block":
;            # TODO: field editing
;            break
;        elif item.type == "Circle":
;            if objName == "edit-CircleCenterX":
;                p = item.objectCenter()
;                p.setX(edit-[CIRCLE-CENTER-X].text().toDouble())
;                item.setPos(p)

;            if objName == "edit-CircleCenterY":
;                tempCircleObj = item
;                if tempCircleObj:
;                    p = tempCircleObj.objectCenter()
;                    p.setY(edit-[CIRCLE-CENTER-Y].text().toDouble())
;                    tempCircleObj.setPos(p)

;            if objName == "edit-CircleRadius":
;                tempCircleObj = item
;                if tempCircleObj:
;                    tempCircleObj.setObjectRadius(edit-[CIRCLE-RADIUS].text().toDouble())

;            if objName == "edit-CircleDiameter":
;                tempCircleObj = item
;                if tempCircleObj:
;                    tempCircleObj.setObjectDiameter(edit-[CIRCLE-DIAMETER].text().toDouble())

;            if objName == "edit-circle-area":
;                tempCircleObj = item
;                if tempCircleObj:
;                    tempCircleObj.setObjectArea(edit-[CIRCLE-AREA].text().toDouble())
;            if objName == "edit-CircleCircumference":
;                tempCircleObj = item
;                if tempCircleObj:
;                    tempCircleObj.setObjectCircumference(edit-[CIRCLE-CIRCUMFERENCE].text().toDouble())

;            break

;        elif item.type == "DIMALIGNED":
;            # TODO: field editing
;            break

;        elif item.type == "DIMANGULAR":
;            # TODO: field editing
;            break

;        elif item.type == "DIMARCLENGTH":
;            # TODO: field editing
;            break

;        elif item.type == "DIMDIAMETER":
;            # TODO: field editing
;            break

;        elif item.type == "DIMLEADER":
;            # TODO: field editing
;            break

;        elif item.type == "DIMLINEAR": #TODO: field editing
;            break

;        elif item.type == "DIMORDINATE": #TODO: field editing
;            break

;        elif item.type == "DIMRADIUS": #TODO: field editing
;            break

;        elif item.type == "ELLIPSE":
;            if objName == "edit-ellipse-center-x":
;                p = item.center()
;                p.x = edit-[ELLIPSE-CENTER-X].text().toDouble()
;                item.setPos(p)

;            if objName == "edit-ellipseCenterY":
;                p = item.center()
;                p.y = edit-[ELLIPSE-CENTER-Y].text().toDouble()
;                item.setPos(p)

;            if objName == "edit-EllipseRadiusMajor":
;                item.setObjectRadiusMajor(edit-[ELLIPSE-RADIUS-MAJOR].text().toDouble())

;            if objName == "edit-EllipseRadiusMinor":
;                item.set-radius-minor(edit--ELLIPSE-RADIUS-MINOR.text().toDouble())

;            if objName == "edit-EllipseDiameterMajor":
;                item.setObjectDiameterMajor(edit--ELLIPSE-DIAMETER-MAJOR.text().toDouble())

;            if objName == "edit-EllipseDiameterMinor":
;                item.setObjectDiameterMinor(edit-[ELLIPSE-DIAMETER-MINOR].text().toDouble())

;            break
;        elif IMAGE: #TODO: field editing
;            break
;        elif INFINITELINE: #TODO: field editing
;            break
;        elif LINE:
;            if objName == "edit-LineStartX":
;                item.setObjectX1(edit-[LINE-START-X].text().toDouble())

;            elif objName == "edit-LineStartY":
;                item.setObjectY1(-edit-[LINE-START-Y].text().toDouble())

;            elif objName == "edit-LineEndX":
;                item.setObjectX2(edit-[LINE-END-X].text().toDouble())

;            elif objName == "edit-LineEndY":
;                item.setObjectY2(-edit-[LINE-END-Y].text().toDouble())

;        elif item.type == "PATH":
;            #TODO: field editing

;        elif item.type == "POINT":
;            if objName == "edit-PointX":
;                item.setObjectX(edit-[POINT-X].text().toDouble())

;            elif objName == "edit-PointY":
;                item.setObjectY(-edit-[POINT-Y].text().toDouble())

;        elif item.type == "POLYGON":
;            (debug-message "TYPE Polygon has no field editing")

;        elif item.type == "Polyline":
;            (debug-message "TYPE Polyline has no field editing")

;        elif item.type == "RAY":
;            # TODO: field editing
;            (debug-message "TYPE Polyline has no field editing")

;        elif item.type == "RECTANGLE":
;            # TODO: field editing
;            (debug-message "TYPE Polyline has no field editing")

;        elif item.type == "TEXTMULTI":
;            # TODO: field editing
;            (debug-message "TYPE Polyline has no field editing")

;        elif item.type == "TEXTSINGLE":
;            # TODO: field editing
;            if objName == "edit-TextSingleContents":
;                item.setObjectText(edit-TextSingleContents.text())

;            if objName == "comboBoxTextSingleFont":
;                if comboBoxTextSingleFont.currentText() == field-varies-text:
;                    break
;                item.setTextFont(comboBoxTextSingleFont.currentFont().family())
;            if objName == "comboBoxTextSingleJustify":
;                if comboBoxTextSingleJustify.currentText() != field-varies-text:
;                    item.setTextJustify(comboBoxTextSingleJustify.itemData(comboBoxTextSingleJustify.currentIndex()).toString())

;            if objName == "edit-TextSingleHeight":
;                tempTextSingleObj = static-cast<TextSingle*>(item)
;                if (tempTextSingleObj) {
;                    tempTextSingleObj.setTextSize(edit-TextSingleHeight.text().toDouble())

;            if objName == "edit-TextSingleRotation":
;                tempTextSingleObj = static-cast<TextSingle*>(item)
;                if tempTextSingleObj:
;                    tempTextSingleObj.setRotation(-edit-TextSingleRotation.text().toDouble())

;            if objName == "edit-TextSingleX":
;                tempTextSingleObj = static-cast<TextSingle*>(item)
;                if tempTextSingleObj:
;                    tempTextSingleObj.setX(edit-TextSingleX.text().toDouble())

;            if objName == "edit-TextSingleY":
;                tempTextSingleObj = static-cast<TextSingle*>(item)
;                if tempTextSingleObj:
;                    tempTextSingleObj.setY(edit-TextSingleY.text().toDouble())

;            if objName == "comboBoxTextSingleBackward":
;                if comboBoxTextSingleBackward.currentText() != field-varies-text:
;                    tempTextSingleObj = static-cast<TextSingle*>(item)
;                    if tempTextSingleObj:
;                        tempTextSingleObj.setTextBackward(comboBoxTextSingleBackward.itemData(comboBoxTextSingleBackward.currentIndex()))

;            if objName == "comboBoxTextSingleUpsideDown":
;                if comboBoxTextSingleUpsideDown.currentText() != field-varies-text:
;                    item.setTextUpsideDown(comboBoxTextSingleUpsideDown.itemData(comboBoxTextSingleUpsideDown.currentIndex()))

;    # Block this slot from running twice since calling setSelectedItems will trigger it
;    blockSignals = 1

;    widget = QApplication-focusWidget()
;    # Update so all fields have fresh data
;    # TODO: Improve this

;    setSelectedItems(selectedItemList)
;    hideAllGroups()
;    showGroups(obj-type)

;    if widget:
;        widget.setFocus(Qt-OtherFocusReason)

;    blockSignals = 0
)
;*/

;/*
; *  To make the undo history easier to manage we use a dict for
; *  keeping all the action information together.
; *
; *  For more commentary on this file see the Settings Dialog sections
; *  of the README.
; */
(define ()
;load-icon(char *fname)
;    (debug-message "load-icon with fname:")
;    (debug-message fname)
)

(define ()
;addColorsTocombo-box(int combo-box)
;/*
;    combo-box.add-item(load-icon(colorred-xpm), translate("Red"), tk.Rgb(255, 0, 0))
;    combo-box.add-item(load-icon(coloryellow-xpm), translate("Yellow"), tk.Rgb(255,255, 0))
;    combo-box.add-item(load-icon(colorgreen-xpm), translate("Green"), tk.Rgb(  0,255, 0))
;    combo-box.add-item(load-icon(colorcyan-xpm), translate("Cyan"), tk.Rgb(  0,255,255))
;    combo-box.add-item(load-icon(colorblue-xpm), translate("Blue"), tk.Rgb(  0, 0,255))
;    combo-box.add-item(load-icon(colormagenta-xpm), translate("Magenta"), tk.Rgb(255, 0,255))
;    combo-box.add-item(load-icon(colorwhite-xpm), translate("White"), tk.Rgb(255,255,255))
;    # TODO: Add Other... so the user can select custom colors */
)

(define ()
;combo-boxLanguageCurrent-index-changed(char *lang)
;/*
;    dialog-general-language = lang.toLower()
;    */
)

(define ()
;combo-box-icon-themeCurrent-index-changed(char *theme)
;/*
;    strcpy(dialog-general-icon-theme, theme)
;    */
)

(define ()
;combo-box-icon-sizeCurrent-index-changed(int index)
;/*
;    combo-box = sender()
;    if (combo-box) {
;        ok = 0
;        dialog-general-icon-size, ok = combo-box.itemData(index).toUInt()
;        if (!ok) {
;            dialog-general-icon-size = 16
;        }
;    }
;    else {
;        dialog-general-icon-size = 16
;    }
;    */
)

(define ()
;check-boxGeneralMdiBGUseLogo-state-changed(int checked)
;/*
;    preview.general-mdi-bg-use-logo = checked
;    mdi-area.useBackgroundLogo(int checked); */
)

(define ()
;chooseGeneralMdiBackgroundLogo(void)
;/*
;    button = sender()
;    if button) {
;        selectedImage = tk.FileDialog-get-open-fname(this, translate("Open File"),
;                        tk.StandardPaths-writableLocation(QStandardPaths-PicturesLocation),
;                        translate("Images (*.bmp *.png *.jpg)"))

;        if selectedImage != "") {
;            accept.general-mdi-bg-logo = selectedImage

;        #Update immediately so it can be previewed
;        mdi-area.setBackgroundLogo(accept-.general-mdi-bg-logo); */
)

(define ()
;check-boxGeneralMdiBGUseTexture-state-changed(int checked)
;/*
;    preview.general-mdi-bg-use-texture = checked
;    mdi-area.useBackgroundTexture(int checked)
;    */
)

(define ()
;chooseGeneralMdiBackgroundTexture(void)
;/*
;    button = sender()
;    if (button) {
;        selectedImage = tk.FileDialog-get-open-fname(
;            this, translate("Open File"),
;            tk.StandardPaths-writableLocation(QStandardPaths-PicturesLocation),
;            translate("Images (*.bmp *.png *.jpg)"))

;        if (selectedImage != "") {
;            accept.general-mdi-bg-texture = selectedImage
;        }*/

;        /* Update immediately so it can be previewed. */ /*
;        mdi-area.setBackgroundTexture(accept-.general-mdi-bg-texture)
;    }*/
)

(define ()
;check-boxGeneralMdiBGUseColor-state-changed(int checked)
;/*
;    preview.general-mdi-bg-use-color = checked
;    mdi-area.useBackgroundColor(int checked)
;*/
)

(define ()
;chooseGeneralMdiBackgroundColor(void)
;/*
;    button = sender()
;    if (button) {
;        color-dialog = color-dialog(Color(accept-.general-mdi-bg-color), this)
;        #connect(color-dialog, SIGNAL(currentColorChanged()), this, SLOT(currentGeneralMdiBackgroundColorChanged()))
;        color-dialog-exec()

;        if (color-dialog-result() == "Accepted") {
;            accept.general-mdi-bg-color = color-dialog-selectedColor().rgb()
;            pix = Image(16,16)
;            pix.fill(Color(accept-.general-mdi-bg-color))
;            button.setIcon(pix)
;            mdi-area.setBackgroundColor(Color(accept-.general-mdi-bg-color))
;        }
;        else {
;            mdi-area.setBackgroundColor(Color(dialog-general-mdi-bg-color))
;        }
;    } */
)

(define ()
;currentGeneralMdiBackgroundColorChanged(EmbColor color)
;   /* preview.general-mdi-bg-color = color.rgb()
;    mdi-area.setBackgroundColor(Color(preview.general-mdi-bg-color)); */
;    /*
;    lambda method constructor?
;    */
)

(define ()
;check-boxTipOfTheDay-state-changed(void)
;    /*
;    check-func(check-boxTipOfTheDay-state-changed, general-tip-of-the-day)
;    check-func(check-boxUseOpenGL-state-changed, INT-DISPLAY-USE-OPENGL)
;    check-func(check-boxRenderHintAA-state-changed, display-renderhint-aa)
;    check-func(check-boxRenderHintTextAA-state-changed, display-renderhint-text-aa)
;    check-func(check-boxRenderHintSmoothPix-state-changed, display-renderhint-smooth-pix)
;    check-func(check-boxRenderHintHighAA-state-changed, display-renderhint-high-aa)
;    check-func(check-boxRenderHintNonCosmetic-state-changed, display-renderhint-noncosmetic)
;    */
)

(define ()
;check-boxShowScrollBars-state-changed(int checked)
;/*
;    preview.display-show-scrollbars = checked
;    updateAllViewScrollBars(preview.display-show-scrollbars); */
)

(define ()
;spin-boxzoom-scale-actionIn-value-changed(double value)
;    /* dialog-display-zoom-scale-action-in = value; */
)

(define ()
;spin-boxzoom-scale-actionOut-value-changed(double value)
;    /*dialog-display-zoom-scale-action-out = value; */
)

(define ()
;check-boxDisableBG-state-changed(int checked)
;    /*dialog-printing-disable-bg = checked; */
)

(define ()
;chooseDisplayCrossHairColor(void)
;/*
;    button = sender()
;    if button) {
;        color-dialog = color-dialog(Color(accept-.display-crosshair-color), this)
;        #connect(color-dialog, SIGNAL(currentColorChanged()), this, SLOT(currentDisplayCrossHairColorChanged()))
;        color-dialog-exec()

;        if color-dialog-result() == "Accepted") {
;            accept.display-crosshair-color = color-dialog-selectedColor().rgb()
;            pix = Image(16,16)
;            pix.fill(Color(accept-.display-crosshair-color))
;            button.setIcon(pix)
;            updateAllViewCrossHairColors(accept-.display-crosshair-color)
;        }
;        else {
;            updateAllViewCrossHairColors(dialog-display-crosshair-color)
;        }
;    } */
)

(define ()
;currentDisplayCrossHairColorChanged(EmbColor color)
;/*
;    preview.display-crosshair-color = color.rgb()
;    updateAllViewCrossHairColors(preview.display-crosshair-color); */
)
 /*
(define ()
;chooseDisplayBackgroundColor()
;    button = sender()
;    if button) {
;        color-dialog = color-dialog(Color(accept-.display-bg-color), this)
;        #connect(color-dialog, SIGNAL(currentColorChanged()), this, SLOT(currentDisplayBackgroundColorChanged()))
;        color-dialog-exec()

;        if color-dialog-result() == "Accepted") {
;            accept.display-bg-color = color-dialog-selectedColor().rgb()
;            pix = Image(16, 16)
;            pix.fill(Color(accept-.display-bg-color))
;            button.setIcon(pix)
;            updateAllViewBackgroundColors(accept-.display-bg-color)
;        else) {
;            updateAllViewBackgroundColors(dialog-display-bg-color)

(define ()
;currentDisplayBackgroundColorChanged(EmbColor color)
;    preview.display-bg-color = color.rgb()
;    updateAllViewBackgroundColors(preview.display-bg-color)
)

(define ()
;chooseDisplaySelectBoxLeftColor()
;    button = sender()
;    if (button) {
;        color-dialog = color-dialog(Color(accept--display-selectbox-left-color), this)
;        #connect(color-dialog, SIGNAL(currentColorChanged()), this, SLOT(currentDisplaySelectBoxLeftColorChanged()))
;        color-dialog-exec()

;        if (color-dialog-result() == tk.Dialog-Accepted) {
;            accept-display-selectbox-left-color = color-dialog-selectedColor().rgb()
;            pix = Image(16, 16)
;            pix.fill(Color(accept--display-selectbox-left-color))
;            button.setIcon(pix)
;            update-all-view-select-box-colors(accept--display-selectbox-left-color,
;                accept-display-selectbox-left-fill,
;                accept-display-selectbox-right-color,
;                accept.display-selectbox-right-fill,
;                preview.display-selectbox-alpha)
;        }
;        else {
;            update-all-view-select-box-colors(
;                dialog-display-selectbox-left-color,
;                dialog-display-selectbox-left-fill,
;                dialog-display-selectbox-right-color,
;                dialog-display-selectbox-right-fill,
;                preview.display-selectbox-alpha)
;        }
;    }
)

(define ()
;currentDisplaySelectBoxLeftColorChanged(color)
;    preview-display-selectbox-left-color = color.rgb()
;    update-all-view-select-box-colors(
;        preview-display-selectbox-left-color,
;        preview-display-selectbox-left-fill,
;        preview-display-selectbox-right-color,
;        preview-display-selectbox-right-fill,
;        preview-display-selectbox-alpha)
)

(define ()
;chooseDisplaySelectBoxLeftFill(void)
;    button = sender()
;    if (button) {
;        color-dialog = color-dialog(Color(accept-display-selectbox-left-fill), this)
;        #connect(color-dialog, SIGNAL(currentColorChanged()), this, SLOT(currentDisplaySelectBoxLeftFillChanged()))
;        color-dialog-exec()

;        if (color-dialog-result() == "Accepted") {
;            accept-display-selectbox-left-fill = color-dialog-selectedColor().rgb()
;            pix = Image(16, 16)
;            pix.fill(Color(accept-display-selectbox-left-fill))
;            button.setIcon(pix)
;            update-all-view-select-box-colors(
;                accept-display-selectbox-left-color,
;                accept-display-selectbox-left-fill,
;                accept-display-selectbox-right-color,
;                accept-display-selectbox-right-fill,
;                preview-display-selectbox-alpha)
;        }
;        else {
;            update-all-view-select-box-colors(
;                dialog-display-selectbox-left-color,
;                dialog-display-selectbox-left-fill,
;                dialog-display-selectbox-right-color,
;                dialog-display-selectbox-right-fill,
;                preview-display-selectbox-alpha)
;        }
;    }
)

(define ()
;current-display-selectBoxLeftFillChanged(color)
;    preview-display-selectbox-left-fill = color.rgb()
;    update-all-view-select-box-colors(
;        preview-display-selectbox-left-color,
;        preview-display-selectbox-left-fill,
;        preview-display-selectbox-right-color,
;        preview-display-selectbox-right-fill,
;        preview-display-selectbox-alpha)
)

(define ()
;choose-display-select-box-right-color(void)
;    button = sender()
;    if (button) {
;        color-dialog = color-dialog(Color(accept--display-selectbox-right-color), this)
;        #connect(color-dialog, SIGNAL(currentColorChanged()), this, SLOT(currentDisplaySelectBoxRightColorChanged()))
;        color-dialog-exec()

;        if (color-dialog-result() == "Accepted") {
;            accept-display-selectbox-right-color = color-dialog-selectedColor().rgb()
;            pix = Image(16, 16)
;            pix.fill(Color(accept-display-selectbox-right-color))
;            button.setIcon(pix)
;            update-all-view-select-box-colors(
;                accept-display-selectbox-left-color,
;                accept-display-selectbox-left-fill,
;                accept-display-selectbox-right-color,
;                accept-display-selectbox-right-fill,
;                preview-display-selectbox-alpha)
;        }
;        else {
;            update-all-view-select-box-colors(
;                dialog-display-selectbox-left-color,
;                dialog-display-selectbox-left-fill,
;                dialog-display-selectbox-right-color,
;                dialog-display-selectbox-right-fill,
;                preview-display-selectbox-alpha)
;        }
;    }
)

(define ()
;currentDisplaySelectBoxRightColorChanged(EmbColor color)
;    preview-display-selectbox-right-color = color.rgb()
;    update-all-view-select-box-colors(
;        preview-display-selectbox-left-color,
;        preview-display-selectbox-left-fill,
;        preview-display-selectbox-right-color,
;        preview-display-selectbox-right-fill,
;        preview-display-selectbox-alpha)
)

(define ()
;chooseDisplaySelectBoxRightFill(void)
;    button = sender()
;    if (button) {
;        color-dialog = color-dialog(Color(accept-.display-selectbox-right-fill), this)
;        #connect(color-dialog, SIGNAL(currentColorChanged()), this, SLOT(currentDisplaySelectBoxRightFillChanged()))
;        color-dialog-exec()

;        if (color-dialog-result() == "Accepted") {
;            accept.display-selectbox-right-fill = color-dialog-selectedColor().rgb()
;            pix = Image(16, 16)
;            pix.fill(Color(accept-.display-selectbox-right-fill))
;            button.setIcon(pix)
;            update-all-view-select-box-colors(
;                accept-display-selectbox-left-color,
;                accept-display-selectbox-left-fill,
;                accept-display-selectbox-right-color,
;                accept-display-selectbox-right-fill,
;                preview-display-selectbox-alpha)
;        }
;        else {
;            update-all-view-select-box-colors(
;                dialog-display-selectbox-left-color,
;                dialog-display-selectbox-left-fill,
;                dialog-display-selectbox-right-color,
;                dialog-display-selectbox-right-fill,
;                preview-display-selectbox-alpha)
;        }
;    }
)

(define ()
;currentDisplaySelectBoxRightFillChanged(color)
;    preview.display-selectbox-right-fill = color.rgb()
;    update-all-view-select-box-colors(
;        preview-display-selectbox-left-color,
;        preview-display-selectbox-left-fill,
;        preview-display-selectbox-right-color,
;        preview-display-selectbox-right-fill,
;        preview-display-selectbox-alpha)
)

(define ()
;spin-boxDisplaySelectBoxAlpha-value-changed(value)
;    preview.display-selectbox-alpha = value
;    update-all-view-select-box-colors(
;        accept-display-selectbox-left-color,
;        accept-display-selectbox-left-fill,
;        accept-display-selectbox-right-color,
;        accept-display-selectbox-right-fill,
;        preview-display-selectbox-alpha)
)
;*/
;/* .
;
(define ()
;check-boxCustomFilter-state-changed(int checked)
;    check-box = sender()
;    if check-box) {
;        format = check-box.text()
;        (debug-message "CustomFilter: %s %d", tk.Printable(format), checked)
;        if (checked) {
;            opensave-custom-filter.append(" *." + format.toLower())
;        }
;        else {
;            opensave-custom-filter.remove("*." + format, tk.t-CaseInsensitive)
;        }
;        #dialog-opensave-custom-filter = checked; #TODO
;    }
)
;*/
;/* .
;
(define ()
;buttonCustomFilterSelectAllClicked(void)
;    buttonCustomFilterSelectAll(1)
;    opensave-custom-filter = "supported"
)
;*/
;/* .
;
(define ()
;buttonCustomFilterClearAllClicked(void)
;    buttonCustomFilterClearAll(0)
;    opensave-custom-filter.clear()
)
;*/
;/* .
;*/ /*
(define ()
;check-boxGridColorMatchCrossHair-state-changed(int checked)
;    dialog-grid-color-match-crosshair = checked
;    if dialog-grid-color-match-crosshair) {
;        updateAllViewGridColors(accept-.display-crosshair-color)

;    else) {
;        updateAllViewGridColors(accept-.grid-color)

;    sender-obj = sender()
;    if (!sender-obj) {
;        return
;    }

;    parent = sender-obj.parent()
;    if (!parent) {
;        return

;    labelGridColor = parent.find-child("labelGridColor")
;    if labelGridColor) {
;        labelGridColor.set-enabled(!dialog-grid-color-match-crosshair)

;    buttonGridColor = parent.find-child("buttonGridColor")
;    if buttonGridColor) {
;        buttonGridColor.set-enabled(!dialog-grid-color-match-crosshair)
)
;*/
;/* .
;
(define ()
;chooseGridColor(void)
;    button = sender()
;    if (button) {
;        color-dialog = color-dialog(Color(accept-.grid-color), this)
;        #connect(color-dialog, SIGNAL(currentColorChanged()), this, SLOT(currentGridColorChanged()))
;        color-dialog-exec()

;        if (color-dialog-result() == "Accepted") {
;            accept.grid-color = color-dialog-selectedColor().rgb()
;            pix = Image(16, 16)
;            pix.fill(Color(accept-.grid-color))
;            button.setIcon(pix)
;            updateAllViewGridColors(accept-.grid-color)
;        }
;        else {
;            updateAllViewGridColors(dialog-grid-color)
;        }
;    }
)*/
 /*
(define ()
;currentGridColorChanged(color)
;    preview.grid-color = color.rgb()
;    updateAllViewGridColors(preview.grid-color)
)*/
 /*
(define ()
;check-box-grid-load-from-file-state-changed(int checked)
;    dialog-grid-load-from-file = checked

;    sender-obj = sender()
;    if (!sender-obj) {
;        return

;    parent = sender-obj.parent()
;    if (!parent) {
;        return

;    label-grid-type = parent.find-child("label-grid-type")
;    if label-grid-type) {
;        label-grid-type.set-enabled(!dialog-grid-load-from-file)

;    combo-box-grid-type = parent.find-child("combo-box-grid-type")
;    if combo-box-grid-type) {
;        combo-box-grid-type.set-enabled(!dialog-grid-load-from-file)

;    check-box-grid-center-on-origin = parent.find-child("check-box-grid-center-on-origin")
;    if check-box-grid-center-on-origin) {
;        check-box-grid-center-on-origin.set-enabled(!dialog-grid-load-from-file)

;    label-grid-center-x = parent.find-child("label-grid-center-x")
;    if label-grid-center-x) {
;        label-grid-center-x.set-enabled(!dialog-grid-load-from-file and not dialog-grid-center-on-origin)

;    spin-boxGridCenterX = parent.find-child("spin-boxGridCenterX")
;    if spin-boxGridCenterX) {
;        spin-boxGridCenterX.set-enabled(!dialog-grid-load-from-file and not dialog-grid-center-on-origin)

;    label-grid-center-y = parent.find-child("label-grid-center-y")
;    if label-grid-center-y) {
;        label-grid-center-y.set-enabled(!dialog-grid-load-from-file and not dialog-grid-center-on-origin)

;    spin-box-grid-center-y = parent.find-child("spin-box-grid-center-y")
;    if spin-box-grid-center-y) {
;        spin-box-grid-center-y.set-enabled(!dialog-grid-load-from-file and not dialog-grid-center-on-origin)

;    label-grid-sizeX = parent.find-child("label-grid-sizeX")
;    if label-grid-sizeX) {
;        label-grid-sizeX.set-enabled(!dialog-grid-load-from-file)

;    spin-box-grid-sizeX = parent.find-child("spin-box-grid-sizeX")
;    if spin-box-grid-sizeX) {
;        spin-box-grid-sizeX.set-enabled(!dialog-grid-load-from-file)

;    label-grid-sizeY = parent.find-child("label-grid-sizeY")
;    if label-grid-sizeY) {
;        label-grid-sizeY.set-enabled(!dialog-grid-load-from-file)

;    spin-box-grid-sizeY = parent.find-child("spin-box-grid-sizeY")
;    if spin-box-grid-sizeY) {
;        spin-box-grid-sizeY.set-enabled(!dialog-grid-load-from-file)

;    labelGridSpacingX = parent.find-child("labelGridSpacingX")
;    if labelGridSpacingX) {
;        labelGridSpacingX.set-enabled(!dialog-grid-load-from-file)

;    spin-boxGridSpacingX = parent.find-child("spin-boxGridSpacingX")
;    if spin-boxGridSpacingX) {
;        spin-boxGridSpacingX.set-enabled(!dialog-grid-load-from-file)

;    labelGridSpacingY = parent.find-child("labelGridSpacingY")
;    if labelGridSpacingY) {
;        labelGridSpacingY.set-enabled(!dialog-grid-load-from-file)

;    spin-boxGridSpacingY = parent.find-child("spin-boxGridSpacingY")
;    if spin-boxGridSpacingY) {
;        spin-boxGridSpacingY.set-enabled(!dialog-grid-load-from-file)

;    label-grid-sizeRadius = parent.find-child("label-grid-sizeRadius")
;    if label-grid-sizeRadius) {
;        label-grid-sizeRadius.set-enabled(!dialog-grid-load-from-file)

;    spin-box-grid-sizeRadius = parent.find-child("spin-box-grid-sizeRadius")
;    if spin-box-grid-sizeRadius) {
;        spin-box-grid-sizeRadius.set-enabled(!dialog-grid-load-from-file)

;    labelGridSpacingRadius = parent.find-child("labelGridSpacingRadius")
;    if labelGridSpacingRadius) {
;        labelGridSpacingRadius.set-enabled(!dialog-grid-load-from-file)

;    spin-boxGridSpacingRadius = parent.find-child("spin-boxGridSpacingRadius")
;    if spin-boxGridSpacingRadius) {
;        spin-boxGridSpacingRadius.set-enabled(!dialog-grid-load-from-file)

;    labelGridSpacingAngle = parent.find-child("labelGridSpacingAngle")
;    if labelGridSpacingAngle) {
;        labelGridSpacingAngle.set-enabled(!dialog-grid-load-from-file)

;    spin-boxGridSpacingAngle = parent.find-child("spin-boxGridSpacingAngle")
;    if spin-boxGridSpacingAngle) {
;        spin-boxGridSpacingAngle.set-enabled(!dialog-grid-load-from-file)
)
;*/
;/* .
;
(define ()
;combo-box-grid-typeCurrent-index-changed(type-)
;    dialog-grid-type = type-

;    sender-obj = sender()
;    if (!sender-obj) {
;        return

;    parent = sender-obj.parent()
;    if (!parent) {
;        return

;    visibility = False
;    if type- == "Circular") {
;        visibility = 1

;    label-grid-size-x = parent.find-child("label-grid-sizeX")
;    if label-grid-size-x) {
;        label-grid-size-x.set-visible(!visibility)

;    spin-box-grid-sizeX = parent.find-child("spin-box-grid-sizeX")
;    if spin-box-grid-sizeX) {
;        spin-box-grid-sizeX.set-visible(!visibility)

;    label-grid-sizeY = parent.find-child("label-grid-sizeY")
;    if label-grid-sizeY) {
;        label-grid-sizeY.set-visible(!visibility)

;    spin-box-grid-sizeY = parent.find-child("spin-box-grid-sizeY")
;    if spin-box-grid-sizeY) {
;        spin-box-grid-sizeY.set-visible(!visibility)

;    labelGridSpacingX = parent.find-child("labelGridSpacingX")
;    if labelGridSpacingX) {
;        labelGridSpacingX.set-visible(!visibility)

;    spin-boxGridSpacingX = parent.find-child("spin-boxGridSpacingX")
;    if spin-boxGridSpacingX) {
;        spin-boxGridSpacingX.set-visible(!visibility)

;    labelGridSpacingY = parent.find-child("labelGridSpacingY")
;    if labelGridSpacingY) {
;        labelGridSpacingY.set-visible(!visibility)

;    spin-boxGridSpacingY = parent.find-child("spin-boxGridSpacingY")
;    if spin-boxGridSpacingY) {
;        spin-boxGridSpacingY.set-visible(!visibility)

;    label-grid-sizeRadius = parent.find-child("label-grid-sizeRadius")
;    if label-grid-sizeRadius) {
;        label-grid-sizeRadius.set-visible(visibility)

;    spin-box-grid-sizeRadius = parent.find-child("spin-box-grid-sizeRadius")
;    if spin-box-grid-sizeRadius) {
;        spin-box-grid-sizeRadius.set-visible(visibility)

;    labelGridSpacingRadius = parent.find-child("labelGridSpacingRadius")
;    if labelGridSpacingRadius) {
;        labelGridSpacingRadius.set-visible(visibility)

;    spin-boxGridSpacingRadius = parent.find-child("spin-boxGridSpacingRadius")
;    if spin-boxGridSpacingRadius) {
;        spin-boxGridSpacingRadius.set-visible(visibility)

;    labelGridSpacingAngle = parent.find-child("labelGridSpacingAngle")
;    if labelGridSpacingAngle) {
;        labelGridSpacingAngle.set-visible(visibility)

;    spin-boxGridSpacingAngle = parent.find-child("spin-boxGridSpacingAngle")
;    if spin-boxGridSpacingAngle) {
;        spin-boxGridSpacingAngle.set-visible(visibility)
)
;*/
 /*
(define ()
;check-box-grid-center-on-origin-state-changed(int checked)
;    dialog-grid-center-on-origin = checked

;    sender-obj = sender()
;    if (!sender-obj) {
;        return

;    parent = sender-obj.parent()
;    if (!parent) {
;        return

;    label-grid-center-x = parent.find-child("label-grid-center-x")
;    if label-grid-center-x) {
;        label-grid-center-x.set-enabled(!dialog-grid-center-on-origin)

;    spin-boxGridCenterX = parent.find-child("spin-boxGridCenterX")
;    if spin-boxGridCenterX) {
;        spin-boxGridCenterX.set-enabled(!dialog-grid-center-on-origin)

;    label-grid-center-y = parent.find-child("label-grid-center-y")
;    if label-grid-center-y) {
;        label-grid-center-y.set-enabled(!dialog-grid-center-on-origin)

;    spin-box-grid-center-y = parent.find-child("spin-box-grid-center-y")
;    if spin-box-grid-center-y) {
;        spin-box-grid-center-y.set-enabled(!dialog-grid-center-on-origin)
)
;*/

(define ()
;combo-box-ruler-metric-current-index-changed(int index)
;    /*
;    combo-box = sender()
;    if (combo-box) {
;        ok = False
;        dialog-ruler-metric = combo-box.itemData(index)
;    }
;    else {
;        dialog-ruler-metric = 1
;    }*/
)

(define ()
;chooseRulerColor(void)
;    /*
;    button = sender()
;    if (button) {
;        color-dialog = color-dialog(
;            Color(accept-.ruler-color), this)
;        # connect(color-dialog, SIGNAL(currentColorChanged()),
;        # this, SLOT(currentRulerColorChanged()))
;        color-dialog-exec()

;        if (color-dialog-result() == "QDialog-Accepted") {
;            accept.ruler-color = color-dialog-selectedColor().rgb()
;            pix = Image(16, 16)
;            pix.fill(Color(accept-.ruler-color))
;            button.setIcon(pix)
;            updateAllViewRulerColors(accept-.ruler-color)
;        }
;        else {
;            updateAllViewRulerColors(dialog-ruler-color)
;        }
;    }
;    */
)

;/*
; */
(define ()
;currentRulerColorChanged(EmbColor color)
;    /*
;    preview.ruler-color = color.rgb()
;    updateAllViewRulerColors(preview.ruler-color)
;    */
)

;/*
;
(define ()
;buttonQSnapSelectAllClicked(void)
;    buttonQSnapSelectAll(1)
)

;/*
; * TODO:
; * Figure out how to abstract the slot in a way that it can be used for
; * combo-boxes in general
; * Currently combo-boxQSnapLocatorColorCurrent-index-changed(int index)
; *       combo-boxSelectionCoolGripColorCurrent-index-changed(int index)
; *       combo-boxSelectionHotGripColorCurrent-index-changed(int index)
; * are all similar except the dialog- variable being worked on and the
; * tk.Variant.
;
(define ()
;buttonQSnapClearAllClicked(void)
;    buttonQSnapClearAll(0)
)

;/* TODO: Alert user if color matched the display bg color
;
(define ()
;combo-boxQSnapLocatorColorCurrent-index-changed(int index)
;    combo-box = sender()
;    default-color = tk.Rgb(255,255,0)
;    # Yellow
;    if combo-box) {
;        dialog-qsnap-locator-color, ok = combo-box.itemData(index).toUInt()
;        if (!ok) {
;            dialog-qsnap-locator-color = default-color
;    else) {
;        dialog-qsnap-locator-color = default-color
)
 /*
(define ()
;sliderQSnap-locator-size-value-changed(double value)
;    dialog-qsnap-locator-size = value
)
 /*
(define ()
;sliderQSnap-aperture-size-value-changed(double value)
;    dialog-qsnap-aperture-size = value
)

(define ()
;check-boxLwtShowLwt-state-changed(int checked)
;    preview.lwt-show-lwt = checked
;    if preview.lwt-show-lwt) {
;        enable-lwt()
;    else) {
;        disableLwt()

;    sender-obj = sender()
;    if sender-obj) {
;        parent = sender-obj.parent()
;        if parent) {
;            check-boxRealRender = parent.find-child("check-boxRealRender")
;            if check-boxRealRender) {
;                check-boxRealRender.set-enabled(preview.lwt-show-lwt)

(define ()
;check-boxLwtRealRender-state-changed(int checked)
;    preview-lwt-real-render = checked
;    if preview-lwt-real-render) {
;        enableReal()
;    else) {
;        disableReal()
)

(define ()
;combo-boxSelectionCoolGripColorCurrent-index-changed(index)
;    # TODO: Alert user if color matched the display bg color
;    combo-box = sender()
;    default-color = tk.Rgb(0,0,255)
;    # Blue
;    if combo-box) {
;        dialog-selection-coolgrip-color, ok = combo-box.item-data(index).toUInt()
;        if (!ok) {
;            dialog-selection-coolgrip-color = default-color
;    else) {
;        dialog-selection-coolgrip-color = default-color
)

(define ()
;combo-box-selectionHotGripColorCurrent-index-changed(index)
;    # TODO: Alert user if color matched the display bg color
;    combo-box = sender()
;    default-color = tk.Rgb(255,0,0)
;    # Red
;    if combo-box) {
;        dialog-selection-hotgrip-color, ok = combo-box.item-data(index).toUInt()
;        if (!ok) {
;            dialog-selection-hotgrip-color = default-color
;    else) {
;        dialog-selection-hotgrip-color = default-color
)
;*/
;/* . */ /*
(define ()
;accept-changes(void)
;    for k in preview.keys()
;        dialog[k] = preview[k]
;    for k in accept.keys()
;        dialog[k] = preview[k]

;    if dialog-grid-color-match-crosshair) {
;        dialog-grid-color = accept-display-crosshair-color

;    # Make sure the user sees the changes applied immediately.
;    mdi-area.use-background-logo(dialog-general-mdi-bg-use-logo)
;    mdi-area.use-background-texture(dialog-general-mdi-bg-use-texture)
;    mdi-area.use-background-color(dialog-general-mdi-bg-use-color)
;    mdi-area.set-background-logo(dialog-general-mdi-bg-logo)
;    mdi-area.set-background-texture(dialog-general-mdi-bg-texture)
;    mdi-area.set-background-color(dialog-general-mdi-bg-color)
;    icon-resize(dialog-general-icon-size)
;    update-all-view-scrollBars(dialog-display-show-scrollbars)
;    update-all-view-cross-hair-colors(dialog-display-crosshair-color)
;    update-all-view-background-colors(dialog-display-bg-color)
;    update-all-view-select-box-colors(
;        dialog-display-selectbox-left-color,
;        dialog-display-selectbox-left-fill,
;        dialog-display-selectbox-right-color,
;        dialog-display-selectbox-right-fill,
;        dialog-display-selectbox-alpha)
;    update-all-view-grid-colors(dialog-grid-color)
;    update-all-view-ruler-colors(dialog-ruler-color)

;    if dialog-lwt-show-lwt) {
;        enable-lwt()
;    else) {
;        disableLwt()

;    if dialog-lwt-real-render) {
;        enableReal()
;    else) {
;        disableReal()

;    update-pick-add-mode(dialog-selection-mode-pickadd)

;    writeSettings()
;    accept()
)*/

;/*
;TODO: inform the user if they have changed settings

;Update the view since the user must accept the preview
;*/ /*
(define ()
;reject-changes(void)
;    mdi-area.use-background-logo(dialog-general-mdi-bg-use-logo)
;    mdi-area.use-background-texture(dialog-general-mdi-bg-use-texture)
;    mdi-area.use-background-color(dialog-general-mdi-bg-use-color)
;    mdi-area.set-background-logo(dialog-general-mdi-bg-logo)
;    mdi-area.set-background-texture(dialog-general-mdi-bg-texture)
;    mdi-area.set-background-color(dialog-general-mdi-bg-color)
;    update-all-view-scroll-bars(dialog-display-show-scrollbars)
;    update-all-view-cross-hair-colors(dialog-display-crosshair-color)
;    update-all-view-background-colors(dialog-display-bg-color)
;    update-all-view-select-box-colors(
;        dialog-display-selectbox-left-color,
;        dialog-display-selectbox-left-fill,
;        dialog-display-selectbox-right-color,
;        dialog-display-selectbox-right-fill,
;        dialog-display-selectbox-alpha)
;    update-all-view-grid-colors(dialog-grid-color)
;    update-all-view-ruler-colors(dialog-ruler-color)

;    if dialog-lwt-show-lwt) {
;        enable-lwt()
;    else) {
;        disableLwt()

;    if dialog-lwt-real-render) {
;        enableReal()
;    else) {
;        disableReal()

;    reject()
)

;/*
; * For safe packaging, and to reduce the risk of program
; * crashing errors the resources are loaded into the
; * application folder each time the program boots.
; */
(define ()
;load-image(char *path)
;    FILE *f
;    /*
;    image-fname = APPLICATION-FOLDER + os.sep + path
;    with open(image-fname, "wb") as image-file: {
;        icon = icons[path].replace("\n", "")
;        icon = icon.replace(" ", "")
;        decoded-image = binascii.unhexlify(icon)
;        image-file.write(decoded-image)
;    }
;    return tk.PhotoImage(file=image-fname); */
)

;/* Utility for creating the icons datafile.
; */
;int
;build-icons-json(char *folder)
;    /*
;    for (file in os.listdir(folder)) {
;        if (".png" in file) {
;            FILE *f = fopen(folder+os.sep+file, "rb")
;            icons[file] = image-file.fread().hex()
;            fclose(f)
;        }
;    } */
;    return 0
)

;/* 
;Whenever the code happens across a todo call, write it in a log file.
(define ()
;def todo(char *msg, int action)
;    if debug-mode) {
;        with open("todo.txt", "a", encoding="utf-8") as logfile) {
;            logfile.write(f"{msg}: {action}")
;        }
;    }
)

;Whenever the code happens across a todo call, write it in a log file.
;def error(char *msg, int action)
;    if debug-mode) {
;        with open("error.txt", "a", encoding="utf-8") as logfile) {
;            logfile.write(f"{msg}: {action}")
;        }
;    }
)
;*/


;/*
;def platform-string()
;    r" Return the host system label for debugging purposes. "
;    host-system = os.uname().sysname + " " + os.uname().release
;    (debug-message f"Platform: {host-system}")
;    return host-system */



;/* The Color class definition.
; */

;int color-mode
;int stitches-total
;int stitches-real
;int stitches-jump
;int stitches-trim
;int color-total
;int color-changes

;/* 
; * To manage thread colors and such, this class can call the settings
; * JSON dict.
; */
(define ()
;color-init(void)
;    /* color-mode = COLOR-BACKGROUND
;    strcpy(prefix, "Enter RED,GREEN,BLUE values for background or [Crosshair/Grid]: ")
;    set-prompt-prefix(translate(prefix)); */
)
 /*
(define ()
;color-prompt(char *cmd)
;    int output[3], valid, new-mode
;    valid = 0
;    new-mode = -1
;    if (cmd[0] == 'C' || !strcmp(cmd, "CROSSHAIR")) {
;        new-mode = COLOR-CROSSHAIR
;    }
;    if (cmd[0] == 'G' || !strcmp(cmd, "GRID")) {
;        new-mode = COLOR-GRID
;    }
;    if (cmd[0] == 'B' || !strcmp(cmd, "BACKGROUND")) {
;        new-mode = COLOR-BACKGROUND
;    }
;    if (color-mode != new-mode) {
;        switch (new-mode) {
;        case COLOR-BACKGROUND) {
;            color-mode = COLOR-BACKGROUND
;            set-prompt-prefix(translate("Specify background color: "))
;            break
;        case COLOR-CROSSHAIR) {
;            color-mode = COLOR-CROSSHAIR
;            set-prompt-prefix(translate("Specify crosshair color: "))
;            break
;        case COLOR-GRID) {
;            color-mode = COLOR-GRID
;            set-prompt-prefix(translate("Specify grid color: "))
;            break
;        }
;        return
;    }
;    valid = parse-three-ints(cmd, output)
;    switch (color-mode) {
;    case COLOR-BACKGROUND) {
;        if (valid) {
;            setBackgroundColor(output[0], output[1], output[2])
;        }
;        else {
;            alert("Invalid color.", "R,G,B values must be in the range of 0-255.")
;            set-prompt-prefix(translate("Specify background color: "))
;        }
;        break
;    case COLOR-CROSSHAIR) {
;        if (valid) {
;            setCrossHairColor(output[0], output[1], output[2])
;        }
;        else {
;            alert("Invalid color.", "R,G,B values must be in the range of 0-255.")
;            set-prompt-prefix(translate("Specify crosshair color: "))
;        }
;        break
;    case COLOR-GRID) {
;        if (valid) {
;            setGridColor(output[0], output[1], output[2])
;        }
;        else {
;            alert("Invalid color.", "R,G,B values must be in the range of 0-255.")
;            set-prompt-prefix(translate("Specify grid color: "))
;        }
;        break
;    default) {
;        break
;    }
)
;*/
;/*  The layer manager.
; */
(define ()
;layer-manager-init(LayerManager *mgr, int tab)
;    /*
;    layer-model = tk.StandardItemModel(mw, 0, 8)

;    layer-model-sorted = tk.SortFilterPoxyModel()
;    layer-model-sorted.setDynamicSortFilter(1)
;    layer-model-sorted.setSourceModel(layer-model)

;    treeView = tk.TreeView(mw)
;    treeView.setRootIsDecorated(0)
;    treeView.setAlternatingRowColors(1)
;    treeView.setModel(layer-model-sorted)
;    treeView.setSortingEnabled(1)
;    treeView.sortByColumn(0, "AscendingOrder")

;    mainLayout = tk.VBoxLayout()
;    mainLayout.addWidget(treeView)
;    set-layout(mainLayout)

;    set-window-title(translate("Layer Manager"))
;    set-minimum-size(750, 550)

;    layer-model.set-header-data(0, "horizontal", translate("Name"))
;    layer-model.set-header-data(1, "horizontal", translate("Visible"))
;    layer-model.set-header-data(2, "horizontal", translate("Frozen"))
;    layer-model.set-header-data(3, "horizontal", translate("Z Value"))
;    layer-model.set-header-data(4, "horizontal", translate("Color"))
;    layer-model.set-header-data(5, "horizontal", translate("Linetype"))
;    layer-model.set-header-data(6, "horizontal", translate("Lineweight"))
;    layer-model.set-header-data(7, "horizontal", translate("Print"))

;    add-layer("0", 1, 0, 0.0, (0, 0, 0), "Continuous", "Default", 1)
;    add-layer("1", 1, 0, 1.0, (0, 0, 0), "Continuous", "Default", 1)
;    add-layer("2", 1, 0, 2.0, (0, 0, 0), "Continuous", "Default", 1)
;    add-layer("3", 1, 0, 3.0, (0, 0, 0), "Continuous", "Default", 1)
;    add-layer("4", 1, 0, 4.0, (0, 0, 0), "Continuous", "Default", 1)
;    add-layer("5", 1, 0, 5.0, (0, 0, 0), "Continuous", "Default", 1)
;    add-layer("6", 1, 0, 6.0, (0, 0, 0), "Continuous", "Default", 1)
;    add-layer("7", 1, 0, 7.0, (0, 0, 0), "Continuous", "Default", 1)
;    add-layer("8", 1, 0, 8.0, (0, 0, 0), "Continuous", "Default", 1)
;    add-layer("9", 1, 0, 9.0, (0, 0, 0), "Continuous", "Default", 1)

;    for i in range(layer-model.count())
;        treeView.resizeColumnToContents(i)

;    Application-setOverrideCursor(Qt-ArrowCursor)

;    return self
;    */
)

(define ()
;layer-manager-add(
;    LayerManager *mgr,
;    char *name,
;    int visible,
;    int frozen,
;    int zValue,
;    char *color,
;    char *lineType,
;    double line-weight)
;    strcpy(mgr->name, name)
;    mgr->visible = visible
;    mgr->frozen = frozen
;    mgr->z-value = zValue
;    strcpy(mgr->color, color)
;    strcpy(mgr->line-type, lineType)
;    mgr->line-weight = line-weight
;    /*
;    # const print)
;    layer-model.insertRow(0)
;    layer-model.set-data(layer-model.index(0, 0), name)
;    layer-model.set-data(layer-model.index(0, 1), visible)
;    layer-model.set-data(layer-model.index(0, 2), frozen)
;    layer-model.set-data(layer-model.index(0, 3), zValue)

;    colorPix = QPixmap(16, 16)
;    colorPix.fill(Color(color))
;    layer-model.itemFromIndex(layer-model.index(0, 4)).setIcon(QIcon(colorPix))
;    layer-model.set-data(layer-model.index(0, 4), Color(color))

;    layer-model.set-data(layer-model.index(0, 5), lineType)
;    layer-model.set-data(layer-model.index(0, 6), lineWeight)
;    #layer-model.set-data(layer-model.index(0, 7), print)
;    */
)

(define ()
;layer-model(void)
;    return
)

(define ()
;layer-model-sorted(void)
;    return
)

(define ()
;tree-view(void)
;    return
)

(define ()
;layer-manager-delete(int tab)
;    /* restore-override-cursor(); */
)

;/*
; *  The dialog showing details of the pattern including histograms.
; */


;/* Creates a dialog showing key information about the pattern,
; * ideally this will update as the pattern changes without any key presses
; * or clicks.
; */
(define ()
;details-dialog-init(void)
;    /* kiss-window dialog = kiss-window()
;    dialog-setMinimumSize(750, 550)
;    dialog-title(translate("Embroidery Design Details"))
;    */

;    stitches-total = 0
;    stitches-real = 0
;    stitches-jump = 0
;    stitches-trim = 0
;    color-total = 0
;    color-changes = 0

;    /*
;    bounding-rect = Rect(0.0, 0.0, 0.1, 0.1)

;    get-info()
;    main-widget = create-main-widget()

;    button-box = tk.ButtonBox(dialog, text="QDialogButtonBox-Ok"); */
;    /* # connect(buttonBox, SIGNAL(accepted()), SLOT(accept())); */
;    /*
;    vbox-layout-main = tk.VBoxLayout()
;    vbox-layout-main.add-widget(main-widget)
;    vbox-layout-main.add-widget(button-box)
;    dialog-set-layout(vbox-layout-main)

;    mw.setOverrideCursor("ArrowCursor"); */
)

;/*
; */
(define ()
;details-dialog-free(void)
;    /* mw.restoreOverrideCursor(); */
)

;/*
; */
(define ()
;create-histogram(void)
;    (debug-message "TODO: createHistogram")
)

;/*
; */
(define ()
;get-info(EmbPattern *pattern)
;    /* TODO: generate a temporary pattern from the scene data. */

;    /* TODO: grab this information from the pattern */
;    stitches-total = 5
;    /* TODO: embStitchList-count(pattern->stitchList, TOTAL); */
;    stitches-real = 4
;    /* TODO: embStitchList-count(pattern.stitchList, NORMAL); */
;    stitches-jump = 3
;    /* TODO: embStitchList-count(pattern.stitchList, JUMP); */
;    stitches-trim = 2
;    /* TODO: embStitchList-count(pattern.stitchList, TRIM); */
;    color-total = 1
;    /* TODO: embThreadList-count(pattern.threadList, TOTAL); */
;    color-changes = 0
;    /* TODO: embThreadList-count(pattern.threadList, CHANGES); */
;    /* bounding-rect.set-rect(0, 0, 50, 100); */
;    /* # TODO: embPattern-calcBoundingBox(pattern); */
)

;/*
; * .
; */
(define ()
;create-main-widget(void)
;    /* widget = tk.Widget(dialog)

;    /* # Misc */
;    /* group-box-misc = tk.GroupBox(translate("General Information"), widget)

;    Labels = []
;    fields = []

;    for i in range(12)
;        details-labels = mw.setting-details-label-text
;        Labels[i] = tk.Label(translate(details-labels[i]))

;    fields[0] = tk.Label(str(stitches-total))
;    fields[1] = tk.Label(str(stitches-real))
;    fields[2] = tk.Label(str(stitches-jump))
;    fields[3] = tk.Label(str(stitches-trim))
;    fields[4] = tk.Label(str(color-total))
;    fields[5] = tk.Label(str(colorChanges))
;    fields[6] = tk.Label(str(bounding-rect.left()) + " mm")
;    fields[7] = tk.Label(str(bounding-rect.top()) + " mm")
;    fields[8] = tk.Label(str(bounding-rect.right()) + " mm")
;    fields[9] = tk.Label(str(bounding-rect.bottom()) + " mm")
;    fields[10] = tk.Label(str(bounding-rect.width()) + " mm")
;    fields[11] = tk.Label(str(bounding-rect.height()) + " mm")

;    grid-layout-misc = GridLayout(group-box-misc)
;    for i in range(12)
;        grid-layout-misc.add-widget(tk.Labels[i], i, 0, "Qt-AlignLeft")
;        grid-layout-misc.add-widget(fields[i], i, 1, "Qt-AlignLeft")

;    grid-layout-misc.setColumnStretch(1, 1)
;    group-box-misc.set-layout(grid-layout-misc)

;    /*
;    # TODO: Color Histogram

;    # Stitch Distribution
;    # groupBoxDist = QGroupBox(translate("Stitch Distribution"), widget)

;    # TODO: Stitch Distribution Histogram
;    */

;    /* Widget Layout */
;    /* vbox-layout-main = tk.VBoxLayout(widget)
;    vbox-layout-main.add-widget(group-box-misc); */
;    /* vbox-layout-main.add-widget(groupBoxDist); */
;    /* vbox-layout-main.addStretch(1)
;    widget.set-layout(vbox-layout-main)

;    scroll-area = tk.scroll-area()
;    scroll-area.set-widget-resizable(1)
;    scroll-area.set-widget(widget)
;    return scroll-area; */
)

;/*
; *  To display an embedded image as a widget in SDL2.
; */
(define ()
;image-widget-init(char *filename)
;    /* (debug-message "ImageWidget Constructor")
;    img = img-load(filename)

;    min-width = img.width()
;    min-height = img.height()
;    max-width = img.width()
;    max-height = img.height()

;    img.show(); */
)

(define ()
;image-widget-load(char *fileName)
;    /* return img.load(fileName); */
)

(define ()
;image-widget-save(char *fileName)
;    /* return img.save(fileName, "PNG"); */
)

;/*
; *
; */
(define ()
;paintEvent(SDL-Event event)
;    /* 
;    painter = Painter()
;    painter.setViewport(0, 0, img.width(), img.height())
;    painter.setWindow(0, 0, img.width(), img.height())
;    painter.drawImage(0, 0, img); */
)


;/*
;    Tooltip manager. SDL doesn't support tooltips out of the box.
;    ------------------------------------------------------------
;    
;    
;    Example here) {
;    https://stackoverflow.com/questions/3221956/how-do-i-display-tooltips-in-tkinter
;    https://gamedev.stackexchange.com/questions/186482/sdl2-show-a-tooltip-at-the-cursor-that-displays-rgb-of-the-pixel-under-the-cur
; *
; *  ------------------------------------------------------------
; *  Preview Dialog
; *  ------------------------------------------------------------
; *
; *  Preview the output.
; * 
; */
;/*
(define ()
;PreviewDialog-init--(self, parent, caption, dir, filter)
;    (debug-message "PreviewDialog Constructor")

;    #TODO: get actual thumbnail image from file, lets also use a size of 128x128 for now...
;    #TODO: make thumbnail size adjustable thru settings dialog
;    img-widget = ImageWidget("icons/default/nopreview.png")

;    lay = layout()
;    if lay) {
;        columns = lay.columnCount()
;        rows = lay.rowCount()
;        lay.addWidget(img-widget, 0, columns, rows, 1)

;    modal = 1
;    option = "FileDialog-DontUseNativeDialog"
;    view-mode = "FileDialog-Detail"
;    file-mode = "FileDialog-ExistingFiles"

;    #TODO: connect the currentChanged signal to update the preview img-widget.

(define ()
;PreviewDialogtoPolyline(self, pattern, obj-pos, obj-path, layer, color, line-type,  line-weight)
;    (debug-message "Unused arguments:")
;    (debug-message f"    {pattern}, {obj-pos}, {obj-path},")
;    (debug-message f"    {layer}, {color}, {line-type}, {line-weight}.")
)

; ------------------------------------------------------------
;
; The color selection docker class definition file.
;
; The color selection docker.
;
; From a duplicated version) {

;SelectBox(Shape s, QWidget* parent = 0)

;def setDirection(int dir)
;def setColors(colorL, fillL, colorR, fillR, newAlpha)
;def paintEvent(QPaintEvent*)
;def forceRepaint()
;def force-repaint()
;    #HACK: Take that QRubberBand!
;    hack = size()
;    resize(hack + QSize(1,1))
;    resize(hack)
;    # WARNING) {
;    # DO NOT SET THE QMDISUBWINDOW (this) FOCUSPROXY TO THE PROMPT
;    # AS IT WILL CAUSE THE WINDOW MENU TO NOT SWITCH WINDOWS PROPERLY!
;    # ALTHOUGH IT SEEMS THAT SETTING INTERNAL WIDGETS FOCUSPROXY IS OK.

;    #    gview.setFocusProxy(mw.prompt)

;    resize(sizeHint())

;    curLayer = "0"
;    curColor = 0; #TODO: color ByLayer
;    curline-type = "ByLayer"
;    curline-weight = "ByLayer"

;    # Due to strange Qt4.2.3 feature the child window icon is not drawn
;    # in the main menu if showMaximized() is called for a non-visible child window
;    # Therefore calling show() first...
;    show()
;    showMaximized()

;    setFocusPolicy(WheelFocus)
;    setFocus()

;    onWindowActivated()
)

; Default values.
;
(define (select-box-init tools)
;    tools->left-brush.color = "#FFFFFF"
;    tools->left-brush.style = BRUSH-STYLE-SOLID
;    tools->right-brush.color = "#FFFFFF"
;    tools->right-brush.style = BRUSH-STYLE-SOLID
;    tools->left-pen.color = "#FFFFFF"
;    tools->left-pen.style = LINE-STYLE-SOLID
;    tools->right-pen.color = "#FFFFFF"
;    tools->right-pen.style = LINE-STYLE-SOLID
;    tools->alpha = 0xFF
;    tools->box-dir = 0
;    select-box-direction(tools, tools->box-dir)
     ; not sure what this line was for 
;    select-box-colors("darkGreen", "green", "darkBlue", "blue", 32)
)

; Choose between the left an right tools.
;
(define (select-box-direction tools dir)
;    tools->box-dir = dir
;    if (dir == DIRECTION-RIGHT) {
;        tools->dir-pen = tools->right-pen
;        tools->dir-brush = tools->right-brush
;    }
;    else {
;        tools->dir-pen = tools->left-pen
;        tools->dir-brush = tools->left-brush
;    }
)

; TODO: allow customization.
;
(define (select-box-colors
    tools color-left fill-left color-right fill-right new-alpha)
;    (debug-message "SelectBox colors()")
;    tools->alpha = new-alpha
;
;    tools->left-pen.color = color-left
;    tools->left-pen.style = LINE-STYLE-DASHED
;    tools->left-brush.color = fill-left + new-alpha
;    tools->left-brush.style = BRUSH-STYLE-SOLID
;
;    tools->right-pen.color = color-right
;    tools->right-pen.style = LINE-STYLE-SOLID
;    tools->right-brush.color = fill-right + new-alpha
;    tools->right-brush.style = BRUSH-STYLE-SOLID
;
;    direction(tools->box-dir)
;
;    select-box-force-repaint()
)

; Carry out a paint given the current pen and brush.
; May need the canvas passing in.
;
(define (select-box-paint-event tools event)
;    painter = QPainter()
;    painter.pen(dir-pen)
;    painter.fill-rect(0, 0, width()-1, height()-1, dir-brush)
;    painter.draw-rect(0, 0, width()-1, height()-1)
)

; HACK: Take that QRubberBand!
;
(define (select-box-force-repaint)
;    hack = size()
;    resize(hack + (1, 1))
;    resize(hack)
)

(define (status-bar-update status-bar)

)

(define () status-bar-context-menu-event(WindowTab *status-bar, SDL-Event *event)
;    setOverrideCursor(Qt-ArrowCursor)
;    menu- = QMenu(this)
;    switch (object-name) {
;    case SNAP:
;        settingsSnapAction = Action(load-icon(gridsnapsettings-xpm), "Settings...", menu-)
;        connect(settingsSnapAction, SIGNAL(triggered()), this, SLOT(settingsSnap()))
;        menu-.addAction(settingsSnapAction)
;        break

;    case GRID:
;        settingsGridAction = Action(load-icon(gridsettings-xpm), "Settings...", menu-)
;        connect(settingsGridAction, SIGNAL(triggered()), this, SLOT(settingsGrid()))
;        menu-.addAction(settingsGridAction)
;        break

;    case RULER:
;        settingsRulerAction = Action( Icon("icons/rulersettings.png"), "Settings...", menu-)
;        connect(settingsRulerAction, SIGNAL(triggered()), this, SLOT(settingsRuler()))
;        menu-.addAction(settingsRulerAction)
;        break

;    case ORTHO:
;        settingsOrthoAction = Action( Icon("icons/orthosettings.png"), "Settings...", menu-)
;        connect(settingsOrthoAction, SIGNAL(triggered()), this, SLOT(settingsOrtho()))
;        menu-.addAction(settingsOrthoAction)
;        break

;    case POLAR:
;        settingsPolarAction = Action( Icon("icons/polarsettings.png"), "Settings...", menu-)
;        connect(settingsPolarAction, SIGNAL(triggered()), this, SLOT(settingsPolar()))
;        menu-.addAction(settingsPolarAction)
;        break

;    case QSNAP:
;        settingsQSnapAction = Action( Icon("icons/qsnapsettings.png"), "Settings...", menu-)
;        connect(settingsQSnapAction, SIGNAL(triggered()), this, SLOT(settingsQSnap()))
;        menu-.addAction(settingsQSnapAction)

;    case QTRACK:
;        settingsQTrackAction = Action( Icon("icons/qtracksettings.png"), "Settings...", menu-)
;        connect(settingsQTrackAction, SIGNAL(triggered()), this, SLOT(settingsQTrack()))
;        menu-.addAction(settingsQTrackAction)
;        break

;    case LWT:
;        gview = main-win.active-view()
;        if (gview) {
;            enable-real-action = Action(Icon("icons/realrender.png"), "RealRender On", menu-)
;            enable-real-action.setEnabled(!gview.isRealEnabled())
;            connect(enable-real-action, SIGNAL(triggered()), this, SLOT(enableReal()))
;            menu-.addAction(enable-real-action)

;            disable-real-action = Action(Icon("icons/realrender.png"), "RealRender Off", menu-)
;            disable-real-action.setEnabled(gview.isRealEnabled())
;            connect(disable-real-action, SIGNAL(triggered()), this, SLOT(disableReal()))
;            menu-.addAction(disable-real-action)
;        }

;        settingsLwtAction = Action(load-icon(lineweightsettings-xpm), "Settings...", menu-)
;        connect(settingsLwtAction, SIGNAL(triggered()), this, SLOT(settingsLwt()))
;        menu-.addAction(settingsLwtAction)
;        break

;    default:
;        break
;    }

;    menu-.exec(event.globalPos())
;    restoreOverrideCursor()
;    statusbar.clearMessage()
;    */
)

; TODO: set format from settings.
;
(define () status-bar-mouse-coord(WindowTab *tab, int x, int y)
;    if (tab->number-mode == ARCHITECTURAL) {
;        return
;    }
;    if (tab->number-mode == ENGINEERING) {
;        return
;    }
;    if (tab->number-mode == FRACTIONAL) {
;        return
;    }
;    if (tab->number-mode == SCIENTIFIC) {
;        /* status-bar-mouse-coord.setText("".setNum(x, 'E', 4)
;            + ", " + "".setNum(y, 'E', 4))
;        # TODO: use precision from unit settings */
;        return
;    }
;    /* Else decimal */
;    /*
;     * status-bar-mouse-coord.setText("".setNum(x, 'F', 4) + ", "
;     * + "".setNum(y, 'F', 4))
;     * #TODO: use precision from unit settings */
)

(define () status-bar-init(WindowTab *status-bar)
;    /*
(define ()
;--init--(self, buttonText, mw, statbar, parent)
;    statusbar = statbar

;    this.set-object-name("StatusBarButton" + buttonText)

;    this.setText(buttonText)
;    this.setAutoRaise(1)
;    this.setCheckable(1)

;    if (object-name >= 0 && object-name < N-STATUS) {
;        status[object-name] = !status[object-name]
;    }
)

; class StatusBar()
;/*
; * StatusBar( QWidget* parent = 0)
; * def setMouseCoord(x, y)
; */
;/*  def --init--(self, mw, parent)
;    this.set-object-name("StatusBar")

;    for i in range(N-STATUS)
;        status-bar[i] = StatusBarButton(status-bar-label[i], main-win, this, this)

;    status-bar-mouse-coord = tk.Label(this)

;    status-bar-mouse-coord.set-minimum-width(300)
;    # Must fit this text always
;    status-bar-mouse-coord.set-maximum-width(300)
;    # "+1.2345E+99, +1.2345E+99, +1.2345E+99"

;    this.add-widget(status-bar-mouse-coord)
;    for i in range(N-STATUS) {
;        this.add-widget(status-bar[i])
;    }
;    */
)

; The View class definition file.
;
; How we manage the content of the main editing area in the window.
;
; There are 4 regions managed as views, .
;
; We don't have a seperate window for the pop-ups like the file
; browser for opening or saving a file. Instead, a view will
; be created
;
(define (view-init view mw the-scene)
;    mw = mw
;    gscene = the-scene
;    frame-shape = "No frame"
;    hash-deleted-objects = {}
;    sparerubber-list = []
;    pan-distance = 0.0
;    pan-start-x = 0.0
;    pan-start-y = 0.0
;    rubber-room-list = 0
;    gripBase-obj = 0
;    tempBase-obj = 0
;    select-box = 0
;    cut-copy-mouse-point = 0
;    paste-object-item-group = 0
;    preview-object-list = 0
;    preview-object-item-group = 0
;    preview-point = 0
;    preview-data = 0
;    preview-mode = 0
;    origin-path = Path()
;    grid-color = Color()
;    grid-path = Path()
;*/
;    /* 
;    NOTE: self has to be done before setting mouse tracking.
;    TODO: Review OpenGL for Qt5 later
;    if settings.INT-DISPLAY-USE-OPENGL:
;        (debug-message "Using OpenGL...")
;        setViewport(new QGLWidget(QGLFormat(QGL-DoubleBuffer)))
;     */

;    /* TODO: Review RenderHints later
;    # set-render-hint(Painter-Antialiasing,
;    #               display-render-hintAA())
;    # set-render-hint(Painter-TextAntialiasing,
;    #               display-render-hintTextAA())
;    # set-render-hint(Painter-SmoothPixmapTransform,
;    #               display-render-hintSmoothPix())
;    # set-render-hint(Painter-HighQualityAntialiasing,
;    #               display-render-hintHighAA())
;    # set-render-hint(Painter-NonCosmeticDefaultPen,
;    #               display-render-hint-noncosmetic)

;    # NOTE
;    # ----
;    # FullViewportUpdate MUST be used for both the GL and Qt renderers.
;    # Qt renderer will not draw the foreground properly if it isnt set.
;    */ /*

;    setViewportUpdateMode(Graphicsdef-FullViewportUpdate)

;    pan-distance = 10
;    #TODO: should there be a setting for self???

;    set-cursor("BlankCursor")
;    horizontal-scroll-bar().set-cursor("ArrowCursor")
;    vertical-scroll-bar().set-cursor("ArrowCursor")
;    qsnap-locator-color = qsnap-locator-color
;    grip-color-cool = selection-coolgrip-color
;    grip-color-hot = selection-hotgrip-color
;    set-crosshair-color(display-crosshair-color))
;    set-cross-hair-size(display-crosshair-percent)
;    setgrid-color(grid-color)

;    if INT-GRID-SHOW-ON-LOAD:
;        create-grid(grid-type)
;    else {
;        create-grid("")

;    toggleRuler(ruler-show-on-load)
;    toggleReal(1)
;    #TODO: load self from file, else settings with default being 1

;    gripping-active = 0
;    rapid-move-active = 0
;    preview-mode = "PREVIEW-MODE-NULL"
;    preview-data = 0
;    preview-object-item-group = 0
;    paste-object-item-group = 0
;    preview-active = 0
;    pasting-active = 0
;    moving-active = 0
;    selecting-active = 0
;    zoom-window-active = 0
;    panning-real-time-active = 0
;    panning-point-active = 0
;    panning-active = 0
;    qsnap-active = 0
;    qsnap-toggle = 0
;*/
;    /* Randomize the hot grip location initially so it's not located at (0,0). */ /*
;    srand(1234)

;    sceneGripPoint = Vector((rand()%1000)*0.1, (rand()%1000)*0.1)

;    gripBase-obj = 0
;    tempBase-obj = 0

;    select-box = select-box("RubberBand-Rectangle")
;    select-box.set-colors(
;        display-select-box-left-color,
;        display-select-box-left-fill,
;        display-select-box-right-color,
;        display-select-box-right-fill,
;        display-select-box-alpha)

;    show-scroll-bars(display-show-scrollbars)
;    set-corner-button()

;    installEventFilter(void)

;    setMouseTracking(1)
;    set-background-color(display-bg-color)
;    /*  TODO: wrap self with a setBackgroundPixmap() function:
;          set-background-brush(Pixmap("images/canvas))

;    /* connect(gscene, SIGNAL(selection-changed()), self,
;        SLOT(selection-changed())) /*
)

; Prevent memory leaks by deleting any objects that were removed from the scene.
;
(define (delete-objects)
;  (delete-all hash-deleted-objects.begin() hash-deleted-objects.end())
;  (clear hash-deleted-objects)

  ; Prevent memory leaks by deleting any unused instances
;  (delete-all preview-object-list.begin() preview-object-list.end())
;  (clear preview-object-list)
)

; Selected objects are stored as a global variable indexed by tab.
; delta is a vector.
;
(define (move-selected delta)

)

; Selected objects are stored as a global variable indexed by tab.
; point1 and point2 are vectors.
;
(define (mirror-selected point1 point2)

)

; Sets the crosshair color for the current view.
;
(define (set-crosshair-color color)

)

(define ()
;set-crosshair-size(self, percent)
;    return
)

(define ()
;load-ruler-settings(void)
;    return
)

(define ()
;center(void)
;    return map-to-scene(rect().center())
)

(define ()
;enter-event(self, event)
;    mdi-win = mw
;    if mdi-win:
;        mdiArea.setActiveSubWindow(mdi-win)
)

(define ()
;add-object(self, obj)
;    gscene.addItem(-obj)
;    gscene.update()
;    hash-deleted-objects.remove(-obj.-objID)
)

(define ()
;delete-object(self, obj)
;    # NOTE: We really just remove the objects from the scene.
;    #       deletion actually occurs in the destructor.
;    obj.set-selected(0)
;    gscene.remove-item(-obj)
;    gscene.update()
;    hash-deleted-objects.insert(-obj.-objID, obj)
)

(define ()
;preview-on(self, clone, mode, x, y, data)
;    (debug-message "View preview-on()")
;    preview-off()
;    # Free the old objects before creating ones

;    preview-mode = mode

;    # Create objects and add them to the scene in an item group.
;    if clone == "PREVIEW-CLONE-SELECTED":
;        preview-object-list = create-object-list(gscene.selected-items())
;    elif clone == PREVIEW-CLONE-RUBBER:
;        preview-object-list = create-object-list(rubber-room-list)
;    else {
;        return
;    preview-object-item-group = gscene.create-item-group(preview-object-list)

;    if (preview-mode == PREVIEW-MODE-MOVE ||
;        preview-mode == "PREVIEW-MODE-ROTATE" ||
;        preview-mode == "PREVIEW-MODE-SCALE") {
;        preview-point = Vector(x, y)
;        # NOTE: Move: basePt
;        # Rotate: basePt
;        # Scale: basePt
;        preview-data = data
;        # NOTE: Move: unused
;        # Rotate: refAngle
;        # Scale: refFactor
;        preview-active = 1
;    }
;    else {
;        preview-mode = PREVIEW-MODE-NULL
;        preview-point = Vector()
;        preview-data = 0
;        preview-active = 0
;    }

;    gscene.update()
)

(define ()
;preview-off(void)
;    " , "
;    # Prevent memory leaks by deleting any unused instances.
;    DeleteAll(preview-object-list.begin(), preview-object-list.end())
;    preview-object-list.clear()

;    if preview-object-item-group:
;        gscene.remove-item(preview-object-item-group)
;        del preview-object-item-group
;        preview-object-item-group = 0

;    preview-active = 0

;    gscene.update()
;*/

(define ()
;enable-move-rapid-fire(void)
;    (debug-message "Enabling rapid move.")
;    rapid-move-active = 1
)

(define ()
;disable-move-rapid-fire(void)
;    (debug-message "Disabling rapid move.")
;    rapid-move-active = 0
)

;/* TODO: This check should be removed later.
; */
(define ()
;allow-rubber(void)
;    /* return not rubber-room-list.size()
)

(define ()
;add-to-rubber-room(int item)
;    /*
;    rubber-room-list.append(item)
;    item.show()
;    gscene.update()
;    */
)

(define ()
;vulcanize-rubber-room(void)
;    /*
;    for (base in rubber-room-list) {
;        if (base) {
;            vulcanize-object(base)
;        }
;    }

;    rubber-room-list.clear()
;    gscene.update()
;    */
)

(define ()
;vulcanize-object(int obj)
;    /*
;    if (!obj) {
;        return
;    }
;    gscene.remove-item(-obj)
;    # Prevent Qt Runtime Warning, QGraphicsScene-addItem:
;    # item has alreadelta-y been added to self scene.
;    obj.vulcanize()
)

(define ()
;clear-rubber-room(void)
;    /*
;    for (item in rubber-room-list) {
;        if (item) {
;            if ((item.type == OBJ-TYPE-PATH
;             && spare-rubber-list.contains("SPARE-RUBBER-PATH")) ||
;            (item.type == OBJ-TYPE-POLYGON
;             && spare-rubber-list.contains("SPARE-RUBBER-POLYGON")) ||
;            (item.type == OBJ-TYPE-POLYLINE
;             && spare-rubber-list.contains("SPARE-RUBBER-POLYLINE")) ||
;            (sparerubber-list.contains(item.-objID))) {
;                if (!item.-objectPath().element-count(void) {
;                    error-title = translate("Empty Rubber object Error")
;                    error-message = translate(
;"The rubber object added contains no points. "
;+ "The command that created self object has flawed logic. "
;+ "The object will be deleted.")
;                    critical(error-title, error-message)
;                    gscene.remove-item(item)
;                    del item
;                }
;                else {
;                    vulcanize-object(item)
;                }
;            }
;            else {
;                gscene.remove-item(item)
;                del item
;            }
;        }
;    }

;    rubber-room-list.clear()
;    spare-rubber-list.clear()
;    gscene.update()
;    */
)

(define ()
;spare-rubber(int id)
;    /* spare-rubber-list.append(id); */
)

(define ()
;set-rubber-mode(int mode)
;    /*
;    for item in rubber-room-list) {
;        if item) {
;            item.set-object-rubber-mode(mode)
;        }
;    }

;    gscene.update()
;    */
)

; key (string)
; point (vector)
;
(define (set-rubber-point key point)
;  (let*
;    for item in rubber-room-list) {
;        if item) {
;            item.set-object-rubber-point(key, point)
;        }
;    }

;    (update-scene)
;    )
)

; key (string)
; txt (string)
;
(define (set-rubber-text key txt)
   (let*
;    for (item in rubber-room-list) {
;        if (item) {
;            item.set-objectRubberText(key, txt)
;        }
;    }
      (update-scene)))

; (EmbColor color)
;
(define (set-grid-color color)
;    grid-color = color
;    gscene.set-property("VIEW-COLOR-GRID", color)
;    if (gscene) {
;        gscene.update()
;    }
)

; color (EmbColor)
;
(define (set-ruler-color color)
;    (define (ruler-color) color)
;    (update-scene)
)

(define ()
;set-grid(int active)
;    (debug-message "View toggleGrid()")
;    /* set-override-cursor("WaitCursor")
;    if on) {
;        create-grid(grid-type)
;    else {
;        create-grid("")
;    }
;    restore-override-cursor()
)

(define ()
;set-ruler(int active)
;    (debug-message "View toggle-ruler()")
;    /*
;    set-override-cursor("WaitCursor")
;    gscene.set-property("ENABLE-RULER", active)
;    ruler-color = Color(ruler-color)
;    gscene.update()
;    restore-override-cursor()
)

(define ()
;set-ortho(int active)
;    (debug-message "View toggleOrtho()")
;    /* set-override-cursor("WaitCursor")
;    /* TODO: finish this. */ /*
;    gscene.set-property("ENABLE-ORTHO", active)
;    gscene.update()
;    restore-override-cursor()
)

(define ()
;set-polar(int active)
;    (debug-message "View togglePolar()")
;    /*
;    set-override-cursor("WaitCursor")
;    /* TODO: finish this. */ /*
;    gscene.set-property("ENABLE-POLAR", active)
;    gscene.update()
;    restore-override-cursor()
)

(define ()
;set-qsnap(int active)
;    (debug-message "View toggleQSnap()")
;    /*
;    set-override-cursor("WaitCursor")
;    qsnap-toggle = on
;    gscene.set-property("ENABLE-QSNAP", active)
;    gscene.update()
;    restore-override-cursor()
)

;/* TODO: finish this.
; */
(define ()
;set-qtrack(int active)
;    (debug-message "View toggleQTrack()")
;    /*
;    set-override-cursor("WaitCursor")
;    gscene.set-property("ENABLE-QTRACK", active)
;    gscene.update()
;    restore-override-cursor()
;    */
)

(define ()
;set-lwt(int active)
;    (debug-message "View toggleLwt()")
;    /*
;    set-override-cursor("WaitCursor")
;    gscene.set-property("ENABLE-LWT", active)
;    gscene.update()
;    restore-override-cursor()
)

(define ()
;set-real(int active)
;    (debug-message "View toggleReal()")
;    /*
;    set-override-cursor("WaitCursor")
;    gscene.set-property("ENABLE-REAL", active)
;    gscene.update()
;    restore-override-cursor()
)

;/* lwt and real should be per-document
; */
(define ()
;is-lwt-enabled(void)
;    /* return gscene.property("ENABLE-LWT"); */
)

(define ()
;is-real-enabled(void)
;    /* return gscene.property("ENABLE-REAL"); */
)

(define ()
;update-mouse-coords(EmbVector position)
;    /*
;    view-mouse-point = Vector(x, y)
;    scene-mouse-point = to-emb-vector(map-to-scene(view-mouse-point))
;    gscene.set-property("SCENE-QSNAP-POINT", scene-mouse-point); */
;    /* TODO: if qsnap functionality is enabled, use it rather than the mouse point. */ /*
;    gscene.set-property("SCENE-MOUSE-POINT", scene-mouse-point)
;    gscene.set-property("VIEW-MOUSE-POINT", view-mouse-point)
;    statusbar.setMouseCoord(scene-mouse-point.x, -scene-mouse-point.y)
)

;/* 
; * NOTE:
; * crosshair-size is in pixels and is a percentage of your screen width
; * Example: (1280*0.05)/2 = 32, thus 32 + 1 + 32 = 65 pixel wide crosshair.
; */
(define ()
;set-crossHairSize(double percent)
;    /*
;    screen-width = qApp.screens()[0].geometry().width()
;    if (percent > 0 && percent < 100) {
;        crosshair-size = (screen-width*(percent/100.0))/2
;    }
;    else {
;        crosshair-size = screen-width
;    }
;    */
)

(define ()
;set-corner-button(void)
;    /*
;    num = display-scrollbar-widget-num
;    if (num) {
;        cornerButton = tk.PushButton(void)
;        cornerButton.setFlat(1)
;        act = action-hash.value(num)
;        /* NOTE: Prevent crashing if the action is NULL. */ /*
;        if (!act) {
;            error-title = translate("Corner Widget Error")
;            message = translate("There are unused enum values in COMMAND-ACTIONS. Please report self as a bug.")
;            information(error-title, message)
;            setCornerWidget(0)
;        }
;        else {
;            cornerButton.setIcon(act.icon())
;            # connect(cornerButton, SIGNAL(clicked()), self, SLOT(cornerButtonClicked()))
;            setCornerWidget(cornerButton)
;            cornerButton.set-cursor(Qt-ArrowCursor)
;        }
;    }
;    else {
;        setCornerWidget(0)
;    }
;    */
)

(define ()
;cornerButtonClicked(void)
;    /*
;    (debug-message "Corner Button Clicked.")
;    display = display-scrollbar-widget-num
;    action-hash.value(display).trigger()
;    */
)

(define ()
;selection-changed(void)
;    /*
;    if dock-prop-edit.isVisible()
;        dock-prop-edit.setselected-items(gscene.selected-items())
;    */
)

(define ()
;mouse-double-click-event(SDL-Event event)
;     /*
;    if event.button() == "LeftButton":
;        item = gscene.itemAt(map-to-scene(event.pos()), QTransform())
;        if item:
;            dock-prop-edit.show()
;    */
)

(define ()
;mouse-press-event(SDL-Event event)
;    /*
;    update-mouse-coords(event.x, event.y)
;    if (event.button() == "LeftButton") {
;        path = Path()
;        pickList = gscene.items(Rect(map-to-scene(
;            view-mouse-point.x()-pickBoxSize,
;            view-mouse-point.y()-pickBoxSize),
;            map-to-scene(view-mouse-point.x()+pickBoxSize,
;            view-mouse-point.y()+pickBoxSize)))

;        itemsInPickBox = pickList.size()
;        if (itemsInPickBox && !selecting-active && !gripping-active) {
;            itemsAlreadelta-ySelected = pickList.at(0).is-selected()
;            if (!itemsAlreadelta-ySelected) {
;                pickList.at(0).set-selected(1)
;            }
;            else {
;                foundGrip = 0
;                base = pickList[0]
;                #TODO: Allow multiple objects to be gripped at once
;                if (!base) {
;                    return
;                }

;                qsnap-offset = Vector(qsnap-locator-size, qsnap-locator-size)
;                gripPoint = base.mouseSnapPoint(scene-mouse-point)
;                p1 = map-from-scene(gripPoint) - qsnap-offset
;                q1 = map-from-scene(gripPoint) + qsnap-offset
;                gripRect = Rect(map-to-scene(p1), map-to-scene(q1))
;                pickRect = Rect(map-to-scene(view-mouse-point.x()-pickBoxSize, view-mouse-point.y()-pickBoxSize),
;                                map-to-scene(view-mouse-point.x()+pickBoxSize, view-mouse-point.y()+pickBoxSize))
;                if gripRect.intersects(pickRect)
;                    foundGrip = 1

;                /* If the pick point is within the item's grip box,
;                    * start gripping.
;                    */ /*
;                if (foundGrip) {
;                    start-gripping(base)
;                }
;                else { */
;                    /* start moving */ /*
;                    moving-active = 1
;                    pressPoint = event.pos()
;                    scenePressPoint = map-to-scene(pressPoint)
;                }

;        elif (gripping-active) {
;            stop-gripping(1)
;        }
;        elif (!selecting-active) {
;            selecting-active = 1
;            pressPoint = event.pos()
;            scenePressPoint = map-to-scene(pressPoint)

;            if (!select-box:
;                select-box = select-box(QRubberBand-Rectangle)
;            select-box.set-geometry(Rect(pressPoint, pressPoint))
;            select-box.show()
;        }
;        else {
;            selecting-active = 0
;            select-box.hide()
;            releasePoint = event.pos()
;            scene-release-point = map-to-scene(releasePoint)

;            #Start select-box Code
;            path.add-polygon(map-to-scene(select-box.geometry()))
;            if (scene-release-point.x > scenePressPoint.x) {
;                if (selection-mode-pickadd) {
;                    if (shift-key) {
;                        item-list = gscene.items(path, "ContainsItemShape")
;                        for item in item-list:
;                            item.set-selected(0)

;                    else {
;                        item-list = gscene.items(path, "ContainsItemShape")
;                        for item in item-list:
;                            item.set-selected(1)
;                    }
;                }
;                else {
;                    if (shift-key) {
;                        item-list = gscene.items(path, "ContainsItemShape")
;                        if (!item-list.size()
;                            clear-selection()
;                        else {
;                            for item in item-list:
;                                item.set-selected(!item.is-selected()) #Toggle selected

;                    else {
;                        clear-selection()
;                        item-list = gscene.items(path, "ContainsItemShape")
;                        for item in item-list:
;                            item.set-selected(1)
;            }
;            else {
;                if (selection-mode-pickadd) {
;                    if (shift-key) {
;                        item-list = gscene.items(path, "intersects-item-shape")
;                        for item in item-list) {
;                            item.set-selected(0)
;                        }
;                    }
;                    else {
;                        item-list = gscene.items(path, "intersects-item-shape")
;                        for (item in item-list) {
;                            item.set-selected(1)
;                        }
;                    }
;                }
;                else {
;                    if (shift-key) {
;                        item-list = gscene.items(path, "intersects-item-shape")
;                        if (!item-list.size(void)
;                            clear-selection()

;                        else {
;                            for item in item-list:
;                                item.set-selected(!item.is-selected())
;                                #Toggle selected

;                    }
;                    else {
;                        clear-selection()
;                        item-list = gscene.items(path, "intersects-item-shape")
;                        for item in item-list) {
;                            item.set-selected(1)
;                        }
;                   }
;               }
;            #End select-box Code

;        if (pasting-active) {
;            item-list = paste-object-item-group.childItems()
;            gscene.destroy-item-group(paste-object-item-group)
;            for item in item-list:
;                gscene.remove-item(item)
;                # Prevent Qt Runtime Warning,
;                # QGraphicsScene-addItem: item has alreadelta-y been
;                # added to self scene

;            for item in item-list:
;                if item:
;                    (debug-message "TODO: Loop bodelta-y")

;            pasting-active = 0
;            selecting-active = 0

;        if zoom-window-active:
;            fit-in-view(path.bounding-rect(), Qt-KeepAspectRatio)
;            clear-selection()

;    if event.button() == "MiddleButton":
;        pan-start(event.pos())
;        #The Undo command will record the spot where the pan started.
;        event.accept()

;    gscene.update()
;*/
)

(define ()
;pan-start(EmbVector point)
;    /*
;    recalculate-limits()

;    align-scene-point-withViewPoint(map-to-scene(point), point)

;    panning-active = 1
;    pan-start = point
;    */
)

;/*
; * NOTE:
; * Increase the scene-rect limits if the point we want to go to lies outside of scene-rect's limits
; * If the scene-rect limits aren't increased, you cannot pan past its limits
; */
(define ()
;recalculate-limits(void)
;    SDL-Rect scene-rect, new-rect, rect
;    /*
;    viewRect = Rect(map-to-scene(rect().top-left()), map-to-scene(rect().bottom-right()))
;    scene-rect = gscene.scene-rect()
;    new-rect = viewRect.adjusted(
;        -viewRect.width(), -viewRect.height(),
;        viewRect.width(), viewRect.height())
;    if (!scene-rect.contains(new-rect.top-left()) || !scene-rect.contains(new-rect.bottom-right()) {
;        rect = scene-rect.adjusted(
;            -viewRect.width(), -viewRect.height(),
;            viewRect.width(), viewRect.height())
;        gscene.setscene-rect(rect)
;    }
;    */
)

;/*
;    center-on also updates the scrollbars,
;    which shifts things out of wack o-O
; */
(define ()
;center-at(EmbVector centerPoint)
;     /*
;    center-on(centerPoint)
;    # Reshift to the center
;    offset = centerPoint - center()
;    new-center = centerPoint + offset
;    center-on(new-center)
;    */
)

;/* center-on also updates the scrollbars, which shifts things out of wack o-O
; */
(define ()
;align-scene-point-with-view-point(EmbVector scene-point, EmbVector view-point)
;    /*
;    view-center = center()
;    point-before = scene-point
;    center-on(view-center)
;    #Reshift to the center so the scene and view points align
;    point-after = map-to-scene(view-point)
;    offset = point-before - point-after
;    new-center = view-center + offset
;    center-on(new-center)
;    */
)

(define ()
;mouse-move-event(SDL-Event event)
;    /*
;    mouse = Cursor-pos()
;    update-mouse-coords(mouse.x(), mouse.y())
;    move-point = event.pos()
;    scenemove-point = map-to-scene(move-point)
;    */

;    if (preview-active) {
;        /*
;        if (preview-mode == "PREVIEW-MODE-MOVE") {
;            preview-object-item-group.set-pos(scene-mouse-point - preview-point)
;        }
;        elif (preview-mode == "PREVIEW-MODE-ROTATE") {
;            x = preview-point.x()
;            y = preview-point.y()
;            mouse-angle = Line(x, y, scene-mouse-point.x, scene-mouse-point.y).angle()

;            rad = radians(preview-data-mouse-angle)
;            p = Vector(-x, -y)
;            rot = rotate-vector(p, rad)
;            rot.x += x
;            rot.y += y

;            preview-object-item-group.set-pos(rot.x, rot.y)
;            preview-object-item-group.set-rotation(preview-data-mouse-angle)
;        }
;        elif (preview-mode == "PREVIEW-MODE-SCALE") {
;            x = preview-point.x
;            y = preview-point.y
;            scale-factor = preview-data

;            factor = Line(x, y, scene-mouse-point.x, scene-mouse-point.y).length() / scale-factor

;            preview-object-item-group.setScale(1)
;            preview-object-item-group.set-pos(0,0)

;            if (scale-factor <= 0.0) {
;                message = "Hi there. If you are not a developer, report this as a bug."
;                message += " If you are a developer, your code needs examined,"
;                message += " and possibly your head too."
;                critical(self, translate("scale-factor Error"), translate(message))

;            else {
;                # Calculate the offset
;                old = Vector(0, 0)
;                scale-line = Line(x, y, old.x, old.y)
;                scale-line.set-length(scale-line.length()*factor)

;                delta-x = scale-line.point2-x() - old.x
;                delta-y = scale-line.point2-y() - old.y
;            }
;        }
;        */
;    }
;    /*
;                preview-object-item-group.setScale(preview-object-item-group.scale()*factor)
;                preview-object-item-group.moveBy(delta-x, delta-y)
;    */

;    if (pasting-active) {
;        /*
;        v = scene-mouse-point.subtract(pasteDelta)
;        paste-object-item-group.set-pos(v)
;        */
;    }

;    if (moving-active) {
;        /* Ensure that the preview is only shown if the mouse has moved. */
;        if (!preview-active) {
;            /* preview-on("PREVIEW-CLONE-SELECTED", "PREVIEW-MODE-MOVE",
;                   scenePressPoint.x(), scenePressPoint.y(), 0);  */
;        }
;    }

;    if (selecting-active) {
;        /*
;        if (scenemove-point.x() >= scenePressPoint.x(void)) {
;            select-box.setDirection(1)
;        }

;        else { select-box.setDirection(0)
;        select-box.set-geometry(
;            Rect(map-from-scene(scenePressPoint), event.pos()).normalized())
;        event.accept()
;        */
;    }

;    if (panning-active) {
;        /*
;        horizontal-scroll-bar().set-value(
;            horizontal-scroll-bar().value() - (event.x() - pan-start-x))
;        vertical-scroll-bar().set-value(
;            vertical-scroll-bar().value() - (event.y() - pan-start-y))
;        pan-start.x = event.x
;        pan-start.y = event.y
;        event.accept()
;        */
;    }

;    /* gscene.update()
;    */
)

(define ()
;mouse-release-event(SDL-Event event)
;    /*
;    update-mouse-coords(event)
;    if (event.button() == "left-button") {
;        if (moving-active) {
;            preview-off()
;            delta = scene-mouse-point.subtract(scene-press-point)
;            /* Ensure that moving only happens if the mouse has moved. */ /*
;            if (delta.x or delta.y) {
;                moveSelected(delta)
;            }
;            moving-active = 0
;        }

;        event.accept()
;    }

;    if (event.button() == "MiddleButton") {
;        panning-active = 0 */
;        /* The Undo command will record the spot where the pan completed. */ /*
;        event.accept()
;    }

;    if (event.button() == "XButton1") {
;        (debug-message "XButton1")
;        main-undo(); */
;        /*  TODO: Make this customizable */ /*
;        event.accept()
;    }

;    if (event.button() == "XButton2") {
;        (debug-message "XButton2")
;        main-redo(); */
;        /* TODO: Make this customizable */ /*
;        event.accept()
;    }
;    gscene.update();*/
)

(define ()
;wheel-event(SDL-Event event)
;    double zoomDir = 1.0
;    /* zoomDir = event.pixel-delta().y; */
;    /*  TODO: double check self */
;    /*mousePoint = event.global-pos(); */
;    /* TODO: self is causing weird versioning errors, */
;    /* this appears to be supported on Qt5.12. */
;    /* update-mouse-coords(mousePoint.x(), mousePoint.y()); */
;    if (zoomDir > 0) {
;        (debug-message ".")
;    }
;    else {
;        (debug-message ".")
;    }
)

(define ()
;zoom-to-point(EmbVector mouse-point, float zoom-dir)
;    double s
;    /*
;    point-before-scale(map-to-scene(mouse-point))

;    # Do The zoom
;    s = 1.0
;    if (zoom-dir > 0) {
;        if (!allow-zoom-in()) {
;            return
;        }
;        s = display-zoom-scale-action-in
;    }
;    else {
;        if (!allow-zoom-out()) {
;            return
;        }
;        s = display-zoom-scale-action-out
;    }

;    scale(s, s)
;    align-scene-point-with-view-point(point-before-scale, mouse-point)
;    recalculate-limits()
;    align-scene-point-with-view-point(point-before-scale, mouse-point)

;    update-mouse-coords(mouse-point.x(), mouse-point.y())
;    if pasting-active:
;        v = scene-mouse-point.subtract(paste-delta)
;        paste-object-item-group.set-pos(v)

;    if (selecting-active) {
;        rect = Rect(map-from-scene(scenePressPoint), mousePoint).normalized()
;        select-box.set-geometry(rect)
;    }

;    gscene.update()
;    */
)

(define ()
;context-menu-event(SDL-Event event)
;    int i
;    /*
;    iconTheme = general-icon-theme

;    menu = ""
;    item-list = gscene.selected-items()
;    selection-empty = item-list.is-empty()

;    for (i=0; i<len(item-list); i++) {
;        if (item-list[i].type != "Not Set") {
;            selection-empty = 0
;            break
;        }
;    } */

;    if (pasting-active) {
;        return
;    }

;    /*
;    if (zoom-window-active) {
;        cancel-zoom-win-action = Action("&Cancel (zoom-window-action)")
;        cancel-zoom-win-action.set-status-tip("Cancels the zoom-window-action Command.")
;        # connect(cancel-zoom-win-action, SIGNAL(triggered()), self, SLOT(escapePressed()))
;        menu.add-action(cancel-zoom-win-action)
;    }

;    menu.add-separator()
;    menu.add-action(action-hash.value("cut"))
;    menu.add-action(action-hash.value("copy"))
;    menu.add-action(action-hash.value("paste"))
;    menu.add-separator()

;    if (!selection-empty) {
;        delete-action = Action(load-icon(erase-xpm), "D&elete")
;        status-tip = "Removes objects from a drawing."
;        delete-action.set-status-tip(status-tip)
;        # connect(delete-action, SIGNAL(triggered()), self, SLOT(deleteSelected()))
;        menu.add-action(delete-action)

;        move-action = Action(load-icon(move-xpm), "&Move")
;        status-tip = "Displaces objects a specified distance in a specified direction."
;        move-action.set-status-tip(status-tip)
;        connect(move-action, SIGNAL(triggered()), self, SLOT(move-action())) /*
;        menu.add-action(move-action)

;        scale-action = Action(load-icon(scale-xpm), "Sca&le")
;        status-tip = "Enlarges or reduces objects proportionally in the X, Y, and Z directions."
;        scale-action.set-status-tip(status-tip)
;        */ /* connect(scale-action, SIGNAL(triggered()), self, SLOT(scale-action())) /*
;        menu.add-action(scale-action)

;        rotate-action = Action(load-icon(rotate-xpm), "R&otate")
;        status-tip = "Rotates objects about a base point."
;        rotate-action.set-status-tip(status-tip)
;        connect(rotate-action, SIGNAL(triggered()), self, SLOT(rotate-action())) /*
;        menu.add-action(rotate-action)

;        menu.add-separator()

;        clear-action = Action("Cle&ar Selection")
;        clear-action.set-status-tip("Removes all objects from the selection set.")
;        connect(clear-action, SIGNAL(triggered()), self, SLOT(clear-selection())) /*
;        menu.add-action(clear-action)
;    }

;    menu.exec(event.globalPos())
)

(define ()
;delete-pressed(void)
;    (debug-message "View delete-pressed()")
;    /*
;    set-override-cursor = tk.Application("WaitCursor")
;    mdi-win = mdi-area.active-sub-window()
;    if (mdi-win) {
;        mdi-win.deletePressed()
;    }
;    restore-override-cursor()
;    */
;    if (pasting-active) {
;        /*
;        gscene.remove-item(paste-object-item-group)
;        del paste-object-item-group
;        */
;    }

;    pasting-active = 0
;    zoom-window-active = 0
;    selecting-active = 0
;    /*
;    select-box.hide()
;    stop-gripping(0)
;    deleteSelected()
;    */
)

(define (escape-pressed)
;    (debug-message "View escape-pressed()")
;    if (pasting-active) {
;        /*
;        gscene.remove-item(paste-object-item-group)
;        del paste-object-item-group
;        */
;    }

;    pasting-active = 0
;    zoom-window-active = 0
;    selecting-active = 0
;    /*
;    select-box.hide()
;    if (gripping-active) {
;        stop-gripping(0)
;    }
;    else {
;        clear-selection()
;    }
;    set-override-cursor("WaitCursor")
;    mdi-win = mdi-area.active-sub-window()
;    if mdi-win:
;        mdi-win.escapePressed()
;    restoreOverrideCursor()

;    gview = active-view()
;    if (gview) {
;        gview.clearRubberRoom()
;        gview.previewOff()
;        gview.disableMoveRapidFire()
;    }
;    */
)

(define (start-gripping obj)
   (if (obj)
      (let*
         (define (gripping-active) 1)
         (define (gripBase-obj) obj)
;    sceneGripPoint = gripBase-obj.mouseSnapPoint(scene-mouse-point)
;    gripBase-obj.set-object-rubber-point("GRIP-POINT", sceneGripPoint)
;    gripBase-obj.set-object-rubber-mode("OBJ-RUBBER-GRIP")
    )))

(define (stop-gripping accept)
   (let*
      (define (gripping-active) 0)
;    if (gripBase-obj) {
;        gripBase-obj.vulcanize()
;        if (accept) {
;            selection-changed(); */
;            /*  Update the Property Editor */ /*
;        }

;        gripBase-obj = 0
;    }
;    */
    ; Move the sceneGripPoint to a place where it will never be hot.
;    /* sceneGripPoint = scene-rect().top-left(); */
   ))

Arc
Geometry
Center X,double,user
Center Y,double,user
Radius,double,user
Start Angle,double,user
End Angle,double,user
Start X,double,system
Start Y,double,system
End X,double,system
End Y,double,system
Area,double,system
Length,double,system
Chord,double,system
Included Angle,double,system
END,END,END

char *arc-properties[] = {
    "Center X,double,user",
    "Center Y,double,user",
    "Radius,double,user",
    "Start Angle,double,user",
    "End Angle,double,user",
    "Start X,double,system",
    "Start Y,double,system",
    "End X,double,system",
    "End Y,double,system",
    "Area,double,system",
    "Length,double,system",
    "Chord,double,system",
    "Included Angle,double,system",
    "END,END,END"
}

PropertyBox arc-tab = {
    "Arc Properties",
    OBJ-TYPE-ARC,
    arc-properties
}

Circle
Geometry
Center X,double,user
Center Y,double,user
Radius,double,user
Diameter,double,system
Area,double,system
Circumference,double,system
END,END,END

Ellipse
Geometry
Center X,double,system
Center Y,double,system
Radius Major,double,system
Radius Minor,double,system
Diameter Major,double,system
Diameter Minor,double,system
END,END,END

Settings Tabs
    "General",
    "Files/Path",
    "Display",
    "Open/Save",
    "Printing",
    "Snap",
    "Grid/Ruler",
    "Ortho/Polar",
    "QuickSnap",
    "QuickTrack",
    "LineWeight",
    "Selection"

Image
GroupBox,Geometry
Position X,double,system
Position Y,double,system
Width,double,system
Height,double,system
END,END,END
GroupBox,Misc
Name,double,system
Path,double,system
END,END,END

Infinite Line
GroupBox,Geometry
X1,double,user
Y1,double,user
X2,double,user
Y2,double,user
Vector X,double,system
Vector Y,double,system
END,END,END

(define (statusbar-labels)
  (vector
    "SNAP"
    "GRID"
    "RULER"
    "ORTHO"
    "POLAR"
    "QSNAP"
    "QTRACK"
    "LWT"
    "END"
  )
)

(define (geometry-rect-properties)
   (vector
      "Rect"
      "GroupBox" "Geometry"
      "Corner X1" "double" "user"
      "Corner Y1" "double" "user"
      "Corner X2" "double" "user"
      "Corner Y2" "double" "user"
      "Corner X3" "double" "user"
      "Corner Y3" "double" "user"
      "Corner X4" "double" "user"
      "Corner Y4" "double" "user"
      "Height" "double" "user"
      "Width" "double" "user"
      "Area" "double" "system"
      "END" "END" "END"
   )
)

(define (details-labels)
  (vector
    "Total Stitches:"
    "Real Stitches:"
    "Jump Stitches:"
    "Trim Stitches:"
    "Total Colors:"
    "Color Changes:"
    "Left:"
    "Top:"
    "Right:"
    "Bottom:"
    "Width:"
    "Height:"
  )
)

