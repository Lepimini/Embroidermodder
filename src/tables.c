/* This file is part of Embroidermodder 2.
 *
 * -----------------------------------------------------------------------------
 *
 * Copyright 2013-2022 The Embroidermodder Team
 * Embroidermodder 2 is Open Source Software under the zlib licence.
 * See LICENCE for details.
 *
 * -----------------------------------------------------------------------------
 *
 * The data that corresponds to simple tables in the docs.
 */

#include "embroidermodder.h"

const char *tips[] = {
    "we need more tips?",
    "you can change the color of the display through settings?",
    "you can hide the scrollbars to increase the viewable area through settings?",
    "you can change the icon size for increased visibility?",
    "you can toggle the grid on and off by pressing the button in the statusbar?",
    "the grid size can be changed to match your hoop size through settings?",
    "the crosshair size is based on a percentage of your screen size? Setting it to 100 may help you visually line things up better.",
    "you can pan by pressing the middle mouse button and dragging your mouse across the screen?",
    "you can open and edit multiple designs simultaneously?",
    "that many embroidery machines support the .dst format?",
    "that you can zoom in and out using your mouse wheel?",
    "that you can use circular and isometric grids?",
    "about our command line format converter?",
    "that you can use the 'DAY' and 'NIGHT' commands to quickly switch the view colors to commonly used white or black?",
    "that you can quickly change the background, crosshair and grid colors using the 'RGB' command?",
    "\0",
};

const char *details_label_text[] = {
    "Total Stitches:",
    "Real Stitches:",
    "Jump Stitches:",
    "Trim Stitches:",
    "Total Colors:",
    "Color Changes:",
    "Left:",
    "Top:",
    "Right:",
    "Bottom:",
    "Width:",
    "Height:",
};

const char *obj_names[] = {
    "Unknown",
    "Base",
    "Arc",
    "Block",
    "Circle",
    "Aligned Dimension",
    "Angular Dimension",
    "Arc Length Dimension",
    "Diameter Dimension",
    "Leader Dimension",
    "Linear Dimension",
    "Ordinate Dimension",
    "Radius Dimension",
    "Ellipse",
    "Elliptical Arc",
    "Rubber",
    "Grid",
    "Hatch",
    "Image",
    "Infinite Line",
    "Line",
    "Path",
    "Point",
    "Polygon",
    "Polyline",
    "Ray",
    "Rectangle",
    "Slot",
    "Spline",
    "Multi Line Text",
    "Single Line Text",
    "Unknown",
};

const char *toolbar_label[] = {
    "File",
    "Edit",
    "View",
    "Zoom",
    "Pan",
    "Icon",
    "Help",
    "Layer",
    "Text",
    "Properties",
};

const char *menu_label[] = {
    "&File",
    "&Edit",
    "&View",
    "&Settings",
    "&Window",
    "&Help",
    "Open &Recent",
    "&Zoom",
    "&Pan",
};

const char *status_bar_label[] = {
    "SNAP",
    "GRID",
    "RULER",
    "ORTHO",
    "POLAR",
    "QSNAP",
    "QTRACK",
    "LWT",
};

const char *folders[] = {
    "",
    "commands",
    "help",
    "icons",
    "images",
    "samples",
    "translations",
};

const char *settings_tab_label[] = {
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
    "Selection",
};

const char *origin_string[] = {
    "M 0.0 0.5",
    "A -0.5 -0.5 1.0 1.0 90.0 360.0",
    "A -0.5 -0.5 1.0 1.0 90.0 -360.0",
    "L 0.0 -0.5",
    "A -0.5 -0.5 1.0 1.0 270.0 90.0",
    "L -0.5 0.0",
    "A -0.5 -0.5 1.0 1.0 180.0 -90.0",
    "Z",
    "\0"
};

int file_toolbar[] = {
    ACTION_new,
    ACTION_open,
    ACTION_save,
    ACTION_saveas,
    ACTION_print,
    ACTION_designdetails,
    -1,
    ACTION_undo,
    ACTION_redo,
    -1,
    ACTION_help,
    -2
};

int edit_toolbar[] = {
    ACTION_cut,
    ACTION_copy,
    ACTION_paste,
    -2
};

int view_toolbar[] = {
    ACTION_day,
    ACTION_night,
    -2
};

int pan_toolbar[] = {
    ACTION_panrealtime,
    ACTION_panpoint,
    -1,
    ACTION_panleft,
    ACTION_panright,
    ACTION_panup,
    ACTION_pandown,
    -2
};

int icon_toolbar[] = {
    ACTION_icon16,
    ACTION_icon24,
    ACTION_icon32,
    ACTION_icon48,
    ACTION_icon64,
    ACTION_icon128,
    -2
};

int help_toolbar[] = {
    ACTION_help,
    -1,
    ACTION_changelog,
    -1,
    ACTION_about,
    -1,
    ACTION_whatsthis,
    -2
};

int zoom_toolbar[] = {
    ACTION_zoomwindow,
    ACTION_zoomdynamic,
    ACTION_zoomscale,
    -1,
    ACTION_zoomcenter,
    ACTION_zoomin,
    ACTION_zoomout,
    -1,
    ACTION_zoomselected,
    ACTION_zoomall,
    ACTION_zoomextents,
    -2
};

int layer_toolbar[] = {
    -2
};

int text_toolbar[] = {
    -2
};

int properties_toolbar[] = {
    -2
};

int *toolbars[] = {
    file_toolbar,
    edit_toolbar,
    view_toolbar,
    zoom_toolbar,
    pan_toolbar,
    icon_toolbar,
    help_toolbar,
    layer_toolbar,
    text_toolbar,
    properties_toolbar
};


int file_menu[] = {
    ACTION_new,
    ACTION_open,
    ACTION_save,
    ACTION_saveas,
    ACTION_print,
    ACTION_designdetails,
    -1,
    ACTION_help,
    -1,
    ACTION_exit,
    -2
};

int edit_menu[] = {
    ACTION_undo,
    ACTION_redo,
    -1,
    ACTION_cut,
    ACTION_copy,
    ACTION_paste,
    -2
};

int view_menu[] = {
    ACTION_day,
    ACTION_night,
    -2
};

int pan_menu[] = {
    ACTION_panrealtime,
    ACTION_panpoint,
    -1,
    ACTION_panleft,
    ACTION_panright,
    ACTION_panup,
    ACTION_pandown,
    -2
};

int icon_menu[] = {
    ACTION_icon16,
    ACTION_icon24,
    ACTION_icon32,
    ACTION_icon48,
    ACTION_icon64,
    ACTION_icon128,
    -2
};

int help_menu[] = {
    ACTION_help,
    -1,
    ACTION_changelog,
    -1,
    ACTION_tipoftheday,
    -1,
    ACTION_about,
    -1,
    ACTION_whatsthis,
    -2
};

int zoom_menu[] = {
    ACTION_zoomwindow,
    ACTION_zoomdynamic,
    ACTION_zoomscale,
    -1,
    ACTION_zoomcenter,
    ACTION_zoomin,
    ACTION_zoomout,
    -1,
    ACTION_zoomselected,
    ACTION_zoomall,
    ACTION_zoomextents,
    -2
};

int settings_menu[] = {
    ACTION_settingsdialog,
    -1,
    -2
};

int recent_menu[] = {
    -1,
    -2
};

int window_menu[] = {
    -1,
    -2
};

int *menus[] = {
    file_menu,
    edit_menu,
    view_menu,
    settings_menu,
    window_menu,
    help_menu,
    recent_menu,
    zoom_menu,
    pan_menu
};

float symbol_scale = 0.01;

/* Symbols use the SVG path syntax.
 *
 * In theory, we could combine the icons and symbols systems,
 * since they could be rendered once and stored as icons in Qt.
 * (Or as textures in FreeGLUT.)
 *
 * Also we want to render the patterns themselves using SVG
 * syntax, so it would save on repeated work overall.
 */
const char *symbol_list[] = {
    /* 0 */ "icon 0",
    /* 1 */ "M 5 100 L 45 100 M 0 25 L 25 0 L 25 100",
    /* 2 */ "icon 2",
    /* 3 */ "icon 3",
    /* 4 */ "M 50 100 L 50 0 L 0 50 L 50 50",
    /* 5 */ "icon 5",
    /* 6 */ "icon 6",
    /* 7 */ "M 0 0 L 50 0 L 25 75 L 25 100",
    /* 8 */ "icon 8",
    /* 9 */ "icon 9",
    /* - */ "M 0 50 L 50 50",
    /* ' */ "M 25 100 L 25 25",
    /* " */ "M 10 0 L 10 25 M 40 0 L 40 25"
};

#if 0
path_symbol icon_zero[] = {
    /* path.addEllipse(QPointF(x+0.25*xScale, y-0.50*yScale), 0.25*xScale, 0.50*yScale);*/
    M 0 -0.75
    L 0 -0.25
    A 0 -0.5 0.5 0.5 180.0 180.0
    L 0.5, -0.75
    A 0 -1.0, 0.5, 0.5, 0.0, 180.0
};

path_symbol icon_two[] = {
    {PATHS_MOVETO, 0 -0.75
    A {0.45, 1.00, 0.50, 180.00, -216.87
    L 0 0.0
    L {0.50, 0.0
};

path_symbol icon_three[] = {
    {PATHS_ARCMOVETO, 0 -0.50, 0.50, 0.50, 195.00
    A 0 -0.50, 0.50, 195.00, 255.00
    A 0 -0.50, 0.50, 270.00, 255.00
};

path_symbol icon_five[] = {
    M 50 0 L 0 0 L 0 50 L 25 50 A 0.0, -0.5 0.5 0.5 90.0 -180.0 L 0 0
};

path_symbol icon_six[] = {
    path.addEllipse(QPointF(x+0.25*xScale, y-0.25*yScale), 0.25*xScale, 0.25*yScale);
    M 0 75 L 0 25
    path.arcTo(x+0.00*xScale, y-1.00*yScale, 0.50*xScale, 0.50*yScale, 180.00, -140.00);
};

path_symbol icon_eight[] = {
    path.addEllipse(QPointF(x+0.25*xScale, y-0.25*yScale), 0.25*xScale, 0.25*yScale);
    path.addEllipse(QPointF(x+0.25*xScale, y-0.75*yScale), 0.25*xScale, 0.25*yScale);
};

path_symbol icon_nine[] = {
    path.addEllipse(QPointF(x+0.25*xScale, y-0.75*yScale), 0.25*xScale, 0.25*yScale);
    M 0.50*xScale, y-0.75*yScale);
    L x+0.50*xScale, y-0.25*yScale);
    path.arcTo(x+0.00*xScale, y-0.50*yScale, 0.50*xScale, 0.50*yScale, 0.00, -140.00);
};

#endif


/* New for toolbars: modify and draw. Inquiry toolbar?
 *
 * TODO: associate the property editor with the function callbacks using
 * a function pointer.
 */

/* property_editor_row property_editors[] = { */
/*
QGroupBox* PropertyEditor::createGroupBoxGeometryCircle()
{
    groupBoxGeometryCircle = new QGroupBox(tr("Geometry"), this);

    toolButtonCircleCenterX = createToolButton("blank", tr("Center X"));
    toolButtonCircleCenterY = createToolButton("blank", tr("Center Y"));
    toolButtonCircleRadius = createToolButton("blank", tr("Radius"));
    toolButtonCircleDiameter = createToolButton("blank", tr("Diameter"));
    toolButtonCircleArea = createToolButton("blank", tr("Area"));
    toolButtonCircleCircumference = createToolButton("blank", tr("Circumference"));

    lineEditCircleCenterX = createLineEdit("double", 0);
    lineEditCircleCenterY = createLineEdit("double", 0);
    lineEditCircleRadius = createLineEdit("double", 0);
    lineEditCircleDiameter = createLineEdit("double", 0);
    lineEditCircleArea = createLineEdit("double", 0);
    lineEditCircleCircumference = createLineEdit("double", 0);

    mapSignal(lineEditCircleCenterX, "lineEditCircleCenterX", OBJ_TYPE_CIRCLE);
    mapSignal(lineEditCircleCenterY, "lineEditCircleCenterY", OBJ_TYPE_CIRCLE);
    mapSignal(lineEditCircleRadius, "lineEditCircleRadius", OBJ_TYPE_CIRCLE);
    mapSignal(lineEditCircleDiameter, "lineEditCircleDiameter", OBJ_TYPE_CIRCLE);
    mapSignal(lineEditCircleArea, "lineEditCircleArea", OBJ_TYPE_CIRCLE);
    mapSignal(lineEditCircleCircumference, "lineEditCircleCircumference", OBJ_TYPE_CIRCLE);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonCircleCenterX, lineEditCircleCenterX);
    formLayout->addRow(toolButtonCircleCenterY, lineEditCircleCenterY);
    formLayout->addRow(toolButtonCircleRadius, lineEditCircleRadius);
    formLayout->addRow(toolButtonCircleDiameter, lineEditCircleDiameter);
    formLayout->addRow(toolButtonCircleArea, lineEditCircleArea);
    formLayout->addRow(toolButtonCircleCircumference, lineEditCircleCircumference);
    groupBoxGeometryCircle->setLayout(formLayout);

    return groupBoxGeometryCircle;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryImage()
{
    groupBoxGeometryImage = new QGroupBox(tr("Geometry"), this);

    toolButtonImageX = createToolButton("blank", tr("Position X"));
    toolButtonImageY = createToolButton("blank", tr("Position Y"));
    toolButtonImageWidth = createToolButton("blank", tr("Width"));
    toolButtonImageHeight = createToolButton("blank", tr("Height"));

    lineEditImageX = createLineEdit("double", 0);
    lineEditImageY = createLineEdit("double", 0);
    lineEditImageWidth = createLineEdit("double", 0);
    lineEditImageHeight = createLineEdit("double", 0);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonImageX, lineEditImageX);
    formLayout->addRow(toolButtonImageY, lineEditImageY);
    formLayout->addRow(toolButtonImageWidth, lineEditImageWidth);
    formLayout->addRow(toolButtonImageHeight, lineEditImageHeight);
    groupBoxGeometryImage->setLayout(formLayout);

    return groupBoxGeometryImage;
}

QGroupBox* PropertyEditor::createGroupBoxMiscImage()
{
    groupBoxMiscImage = new QGroupBox(tr("Misc"), this);

    toolButtonImageName = createToolButton("blank", tr("Name"));
    toolButtonImagePath = createToolButton("blank", tr("Path"));

    lineEditImageName = createLineEdit("double", 1);
    lineEditImagePath = createLineEdit("double", 1);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonImageName, lineEditImageName);
    formLayout->addRow(toolButtonImagePath, lineEditImagePath);
    groupBoxMiscImage->setLayout(formLayout);

    return groupBoxMiscImage;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryInfiniteLine()
{
    groupBoxGeometryInfiniteLine = new QGroupBox(tr("Geometry"), this);

    toolButtonInfiniteLineX1 = createToolButton("blank", tr("Start X"));
    toolButtonInfiniteLineY1 = createToolButton("blank", tr("Start Y"));
    toolButtonInfiniteLineX2 = createToolButton("blank", tr("2nd X"));
    toolButtonInfiniteLineY2 = createToolButton("blank", tr("2nd Y"));
    toolButtonInfiniteLineVectorX = createToolButton("blank", tr("Vector X"));
    toolButtonInfiniteLineVectorY = createToolButton("blank", tr("Vector Y"));

    lineEditInfiniteLineX1 = createLineEdit("double", 0);
    lineEditInfiniteLineY1 = createLineEdit("double", 0);
    lineEditInfiniteLineX2 = createLineEdit("double", 0);
    lineEditInfiniteLineY2 = createLineEdit("double", 0);
    lineEditInfiniteLineVectorX = createLineEdit("double", 1);
    lineEditInfiniteLineVectorY = createLineEdit("double", 1);

    //TODO: mapSignal for infinite lines

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonInfiniteLineX1, lineEditInfiniteLineX1);
    formLayout->addRow(toolButtonInfiniteLineY1, lineEditInfiniteLineY1);
    formLayout->addRow(toolButtonInfiniteLineX2, lineEditInfiniteLineX2);
    formLayout->addRow(toolButtonInfiniteLineY2, lineEditInfiniteLineY2);
    formLayout->addRow(toolButtonInfiniteLineVectorX, lineEditInfiniteLineVectorX);
    formLayout->addRow(toolButtonInfiniteLineVectorY, lineEditInfiniteLineVectorY);
    groupBoxGeometryInfiniteLine->setLayout(formLayout);

    return groupBoxGeometryInfiniteLine;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryLine()
{
    groupBoxGeometryLine = new QGroupBox(tr("Geometry"), this);

    toolButtonLineStartX = createToolButton("blank", tr("Start X"));
    toolButtonLineStartY = createToolButton("blank", tr("Start Y"));
    toolButtonLineEndX = createToolButton("blank", tr("End X"));
    toolButtonLineEndY = createToolButton("blank", tr("End Y"));
    toolButtonLineDeltaX = createToolButton("blank", tr("Delta X"));
    toolButtonLineDeltaY = createToolButton("blank", tr("Delta Y"));
    toolButtonLineAngle = createToolButton("blank", tr("Angle"));
    toolButtonLineLength = createToolButton("blank", tr("Length"));

    lineEditLineStartX = createLineEdit("double", 0);
    lineEditLineStartY = createLineEdit("double", 0);
    lineEditLineEndX = createLineEdit("double", 0);
    lineEditLineEndY = createLineEdit("double", 0);
    lineEditLineDeltaX = createLineEdit("double", 1);
    lineEditLineDeltaY = createLineEdit("double", 1);
    lineEditLineAngle = createLineEdit("double", 1);
    lineEditLineLength = createLineEdit("double", 1);

    mapSignal(lineEditLineStartX, "lineEditLineStartX", OBJ_TYPE_LINE);
    mapSignal(lineEditLineStartY, "lineEditLineStartY", OBJ_TYPE_LINE);
    mapSignal(lineEditLineEndX, "lineEditLineEndX", OBJ_TYPE_LINE);
    mapSignal(lineEditLineEndY, "lineEditLineEndY", OBJ_TYPE_LINE);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonLineStartX, lineEditLineStartX);
    formLayout->addRow(toolButtonLineStartY, lineEditLineStartY);
    formLayout->addRow(toolButtonLineEndX, lineEditLineEndX);
    formLayout->addRow(toolButtonLineEndY, lineEditLineEndY);
    formLayout->addRow(toolButtonLineDeltaX, lineEditLineDeltaX);
    formLayout->addRow(toolButtonLineDeltaY, lineEditLineDeltaY);
    formLayout->addRow(toolButtonLineAngle, lineEditLineAngle);
    formLayout->addRow(toolButtonLineLength, lineEditLineLength);
    groupBoxGeometryLine->setLayout(formLayout);

    return groupBoxGeometryLine;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryPath()
{
    groupBoxGeometryPath = new QGroupBox(tr("Geometry"), this);

    toolButtonPathVertexNum = createToolButton("blank", tr("Vertex #"));
    toolButtonPathVertexX = createToolButton("blank", tr("Vertex X"));
    toolButtonPathVertexY = createToolButton("blank", tr("Vertex Y"));
    toolButtonPathArea = createToolButton("blank", tr("Area"));
    toolButtonPathLength = createToolButton("blank", tr("Length"));

    comboBoxPathVertexNum = createComboBox(0);
    lineEditPathVertexX = createLineEdit("double", 0);
    lineEditPathVertexY = createLineEdit("double", 0);
    lineEditPathArea = createLineEdit("double", 1);
    lineEditPathLength = createLineEdit("double", 1);

    //TODO: mapSignal for paths

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonPathVertexNum, comboBoxPathVertexNum);
    formLayout->addRow(toolButtonPathVertexX, lineEditPathVertexX);
    formLayout->addRow(toolButtonPathVertexY, lineEditPathVertexY);
    formLayout->addRow(toolButtonPathArea, lineEditPathArea);
    formLayout->addRow(toolButtonPathLength, lineEditPathLength);
    groupBoxGeometryPath->setLayout(formLayout);

    return groupBoxGeometryPath;
}

QGroupBox* PropertyEditor::createGroupBoxMiscPath()
{
    groupBoxMiscPath = new QGroupBox(tr("Misc"), this);

    toolButtonPathClosed = createToolButton("blank", tr("Closed"));

    comboBoxPathClosed = createComboBox(0);

    //TODO: mapSignal for paths

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonPathClosed, comboBoxPathClosed);
    groupBoxMiscPath->setLayout(formLayout);

    return groupBoxMiscPath;
}


QGroupBox* PropertyEditor::createGroupBoxGeometryPolygon()
{
    groupBoxGeometryPolygon = new QGroupBox(tr("Geometry"), this);

    {
        OBJ_TYPE_POLYGON, POLYGON_CENTER_X,
        0, "blank", "Center X", LINE_EDIT_MODE, "lineEditPolygonCenterX"
    },
    {
        OBJ_TYPE_POLYGON, POLYGON_CENTER_Y,
        0, "blank", "Center Y", LINE_EDIT_MODE, "lineEditPolygonCenterY"
    },
    {
        OBJ_TYPE_POLYGON, POLYGON_VERTEX_RADIUS,
        0, "blank", "Vertex Radius", LINE_EDIT_MODE, "lineEditPolygonVertexRadius"
    }

    toolButtonPolygonRadiusSide = createToolButton("blank", tr("Side Radius"));
    toolButtonPolygonDiameterVertex = createToolButton("blank", tr("Vertex Diameter"));
    toolButtonPolygonDiameterSide = createToolButton("blank", tr("Side Diameter"));
    toolButtonPolygonInteriorAngle = createToolButton("blank", tr("Interior Angle"));

    lineEditPolygonRadiusSide = createLineEdit("double", 0);
    lineEditPolygonDiameterVertex = createLineEdit("double", 0);
    lineEditPolygonDiameterSide = createLineEdit("double", 0);
    lineEditPolygonInteriorAngle = createLineEdit("double", 1);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonPolygonRadiusSide, lineEditPolygonRadiusSide);
    formLayout->addRow(toolButtonPolygonDiameterVertex, lineEditPolygonDiameterVertex);
    formLayout->addRow(toolButtonPolygonDiameterSide, lineEditPolygonDiameterSide);
    formLayout->addRow(toolButtonPolygonInteriorAngle, lineEditPolygonInteriorAngle);
    groupBoxGeometryPolygon->setLayout(formLayout);

    return groupBoxGeometryPolygon;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryPolyline()
{
    groupBoxGeometryPolyline = new QGroupBox(tr("Geometry"), this);

    toolButtonPolylineVertexNum = createToolButton("blank", tr("Vertex #"));
    toolButtonPolylineVertexX = createToolButton("blank", tr("Vertex X"));
    toolButtonPolylineVertexY = createToolButton("blank", tr("Vertex Y"));
    toolButtonPolylineArea = createToolButton("blank", tr("Area"));
    toolButtonPolylineLength = createToolButton("blank", tr("Length"));

    comboBoxPolylineVertexNum = createComboBox(0);
    lineEditPolylineVertexX = createLineEdit("double", 0);
    lineEditPolylineVertexY = createLineEdit("double", 0);
    lineEditPolylineArea = createLineEdit("double", 1);
    lineEditPolylineLength = createLineEdit("double", 1);

    //TODO: mapSignal for polylines

    QFormLayout* formLayout = new QFormLayout(this);
    "comboBoxPolylineVertexNum"
    "lineEditPolylineVertexX"
    "lineEditPolylineVertexY"
    "lineEditPolylineArea"
    "lineEditPolylineLength"
    groupBoxGeometryPolyline->setLayout(formLayout);

    return groupBoxGeometryPolyline;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryRay()
{
    toolButtonRayX2 = createToolButton();
    toolButtonRayY2 = createToolButton("blank", tr("2nd Y"));
    toolButtonRayVectorX = createToolButton("blank", tr("Vector X"));
    toolButtonRayVectorY = createToolButton("blank", tr("Vector Y"));

    "blank", "Start X", 0, "lineEditRayX1"
    "blank", "Start Y", 0, "lineEditRayY1"
    "blank", "2nd X", 0, "lineEditRayX2"
    "blank", "2nd Y", 0, "lineEditRayY2"
    "blank", "Vector X", 1, "lineEditRayVectorX"
    1, "lineEditRayVectorY"
}

QGroupBox* PropertyEditor::createGroupBoxGeometryTextMulti()
{
    groupBoxGeometryTextMulti = new QGroupBox(tr("Geometry"), this);

    toolButtonTextMultiX = createToolButton("blank", tr("Position X"));
    toolButtonTextMultiY = createToolButton("blank", tr("Position Y"));

    lineEditTextMultiX = createLineEdit("double", 0);
    lineEditTextMultiY = createLineEdit("double", 0);


    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonTextMultiX, lineEditTextMultiX);
    formLayout->addRow(toolButtonTextMultiY, lineEditTextMultiY);
    groupBoxGeometryTextMulti->setLayout(formLayout);

    return groupBoxGeometryTextMulti;
}

QGroupBox* PropertyEditor::createGroupBoxTextTextSingle()
{
    groupBoxTextTextSingle = new QGroupBox(tr("Text"), this);

    {
        "blank",
        "Contents",
        "toolButtonTextSingleContents"
    },
    toolButtonTextSingleFont = createToolButton("blank", tr("Font"));
    toolButtonTextSingleJustify = createToolButton("blank", tr("Justify"));
    toolButtonTextSingleHeight = createToolButton("blank", tr("Height"));
    toolButtonTextSingleRotation = createToolButton("blank", tr("Rotation"));

    lineEditTextSingleContents = createLineEdit("string", 0);
    comboBoxTextSingleFont = createFontComboBox(0);
    comboBoxTextSingleJustify = createComboBox(0);
    lineEditTextSingleHeight = createLineEdit("double", 0);
    lineEditTextSingleRotation = createLineEdit("double", 0);

    mapSignal(lineEditTextSingleContents, "lineEditTextSingleContents", OBJ_TYPE_TEXTSINGLE);
    mapSignal(comboBoxTextSingleFont, "comboBoxTextSingleFont", OBJ_TYPE_TEXTSINGLE);
    mapSignal(comboBoxTextSingleJustify, "comboBoxTextSingleJustify", OBJ_TYPE_TEXTSINGLE);
    mapSignal(lineEditTextSingleHeight, "lineEditTextSingleHeight", OBJ_TYPE_TEXTSINGLE);
    mapSignal(lineEditTextSingleRotation, "lineEditTextSingleRotation", OBJ_TYPE_TEXTSINGLE);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonTextSingleContents, lineEditTextSingleContents);
    formLayout->addRow(toolButtonTextSingleFont, comboBoxTextSingleFont);
    formLayout->addRow(toolButtonTextSingleJustify, comboBoxTextSingleJustify);
    formLayout->addRow(toolButtonTextSingleHeight, lineEditTextSingleHeight);
    formLayout->addRow(toolButtonTextSingleRotation, lineEditTextSingleRotation);
    groupBoxTextTextSingle->setLayout(formLayout);

    return groupBoxTextTextSingle;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryTextSingle()
{
    groupBoxGeometryTextSingle = new QGroupBox(tr("Geometry"), this);

    toolButtonTextSingleX = createToolButton("blank", tr("Position X"));
    toolButtonTextSingleY = createToolButton("blank", tr("Position Y"));

    lineEditTextSingleX = createLineEdit("double", 0);
    lineEditTextSingleY = createLineEdit("double", 0);

    mapSignal(lineEditTextSingleX, "lineEditTextSingleX", OBJ_TYPE_TEXTSINGLE);
    mapSignal(lineEditTextSingleY, "lineEditTextSingleY", OBJ_TYPE_TEXTSINGLE);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonTextSingleX, lineEditTextSingleX);
    formLayout->addRow(toolButtonTextSingleY, lineEditTextSingleY);
    groupBoxGeometryTextSingle->setLayout(formLayout);

    return groupBoxGeometryTextSingle;
}

QGroupBox* PropertyEditor::createGroupBoxMiscTextSingle()
{
    groupBoxMiscTextSingle = new QGroupBox(tr("Misc"), this);

    toolButtonTextSingleBackward = createToolButton("blank", tr("Backward"));
    toolButtonTextSingleUpsideDown = createToolButton("blank", tr("UpsideDown"));

    comboBoxTextSingleBackward = createComboBox(0);
    comboBoxTextSingleUpsideDown = createComboBox(0);

    mapSignal(comboBoxTextSingleBackward, "comboBoxTextSingleBackward", OBJ_TYPE_TEXTSINGLE);
    mapSignal(comboBoxTextSingleUpsideDown, "comboBoxTextSingleUpsideDown", OBJ_TYPE_TEXTSINGLE);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonTextSingleBackward, comboBoxTextSingleBackward);
    formLayout->addRow(toolButtonTextSingleUpsideDown, comboBoxTextSingleUpsideDown);
    groupBoxMiscTextSingle->setLayout(formLayout);

    return groupBoxMiscTextSingle;
}

*/
#if 0
    {
        /* 0 */
        OBJ_TYPE_ARC, ARC_CENTER_X,
        0, "blank", "Center X", LINE_EDIT_DOUBLE, "lineEditArcCenterX"
    },
    {
        /* 1 */
        OBJ_TYPE_ARC, ARC_CENTER_Y,
        0, "blank", "Center Y", LINE_EDIT_DOUBLE, "lineEditArcCenterY"
    },
    {
        /* 2 */
        OBJ_TYPE_ARC, ARC_RADIUS,
        0, "blank", "Radius", LINE_EDIT_DOUBLE, "lineEditArcRadius"
    },
    {
        /* 3 */
        OBJ_TYPE_ARC, ARC_START_ANGLE,
        0, "blank", "Start Angle", LINE_EDIT_DOUBLE, "lineEditArcStartAngle"
    },
    {
        /* 4 */
        OBJ_TYPE_ARC, ARC_END_ANGLE,
        0, "blank", "End Angle", LINE_EDIT_DOUBLE, "lineEditArcEndAngle"
    },
    {
        /* 5 */
        OBJ_TYPE_ARC, ARC_START_X,
        1, "blank", "Start X", LINE_EDIT_DOUBLE, "lineEditArcStartX"
    },
    {
        /* 6 */
        OBJ_TYPE_ARC, ARC_START_Y,
        1, "blank", "Start Y", LINE_EDIT_DOUBLE, "lineEditArcStartY"
    },
    {
        /* 7 */
        OBJ_TYPE_ARC, ARC_END_X,
        1, "blank", "End X", LINE_EDIT_DOUBLE, "lineEditArcEndX"
    },
    {
        /* 8 */
        OBJ_TYPE_ARC, ARC_END_Y,
        1, "blank", "End Y", LINE_EDIT_DOUBLE, "lineEditArcEndY"
    },
    {
        /* 9 */
        OBJ_TYPE_ARC, ARC_AREA,
        1, "blank", "Area", LINE_EDIT_DOUBLE, "lineEditArcArea"
    },
/*        ARC_LENGTH, 1, "blank", "ArcLength");
    create_lineedit_row(formLayout, ARC_CHORD, 1, "blank", "ArcChord");
    create_lineedit_row(formLayout, ARC_INC_ANGLE, 1, "blank", "ArcIncludedAngle");
    ARC_CLOCKWISE, "int", 1, "blank", "Clockwise", */
    {
        /* 9 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_CENTER_X,
        0, "blank", "Center X", LINE_EDIT_DOUBLE, "lineEditEllipseCenterX"
    },
    {
        /* 10 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_CENTER_Y,
        0, "blank", "Center Y", LINE_EDIT_DOUBLE, "lineEditEllipseCenterY"
    },
    {
        /* 11 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_RADIUS_MAJOR,
        0, "blank", "Radius Major", LINE_EDIT_DOUBLE, "lineEditEllipseRadiusMajor"
    },
    {
        /* 12 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_RADIUS_MINOR,
        0, "blank", "Radius Minor", LINE_EDIT_DOUBLE, "lineEditEllipseRadiusMinor"
    },
    {
        /* 13 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_DIAMETER_MAJOR,
        0, "blank", "Diameter Major", LINE_EDIT_DOUBLE, "lineEditEllipseDiameterMajor"
    },
    {
        /* 14 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_DIAMETER_MINOR,
        0, "blank", "Diameter Minor", LINE_EDIT_DOUBLE, "lineEditEllipseDiameterMinor"
    },
    {
        /* 15 */
        OBJ_TYPE_BLOCK, BLOCK_X,
        0, "blank", "Position X", LINE_EDIT_DOUBLE, "lineEditBlockX"
    },
    {
        /* 16 */
        OBJ_TYPE_BLOCK, BLOCK_Y,
        0, "blank", "Position Y", LINE_EDIT_DOUBLE, "lineEditBlockY"
    },
    {
        /* 17 */
        OBJ_TYPE_POINT, POINT_X,
        0, "blank", "Position X", LINE_EDIT_DOUBLE, "lineEditPointX"
    },
    {
        /* 18 */
        OBJ_TYPE_POINT, POINT_Y,
        0, "blank", "Position Y", LINE_EDIT_DOUBLE, "lineEditPointY"
    },
    {
        /* 19 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_X1,
        0, "blank", "Corner 1 X", LINE_EDIT_DOUBLE, "lineEditRectangleCorner1X"
    },
    {
        /* 20 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_Y1,
        0, "blank", "Corner 1 Y", LINE_EDIT_DOUBLE, "lineEditRectangleCorner1Y"
    },
    {
        /* 21 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_X2,
        0, "blank", "Corner 2 X", LINE_EDIT_DOUBLE, "lineEditRectangleCorner2X"
    },
    {
        /* 22 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_Y2,
        0, "blank", "Corner 2 Y", LINE_EDIT_DOUBLE, "lineEditRectangleCorner2Y"
    },
    {
        /* 23 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_X3,
        0, "blank", "Corner 3 X", LINE_EDIT_DOUBLE, "lineEditRectangleCorner3X"
    },
    {
        /* 24 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_Y3,
        0, "blank", "Corner 3 Y", LINE_EDIT_DOUBLE, "lineEditRectangleCorner3Y"
    },
    {
        /* 25 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_X4,
        0, "blank", "Corner 4 X", LINE_EDIT_DOUBLE, "lineEditRectangleCorner4X"
    },
    {
        /* 26 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_Y4,
        0, "blank", "Corner 4 Y", LINE_EDIT_DOUBLE, "lineEditRectangleCorner4Y"
    },
    {
        /* 27 */
        OBJ_TYPE_RECTANGLE, RECT_WIDTH,
        0, "blank", "Width", LINE_EDIT_DOUBLE, "lineEditRectangleWidth"
    },
    {
        /* 28 */
        OBJ_TYPE_RECTANGLE, RECT_HEIGHT,
        0, "blank", "Height", LINE_EDIT_DOUBLE, "lineEditRectangleHeight"
    },
    {
        /* 29 */
        OBJ_TYPE_RECTANGLE, RECT_AREA,
        1, "blank", "Area", LINE_EDIT_DOUBLE, "lineEditRectangleArea"
    },
    {
        /* END */
        OBJ_TYPE_UNKNOWN, 0,
        "NULL", 0, "NULL", "NULL", 0, "NULL"
    }
};
#endif

action action_list[] = {
    {
        /* 0 */
        OBJ_TYPE_NULL,
        donothing_xpm,
        "donothing",
        "&Do Nothing",
        "Does nothing.",
        "\\0",
        doNothing
    },
    {
        /* 1 */
        OBJ_TYPE_NULL,
        new_xpm,
        "new",
        "&New",
        "Create a new file.",
        "Ctrl+N",
        newFile
    },
    {
        /* 2 */
        OBJ_TYPE_NULL,
        open_xpm,
        "open",
        "&Open",
        "Open an existing file.",
        "Ctrl+O",
        openFile
    },
    {
        /* 3 */
        OBJ_TYPE_NULL,
        save_xpm,
        "save",
        "&Save",
        "Save the design to disk.",
        "Ctrl+S",
        saveFile
    },
    {
        /* 4 */
        OBJ_TYPE_NULL,
        saveas_xpm,
        "saveas",
        "Save &As",
        "Save the design under a new name.",
        "Ctrl+Shift+S",
        saveAsFile
    },
    {
        /* 5 */
        OBJ_TYPE_NULL,
        print_xpm,
        "print",
        "&Print",
        "Print the design.",
        "Ctrl+P",
        main_print
    },
    {
        /* 6 */
        OBJ_TYPE_NULL,
        designdetails_xpm,
        "designdetails",
        "&Details",
        "Details of the current design.",
        "Ctrl+D",
        designDetails
    },
    {
        /* 7 */
        OBJ_TYPE_NULL,
        exit_xpm,
        "exit",
        "E&xit",
        "Exit the application.",
        "Ctrl+Q",
        main_exit
    },
    {
        /* 8 */
        OBJ_TYPE_NULL,
        cut_xpm,
        "cut",
        "Cu&t",
        "Cut the current selection's contents to the clipboard.",
        "Ctrl+X",
        main_cut
    },
    {
        /* 9 */
        OBJ_TYPE_NULL,
        copy_xpm,
        "copy",
        "&Copy",
        "Copy the current selection's contents to the clipboard.",
        "Ctrl+C",
        main_copy
    },
    {
        /* 10 */
        OBJ_TYPE_NULL,
        paste_xpm,
        "paste",
        "&Paste",
        "Paste the clipboard's contents into the current selection.",
        "Ctrl+V",
        main_paste
    },
    {
        /* 11 */
        OBJ_TYPE_NULL,
        undo_xpm,
        "undo",
        "&Undo",
        "Reverses the most recent action.",
        "Ctrl+Z",
        main_undo
    },
    {
        /* 12 */
        OBJ_TYPE_NULL,
        redo_xpm,
        "redo",
        "&Redo",
        "Reverses the effects of the previous undo action.",
        "Ctrl+Shift+Z",
        main_redo
    },
    {
        /* 13 */
        OBJ_TYPE_NULL,
        windowclose_xpm,
        "windowclose",
        "Cl&ose",
        "Close the active window.",
        "\\0",
        windowClose
    },
    {
        /* 14 */
        OBJ_TYPE_NULL,
        windowcloseall_xpm,
        "windowcloseall",
        "Close &All",
        "Close all the windows.",
        "\\0",
        windowCloseAll
    },
    {
        /* 15 */
        OBJ_TYPE_NULL,
        windowcascade_xpm,
        "windowcascade",
        "&Cascade",
        "Cascade the windows.",
        "\\0",
        windowCascade
    },
    {
        /* 16 */
        OBJ_TYPE_NULL,
        windowtile_xpm,
        "windowtile",
        "&Tile",
        "Tile the windows.",
        "\\0",
        windowTile
    },
    {
        OBJ_TYPE_NULL,
        windownext_xpm,
        "windownext",
        "Ne&xt",
        "Move the focus to the next window.",
        "\\0",
        windowNext
    },
    {
        OBJ_TYPE_NULL,
        windowprevious_xpm,
        "windowprevious",
        "Pre&vious",
        "Move the focus to the previous window.",
        "\\0",
        windowPrevious
    },
    {
        OBJ_TYPE_NULL,
        help_xpm,
        "help",
        "&Help",
        "Displays help.",
        "F1",
        main_help
    },
    {
        OBJ_TYPE_NULL,
        changelog_xpm,
        "changelog",
        "&Changelog",
        "Describes new features in this product.",
        "\\0",
        changelog
    },
    {
        OBJ_TYPE_NULL,
        tipoftheday_xpm,
        "tipoftheday",
        "&Tip Of The Day",
        "Displays a dialog with useful tips",
        "\\0",
        tipOfTheDay
    },
    {
        OBJ_TYPE_NULL,
        about_xpm,
        "about",
        "&About Embroidermodder 2",
        "Displays information about this product.",
        "F2",
        main_about
    },
    {
        OBJ_TYPE_NULL,
        whatsthis_xpm,
        "whatsthis",
        "&What's This?",
        "What's This? Context Help!",
        "\\0",
        whatsthisContextHelp
    },
    {
        OBJ_TYPE_NULL,
        icon16_xpm,
        "icon16",
        "Icon&16",
        "Sets the toolbar icon size to 16x16.",
        "\\0",
        icon16
    },
    {
        OBJ_TYPE_NULL,
        icon24_xpm,
        "icon24",
        "Icon&24",
        "Sets the toolbar icon size to 24x24.",
        "\\0",
        icon24
    },
    {
        OBJ_TYPE_NULL,
        icon32_xpm,
        "icon32",
        "Icon&32",
        "Sets the toolbar icon size to 32x32.",
        "\\0",
        icon32
    },
    {
        OBJ_TYPE_NULL,
        icon48_xpm,
        "icon48",
        "Icon&48",
        "Sets the toolbar icon size to 48x48.",
        "\\0",
        icon48
    },
    {
        OBJ_TYPE_NULL,
        icon64_xpm,
        "icon64",
        "Icon&64",
        "Sets the toolbar icon size to 64x64.",
        "\\0",
        icon64
    },
    {
        OBJ_TYPE_NULL,
        icon128_xpm,
        "icon128",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128.",
        "\\0",
        icon128
    },
    {
        OBJ_TYPE_NULL,
        settingsdialog_xpm,
        "settingsdialog",
        "&Settings",
        "Configure settings specific to this product.",
        "\\0",
        settingsDialog
    },
    {
        OBJ_TYPE_NULL,
        makelayercurrent_xpm,
        "makelayercurrent",
        "&Make Layer Active",
        "Makes the layer of a selected object the active layer",
        "\\0",
        makeLayerCurrent
    },
    {
        OBJ_TYPE_NULL,
        layers_xpm,
        "layers",
        "&Layers",
        "Manages layers and layer properties:  LAYER",
        "\\0",
        layerManager
    },
    {
        OBJ_TYPE_NULL,
        layerselector_xpm,
        "layerselector",
        "&Layer Selector",
        "Dropdown selector for changing the current layer",
        "\\0",
        layerSelector
    },
    {
        OBJ_TYPE_NULL,
        layerprevious_xpm,
        "layerprevious",
        "&Layer Previous",
        "Restores the previous layer settings:  LAYERP",
        "\\0",
        layerPrevious
    },
    {
        OBJ_TYPE_NULL,
        colorselector_xpm,
        "colorselector",
        "&Color Selector",
        "Dropdown selector for changing the current thread color",
        "\\0",
        colorSelector
    },
    {
        OBJ_TYPE_NULL,
        linetypeselector_xpm,
        "linetypeselector",
        "&Stitchtype Selector",
        "Dropdown selector for changing the current stitch type",
        "\\0",
        lineTypeSelector
    },
    {
        OBJ_TYPE_NULL,
        lineweightselector_xpm,
        "lineweightselector",
        "&Threadweight Selector",
        "Dropdown selector for changing the current thread weight",
        "\\0",
        lineWeightSelector
    },
    {
        OBJ_TYPE_NULL,
        hidealllayers_xpm,
        "hidealllayers",
        "&Hide All Layers",
        "Turns the visibility off for all layers in the current drawing:  HIDEALL",
        "\\0",
        hideAllLayers
    },
    {
        OBJ_TYPE_NULL,
        showalllayers_xpm,
        "showalllayers",
        "&Show All Layers",
        "Turns the visibility on for all layers in the current drawing:  SHOWALL",
        "\\0",
        showAllLayers
    },
    {
        OBJ_TYPE_NULL,
        freezealllayers_xpm,
        "freezealllayers",
        "&Freeze All Layers",
        "Freezes all layers in the current drawing:  FREEZEALL",
        "\\0",
        freezeAllLayers
    },
    {
        OBJ_TYPE_NULL,
        thawalllayers_xpm,
        "thawalllayers",
        "&Thaw All Layers",
        "Thaws all layers in the current drawing:  THAWALL",
        "\\0",
        thawAllLayers
    },
    {
        OBJ_TYPE_NULL,
        lockalllayers_xpm,
        "lockalllayers",
        "&Lock All Layers",
        "Locks all layers in the current drawing:  LOCKALL",
        "\\0",
        lockAllLayers
    },
    {
        OBJ_TYPE_NULL,
        unlockalllayers_xpm,
        "unlockalllayers",
        "&Unlock All Layers",
        "Unlocks all layers in the current drawing:  UNLOCKALL",
        "\\0",
        unlockAllLayers
    },
    {
        OBJ_TYPE_NULL,
        textbold_xpm,
        "textbold",
        "&Bold Text",
        "Sets text to be bold.",
        "\\0",
        textBold
    },
    {
        OBJ_TYPE_NULL,
        textitalic_xpm,
        "textitalic",
        "&Italic Text",
        "Sets text to be italic.",
        "\\0",
        textItalic
    },
    {
        OBJ_TYPE_NULL,
        textoverline_xpm,
        "textunderline",
        "&Underline Text",
        "Sets text to be underlined.",
        "\\0",
        textOverline
    },
    {
        OBJ_TYPE_NULL,
        textstrikeout_xpm,
        "textstrikeout",
        "&StrikeOut Text",
        "Sets text to be striked out.",
        "\\0",
        textStrikeout
    },
    {
        OBJ_TYPE_NULL,
        textoverline_xpm,
        "textoverline",
        "&Overline Text",
        "Sets text to be overlined.",
        "\\0",
        textOverline
    },
    {
        OBJ_TYPE_NULL,
        zoomrealtime_xpm,
        "zoomrealtime",
        "Zoom &Realtime",
        "Zooms to increase or decrease the apparent size of objects in the current viewport.",
        "\\0",
        zoomRealtime
    },
    {
        OBJ_TYPE_NULL,
        zoomprevious_xpm,
        "zoomprevious",
        "Zoom &Previous",
        "Zooms to display the previous view.",
        "\\0",
        zoomPrevious
    },
    {
        OBJ_TYPE_NULL,
        zoomwindow_xpm,
        "zoomwindow",
        "Zoom &Window",
        "Zooms to display an area specified by a rectangular window.",
        "\\0",
        zoomWindow
    },
    {
        OBJ_TYPE_NULL,
        zoomdynamic_xpm,
        "zoomdynamic",
        "Zoom &Dynamic",
        "Zooms to display the generated portion of the drawing.",
        "\\0",
        zoomDynamic
    },
    {
        OBJ_TYPE_NULL,
        zoomscale_xpm,
        "zoomscale",
        "Zoom &Scale",
        "Zooms the display using a specified scale factor.",
        "\\0",
        zoomScale
    },
    {
        OBJ_TYPE_NULL,
        zoomcenter_xpm,
        "zoomcenter",
        "Zoom &Center",
        "Zooms to display a view specified by a center point and magnification or height.",
        "\\0",
        zoomCenter
    },
    {
        OBJ_TYPE_NULL,
        zoomin_xpm,
        "zoomin",
        "Zoom &In",
        "Zooms to increase the apparent size of objects.",
        "\\0",
        zoomIn
    },
    {
        OBJ_TYPE_NULL,
        zoomout_xpm,
        "zoomout",
        "Zoom &Out",
        "Zooms to decrease the apparent size of objects.",
        "\\0",
        zoomOut
    },
    {
        OBJ_TYPE_NULL,
        zoomselected_xpm,
        "zoomselected",
        "Zoom Selec&ted",
        "Zooms to display the selected objects.",
        "\\0",
        zoomSelected
    },
    {
        OBJ_TYPE_NULL,
        zoomall_xpm,
        "zoomall",
        "Zoom &All",
        "Zooms to display the drawing extents or the grid limits.",
        "\\0",
        zoomAll
    },
    {
        OBJ_TYPE_NULL,
        zoomextents_xpm,
        "zoomextents",
        "Zoom &Extents",
        "Zooms to display the drawing extents.",
        "\\0",
        zoomExtents
    },
    {
        OBJ_TYPE_NULL,
        panrealtime_xpm,
        "panrealtime",
        "&Pan Realtime",
        "Moves the view in the current viewport.",
        "\\0",
        panrealtime
    },
    {
        OBJ_TYPE_NULL,
        panpoint_xpm,
        "panpoint",
        "&Pan Point",
        "Moves the view by the specified distance.",
        "\\0",
        panpoint
    },
    {
        OBJ_TYPE_NULL,
        panleft_xpm,
        "panleft",
        "&Pan Left",
        "Moves the view to the left.",
        "\\0",
        panLeft
    },
    {
        OBJ_TYPE_NULL,
        panright_xpm,
        "panright",
        "&Pan Right",
        "Moves the view to the right.",
        "\\0",
        panRight
    },
    {
        OBJ_TYPE_NULL,
        panup_xpm,
        "panup",
        "&Pan Up",
        "Moves the view up.",
        "\\0",
        panUp
    },
    {
        OBJ_TYPE_NULL,
        pandown_xpm,
        "pandown",
        "&Pan Down",
        "Moves the view down.",
        "\\0",
        panDown
    },
    {
        OBJ_TYPE_NULL,
        day_xpm,
        "day",
        "&Day",
        "Updates the current view using day vision settings.",
        "\\0",
        dayVision
    },
    {
        OBJ_TYPE_NULL,
        night_xpm,
        "night",
        "&Night",
        "Updates the current view using night vision settings.",
        "\\0",
        nightVision
    },
    {
        OBJ_TYPE_NULL,
        circle_xpm,
        "circle",
        "&Circle",
        "Creates a circle:  CIRCLE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        line_xpm,
        "line",
        "&Line",
        "Creates straight line segments:  LINE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        distance_xpm,
        "distance",
        "&Distance",
        "Measures the distance and angle between two points:  DIST",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        dolphin_xpm,
        "dolphin",
        "&Dolphin",
        "Creates a dolphin:  DOLPHIN",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        ellipse_xpm,
        "ellipse",
        "&Ellipse",
        "Creates a ellipse:  ELLIPSE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        erase_xpm,
        "delete",
        "D&elete",
        "Removes objects from a drawing:  DELETE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        heart_xpm,
        "heart",
        "&Heart",
        "Creates a heart:  HEART",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        locatepoint_xpm,
        "locatepoint",
        "&Locate Point",
        "Displays the coordinate values of a location:  ID",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        donothing_xpm,
        "trebleclef",
        "TrebleClef",
        "Creates a treble clef:  TREBLECLEF",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        path_xpm,
        "path",
        "&Path",
        "Creates a 2D path:  PATH",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        donothing_xpm,
        "platform",
        "&Platform",
        "List which platform is in use:  PLATFORM",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        point_xpm,
        "point",
        "&Point",
        "Creates multiple points:  POINT",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        polygon_xpm,
        "polygon",
        "Pol&ygon",
        "Creates a regular polygon:  POLYGON",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        polyline_xpm,
        "polyline",
        "&Polyline",
        "Creates a 2D polyline:  PLINE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        quickleader_xpm,
        "quickleader",
        "&QuickLeader",
        "Creates a leader and annotation:  QUICKLEADER",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        rectangle_xpm,
        "rectangle",
        "&Rectangle",
        "Creates a rectangular polyline: RECTANGLE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        rgb_xpm,
        "rgb",
        "&RGB",
        "Updates the current view colors:  RGB",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        move_xpm,
        "move",
        "&Move",
        "Displaces objects a specified distance in a specified direction: MOVE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        rotate_xpm,
        "rotate",
        "&Rotate",
        "Rotates objects about a base point:  ROTATE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        sandbox_xpm,
        "sandbox",
        "Sandbox",
        "A sandbox to play in:  SANDBOX",
        "\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        scale_xpm,
        "scale",
        "Sca&le",
        "Enlarges or reduces objects proportionally in the X, Y, and Z directions:  SCALE",
        "\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        donothing_xpm,
        "selectall",
        "&Select All",
        "Selects all objects:  SELECTALL",
        "\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        singlelinetext_xpm,
        "singlelinetext",
        "&Single Line Text",
        "Creates single-line text objects:  TEXT",
        "\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        snowflake_xpm,
        "snowflake",
        "&Snowflake",
        "Creates a snowflake:  SNOWFLAKE",
        "\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        star_xpm,
        "star",
        "&Star",
        "Creates a star:  STAR",
        "\0",
        doNothing
    },
    {
        /* end symbol */
        OBJ_TYPE_NULL,
        donothing_xpm,
        "\0",
        "\0",
        "\0",
        "\0",
        doNothing
    }
};

