/* This file is part of Embroidermodder 2.
 * ------------------------------------------------------------
 * Copyright 2013-2022 The Embroidermodder Team
 * Embroidermodder 2 is Open Source Software.
 * See LICENCE for licensing terms.
 * ------------------------------------------------------------
 * This file is the heart of the program and calls all the others.
 * New developers should start reading here.
 */

#include <math.h>
#include <string.h>

#if defined(__unix__) || defined(__linux__)
#include <sys/utsname.h>
#include <string.h>
#endif

#include "embroidermodder.h"

QToolBar* toolbar[10];
QMenu* menu[10];
StatusBarButton* status_bar[8];
QToolButton* toolButton[PROPERTY_EDITORS];
QLineEdit* lineEdit[LINEEDIT_PROPERTY_EDITORS];
QComboBox* comboBox[COMBOBOX_PROPERTY_EDITORS];

QStringList opensave_recent_list_of_files;
QString opensave_custom_filter;

QToolButton* toolButtonTextSingleContents;
QToolButton* toolButtonTextSingleFont;
QToolButton* toolButtonTextSingleJustify;
QToolButton* toolButtonTextSingleHeight;
QToolButton* toolButtonTextSingleRotation;

QLineEdit* lineEditTextSingleContents;
QFontComboBox* comboBoxTextSingleFont;
QComboBox* comboBoxTextSingleJustify;
QLineEdit* lineEditTextSingleHeight;
QLineEdit* lineEditTextSingleRotation;

QToolButton* toolButtonGeneralLayer;
QToolButton* toolButtonGeneralColor;
QToolButton* toolButtonGeneralLineType;
QToolButton* toolButtonGeneralLineWeight;

QComboBox* comboBoxGeneralLayer;
QComboBox* comboBoxGeneralColor;
QComboBox* comboBoxGeneralLineType;
QComboBox* comboBoxGeneralLineWeight;

QToolButton* toolButtonImageX;
QToolButton* toolButtonImageY;
QToolButton* toolButtonImageWidth;
QToolButton* toolButtonImageHeight;

QLineEdit*   lineEditImageX;
QLineEdit*   lineEditImageY;
QLineEdit*   lineEditImageWidth;
QLineEdit*   lineEditImageHeight;

QGroupBox*   groupBoxMiscImage;

QToolButton* toolButtonImageName;
QToolButton* toolButtonImagePath;

QLineEdit*   lineEditImageName;
QLineEdit*   lineEditImagePath;

QToolButton* toolButtonPolygonCenterX;
QToolButton* toolButtonPolygonCenterY;
QToolButton* toolButtonPolygonRadiusVertex;
QToolButton* toolButtonPolygonRadiusSide;
QToolButton* toolButtonPolygonDiameterVertex;
QToolButton* toolButtonPolygonDiameterSide;
QToolButton* toolButtonPolygonInteriorAngle;

QLineEdit* lineEditPolygonCenterX;
QLineEdit*   lineEditPolygonCenterY;
QLineEdit*   lineEditPolygonRadiusVertex;
QLineEdit*   lineEditPolygonRadiusSide;
QLineEdit*   lineEditPolygonDiameterVertex;
QLineEdit*   lineEditPolygonDiameterSide;
QLineEdit*   lineEditPolygonInteriorAngle;

EmbVector pasteDelta;
QPointF scenePressPoint;
QPoint pressPoint;
QPointF sceneMovePoint;
QPoint movePoint;
QPointF sceneReleasePoint;
QPoint releasePoint;
QPointF sceneGripPoint;

QColor rulerColor;

QPoint  viewMousePoint;
EmbVector sceneMousePoint;
unsigned int qsnapLocatorColor;
unsigned int gripColorCool;
unsigned int gripColorHot;
unsigned int crosshairColor;
int precisionAngle;
int precisionLength;

QLabel* statusBarMouseCoord;

QToolButton* toolButtonInfiniteLineX1;
QToolButton* toolButtonInfiniteLineY1;
QToolButton* toolButtonInfiniteLineX2;
QToolButton* toolButtonInfiniteLineY2;
QToolButton* toolButtonInfiniteLineVectorX;
QToolButton* toolButtonInfiniteLineVectorY;

QLineEdit*   lineEditInfiniteLineX1;
QLineEdit*   lineEditInfiniteLineY1;
QLineEdit*   lineEditInfiniteLineX2;
QLineEdit*   lineEditInfiniteLineY2;
QLineEdit*   lineEditInfiniteLineVectorX;
QLineEdit*   lineEditInfiniteLineVectorY;

/*Used when checking if fields vary*/
QString fieldOldText;
QString fieldNewText;
QString fieldVariesText;
QString fieldYesText;
QString fieldNoText;
QString fieldOnText;
QString fieldOffText;

QToolButton* toolButtonArcClockwise;
QComboBox* comboBoxArcClockwise;

QGroupBox* groupBoxGeometry[32];
QGroupBox* groupBoxGeneral;
QGroupBox* groupBoxMiscArc;
QGroupBox* groupBoxMiscPath;
QGroupBox* groupBoxMiscPolyline;
QGroupBox* groupBoxTextTextSingle;
QGroupBox* groupBoxMiscTextSingle;

QToolButton* toolButtonBlockX;
QToolButton* toolButtonBlockY;

QLineEdit* lineEditBlockX;
QLineEdit* lineEditBlockY;

QToolButton* toolButtonPathVertexNum;
QToolButton* toolButtonPathVertexX;
QToolButton* toolButtonPathVertexY;
QToolButton* toolButtonPathArea;
QToolButton* toolButtonPathLength;

QComboBox*   comboBoxPathVertexNum;
QLineEdit* lineEditPathVertexX;
QLineEdit* lineEditPathVertexY;
QLineEdit* lineEditPathArea;
QLineEdit* lineEditPathLength;

QToolButton* toolButtonPathClosed;

QComboBox*   comboBoxPathClosed;

QToolButton* toolButtonPolylineVertexNum;
QToolButton* toolButtonPolylineVertexX;
QToolButton* toolButtonPolylineVertexY;
QToolButton* toolButtonPolylineArea;
QToolButton* toolButtonPolylineLength;

QComboBox*   comboBoxPolylineVertexNum;
QLineEdit*   lineEditPolylineVertexX;
QLineEdit*   lineEditPolylineVertexY;
QLineEdit*   lineEditPolylineArea;
QLineEdit*   lineEditPolylineLength;

QToolButton* toolButtonPolylineClosed;

QComboBox*   comboBoxPolylineClosed;

QToolButton* toolButtonRayX1;
QToolButton* toolButtonRayY1;
QToolButton* toolButtonRayX2;
QToolButton* toolButtonRayY2;
QToolButton* toolButtonRayVectorX;
QToolButton* toolButtonRayVectorY;

QLineEdit*   lineEditRayX1;
QLineEdit*   lineEditRayY1;
QLineEdit*   lineEditRayX2;
QLineEdit*   lineEditRayY2;
QLineEdit*   lineEditRayVectorX;
QLineEdit*   lineEditRayVectorY;

QToolButton* toolButtonTextMultiX;
QToolButton* toolButtonTextMultiY;

QLineEdit*   lineEditTextMultiX;
QLineEdit*   lineEditTextMultiY;

QToolButton* toolButtonTextSingleX;
QToolButton* toolButtonTextSingleY;

QLineEdit*   lineEditTextSingleX;
QLineEdit*   lineEditTextSingleY;

QToolButton* toolButtonTextSingleBackward;
QToolButton* toolButtonTextSingleUpsideDown;

QComboBox*   comboBoxTextSingleBackward;
QComboBox*   comboBoxTextSingleUpsideDown;

MainWindow* _mainWin = 0;

/*
 * WARNING
 * -------
 * DO NOT enable QGraphicsItem::ItemIsMovable. If it is enabled,
 * and the item is double clicked, the scene will erratically move the item while zooming.
 * All movement has to be handled explicitly by us, not by the scene.
 */


void MainWindow::readSettings()
{
    debug_message("Reading Settings...");

    /* This file needs to be read from the users home directory to ensure it is writable. */
    QPoint pos(settings.window_x, settings.window_y);
    QSize size(settings.window_width, settings.window_height);

    /*
    layoutState = settings_file.value("LayoutState").toByteArray();
    if(!restoreState(layoutState))
    {
        debug_message("LayoutState NOT restored! Setting Default Layout...");
        //someToolBar->setVisible(1);
    }
    */

    load_settings();

    move(pos);
    resize(size);
}

void MainWindow::writeSettings()
{
    debug_message("Writing Settings...");

    settings.window_x = _mainWin->pos().x();
    settings.window_y = _mainWin->pos().y();
    settings.window_width = _mainWin->size().width();
    settings.window_height = _mainWin->size().height();

    save_settings();
}

void MainWindow::settingsDialog(const QString& showTab)
{
    Settings_Dialog dialog_(this, showTab, this);
    dialog_.exec();
}

View::View(MainWindow* mw, QGraphicsScene* theScene, QWidget* parent) : QGraphicsView(theScene, parent)
{
    mainWin = mw;
    gscene = theScene;

    setFrameShape(QFrame::NoFrame);

    /* NOTE: This has to be done before setting mouse tracking. */
    /*TODO: Review OpenGL for Qt5 later*/
    /*if (mainWin->settings.display_use_opengl) {*/
    /*    debug_message("Using OpenGL...");*/
    /*    setViewport(new QGLWidget(QGLFormat(QGL::DoubleBuffer)));*/
    /*}*/

    /*TODO: Review RenderHints later*/
    /*setRenderHint(QPainter::Antialiasing, mainWin->settings.display_render_hintAA());*/
    /*setRenderHint(QPainter::TextAntialiasing, mainWin->settings.display_render_hintTextAA());*/
    /*setRenderHint(QPainter::SmoothPixmapTransform, mainWin->settings.display_render_hintSmoothPix());*/
    /*setRenderHint(QPainter::HighQualityAntialiasing, mainWin->settings.display_render_hintHighAA());*/
    /*setRenderHint(QPainter::NonCosmeticDefaultPen, mainWin->settings.display_render_hint_noncosmetic);*/

    /* NOTE
     * ----
     * FullViewportUpdate MUST be used for both the GL and Qt renderers.
     * Qt renderer will not draw the foreground properly if it isnt set.
     */
    setViewportUpdateMode(QGraphicsView::FullViewportUpdate);

    panDistance = 10; /*TODO: should there be a setting for this???*/

    setCursor(Qt::BlankCursor);
    horizontalScrollBar()->setCursor(Qt::ArrowCursor);
    verticalScrollBar()->setCursor(Qt::ArrowCursor);
    qsnapLocatorColor = settings.qsnap_locator_color;
    gripColorCool = settings.selection_coolgrip_color;
    gripColorHot = settings.selection_hotgrip_color;
    setCrossHairColor(settings.display_crosshair_color);
    setCrossHairSize(settings.display_crosshair_percent);
    setGridColor(settings.grid_color);

    if (settings.grid_show_on_load)
        createGrid(settings.grid_type);
    else
        createGrid("");

    toggleRuler(settings.ruler_show_on_load);
    toggleReal(1); /*TODO: load this from file, else settings with default being 1*/

    settings.grippingActive = 0;
    settings.rapidMoveActive = 0;
    previewMode = PREVIEW_MODE_NULL;
    previewData = 0;
    previewObjectItemGroup = 0;
    pasteObjectItemGroup = 0;
    settings.previewActive = 0;
    settings.pastingActive = 0;
    settings.movingActive = 0;
    settings.selectingActive = 0;
    settings.zoomWindowActive = 0;
    settings.panningRealTimeActive = 0;
    settings.panningPointActive = 0;
    settings.panningActive = 0;
    settings.qSnapActive = 0;
    settings.qSnapToggle = 0;

    /* Randomize the hot grip location initially so it's not located at (0,0). */
    srand(1234);

    sceneGripPoint = QPointF((rand()%1000)*0.1, (rand()%1000)*0.1);

    gripBaseObj = 0;
    tempBaseObj = 0;

    selectBox = new SelectBox(QRubberBand::Rectangle, this);
    selectBox->setColors(QColor(settings.display_selectbox_left_color),
                         QColor(settings.display_selectbox_left_fill),
                         QColor(settings.display_selectbox_right_color),
                         QColor(settings.display_selectbox_right_fill),
                         settings.display_selectbox_alpha);

    showScrollBars(settings.display_show_scrollbars);
    setCornerButton();

    installEventFilter(this);

    setMouseTracking(1);
    setBackgroundColor(settings.display_bg_color);
    /*TODO: wrap this with a setBackgroundPixmap() function: setBackgroundBrush(QPixmap("images/canvas));*/

    connect(gscene, SIGNAL(selectionChanged()), this, SLOT(selectionChanged()));
}

View::~View()
{
    /*Prevent memory leaks by deleting any objects that were removed from the scene*/
    qDeleteAll(hashDeletedObjects.begin(), hashDeletedObjects.end());
    hashDeletedObjects.clear();

    /*Prevent memory leaks by deleting any unused instances*/
    qDeleteAll(previewObjectList.begin(), previewObjectList.end());
    previewObjectList.clear();
}

void View::enterEvent(QEvent* /*event*/)
{
    QMdiSubWindow* mdiWin = qobject_cast<QMdiSubWindow*>(parent());
    if(mdiWin) mainWin->mdiArea->setActiveSubWindow(mdiWin);
}

void View::addObject(BaseObject* obj)
{
    gscene->addItem(obj);
    gscene->update();
    hashDeletedObjects.remove(obj->objID);
}

void View::deleteObject(BaseObject* obj)
{
    /*NOTE: We really just remove the objects from the scene. deletion actually occurs in the destructor.*/
    obj->setSelected(0);
    gscene->removeItem(obj);
    gscene->update();
    hashDeletedObjects.insert(obj->objID, obj);
}

void View::previewOn(int clone, int mode, float x, float y, float data)
{
    debug_message("View previewOn()");
    previewOff(); /*Free the old objects before creating new ones*/

    previewMode = mode;

    /*Create new objects and add them to the scene in an item group.*/
    if     (clone == PREVIEW_CLONE_SELECTED) previewObjectList = createObjectList(gscene->selectedItems());
    else if(clone == PREVIEW_CLONE_RUBBER)   previewObjectList = createObjectList(rubberRoomList);
    else return;
    previewObjectItemGroup = gscene->createItemGroup(previewObjectList);

    if(previewMode == PREVIEW_MODE_MOVE   ||
       previewMode == PREVIEW_MODE_ROTATE ||
       previewMode == PREVIEW_MODE_SCALE)
    {
        previewPoint = QPointF(x, y); /*NOTE: Move: basePt; Rotate: basePt;   Scale: basePt;*/
        previewData = data;           /*NOTE: Move: unused; Rotate: refAngle; Scale: refFactor;*/
        settings.previewActive = 1;
    }
    else
    {
        previewMode = PREVIEW_MODE_NULL;
        previewPoint = QPointF();
        previewData = 0;
        settings.previewActive = 0;
    }

    gscene->update();
}

void View::previewOff()
{
    /*Prevent memory leaks by deleting any unused instances*/
    qDeleteAll(previewObjectList.begin(), previewObjectList.end());
    previewObjectList.clear();

    if(previewObjectItemGroup)
    {
        gscene->removeItem(previewObjectItemGroup);
        delete previewObjectItemGroup;
        previewObjectItemGroup = 0;
    }

    settings.previewActive = 0;

    gscene->update();
}

void View::enableMoveRapidFire()
{
    settings.rapidMoveActive = 1;
}

void View::disableMoveRapidFire()
{
    settings.rapidMoveActive = 0;
}

int View::allowRubber()
{
    /*if(!rubberRoomList.size()) //TODO: this check should be removed later*/
        return 1;
    return 0;
}

void View::addToRubberRoom(QGraphicsItem* item)
{
    rubberRoomList.append(item);
    item->show();
    gscene->update();
}

void View::vulcanizeRubberRoom()
{
    foreach(QGraphicsItem* item, rubberRoomList)
    {
        BaseObject* base = static_cast<BaseObject*>(item);
        if(base) vulcanizeObject(base);
    }
    rubberRoomList.clear();
    gscene->update();
}

void View::vulcanizeObject(BaseObject* obj)
{
    if(!obj) return;
    gscene->removeItem(obj);
    /* Prevent Qt Runtime Warning, QGraphicsScene::addItem:
     * item has already been added to this scene.
     */
    obj->vulcanize();
}

void View::clearRubberRoom()
{
    foreach(QGraphicsItem* item, rubberRoomList)
    {
        BaseObject* base = static_cast<BaseObject*>(item);
        if(base)
        {
            int type = base->type();
            if((type == OBJ_TYPE_PATH     && spareRubberList.contains(SPARE_RUBBER_PATH))     ||
               (type == OBJ_TYPE_POLYGON  && spareRubberList.contains(SPARE_RUBBER_POLYGON))  ||
               (type == OBJ_TYPE_POLYLINE && spareRubberList.contains(SPARE_RUBBER_POLYLINE)) ||
               (spareRubberList.contains(base->objID)))
            {
                if(!base->objectPath().elementCount())
                {
                    QMessageBox::critical(this, tr("Empty Rubber Object Error"),
                                          tr("The rubber object added contains no points. "
  "The command that created this object has flawed logic. "
  "The object will be deleted."));
                    gscene->removeItem(item);
                    delete item;
                }
                else
                    vulcanizeObject(base);
            }
            else
            {
                gscene->removeItem(item);
                delete item;
            }
        }
    }

    rubberRoomList.clear();
    spareRubberList.clear();
    gscene->update();
}

void View::spareRubber(int id)
{
    spareRubberList.append(id);
}

void View::setRubberMode(int mode)
{
    foreach(QGraphicsItem* item, rubberRoomList)
    {
        BaseObject* base = static_cast<BaseObject*>(item);
        if(base) { base->setObjectRubberMode(mode); }
    }
    gscene->update();
}

void View::setRubberPoint(const QString& key, const QPointF& point)
{
    foreach(QGraphicsItem* item, rubberRoomList)
    {
        BaseObject* base = static_cast<BaseObject*>(item);
        if(base) { base->setObjectRubberPoint(key, point); }
    }
    gscene->update();
}

void View::setRubberText(const QString& key, const QString& txt)
{
    foreach(QGraphicsItem* item, rubberRoomList)
    {
        BaseObject* base = static_cast<BaseObject*>(item);
        if(base) { base->setObjectRubberText(key, txt); }
    }
    gscene->update();
}

void View::setGridColor(unsigned int color)
{
    gridColor = QColor(color);
    gscene->setProperty("VIEW_COLOR_GRID", color);
    if(gscene) gscene->update();
}

void View::setRulerColor(unsigned int color)
{
    rulerColor = QColor(color);
    gscene->update();
}

void View::createGrid(const QString& gridType)
{
    if (gridType == "Rectangular") {
        createGridRect();
        gscene->setProperty("ENABLE_GRID", 1);
    }
    else if(gridType == "Circular") {
        createGridPolar();
        gscene->setProperty("ENABLE_GRID", 1);
    }
    else if(gridType == "Isometric") {
        createGridIso();
        gscene->setProperty("ENABLE_GRID", 1);
    }
    else {
        gridPath = QPainterPath();
        gscene->setProperty("ENABLE_GRID", 0);
    }

    createOrigin();

    /* EXPERIMENT
     * Tagging experiments with the path system to the origin.
     */

    float position[] = {10.0, 0.0};
    float scale[] = {1.0, 1.0};
    add_list_to_path(&originPath, origin_string, position, scale);

    gscene->update();
}

void View::createOrigin() /* TODO: Make Origin Customizable */
{
    originPath = QPainterPath();

    if (settings.grid_show_origin) {
        /* originPath.addEllipse(QPointF(0,0), 0.5, 0.5);*/
        /* TODO: Make Origin Customizable */
        float position[] = {0.0, 0.0};
        float scale[] = {1.0, 1.0};
        add_list_to_path(&originPath, origin_string, position, scale);
    }
}

void View::createGridRect()
{
    float xSpacing = settings.grid_spacing.x;
    float ySpacing = settings.grid_spacing.y;

    QRectF gr(0, 0, settings.grid_size.x, -settings.grid_size.y);
    /*Ensure the loop will work correctly with negative numbers*/
    float x1 = embMinDouble(gr.left(), gr.right());
    float y1 = embMinDouble(gr.top(), gr.bottom());
    float x2 = embMaxDouble(gr.left(), gr.right());
    float y2 = embMaxDouble(gr.top(), gr.bottom());

    gridPath = QPainterPath();
    gridPath.addRect(gr);
    for (float gx = x1; gx < x2; gx += xSpacing) {
        for (float gy = y1; gy < y2; gy += ySpacing) {
            gridPath.moveTo(x1,gy);
            gridPath.lineTo(x2,gy);
            gridPath.moveTo(gx,y1);
            gridPath.lineTo(gx,y2);
        }
    }

    /*Center the Grid*/
    QRectF gridRect = gridPath.boundingRect();
    float bx = gridRect.width()/2.0;
    float by = -gridRect.height()/2.0;
    float cx = settings.grid_center.x;
    float cy = -settings.grid_center.y;
    float dx = cx - bx;
    float dy = cy - by;

    if(settings.grid_center_on_origin)
        gridPath.translate(-bx, -by);
    else
        gridPath.translate(dx, dy);
}

void View::createGridPolar()
{
    float radSpacing = settings.grid_spacing_radius;
    float angSpacing = settings.grid_spacing_angle;

    float rad = settings.grid_size_radius;

    gridPath = QPainterPath();
    gridPath.addEllipse(QPointF(0,0), rad, rad);
    for(float r = 0; r < rad; r += radSpacing) {
        gridPath.addEllipse(QPointF(0,0), r, r);
    }
    for(float ang = 0; ang < 360; ang += angSpacing) {
        gridPath.moveTo(0,0);
        gridPath.lineTo(QLineF::fromPolar(rad, ang).p2());
    }

    if(!settings.grid_center_on_origin)
        gridPath.translate(settings.grid_center.x, -settings.grid_center.y);
}

void View::createGridIso()
{
    /* Ensure the loop will work correctly with negative numbers */
    float isoW = fabs(settings.grid_size.x);
    float isoH = fabs(settings.grid_size.y);

    QPointF p1 = QPointF(0,0);
    QPointF p2 = QLineF::fromPolar(isoW, 30).p2();
    QPointF p3 = QLineF::fromPolar(isoH, 150).p2();
    QPointF p4 = p2 + p3;

    gridPath = QPainterPath();
    gridPath.moveTo(p1);
    gridPath.lineTo(p2);
    gridPath.lineTo(p4);
    gridPath.lineTo(p3);
    gridPath.lineTo(p1);

    for (float x = 0; x < isoW; x += settings.grid_spacing.x) {
        for (float y = 0; y < isoH; y += settings.grid_spacing.y) {
            QPointF px = QLineF::fromPolar(x, 30).p2();
            QPointF py = QLineF::fromPolar(y, 150).p2();

            gridPath.moveTo(px);
            gridPath.lineTo(px+p3);
            gridPath.moveTo(py);
            gridPath.lineTo(py+p2);
        }
    }

    /*Center the Grid*/

    QRectF gridRect = gridPath.boundingRect();
    /* bx is unused*/
    float by = -gridRect.height()/2.0;
    float cx = settings.grid_center.x;
    float cy = -settings.grid_center.y;

    if (settings.grid_center_on_origin) {
        gridPath.translate(0, -by);
    }
    else {
        gridPath.translate(0, -by);
        gridPath.translate(cx, cy);
    }
}

void View::toggleSnap(int on)
{
    debug_message("View toggleSnap()");
    QApplication::setOverrideCursor(Qt::WaitCursor);
    /*TODO: finish this*/
    gscene->setProperty("ENABLE_SNAP", on);
    gscene->update();
    QApplication::restoreOverrideCursor();
}

void View::toggleGrid(int on)
{
    debug_message("View toggleGrid()");
    QApplication::setOverrideCursor(Qt::WaitCursor);
    if(on) { createGrid(settings.grid_type); }
    else   { createGrid(""); }
    QApplication::restoreOverrideCursor();
}

void View::toggleRuler(int on)
{
    debug_message("View toggleRuler()");
    QApplication::setOverrideCursor(Qt::WaitCursor);
    gscene->setProperty("ENABLE_RULER", on);
    settings.rulerMetric = settings.ruler_metric;
    rulerColor = QColor(settings.ruler_color);
    settings.rulerPixelSize = settings.ruler_pixel_size;
    gscene->update();
    QApplication::restoreOverrideCursor();
}

void View::toggleOrtho(int on)
{
    debug_message("View toggleOrtho()");
    QApplication::setOverrideCursor(Qt::WaitCursor);
    /*TODO: finish this*/
    gscene->setProperty("ENABLE_ORTHO", on);
    gscene->update();
    QApplication::restoreOverrideCursor();
}

void View::togglePolar(int on)
{
    debug_message("View togglePolar()");
    QApplication::setOverrideCursor(Qt::WaitCursor);
    /*TODO: finish this*/
    gscene->setProperty("ENABLE_POLAR", on);
    gscene->update();
    QApplication::restoreOverrideCursor();
}

void View::toggleQSnap(int on)
{
    debug_message("View toggleQSnap()");
    QApplication::setOverrideCursor(Qt::WaitCursor);
    settings.qSnapToggle = on;
    gscene->setProperty("ENABLE_QSNAP", on);
    gscene->update();
    QApplication::restoreOverrideCursor();
}

void View::toggleQTrack(int on)
{
    debug_message("View toggleQTrack()");
    QApplication::setOverrideCursor(Qt::WaitCursor);
    /*TODO: finish this*/
    gscene->setProperty("ENABLE_QTRACK", on);
    gscene->update();
    QApplication::restoreOverrideCursor();
}

void View::toggleLwt(int on)
{
    debug_message("View toggleLwt()");
    QApplication::setOverrideCursor(Qt::WaitCursor);
    gscene->setProperty("ENABLE_LWT", on);
    gscene->update();
    QApplication::restoreOverrideCursor();
}

void View::toggleReal(int on)
{
    debug_message("View toggleReal()");
    QApplication::setOverrideCursor(Qt::WaitCursor);
    gscene->setProperty("ENABLE_REAL", on);
    gscene->update();
    QApplication::restoreOverrideCursor();
}

int View::isLwtEnabled()
{
    return gscene->property("ENABLE_LWT").toBool();
}

int View::isRealEnabled()
{
    return gscene->property("ENABLE_REAL").toBool();
}

void View::drawBackground(QPainter* painter, const QRectF& rect)
{
    painter->fillRect(rect, backgroundBrush());

    /* HACK int a = rect.intersects(gridPath.controlPointRect(); */
    int a = 1;
    if (gscene->property("ENABLE_GRID").toBool() && a)
    {
        QPen gridPen(gridColor);
        gridPen.setJoinStyle(Qt::MiterJoin);
        gridPen.setCosmetic(1);
        painter->setPen(gridPen);
        painter->drawPath(gridPath);
        painter->drawPath(originPath);
        painter->fillPath(originPath, gridColor);
    }
}

/*
float little = 0.20, medium = 0.40;
float tic_metric_lengths[] = {
    0.0, little, little, little, little, middle,
    little, little, little, little
};
float tic_imperial_lengths[] = {
    0.0, little, little, little, medium,
    little, little, little, medium,
    little, little, little, medium,
    little, little, little
};
*/

void View::drawForeground(QPainter* painter, const QRectF& rect)
{
    /* ==================================================
     * Draw grip points for all selected objects
     * ================================================== */

    QPen gripPen(QColor::fromRgb(gripColorCool));
    gripPen.setWidth(2);
    gripPen.setJoinStyle(Qt::MiterJoin);
    gripPen.setCosmetic(1);
    painter->setPen(gripPen);
    QPoint gripOffset(settings.selection_grip_size, settings.selection_grip_size);

    QList<QPointF> selectedGripPoints;
    QList<QGraphicsItem*> selectedItemList = gscene->selectedItems();
    if (selectedItemList.size() <= 100) {
        foreach(QGraphicsItem* item, selectedItemList) {
            if(item->type() >= OBJ_TYPE_BASE) {
                tempBaseObj = static_cast<BaseObject*>(item);
                if(tempBaseObj) { selectedGripPoints = tempBaseObj->allGripPoints(); }

                foreach(QPointF ssp, selectedGripPoints) {
                    QPoint p1 = mapFromScene(ssp) - gripOffset;
                    QPoint q1 = mapFromScene(ssp) + gripOffset;

                    if(ssp == sceneGripPoint)
                        painter->fillRect(QRectF(mapToScene(p1), mapToScene(q1)), QColor::fromRgb(gripColorHot));
                    else
                        painter->drawRect(QRectF(mapToScene(p1), mapToScene(q1)));
                }
            }
        }
    }

    /* ==================================================
     * Draw the closest qsnap point
     * ================================================== */

    if(!settings.selectingActive) /*TODO: && findClosestSnapPoint == 1*/
    {
        QPen qsnapPen(QColor::fromRgb(qsnapLocatorColor));
        qsnapPen.setWidth(2);
        qsnapPen.setJoinStyle(Qt::MiterJoin);
        qsnapPen.setCosmetic(1);
        painter->setPen(qsnapPen);
        QPoint qsnapOffset(settings.qsnap_locator_size, settings.qsnap_locator_size);

        QList<QPointF> apertureSnapPoints;
        QList<QGraphicsItem *> apertureItemList = items(viewMousePoint.x()-settings.qsnap_aperture_size,
                                                        viewMousePoint.y()-settings.qsnap_aperture_size,
                                                        settings.qsnap_aperture_size*2,
                                                        settings.qsnap_aperture_size*2);
        foreach (QGraphicsItem* item, apertureItemList) {
            if (item->type() >= OBJ_TYPE_BASE) {
                tempBaseObj = static_cast<BaseObject*>(item);
                if(tempBaseObj) { apertureSnapPoints << tempBaseObj->mouseSnapPoint(to_qpointf(sceneMousePoint)); }
            }
        }
        /*TODO: Check for intersection snap points and add them to the list*/
        foreach(QPointF asp, apertureSnapPoints)
        {
            QPoint p1 = mapFromScene(asp) - qsnapOffset;
            QPoint q1 = mapFromScene(asp) + qsnapOffset;
            painter->drawRect(QRectF(mapToScene(p1), mapToScene(q1)));
        }
    }

    /* ==================================================
     * Draw horizontal and vertical rulers
     * ================================================== */

    if (gscene->property("ENABLE_RULER").toBool()) {
        int proceed = 1;

        int vw = width();  /*View Width*/
        int vh = height(); /*View Height*/
        QPointF origin = mapToScene(0,0);
        QPointF rulerHoriz = mapToScene(vw, settings.rulerPixelSize);
        QPointF rulerVert = mapToScene(settings.rulerPixelSize, vh);

        float ox = origin.x();
        float oy = origin.y();

        float rhx = rulerHoriz.x();
        float rhy = rulerHoriz.y();
        float rhw = rhx - ox;
        float rhh = rhy - oy;

        float rvx = rulerVert.x();
        float rvy = rulerVert.y();
        float rvw = rvx - ox;
        float rvh = rvy - oy;

        /*
         * NOTE:
         * Drawing ruler if zoomed out too far will cause an assertion failure.
         * We will limit the maximum size the ruler can be shown at.
         */

        unsigned short maxSize = -1; /*Intentional underflow*/
        if(rhw >= maxSize || rvh >= maxSize) proceed = 0;

        if (proceed) {
            int distance = mapToScene(settings.rulerPixelSize*3, 0).x() - ox;
            QString distStr = QString().setNum(distance);
            int distStrSize = distStr.size();
            int msd = distStr.at(0).digitValue(); /*Most Significant Digit*/

            if(msd != -1)
            {

                msd++;
                if(msd == 10)
                {
                    msd = 1;
                    distStr.resize(distStrSize+1);
                    distStrSize++;
                }

                distStr.replace(0, 1, QString().setNum(msd));
                for(int i = 1; i < distStrSize; ++i)
                {
                    distStr.replace(i, 1, '0');
                }
                int unit = distStr.toInt();
                float fraction;
                int feet = 1;
                if (settings.rulerMetric) {
                    if(unit < 10) unit = 10;
                    fraction = unit/10;
                }
                else {
                    if (unit <= 1) {
                        unit = 1;
                        feet = 0;
                        fraction = (float)(unit/16);
                    }
                    else
                    {
                        unit = roundToMultiple(1, unit, 12);
                        fraction = unit/12;
                    }
                }

                float little = 0.20;
                float medium = 0.40;
                float rhTextOffset = mapToScene(3, 0).x() - ox;
                float rvTextOffset = mapToScene(0, 3).y() - oy;
                float textHeight = rhh*medium;

                QVector<QLineF> lines;
                lines.append(QLineF(ox, rhy, rhx, rhy));
                lines.append(QLineF(rvx, oy, rvx, rvy));

                float mx = sceneMousePoint.x;
                float my = sceneMousePoint.y;
                lines.append(QLineF(mx, rhy, mx, oy));
                lines.append(QLineF(rvx, my, ox, my));

                QTransform transform;

                QPen rulerPen(QColor(0,0,0));
                rulerPen.setCosmetic(1);
                painter->setPen(rulerPen);
                painter->fillRect(QRectF(ox, oy, rhw, rhh), rulerColor);
                painter->fillRect(QRectF(ox, oy, rvw, rvh), rulerColor);

                int xFlow, xStart, yFlow, yStart;
                if (willUnderflowInt32(ox, unit)) {
                    proceed = 0;
                }
                else {
                    xFlow = roundToMultiple(0, ox, unit);
                }
                if (willUnderflowInt32(xFlow, unit)) {
                    proceed = 0;
                }
                else { xStart = xFlow - unit; }
                if (willUnderflowInt32(oy, unit)) { proceed = 0; }
                else { yFlow = roundToMultiple(0, oy, unit); }
                if(willUnderflowInt32(yFlow, unit)) { proceed = 0; }
                else                             { yStart = yFlow - unit; }

                if (proceed) {
                    for (int x = xStart; x < rhx; x += unit) {
                        transform.translate(x+rhTextOffset, rhy-rhh/2);
                        QPainterPath rulerTextPath;
                        if (settings.rulerMetric) {
                            rulerTextPath = transform.map(createRulerTextPath(0, 0, QString().setNum(x), textHeight));
                        }
                        else {
                            if(feet)
                                rulerTextPath = transform.map(createRulerTextPath(0, 0, QString().setNum(x/12).append('\''), textHeight));
                            else
                                rulerTextPath = transform.map(createRulerTextPath(0, 0, QString().setNum(x).append('\"'), textHeight));
                        }
                        transform.reset();
                        painter->drawPath(rulerTextPath);

                        lines.append(QLineF(x, rhy, x, oy));
                        if (settings.rulerMetric) {
                            lines.append(QLineF(x, rhy, x, oy));
                            lines.append(QLineF(x+fraction  , rhy, x+fraction, rhy-rhh*little));
                            lines.append(QLineF(x+fraction*2, rhy, x+fraction*2, rhy-rhh*little));
                            lines.append(QLineF(x+fraction*3, rhy, x+fraction*3, rhy-rhh*little));
                            lines.append(QLineF(x+fraction*4, rhy, x+fraction*4, rhy-rhh*little));
                            lines.append(QLineF(x+fraction*5, rhy, x+fraction*5, rhy-rhh*medium)); /*Half*/
                            lines.append(QLineF(x+fraction*6, rhy, x+fraction*6, rhy-rhh*little));
                            lines.append(QLineF(x+fraction*7, rhy, x+fraction*7, rhy-rhh*little));
                            lines.append(QLineF(x+fraction*8, rhy, x+fraction*8, rhy-rhh*little));
                            lines.append(QLineF(x+fraction*9, rhy, x+fraction*9, rhy-rhh*little));
                        }
                        else {
                            if (feet) {
                                for (int i = 0; i < 12; ++i) {
                                    lines.append(QLineF(x+fraction*i, rhy, x+fraction*i, rhy-rhh*medium));
                                }
                            }
                            else
                            {
                                lines.append(QLineF(x+fraction   , rhy, x+fraction, rhy-rhh*little));
                                lines.append(QLineF(x+fraction* 2, rhy, x+fraction* 2, rhy-rhh*little));
                                lines.append(QLineF(x+fraction* 3, rhy, x+fraction* 3, rhy-rhh*little));
                                lines.append(QLineF(x+fraction* 4, rhy, x+fraction* 4, rhy-rhh*medium)); /*Quarter*/
                                lines.append(QLineF(x+fraction* 5, rhy, x+fraction* 5, rhy-rhh*little));
                                lines.append(QLineF(x+fraction* 6, rhy, x+fraction* 6, rhy-rhh*little));
                                lines.append(QLineF(x+fraction* 7, rhy, x+fraction* 7, rhy-rhh*little));
                                lines.append(QLineF(x+fraction* 8, rhy, x+fraction* 8, rhy-rhh*medium)); /*Half*/
                                lines.append(QLineF(x+fraction* 9, rhy, x+fraction* 9, rhy-rhh*little));
                                lines.append(QLineF(x+fraction*10, rhy, x+fraction*10, rhy-rhh*little));
                                lines.append(QLineF(x+fraction*11, rhy, x+fraction*11, rhy-rhh*little));
                                lines.append(QLineF(x+fraction*12, rhy, x+fraction*12, rhy-rhh*medium)); /*Quarter*/
                                lines.append(QLineF(x+fraction*13, rhy, x+fraction*13, rhy-rhh*little));
                                lines.append(QLineF(x+fraction*14, rhy, x+fraction*14, rhy-rhh*little));
                                lines.append(QLineF(x+fraction*15, rhy, x+fraction*15, rhy-rhh*little));
                            }
                        }
                    }
                    for (int y = yStart; y < rvy; y += unit) {
                        transform.translate(rvx-rvw/2, y-rvTextOffset);
                        transform.rotate(-90);
                        QPainterPath rulerTextPath;
                        if (settings.rulerMetric) {
                            rulerTextPath = transform.map(createRulerTextPath(0, 0, QString().setNum(-y), textHeight));
                        }
                        else {
                            if(feet)
                                rulerTextPath = transform.map(createRulerTextPath(0, 0, QString().setNum(-y/12).append('\''), textHeight));
                            else
                                rulerTextPath = transform.map(createRulerTextPath(0, 0, QString().setNum(-y).append('\"'), textHeight));
                        }
                        transform.reset();
                        painter->drawPath(rulerTextPath);

                        lines.append(QLineF(rvx, y, ox, y));
                        if (settings.rulerMetric) {
                            lines.append(QLineF(rvx, y+fraction  , rvx-rvw*little, y+fraction));
                            lines.append(QLineF(rvx, y+fraction*2, rvx-rvw*little, y+fraction*2));
                            lines.append(QLineF(rvx, y+fraction*3, rvx-rvw*little, y+fraction*3));
                            lines.append(QLineF(rvx, y+fraction*4, rvx-rvw*little, y+fraction*4));
                            lines.append(QLineF(rvx, y+fraction*5, rvx-rvw*medium, y+fraction*5)); /*Half*/
                            lines.append(QLineF(rvx, y+fraction*6, rvx-rvw*little, y+fraction*6));
                            lines.append(QLineF(rvx, y+fraction*7, rvx-rvw*little, y+fraction*7));
                            lines.append(QLineF(rvx, y+fraction*8, rvx-rvw*little, y+fraction*8));
                            lines.append(QLineF(rvx, y+fraction*9, rvx-rvw*little, y+fraction*9));
                        }
                        else {
                            if (feet) {
                                for (int i = 0; i < 12; ++i) {
                                    lines.append(QLineF(rvx, y+fraction*i, rvx-rvw*medium, y+fraction*i));
                                }
                            }
                            else {
                                lines.append(QLineF(rvx, y+fraction   , rvx-rvw*little, y+fraction));
                                lines.append(QLineF(rvx, y+fraction* 2, rvx-rvw*little, y+fraction* 2));
                                lines.append(QLineF(rvx, y+fraction* 3, rvx-rvw*little, y+fraction* 3));
                                lines.append(QLineF(rvx, y+fraction* 4, rvx-rvw*medium, y+fraction* 4)); /*Quarter*/
                                lines.append(QLineF(rvx, y+fraction* 5, rvx-rvw*little, y+fraction* 5));
                                lines.append(QLineF(rvx, y+fraction* 6, rvx-rvw*little, y+fraction* 6));
                                lines.append(QLineF(rvx, y+fraction* 7, rvx-rvw*little, y+fraction* 7));
                                lines.append(QLineF(rvx, y+fraction* 8, rvx-rvw*medium, y+fraction* 8)); /*Half*/
                                lines.append(QLineF(rvx, y+fraction* 9, rvx-rvw*little, y+fraction* 9));
                                lines.append(QLineF(rvx, y+fraction*10, rvx-rvw*little, y+fraction*10));
                                lines.append(QLineF(rvx, y+fraction*11, rvx-rvw*little, y+fraction*11));
                                lines.append(QLineF(rvx, y+fraction*12, rvx-rvw*medium, y+fraction*12)); /*Quarter*/
                                lines.append(QLineF(rvx, y+fraction*13, rvx-rvw*little, y+fraction*13));
                                lines.append(QLineF(rvx, y+fraction*14, rvx-rvw*little, y+fraction*14));
                                lines.append(QLineF(rvx, y+fraction*15, rvx-rvw*little, y+fraction*15));
                            }
                        }
                    }
                }

                painter->drawLines(lines);
                painter->fillRect(QRectF(ox, oy, rvw, rhh), rulerColor);
            }
        }
    }

    /*==================================================*/
    /*Draw the crosshair*/
    /*==================================================*/

    if (!settings.selectingActive) {
        /*painter->setBrush(Qt::NoBrush);*/
        QPen crosshairPen(QColor::fromRgb(crosshairColor));
        crosshairPen.setCosmetic(1);
        painter->setPen(crosshairPen);
        painter->drawLine(QLineF(mapToScene(viewMousePoint.x(), viewMousePoint.y()-settings.crosshairSize),
                                 mapToScene(viewMousePoint.x(), viewMousePoint.y()+settings.crosshairSize)));
        painter->drawLine(QLineF(mapToScene(viewMousePoint.x()-settings.crosshairSize, viewMousePoint.y()),
                                 mapToScene(viewMousePoint.x()+settings.crosshairSize, viewMousePoint.y())));
        painter->drawRect(QRectF(
            mapToScene(viewMousePoint.x()-settings.selection_pickbox_size,
                viewMousePoint.y()-settings.selection_pickbox_size),
            mapToScene(viewMousePoint.x()+settings.selection_pickbox_size,
                viewMousePoint.y()+settings.selection_pickbox_size)));
    }
}

int View::willUnderflowInt32(int a, int b)
{
    int c;
    Q_ASSERT(LLONG_MAX>INT_MAX);
    c = (int)a-b;
    return (c < INT_MIN || c > INT_MAX);
}

int View::willOverflowInt32(int a, int b)
{
    int c;
    Q_ASSERT(LLONG_MAX>INT_MAX);
    c = (int)a+b;
    return (c < INT_MIN || c > INT_MAX);
}


QPainterPath View::createRulerTextPath(float x, float y, QString str, float height)
{
    QPainterPath path;

    float xScale = height;
    float yScale = height;
    float scale[2];
    float pos[2];
    pos[0] = x;
    pos[1] = y;
    scale[0] = 0.01*height;
    scale[1] = 0.01*height;

    int len = str.length();
    for (int i = 0; i < len; ++i) {
        if (str[i] == QChar('1')) {
            add_to_path(&path, symbol_list[SYMBOL_one], pos, scale);
        }
        else if(str[i] == QChar('2')) {
            path.moveTo(x+0.00*xScale, y-0.75*yScale);
            path.arcTo(x+0.00*xScale, y-1.00*yScale, 0.50*xScale, 0.50*yScale, 180.00, -216.87);
            path.lineTo(x+0.00*xScale, y-0.00*yScale);
            path.lineTo(x+0.50*xScale, y-0.00*yScale);
        }
        else if(str[i] == QChar('3'))
        {
            path.arcMoveTo(x+0.00*xScale, y-0.50*yScale, 0.50*xScale, 0.50*yScale, 195.00);
            path.arcTo(x+0.00*xScale, y-0.50*yScale, 0.50*xScale, 0.50*yScale, 195.00, 255.00);
            path.arcTo(x+0.00*xScale, y-1.00*yScale, 0.50*xScale, 0.50*yScale, 270.00, 255.00);
        }
        else if(str[i] == QChar('4'))
        {
            path.moveTo(x+0.50*xScale, y-0.00*yScale);
            path.lineTo(x+0.50*xScale, y-1.00*yScale);
            path.lineTo(x+0.00*xScale, y-0.50*yScale);
            path.lineTo(x+0.50*xScale, y-0.50*yScale);
        }
        else if(str[i] == QChar('5'))
        {
            path.moveTo(x+0.50*xScale, y-1.00*yScale);
            path.lineTo(x+0.00*xScale, y-1.00*yScale);
            path.lineTo(x+0.00*xScale, y-0.50*yScale);
            path.lineTo(x+0.25*xScale, y-0.50*yScale);
            path.arcTo(x+0.00*xScale, y-0.50*yScale, 0.50*xScale, 0.50*yScale, 90.00, -180.00);
            path.lineTo(x+0.00*xScale, y-0.00*yScale);
        }
        else if(str[i] == QChar('6'))
        {
            path.addEllipse(QPointF(x+0.25*xScale, y-0.25*yScale), 0.25*xScale, 0.25*yScale);
            path.moveTo(x+0.00*xScale, y-0.25*yScale);
            path.lineTo(x+0.00*xScale, y-0.75*yScale);
            path.arcTo(x+0.00*xScale, y-1.00*yScale, 0.50*xScale, 0.50*yScale, 180.00, -140.00);
        }
        else if(str[i] == QChar('7'))
        {
            path.moveTo(x+0.00*xScale, y-1.00*yScale);
            path.lineTo(x+0.50*xScale, y-1.00*yScale);
            path.lineTo(x+0.25*xScale, y-0.25*yScale);
            path.lineTo(x+0.25*xScale, y-0.00*yScale);
        }
        else if(str[i] == QChar('8'))
        {
            path.addEllipse(QPointF(x+0.25*xScale, y-0.25*yScale), 0.25*xScale, 0.25*yScale);
            path.addEllipse(QPointF(x+0.25*xScale, y-0.75*yScale), 0.25*xScale, 0.25*yScale);
        }
        else if(str[i] == QChar('9'))
        {
            path.addEllipse(QPointF(x+0.25*xScale, y-0.75*yScale), 0.25*xScale, 0.25*yScale);
            path.moveTo(x+0.50*xScale, y-0.75*yScale);
            path.lineTo(x+0.50*xScale, y-0.25*yScale);
            path.arcTo(x+0.00*xScale, y-0.50*yScale, 0.50*xScale, 0.50*yScale, 0.00, -140.00);
        }
        else if(str[i] == QChar('0'))
        {
            /*path.addEllipse(QPointF(x+0.25*xScale, y-0.50*yScale), 0.25*xScale, 0.50*yScale);*/

            path.moveTo(x+0.00*xScale, y-0.75*yScale);
            path.lineTo(x+0.00*xScale, y-0.25*yScale);
            path.arcTo(x+0.00*xScale, y-0.50*yScale, 0.50*xScale, 0.50*yScale, 180.00, 180.00);
            path.lineTo(x+0.50*xScale, y-0.75*yScale);
            path.arcTo(x+0.00*xScale, y-1.00*yScale, 0.50*xScale, 0.50*yScale, 0.00, 180.00);
        }
        else if(str[i] == QChar('-'))
        {
            path.moveTo(x+0.00*xScale, y-0.50*yScale);
            path.lineTo(x+0.50*xScale, y-0.50*yScale);
        }
        else if(str[i] == QChar('\''))
        {
            path.moveTo(x+0.25*xScale, y-1.00*yScale);
            path.lineTo(x+0.25*xScale, y-0.75*yScale);
        }
        else if(str[i] == QChar('\"'))
        {
            path.moveTo(x+0.10*xScale, y-1.00*yScale);
            path.lineTo(x+0.10*xScale, y-0.75*yScale);
            path.moveTo(x+0.40*xScale, y-1.00*yScale);
            path.lineTo(x+0.40*xScale, y-0.75*yScale);
        }

        x += 0.75*xScale;
        pos[0] = x;
    }

    return path;
}

int View::roundToMultiple(int roundUp, int numToRound, int multiple)
{
    if(multiple == 0)
        return numToRound;
    int remainder = numToRound % multiple;
    if(remainder == 0)
        return numToRound;

    if(numToRound < 0 && roundUp)
        return numToRound - remainder;
    if(roundUp)
        return numToRound + multiple - remainder;
    /*else round down*/
    if(numToRound < 0 && !roundUp)
        return numToRound - multiple - remainder;
    return numToRound - remainder;
}

void View::updateMouseCoords(int x, int y)
{
    viewMousePoint = QPoint(x, y);
    sceneMousePoint = to_emb_vector(mapToScene(viewMousePoint));
    gscene->setProperty("SCENE_QSNAP_POINT", to_qpointf(sceneMousePoint)); /*TODO: if qsnap functionality is enabled, use it rather than the mouse point*/
    gscene->setProperty("SCENE_MOUSE_POINT", to_qpointf(sceneMousePoint));
    gscene->setProperty("VIEW_MOUSE_POINT", viewMousePoint);
    mainWin->statusbar->setMouseCoord(sceneMousePoint.x, -sceneMousePoint.y);
}

void View::setCrossHairSize(unsigned char percent)
{
    /*NOTE: crosshairSize is in pixels and is a percentage of your screen width*/
    /*NOTE: Example: (1280*0.05)/2 = 32, thus 32 + 1 + 32 = 65 pixel wide crosshair*/
    unsigned int screenWidth = qApp->screens()[0]->geometry().width();
    if(percent > 0 && percent < 100) {
        settings.crosshairSize = (screenWidth*(percent/100.0))/2;
    }
    else {
        settings.crosshairSize = screenWidth;
    }
}

void View::setCornerButton()
{
    int num = settings.display_scrollbar_widget_num;
    if (num) {
        QPushButton* cornerButton = new QPushButton(this);
        cornerButton->setFlat(1);
        QAction* act = mainWin->actionHash.value(num);
        /*NOTE: Prevent crashing if the action is NULL.*/
        if (!act) {
            QMessageBox::information(this, tr("Corner Widget Error"), tr("There are unused enum values in COMMAND_ACTIONS. Please report this as a bug."));
            setCornerWidget(0);
        }
        else {
            cornerButton->setIcon(act->icon());
            connect(cornerButton, SIGNAL(clicked()), this, SLOT(cornerButtonClicked()));
            setCornerWidget(cornerButton);
            cornerButton->setCursor(Qt::ArrowCursor);
        }
    }
    else {
        setCornerWidget(0);
    }
}

void View::cornerButtonClicked()
{
    debug_message("Corner Button Clicked.");
    mainWin->actionHash.value(settings.display_scrollbar_widget_num)->trigger();
}

void View::zoomIn()
{
    debug_message("View zoomIn()");
    if (!allowZoomIn()) {
        return;
    }
    QApplication::setOverrideCursor(Qt::WaitCursor);
    QPointF cntr = mapToScene(QPoint(width()/2,height()/2));
    float s = settings.display_zoomscale_in;
    scale(s, s);

    centerOn(cntr);
    QApplication::restoreOverrideCursor();
}

void View::zoomOut()
{
    debug_message("View zoomOut()");
    if(!allowZoomOut()) { return; }
    QApplication::setOverrideCursor(Qt::WaitCursor);
    QPointF cntr = mapToScene(QPoint(width()/2,height()/2));
    float s = settings.display_zoomscale_out;
    scale(s, s);

    centerOn(cntr);
    QApplication::restoreOverrideCursor();
}

void View::zoomWindow()
{
    settings.zoomWindowActive = 1;
    settings.selectingActive = 0;
    clearSelection();
}

void View::zoomSelected()
{
    QApplication::setOverrideCursor(Qt::WaitCursor);
    QList<QGraphicsItem*> itemList = gscene->selectedItems();
    QPainterPath selectedRectPath;
    foreach(QGraphicsItem* item, itemList) {
        selectedRectPath.addPolygon(item->mapToScene(item->boundingRect()));
    }
    QRectF selectedRect = selectedRectPath.boundingRect();
    if (selectedRect.isNull()) {
        QMessageBox::information(this, tr("ZoomSelected Preselect"), tr("Preselect objects before invoking the zoomSelected command."));
        /*TODO: Support Post selection of objects*/
    }
    fitInView(selectedRect, Qt::KeepAspectRatio);
    QApplication::restoreOverrideCursor();
}

void View::zoomExtents()
{
    QApplication::setOverrideCursor(Qt::WaitCursor);
    QRectF extents = gscene->itemsBoundingRect();
    if (extents.isNull()) {
        extents.setWidth(settings.grid_size.x);
        extents.setHeight(settings.grid_size.y);
        extents.moveCenter(QPointF(0,0));
    }
    fitInView(extents, Qt::KeepAspectRatio);
    QApplication::restoreOverrideCursor();
}

void View::panRealTime()
{
    settings.panningRealTimeActive = 1;
}

void View::panPoint()
{
    settings.panningPointActive = 1;
}

void View::panLeft()
{
    horizontalScrollBar()->setValue(horizontalScrollBar()->value() + panDistance);
    updateMouseCoords(viewMousePoint.x(), viewMousePoint.y());
    gscene->update();
}

void View::panRight()
{
    horizontalScrollBar()->setValue(horizontalScrollBar()->value() - panDistance);
    updateMouseCoords(viewMousePoint.x(), viewMousePoint.y());
    gscene->update();
}

void View::panUp()
{
    verticalScrollBar()->setValue(verticalScrollBar()->value() + panDistance);
    updateMouseCoords(viewMousePoint.x(), viewMousePoint.y());
    gscene->update();
}

void View::panDown()
{
    verticalScrollBar()->setValue(verticalScrollBar()->value() - panDistance);
    updateMouseCoords(viewMousePoint.x(), viewMousePoint.y());
    gscene->update();
}

void View::selectAll()
{
    QPainterPath allPath;
    allPath.addRect(gscene->sceneRect());
    gscene->setSelectionArea(allPath, Qt::ReplaceSelection, Qt::IntersectsItemShape, this->transform());
}

void View::selectionChanged()
{
    if(mainWin->dockPropEdit->isVisible())
    {
        mainWin->dockPropEdit->setSelectedItems(gscene->selectedItems());
    }
}

void View::mouseDoubleClickEvent(QMouseEvent* event)
{
    if(event->button() == Qt::LeftButton)
    {
        QGraphicsItem* item = gscene->itemAt(mapToScene(event->pos()), QTransform());
        if(item)
        {
            mainWin->dockPropEdit->show();
        }
    }
}

void View::mousePressEvent(QMouseEvent* event)
{
    updateMouseCoords(event->x(), event->y());
    if(event->button() == Qt::LeftButton)
    {
        QPainterPath path;
        QList<QGraphicsItem*> pickList = gscene->items(QRectF(mapToScene(viewMousePoint.x()-settings.pickBoxSize, viewMousePoint.y()-settings.pickBoxSize),
                                                              mapToScene(viewMousePoint.x()+settings.pickBoxSize, viewMousePoint.y()+settings.pickBoxSize)));

        int itemsInPickBox = pickList.size();
        if(itemsInPickBox && !settings.selectingActive && !settings.grippingActive)
        {
            int itemsAlreadySelected = pickList.at(0)->isSelected();
            if (!itemsAlreadySelected) {
                pickList.at(0)->setSelected(1);
            }
            else {
                int foundGrip = 0;
                BaseObject* base = static_cast<BaseObject*>(pickList.at(0)); /*TODO: Allow multiple objects to be gripped at once*/
                if(!base) return;

                QPoint qsnapOffset(settings.qsnap_locator_size, settings.qsnap_locator_size);
                QPointF gripPoint = base->mouseSnapPoint(to_qpointf(sceneMousePoint));
                QPoint p1 = mapFromScene(gripPoint) - qsnapOffset;
                QPoint q1 = mapFromScene(gripPoint) + qsnapOffset;
                QRectF gripRect = QRectF(mapToScene(p1), mapToScene(q1));
                QRectF pickRect = QRectF(mapToScene(viewMousePoint.x()-settings.pickBoxSize, viewMousePoint.y()-settings.pickBoxSize),
                                        mapToScene(viewMousePoint.x()+settings.pickBoxSize, viewMousePoint.y()+settings.pickBoxSize));
                if(gripRect.intersects(pickRect))
                    foundGrip = 1;

                /*If the pick point is within the item's grip box, start gripping*/
                if(foundGrip)
                {
                    startGripping(base);
                }
                else /*start moving*/
                {
                    settings.movingActive = 1;
                    pressPoint = event->pos();
                    scenePressPoint = mapToScene(pressPoint);
                }
            }
        }
        else if (settings.grippingActive) {
            stopGripping(1);
        }
        else if (!settings.selectingActive) {
            settings.selectingActive = 1;
            pressPoint = event->pos();
            scenePressPoint = mapToScene(pressPoint);

            if(!selectBox)
                selectBox = new SelectBox(QRubberBand::Rectangle, this);
            selectBox->setGeometry(QRect(pressPoint, pressPoint));
            selectBox->show();
        }
        else
        {
            settings.selectingActive = 0;
            selectBox->hide();
            releasePoint = event->pos();
            sceneReleasePoint = mapToScene(releasePoint);

            /*Start SelectBox Code*/
            path.addPolygon(mapToScene(selectBox->geometry()));
            if(sceneReleasePoint.x() > scenePressPoint.x())
            {
                if (settings.selection_mode_pickadd) {
                    if(mainWin->isShiftPressed())
                    {
                        QList<QGraphicsItem*> itemList = gscene->items(path, Qt::ContainsItemShape);
                        foreach(QGraphicsItem* item, itemList)
                            item->setSelected(0);
                    }
                    else
                    {
                        QList<QGraphicsItem*> itemList = gscene->items(path, Qt::ContainsItemShape);
                        foreach(QGraphicsItem* item, itemList)
                            item->setSelected(1);
                    }
                }
                else {
                    if (mainWin->isShiftPressed()) {
                        QList<QGraphicsItem*> itemList = gscene->items(path, Qt::ContainsItemShape);
                        if(!itemList.size())
                            clearSelection();
                        else {
                            foreach(QGraphicsItem* item, itemList)
                                item->setSelected(!item->isSelected()); /*Toggle selected*/
                        }
                    }
                    else {
                        clearSelection();
                        QList<QGraphicsItem*> itemList = gscene->items(path, Qt::ContainsItemShape);
                        foreach(QGraphicsItem* item, itemList)
                            item->setSelected(1);
                    }
                }
            }
            else {
                if (settings.selection_mode_pickadd) {
                    if(mainWin->isShiftPressed()) {
                        QList<QGraphicsItem*> itemList = gscene->items(path, Qt::IntersectsItemShape);
                        foreach(QGraphicsItem* item, itemList)
                            item->setSelected(0);
                    }
                    else {
                        QList<QGraphicsItem*> itemList = gscene->items(path, Qt::IntersectsItemShape);
                        foreach(QGraphicsItem* item, itemList)
                            item->setSelected(1);
                    }
                }
                else {
                    if (mainWin->isShiftPressed()) {
                        QList<QGraphicsItem*> itemList = gscene->items(path, Qt::IntersectsItemShape);
                        if (!itemList.size()) {
                            clearSelection();
                        }
                        else {
                            foreach(QGraphicsItem* item, itemList)
                                item->setSelected(!item->isSelected()); /*Toggle selected*/
                        }
                    }
                    else
                    {
                        clearSelection();
                        QList<QGraphicsItem*> itemList = gscene->items(path, Qt::IntersectsItemShape);
                        foreach(QGraphicsItem* item, itemList)
                            item->setSelected(1);
                    }
                }
            }
            /*End SelectBox Code*/
        }

        if (settings.pastingActive) {
            QList<QGraphicsItem*> itemList = pasteObjectItemGroup->childItems();
            gscene->destroyItemGroup(pasteObjectItemGroup);
            foreach(QGraphicsItem* item, itemList) {
                gscene->removeItem(item); /*Prevent Qt Runtime Warning, QGraphicsScene::addItem: item has already been added to this scene*/
            }

            foreach(QGraphicsItem* item, itemList) {
                BaseObject* base = static_cast<BaseObject*>(item);
                if (base) {
                }
            }

            settings.pastingActive = 0;
            settings.selectingActive = 0;
        }
        if (settings.zoomWindowActive) {
            fitInView(path.boundingRect(), Qt::KeepAspectRatio);
            clearSelection();
        }
    }
    if (event->button() == Qt::MiddleButton) {
        panStart(event->pos());
        /*The Undo command will record the spot where the pan started.*/
        event->accept();
    }
    gscene->update();
}

void View::panStart(const QPoint& point)
{
    recalculateLimits();

    alignScenePointWithViewPoint(mapToScene(point), point);

    settings.panningActive = 1;
    panStartX = point.x();
    panStartY = point.y();
}

void View::recalculateLimits()
{
    /*NOTE: Increase the sceneRect limits if the point we want to go to lies outside of sceneRect's limits*/
    /*      If the sceneRect limits aren't increased, you cannot pan past its limits*/
    QRectF  viewRect(mapToScene(rect().topLeft()), mapToScene(rect().bottomRight()));
    QRectF  sceneRect(gscene->sceneRect());
    QRectF  newRect = viewRect.adjusted(-viewRect.width(), -viewRect.height(), viewRect.width(), viewRect.height());
    if (!sceneRect.contains(newRect.topLeft()) || !sceneRect.contains(newRect.bottomRight())) {
        gscene->setSceneRect(sceneRect.adjusted(-viewRect.width(),
                                                -viewRect.height(),
                                                viewRect.width(),
                                                viewRect.height()));
    }
}

void View::centerAt(const QPointF& centerPoint)
{
    /*centerOn also updates the scrollbars, which shifts things out of wack o_O*/
    centerOn(centerPoint);
    /*Reshift to the new center*/
    QPointF offset = centerPoint - center();
    QPointF newCenter = centerPoint + offset;
    centerOn(newCenter);
}

void View::alignScenePointWithViewPoint(const QPointF& scenePoint, const QPoint& viewPoint)
{
    QPointF viewCenter = center();
    QPointF pointBefore = scenePoint;
    /*centerOn also updates the scrollbars, which shifts things out of wack o_O*/
    centerOn(viewCenter);
    /*Reshift to the new center so the scene and view points align*/
    QPointF pointAfter = mapToScene(viewPoint);
    QPointF offset = pointBefore - pointAfter;
    QPointF newCenter = viewCenter + offset;
    centerOn(newCenter);
}

void View::mouseMoveEvent(QMouseEvent* event)
{
    QPoint mouse = QCursor::pos();
    updateMouseCoords(mouse.x(), mouse.y());
    movePoint = event->pos();
    sceneMovePoint = mapToScene(movePoint);

    if (settings.previewActive) {
        if (previewMode == PREVIEW_MODE_MOVE) {
            previewObjectItemGroup->setPos(to_qpointf(sceneMousePoint) - previewPoint);
        }
        else if (previewMode == PREVIEW_MODE_ROTATE) {
            EmbVector rot, p;
            float x = previewPoint.x();
            float y = previewPoint.y();
            float mouseAngle = QLineF(x, y, sceneMousePoint.x, sceneMousePoint.y).angle();

            float rad = radians(previewData-mouseAngle);
            p.x = -x;
            p.y = -y;
            rot = rotate_vector(p, rad);
            rot.x += x;
            rot.y += y;

            previewObjectItemGroup->setPos(rot.x, rot.y);
            previewObjectItemGroup->setRotation(previewData-mouseAngle);
        }
        else if (previewMode == PREVIEW_MODE_SCALE) {
            float x = previewPoint.x();
            float y = previewPoint.y();
            float scaleFactor = previewData;

            float factor = QLineF(x, y, sceneMousePoint.x, sceneMousePoint.y).length()/scaleFactor;

            previewObjectItemGroup->setScale(1);
            previewObjectItemGroup->setPos(0,0);

            if(scaleFactor <= 0.0) {
                QMessageBox::critical(this, QObject::tr("ScaleFactor Error"),
                                    QObject::tr("Hi there. If you are not a developer, report this as a bug. "
  "If you are a developer, your code needs examined, and possibly your head too."));
            }
            else {
                /*Calculate the offset*/
                float oldX = 0;
                float oldY = 0;
                QLineF scaleLine(x, y, oldX, oldY);
                scaleLine.setLength(scaleLine.length()*factor);
                float newX = scaleLine.x2();
                float newY = scaleLine.y2();

                float dx = newX - oldX;
                float dy = newY - oldY;

                previewObjectItemGroup->setScale(previewObjectItemGroup->scale()*factor);
                previewObjectItemGroup->moveBy(dx, dy);
            }
        }
    }
    if (settings.pastingActive) {
        EmbVector v;
        embVector_subtract(sceneMousePoint, pasteDelta, &v);
        pasteObjectItemGroup->setPos(to_qpointf(v));
    }
    if (settings.movingActive) {
        /*Ensure that the preview is only shown if the mouse has moved.*/
        if (!settings.previewActive) {
            previewOn(PREVIEW_CLONE_SELECTED, PREVIEW_MODE_MOVE, scenePressPoint.x(), scenePressPoint.y(), 0);
        }
    }
    if (settings.selectingActive) {
        if (sceneMovePoint.x() >= scenePressPoint.x()) {
            selectBox->setDirection(1);
        }
        else { selectBox->setDirection(0); }
        selectBox->setGeometry(QRect(mapFromScene(scenePressPoint), event->pos()).normalized());
        event->accept();
    }
    if (settings.panningActive) {
        horizontalScrollBar()->setValue(horizontalScrollBar()->value() - (event->x() - panStartX));
        verticalScrollBar()->setValue(verticalScrollBar()->value() - (event->y() - panStartY));
        panStartX = event->x();
        panStartY = event->y();
        event->accept();
    }
    gscene->update();
}

void View::mouseReleaseEvent(QMouseEvent* event)
{
    updateMouseCoords(event->x(), event->y());
    if (event->button() == Qt::LeftButton) {
        if (settings.movingActive) {
            previewOff();
            float dx = sceneMousePoint.x-scenePressPoint.x();
            float dy = sceneMousePoint.y-scenePressPoint.y();
            /*Ensure that moving only happens if the mouse has moved.*/
            if(dx || dy) moveSelected(dx, dy);
            settings.movingActive = 0;
        }
        event->accept();
    }
    if (event->button() == Qt::MiddleButton) {
        settings.panningActive = 0;
        /*The Undo command will record the spot where the pan completed.*/
        event->accept();
    }
    if (event->button() == Qt::XButton1) {
        debug_message("XButton1");
        main_undo(); /* TODO: Make this customizable */
        event->accept();
    }
    if (event->button() == Qt::XButton2) {
        debug_message("XButton2");
        main_redo(); /* TODO: Make this customizable */
        event->accept();
    }
    gscene->update();
}

int View::allowZoomIn()
{
    QPointF origin = mapToScene(0,0);
    QPointF corner = mapToScene(width(), height());
    float maxWidth = corner.x() - origin.x();
    float maxHeight = corner.y() - origin.y();

    float zoomInLimit = 0.0000000001;
    if(qMin(maxWidth, maxHeight) < zoomInLimit)
    {
        debug_message("ZoomIn limit reached. (limit=%.10f)", zoomInLimit);
        return 0;
    }

    return 1;
}

int View::allowZoomOut()
{
    QPointF origin = mapToScene(0,0);
    QPointF corner = mapToScene(width(), height());
    float maxWidth = corner.x() - origin.x();
    float maxHeight = corner.y() - origin.y();

    float zoomOutLimit = 10000000000000.0;
    if (embMaxDouble(maxWidth, maxHeight) > zoomOutLimit) {
        debug_message("ZoomOut limit reached. (limit=%.1f)", zoomOutLimit);
        return 0;
    }

    return 1;
}

void View::wheelEvent(QWheelEvent* event)
{
    int zoomDir = event->pixelDelta().y(); /* TODO: double check this*/
    QPointF mousePoint = event->globalPos(); /* TODO: this is causing weird versioning errors, this appears to be supported on Qt5.12. */

    updateMouseCoords(mousePoint.x(), mousePoint.y());
    if (zoomDir > 0) {
    }
    else {
    }
}

void View::zoomToPoint(const QPoint& mousePoint, int zoomDir)
{
    QPointF pointBeforeScale(mapToScene(mousePoint));

    /*Do The zoom*/
    float s;
    if(zoomDir > 0) {
        if(!allowZoomIn()) { return; }
        s = settings.display_zoomscale_in;
    }
    else {
        if(!allowZoomOut()) { return; }
        s = settings.display_zoomscale_out;
    }

    scale(s, s);
    alignScenePointWithViewPoint(pointBeforeScale, mousePoint);
    recalculateLimits();
    alignScenePointWithViewPoint(pointBeforeScale, mousePoint);

    updateMouseCoords(mousePoint.x(), mousePoint.y());
    if (settings.pastingActive) {
        EmbVector v;
        embVector_subtract(sceneMousePoint, pasteDelta, &v);
        pasteObjectItemGroup->setPos(to_qpointf(v));
    }
    if (settings.selectingActive) {
        selectBox->setGeometry(QRect(mapFromScene(scenePressPoint), mousePoint).normalized());
    }
    gscene->update();
}

void View::contextMenuEvent(QContextMenuEvent* event)
{
    QString iconTheme = settings.general_icon_theme;

    QMenu menu;
    QList<QGraphicsItem*> itemList = gscene->selectedItems();
    int selectionEmpty = itemList.isEmpty();

    for (int i = 0; i < itemList.size(); i++) {
        if (itemList.at(i)->data(OBJ_TYPE) != OBJ_TYPE_NULL) {
            selectionEmpty = 0;
            break;
        }
    }

    if (settings.pastingActive) {
        return;
    }
    if (settings.zoomWindowActive) {
        QAction* cancelZoomWinAction = new QAction("&Cancel (ZoomWindow)", this);
        cancelZoomWinAction->setStatusTip("Cancels the ZoomWindow Command.");
        connect(cancelZoomWinAction, SIGNAL(triggered()), this, SLOT(escapePressed()));
        menu.addAction(cancelZoomWinAction);
    }

    menu.addSeparator();
    menu.addAction(mainWin->actionHash.value(ACTION_cut));
    menu.addAction(mainWin->actionHash.value(ACTION_copy));
    menu.addAction(mainWin->actionHash.value(ACTION_paste));
    menu.addSeparator();

    if (!selectionEmpty) {
        QAction* deleteAction = new QAction(loadIcon(icon_erase), "D&elete", this);
        deleteAction->setStatusTip("Removes objects from a drawing.");
        connect(deleteAction, SIGNAL(triggered()), this, SLOT(deleteSelected()));
        menu.addAction(deleteAction);

        QAction* moveAction = new QAction(loadIcon(icon_move), "&Move", this);
        moveAction->setStatusTip("Displaces objects a specified distance in a specified direction.");
        connect(moveAction, SIGNAL(triggered()), this, SLOT(moveAction()));
        menu.addAction(moveAction);

        QAction* scaleAction = new QAction(loadIcon(icon_scale), "Sca&le", this);
        scaleAction->setStatusTip("Enlarges or reduces objects proportionally in the X, Y, and Z directions.");
        connect(scaleAction, SIGNAL(triggered()), this, SLOT(scaleAction()));
        menu.addAction(scaleAction);

        QAction* rotateAction = new QAction(loadIcon(icon_rotate), "R&otate", this);
        rotateAction->setStatusTip("Rotates objects about a base point.");
        connect(rotateAction, SIGNAL(triggered()), this, SLOT(rotateAction()));
        menu.addAction(rotateAction);

        menu.addSeparator();

        QAction* clearAction = new QAction("Cle&ar Selection", this);
        clearAction->setStatusTip("Removes all objects from the selection set.");
        connect(clearAction, SIGNAL(triggered()), this, SLOT(clearSelection()));
        menu.addAction(clearAction);
    }

    menu.exec(event->globalPos());
}

void View::deletePressed()
{
    debug_message("View deletePressed()");
    if (settings.pastingActive) {
        gscene->removeItem(pasteObjectItemGroup);
        delete pasteObjectItemGroup;
    }
    settings.pastingActive = 0;
    settings.zoomWindowActive = 0;
    settings.selectingActive = 0;
    selectBox->hide();
    stopGripping(0);
    deleteSelected();
}

void View::escapePressed()
{
    debug_message("View escapePressed()");
    if (settings.pastingActive) {
        gscene->removeItem(pasteObjectItemGroup);
        delete pasteObjectItemGroup;
    }
    settings.pastingActive = 0;
    settings.zoomWindowActive = 0;
    settings.selectingActive = 0;
    selectBox->hide();
    if(settings.grippingActive) stopGripping(0);
    else clearSelection();
}

void View::startGripping(BaseObject* obj)
{
    if(!obj) return;
    settings.grippingActive = 1;
    gripBaseObj = obj;
    sceneGripPoint = gripBaseObj->mouseSnapPoint(to_qpointf(sceneMousePoint));
    gripBaseObj->setObjectRubberPoint("GRIP_POINT", sceneGripPoint);
    gripBaseObj->setObjectRubberMode(OBJ_RUBBER_GRIP);
}

void View::stopGripping(int accept)
{
    settings.grippingActive = 0;
    if(gripBaseObj)
    {
        gripBaseObj->vulcanize();
        if(accept)
        {
            selectionChanged(); /*Update the Property Editor*/
        }
        gripBaseObj = 0;
    }
    /*Move the sceneGripPoint to a place where it will never be hot*/
    sceneGripPoint = sceneRect().topLeft();
}

void View::clearSelection()
{
    gscene->clearSelection();
}

void View::deleteSelected()
{
    QList<QGraphicsItem*> itemList = gscene->selectedItems();
    int numSelected = itemList.size();
    
    for(int i = 0; i < itemList.size(); i++)
    {
        if(itemList.at(i)->data(OBJ_TYPE) != OBJ_TYPE_NULL)
        {
            BaseObject* base = static_cast<BaseObject*>(itemList.at(i));
            if(base)
            {
            }
        }
    }
}

void View::cut()
{
    if(gscene->selectedItems().isEmpty())
    {
        QMessageBox::information(this, tr("Cut Preselect"), tr("Preselect objects before invoking the cut command."));
        return; /*TODO: Prompt to select objects if nothing is preselected*/
    }

    copySelected();
    deleteSelected();
}

void View::copy()
{
    if(gscene->selectedItems().isEmpty())
    {
        QMessageBox::information(this, tr("Copy Preselect"), tr("Preselect objects before invoking the copy command."));
        return; /* TODO: Prompt to select objects if nothing is preselected */
    }

    copySelected();
    clearSelection();
}

void View::copySelected()
{
    QList<QGraphicsItem*> selectedList = gscene->selectedItems();

    /* Prevent memory leaks by deleting any unpasted instances */
    qDeleteAll(mainWin->cutCopyObjectList.begin(), mainWin->cutCopyObjectList.end());
    mainWin->cutCopyObjectList.clear();

    /*
     * Create new objects but do not add them to the scene just yet.
     * By creating them now, ensures that pasting will still work
     * if the original objects are deleted before the paste occurs.
     */
    mainWin->cutCopyObjectList = createObjectList(selectedList);
}

void View::paste()
{
    if (settings.pastingActive) {
        gscene->removeItem(pasteObjectItemGroup);
        delete pasteObjectItemGroup;
    }

    pasteObjectItemGroup = gscene->createItemGroup(mainWin->cutCopyObjectList);
    pasteDelta = to_emb_vector(pasteObjectItemGroup->boundingRect().bottomLeft());
    EmbVector v;
    embVector_subtract(sceneMousePoint, pasteDelta, &v);
    pasteObjectItemGroup->setPos(to_qpointf(v));
    settings.pastingActive = 1;

    /* Re-create the list in case of multiple pastes */
    mainWin->cutCopyObjectList = createObjectList(mainWin->cutCopyObjectList);
}

QList<QGraphicsItem*> View::createObjectList(QList<QGraphicsItem*> list)
{
    QList<QGraphicsItem*> copyList;

    for (int i = 0; i < list.size(); i++) {
        QGraphicsItem* item = list.at(i);
        if (!item)
            continue;

        int objType = item->data(OBJ_TYPE).toInt();

        if (objType == OBJ_TYPE_ARC) {
            ArcObject* arcObj = static_cast<ArcObject*>(item);
            if(arcObj)
            {
                ArcObject* copyArcObj = new ArcObject(arcObj);
                copyList.append(copyArcObj);
            }
        }
        else if(objType == OBJ_TYPE_BLOCK)
        {
            /*TODO: cut/copy blocks*/
        }
        else if(objType == OBJ_TYPE_CIRCLE)
        {
            CircleObject* circObj = static_cast<CircleObject*>(item);
            if(circObj)
            {
                CircleObject* copyCircObj = new CircleObject(circObj);
                copyList.append(copyCircObj);
            }
        }
        else if(objType == OBJ_TYPE_DIMALIGNED)
        {
            /*TODO: cut/copy aligned dimensions*/
        }
        else if(objType == OBJ_TYPE_DIMANGULAR)
        {
            /*TODO: cut/copy angular dimensions*/
        }
        else if(objType == OBJ_TYPE_DIMARCLENGTH)
        {
            /*TODO: cut/copy arclength dimensions*/
        }
        else if(objType == OBJ_TYPE_DIMDIAMETER)
        {
            /*TODO: cut/copy diameter dimensions*/
        }
        else if(objType == OBJ_TYPE_DIMLEADER)
        {
            DimLeaderObject* dimLeaderObj = static_cast<DimLeaderObject*>(item);
            if(dimLeaderObj)
            {
                DimLeaderObject* copyDimLeaderObj = new DimLeaderObject(dimLeaderObj);
                copyList.append(copyDimLeaderObj);
            }
        }
        else if(objType == OBJ_TYPE_DIMLINEAR)
        {
            /*TODO: cut/copy linear dimensions*/
        }
        else if(objType == OBJ_TYPE_DIMORDINATE)
        {
            /*TODO: cut/copy ordinate dimensions*/
        }
        else if(objType == OBJ_TYPE_DIMRADIUS)
        {
            /*TODO: cut/copy radius dimensions*/
        }
        else if(objType == OBJ_TYPE_ELLIPSE)
        {
            EllipseObject* elipObj = static_cast<EllipseObject*>(item);
            if(elipObj)
            {
                EllipseObject* copyElipObj = new EllipseObject(elipObj);
                copyList.append(copyElipObj);
            }
        }
        else if(objType == OBJ_TYPE_ELLIPSEARC)
        {
            /*TODO: cut/copy elliptical arcs*/
        }
        else if(objType == OBJ_TYPE_IMAGE)
        {
            /*TODO: cut/copy images*/
        }
        else if(objType == OBJ_TYPE_INFINITELINE)
        {
            /*TODO: cut/copy infinite lines*/
        }
        else if(objType == OBJ_TYPE_LINE)
        {
            LineObject* lineObj = static_cast<LineObject*>(item);
            if(lineObj)
            {
                LineObject* copyLineObj = new LineObject(lineObj);
                copyList.append(copyLineObj);
            }
        }
        else if(objType == OBJ_TYPE_PATH)
        {
            PathObject* pathObj = static_cast<PathObject*>(item);
            if(pathObj)
            {
                PathObject* copyPathObj = new PathObject(pathObj);
                copyList.append(copyPathObj);
            }
        }
        else if(objType == OBJ_TYPE_POINT)
        {
            PointObject* pointObj = static_cast<PointObject*>(item);
            if(pointObj)
            {
                PointObject* copyPointObj = new PointObject(pointObj);
                copyList.append(copyPointObj);
            }
        }
        else if(objType == OBJ_TYPE_POLYGON)
        {
            PolygonObject* pgonObj = static_cast<PolygonObject*>(item);
            if(pgonObj)
            {
                PolygonObject* copyPgonObj = new PolygonObject(pgonObj);
                copyList.append(copyPgonObj);
            }
        }
        else if(objType == OBJ_TYPE_POLYLINE)
        {
            PolylineObject* plineObj = static_cast<PolylineObject*>(item);
            if(plineObj)
            {
                PolylineObject* copyPlineObj = new PolylineObject(plineObj);
                copyList.append(copyPlineObj);
            }
        }
        else if(objType == OBJ_TYPE_RAY)
        {
            /*TODO: cut/copy rays*/
        }
        else if(objType == OBJ_TYPE_RECTANGLE)
        {
            RectObject* rectObj = static_cast<RectObject*>(item);
            if(rectObj)
            {
                RectObject* copyRectObj = new RectObject(rectObj);
                copyList.append(copyRectObj);
            }
        }
        else if(objType == OBJ_TYPE_TEXTSINGLE)
        {
            TextSingleObject* textObj = static_cast<TextSingleObject*>(item);
            if(textObj)
            {
                TextSingleObject* copyTextObj = new TextSingleObject(textObj);
                copyList.append(copyTextObj);
            }
        }
    }

    return copyList;
}

void View::repeatAction()
{
}

void View::moveAction()
{
}

void View::moveSelected(float dx, float dy)
{
    QList<QGraphicsItem*> itemList = gscene->selectedItems();
    int numSelected = itemList.size();
    
    foreach(QGraphicsItem* item, itemList)
    {
        BaseObject* base = static_cast<BaseObject*>(item);
        if(base)
        {
        }
    }

    /*Always clear the selection after a move*/
    gscene->clearSelection();
}

void View::rotateAction()
{
}

void View::rotateSelected(float x, float y, float rot)
{
    QList<QGraphicsItem*> itemList = gscene->selectedItems();
    int numSelected = itemList.size();
    foreach(QGraphicsItem* item, itemList)
    {
        BaseObject* base = static_cast<BaseObject*>(item);
        if(base)
        {
        }
    }

    /*Always clear the selection after a rotate*/
    gscene->clearSelection();
}

void View::mirrorSelected(float x1, float y1, float x2, float y2)
{
    QList<QGraphicsItem*> itemList = gscene->selectedItems();
    int numSelected = itemList.size();
    foreach(QGraphicsItem* item, itemList)
    {
        BaseObject* base = static_cast<BaseObject*>(item);
        if(base)
        {
        }
    }

    /*Always clear the selection after a mirror*/
    gscene->clearSelection();
}

void View::scaleAction()
{
}

void View::scaleSelected(float x, float y, float factor)
{
    QList<QGraphicsItem*> itemList = gscene->selectedItems();
    int numSelected = itemList.size();
    foreach(QGraphicsItem* item, itemList)
    {
        BaseObject* base = static_cast<BaseObject*>(item);
        if(base)
        {
        }
    }

    /*Always clear the selection after a scale*/
    gscene->clearSelection();
}

int View::numSelected()
{
    return gscene->selectedItems().size();
}

void View::showScrollBars(int val)
{
    if(val)
    {
        setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOn);
        setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOn);
    }
    else
    {
        setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    }
}

void View::setCrossHairColor(unsigned int color)
{
    crosshairColor = color;
    gscene->setProperty("VIEW_COLOR_CROSSHAIR", color);
    if(gscene) gscene->update();
}

void View::setBackgroundColor(unsigned int color)
{
    setBackgroundBrush(QColor(color));
    gscene->setProperty("VIEW_COLOR_BACKGROUND", color);
    if(gscene) gscene->update();
}

void View::setSelectBoxColors(unsigned int colorL, unsigned int fillL, unsigned int colorR, unsigned int fillR, int alpha)
{
    selectBox->setColors(QColor(colorL), QColor(fillL), QColor(colorR), QColor(fillR), alpha);
}

Settings_Dialog::Settings_Dialog(MainWindow* mw, const QString& showTab, QWidget* parent) : QDialog(parent)
{
    int i;
    mainWin = mw;
    setMinimumSize(750,550);

    tabWidget = new QTabWidget(this);

    /*TODO: Add icons to tabs*/
    tabWidget->addTab(createTabGeneral(), tr("General"));
    tabWidget->addTab(createTabFilesPaths(), tr("Files/Paths"));
    tabWidget->addTab(createTabDisplay(), tr("Display"));
    tabWidget->addTab(createTabOpenSave(), tr("Open/Save"));
    tabWidget->addTab(createTabPrinting(), tr("Printing"));
    tabWidget->addTab(createTabSnap(), tr("Snap"));
    tabWidget->addTab(createTabGridRuler(), tr("Grid/Ruler"));
    tabWidget->addTab(createTabOrthoPolar(), tr("Ortho/Polar"));
    tabWidget->addTab(createTabQuickSnap(), tr("QuickSnap"));
    tabWidget->addTab(createTabQuickTrack(), tr("QuickTrack"));
    tabWidget->addTab(createTabLineWeight(), tr("LineWeight"));
    tabWidget->addTab(createTabSelection(), tr("Selection"));

    for (i=0; i<12; i++) {
        if (showTab == settings_tab_label[i]) {
            tabWidget->setCurrentIndex(i);
        }
    }

    buttonBox = new QDialogButtonBox(QDialogButtonBox::Ok | QDialogButtonBox::Cancel);

    connect(buttonBox, SIGNAL(accepted()), this, SLOT(acceptChanges()));
    connect(buttonBox, SIGNAL(rejected()), this, SLOT(rejectChanges()));

    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(this);
    vboxLayoutMain->addWidget(tabWidget);
    vboxLayoutMain->addWidget(buttonBox);
    setLayout(vboxLayoutMain);

    setWindowTitle(tr("Settings"));

    QApplication::setOverrideCursor(Qt::ArrowCursor);
}

Settings_Dialog::~Settings_Dialog()
{
    QApplication::restoreOverrideCursor();
}

QWidget* Settings_Dialog::createTabGeneral()
{
    QWidget* widget = new QWidget(this);

    /*Language*/
    QGroupBox* groupBoxLanguage = new QGroupBox(tr("Language"), widget);

    QLabel* labelLanguage = new QLabel(tr("Language (Requires Restart)"), groupBoxLanguage);
    QComboBox* comboBoxLanguage = new QComboBox(groupBoxLanguage);
    to_lower(dialog.general_language, settings.general_language);
    comboBoxLanguage->addItem("Default");
    comboBoxLanguage->addItem("System");
    comboBoxLanguage->insertSeparator(2);
    QDir trDir(qApp->applicationDirPath());
    trDir.cd("translations");
    foreach(QString dirName, trDir.entryList(QDir::Dirs | QDir::NoDotAndDotDot))
    {
        dirName[0] = dirName[0].toUpper();
        comboBoxLanguage->addItem(dirName);
    }
    QString current = dialog.general_language;
    current[0] = current[0].toUpper();
    comboBoxLanguage->setCurrentIndex(comboBoxLanguage->findText(current));
    connect(comboBoxLanguage, SIGNAL(currentIndexChanged(const QString&)), this, SLOT(comboBoxLanguageCurrentIndexChanged(const QString&)));

    QVBoxLayout* vboxLayoutLanguage = new QVBoxLayout(groupBoxLanguage);
    vboxLayoutLanguage->addWidget(labelLanguage);
    vboxLayoutLanguage->addWidget(comboBoxLanguage);
    groupBoxLanguage->setLayout(vboxLayoutLanguage);

    /*Icons*/
    QGroupBox* groupBoxIcon = new QGroupBox(tr("Icons"), widget);

    QLabel* labelIconTheme = new QLabel(tr("Icon Theme"), groupBoxIcon);
    QComboBox* comboBoxIconTheme = new QComboBox(groupBoxIcon);
    QDir dir(qApp->applicationDirPath());
    dir.cd("icons");
    strcpy(dialog.general_icon_theme, settings.general_icon_theme);
    foreach(QString dirName, dir.entryList(QDir::Dirs | QDir::NoDotAndDotDot))
    {
        comboBoxIconTheme->addItem(loadIcon(icon_theme), dirName);
    }
    comboBoxIconTheme->setCurrentIndex(comboBoxIconTheme->findText(dialog.general_icon_theme));
    connect(comboBoxIconTheme, SIGNAL(currentIndexChanged(const QString&)), this, SLOT(comboBoxIconThemeCurrentIndexChanged(const QString&)));

    QLabel* labelIconSize = new QLabel(tr("Icon Size"), groupBoxIcon);
    QComboBox* comboBoxIconSize = new QComboBox(groupBoxIcon);
    comboBoxIconSize->addItem(loadIcon(icon_icon16), "Very Small", 16);
    comboBoxIconSize->addItem(loadIcon(icon_icon24), "Small", 24);
    comboBoxIconSize->addItem(loadIcon(icon_icon32), "Medium", 32);
    comboBoxIconSize->addItem(loadIcon(icon_icon48), "Large", 48);
    comboBoxIconSize->addItem(loadIcon(icon_icon64), "Very Large", 64);
    comboBoxIconSize->addItem(loadIcon(icon_icon128), "I'm Blind", 128);
    dialog.general_icon_size = settings.general_icon_size;
    comboBoxIconSize->setCurrentIndex(comboBoxIconSize->findData(dialog.general_icon_size));
    connect(comboBoxIconSize, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxIconSizeCurrentIndexChanged(int)));

    QVBoxLayout* vboxLayoutIcon = new QVBoxLayout(groupBoxIcon);
    vboxLayoutIcon->addWidget(labelIconTheme);
    vboxLayoutIcon->addWidget(comboBoxIconTheme);
    vboxLayoutIcon->addWidget(labelIconSize);
    vboxLayoutIcon->addWidget(comboBoxIconSize);
    groupBoxIcon->setLayout(vboxLayoutIcon);

    /*Mdi Background*/
    QGroupBox* groupBoxMdiBG = new QGroupBox(tr("Background"), widget);

    QCheckBox* checkBoxMdiBGUseLogo = new QCheckBox(tr("Use Logo"), groupBoxMdiBG);
    dialog.general_mdi_bg_use_logo = settings.general_mdi_bg_use_logo;
    preview.general_mdi_bg_use_logo = dialog.general_mdi_bg_use_logo;
    checkBoxMdiBGUseLogo->setChecked(preview.general_mdi_bg_use_logo);
    connect(checkBoxMdiBGUseLogo, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGeneralMdiBGUseLogoStateChanged(int)));

    QPushButton* buttonMdiBGLogo = new QPushButton(tr("Choose"), groupBoxMdiBG);
    buttonMdiBGLogo->setEnabled(dialog.general_mdi_bg_use_logo);
    strcpy(dialog.general_mdi_bg_logo, settings.general_mdi_bg_logo);
    strcpy(accept_.general_mdi_bg_logo, dialog.general_mdi_bg_logo);
    connect(buttonMdiBGLogo, SIGNAL(clicked()), this, SLOT(chooseGeneralMdiBackgroundLogo()));
    connect(checkBoxMdiBGUseLogo, SIGNAL(toggled(int)), buttonMdiBGLogo, SLOT(setEnabled(int)));

    QCheckBox* checkBoxMdiBGUseTexture = new QCheckBox(tr("Use Texture"), groupBoxMdiBG);
    dialog.general_mdi_bg_use_texture = settings.general_mdi_bg_use_texture;
    preview.general_mdi_bg_use_texture = dialog.general_mdi_bg_use_texture;
    checkBoxMdiBGUseTexture->setChecked(preview.general_mdi_bg_use_texture);
    connect(checkBoxMdiBGUseTexture, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGeneralMdiBGUseTextureStateChanged(int)));

    QPushButton* buttonMdiBGTexture = new QPushButton(tr("Choose"), groupBoxMdiBG);
    buttonMdiBGTexture->setEnabled(dialog.general_mdi_bg_use_texture);
    strcpy(dialog.general_mdi_bg_texture, settings.general_mdi_bg_texture);
    strcpy(accept_.general_mdi_bg_texture, dialog.general_mdi_bg_texture);
    connect(buttonMdiBGTexture, SIGNAL(clicked()), this, SLOT(chooseGeneralMdiBackgroundTexture()));
    connect(checkBoxMdiBGUseTexture, SIGNAL(toggled(int)), buttonMdiBGTexture, SLOT(setEnabled(int)));

    QCheckBox* checkBoxMdiBGUseColor = new QCheckBox(tr("Use Color"), groupBoxMdiBG);
    dialog.general_mdi_bg_use_color = settings.general_mdi_bg_use_color;
    preview.general_mdi_bg_use_color = dialog.general_mdi_bg_use_color;
    checkBoxMdiBGUseColor->setChecked(preview.general_mdi_bg_use_color);
    connect(checkBoxMdiBGUseColor, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGeneralMdiBGUseColorStateChanged(int)));

    QPushButton* buttonMdiBGColor = new QPushButton(tr("Choose"), groupBoxMdiBG);
    buttonMdiBGColor->setEnabled(dialog.general_mdi_bg_use_color);
    dialog.general_mdi_bg_color = settings.general_mdi_bg_color;
    preview.general_mdi_bg_color = dialog.general_mdi_bg_color;
    accept_.general_mdi_bg_color = dialog.general_mdi_bg_color;
    QPixmap mdiBGPix(16,16);
    mdiBGPix.fill(QColor(preview.general_mdi_bg_color));
    buttonMdiBGColor->setIcon(QIcon(mdiBGPix));
    connect(buttonMdiBGColor, SIGNAL(clicked()), this, SLOT(chooseGeneralMdiBackgroundColor()));
    connect(checkBoxMdiBGUseColor, SIGNAL(toggled(int)), buttonMdiBGColor, SLOT(setEnabled(int)));

    QGridLayout* gridLayoutMdiBG = new QGridLayout(widget);
    gridLayoutMdiBG->addWidget(checkBoxMdiBGUseLogo, 0, 0, Qt::AlignLeft);
    gridLayoutMdiBG->addWidget(buttonMdiBGLogo, 0, 1, Qt::AlignRight);
    gridLayoutMdiBG->addWidget(checkBoxMdiBGUseTexture, 1, 0, Qt::AlignLeft);
    gridLayoutMdiBG->addWidget(buttonMdiBGTexture, 1, 1, Qt::AlignRight);
    gridLayoutMdiBG->addWidget(checkBoxMdiBGUseColor, 2, 0, Qt::AlignLeft);
    gridLayoutMdiBG->addWidget(buttonMdiBGColor, 2, 1, Qt::AlignRight);
    groupBoxMdiBG->setLayout(gridLayoutMdiBG);

    /*Tips*/
    QGroupBox* groupBoxTips = new QGroupBox(tr("Tips"), widget);

    QCheckBox* checkBoxTipOfTheDay = new QCheckBox(tr("Show Tip of the Day on startup"), groupBoxTips);
    dialog.general_tip_of_the_day = settings.general_tip_of_the_day;
    checkBoxTipOfTheDay->setChecked(dialog.general_tip_of_the_day);
    connect(checkBoxTipOfTheDay, SIGNAL(stateChanged(int)), this, SLOT(checkBoxTipOfTheDayStateChanged(int)));

    QVBoxLayout* vboxLayoutTips = new QVBoxLayout(groupBoxTips);
    vboxLayoutTips->addWidget(checkBoxTipOfTheDay);
    groupBoxTips->setLayout(vboxLayoutTips);

    /*Help Browser*/
    QGroupBox* groupBoxHelpBrowser = new QGroupBox(tr("Help Browser"), widget);

    QRadioButton* radioButtonSystemHelpBrowser = new QRadioButton(tr("System"), groupBoxHelpBrowser);
    radioButtonSystemHelpBrowser->setChecked(settings.general_system_help_browser);
    QRadioButton* radioButtonCustomHelpBrowser = new QRadioButton(tr("Custom"), groupBoxHelpBrowser);
    radioButtonCustomHelpBrowser->setChecked(!settings.general_system_help_browser);
    radioButtonCustomHelpBrowser->setEnabled(0); /*TODO: finish this*/

    QVBoxLayout* vboxLayoutHelpBrowser = new QVBoxLayout(groupBoxHelpBrowser);
    vboxLayoutHelpBrowser->addWidget(radioButtonSystemHelpBrowser);
    vboxLayoutHelpBrowser->addWidget(radioButtonCustomHelpBrowser);
    groupBoxHelpBrowser->setLayout(vboxLayoutHelpBrowser);

    /*Widget Layout*/
    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(widget);
    vboxLayoutMain->addWidget(groupBoxLanguage);
    vboxLayoutMain->addWidget(groupBoxIcon);
    vboxLayoutMain->addWidget(groupBoxMdiBG);
    vboxLayoutMain->addWidget(groupBoxTips);
    vboxLayoutMain->addWidget(groupBoxHelpBrowser);
    vboxLayoutMain->addStretch(1);
    widget->setLayout(vboxLayoutMain);

    QScrollArea* scrollArea = new QScrollArea(this);
    scrollArea->setWidgetResizable(1);
    scrollArea->setWidget(widget);
    return scrollArea;
}

QWidget* Settings_Dialog::createTabFilesPaths()
{
    QWidget* widget = new QWidget(this);

    QScrollArea* scrollArea = new QScrollArea(this);
    scrollArea->setWidgetResizable(1);
    scrollArea->setWidget(widget);
    return scrollArea;
}

QWidget* Settings_Dialog::createTabDisplay()
{
    QWidget* widget = new QWidget(this);

    /*Rendering*/
    /*TODO: Review OpenGL and Rendering settings for future inclusion*/
    /*
    QGroupBox* groupBoxRender = new QGroupBox(tr("Rendering"), widget);

    QCheckBox* checkBoxUseOpenGL = new QCheckBox(tr("Use OpenGL"), groupBoxRender);
    dialog.display_use_opengl = settings.display_use_open_gl;
    checkBoxUseOpenGL->setChecked(dialog.display_use_opengl);
    connect(checkBoxUseOpenGL, SIGNAL(stateChanged(int)), this, SLOT(checkBoxUseOpenGLStateChanged(int)));

    QCheckBox* checkBoxRenderHintAA = new QCheckBox(tr("Antialias"), groupBoxRender);
    dialog.display_renderhint_aa = settings.display_render_hint_aa;
    checkBoxRenderHintAA->setChecked(dialog.display_renderhint_aa);
    connect(checkBoxRenderHintAA, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRenderHintAAStateChanged(int)));

    QCheckBox* checkBoxRenderHintTextAA = new QCheckBox(tr("Antialias Text"), groupBoxRender);
    dialog.display_renderhint_text_aa = settings.display_render_hint_text_aa;
    checkBoxRenderHintTextAA->setChecked(dialog.display_renderhint_text_aa);
    connect(checkBoxRenderHintTextAA, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRenderHintTextAAStateChanged(int)));

    QCheckBox* checkBoxRenderHintSmoothPix = new QCheckBox(tr("Smooth Pixmap"), groupBoxRender);
    dialog.display_renderhint_smooth_pix = settings.display_render_hint_smooth_pix;
    checkBoxRenderHintSmoothPix->setChecked(dialog.display_renderhint_smooth_pix);
    connect(checkBoxRenderHintSmoothPix, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRenderHintSmoothPixStateChanged(int)));

    QCheckBox* checkBoxRenderHintHighAA = new QCheckBox(tr("High Quality Antialiasing (OpenGL)"), groupBoxRender);
    dialog.display_renderhint_high_aa = settings.display_render_hint_high_aa;
    checkBoxRenderHintHighAA->setChecked(dialog.display_renderhint_high_aa);
    connect(checkBoxRenderHintHighAA, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRenderHintHighAAStateChanged(int)));

    QCheckBox* checkBoxRenderHintNonCosmetic = new QCheckBox(tr("Non Cosmetic"), groupBoxRender);
    dialog.display_renderhint_noncosmetic = settings.display_render_hint_non_cosmetic;
    checkBoxRenderHintNonCosmetic->setChecked(dialog.display_renderhint_noncosmetic);
    connect(checkBoxRenderHintNonCosmetic, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRenderHintNonCosmeticStateChanged(int)));

    QVBoxLayout* vboxLayoutRender = new QVBoxLayout(groupBoxRender);
    vboxLayoutRender->addWidget(checkBoxUseOpenGL);
    vboxLayoutRender->addWidget(checkBoxRenderHintAA);
    vboxLayoutRender->addWidget(checkBoxRenderHintTextAA);
    vboxLayoutRender->addWidget(checkBoxRenderHintSmoothPix);
    vboxLayoutRender->addWidget(checkBoxRenderHintHighAA);
    vboxLayoutRender->addWidget(checkBoxRenderHintNonCosmetic);
    groupBoxRender->setLayout(vboxLayoutRender);
    */

    /*ScrollBars*/
    QGroupBox* groupBoxScrollBars = new QGroupBox(tr("ScrollBars"), widget);

    QCheckBox* checkBoxShowScrollBars = new QCheckBox(tr("Show ScrollBars"), groupBoxScrollBars);
    dialog.display_show_scrollbars = settings.display_show_scrollbars;
    preview.display_show_scrollbars = dialog.display_show_scrollbars;
    checkBoxShowScrollBars->setChecked(preview.display_show_scrollbars);
    connect(checkBoxShowScrollBars, SIGNAL(stateChanged(int)), this, SLOT(checkBoxShowScrollBarsStateChanged(int)));

    QLabel* labelScrollBarWidget = new QLabel(tr("Perform action when clicking corner widget"), groupBoxScrollBars);
    QComboBox* comboBoxScrollBarWidget = new QComboBox(groupBoxScrollBars);
    dialog.display_scrollbar_widget_num = settings.display_scrollbar_widget_num;
    int numActions = mainWin->actionHash.size();
    for(int i = 0; i < numActions; i++)
    {
        QAction* action = mainWin->actionHash.value(i);
        if(action) comboBoxScrollBarWidget->addItem(action->icon(), action->text().replace("&", ""));
    }
    comboBoxScrollBarWidget->setCurrentIndex(dialog.display_scrollbar_widget_num);
    connect(comboBoxScrollBarWidget, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxScrollBarWidgetCurrentIndexChanged(int)));

    QVBoxLayout* vboxLayoutScrollBars = new QVBoxLayout(groupBoxScrollBars);
    vboxLayoutScrollBars->addWidget(checkBoxShowScrollBars);
    vboxLayoutScrollBars->addWidget(labelScrollBarWidget);
    vboxLayoutScrollBars->addWidget(comboBoxScrollBarWidget);
    groupBoxScrollBars->setLayout(vboxLayoutScrollBars);

    /*Colors*/
    QGroupBox* groupBoxColor = new QGroupBox(tr("Colors"), widget);

    QLabel* labelCrossHairColor = new QLabel(tr("Crosshair Color"), groupBoxColor);
    QPushButton* buttonCrossHairColor = new QPushButton(tr("Choose"), groupBoxColor);
    dialog.display_crosshair_color = settings.display_crosshair_color;
    preview.display_crosshair_color = dialog.display_crosshair_color;
    accept_.display_crosshair_color = dialog.display_crosshair_color;
    QPixmap crosshairPix(16,16);
    crosshairPix.fill(QColor(preview.display_crosshair_color));
    buttonCrossHairColor->setIcon(QIcon(crosshairPix));
    connect(buttonCrossHairColor, SIGNAL(clicked()), this, SLOT(chooseDisplayCrossHairColor()));

    QLabel* labelBGColor = new QLabel(tr("Background Color"), groupBoxColor);
    QPushButton* buttonBGColor = new QPushButton(tr("Choose"), groupBoxColor);
    dialog.display_bg_color = settings.display_bg_color;
    preview.display_bg_color = dialog.display_bg_color;
    accept_.display_bg_color = dialog.display_bg_color;
    QPixmap bgPix(16,16);
    bgPix.fill(QColor(preview.display_bg_color));
    buttonBGColor->setIcon(QIcon(bgPix));
    connect(buttonBGColor, SIGNAL(clicked()), this, SLOT(chooseDisplayBackgroundColor()));

    QLabel* labelSelectBoxLeftColor = new QLabel(tr("Selection Box Color (Crossing)"), groupBoxColor);
    QPushButton* buttonSelectBoxLeftColor = new QPushButton(tr("Choose"), groupBoxColor);
    dialog.display_selectbox_left_color = settings.display_selectbox_left_color;
    preview.display_selectbox_left_color = dialog.display_selectbox_left_color;
    accept_.display_selectbox_left_color = dialog.display_selectbox_left_color;
    QPixmap sBoxLCPix(16,16);
    sBoxLCPix.fill(QColor(preview.display_selectbox_left_color));
    buttonSelectBoxLeftColor->setIcon(QIcon(sBoxLCPix));
    connect(buttonSelectBoxLeftColor, SIGNAL(clicked()), this, SLOT(chooseDisplaySelectBoxLeftColor()));

    QLabel* labelSelectBoxLeftFill = new QLabel(tr("Selection Box Fill (Crossing)"), groupBoxColor);
    QPushButton* buttonSelectBoxLeftFill = new QPushButton(tr("Choose"), groupBoxColor);
    dialog.display_selectbox_left_fill = settings.display_selectbox_left_fill;
    preview.display_selectbox_left_fill = dialog.display_selectbox_left_fill;
    accept_.display_selectbox_left_fill = dialog.display_selectbox_left_fill;
    QPixmap sBoxLFPix(16,16);
    sBoxLFPix.fill(QColor(preview.display_selectbox_left_fill));
    buttonSelectBoxLeftFill->setIcon(QIcon(sBoxLFPix));
    connect(buttonSelectBoxLeftFill, SIGNAL(clicked()), this, SLOT(chooseDisplaySelectBoxLeftFill()));

    QLabel* labelSelectBoxRightColor = new QLabel(tr("Selection Box Color (Window)"), groupBoxColor);
    QPushButton* buttonSelectBoxRightColor = new QPushButton(tr("Choose"), groupBoxColor);
    dialog.display_selectbox_right_color = settings.display_selectbox_right_color;
    preview.display_selectbox_right_color = dialog.display_selectbox_right_color;
    accept_.display_selectbox_right_color = dialog.display_selectbox_right_color;
    QPixmap sBoxRCPix(16,16);
    sBoxRCPix.fill(QColor(preview.display_selectbox_right_color));
    buttonSelectBoxRightColor->setIcon(QIcon(sBoxRCPix));
    connect(buttonSelectBoxRightColor, SIGNAL(clicked()), this, SLOT(chooseDisplaySelectBoxRightColor()));

    QLabel* labelSelectBoxRightFill = new QLabel(tr("Selection Box Fill (Window)"), groupBoxColor);
    QPushButton* buttonSelectBoxRightFill = new QPushButton(tr("Choose"), groupBoxColor);
    dialog.display_selectbox_right_fill = settings.display_selectbox_right_fill;
    preview.display_selectbox_right_fill = dialog.display_selectbox_right_fill;
    accept_.display_selectbox_right_fill = dialog.display_selectbox_right_fill;
    QPixmap sBoxRFPix(16,16);
    sBoxRFPix.fill(QColor(preview.display_selectbox_right_fill));
    buttonSelectBoxRightFill->setIcon(QIcon(sBoxRFPix));
    connect(buttonSelectBoxRightFill, SIGNAL(clicked()), this, SLOT(chooseDisplaySelectBoxRightFill()));

    QLabel* labelSelectBoxAlpha = new QLabel(tr("Selection Box Fill Alpha"), groupBoxColor);
    QSpinBox* spinBoxSelectBoxAlpha = new QSpinBox(groupBoxColor);
    spinBoxSelectBoxAlpha->setRange(0, 255);
    dialog.display_selectbox_alpha = settings.display_selectbox_alpha;
    preview.display_selectbox_alpha = dialog.display_selectbox_alpha;
    spinBoxSelectBoxAlpha->setValue(preview.display_selectbox_alpha);
    connect(spinBoxSelectBoxAlpha, SIGNAL(valueChanged(int)), this, SLOT(spinBoxDisplaySelectBoxAlphaValueChanged(int)));

    QGridLayout* gridLayoutColor = new QGridLayout(widget);
    gridLayoutColor->addWidget(labelCrossHairColor, 0, 0, Qt::AlignLeft);
    gridLayoutColor->addWidget(buttonCrossHairColor, 0, 1, Qt::AlignRight);
    gridLayoutColor->addWidget(labelBGColor, 1, 0, Qt::AlignLeft);
    gridLayoutColor->addWidget(buttonBGColor, 1, 1, Qt::AlignRight);
    gridLayoutColor->addWidget(labelSelectBoxLeftColor, 2, 0, Qt::AlignLeft);
    gridLayoutColor->addWidget(buttonSelectBoxLeftColor, 2, 1, Qt::AlignRight);
    gridLayoutColor->addWidget(labelSelectBoxLeftFill, 3, 0, Qt::AlignLeft);
    gridLayoutColor->addWidget(buttonSelectBoxLeftFill, 3, 1, Qt::AlignRight);
    gridLayoutColor->addWidget(labelSelectBoxRightColor, 4, 0, Qt::AlignLeft);
    gridLayoutColor->addWidget(buttonSelectBoxRightColor, 4, 1, Qt::AlignRight);
    gridLayoutColor->addWidget(labelSelectBoxRightFill, 5, 0, Qt::AlignLeft);
    gridLayoutColor->addWidget(buttonSelectBoxRightFill, 5, 1, Qt::AlignRight);
    gridLayoutColor->addWidget(labelSelectBoxAlpha, 6, 0, Qt::AlignLeft);
    gridLayoutColor->addWidget(spinBoxSelectBoxAlpha, 6, 1, Qt::AlignRight);
    groupBoxColor->setLayout(gridLayoutColor);

    /*Zoom*/
    QGroupBox* groupBoxZoom = new QGroupBox(tr("Zoom"), widget);

    QLabel* labelZoomScaleIn = new QLabel(tr("Zoom In Scale"), groupBoxZoom);
    QDoubleSpinBox* spinBoxZoomScaleIn = new QDoubleSpinBox(groupBoxZoom);
    dialog.display_zoomscale_in = settings.display_zoomscale_in;
    spinBoxZoomScaleIn->setValue(dialog.display_zoomscale_in);
    spinBoxZoomScaleIn->setSingleStep(0.01);
    spinBoxZoomScaleIn->setRange(1.01, 10.00);
    connect(spinBoxZoomScaleIn, SIGNAL(valueChanged(double)), this, SLOT(spinBoxZoomScaleInValueChanged(double)));

    QLabel* labelZoomScaleOut = new QLabel(tr("Zoom Out Scale"), groupBoxZoom);
    QDoubleSpinBox* spinBoxZoomScaleOut = new QDoubleSpinBox(groupBoxZoom);
    dialog.display_zoomscale_out = settings.display_zoomscale_out;
    spinBoxZoomScaleOut->setValue(dialog.display_zoomscale_out);
    spinBoxZoomScaleOut->setSingleStep(0.01);
    spinBoxZoomScaleOut->setRange(0.01, 0.99);
    connect(spinBoxZoomScaleOut, SIGNAL(valueChanged(double)), this, SLOT(spinBoxZoomScaleOutValueChanged(double)));

    QGridLayout* gridLayoutZoom = new QGridLayout(groupBoxZoom);
    gridLayoutZoom->addWidget(labelZoomScaleIn, 0, 0, Qt::AlignLeft);
    gridLayoutZoom->addWidget(spinBoxZoomScaleIn, 0, 1, Qt::AlignRight);
    gridLayoutZoom->addWidget(labelZoomScaleOut, 1, 0, Qt::AlignLeft);
    gridLayoutZoom->addWidget(spinBoxZoomScaleOut, 1, 1, Qt::AlignRight);
    groupBoxZoom->setLayout(gridLayoutZoom);

    /*Widget Layout*/
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget);
    /*vboxLayoutMain->addWidget(groupBoxRender); //TODO: Review OpenGL and Rendering settings for future inclusion*/
    vboxLayoutMain->addWidget(groupBoxScrollBars);
    vboxLayoutMain->addWidget(groupBoxColor);
    vboxLayoutMain->addWidget(groupBoxZoom);
    vboxLayoutMain->addStretch(1);
    widget->setLayout(vboxLayoutMain);

    QScrollArea* scrollArea = new QScrollArea(this);
    scrollArea->setWidgetResizable(1);
    scrollArea->setWidget(widget);
    return scrollArea;
}

/* TODO: finish open/save options */
QWidget* Settings_Dialog::createTabOpenSave()
{
    QWidget* widget = new QWidget(this);

    /*Custom Filter*/
    QGroupBox* groupBoxCustomFilter = new QGroupBox(tr("Custom Filter"), widget);
    groupBoxCustomFilter->setEnabled(0); /*TODO: Fixup custom filter*/

    QPushButton* buttonCustomFilterSelectAll = new QPushButton(tr("Select All"), groupBoxCustomFilter);
    connect(buttonCustomFilterSelectAll, SIGNAL(clicked()), this, SLOT(buttonCustomFilterSelectAllClicked()));
    QPushButton* buttonCustomFilterClearAll = new QPushButton("Clear All", groupBoxCustomFilter);
    connect(buttonCustomFilterClearAll, SIGNAL(clicked()), this, SLOT(buttonCustomFilterClearAllClicked()));
    QGridLayout* gridLayoutCustomFilter = new QGridLayout(groupBoxCustomFilter);

    int i;
    for (i=0; i<numberOfFormats; i++) {
        QCheckBox* c = new QCheckBox(formatTable[i].extension, groupBoxCustomFilter);
        c->setChecked(opensave_custom_filter.contains(QString("*") + formatTable[i].extension, Qt::CaseInsensitive));
        connect(c, SIGNAL(stateChanged(int)), this, SLOT(checkBoxCustomFilterStateChanged(int)));
        connect(this, SIGNAL(buttonCustomFilterSelectAll(int)), c, SLOT(setChecked(int)));
        connect(this, SIGNAL(buttonCustomFilterClearAll(int)), c, SLOT(setChecked(int)));
        gridLayoutCustomFilter->addWidget(c, i%10, i/10, Qt::AlignLeft);
    }

    gridLayoutCustomFilter->addWidget(buttonCustomFilterSelectAll, 0, 7, Qt::AlignLeft);
    gridLayoutCustomFilter->addWidget(buttonCustomFilterClearAll, 1, 7, Qt::AlignLeft);
    gridLayoutCustomFilter->setColumnStretch(7,1);
    groupBoxCustomFilter->setLayout(gridLayoutCustomFilter);

    if(opensave_custom_filter.contains("supported", Qt::CaseInsensitive)) buttonCustomFilterSelectAllClicked();

    /* Opening */
    QGroupBox* groupBoxOpening = new QGroupBox(tr("File Open"), widget);

    QComboBox* comboBoxOpenFormat = new QComboBox(groupBoxOpening);

    QCheckBox* checkBoxOpenThumbnail = new QCheckBox(tr("Preview Thumbnails"), groupBoxOpening);
    checkBoxOpenThumbnail->setChecked(0);

    /* TODO: Add a button to clear the recent history. */

    QLabel* labelRecentMaxFiles = new QLabel(tr("Number of recently accessed files to show"), groupBoxOpening);
    QSpinBox* spinBoxRecentMaxFiles = new QSpinBox(groupBoxOpening);
    spinBoxRecentMaxFiles->setRange(0, 10);
    dialog.opensave_recent_max_files = settings.opensave_recent_max_files;
    spinBoxRecentMaxFiles->setValue(dialog.opensave_recent_max_files);
    connect(spinBoxRecentMaxFiles, SIGNAL(valueChanged(int)), this, SLOT(spinBoxRecentMaxFilesValueChanged(int)));

    QFrame* frameRecent = new QFrame(groupBoxOpening);
    QGridLayout* gridLayoutRecent = new QGridLayout(frameRecent);
    gridLayoutRecent->addWidget(labelRecentMaxFiles, 0, 0, Qt::AlignLeft);
    gridLayoutRecent->addWidget(spinBoxRecentMaxFiles, 0, 1, Qt::AlignRight);
    frameRecent->setLayout(gridLayoutRecent);

    QVBoxLayout* vboxLayoutOpening = new QVBoxLayout(groupBoxOpening);
    vboxLayoutOpening->addWidget(comboBoxOpenFormat);
    vboxLayoutOpening->addWidget(checkBoxOpenThumbnail);
    vboxLayoutOpening->addWidget(frameRecent);
    groupBoxOpening->setLayout(vboxLayoutOpening);

    /*Saving*/
    QGroupBox* groupBoxSaving = new QGroupBox(tr("File Save"), widget);

    QComboBox* comboBoxSaveFormat = new QComboBox(groupBoxSaving);

    QCheckBox* checkBoxSaveThumbnail = new QCheckBox(tr("Save Thumbnails"), groupBoxSaving);
    checkBoxSaveThumbnail->setChecked(0);

    QCheckBox* checkBoxAutoSave = new QCheckBox(tr("AutoSave"), groupBoxSaving);
    checkBoxAutoSave->setChecked(0);

    QVBoxLayout* vboxLayoutSaving = new QVBoxLayout(groupBoxSaving);
    vboxLayoutSaving->addWidget(comboBoxSaveFormat);
    vboxLayoutSaving->addWidget(checkBoxSaveThumbnail);
    vboxLayoutSaving->addWidget(checkBoxAutoSave);
    groupBoxSaving->setLayout(vboxLayoutSaving);

    /*Trimming*/
    QGroupBox* groupBoxTrim = new QGroupBox(tr("Trimming"), widget);

    QLabel* labelTrimDstNumJumps = new QLabel(tr("DST Only: Minimum number of jumps to trim"), groupBoxTrim);
    QSpinBox* spinBoxTrimDstNumJumps = new QSpinBox(groupBoxTrim);
    spinBoxTrimDstNumJumps->setRange(1, 20);
    dialog.opensave_trim_dst_num_jumps = settings.opensave_trim_dst_num_jumps;
    spinBoxTrimDstNumJumps->setValue(dialog.opensave_trim_dst_num_jumps);
    connect(spinBoxTrimDstNumJumps, SIGNAL(valueChanged(int)), this, SLOT(spinBoxTrimDstNumJumpsValueChanged(int)));

    QFrame* frameTrimDstNumJumps = new QFrame(groupBoxTrim);
    QGridLayout* gridLayoutTrimDstNumJumps = new QGridLayout(frameTrimDstNumJumps);
    gridLayoutTrimDstNumJumps->addWidget(labelTrimDstNumJumps, 0, 0, Qt::AlignLeft);
    gridLayoutTrimDstNumJumps->addWidget(spinBoxTrimDstNumJumps, 0, 1, Qt::AlignRight);
    frameTrimDstNumJumps->setLayout(gridLayoutTrimDstNumJumps);

    QVBoxLayout* vboxLayoutTrim = new QVBoxLayout(groupBoxTrim);
    vboxLayoutTrim->addWidget(frameTrimDstNumJumps);
    groupBoxTrim->setLayout(vboxLayoutTrim);

    /*Widget Layout*/
    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(widget);
    vboxLayoutMain->addWidget(groupBoxCustomFilter);
    vboxLayoutMain->addWidget(groupBoxOpening);
    vboxLayoutMain->addWidget(groupBoxSaving);
    vboxLayoutMain->addWidget(groupBoxTrim);
    vboxLayoutMain->addStretch(1);
    widget->setLayout(vboxLayoutMain);

    QScrollArea* scrollArea = new QScrollArea(this);
    scrollArea->setWidgetResizable(1);
    scrollArea->setWidget(widget);
    return scrollArea;
}

QWidget* Settings_Dialog::createTabPrinting()
{
    /*
    QWidget* widget = new QWidget(this);

    //Default Printer
    QGroupBox* groupBoxDefaultPrinter = new QGroupBox(tr("Default Printer"), widget);

    QRadioButton* radioButtonUseSame = new QRadioButton(tr("Use as default device"), groupBoxDefaultPrinter);
    radioButtonUseSame->setChecked(!settings.printing_use_last_device);
    QRadioButton* radioButtonUseLast = new QRadioButton(tr("Use last used device"), groupBoxDefaultPrinter);
    radioButtonUseLast->setChecked(settings.printing_use_last_device);

    QComboBox* comboBoxDefaultDevice = new QComboBox(groupBoxDefaultPrinter);
    QList<QPrinterInfo> listAvailPrinters = QPrinterInfo::availablePrinters();
    foreach(QPrinterInfo info, listAvailPrinters)
    {
        comboBoxDefaultDevice->addItem(loadIcon(icon_print), info.printerName());
    }

    QVBoxLayout* vboxLayoutDefaultPrinter = new QVBoxLayout(groupBoxDefaultPrinter);
    vboxLayoutDefaultPrinter->addWidget(radioButtonUseSame);
    vboxLayoutDefaultPrinter->addWidget(comboBoxDefaultDevice);
    vboxLayoutDefaultPrinter->addWidget(radioButtonUseLast);
    groupBoxDefaultPrinter->setLayout(vboxLayoutDefaultPrinter);

    //Save Ink
    QGroupBox* groupBoxSaveInk = new QGroupBox(tr("Save Ink"), widget);

    QCheckBox* checkBoxDisableBG = new QCheckBox(tr("Disable Background"), groupBoxSaveInk);
    dialog.printing_disable_bg = settings.printing_disable_bg;
    checkBoxDisableBG->setChecked(dialog.printing_disable_bg);
    connect(checkBoxDisableBG, SIGNAL(stateChanged(int)), this, SLOT(checkBoxDisableBGStateChanged(int)));

    QVBoxLayout* vboxLayoutSaveInk = new QVBoxLayout(groupBoxSaveInk);
    vboxLayoutSaveInk->addWidget(checkBoxDisableBG);
    groupBoxSaveInk->setLayout(vboxLayoutSaveInk);

    //Widget Layout
    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(widget);
    vboxLayoutMain->addWidget(groupBoxDefaultPrinter);
    vboxLayoutMain->addWidget(groupBoxSaveInk);
    vboxLayoutMain->addStretch(1);
    widget->setLayout(vboxLayoutMain);

    */
    QScrollArea* scrollArea = new QScrollArea(this);
    /*scrollArea->setWidgetResizable(1);
    scrollArea->setWidget(widget); */
    return scrollArea;
}

QWidget* Settings_Dialog::createTabSnap()
{
    QWidget* widget = new QWidget(this);

    /*TODO: finish this*/

    QScrollArea* scrollArea = new QScrollArea(this);
    scrollArea->setWidgetResizable(1);
    scrollArea->setWidget(widget);
    return scrollArea;
}

QWidget* Settings_Dialog::createTabGridRuler()
{
    QWidget* widget = new QWidget(this);

    /*Grid Misc*/
    QGroupBox* groupBoxGridMisc = new QGroupBox(tr("Grid Misc"), widget);

    QCheckBox* checkBoxGridShowOnLoad = new QCheckBox(tr("Initially show grid when loading a file"), groupBoxGridMisc);
    dialog.grid_show_on_load = settings.grid_show_on_load;
    checkBoxGridShowOnLoad->setChecked(dialog.grid_show_on_load);
    connect(checkBoxGridShowOnLoad, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGridShowOnLoadStateChanged(int)));

    QCheckBox* checkBoxGridShowOrigin = new QCheckBox(tr("Show the origin when the grid is enabled"), groupBoxGridMisc);
    dialog.grid_show_origin = settings.grid_show_origin;
    checkBoxGridShowOrigin->setChecked(dialog.grid_show_origin);
    connect(checkBoxGridShowOrigin, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGridShowOriginStateChanged(int)));

    QGridLayout* gridLayoutGridMisc = new QGridLayout(widget);
    gridLayoutGridMisc->addWidget(checkBoxGridShowOnLoad, 0, 0, Qt::AlignLeft);
    gridLayoutGridMisc->addWidget(checkBoxGridShowOrigin, 1, 0, Qt::AlignLeft);
    groupBoxGridMisc->setLayout(gridLayoutGridMisc);

    /*Grid Color*/
    QGroupBox* groupBoxGridColor = new QGroupBox(tr("Grid Color"), widget);

    QCheckBox* checkBoxGridColorMatchCrossHair = new QCheckBox(tr("Match grid color to crosshair color"), groupBoxGridColor);
    dialog.grid_color_match_crosshair = settings.grid_color_match_crosshair;
    checkBoxGridColorMatchCrossHair->setChecked(dialog.grid_color_match_crosshair);
    connect(checkBoxGridColorMatchCrossHair, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGridColorMatchCrossHairStateChanged(int)));

    QLabel* labelGridColor = new QLabel(tr("Grid Color"), groupBoxGridColor);
    labelGridColor->setObjectName("labelGridColor");
    QPushButton* buttonGridColor = new QPushButton(tr("Choose"), groupBoxGridColor);
    buttonGridColor->setObjectName("buttonGridColor");
    if(dialog.grid_color_match_crosshair) { dialog.grid_color = settings.display_crosshair_color; }
    else                                  { dialog.grid_color = settings.grid_color;             }
    preview.grid_color = dialog.grid_color;
    accept_.grid_color = dialog.grid_color;
    QPixmap gridPix(16,16);
    gridPix.fill(QColor(preview.grid_color));
    buttonGridColor->setIcon(QIcon(gridPix));
    connect(buttonGridColor, SIGNAL(clicked()), this, SLOT(chooseGridColor()));

    labelGridColor->setEnabled(!dialog.grid_color_match_crosshair);
    buttonGridColor->setEnabled(!dialog.grid_color_match_crosshair);

    QGridLayout* gridLayoutGridColor = new QGridLayout(widget);
    gridLayoutGridColor->addWidget(checkBoxGridColorMatchCrossHair, 0, 0, Qt::AlignLeft);
    gridLayoutGridColor->addWidget(labelGridColor, 1, 0, Qt::AlignLeft);
    gridLayoutGridColor->addWidget(buttonGridColor, 1, 1, Qt::AlignRight);
    groupBoxGridColor->setLayout(gridLayoutGridColor);

    /*Grid Geometry*/
    QGroupBox* groupBoxGridGeom = new QGroupBox(tr("Grid Geometry"), widget);

    QCheckBox* checkBoxGridLoadFromFile = new QCheckBox(tr("Set grid size from opened file"), groupBoxGridGeom);
    dialog.grid_load_from_file = settings.grid_load_from_file;
    checkBoxGridLoadFromFile->setChecked(dialog.grid_load_from_file);
    connect(checkBoxGridLoadFromFile, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGridLoadFromFileStateChanged(int)));

    QLabel* labelGridType = new QLabel(tr("Grid Type"), groupBoxGridGeom);
    labelGridType->setObjectName("labelGridType");
    QComboBox* comboBoxGridType = new QComboBox(groupBoxGridGeom);
    comboBoxGridType->setObjectName("comboBoxGridType");
    comboBoxGridType->addItem("Rectangular");
    comboBoxGridType->addItem("Circular");
    comboBoxGridType->addItem("Isometric");
    strcpy(dialog.grid_type, settings.grid_type);
    comboBoxGridType->setCurrentIndex(comboBoxGridType->findText(dialog.grid_type));
    connect(comboBoxGridType, SIGNAL(currentIndexChanged(const QString&)), this, SLOT(comboBoxGridTypeCurrentIndexChanged(const QString&)));

    QCheckBox* checkBoxGridCenterOnOrigin = new QCheckBox(tr("Center the grid on the origin"), groupBoxGridGeom);
    checkBoxGridCenterOnOrigin->setObjectName("checkBoxGridCenterOnOrigin");
    dialog.grid_center_on_origin = settings.grid_center_on_origin;
    checkBoxGridCenterOnOrigin->setChecked(dialog.grid_center_on_origin);
    connect(checkBoxGridCenterOnOrigin, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGridCenterOnOriginStateChanged(int)));

    QLabel* labelGridCenterX = new QLabel(tr("Grid Center X"), groupBoxGridGeom);
    labelGridCenterX->setObjectName("labelGridCenterX");
    QDoubleSpinBox* spinBoxGridCenterX = new QDoubleSpinBox(groupBoxGridGeom);
    spinBoxGridCenterX->setObjectName("spinBoxGridCenterX");
    dialog.grid_center.x = settings.grid_center.x;
    spinBoxGridCenterX->setSingleStep(1.000);
    spinBoxGridCenterX->setRange(-1000.000, 1000.000);
    spinBoxGridCenterX->setValue(dialog.grid_center.x);
    connect(spinBoxGridCenterX, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridCenterXValueChanged(double)));

    QLabel* labelGridCenterY = new QLabel(tr("Grid Center Y"), groupBoxGridGeom);
    labelGridCenterY->setObjectName("labelGridCenterY");
    QDoubleSpinBox* spinBoxGridCenterY = new QDoubleSpinBox(groupBoxGridGeom);
    spinBoxGridCenterY->setObjectName("spinBoxGridCenterY");
    dialog.grid_center.y = settings.grid_center.y;
    spinBoxGridCenterY->setSingleStep(1.000);
    spinBoxGridCenterY->setRange(-1000.000, 1000.000);
    spinBoxGridCenterY->setValue(dialog.grid_center.y);
    connect(spinBoxGridCenterY, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridCenterYValueChanged(double)));

    QLabel* labelGridSizeX = new QLabel(tr("Grid Size X"), groupBoxGridGeom);
    labelGridSizeX->setObjectName("labelGridSizeX");
    QDoubleSpinBox* spinBoxGridSizeX = new QDoubleSpinBox(groupBoxGridGeom);
    spinBoxGridSizeX->setObjectName("spinBoxGridSizeX");
    dialog.grid_size.x = settings.grid_size.x;
    spinBoxGridSizeX->setSingleStep(1.000);
    spinBoxGridSizeX->setRange(1.000, 1000.000);
    spinBoxGridSizeX->setValue(dialog.grid_size.x);
    connect(spinBoxGridSizeX, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSizeXValueChanged(double)));

    QLabel* labelGridSizeY = new QLabel(tr("Grid Size Y"), groupBoxGridGeom);
    labelGridSizeY->setObjectName("labelGridSizeY");
    QDoubleSpinBox* spinBoxGridSizeY = new QDoubleSpinBox(groupBoxGridGeom);
    spinBoxGridSizeY->setObjectName("spinBoxGridSizeY");
    dialog.grid_size.y = settings.grid_size.y;
    spinBoxGridSizeY->setSingleStep(1.000);
    spinBoxGridSizeY->setRange(1.000, 1000.000);
    spinBoxGridSizeY->setValue(dialog.grid_size.y);
    connect(spinBoxGridSizeY, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSizeYValueChanged(double)));

    QLabel* labelGridSpacingX = new QLabel(tr("Grid Spacing X"), groupBoxGridGeom);
    labelGridSpacingX->setObjectName("labelGridSpacingX");
    QDoubleSpinBox* spinBoxGridSpacingX = new QDoubleSpinBox(groupBoxGridGeom);
    spinBoxGridSpacingX->setObjectName("spinBoxGridSpacingX");
    dialog.grid_spacing.x = settings.grid_spacing.x;
    spinBoxGridSpacingX->setSingleStep(1.000);
    spinBoxGridSpacingX->setRange(0.001, 1000.000);
    spinBoxGridSpacingX->setValue(dialog.grid_spacing.x);
    connect(spinBoxGridSpacingX, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSpacingXValueChanged(double)));

    QLabel* labelGridSpacingY = new QLabel(tr("Grid Spacing Y"), groupBoxGridGeom);
    labelGridSpacingY->setObjectName("labelGridSpacingY");
    QDoubleSpinBox* spinBoxGridSpacingY = new QDoubleSpinBox(groupBoxGridGeom);
    spinBoxGridSpacingY->setObjectName("spinBoxGridSpacingY");
    dialog.grid_spacing.y = settings.grid_spacing.y;
    spinBoxGridSpacingY->setSingleStep(1.000);
    spinBoxGridSpacingY->setRange(0.001, 1000.000);
    spinBoxGridSpacingY->setValue(dialog.grid_spacing.y);
    connect(spinBoxGridSpacingY, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSpacingYValueChanged(double)));

    QLabel* labelGridSizeRadius = new QLabel(tr("Grid Size Radius"), groupBoxGridGeom);
    labelGridSizeRadius->setObjectName("labelGridSizeRadius");
    QDoubleSpinBox* spinBoxGridSizeRadius = new QDoubleSpinBox(groupBoxGridGeom);
    spinBoxGridSizeRadius->setObjectName("spinBoxGridSizeRadius");
    dialog.grid_size_radius = settings.grid_size_radius;
    spinBoxGridSizeRadius->setSingleStep(1.000);
    spinBoxGridSizeRadius->setRange(1.000, 1000.000);
    spinBoxGridSizeRadius->setValue(dialog.grid_size_radius);
    connect(spinBoxGridSizeRadius, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSizeRadiusValueChanged(double)));

    QLabel* labelGridSpacingRadius = new QLabel(tr("Grid Spacing Radius"), groupBoxGridGeom);
    labelGridSpacingRadius->setObjectName("labelGridSpacingRadius");
    QDoubleSpinBox* spinBoxGridSpacingRadius = new QDoubleSpinBox(groupBoxGridGeom);
    spinBoxGridSpacingRadius->setObjectName("spinBoxGridSpacingRadius");
    dialog.grid_spacing_radius = settings.grid_spacing_radius;
    spinBoxGridSpacingRadius->setSingleStep(1.000);
    spinBoxGridSpacingRadius->setRange(0.001, 1000.000);
    spinBoxGridSpacingRadius->setValue(dialog.grid_spacing_radius);
    connect(spinBoxGridSpacingRadius, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSpacingRadiusValueChanged(double)));

    QLabel* labelGridSpacingAngle = new QLabel(tr("Grid Spacing Angle"), groupBoxGridGeom);
    labelGridSpacingAngle->setObjectName("labelGridSpacingAngle");
    QDoubleSpinBox* spinBoxGridSpacingAngle = new QDoubleSpinBox(groupBoxGridGeom);
    spinBoxGridSpacingAngle->setObjectName("spinBoxGridSpacingAngle");
    dialog.grid_spacing_angle = settings.grid_spacing_angle;
    spinBoxGridSpacingAngle->setSingleStep(1.000);
    spinBoxGridSpacingAngle->setRange(0.001, 1000.000);
    spinBoxGridSpacingAngle->setValue(dialog.grid_spacing_angle);
    connect(spinBoxGridSpacingAngle, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSpacingAngleValueChanged(double)));

    labelGridType->setEnabled(!dialog.grid_load_from_file);
    comboBoxGridType->setEnabled(!dialog.grid_load_from_file);
    checkBoxGridCenterOnOrigin->setEnabled(!dialog.grid_load_from_file);
    labelGridCenterX->setEnabled(!dialog.grid_load_from_file);
    spinBoxGridCenterX->setEnabled(!dialog.grid_load_from_file);
    labelGridCenterY->setEnabled(!dialog.grid_load_from_file);
    spinBoxGridCenterY->setEnabled(!dialog.grid_load_from_file);
    labelGridSizeX->setEnabled(!dialog.grid_load_from_file);
    spinBoxGridSizeX->setEnabled(!dialog.grid_load_from_file);
    labelGridSizeY->setEnabled(!dialog.grid_load_from_file);
    spinBoxGridSizeY->setEnabled(!dialog.grid_load_from_file);
    labelGridSpacingX->setEnabled(!dialog.grid_load_from_file);
    spinBoxGridSpacingX->setEnabled(!dialog.grid_load_from_file);
    labelGridSpacingY->setEnabled(!dialog.grid_load_from_file);
    spinBoxGridSpacingY->setEnabled(!dialog.grid_load_from_file);
    labelGridSizeRadius->setEnabled(!dialog.grid_load_from_file);
    spinBoxGridSizeRadius->setEnabled(!dialog.grid_load_from_file);
    labelGridSpacingRadius->setEnabled(!dialog.grid_load_from_file);
    spinBoxGridSpacingRadius->setEnabled(!dialog.grid_load_from_file);
    labelGridSpacingAngle->setEnabled(!dialog.grid_load_from_file);
    spinBoxGridSpacingAngle->setEnabled(!dialog.grid_load_from_file);

    int visibility = 0;
    if(dialog.grid_type == "Circular") visibility = 1;
    labelGridSizeX->setVisible(!visibility);
    spinBoxGridSizeX->setVisible(!visibility);
    labelGridSizeY->setVisible(!visibility);
    spinBoxGridSizeY->setVisible(!visibility);
    labelGridSpacingX->setVisible(!visibility);
    spinBoxGridSpacingX->setVisible(!visibility);
    labelGridSpacingY->setVisible(!visibility);
    spinBoxGridSpacingY->setVisible(!visibility);
    labelGridSizeRadius->setVisible(visibility);
    spinBoxGridSizeRadius->setVisible(visibility);
    labelGridSpacingRadius->setVisible(visibility);
    spinBoxGridSpacingRadius->setVisible(visibility);
    labelGridSpacingAngle->setVisible(visibility);
    spinBoxGridSpacingAngle->setVisible(visibility);

    QGridLayout* gridLayoutGridGeom = new QGridLayout(groupBoxGridGeom);
    gridLayoutGridGeom->addWidget(checkBoxGridLoadFromFile, 0, 0, Qt::AlignLeft);
    gridLayoutGridGeom->addWidget(labelGridType, 1, 0, Qt::AlignLeft);
    gridLayoutGridGeom->addWidget(comboBoxGridType, 1, 1, Qt::AlignRight);
    gridLayoutGridGeom->addWidget(checkBoxGridCenterOnOrigin, 2, 0, Qt::AlignLeft);
    gridLayoutGridGeom->addWidget(labelGridCenterX, 3, 0, Qt::AlignLeft);
    gridLayoutGridGeom->addWidget(spinBoxGridCenterX, 3, 1, Qt::AlignRight);
    gridLayoutGridGeom->addWidget(labelGridCenterY, 4, 0, Qt::AlignLeft);
    gridLayoutGridGeom->addWidget(spinBoxGridCenterY, 4, 1, Qt::AlignRight);
    gridLayoutGridGeom->addWidget(labelGridSizeX, 5, 0, Qt::AlignLeft);
    gridLayoutGridGeom->addWidget(spinBoxGridSizeX, 5, 1, Qt::AlignRight);
    gridLayoutGridGeom->addWidget(labelGridSizeY, 6, 0, Qt::AlignLeft);
    gridLayoutGridGeom->addWidget(spinBoxGridSizeY, 6, 1, Qt::AlignRight);
    gridLayoutGridGeom->addWidget(labelGridSpacingX, 7, 0, Qt::AlignLeft);
    gridLayoutGridGeom->addWidget(spinBoxGridSpacingX, 7, 1, Qt::AlignRight);
    gridLayoutGridGeom->addWidget(labelGridSpacingY, 8, 0, Qt::AlignLeft);
    gridLayoutGridGeom->addWidget(spinBoxGridSpacingY, 8, 1, Qt::AlignRight);
    gridLayoutGridGeom->addWidget(labelGridSizeRadius, 9, 0, Qt::AlignLeft);
    gridLayoutGridGeom->addWidget(spinBoxGridSizeRadius, 9, 1, Qt::AlignRight);
    gridLayoutGridGeom->addWidget(labelGridSpacingRadius, 10, 0, Qt::AlignLeft);
    gridLayoutGridGeom->addWidget(spinBoxGridSpacingRadius, 10, 1, Qt::AlignRight);
    gridLayoutGridGeom->addWidget(labelGridSpacingAngle, 11, 0, Qt::AlignLeft);
    gridLayoutGridGeom->addWidget(spinBoxGridSpacingAngle, 11, 1, Qt::AlignRight);
    groupBoxGridGeom->setLayout(gridLayoutGridGeom);

    /*Ruler Misc*/
    QGroupBox* groupBoxRulerMisc = new QGroupBox(tr("Ruler Misc"), widget);

    QCheckBox* checkBoxRulerShowOnLoad = new QCheckBox(tr("Initially show ruler when loading a file"), groupBoxRulerMisc);
    dialog.ruler_show_on_load = settings.ruler_show_on_load;
    checkBoxRulerShowOnLoad->setChecked(dialog.ruler_show_on_load);
    connect(checkBoxRulerShowOnLoad, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRulerShowOnLoadStateChanged(int)));

    QLabel* labelRulerMetric = new QLabel(tr("Ruler Units"), groupBoxRulerMisc);
    QComboBox* comboBoxRulerMetric = new QComboBox(groupBoxRulerMisc);
    comboBoxRulerMetric->addItem("Imperial", 0);
    comboBoxRulerMetric->addItem("Metric", 1);
    dialog.ruler_metric = settings.ruler_metric;
    comboBoxRulerMetric->setCurrentIndex(comboBoxRulerMetric->findData(dialog.ruler_metric));
    connect(comboBoxRulerMetric, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxRulerMetricCurrentIndexChanged(int)));

    QGridLayout* gridLayoutRulerMisc = new QGridLayout(widget);
    gridLayoutRulerMisc->addWidget(checkBoxRulerShowOnLoad, 0, 0, Qt::AlignLeft);
    gridLayoutRulerMisc->addWidget(labelRulerMetric, 1, 0, Qt::AlignLeft);
    gridLayoutRulerMisc->addWidget(comboBoxRulerMetric, 1, 1, Qt::AlignRight);
    groupBoxRulerMisc->setLayout(gridLayoutRulerMisc);

    /*Ruler Color*/
    QGroupBox* groupBoxRulerColor = new QGroupBox(tr("Ruler Color"), widget);

    QLabel* labelRulerColor = new QLabel(tr("Ruler Color"), groupBoxRulerColor);
    labelRulerColor->setObjectName("labelRulerColor");
    QPushButton* buttonRulerColor = new QPushButton(tr("Choose"), groupBoxRulerColor);
    buttonRulerColor->setObjectName("buttonRulerColor");
    dialog.ruler_color = settings.ruler_color;
    preview.ruler_color = dialog.ruler_color;
    accept_.ruler_color = dialog.ruler_color;
    QPixmap rulerPix(16,16);
    rulerPix.fill(QColor(preview.ruler_color));
    buttonRulerColor->setIcon(QIcon(rulerPix));
    connect(buttonRulerColor, SIGNAL(clicked()), this, SLOT(chooseRulerColor()));

    QGridLayout* gridLayoutRulerColor = new QGridLayout(widget);
    gridLayoutRulerColor->addWidget(labelRulerColor, 1, 0, Qt::AlignLeft);
    gridLayoutRulerColor->addWidget(buttonRulerColor, 1, 1, Qt::AlignRight);
    groupBoxRulerColor->setLayout(gridLayoutRulerColor);

    /*Ruler Geometry*/
    QGroupBox* groupBoxRulerGeom = new QGroupBox(tr("Ruler Geometry"), widget);

    QLabel* labelRulerPixelSize = new QLabel(tr("Ruler Pixel Size"), groupBoxRulerGeom);
    labelRulerPixelSize->setObjectName("labelRulerPixelSize");
    QDoubleSpinBox* spinBoxRulerPixelSize = new QDoubleSpinBox(groupBoxRulerGeom);
    spinBoxRulerPixelSize->setObjectName("spinBoxRulerPixelSize");
    dialog.ruler_pixel_size = settings.ruler_pixel_size;
    spinBoxRulerPixelSize->setSingleStep(1.000);
    spinBoxRulerPixelSize->setRange(20.000, 100.000);
    spinBoxRulerPixelSize->setValue(dialog.ruler_pixel_size);
    connect(spinBoxRulerPixelSize, SIGNAL(valueChanged(double)), this, SLOT(spinBoxRulerPixelSizeValueChanged(double)));

    QGridLayout* gridLayoutRulerGeom = new QGridLayout(groupBoxRulerGeom);
    gridLayoutRulerGeom->addWidget(labelRulerPixelSize, 0, 0, Qt::AlignLeft);
    gridLayoutRulerGeom->addWidget(spinBoxRulerPixelSize, 0, 1, Qt::AlignRight);
    groupBoxRulerGeom->setLayout(gridLayoutRulerGeom);

    /*Widget Layout*/
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget);
    vboxLayoutMain->addWidget(groupBoxGridMisc);
    vboxLayoutMain->addWidget(groupBoxGridColor);
    vboxLayoutMain->addWidget(groupBoxGridGeom);
    vboxLayoutMain->addWidget(groupBoxRulerMisc);
    vboxLayoutMain->addWidget(groupBoxRulerColor);
    vboxLayoutMain->addWidget(groupBoxRulerGeom);
    vboxLayoutMain->addStretch(1);
    widget->setLayout(vboxLayoutMain);

    QScrollArea* scrollArea = new QScrollArea(this);
    scrollArea->setWidgetResizable(1);
    scrollArea->setWidget(widget);
    return scrollArea;
}

QWidget* Settings_Dialog::createTabOrthoPolar()
{
    QWidget* widget = new QWidget(this);

    /*TODO: finish this*/

    QScrollArea* scrollArea = new QScrollArea(this);
    scrollArea->setWidgetResizable(1);
    scrollArea->setWidget(widget);
    return scrollArea;
}

#define make_check_box(label, checked, icon, f, x, y) \
    { \
        QCheckBox* c = new QCheckBox(tr(label), groupBoxQSnapLoc); \
        c->setChecked(settings.checked); \
        c->setIcon(loadIcon(icon)); \
        connect(c, SIGNAL(stateChanged(int)), this, SLOT(f(int))); \
        connect(this, SIGNAL(buttonQSnapSelectAll(int)), c, SLOT(setChecked(int))); \
        connect(this, SIGNAL(buttonQSnapClearAll(int)), c, SLOT(setChecked(int))); \
        gridLayoutQSnap->addWidget(c, x, y, Qt::AlignLeft); \
        dialog.checked = settings.checked; \
    }

QWidget* Settings_Dialog::createTabQuickSnap()
{
    QWidget* widget = new QWidget(this);

    /*QSnap Locators*/
    QGroupBox* groupBoxQSnapLoc = new QGroupBox(tr("Locators Used"), widget);
    QPushButton* buttonQSnapSelectAll = new QPushButton(tr("Select All"), groupBoxQSnapLoc);
    QPushButton* buttonQSnapClearAll = new QPushButton(tr("Clear All"), groupBoxQSnapLoc);
    QGridLayout* gridLayoutQSnap = new QGridLayout(groupBoxQSnapLoc);

    connect(buttonQSnapSelectAll, SIGNAL(clicked()), this, SLOT(buttonQSnapSelectAllClicked()));
    connect(buttonQSnapClearAll, SIGNAL(clicked()), this, SLOT(buttonQSnapClearAllClicked()));

    make_check_box("Endpoint", qsnap_endpoint, icon_locator_snaptoendpoint, checkBoxQSnapEndPointStateChanged, 0, 0);
    make_check_box("Midpoint", qsnap_midpoint, icon_locator_snaptomidpoint, checkBoxQSnapMidPointStateChanged, 1, 0);
    make_check_box("Center", qsnap_center, icon_locator_snaptocenter, checkBoxQSnapCenterStateChanged, 2, 0);
    make_check_box("Node", qsnap_node, icon_locator_snaptonode, checkBoxQSnapNodeStateChanged, 3, 0);
    make_check_box("Quadrant", qsnap_quadrant, icon_locator_snaptoquadrant, checkBoxQSnapQuadrantStateChanged, 4, 0);
    make_check_box("Intersection", qsnap_intersection, icon_locator_snaptointersection, checkBoxQSnapIntersectionStateChanged, 5, 0);
    make_check_box("Extension", qsnap_extension, icon_locator_snaptoextension, checkBoxQSnapExtensionStateChanged, 6, 0);
    make_check_box("Insertion", qsnap_insertion, icon_locator_snaptoinsert, checkBoxQSnapInsertionStateChanged, 0, 1);
    make_check_box("Perpendicular", qsnap_perpendicular, icon_locator_snaptoperpendicular, checkBoxQSnapPerpendicularStateChanged, 1, 1);
    make_check_box("Tangent", qsnap_tangent, icon_locator_snaptotangent, checkBoxQSnapTangentStateChanged, 2, 1);
    make_check_box("Nearest", qsnap_nearest, icon_locator_snaptonearest, checkBoxQSnapNearestStateChanged, 3, 1);
    make_check_box("Apparent Intersection", qsnap_apparent, icon_locator_snaptoapparentintersection, checkBoxQSnapApparentIntersectionStateChanged, 4, 1);
    make_check_box("Parallel", qsnap_parallel, icon_locator_snaptoparallel, checkBoxQSnapParallelStateChanged, 5, 1);

    gridLayoutQSnap->addWidget(buttonQSnapSelectAll, 0, 2, Qt::AlignLeft);
    gridLayoutQSnap->addWidget(buttonQSnapClearAll, 1, 2, Qt::AlignLeft);
    gridLayoutQSnap->setColumnStretch(2,1);
    groupBoxQSnapLoc->setLayout(gridLayoutQSnap);

    /*QSnap Visual Config*/
    QGroupBox* groupBoxQSnapVisual = new QGroupBox(tr("Visual Configuration"), widget);

    QLabel* labelQSnapLocColor = new QLabel(tr("Locator Color"), groupBoxQSnapVisual);
    QComboBox* comboBoxQSnapLocColor = new QComboBox(groupBoxQSnapVisual);
    addColorsToComboBox(comboBoxQSnapLocColor);
    dialog.qsnap_locator_color = settings.qsnap_locator_color;
    comboBoxQSnapLocColor->setCurrentIndex(comboBoxQSnapLocColor->findData(dialog.qsnap_locator_color));
    connect(comboBoxQSnapLocColor, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxQSnapLocatorColorCurrentIndexChanged(int)));

    QLabel* labelQSnapLocSize = new QLabel(tr("Locator Size"), groupBoxQSnapVisual);
    QSlider* sliderQSnapLocSize = new QSlider(Qt::Horizontal, groupBoxQSnapVisual);
    sliderQSnapLocSize->setRange(1,20);
    dialog.qsnap_locator_size = settings.qsnap_locator_size;
    sliderQSnapLocSize->setValue(dialog.qsnap_locator_size);
    connect(sliderQSnapLocSize, SIGNAL(valueChanged(int)), this, SLOT(sliderQSnapLocatorSizeValueChanged(int)));

    QVBoxLayout* vboxLayoutQSnapVisual = new QVBoxLayout(groupBoxQSnapVisual);
    vboxLayoutQSnapVisual->addWidget(labelQSnapLocColor);
    vboxLayoutQSnapVisual->addWidget(comboBoxQSnapLocColor);
    vboxLayoutQSnapVisual->addWidget(labelQSnapLocSize);
    vboxLayoutQSnapVisual->addWidget(sliderQSnapLocSize);
    groupBoxQSnapVisual->setLayout(vboxLayoutQSnapVisual);

    /*QSnap Sensitivity Config*/
    QGroupBox* groupBoxQSnapSensitivity = new QGroupBox(tr("Sensitivity"), widget);

    QLabel* labelQSnapApertureSize = new QLabel(tr("Aperture Size"), groupBoxQSnapSensitivity);
    QSlider* sliderQSnapApertureSize = new QSlider(Qt::Horizontal, groupBoxQSnapSensitivity);
    sliderQSnapApertureSize->setRange(1,20);
    dialog.qsnap_aperture_size = settings.qsnap_aperture_size;
    sliderQSnapApertureSize->setValue(dialog.qsnap_aperture_size);
    connect(sliderQSnapApertureSize, SIGNAL(valueChanged(int)), this, SLOT(sliderQSnapApertureSizeValueChanged(int)));

    QVBoxLayout* vboxLayoutQSnapSensitivity = new QVBoxLayout(groupBoxQSnapSensitivity);
    vboxLayoutQSnapSensitivity->addWidget(labelQSnapApertureSize);
    vboxLayoutQSnapSensitivity->addWidget(sliderQSnapApertureSize);
    groupBoxQSnapSensitivity->setLayout(vboxLayoutQSnapSensitivity);

    /*Widget Layout*/
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget);
    vboxLayoutMain->addWidget(groupBoxQSnapLoc);
    vboxLayoutMain->addWidget(groupBoxQSnapVisual);
    vboxLayoutMain->addWidget(groupBoxQSnapSensitivity);
    vboxLayoutMain->addStretch(1);
    widget->setLayout(vboxLayoutMain);

    QScrollArea* scrollArea = new QScrollArea(this);
    scrollArea->setWidgetResizable(1);
    scrollArea->setWidget(widget);
    return scrollArea;
}

#undef make_check_box

QWidget* Settings_Dialog::createTabQuickTrack()
{
    QWidget* widget = new QWidget(this);

    /* TODO: finish this */

    QScrollArea* scrollArea = new QScrollArea(this);
    scrollArea->setWidgetResizable(1);
    scrollArea->setWidget(widget);
    return scrollArea;
}

QWidget* Settings_Dialog::createTabLineWeight()
{
    QWidget* widget = new QWidget(this);

    /* TODO: finish this */

    /* Misc */
    QGroupBox* groupBoxLwtMisc = new QGroupBox(tr("LineWeight Misc"), widget);

    QGraphicsScene* s = mainWin->activeScene();

    QCheckBox* checkBoxShowLwt = new QCheckBox(tr("Show LineWeight"), groupBoxLwtMisc);
    if (s) {
        dialog.lwt_show_lwt = s->property("ENABLE_LWT").toBool();
    }
    else {
        dialog.lwt_show_lwt = settings.lwt_show_lwt;
    }
    preview.lwt_show_lwt = dialog.lwt_show_lwt;
    checkBoxShowLwt->setChecked(preview.lwt_show_lwt);
    connect(checkBoxShowLwt, SIGNAL(stateChanged(int)), this, SLOT(checkBoxLwtShowLwtStateChanged(int)));

    QCheckBox* checkBoxRealRender = new QCheckBox(tr("RealRender"), groupBoxLwtMisc);
    checkBoxRealRender->setObjectName("checkBoxRealRender");
    if (s) {
        dialog.lwt_real_render = s->property("ENABLE_REAL").toBool();
    }
    else {
        dialog.lwt_real_render = settings.lwt_real_render;
    }
    preview.lwt_real_render = dialog.lwt_real_render;
    checkBoxRealRender->setChecked(preview.lwt_real_render);
    connect(checkBoxRealRender, SIGNAL(stateChanged(int)), this, SLOT(checkBoxLwtRealRenderStateChanged(int)));
    checkBoxRealRender->setEnabled(dialog.lwt_show_lwt);

    QLabel* labelDefaultLwt = new QLabel(tr("Default weight"), groupBoxLwtMisc);
    labelDefaultLwt->setEnabled(0); /* TODO: remove later */
    QComboBox* comboBoxDefaultLwt = new QComboBox(groupBoxLwtMisc);
    dialog.lwt_default_lwt = settings.lwt_default_lwt;
    /* TODO: populate the comboBox and set the initial value */
    comboBoxDefaultLwt->addItem(QString().setNum(dialog.lwt_default_lwt, 'F', 2).append(" mm"), dialog.lwt_default_lwt);
    comboBoxDefaultLwt->setEnabled(0); /* TODO: remove later */

    QVBoxLayout* vboxLayoutLwtMisc = new QVBoxLayout(groupBoxLwtMisc);
    vboxLayoutLwtMisc->addWidget(checkBoxShowLwt);
    vboxLayoutLwtMisc->addWidget(checkBoxRealRender);
    vboxLayoutLwtMisc->addWidget(labelDefaultLwt);
    vboxLayoutLwtMisc->addWidget(comboBoxDefaultLwt);
    groupBoxLwtMisc->setLayout(vboxLayoutLwtMisc);

    /*Widget Layout*/
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget);
    vboxLayoutMain->addWidget(groupBoxLwtMisc);
    vboxLayoutMain->addStretch(1);
    widget->setLayout(vboxLayoutMain);

    QScrollArea* scrollArea = new QScrollArea(this);
    scrollArea->setWidgetResizable(1);
    scrollArea->setWidget(widget);
    return scrollArea;
}

QWidget* Settings_Dialog::createTabSelection()
{
    QWidget* widget = new QWidget(this);

    /* Selection Modes */
    QGroupBox* groupBoxSelectionModes = new QGroupBox(tr("Modes"), widget);

    QCheckBox* checkBoxSelectionModePickFirst = new QCheckBox(tr("Allow Preselection (PickFirst)"), groupBoxSelectionModes);
    dialog.selection_mode_pickfirst = settings.selection_mode_pickfirst;
    checkBoxSelectionModePickFirst->setChecked(dialog.selection_mode_pickfirst);
    checkBoxSelectionModePickFirst->setChecked(1); checkBoxSelectionModePickFirst->setEnabled(0); /* TODO: Remove this line when Post-selection is available */
    connect(checkBoxSelectionModePickFirst, SIGNAL(stateChanged(int)), this, SLOT(checkBoxSelectionModePickFirstStateChanged(int)));

    QCheckBox* checkBoxSelectionModePickAdd = new QCheckBox(tr("Add to Selection (PickAdd)"), groupBoxSelectionModes);
    dialog.selection_mode_pickadd = settings.selection_mode_pickadd;
    checkBoxSelectionModePickAdd->setChecked(dialog.selection_mode_pickadd);
    connect(checkBoxSelectionModePickAdd, SIGNAL(stateChanged(int)), this, SLOT(checkBoxSelectionModePickAddStateChanged(int)));

    QCheckBox* checkBoxSelectionModePickDrag = new QCheckBox(tr("Drag to Select (PickDrag)"), groupBoxSelectionModes);
    dialog.selection_mode_pickdrag = settings.selection_mode_pickdrag;
    checkBoxSelectionModePickDrag->setChecked(dialog.selection_mode_pickdrag);
    checkBoxSelectionModePickDrag->setChecked(0); checkBoxSelectionModePickDrag->setEnabled(0); /*TODO: Remove this line when this functionality is available*/
    connect(checkBoxSelectionModePickDrag, SIGNAL(stateChanged(int)), this, SLOT(checkBoxSelectionModePickDragStateChanged(int)));

    QVBoxLayout* vboxLayoutSelectionModes = new QVBoxLayout(groupBoxSelectionModes);
    vboxLayoutSelectionModes->addWidget(checkBoxSelectionModePickFirst);
    vboxLayoutSelectionModes->addWidget(checkBoxSelectionModePickAdd);
    vboxLayoutSelectionModes->addWidget(checkBoxSelectionModePickDrag);
    groupBoxSelectionModes->setLayout(vboxLayoutSelectionModes);

    /*Selection Colors*/
    QGroupBox* groupBoxSelectionColors = new QGroupBox(tr("Colors"), widget);

    QLabel* labelCoolGripColor = new QLabel(tr("Cool Grip (Unselected)"), groupBoxSelectionColors);
    QComboBox* comboBoxCoolGripColor = new QComboBox(groupBoxSelectionColors);
    addColorsToComboBox(comboBoxCoolGripColor);
    dialog.selection_coolgrip_color = settings.selection_coolgrip_color;
    comboBoxCoolGripColor->setCurrentIndex(comboBoxCoolGripColor->findData(dialog.selection_coolgrip_color));
    connect(comboBoxCoolGripColor, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxSelectionCoolGripColorCurrentIndexChanged(int)));

    QLabel* labelHotGripColor = new QLabel(tr("Hot Grip (Selected)"), groupBoxSelectionColors);
    QComboBox* comboBoxHotGripColor = new QComboBox(groupBoxSelectionColors);
    addColorsToComboBox(comboBoxHotGripColor);
    dialog.selection_hotgrip_color = settings.selection_hotgrip_color;
    comboBoxHotGripColor->setCurrentIndex(comboBoxHotGripColor->findData(dialog.selection_hotgrip_color));
    connect(comboBoxHotGripColor, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxSelectionHotGripColorCurrentIndexChanged(int)));

    QVBoxLayout* vboxLayoutSelectionColors = new QVBoxLayout(groupBoxSelectionColors);
    vboxLayoutSelectionColors->addWidget(labelCoolGripColor);
    vboxLayoutSelectionColors->addWidget(comboBoxCoolGripColor);
    vboxLayoutSelectionColors->addWidget(labelHotGripColor);
    vboxLayoutSelectionColors->addWidget(comboBoxHotGripColor);
    groupBoxSelectionColors->setLayout(vboxLayoutSelectionColors);

    /*Selection Sizes*/
    QGroupBox* groupBoxSelectionSizes = new QGroupBox(tr("Sizes"), widget);

    QLabel* labelSelectionGripSize = new QLabel(tr("Grip Size"), groupBoxSelectionSizes);
    QSlider* sliderSelectionGripSize = new QSlider(Qt::Horizontal, groupBoxSelectionSizes);
    sliderSelectionGripSize->setRange(1,20);
    dialog.selection_grip_size = settings.selection_grip_size;
    sliderSelectionGripSize->setValue(dialog.selection_grip_size);
    connect(sliderSelectionGripSize, SIGNAL(valueChanged(int)), this, SLOT(sliderSelectionGripSizeValueChanged(int)));

    QLabel* labelSelectionPickBoxSize = new QLabel(tr("Pickbox Size"), groupBoxSelectionSizes);
    QSlider* sliderSelectionPickBoxSize = new QSlider(Qt::Horizontal, groupBoxSelectionSizes);
    sliderSelectionPickBoxSize->setRange(1,20);
    dialog.selection_pickbox_size = settings.selection_pickbox_size;
    sliderSelectionPickBoxSize->setValue(dialog.selection_pickbox_size);
    connect(sliderSelectionPickBoxSize, SIGNAL(valueChanged(int)), this, SLOT(sliderSelectionPickBoxSizeValueChanged(int)));

    QVBoxLayout* vboxLayoutSelectionSizes = new QVBoxLayout(groupBoxSelectionSizes);
    vboxLayoutSelectionSizes->addWidget(labelSelectionGripSize);
    vboxLayoutSelectionSizes->addWidget(sliderSelectionGripSize);
    vboxLayoutSelectionSizes->addWidget(labelSelectionPickBoxSize);
    vboxLayoutSelectionSizes->addWidget(sliderSelectionPickBoxSize);
    groupBoxSelectionSizes->setLayout(vboxLayoutSelectionSizes);

    /*Widget Layout*/
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget);
    vboxLayoutMain->addWidget(groupBoxSelectionModes);
    vboxLayoutMain->addWidget(groupBoxSelectionColors);
    vboxLayoutMain->addWidget(groupBoxSelectionSizes);
    vboxLayoutMain->addStretch(1);
    widget->setLayout(vboxLayoutMain);

    QScrollArea* scrollArea = new QScrollArea(this);
    scrollArea->setWidgetResizable(1);
    scrollArea->setWidget(widget);
    return scrollArea;
}

void Settings_Dialog::addColorsToComboBox(QComboBox* comboBox)
{
    comboBox->addItem(loadIcon(icon_colorred), tr("Red"), qRgb(255, 0, 0));
    comboBox->addItem(loadIcon(icon_coloryellow), tr("Yellow"), qRgb(255,255, 0));
    comboBox->addItem(loadIcon(icon_colorgreen), tr("Green"), qRgb(  0,255, 0));
    comboBox->addItem(loadIcon(icon_colorcyan), tr("Cyan"), qRgb(  0,255,255));
    comboBox->addItem(loadIcon(icon_colorblue), tr("Blue"), qRgb(  0, 0,255));
    comboBox->addItem(loadIcon(icon_colormagenta), tr("Magenta"), qRgb(255, 0,255));
    comboBox->addItem(loadIcon(icon_colorwhite), tr("White"), qRgb(255,255,255));
    /* TODO: Add Other... so the user can select custom colors */
}

void Settings_Dialog::comboBoxLanguageCurrentIndexChanged(const QString& lang)
{
    strcpy(dialog.general_language, lang.toLower().toLocal8Bit().constData());
}

void Settings_Dialog::comboBoxIconThemeCurrentIndexChanged(const QString& theme)
{
    strcpy(dialog.general_icon_theme, theme.toLocal8Bit().constData());
}

void Settings_Dialog::comboBoxIconSizeCurrentIndexChanged(int index)
{
    QComboBox* comboBox = qobject_cast<QComboBox*>(sender());
    if(comboBox)
    {
        bool ok = 0;
        dialog.general_icon_size = comboBox->itemData(index).toUInt(&ok);
        if(!ok)
            dialog.general_icon_size = 16;
    }
    else
        dialog.general_icon_size = 16;
}

void Settings_Dialog::checkBoxGeneralMdiBGUseLogoStateChanged(int checked)
{
    preview.general_mdi_bg_use_logo = checked;
    mainWin->mdiArea->useBackgroundLogo(checked);
}

void Settings_Dialog::chooseGeneralMdiBackgroundLogo()
{
    QPushButton* button = qobject_cast<QPushButton*>(sender());
    if(button)
    {
        QString selectedImage;
        selectedImage = QFileDialog::getOpenFileName(this, tr("Open File"),
                        QStandardPaths::writableLocation(QStandardPaths::PicturesLocation),
                        tr("Images (*.bmp *.png *.jpg)"));

        if (!selectedImage.isNull())
            strcpy(accept_.general_mdi_bg_logo, selectedImage.toLocal8Bit().constData());

        /*Update immediately so it can be previewed*/
        mainWin->mdiArea->setBackgroundLogo(accept_.general_mdi_bg_logo);
    }
}

void Settings_Dialog::checkBoxGeneralMdiBGUseTextureStateChanged(int checked)
{
    preview.general_mdi_bg_use_texture = checked;
    mainWin->mdiArea->useBackgroundTexture(checked);
}

void Settings_Dialog::chooseGeneralMdiBackgroundTexture()
{
    QPushButton* button = qobject_cast<QPushButton*>(sender());
    if (button) {
        QString selectedImage;
        selectedImage = QFileDialog::getOpenFileName(this, tr("Open File"),
          QStandardPaths::writableLocation(QStandardPaths::PicturesLocation),
                        tr("Images (*.bmp *.png *.jpg)"));

        if (!selectedImage.isNull()) {
            strcpy(accept_.general_mdi_bg_texture, selectedImage.toLocal8Bit().constData());
        }

        /*Update immediately so it can be previewed*/
        mainWin->mdiArea->setBackgroundTexture(accept_.general_mdi_bg_texture);
    }
}

void Settings_Dialog::checkBoxGeneralMdiBGUseColorStateChanged(int checked)
{
    preview.general_mdi_bg_use_color = checked;
    mainWin->mdiArea->useBackgroundColor(checked);
}

void Settings_Dialog::chooseGeneralMdiBackgroundColor()
{
    QPushButton* button = qobject_cast<QPushButton*>(sender());
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.general_mdi_bg_color), this);
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentGeneralMdiBackgroundColorChanged(const QColor&)));
        colorDialog->exec();

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.general_mdi_bg_color = colorDialog->selectedColor().rgb();
            QPixmap pix(16,16);
            pix.fill(QColor(accept_.general_mdi_bg_color));
            button->setIcon(QIcon(pix));
            mainWin->mdiArea->setBackgroundColor(QColor(accept_.general_mdi_bg_color));
        }
        else {
            mainWin->mdiArea->setBackgroundColor(QColor(dialog.general_mdi_bg_color));
        }
    }
}

void Settings_Dialog::currentGeneralMdiBackgroundColorChanged(const QColor& color)
{
    preview.general_mdi_bg_color = color.rgb();
    mainWin->mdiArea->setBackgroundColor(QColor(preview.general_mdi_bg_color));
}


/*
check_func(checkBoxTipOfTheDayStateChanged, general_tip_of_the_day)
check_func(checkBoxUseOpenGLStateChanged, display_use_opengl)
check_func(checkBoxRenderHintAAStateChanged, display_renderhint_aa)
check_func(checkBoxRenderHintTextAAStateChanged, display_renderhint_text_aa)
check_func(checkBoxRenderHintSmoothPixStateChanged, display_renderhint_smooth_pix)
check_func(checkBoxRenderHintHighAAStateChanged, display_renderhint_high_aa)
check_func(checkBoxRenderHintNonCosmeticStateChanged, display_renderhint_noncosmetic)
*/

void Settings_Dialog::checkBoxShowScrollBarsStateChanged(int checked)
{
    preview.display_show_scrollbars = checked;
    mainWin->updateAllViewScrollBars(preview.display_show_scrollbars);
}

void Settings_Dialog::spinBoxZoomScaleInValueChanged(double value)
{
    dialog.display_zoomscale_in = value;
}

void Settings_Dialog::spinBoxZoomScaleOutValueChanged(double value)
{
    dialog.display_zoomscale_out = value;
}

void Settings_Dialog::checkBoxDisableBGStateChanged(int checked)
{
    dialog.printing_disable_bg = checked;
}

void Settings_Dialog::chooseDisplayCrossHairColor()
{
    QPushButton* button = qobject_cast<QPushButton*>(sender());
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_crosshair_color), this);
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplayCrossHairColorChanged(const QColor&)));
        colorDialog->exec();

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.display_crosshair_color = colorDialog->selectedColor().rgb();
            QPixmap pix(16,16);
            pix.fill(QColor(accept_.display_crosshair_color));
            button->setIcon(QIcon(pix));
            mainWin->updateAllViewCrossHairColors(accept_.display_crosshair_color);
        }
        else {
            mainWin->updateAllViewCrossHairColors(dialog.display_crosshair_color);
        }
    }
}

void Settings_Dialog::currentDisplayCrossHairColorChanged(const QColor& color)
{
    preview.display_crosshair_color = color.rgb();
    mainWin->updateAllViewCrossHairColors(preview.display_crosshair_color);
}

void Settings_Dialog::chooseDisplayBackgroundColor()
{
    QPushButton* button = qobject_cast<QPushButton*>(sender());
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_bg_color), this);
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplayBackgroundColorChanged(const QColor&)));
        colorDialog->exec();

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.display_bg_color = colorDialog->selectedColor().rgb();
            QPixmap pix(16,16);
            pix.fill(QColor(accept_.display_bg_color));
            button->setIcon(QIcon(pix));
            mainWin->updateAllViewBackgroundColors(accept_.display_bg_color);
        }
        else {
            mainWin->updateAllViewBackgroundColors(dialog.display_bg_color);
        }
    }
}

void Settings_Dialog::currentDisplayBackgroundColorChanged(const QColor& color)
{
    preview.display_bg_color = color.rgb();
    mainWin->updateAllViewBackgroundColors(preview.display_bg_color);
}

void Settings_Dialog::chooseDisplaySelectBoxLeftColor()
{
    QPushButton* button = qobject_cast<QPushButton*>(sender());
    if(button)
    {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_selectbox_left_color), this);
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplaySelectBoxLeftColorChanged(const QColor&)));
        colorDialog->exec();

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.display_selectbox_left_color = colorDialog->selectedColor().rgb();
            QPixmap pix(16,16);
            pix.fill(QColor(accept_.display_selectbox_left_color));
            button->setIcon(QIcon(pix));
            mainWin->updateAllViewSelectBoxColors(accept_.display_selectbox_left_color,
                accept_.display_selectbox_left_fill,
                accept_.display_selectbox_right_color,
                accept_.display_selectbox_right_fill,
                preview.display_selectbox_alpha);
        }
        else
        {
            mainWin->updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                dialog.display_selectbox_left_fill,
                dialog.display_selectbox_right_color,
                dialog.display_selectbox_right_fill,
                                                  preview.display_selectbox_alpha);
        }
    }
}

void Settings_Dialog::currentDisplaySelectBoxLeftColorChanged(const QColor& color)
{
    preview.display_selectbox_left_color = color.rgb();
    mainWin->updateAllViewSelectBoxColors(preview.display_selectbox_left_color,
                                          preview.display_selectbox_left_fill,
                                          preview.display_selectbox_right_color,
                                          preview.display_selectbox_right_fill,
                                          preview.display_selectbox_alpha);
}

void Settings_Dialog::chooseDisplaySelectBoxLeftFill()
{
    QPushButton* button = qobject_cast<QPushButton*>(sender());
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_selectbox_left_fill), this);
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplaySelectBoxLeftFillChanged(const QColor&)));
        colorDialog->exec();

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.display_selectbox_left_fill = colorDialog->selectedColor().rgb();
            QPixmap pix(16,16);
            pix.fill(QColor(accept_.display_selectbox_left_fill));
            button->setIcon(QIcon(pix));
            mainWin->updateAllViewSelectBoxColors(
                accept_.display_selectbox_left_color,
                accept_.display_selectbox_left_fill,
                accept_.display_selectbox_right_color,
                accept_.display_selectbox_right_fill,
                preview.display_selectbox_alpha);
        }
        else {
            mainWin->updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                                                  dialog.display_selectbox_left_fill,
                                                  dialog.display_selectbox_right_color,
                                                  dialog.display_selectbox_right_fill,
                                                  preview.display_selectbox_alpha);
        }
    }
}

void Settings_Dialog::currentDisplaySelectBoxLeftFillChanged(const QColor& color)
{
    preview.display_selectbox_left_fill = color.rgb();
    mainWin->updateAllViewSelectBoxColors(preview.display_selectbox_left_color,
        preview.display_selectbox_left_fill,
        preview.display_selectbox_right_color,
        preview.display_selectbox_right_fill,
        preview.display_selectbox_alpha);
}

void Settings_Dialog::chooseDisplaySelectBoxRightColor()
{
    QPushButton* button = qobject_cast<QPushButton*>(sender());
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_selectbox_right_color), this);
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplaySelectBoxRightColorChanged(const QColor&)));
        colorDialog->exec();

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.display_selectbox_right_color = colorDialog->selectedColor().rgb();
            QPixmap pix(16,16);
            pix.fill(QColor(accept_.display_selectbox_right_color));
            button->setIcon(QIcon(pix));
            mainWin->updateAllViewSelectBoxColors(accept_.display_selectbox_left_color,
                                                  accept_.display_selectbox_left_fill,
                                                  accept_.display_selectbox_right_color,
                                                  accept_.display_selectbox_right_fill,
                                                  preview.display_selectbox_alpha);
        }
        else {
            mainWin->updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                                                  dialog.display_selectbox_left_fill,
                                                  dialog.display_selectbox_right_color,
                                                  dialog.display_selectbox_right_fill,
                                                  preview.display_selectbox_alpha);
        }
    }
}

void Settings_Dialog::currentDisplaySelectBoxRightColorChanged(const QColor& color)
{
    preview.display_selectbox_right_color = color.rgb();
    mainWin->updateAllViewSelectBoxColors(preview.display_selectbox_left_color,
        preview.display_selectbox_left_fill,
        preview.display_selectbox_right_color,
        preview.display_selectbox_right_fill,
        preview.display_selectbox_alpha);
}

void Settings_Dialog::chooseDisplaySelectBoxRightFill()
{
    QPushButton* button = qobject_cast<QPushButton*>(sender());
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_selectbox_right_fill), this);
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplaySelectBoxRightFillChanged(const QColor&)));
        colorDialog->exec();

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.display_selectbox_right_fill = colorDialog->selectedColor().rgb();
            QPixmap pix(16,16);
            pix.fill(QColor(accept_.display_selectbox_right_fill));
            button->setIcon(QIcon(pix));
            mainWin->updateAllViewSelectBoxColors(accept_.display_selectbox_left_color,
                 accept_.display_selectbox_left_fill,
                 accept_.display_selectbox_right_color,
                 accept_.display_selectbox_right_fill,
                 preview.display_selectbox_alpha);
        }
        else {
            mainWin->updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                                                  dialog.display_selectbox_left_fill,
                                                  dialog.display_selectbox_right_color,
                                                  dialog.display_selectbox_right_fill,
                                                  preview.display_selectbox_alpha);
        }
    }
}

void Settings_Dialog::currentDisplaySelectBoxRightFillChanged(const QColor& color)
{
    preview.display_selectbox_right_fill = color.rgb();
    mainWin->updateAllViewSelectBoxColors(preview.display_selectbox_left_color,
        preview.display_selectbox_left_fill,
        preview.display_selectbox_right_color,
        preview.display_selectbox_right_fill,
        preview.display_selectbox_alpha);
}

void Settings_Dialog::spinBoxDisplaySelectBoxAlphaValueChanged(int value)
{
    preview.display_selectbox_alpha = value;
    mainWin->updateAllViewSelectBoxColors(accept_.display_selectbox_left_color,
        accept_.display_selectbox_left_fill,
        accept_.display_selectbox_right_color,
        accept_.display_selectbox_right_fill,
        preview.display_selectbox_alpha);
}

void Settings_Dialog::checkBoxCustomFilterStateChanged(int checked)
{
    QCheckBox* checkBox = qobject_cast<QCheckBox*>(sender());
    if(checkBox)
    {
        QString format = checkBox->text();
        debug_message("CustomFilter: %s %d", qPrintable(format), checked);
        if(checked)
            opensave_custom_filter.append(" *." + format.toLower());
        else
            opensave_custom_filter.remove("*." + format, Qt::CaseInsensitive);
        /*dialog.opensave_custom_filter = checked; //TODO*/
    }
}

void Settings_Dialog::buttonCustomFilterSelectAllClicked()
{
    emit buttonCustomFilterSelectAll(1);
    opensave_custom_filter = "supported";
}

void Settings_Dialog::buttonCustomFilterClearAllClicked()
{
    emit buttonCustomFilterClearAll(0);
    opensave_custom_filter.clear();
}

void Settings_Dialog::checkBoxGridColorMatchCrossHairStateChanged(int checked)
{
    dialog.grid_color_match_crosshair = checked;
    if (dialog.grid_color_match_crosshair) {
        mainWin->updateAllViewGridColors(accept_.display_crosshair_color);
    }
    else {
        mainWin->updateAllViewGridColors(accept_.grid_color);
    }

    QObject* senderObj = sender();
    if (senderObj) {
        QObject* parent = senderObj->parent();
        if (parent) {
            QLabel* labelGridColor = parent->findChild<QLabel*>("labelGridColor");
            if (labelGridColor)
                labelGridColor->setEnabled(!dialog.grid_color_match_crosshair);
            QPushButton* buttonGridColor = parent->findChild<QPushButton*>("buttonGridColor");
            if (buttonGridColor)
                buttonGridColor->setEnabled(!dialog.grid_color_match_crosshair);
        }
    }
}

void Settings_Dialog::chooseGridColor()
{
    QPushButton* button = qobject_cast<QPushButton*>(sender());
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.grid_color), this);
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentGridColorChanged(const QColor&)));
        colorDialog->exec();

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.grid_color = colorDialog->selectedColor().rgb();
            QPixmap pix(16,16);
            pix.fill(QColor(accept_.grid_color));
            button->setIcon(QIcon(pix));
            mainWin->updateAllViewGridColors(accept_.grid_color);
        }
        else {
            mainWin->updateAllViewGridColors(dialog.grid_color);
        }
    }
}

void Settings_Dialog::currentGridColorChanged(const QColor& color)
{
    preview.grid_color = color.rgb();
    mainWin->updateAllViewGridColors(preview.grid_color);
}

void Settings_Dialog::checkBoxGridLoadFromFileStateChanged(int checked)
{
    dialog.grid_load_from_file = checked;

    QObject* senderObj = sender();
    if (senderObj) {
        QObject* parent = senderObj->parent();
        if (parent) {
            QLabel* labelGridType = parent->findChild<QLabel*>("labelGridType");
            if(labelGridType) labelGridType->setEnabled(!dialog.grid_load_from_file);
            QComboBox* comboBoxGridType = parent->findChild<QComboBox*>("comboBoxGridType");
            if(comboBoxGridType) comboBoxGridType->setEnabled(!dialog.grid_load_from_file);
            QCheckBox* checkBoxGridCenterOnOrigin = parent->findChild<QCheckBox*>("checkBoxGridCenterOnOrigin");
            if(checkBoxGridCenterOnOrigin) checkBoxGridCenterOnOrigin->setEnabled(!dialog.grid_load_from_file);
            QLabel* labelGridCenterX = parent->findChild<QLabel*>("labelGridCenterX");
            if(labelGridCenterX) labelGridCenterX->setEnabled(!dialog.grid_load_from_file && !dialog.grid_center_on_origin);
            QDoubleSpinBox* spinBoxGridCenterX = parent->findChild<QDoubleSpinBox*>("spinBoxGridCenterX");
            if(spinBoxGridCenterX) spinBoxGridCenterX->setEnabled(!dialog.grid_load_from_file && !dialog.grid_center_on_origin);
            QLabel* labelGridCenterY = parent->findChild<QLabel*>("labelGridCenterY");
            if(labelGridCenterY) labelGridCenterY->setEnabled(!dialog.grid_load_from_file && !dialog.grid_center_on_origin);
            QDoubleSpinBox* spinBoxGridCenterY = parent->findChild<QDoubleSpinBox*>("spinBoxGridCenterY");
            if(spinBoxGridCenterY) spinBoxGridCenterY->setEnabled(!dialog.grid_load_from_file && !dialog.grid_center_on_origin);
            QLabel* labelGridSizeX = parent->findChild<QLabel*>("labelGridSizeX");
            if(labelGridSizeX) labelGridSizeX->setEnabled(!dialog.grid_load_from_file);
            QDoubleSpinBox* spinBoxGridSizeX = parent->findChild<QDoubleSpinBox*>("spinBoxGridSizeX");
            if(spinBoxGridSizeX) spinBoxGridSizeX->setEnabled(!dialog.grid_load_from_file);
            QLabel* labelGridSizeY = parent->findChild<QLabel*>("labelGridSizeY");
            if(labelGridSizeY) labelGridSizeY->setEnabled(!dialog.grid_load_from_file);
            QDoubleSpinBox* spinBoxGridSizeY = parent->findChild<QDoubleSpinBox*>("spinBoxGridSizeY");
            if(spinBoxGridSizeY) spinBoxGridSizeY->setEnabled(!dialog.grid_load_from_file);
            QLabel* labelGridSpacingX = parent->findChild<QLabel*>("labelGridSpacingX");
            if(labelGridSpacingX) labelGridSpacingX->setEnabled(!dialog.grid_load_from_file);
            QDoubleSpinBox* spinBoxGridSpacingX = parent->findChild<QDoubleSpinBox*>("spinBoxGridSpacingX");
            if(spinBoxGridSpacingX) spinBoxGridSpacingX->setEnabled(!dialog.grid_load_from_file);
            QLabel* labelGridSpacingY = parent->findChild<QLabel*>("labelGridSpacingY");
            if(labelGridSpacingY) labelGridSpacingY->setEnabled(!dialog.grid_load_from_file);
            QDoubleSpinBox* spinBoxGridSpacingY = parent->findChild<QDoubleSpinBox*>("spinBoxGridSpacingY");
            if(spinBoxGridSpacingY) spinBoxGridSpacingY->setEnabled(!dialog.grid_load_from_file);
            QLabel* labelGridSizeRadius = parent->findChild<QLabel*>("labelGridSizeRadius");
            if(labelGridSizeRadius) labelGridSizeRadius->setEnabled(!dialog.grid_load_from_file);
            QDoubleSpinBox* spinBoxGridSizeRadius = parent->findChild<QDoubleSpinBox*>("spinBoxGridSizeRadius");
            if(spinBoxGridSizeRadius) spinBoxGridSizeRadius->setEnabled(!dialog.grid_load_from_file);
            QLabel* labelGridSpacingRadius = parent->findChild<QLabel*>("labelGridSpacingRadius");
            if (labelGridSpacingRadius) {
                labelGridSpacingRadius->setEnabled(!dialog.grid_load_from_file);
            }
            QDoubleSpinBox* spinBoxGridSpacingRadius = parent->findChild<QDoubleSpinBox*>("spinBoxGridSpacingRadius");
            if (spinBoxGridSpacingRadius) {
                spinBoxGridSpacingRadius->setEnabled(!dialog.grid_load_from_file);
            }
            QLabel* labelGridSpacingAngle = parent->findChild<QLabel*>("labelGridSpacingAngle");
            if (labelGridSpacingAngle) {
                labelGridSpacingAngle->setEnabled(!dialog.grid_load_from_file);
            }
            QDoubleSpinBox* spinBoxGridSpacingAngle = parent->findChild<QDoubleSpinBox*>("spinBoxGridSpacingAngle");
            if(spinBoxGridSpacingAngle) spinBoxGridSpacingAngle->setEnabled(!dialog.grid_load_from_file);
        }
    }
}

void Settings_Dialog::comboBoxGridTypeCurrentIndexChanged(const QString& type)
{
    strcpy(dialog.grid_type, type.toLocal8Bit().constData());

    QObject* senderObj = sender();
    if (senderObj) {
        QObject* parent = senderObj->parent();
        if (parent) {
            int visibility = 0;
            if(type == "Circular") visibility = 1;

            QLabel* labelGridSizeX = parent->findChild<QLabel*>("labelGridSizeX");
            if (labelGridSizeX) {
                labelGridSizeX->setVisible(!visibility);
            }
            QDoubleSpinBox* spinBoxGridSizeX = parent->findChild<QDoubleSpinBox*>("spinBoxGridSizeX");
            if (spinBoxGridSizeX) {
                spinBoxGridSizeX->setVisible(!visibility);
            }
            QLabel* labelGridSizeY = parent->findChild<QLabel*>("labelGridSizeY");
            if (labelGridSizeY) {
                labelGridSizeY->setVisible(!visibility);
            }
            QDoubleSpinBox* spinBoxGridSizeY = parent->findChild<QDoubleSpinBox*>("spinBoxGridSizeY");
            if (spinBoxGridSizeY) {
                spinBoxGridSizeY->setVisible(!visibility);
            }
            QLabel* labelGridSpacingX = parent->findChild<QLabel*>("labelGridSpacingX");
            if(labelGridSpacingX) labelGridSpacingX->setVisible(!visibility);
            QDoubleSpinBox* spinBoxGridSpacingX = parent->findChild<QDoubleSpinBox*>("spinBoxGridSpacingX");
            if(spinBoxGridSpacingX) spinBoxGridSpacingX->setVisible(!visibility);
            QLabel* labelGridSpacingY = parent->findChild<QLabel*>("labelGridSpacingY");
            if(labelGridSpacingY) labelGridSpacingY->setVisible(!visibility);
            QDoubleSpinBox* spinBoxGridSpacingY = parent->findChild<QDoubleSpinBox*>("spinBoxGridSpacingY");
            if(spinBoxGridSpacingY) spinBoxGridSpacingY->setVisible(!visibility);
            QLabel* labelGridSizeRadius = parent->findChild<QLabel*>("labelGridSizeRadius");
            if(labelGridSizeRadius) labelGridSizeRadius->setVisible(visibility);
            QDoubleSpinBox* spinBoxGridSizeRadius = parent->findChild<QDoubleSpinBox*>("spinBoxGridSizeRadius");
            if(spinBoxGridSizeRadius) spinBoxGridSizeRadius->setVisible(visibility);
            QLabel* labelGridSpacingRadius = parent->findChild<QLabel*>("labelGridSpacingRadius");
            if(labelGridSpacingRadius) labelGridSpacingRadius->setVisible(visibility);
            QDoubleSpinBox* spinBoxGridSpacingRadius = parent->findChild<QDoubleSpinBox*>("spinBoxGridSpacingRadius");
            if(spinBoxGridSpacingRadius) spinBoxGridSpacingRadius->setVisible(visibility);
            QLabel* labelGridSpacingAngle = parent->findChild<QLabel*>("labelGridSpacingAngle");
            if(labelGridSpacingAngle) labelGridSpacingAngle->setVisible(visibility);
            QDoubleSpinBox* spinBoxGridSpacingAngle = parent->findChild<QDoubleSpinBox*>("spinBoxGridSpacingAngle");
            if(spinBoxGridSpacingAngle) spinBoxGridSpacingAngle->setVisible(visibility);
        }
    }
}

void Settings_Dialog::checkBoxGridCenterOnOriginStateChanged(int checked)
{
    dialog.grid_center_on_origin = checked;

    QObject* senderObj = sender();
    if (senderObj) {
        QObject* parent = senderObj->parent();
        if (parent) {
            QLabel* labelGridCenterX = parent->findChild<QLabel*>("labelGridCenterX");
            if (labelGridCenterX) {
                labelGridCenterX->setEnabled(!dialog.grid_center_on_origin);
            }
            QDoubleSpinBox* spinBoxGridCenterX = parent->findChild<QDoubleSpinBox*>("spinBoxGridCenterX");
            if (spinBoxGridCenterX) {
                spinBoxGridCenterX->setEnabled(!dialog.grid_center_on_origin);
            }
            QLabel* labelGridCenterY = parent->findChild<QLabel*>("labelGridCenterY");
            if(labelGridCenterY) labelGridCenterY->setEnabled(!dialog.grid_center_on_origin);
            QDoubleSpinBox* spinBoxGridCenterY = parent->findChild<QDoubleSpinBox*>("spinBoxGridCenterY");
            if(spinBoxGridCenterY) spinBoxGridCenterY->setEnabled(!dialog.grid_center_on_origin);
        }
    }
}

void Settings_Dialog::comboBoxRulerMetricCurrentIndexChanged(int index)
{
    QComboBox* comboBox = qobject_cast<QComboBox*>(sender());
    if (comboBox) {
        int ok = 0;
        dialog.ruler_metric = comboBox->itemData(index).toBool();
    }
    else {
        dialog.ruler_metric = 1;
    }
}

void Settings_Dialog::chooseRulerColor()
{
    QPushButton* button = qobject_cast<QPushButton*>(sender());
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.ruler_color), this);
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentRulerColorChanged(const QColor&)));
        colorDialog->exec();

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.ruler_color = colorDialog->selectedColor().rgb();
            QPixmap pix(16,16);
            pix.fill(QColor(accept_.ruler_color));
            button->setIcon(QIcon(pix));
            mainWin->updateAllViewRulerColors(accept_.ruler_color);
        }
        else {
            mainWin->updateAllViewRulerColors(dialog.ruler_color);
        }
    }
}

void Settings_Dialog::currentRulerColorChanged(const QColor& color)
{
    preview.ruler_color = color.rgb();
    mainWin->updateAllViewRulerColors(preview.ruler_color);
}

void Settings_Dialog::buttonQSnapSelectAllClicked()
{
    emit buttonQSnapSelectAll(1);
}

void Settings_Dialog::buttonQSnapClearAllClicked()
{
    emit buttonQSnapClearAll(0);
}

/*
 * TODO:
 * Figure out how to abstract the slot in a way that it can be used for
 * comboBoxes in general
 * Currently comboBoxQSnapLocatorColorCurrentIndexChanged(int index)
 *        comboBoxSelectionCoolGripColorCurrentIndexChanged(int index)
 *        comboBoxSelectionHotGripColorCurrentIndexChanged(int index)
 * are all similar except the dialog. variable being worked on and the
 * QVariant.
 */

void Settings_Dialog::comboBoxQSnapLocatorColorCurrentIndexChanged(int index)
{
    /* TODO: Alert user if color matched the display bg color */
    QComboBox* comboBox = qobject_cast<QComboBox*>(sender());
    unsigned int defaultColor = qRgb(255,255,0); /* Yellow */
    if (comboBox) {
        bool ok = 0;
        dialog.qsnap_locator_color = comboBox->itemData(index).toUInt(&ok);
        if(!ok)
            dialog.qsnap_locator_color = defaultColor;
    }
    else {
        dialog.qsnap_locator_color = defaultColor;
    }
}

void Settings_Dialog::sliderQSnapLocatorSizeValueChanged(int value)
{
    dialog.qsnap_locator_size = value;
}

void Settings_Dialog::sliderQSnapApertureSizeValueChanged(int value)
{
    dialog.qsnap_aperture_size = value;
}

void Settings_Dialog::checkBoxLwtShowLwtStateChanged(int checked)
{
    preview.lwt_show_lwt = checked;
    if (preview.lwt_show_lwt) {
        enableLwt();
    }
    else {
        disableLwt();
    }

    QObject* senderObj = sender();
    if (senderObj) {
        QObject* parent = senderObj->parent();
        if (parent) {
            QCheckBox* checkBoxRealRender = parent->findChild<QCheckBox*>("checkBoxRealRender");
            if (checkBoxRealRender) {
                checkBoxRealRender->setEnabled(preview.lwt_show_lwt);
            }
        }
    }
}

void Settings_Dialog::checkBoxLwtRealRenderStateChanged(int checked)
{
    preview.lwt_real_render = checked;
    if (preview.lwt_real_render) {
        enableReal();
    }
    else {
        disableReal();
    }
}

void Settings_Dialog::comboBoxSelectionCoolGripColorCurrentIndexChanged(int index)
{
    /* TODO: Alert user if color matched the display bg color */
    QComboBox* comboBox = qobject_cast<QComboBox*>(sender());
    unsigned int defaultColor = qRgb(0,0,255); /*Blue*/
    if (comboBox) {
        bool ok = 0;
        dialog.selection_coolgrip_color = comboBox->itemData(index).toUInt(&ok);
        if(!ok)
            dialog.selection_coolgrip_color = defaultColor;
    }
    else {
        dialog.selection_coolgrip_color = defaultColor;
    }
}

void Settings_Dialog::comboBoxSelectionHotGripColorCurrentIndexChanged(int index)
{
    /* TODO: Alert user if color matched the display bg color */
    QComboBox* comboBox = qobject_cast<QComboBox*>(sender());
    unsigned int defaultColor = qRgb(255,0,0); /* Red */
    if (comboBox) {
        bool ok = 0;
        dialog.selection_hotgrip_color = comboBox->itemData(index).toUInt(&ok);
        if (!ok) {
            dialog.selection_hotgrip_color = defaultColor;
        }
    }
    else {
        dialog.selection_hotgrip_color = defaultColor;
    }
}

void Settings_Dialog::acceptChanges()
{
    dialog.general_mdi_bg_use_logo = preview.general_mdi_bg_use_logo;
    dialog.general_mdi_bg_use_texture = preview.general_mdi_bg_use_texture;
    dialog.general_mdi_bg_use_color = preview.general_mdi_bg_use_color;
    strcpy(dialog.general_mdi_bg_logo, accept_.general_mdi_bg_logo);
    strcpy(dialog.general_mdi_bg_texture, accept_.general_mdi_bg_texture);
    dialog.general_mdi_bg_color = accept_.general_mdi_bg_color;
    dialog.display_show_scrollbars = preview.display_show_scrollbars;
    dialog.display_crosshair_color = accept_.display_crosshair_color;
    dialog.display_bg_color = accept_.display_bg_color;
    dialog.display_selectbox_left_color = accept_.display_selectbox_left_color;
    dialog.display_selectbox_left_fill = accept_.display_selectbox_left_fill;
    dialog.display_selectbox_right_color = accept_.display_selectbox_right_color;
    dialog.display_selectbox_right_fill = accept_.display_selectbox_right_fill;
    dialog.display_selectbox_alpha = preview.display_selectbox_alpha;
    if (dialog.grid_color_match_crosshair) {
        dialog.grid_color = accept_.display_crosshair_color;
    }
    else {
        dialog.grid_color = accept_.grid_color;
    }
    dialog.ruler_color = accept_.ruler_color;
    dialog.lwt_show_lwt = preview.lwt_show_lwt;
    dialog.lwt_real_render = preview.lwt_real_render;

    strcpy(settings.general_language, dialog.general_language);
    strcpy(settings.general_icon_theme, dialog.general_icon_theme);
    settings.general_icon_size = dialog.general_icon_size;
    settings.general_mdi_bg_use_logo = dialog.general_mdi_bg_use_logo;
    settings.general_mdi_bg_use_texture = dialog.general_mdi_bg_use_texture;
    settings.general_mdi_bg_use_color = dialog.general_mdi_bg_use_color;
    strcpy(settings.general_mdi_bg_logo, dialog.general_mdi_bg_logo);
    strcpy(settings.general_mdi_bg_texture, dialog.general_mdi_bg_texture);
    settings.general_mdi_bg_color = dialog.general_mdi_bg_color;
    settings.general_tip_of_the_day = dialog.general_tip_of_the_day;
    /*TODO: settings.GeneralSystemHelpBrowser = dialog.general_system_help_browser;*/
    settings.display_use_opengl = dialog.display_use_opengl;
    settings.display_renderhint_aa = dialog.display_renderhint_aa;
    settings.display_renderhint_text_aa = dialog.display_renderhint_text_aa;
    settings.display_renderhint_smooth_pix = dialog.display_renderhint_smooth_pix;
    settings.display_renderhint_high_aa = dialog.display_renderhint_high_aa;
    settings.display_renderhint_noncosmetic = dialog.display_renderhint_noncosmetic;
    settings.display_show_scrollbars = dialog.display_show_scrollbars;
    settings.display_scrollbar_widget_num = dialog.display_scrollbar_widget_num;
    settings.display_crosshair_color = dialog.display_crosshair_color;
    settings.display_bg_color = dialog.display_bg_color;
    settings.display_selectbox_left_color = dialog.display_selectbox_left_color;
    settings.display_selectbox_left_fill = dialog.display_selectbox_left_fill;
    settings.display_selectbox_right_color = dialog.display_selectbox_right_color;
    settings.display_selectbox_right_fill = dialog.display_selectbox_right_fill;
    settings.display_selectbox_alpha = dialog.display_selectbox_alpha;
    settings.display_zoomscale_in = dialog.display_zoomscale_in;
    settings.display_zoomscale_out = dialog.display_zoomscale_out;
    /*TODO: settings.DisplayCrossHairPercent(dialog.display_crosshair_percent);*/
    /*TODO: settings.DisplayUnits(dialog.display_units);*/
    /*TODO: settings.PromptSaveHistoryFilename(dialog.prompt_save_history_filename);*/
    /*TODO: settings.open_format(dialog.opensave_open_format);*/
    /*TODO: settings.open_thumbnail(dialog.opensave_open_thumbnail);*/
    /*TODO: settings.save_format = dialog.opensave_save_format);*/
    /*TODO: settings.save_thumbnail = dialog.opensave_save_thumbnail);*/
    settings.opensave_recent_max_files = dialog.opensave_recent_max_files;
    settings.opensave_trim_dst_num_jumps = dialog.opensave_trim_dst_num_jumps;
    /*TODO: settings.PrintingDefaultDevice = dialog.printing_default_device;*/
    /*TODO: settings.PrintingUseLastDevice = dialog.printing_use_last_device;*/
    settings.printing_disable_bg = dialog.printing_disable_bg;
    settings.grid_show_on_load = dialog.grid_show_on_load;
    settings.grid_show_origin = dialog.grid_show_origin;
    settings.grid_color_match_crosshair = dialog.grid_color_match_crosshair;
    settings.grid_color = dialog.grid_color;
    /*TODO: settings.GridLoadFromFile = dialog.grid_load_from_file;*/
    strcpy(settings.grid_type, dialog.grid_type);
    settings.grid_center_on_origin = dialog.grid_center_on_origin;
    settings.grid_center = dialog.grid_center;
    settings.grid_size = dialog.grid_size;
    settings.grid_spacing = dialog.grid_spacing;
    settings.grid_size_radius = dialog.grid_size_radius;
    settings.grid_spacing_radius = dialog.grid_spacing_radius;
    settings.grid_spacing_angle = dialog.grid_spacing_angle;
    settings.ruler_show_on_load = dialog.ruler_show_on_load;
    settings.ruler_metric = dialog.ruler_metric;
    settings.ruler_color = dialog.ruler_color;
    settings.ruler_pixel_size = dialog.ruler_pixel_size;
    /*TODO: settings.qsnap_enabled = dialog.qsnap_enabled;*/
    settings.qsnap_locator_color = dialog.qsnap_locator_color;
    settings.qsnap_locator_size = dialog.qsnap_locator_size;
    settings.qsnap_aperture_size = dialog.qsnap_aperture_size;
    settings.qsnap_endpoint = dialog.qsnap_endpoint;
    settings.qsnap_midpoint = dialog.qsnap_midpoint;
    settings.qsnap_center = dialog.qsnap_center;
    settings.qsnap_node = dialog.qsnap_node;
    settings.qsnap_quadrant = dialog.qsnap_quadrant;
    settings.qsnap_intersection = dialog.qsnap_intersection;
    settings.qsnap_extension = dialog.qsnap_extension;
    settings.qsnap_insertion = dialog.qsnap_insertion;
    settings.qsnap_perpendicular = dialog.qsnap_perpendicular;
    settings.qsnap_tangent = dialog.qsnap_tangent;
    settings.qsnap_nearest = dialog.qsnap_nearest;
    settings.qsnap_apparent = dialog.qsnap_apparent;
    settings.qsnap_parallel = dialog.qsnap_parallel;
    settings.lwt_show_lwt = dialog.lwt_show_lwt;
    settings.lwt_real_render = dialog.lwt_real_render;
    settings.selection_mode_pickfirst = dialog.selection_mode_pickfirst;
    settings.selection_mode_pickadd = dialog.selection_mode_pickadd;
    settings.selection_mode_pickdrag = dialog.selection_mode_pickdrag;
    settings.selection_coolgrip_color = dialog.selection_coolgrip_color;
    settings.selection_hotgrip_color = dialog.selection_hotgrip_color;
    settings.selection_grip_size = dialog.selection_grip_size;
    settings.selection_pickbox_size = dialog.selection_pickbox_size;

    /*Make sure the user sees the changes applied immediately*/
    mainWin->mdiArea->useBackgroundLogo(dialog.general_mdi_bg_use_logo);
    mainWin->mdiArea->useBackgroundTexture(dialog.general_mdi_bg_use_texture);
    mainWin->mdiArea->useBackgroundColor(dialog.general_mdi_bg_use_color);
    mainWin->mdiArea->setBackgroundLogo(dialog.general_mdi_bg_logo);
    mainWin->mdiArea->setBackgroundTexture(dialog.general_mdi_bg_texture);
    mainWin->mdiArea->setBackgroundColor(dialog.general_mdi_bg_color);
    mainWin->iconResize(dialog.general_icon_size);
    mainWin->updateAllViewScrollBars(dialog.display_show_scrollbars);
    mainWin->updateAllViewCrossHairColors(dialog.display_crosshair_color);
    mainWin->updateAllViewBackgroundColors(dialog.display_bg_color);
    mainWin->updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                                          dialog.display_selectbox_left_fill,
                                          dialog.display_selectbox_right_color,
                                          dialog.display_selectbox_right_fill,
                                          dialog.display_selectbox_alpha);
    mainWin->updateAllViewGridColors(dialog.grid_color);
    mainWin->updateAllViewRulerColors(dialog.ruler_color);
    if (dialog.lwt_show_lwt) {
        enableLwt();
    }
    else { disableLwt(); }
    if (dialog.lwt_real_render) { enableReal(); }
    else { disableReal(); }
    mainWin->updatePickAddMode(dialog.selection_mode_pickadd);

    mainWin->writeSettings();
    accept();
}

void Settings_Dialog::rejectChanges()
{
    /*TODO: inform the user if they have changed settings*/

    /*Update the view since the user must accept the preview*/
    mainWin->mdiArea->useBackgroundLogo(dialog.general_mdi_bg_use_logo);
    mainWin->mdiArea->useBackgroundTexture(dialog.general_mdi_bg_use_texture);
    mainWin->mdiArea->useBackgroundColor(dialog.general_mdi_bg_use_color);
    mainWin->mdiArea->setBackgroundLogo(dialog.general_mdi_bg_logo);
    mainWin->mdiArea->setBackgroundTexture(dialog.general_mdi_bg_texture);
    mainWin->mdiArea->setBackgroundColor(dialog.general_mdi_bg_color);
    mainWin->updateAllViewScrollBars(dialog.display_show_scrollbars);
    mainWin->updateAllViewCrossHairColors(dialog.display_crosshair_color);
    mainWin->updateAllViewBackgroundColors(dialog.display_bg_color);
    mainWin->updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                                          dialog.display_selectbox_left_fill,
                                          dialog.display_selectbox_right_color,
                                          dialog.display_selectbox_right_fill,
                                          dialog.display_selectbox_alpha);
    mainWin->updateAllViewGridColors(dialog.grid_color);
    mainWin->updateAllViewRulerColors(dialog.ruler_color);
    if(dialog.lwt_show_lwt) { enableLwt(); }
    else                    { disableLwt(); }
    if(dialog.lwt_real_render) { enableReal(); }
    else                       { disableReal(); }

    reject();
}



PropertyEditor::PropertyEditor(const QString& iconDirectory, int pickAddMode, QWidget* widgetToFocus, QWidget* parent, Qt::WindowFlags flags) : QDockWidget(parent, flags)
{
    int i;
    iconDir = iconDirectory;
    iconSize = 16;
    propertyEditorButtonStyle = Qt::ToolButtonTextBesideIcon; /*TODO: Make customizable*/
    setMinimumSize(100,100);

    pickAdd = pickAddMode;

    precisionAngle = 0; /*TODO: Load this from settings and provide function for updating from settings*/
    precisionLength = 4; /*TODO: Load this from settings and provide function for updating from settings*/

    signalMapper = new QSignalMapper(this);

    fieldOldText = "";
    fieldNewText = "";
    fieldVariesText = "*Varies*";
    fieldYesText = "Yes";
    fieldNoText = "No";
    fieldOnText = "On";
    fieldOffText = "Off";

    QWidget* widgetMain = new QWidget(this);

    QWidget* widgetSelection = new QWidget(this);
    QHBoxLayout* hboxLayoutSelection = new QHBoxLayout(this);
    hboxLayoutSelection->addWidget(createComboBoxSelected());
    hboxLayoutSelection->addWidget(createToolButtonQSelect());
    hboxLayoutSelection->addWidget(createToolButtonPickAdd());
    widgetSelection->setLayout(hboxLayoutSelection);

    for (i=1; i<OBJ_TYPE_UNKNOWN-OBJ_TYPE_BASE; i++) {
        groupBoxGeometry[i] = createGroupBoxGeometry(i+OBJ_TYPE_BASE);
    }

    QScrollArea* scrollProperties = new QScrollArea(this);
    QWidget* widgetProperties = new QWidget(this);
    QVBoxLayout* vboxLayoutProperties = new QVBoxLayout(this);
    vboxLayoutProperties->addWidget(createGroupBoxGeneral());
    for (i=1; i<OBJ_TYPE_UNKNOWN-OBJ_TYPE_BASE; i++) {
        vboxLayoutProperties->addWidget(groupBoxGeometry[i+OBJ_TYPE_BASE]);
    }
    vboxLayoutProperties->addWidget(createGroupBoxMiscArc());
    vboxLayoutProperties->addWidget(createGroupBoxMiscImage());
    vboxLayoutProperties->addWidget(createGroupBoxMiscPath());
    vboxLayoutProperties->addWidget(createGroupBoxMiscPolyline());
    vboxLayoutProperties->addWidget(createGroupBoxTextTextSingle());
    vboxLayoutProperties->addWidget(createGroupBoxMiscTextSingle());
    vboxLayoutProperties->addStretch(1);
    widgetProperties->setLayout(vboxLayoutProperties);
    scrollProperties->setWidget(widgetProperties);
    scrollProperties->setWidgetResizable(1);

    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(this);
    vboxLayoutMain->addWidget(widgetSelection);
    vboxLayoutMain->addWidget(scrollProperties);
    widgetMain->setLayout(vboxLayoutMain);

    setWidget(widgetMain);
    setWindowTitle(tr("Properties"));
    setAllowedAreas(Qt::LeftDockWidgetArea | Qt::RightDockWidgetArea);

    hideAllGroups();

    connect(signalMapper, SIGNAL(mapped(QObject*)), this, SLOT(fieldEdited(QObject*)));

    focusWidget = widgetToFocus;
    this->installEventFilter(this);
}

PropertyEditor::~PropertyEditor()
{
}

bool PropertyEditor::eventFilter(QObject *obj, QEvent *event)
{
    if(event->type() == QEvent::KeyPress)
    {
        QKeyEvent* pressedKey = (QKeyEvent*)event;
        int key = pressedKey->key();
        switch(key)
        {
            case Qt::Key_Escape:
                if(focusWidget)
                    focusWidget->setFocus(Qt::OtherFocusReason);
                return 1;
                break;
            default:
                pressedKey->ignore();
        }
    }
    return QObject::eventFilter(obj, event);
}

QComboBox* PropertyEditor::createComboBoxSelected()
{
    comboBoxSelected = new QComboBox(this);
    comboBoxSelected->addItem(tr("No Selection"));
    return comboBoxSelected;
}

QToolButton* PropertyEditor::createToolButtonQSelect()
{
    toolButtonQSelect = new QToolButton(this);
    toolButtonQSelect->setIcon(loadIcon(icon_quickselect));
    toolButtonQSelect->setIconSize(QSize(iconSize, iconSize));
    toolButtonQSelect->setText("QSelect");
    toolButtonQSelect->setToolTip("QSelect"); /*TODO: Better Description*/
    toolButtonQSelect->setToolButtonStyle(Qt::ToolButtonIconOnly);
    return toolButtonQSelect;
}

QToolButton* PropertyEditor::createToolButtonPickAdd()
{
    /*TODO: Set as PickAdd or PickNew based on settings*/
    toolButtonPickAdd = new QToolButton(this);
    updatePickAddModeButton(pickAdd);
    connect(toolButtonPickAdd, SIGNAL(clicked(int)), this, SLOT(togglePickAddMode()));
    return toolButtonPickAdd;
}

void PropertyEditor::updatePickAddModeButton(int pickAddMode)
{
    pickAdd = pickAddMode;
    if (pickAdd) {
        toolButtonPickAdd->setIcon(loadIcon(icon_pickadd));
        toolButtonPickAdd->setIconSize(QSize(iconSize, iconSize));
        toolButtonPickAdd->setText("PickAdd");
        toolButtonPickAdd->setToolTip("PickAdd Mode - Add to current selection.\nClick to switch to PickNew Mode.");
        toolButtonPickAdd->setToolButtonStyle(Qt::ToolButtonIconOnly);
    }
    else {
        toolButtonPickAdd->setIcon(loadIcon(icon_picknew));
        toolButtonPickAdd->setIconSize(QSize(iconSize, iconSize));
        toolButtonPickAdd->setText("PickNew");
        toolButtonPickAdd->setToolTip("PickNew Mode - Replace current selection.\nClick to switch to PickAdd Mode.");
        toolButtonPickAdd->setToolButtonStyle(Qt::ToolButtonIconOnly);
    }
}

void PropertyEditor::togglePickAddMode()
{
    emit pickAddModeToggled();
}

void PropertyEditor::setSelectedItems(QList<QGraphicsItem*> itemList)
{
    selectedItemList = itemList;
    /*Hide all the groups initially, then decide which ones to show*/
    hideAllGroups();
    comboBoxSelected->clear();

    if(itemList.isEmpty())
    {
        comboBoxSelected->addItem(tr("No Selection"));
        return;
    }

    QSet<int> typeSet;

    int numObjects[31], i;

    int numAll = itemList.size();
    for (i=0; i<31; i++) {
        numObjects[i] = 0;
    }
    int numTypes = 0;

    foreach (QGraphicsItem* item, itemList) {
        if(!item) continue;

        int objType = item->type();
        typeSet.insert(objType);

        if (objType > OBJ_TYPE_BASE && objType < OBJ_TYPE_UNKNOWN) {
            if (numObjects[objType-OBJ_TYPE_BASE] == 0) {
                numTypes++;
            }
            numObjects[objType-OBJ_TYPE_BASE]++;
        }
        else {
            numObjects[OBJ_TYPE_UNKNOWN-OBJ_TYPE_BASE]++;
        }
    }

    /*==================================================*/
    /* Populate the selection comboBox*/
    /*==================================================*/
    if (numTypes > 1) {
        comboBoxSelected->addItem(tr("Varies") + " (" + QString().setNum(numAll) + ")");
        connect(comboBoxSelected, SIGNAL(currentIndexChanged(int)), this, SLOT(showOneType(int)));
    }

    for (i=0; i<31; i++) {
        if (numObjects[i] > 0) {
            QString comboBoxStr = tr(obj_names[i])
                + " (" + QString().setNum(numObjects[i]) + ")";
            comboBoxSelected->addItem(comboBoxStr, OBJ_TYPE_BASE+i);
        }
    }

    /* ==================================================
     * Load Data into the fields
     * ================================================== */

    /* Clear fields first so if the selected data varies, the comparison is simple */
    clearAllFields();

    foreach(QGraphicsItem* item, itemList) {
        if(!item) continue;

        /* TODO: load data into the General field */

        int objType = item->type();
        switch (objType) {
        case OBJ_TYPE_ARC:
            {
            ArcObject* obj = static_cast<ArcObject*>(item);
            if (obj) {
                QPointF p = obj->objectCenter();
                updateLineEditNumIfVaries(lineEdit[ARC_CENTER_X], p.x(), 0);
                updateLineEditNumIfVaries(lineEdit[ARC_CENTER_Y], -p.y(), 0);
                updateLineEditNumIfVaries(lineEdit[ARC_RADIUS], obj->objectRadius(), 0);
                updateLineEditNumIfVaries(lineEdit[ARC_START_ANGLE], obj->objectStartAngle(), 1);
                updateLineEditNumIfVaries(lineEdit[ARC_END_ANGLE], obj->objectEndAngle(), 1);
                updateLineEditNumIfVaries(lineEdit[ARC_START_X], obj->objectStartPoint().x(), 0);
                updateLineEditNumIfVaries(lineEdit[ARC_START_Y], -obj->objectStartPoint().y(), 0);
                updateLineEditNumIfVaries(lineEdit[ARC_END_X], obj->objectEndPoint().x(), 0);
                updateLineEditNumIfVaries(lineEdit[ARC_END_Y], -obj->objectEndPoint().y(), 0);
                updateLineEditNumIfVaries(lineEdit[ARC_AREA], obj->objectArea(), 0);
                updateLineEditNumIfVaries(lineEdit[ARC_LENGTH], obj->objectArcLength(), 0);
                updateLineEditNumIfVaries(lineEdit[ARC_CHORD], obj->objectChord(), 0);
                updateLineEditNumIfVaries(lineEdit[ARC_INC_ANGLE], obj->objectIncludedAngle(), 1);
                updateComboBoxintIfVaries(comboBox[ARC_CLOCKWISE], obj->objectClockwise(), 1);
            }
            }
            break;
        case OBJ_TYPE_BLOCK:
            {
            /*TODO: load block data*/
            }
            break;
        case OBJ_TYPE_CIRCLE:
            {
            CircleObject* obj = static_cast<CircleObject*>(item);
            if (obj) {
                QPointF p = obj->objectCenter();
                updateLineEditNumIfVaries(lineEdit[CIRCLE_CENTER_X], p.x(), 0);
                updateLineEditNumIfVaries(lineEdit[CIRCLE_CENTER_Y], -p.y(), 0);
                updateLineEditNumIfVaries(lineEdit[CIRCLE_RADIUS], obj->objectRadius(), 0);
                updateLineEditNumIfVaries(lineEdit[CIRCLE_DIAMETER], obj->objectDiameter(), 0);
                updateLineEditNumIfVaries(lineEdit[CIRCLE_AREA], obj->objectArea(), 0);
                updateLineEditNumIfVaries(lineEdit[CIRCLE_CIRCUMFERENCE], obj->objectCircumference(), 0);
            }
            }
            break;
        case OBJ_TYPE_DIMALIGNED:
            {
            /* TODO: load aligned dimension data */
            }
            break;
        case OBJ_TYPE_DIMANGULAR:
            {
            /* TODO: load angular dimension data */
            }
            break;
        case OBJ_TYPE_DIMARCLENGTH:
            {
            /* TODO: load arclength dimension data */
            }
            break;
        case OBJ_TYPE_DIMDIAMETER:
            {
            /* TODO: load diameter dimension data */
            }
            break;
        case OBJ_TYPE_DIMLEADER:
            {
            /* TODO: load leader dimension data */
            }
            break;
        case OBJ_TYPE_DIMLINEAR:
            {
            /* TODO: load linear dimension data */
            }
            break;
        case OBJ_TYPE_DIMORDINATE:
            {
            /* TODO: load ordinate dimension data */
            }
            break;
        case OBJ_TYPE_DIMRADIUS:
            {
            /* TODO: load radius dimension data */
            }
            break;
        case OBJ_TYPE_ELLIPSE:
            {
            EllipseObject* obj = static_cast<EllipseObject*>(item);
            if (obj) {
                QPointF p = obj->objectCenter();
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_CENTER_X], p.x(), 0);
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_CENTER_Y], -p.y(), 0);
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_RADIUS_MAJOR], obj->objectRadiusMajor(), 0);
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_RADIUS_MINOR], obj->objectRadiusMinor(), 0);
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_DIAMETER_MAJOR], obj->objectDiameterMajor(), 0);
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_DIAMETER_MINOR], obj->objectDiameterMinor(), 0);
            }
            }
            break;
        case OBJ_TYPE_IMAGE:
            {
            /*TODO: load image data*/
            }
            break;
        case OBJ_TYPE_INFINITELINE:
            {
            /* TODO: load infinite line data */
            }
            break;
        case OBJ_TYPE_LINE:
            {
            LineObject* obj = static_cast<LineObject*>(item);
            if (obj) {
                updateLineEditNumIfVaries(lineEdit[LINE_START_X], obj->objectEndPoint1().x(), 0);
                updateLineEditNumIfVaries(lineEdit[LINE_START_Y], -obj->objectEndPoint1().y(), 0);
                updateLineEditNumIfVaries(lineEdit[LINE_END_X], obj->objectEndPoint2().x(), 0);
                updateLineEditNumIfVaries(lineEdit[LINE_END_Y], -obj->objectEndPoint2().y(), 0);
                updateLineEditNumIfVaries(lineEdit[LINE_DELTA_X], obj->objectDeltaX(), 0);
                updateLineEditNumIfVaries(lineEdit[LINE_DELTA_Y], -obj->objectDeltaY(), 0);
                updateLineEditNumIfVaries(lineEdit[LINE_ANGLE], obj->objectAngle(), 1);
                updateLineEditNumIfVaries(lineEdit[LINE_LENGTH], obj->objectLength(), 0);
            }
            }
            break;
        case OBJ_TYPE_PATH:
        {
            /*TODO: load path data*/
        }
            break;
        case OBJ_TYPE_POINT:
            {
            PointObject* obj = static_cast<PointObject*>(item);
            if (obj) {
                updateLineEditNumIfVaries(lineEdit[POINT_X], obj->objectX(), 0);
                updateLineEditNumIfVaries(lineEdit[POINT_Y], -obj->objectY(), 0);
            }
            }
            break;
        case OBJ_TYPE_POLYGON:
            {
            /*TODO: load polygon data*/
            }
            break;
        case OBJ_TYPE_POLYLINE:
            {
            /*TODO: load polyline data*/
            }
            break;
        case OBJ_TYPE_RAY:
            {
            /*TODO: load ray data*/
            }
            break;
        case OBJ_TYPE_RECTANGLE:
            {
            RectObject* obj = static_cast<RectObject*>(item);
            if(obj) {
                QPointF corn1 = obj->objectTopLeft();
                QPointF corn2 = obj->objectTopRight();
                QPointF corn3 = obj->objectBottomLeft();
                QPointF corn4 = obj->objectBottomRight();

                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_X1], corn1.x(), 0);
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_Y1], -corn1.y(), 0);
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_X2], corn2.x(), 0);
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_Y2], -corn2.y(), 0);
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_X3], corn3.x(), 0);
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_Y3], -corn3.y(), 0);
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_X4], corn4.x(), 0);
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_Y4], -corn4.y(), 0);
                updateLineEditNumIfVaries(lineEdit[RECT_WIDTH], obj->objectWidth(), 0);
                updateLineEditNumIfVaries(lineEdit[RECT_HEIGHT], -obj->objectHeight(), 0);
                updateLineEditNumIfVaries(lineEdit[RECT_AREA], obj->objectArea(), 0);
            }
            }
            break;
        case OBJ_TYPE_TEXTMULTI:
            {
            /* TODO: load multiline text data */
            }
            break;
        case OBJ_TYPE_TEXTSINGLE:
            {
            TextSingleObject* obj = static_cast<TextSingleObject*>(item);
            if (obj) {
                updateLineEditStrIfVaries(lineEditTextSingleContents, obj->objText);
                updateFontComboBoxStrIfVaries(comboBoxTextSingleFont, obj->objTextFont);
                updateComboBoxStrIfVaries(comboBoxTextSingleJustify, obj->objTextJustify, obj->objectTextJustifyList());
                updateLineEditNumIfVaries(lineEditTextSingleHeight, obj->obj_text.size, 0);
                updateLineEditNumIfVaries(lineEditTextSingleRotation, -obj->rotation(), 1);
                updateLineEditNumIfVaries(lineEditTextSingleX, obj->objectX(), 0);
                updateLineEditNumIfVaries(lineEditTextSingleY, -obj->objectY(), 0);
                updateComboBoxintIfVaries(comboBoxTextSingleBackward, obj->obj_text.backward, 1);
                updateComboBoxintIfVaries(comboBoxTextSingleUpsideDown, obj->obj_text.upsidedown, 1);
            }
            }
            break;
        default:
            break;
        }
    }

    /*==================================================*/
    /* Only show fields if all objects are the same type*/
    /*==================================================*/
    if (numTypes == 1) {
        foreach (int objType, typeSet) {
            showGroups(objType);
        }
    }
}

void PropertyEditor::updateLineEditStrIfVaries(QLineEdit* lineEdit, const QString& str)
{
    fieldOldText = lineEdit->text();
    fieldNewText = str;

    if     (fieldOldText.isEmpty())       lineEdit->setText(fieldNewText);
    else if(fieldOldText != fieldNewText) lineEdit->setText(fieldVariesText);
}

void PropertyEditor::updateLineEditNumIfVaries(QLineEdit* lineEdit, float num, int useAnglePrecision)
{
    int precision = 0;
    if(useAnglePrecision) precision = precisionAngle;
    else                  precision = precisionLength;

    fieldOldText = lineEdit->text();
    fieldNewText.setNum(num, 'f', precision);

    /*Prevent negative zero :D*/
    QString negativeZero = "-0.";
    for(int i = 0; i < precision; ++i)
        negativeZero.append('0');
    if(fieldNewText == negativeZero)
        fieldNewText = negativeZero.replace("-", "");

    if     (fieldOldText.isEmpty())       lineEdit->setText(fieldNewText);
    else if(fieldOldText != fieldNewText) lineEdit->setText(fieldVariesText);
}

void PropertyEditor::updateFontComboBoxStrIfVaries(QFontComboBox* fontComboBox, const QString& str)
{
    fieldOldText = fontComboBox->property("FontFamily").toString();
    fieldNewText = str;
    /*debug_message("old: %d %s, new: %d %s", oldIndex, qPrintable(fontComboBox->currentText()), newIndex, qPrintable(str));*/
    if(fieldOldText.isEmpty())
    {
        fontComboBox->setCurrentFont(QFont(fieldNewText));
        fontComboBox->setProperty("FontFamily", fieldNewText);
    }
    else if(fieldOldText != fieldNewText)
    {
        if(fontComboBox->findText(fieldVariesText) == -1) /*Prevent multiple entries*/
            fontComboBox->addItem(fieldVariesText);
        fontComboBox->setCurrentIndex(fontComboBox->findText(fieldVariesText));
    }
}

void PropertyEditor::updateComboBoxStrIfVaries(QComboBox* comboBox, const QString& str, const QStringList& strList)
{
    fieldOldText = comboBox->currentText();
    fieldNewText = str;

    if(fieldOldText.isEmpty())
    {
        foreach(QString s, strList)
        {
            comboBox->addItem(s, s);
        }
        comboBox->setCurrentIndex(comboBox->findText(fieldNewText));
    }
    else if(fieldOldText != fieldNewText)
    {
        if(comboBox->findText(fieldVariesText) == -1) /*Prevent multiple entries*/
            comboBox->addItem(fieldVariesText);
        comboBox->setCurrentIndex(comboBox->findText(fieldVariesText));
    }
}

void PropertyEditor::updateComboBoxintIfVaries(QComboBox* comboBox, int val, int yesOrNoText)
{
    fieldOldText = comboBox->currentText();
    if(yesOrNoText)
    {
        if(val) fieldNewText = fieldYesText;
        else    fieldNewText = fieldNoText;
    }
    else
    {
        if(val) fieldNewText = fieldOnText;
        else    fieldNewText = fieldOffText;
    }

    if(fieldOldText.isEmpty()) {
        if (yesOrNoText) {
            comboBox->addItem(fieldYesText, 1);
            comboBox->addItem(fieldNoText, 0);
        }
        else {
            comboBox->addItem(fieldOnText, 1);
            comboBox->addItem(fieldOffText, 0);
        }
        comboBox->setCurrentIndex(comboBox->findText(fieldNewText));
    }
    else if(fieldOldText != fieldNewText) {
        /* Prevent multiple entries */
        if(comboBox->findText(fieldVariesText) == -1) {
            comboBox->addItem(fieldVariesText);
        }
        comboBox->setCurrentIndex(comboBox->findText(fieldVariesText));
    }
}

void PropertyEditor::showGroups(int objType)
{
    if (objType>=OBJ_TYPE_BASE && objType<OBJ_TYPE_UNKNOWN) {
        groupBoxGeometry[objType-OBJ_TYPE_BASE]->show();
    }
    if (objType == OBJ_TYPE_ARC) {
        groupBoxMiscArc->show();
    }
    else if(objType == OBJ_TYPE_IMAGE) {
        groupBoxMiscImage->show();
    }
    else if(objType == OBJ_TYPE_PATH) {
        groupBoxMiscPath->show();
    }
    else if(objType == OBJ_TYPE_POLYLINE) {
        groupBoxMiscPolyline->show();
    }
    else if(objType == OBJ_TYPE_TEXTSINGLE) {
        groupBoxTextTextSingle->show();
        groupBoxMiscTextSingle->show();
    }
}

void PropertyEditor::showOneType(int index)
{
    hideAllGroups();
    showGroups(comboBoxSelected->itemData(index).toInt());
}

void PropertyEditor::hideAllGroups()
{
    int i;
    /* NOTE: General group will never be hidden */
    for (i=1; i<OBJ_TYPE_UNKNOWN-OBJ_TYPE_BASE; i++) {
        groupBoxGeometry[i]->hide();
    }
    groupBoxMiscArc->hide();
    groupBoxMiscImage->hide();
    groupBoxMiscPath->hide();
    groupBoxMiscPolyline->hide();
    groupBoxTextTextSingle->hide();
    groupBoxMiscTextSingle->hide();
}

void PropertyEditor::clearAllFields()
{
    int i;
    for (i=0; i<COMBOBOX_PROPERTY_EDITORS; i++) {
        comboBox[i]->clear();
    }
    for (i=0; i<LINEEDIT_PROPERTY_EDITORS; i++) {
        lineEdit[i]->clear();
    }

    /* Text Single */
    comboBoxTextSingleFont->removeItem(comboBoxTextSingleFont->findText(fieldVariesText));
    /* NOTE: Do not clear comboBoxTextSingleFont */
    comboBoxTextSingleFont->setProperty("FontFamily", "");
}

QGroupBox* PropertyEditor::createGroupBoxGeneral()
{
    groupBoxGeneral = new QGroupBox(tr("General"), this);

    toolButtonGeneralLayer = createToolButton("blank", tr("Layer"));      /*TODO: use proper icon*/
    toolButtonGeneralColor = createToolButton("blank", tr("Color"));      /*TODO: use proper icon*/
    toolButtonGeneralLineType = createToolButton("blank", tr("LineType"));   /*TODO: use proper icon*/
    toolButtonGeneralLineWeight = createToolButton("blank", tr("LineWeight")); /*TODO: use proper icon*/

    comboBoxGeneralLayer = createComboBox(0);
    comboBoxGeneralColor = createComboBox(0);
    comboBoxGeneralLineType = createComboBox(0);
    comboBoxGeneralLineWeight = createComboBox(0);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonGeneralLayer, comboBoxGeneralLayer);
    formLayout->addRow(toolButtonGeneralColor, comboBoxGeneralColor);
    formLayout->addRow(toolButtonGeneralLineType, comboBoxGeneralLineType);
    formLayout->addRow(toolButtonGeneralLineWeight, comboBoxGeneralLineWeight);
    groupBoxGeneral->setLayout(formLayout);

    return groupBoxGeneral;
}

QGroupBox* PropertyEditor::createGroupBoxMiscArc()
{
    groupBoxMiscArc = new QGroupBox(tr("Misc"), this);

    toolButtonArcClockwise = createToolButton("blank", tr("Clockwise")); /*TODO: use proper icon*/

    comboBoxArcClockwise = createComboBox(1);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonArcClockwise, comboBoxArcClockwise);
    groupBoxMiscArc->setLayout(formLayout);

    return groupBoxMiscArc;
}

QGroupBox* PropertyEditor::createGroupBoxGeometry(int objType)
{
    int i;
    QGroupBox *gb = new QGroupBox(tr("Geometry"), this);

    /* TODO: use proper icons */
    QFormLayout* formLayout = new QFormLayout(this);
    /*
    for (i=0; property_editors[i].object != OBJ_TYPE_UNKNOWN; i++) {
        if (property_editors[i].object == objType) {
            int index = property_editors[i].id;
            toolButton[index] = createToolButton(property_editors[i].icon, tr(property_editors[i].label));       
            lineEdit[index] = createLineEdit(property_editors[i].type, property_editors[i].read_only);
            formLayout->addRow(toolButton[index], lineEdit[index]);
            mapSignal(lineEdit[index], property_editors[i].signal, objType);
        }
    }
    */
    gb->setLayout(formLayout);

    return gb;
}

QGroupBox* PropertyEditor::createGroupBoxMiscImage()
{
    groupBoxMiscImage = new QGroupBox(tr("Misc"), this);

    toolButtonImageName = createToolButton("blank", tr("Name")); /*TODO: use proper icon*/
    toolButtonImagePath = createToolButton("blank", tr("Path")); /*TODO: use proper icon*/

    lineEditImageName = createLineEdit("double", 1);
    lineEditImagePath = createLineEdit("double", 1);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonImageName, lineEditImageName);
    formLayout->addRow(toolButtonImagePath, lineEditImagePath);
    groupBoxMiscImage->setLayout(formLayout);

    return groupBoxMiscImage;
}

QGroupBox* PropertyEditor::createGroupBoxMiscPath()
{
    groupBoxMiscPath = new QGroupBox(tr("Misc"), this);

    toolButtonPathClosed = createToolButton("blank", tr("Closed")); /*TODO: use proper icon*/

    comboBoxPathClosed = createComboBox(0);

    /*TODO: mapSignal for paths*/

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonPathClosed, comboBoxPathClosed);
    groupBoxMiscPath->setLayout(formLayout);

    return groupBoxMiscPath;
}

QGroupBox* PropertyEditor::createGroupBoxMiscPolyline()
{
    groupBoxMiscPolyline = new QGroupBox(tr("Misc"), this);

    toolButtonPolylineClosed = createToolButton("blank", tr("Closed")); /*TODO: use proper icon*/

    comboBoxPolylineClosed = createComboBox(0);

    /*TODO: mapSignal for polylines*/

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonPolylineClosed, comboBoxPolylineClosed);
    groupBoxMiscPolyline->setLayout(formLayout);

    return groupBoxMiscPolyline;
}

QGroupBox* PropertyEditor::createGroupBoxTextTextSingle()
{
    groupBoxTextTextSingle = new QGroupBox(tr("Text"), this);

    toolButtonTextSingleContents = createToolButton("blank", tr("Contents")); /*TODO: use proper icon*/
    toolButtonTextSingleFont = createToolButton("blank", tr("Font"));     /*TODO: use proper icon*/
    toolButtonTextSingleJustify = createToolButton("blank", tr("Justify"));  /*TODO: use proper icon*/
    toolButtonTextSingleHeight = createToolButton("blank", tr("Height"));   /*TODO: use proper icon*/
    toolButtonTextSingleRotation = createToolButton("blank", tr("Rotation")); /*TODO: use proper icon*/

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

QGroupBox* PropertyEditor::createGroupBoxMiscTextSingle()
{
    groupBoxMiscTextSingle = new QGroupBox(tr("Misc"), this);

    toolButtonTextSingleBackward = createToolButton("blank", tr("Backward"));   /*TODO: use proper icon*/
    toolButtonTextSingleUpsideDown = createToolButton("blank", tr("UpsideDown")); /*TODO: use proper icon*/

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

QToolButton* PropertyEditor::createToolButton(const QString& iconName, const QString& txt)
{
    QToolButton* tb = new QToolButton(this);
    tb->setIcon(loadIcon(icon_blank));
    tb->setIconSize(QSize(iconSize, iconSize));
    tb->setText(txt);
    tb->setToolButtonStyle(propertyEditorButtonStyle);
    tb->setStyleSheet("border:none;");
    return tb;
}

QLineEdit* PropertyEditor::createLineEdit(const QString& validatorType, int readOnly)
{
    QLineEdit* le = new QLineEdit(this);
    if (validatorType == "int") {
        le->setValidator(new QIntValidator(le));
    }
    else if (validatorType == "double") {
        le->setValidator(new QDoubleValidator(le));
    }
    le->setReadOnly(readOnly);
    return le;
}

QComboBox* PropertyEditor::createComboBox(int disable)
{
    QComboBox* cb = new QComboBox(this);
    cb->setDisabled(disable);
    return cb;
}

QFontComboBox* PropertyEditor::createFontComboBox(int disable)
{
    QFontComboBox* fcb = new QFontComboBox(this);
    fcb->setDisabled(disable);
    return fcb;
}

void PropertyEditor::mapSignal(QObject* fieldObj, const QString& name, QVariant value)
{
    fieldObj->setObjectName(name);
    fieldObj->setProperty(qPrintable(name), value);

    if (name.startsWith("lineEdit")) {
        connect(fieldObj, SIGNAL(editingFinished()), signalMapper, SLOT(map()));
    }
    else if (name.startsWith("comboBox")) {
        connect(fieldObj, SIGNAL(activated(const QString&)), signalMapper, SLOT(map()));
    }

    signalMapper->setMapping(fieldObj, fieldObj);
}

void PropertyEditor::fieldEdited(QObject* fieldObj)
{
    ArcObject*  tempArcObj;
    CircleObject*   tempCircleObj;
    EllipseObject*  tempEllipseObj;
    ImageObject*    tempImageObj;
    LineObject* tempLineObj;
    PathObject* tempPathObj;
    PointObject*    tempPointObj;
    PolygonObject*  tempPolygonObj;
    PolylineObject* tempPolylineObj;
    RectObject* tempRectObj;
    TextSingleObject*   tempTextSingleObj;

    static int blockSignals = 0;
    if(blockSignals) return;

    debug_message("==========Field was Edited==========");
    QString objName = fieldObj->objectName();
    int objType = fieldObj->property(qPrintable(objName)).toInt();

    foreach(QGraphicsItem* item, selectedItemList)
    {
        if(item->type() != objType) continue;

        switch(objType)
        {
            case OBJ_TYPE_ARC:
                if(objName == "lineEditArcCenterX") {
                    tempArcObj = static_cast<ArcObject*>(item);
                    if (tempArcObj) {
                        QPointF p = tempArcObj->objectCenter();
                        p.setX(lineEdit[ARC_CENTER_X]->text().toDouble());
                        tempArcObj->setPos(p);
                    }
                }
                if(objName == "lineEditArcCenterY") {
                    tempArcObj = static_cast<ArcObject*>(item);
                    if (tempArcObj) {
                        QPointF p = tempArcObj->objectCenter();
                        p.setY(lineEdit[ARC_CENTER_Y]->text().toDouble());
                        tempArcObj->setPos(p);
                    }
                }
                if(objName == "lineEditArcRadius") {
                    tempArcObj = static_cast<ArcObject*>(item);
                    if (tempArcObj) {
                        tempArcObj->setObjectRadius(lineEdit[ARC_RADIUS]->text().toDouble());
                    }
                }
                if(objName == "lineEditArcStartAngle") {
                    tempArcObj = static_cast<ArcObject*>(item);
                    if (tempArcObj) {
                        tempArcObj->setObjectStartAngle(lineEdit[ARC_START_ANGLE]->text().toDouble());
                    }
                }
                if(objName == "lineEditArcEndAngle") {
                    tempArcObj = static_cast<ArcObject*>(item);
                    if (tempArcObj) {
                        tempArcObj->setObjectEndAngle(lineEdit[ARC_END_ANGLE]->text().toDouble());
                    }
                }
                break;
            case OBJ_TYPE_BLOCK: /*TODO: field editing*/
                break;
            case OBJ_TYPE_CIRCLE:
                if(objName == "lineEditCircleCenterX") {
                    tempCircleObj = static_cast<CircleObject*>(item);
                    if (tempCircleObj) {
                        QPointF p = tempCircleObj->objectCenter();
                        p.setX(lineEdit[CIRCLE_CENTER_X]->text().toDouble());
                        tempCircleObj->setPos(p);
                    }
                }
                if(objName == "lineEditCircleCenterY") {
                    tempCircleObj = static_cast<CircleObject*>(item);
                    if (tempCircleObj) {
                        QPointF p = tempCircleObj->objectCenter();
                        p.setY(lineEdit[CIRCLE_CENTER_Y]->text().toDouble());
                        tempCircleObj->setPos(p);
                    }
                }
                if(objName == "lineEditCircleRadius") {
                    tempCircleObj = static_cast<CircleObject*>(item);
                    if (tempCircleObj) {
                        tempCircleObj->setObjectRadius(lineEdit[CIRCLE_RADIUS]->text().toDouble());
                    }
                }
                if(objName == "lineEditCircleDiameter") {
                    tempCircleObj = static_cast<CircleObject*>(item);
                    if (tempCircleObj) {
                        tempCircleObj->setObjectDiameter(lineEdit[CIRCLE_DIAMETER]->text().toDouble());
                    }
                }
                if(objName == "lineEditCircleArea") {
                    tempCircleObj = static_cast<CircleObject*>(item);
                    if(tempCircleObj) { tempCircleObj->setObjectArea(lineEdit[CIRCLE_AREA]->text().toDouble()); }
                }
                if(objName == "lineEditCircleCircumference") {
                    tempCircleObj = static_cast<CircleObject*>(item);
                    if (tempCircleObj) {
                        tempCircleObj->setObjectCircumference(lineEdit[CIRCLE_CIRCUMFERENCE]->text().toDouble());
                    }
                }
                break;
            case OBJ_TYPE_DIMALIGNED: /*TODO: field editing*/
                break;
            case OBJ_TYPE_DIMANGULAR: /*TODO: field editing*/
                break;
            case OBJ_TYPE_DIMARCLENGTH: /*TODO: field editing*/
                break;
            case OBJ_TYPE_DIMDIAMETER: /*TODO: field editing*/
                break;
            case OBJ_TYPE_DIMLEADER: /*TODO: field editing*/
                break;
            case OBJ_TYPE_DIMLINEAR: /*TODO: field editing*/
                break;
            case OBJ_TYPE_DIMORDINATE: /*TODO: field editing*/
                break;
            case OBJ_TYPE_DIMRADIUS: /*TODO: field editing*/
                break;
            case OBJ_TYPE_ELLIPSE:
                if(objName == "lineEditEllipseCenterX") {
                    tempEllipseObj = static_cast<EllipseObject*>(item);
                    if (tempEllipseObj) {
                        QPointF p = tempCircleObj->objectCenter();
                        p.setX(lineEdit[ELLIPSE_CENTER_X]->text().toDouble());
                        tempCircleObj->setPos(p);
                    }
                }
                if(objName == "lineEditEllipseCenterY") {
                    tempEllipseObj = static_cast<EllipseObject*>(item);
                    if (tempEllipseObj) {
                        QPointF p = tempCircleObj->objectCenter();
                        p.setY(lineEdit[ELLIPSE_CENTER_Y]->text().toDouble());
                        tempCircleObj->setPos(p);
                    }
                }
                if(objName == "lineEditEllipseRadiusMajor") {
                    tempEllipseObj = static_cast<EllipseObject*>(item);
                    if (tempEllipseObj) {
                        tempEllipseObj->setObjectRadiusMajor(lineEdit[ELLIPSE_RADIUS_MAJOR]->text().toDouble());
                    }
                }
                if(objName == "lineEditEllipseRadiusMinor") {
                    tempEllipseObj = static_cast<EllipseObject*>(item);
                    if (tempEllipseObj) {
                        tempEllipseObj->setObjectRadiusMinor(lineEdit[ELLIPSE_RADIUS_MINOR]->text().toDouble());
                    }
                }
                if(objName == "lineEditEllipseDiameterMajor") {
                    tempEllipseObj = static_cast<EllipseObject*>(item);
                    if (tempEllipseObj) {
                        tempEllipseObj->setObjectDiameterMajor(lineEdit[ELLIPSE_DIAMETER_MAJOR]->text().toDouble());
                    }
                }
                if(objName == "lineEditEllipseDiameterMinor") {
                    tempEllipseObj = static_cast<EllipseObject*>(item);
                    if (tempEllipseObj) {
                        tempEllipseObj->setObjectDiameterMinor(lineEdit[ELLIPSE_DIAMETER_MINOR]->text().toDouble());
                    }
                }
                break;
            case OBJ_TYPE_IMAGE: /*TODO: field editing*/
                break;
            case OBJ_TYPE_INFINITELINE: /*TODO: field editing*/
                break;
            case OBJ_TYPE_LINE:
                if(objName == "lineEditLineStartX") {
                    tempLineObj = static_cast<LineObject*>(item);
                    if (tempLineObj) {
                        tempLineObj->setObjectX1(lineEdit[LINE_START_X]->text().toDouble());
                    }
                }
                if(objName == "lineEditLineStartY") {
                    tempLineObj = static_cast<LineObject*>(item);
                    if (tempLineObj) {
                        tempLineObj->setObjectY1(-lineEdit[LINE_START_Y]->text().toDouble());
                    }
                }
                if(objName == "lineEditLineEndX") {
                    tempLineObj = static_cast<LineObject*>(item);
                    if (tempLineObj) {
                        tempLineObj->setObjectX2(lineEdit[LINE_END_X]->text().toDouble());
                    }
                }
                if(objName == "lineEditLineEndY") {
                    tempLineObj = static_cast<LineObject*>(item);
                    if (tempLineObj) {
                        tempLineObj->setObjectY2(-lineEdit[LINE_END_Y]->text().toDouble());
                    }
                }
                break;
            case OBJ_TYPE_PATH: /*TODO: field editing*/
                break;
            case OBJ_TYPE_POINT:
                if(objName == "lineEditPointX") {
                    tempPointObj = static_cast<PointObject*>(item);
                    if (tempPointObj) {
                        tempPointObj->setObjectX(lineEdit[POINT_X]->text().toDouble());
                    }
                }
                if(objName == "lineEditPointY") {
                    tempPointObj = static_cast<PointObject*>(item);
                    if (tempPointObj) {
                        tempPointObj->setObjectY(-lineEdit[POINT_Y]->text().toDouble());
                    }
                }
                break;
            case OBJ_TYPE_POLYGON: /*TODO: field editing*/
                break;
            case OBJ_TYPE_POLYLINE: /*TODO: field editing*/
                break;
            case OBJ_TYPE_RAY: /*TODO: field editing*/
                break;
            case OBJ_TYPE_RECTANGLE: /*TODO: field editing*/
                break;
            case OBJ_TYPE_TEXTMULTI: /*TODO: field editing*/
                break;
            case OBJ_TYPE_TEXTSINGLE: /*TODO: field editing*/
                if(objName == "lineEditTextSingleContents") {
                    tempTextSingleObj = static_cast<TextSingleObject*>(item);
                    if (tempTextSingleObj) {
                        tempTextSingleObj->setObjectText(lineEditTextSingleContents->text());
                    }
                }
                if(objName == "comboBoxTextSingleFont") {
                    if(comboBoxTextSingleFont->currentText() == fieldVariesText) { break; }
                    tempTextSingleObj = static_cast<TextSingleObject*>(item);
                    if(tempTextSingleObj) { tempTextSingleObj->setObjectTextFont(comboBoxTextSingleFont->currentFont().family()); } }
                if (objName == "comboBoxTextSingleJustify") {
                    if (comboBoxTextSingleJustify->currentText() == fieldVariesText) {
                        break;
                    }
                    tempTextSingleObj = static_cast<TextSingleObject*>(item);
                    if (tempTextSingleObj) {
                        tempTextSingleObj->setObjectTextJustify(comboBoxTextSingleJustify->itemData(comboBoxTextSingleJustify->currentIndex()).toString());
                    }
                }
                if(objName == "lineEditTextSingleHeight") {
                    tempTextSingleObj = static_cast<TextSingleObject*>(item);
                    if (tempTextSingleObj) {
                        tempTextSingleObj->setObjectTextSize(lineEditTextSingleHeight->text().toDouble());
                    }
                }
                if(objName == "lineEditTextSingleRotation") {
                    tempTextSingleObj = static_cast<TextSingleObject*>(item);
                    if (tempTextSingleObj) {
                        tempTextSingleObj->setRotation(-lineEditTextSingleRotation->text().toDouble());
                    }
                }
                if(objName == "lineEditTextSingleX") {
                    tempTextSingleObj = static_cast<TextSingleObject*>(item);
                    if(tempTextSingleObj) { tempTextSingleObj->setObjectX(lineEditTextSingleX->text().toDouble()); } }
                if(objName == "lineEditTextSingleY") {
                    tempTextSingleObj = static_cast<TextSingleObject*>(item);
                    if(tempTextSingleObj) { tempTextSingleObj->setObjectY(lineEditTextSingleY->text().toDouble()); } }
                if(objName == "comboBoxTextSingleBackward") {
                    if(comboBoxTextSingleBackward->currentText() == fieldVariesText) { break; }
                    tempTextSingleObj = static_cast<TextSingleObject*>(item);
                    if(tempTextSingleObj) { tempTextSingleObj->setObjectTextBackward(comboBoxTextSingleBackward->itemData(comboBoxTextSingleBackward->currentIndex()).toBool()); } }
                if(objName == "comboBoxTextSingleUpsideDown") {
                    if(comboBoxTextSingleUpsideDown->currentText() == fieldVariesText) { break; }
                    tempTextSingleObj = static_cast<TextSingleObject*>(item);
                    if(tempTextSingleObj) { tempTextSingleObj->setObjectTextUpsideDown(comboBoxTextSingleUpsideDown->itemData(comboBoxTextSingleUpsideDown->currentIndex()).toBool()); } }
                break;
            default:
                break;
        }

    }

    /*Block this slot from running twice since calling setSelectedItems will trigger it*/
    blockSignals = 1;

    QWidget* widget = QApplication::focusWidget();
    /* Update so all fields have fresh data
     * TODO: Improve this
     */
    setSelectedItems(selectedItemList);
    hideAllGroups();
    showGroups(objType);

    if(widget) widget->setFocus(Qt::OtherFocusReason);

    blockSignals = 0;
}

ArcObject::ArcObject(float startX, float startY, float midX, float midY, float endX, float endY, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("ArcObject Constructor()");
    init(startX, startY, midX, midY, endX, endY, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

ArcObject::ArcObject(ArcObject* obj, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("ArcObject Constructor()");
    if(obj)
    {
        init(obj->objectStartPoint().x(), obj->objectStartPoint().y(), obj->objectMidPoint().x(), obj->objectMidPoint().y(), obj->objectEndPoint().x(), obj->objectEndPoint().y(), obj->objectColorRGB(), Qt::SolidLine);
        /* TODO: getCurrentLineType */
        setRotation(obj->rotation());
    }
}

ArcObject::~ArcObject()
{
    debug_message("ArcObject Destructor()");
}

void ArcObject::init(float startX, float startY, float midX, float midY, float endX, float endY, unsigned int rgb, Qt::PenStyle lineType)
{
    setData(OBJ_TYPE, type());
    setData(OBJ_NAME, obj_names[OBJ_TYPE_ARC]);

    setFlag(QGraphicsItem::ItemIsSelectable, 1);

    calculateArcData(startX, startY, midX, midY, endX, endY);

    setObjectColor(rgb);
    setObjectLineType(lineType);
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objPen);
}

void ArcObject::calculateArcData(float startX, float startY, float midX, float midY, float endX, float endY)
{
    EmbArc arc = embArcObject_make(startX, startY,
                 midX, midY,
                 endX, endY).arc;
    EmbVector center;
    getArcCenter(arc, &center);
    arcStartPoint = QPointF(startX - center.x, startY - center.y);
    arcMidPoint = QPointF(midX   - center.x, midY   - center.y);
    arcEndPoint = QPointF(endX   - center.x, endY   - center.y);

    setPos(center.x, center.y);

    float radius = QLineF(center.x, center.y, midX, midY).length();
    updateArcRect(radius);
    updatePath();
    setRotation(0);
    setScale(1);
}

void ArcObject::updateArcRect(float radius)
{
    QRectF arcRect;
    arcRect.setWidth(radius*2.0);
    arcRect.setHeight(radius*2.0);
    arcRect.moveCenter(QPointF(0,0));
    setRect(arcRect);
}

void ArcObject::setObjectRadius(float radius)
{
    if (radius <= 0) {
        radius = 0.0000001;
    }

    QPointF center = scenePos();
    QLineF startLine = QLineF(center, objectStartPoint());
    QLineF midLine = QLineF(center, objectMidPoint());
    QLineF endLine = QLineF(center, objectEndPoint());
    startLine.setLength(radius);
    midLine.setLength(radius);
    endLine.setLength(radius);
    arcStartPoint = startLine.p2();
    arcMidPoint = midLine.p2();
    arcEndPoint = endLine.p2();

    calculateArcData(arcStartPoint.x(), arcStartPoint.y(), arcMidPoint.x(), arcMidPoint.y(), arcEndPoint.x(), arcEndPoint.y());
}

void ArcObject::setObjectStartAngle(float angle)
{
    /*TODO: ArcObject setObjectStartAngle*/
}

void ArcObject::setObjectEndAngle(float angle)
{
    /*TODO: ArcObject setObjectEndAngle*/
}

void ArcObject::setObjectStartPoint(float pointX, float pointY)
{
    calculateArcData(pointX, pointY, arcMidPoint.x(), arcMidPoint.y(), arcEndPoint.x(), arcEndPoint.y());
}

void ArcObject::setObjectMidPoint(const QPointF& point)
{
    setObjectMidPoint(point.x(), point.y());
}

void ArcObject::setObjectMidPoint(float pointX, float pointY)
{
    calculateArcData(arcStartPoint.x(), arcStartPoint.y(), pointX, pointY, arcEndPoint.x(), arcEndPoint.y());
}

void ArcObject::setObjectEndPoint(const QPointF& point)
{
    setObjectEndPoint(point.x(), point.y());
}

void ArcObject::setObjectEndPoint(float pointX, float pointY)
{
    calculateArcData(arcStartPoint.x(), arcStartPoint.y(), arcMidPoint.x(), arcMidPoint.y(), pointX, pointY);
}

float ArcObject::objectStartAngle() const
{
    float angle = QLineF(scenePos(), objectStartPoint()).angle();
    return fmod(angle, 360.0);
}

float ArcObject::objectEndAngle() const
{
    float angle = QLineF(scenePos(), objectEndPoint()).angle();
    return fmod(angle, 360.0);
}

QPointF ArcObject::objectStartPoint() const
{
    EmbVector v = to_emb_vector(arcStartPoint);
    EmbVector rot = scale_and_rotate(v, scale(), radians(rotation()));

    return scenePos() + to_qpointf(rot);
}

QPointF ArcObject::objectMidPoint() const
{
    EmbVector v = to_emb_vector(arcMidPoint);
    EmbVector rot = scale_and_rotate(v, scale(), radians(rotation()));

    return scenePos() + to_qpointf(rot);
}

QPointF ArcObject::objectEndPoint() const
{
    EmbVector v = to_emb_vector(arcEndPoint);
    EmbVector rot = scale_and_rotate(v, scale(), radians(rotation()));

    return scenePos() + to_qpointf(rot);
}

float ArcObject::objectArea() const
{
    /*Area of a circular segment*/
    float r = objectRadius();
    float theta = radians(objectIncludedAngle());
    return ((r*r)/2)*(theta - sin(theta));
}

float ArcObject::objectArcLength() const
{
    return radians(objectIncludedAngle())*objectRadius();
}

float ArcObject::objectChord() const
{
    return QLineF(objectStartPoint().x(), objectStartPoint().y(), objectEndPoint().x(), objectEndPoint().y()).length();
}

float ArcObject::objectIncludedAngle() const
{
    float chord = objectChord();
    float rad = objectRadius();
    if(chord <= 0 || rad <= 0) return 0;
    /* Prevents division by zero and non-existent circles */

    /* NOTE:
     * Due to floating point rounding errors, we need to clamp the
     * quotient so it is in the range [-1, 1].
     * If the quotient is out of that range, then the result of asin()
     * will be NaN.
     */
    float quotient = chord/(2.0*rad);
    if(quotient > 1.0) quotient = 1.0;
    if(quotient < 0.0) quotient = 0.0;
    /* NOTE: 0 rather than -1 since we are enforcing a positive chord
     * and radius.
     */
    return degrees(2.0*asin(quotient));
    /* Properties of a Circle - Get the Included Angle - Reference: ASD9 */
}

int ArcObject::objectClockwise() const
{
    EmbVector start = to_emb_vector(objectStartPoint());
    EmbVector mid = to_emb_vector(objectMidPoint());
    EmbVector end = to_emb_vector(objectEndPoint());
    EmbArc arc = embArcObject_make(start.x, -start.y, mid.x, -mid.y, end.x, -end.y).arc;
    /* NOTE: Y values are inverted here on purpose */
    return isArcClockwise(arc);
}

void ArcObject::updatePath()
{
    float startAngle = (objectStartAngle() + rotation());
    float spanAngle = objectIncludedAngle();

    if(objectClockwise())
        spanAngle = -spanAngle;

    QPainterPath path;
    path.arcMoveTo(rect(), startAngle);
    path.arcTo(rect(), startAngle, spanAngle);
    /*NOTE: Reverse the path so that the inside area isn't considered part of the arc*/
    path.arcTo(rect(), startAngle+spanAngle, -spanAngle);
    setObjectPath(path);
}

void ArcObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/)
{
    QGraphicsScene* objScene = scene();
    if(!objScene) return;

    QPen paintPen = pen();
    painter->setPen(paintPen);
    updateRubber(painter);
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen);

    float startAngle = (objectStartAngle() + rotation())*16;
    float spanAngle = objectIncludedAngle()*16;

    if(objectClockwise())
        spanAngle = -spanAngle;

    float rad = objectRadius();
    QRectF paintRect(-rad, -rad, rad*2.0, rad*2.0);
    painter->drawArc(paintRect, startAngle, spanAngle);
}

void ArcObject::updateRubber(QPainter* painter)
{
    /*TODO: Arc Rubber Modes*/

    /*TODO: updateRubber() gripping for ArcObject*/

}

void ArcObject::vulcanize()
{
    debug_message("ArcObject vulcanize()");
    updateRubber();

    setObjectRubberMode(OBJ_RUBBER_OFF);
}

/* Returns the closest snap point to the mouse point*/
QPointF ArcObject::mouseSnapPoint(const QPointF& mousePoint)
{
    QPointF center = objectCenter();
    QPointF start = objectStartPoint();
    QPointF mid = objectMidPoint();
    QPointF end = objectEndPoint();

    float cntrDist = QLineF(mousePoint, center).length();
    float startDist = QLineF(mousePoint, start).length();
    float midDist = QLineF(mousePoint, mid).length();
    float endDist = QLineF(mousePoint, end).length();

    float minDist = qMin(qMin(cntrDist, startDist), qMin(midDist, endDist));

    if     (minDist == cntrDist)  return center;
    else if(minDist == startDist) return start;
    else if(minDist == midDist)   return mid;
    else if(minDist == endDist)   return end;

    return scenePos();
}

QList<QPointF> ArcObject::allGripPoints()
{
    QList<QPointF> gripPoints;
    gripPoints << objectCenter() << objectStartPoint() << objectMidPoint() << objectEndPoint();
    return gripPoints;
}

void ArcObject::gripEdit(const QPointF& before, const QPointF& after)
{
    /*TODO: gripEdit() for ArcObject*/
}


BaseObject::BaseObject(QGraphicsItem* parent) : QGraphicsPathItem(parent)
{
    debug_message("BaseObject Constructor()");

    objPen.setCapStyle(Qt::RoundCap);
    objPen.setJoinStyle(Qt::RoundJoin);
    lwtPen.setCapStyle(Qt::RoundCap);
    lwtPen.setJoinStyle(Qt::RoundJoin);

    objID = QDateTime::currentMSecsSinceEpoch();
}

BaseObject::~BaseObject()
{
    debug_message("BaseObject Destructor()");
}

void BaseObject::setObjectColor(const QColor& color)
{
    objPen.setColor(color);
    lwtPen.setColor(color);
}

void BaseObject::setObjectColorRGB(unsigned int rgb)
{
    objPen.setColor(QColor(rgb));
    lwtPen.setColor(QColor(rgb));
}

void BaseObject::setObjectLineType(Qt::PenStyle lineType)
{
    objPen.setStyle(lineType);
    lwtPen.setStyle(lineType);
}

void BaseObject::setObjectLineWeight(float lineWeight)
{
    objPen.setWidthF(0); /*NOTE: The objPen will always be cosmetic*/

    if(lineWeight < 0)
    {
        if(lineWeight == OBJ_LWT_BYLAYER)
        {
            lwtPen.setWidthF(0.35); /*TODO: getLayerLineWeight*/
        }
        else if(lineWeight == OBJ_LWT_BYBLOCK)
        {
            lwtPen.setWidthF(0.35); /*TODO: getBlockLineWeight*/
        }
        else
        {
            QMessageBox::warning(0, QObject::tr("Error - Negative Lineweight"),
                                    QObject::tr("Lineweight: %1")
                                    .arg(QString().setNum(lineWeight)));
            debug_message("Lineweight cannot be negative! Inverting sign.");
            lwtPen.setWidthF(-lineWeight);
        }
    }
    else
    {
        lwtPen.setWidthF(lineWeight);
    }
}

QPointF BaseObject::objectRubberPoint(const QString& key) const
{
    if(objRubberPoints.contains(key))
        return objRubberPoints.value(key);

    QGraphicsScene* gscene = scene();
    if(gscene)
        return scene()->property("SCENE_QSNAP_POINT").toPointF();
    return QPointF();
}

QString BaseObject::objectRubberText(const QString& key) const
{
    if(objRubberTexts.contains(key))
        return objRubberTexts.value(key);
    return QString();
}

QRectF BaseObject::boundingRect() const
{
    /*If gripped, force this object to be drawn even if it is offscreen*/
    if(objectRubberMode() == OBJ_RUBBER_GRIP)
        return scene()->sceneRect();
    return path().boundingRect();
}

void BaseObject::drawRubberLine(const QLineF& rubLine, QPainter* painter, const char* colorFromScene)
{
    if(painter)
    {
        QGraphicsScene* objScene = scene();
        if(!objScene) return;
        QPen colorPen = objPen;
        colorPen.setColor(QColor(objScene->property(colorFromScene).toUInt()));
        painter->setPen(colorPen);
        painter->drawLine(rubLine);
        painter->setPen(objPen);
    }
}

void BaseObject::realRender(QPainter* painter, const QPainterPath& renderPath)
{
    QColor color1 = objectColor();       /*lighter color*/
    QColor color2 = color1.darker(150); /*darker color*/

    /*If we have a dark color, lighten it*/
    int darkness = color1.lightness();
    int threshold = 32;
    /*TODO: This number may need adjusted or maybe just add it to settings.*/
    if (darkness < threshold) {
        color2 = color1;
        if (!darkness) {
            color1 = QColor(threshold, threshold, threshold);
        } /*lighter() does not affect pure black*/
        else {
            color1 = color2.lighter(100 + threshold);
        }
    }

    int count = renderPath.elementCount();
    for(int i = 0; i < count-1; ++i)
    {
        QPainterPath::Element elem = renderPath.elementAt(i);
        QPainterPath::Element next = renderPath.elementAt(i+1);

        if(next.isMoveTo()) continue;

        QPainterPath elemPath;
        elemPath.moveTo(elem.x, elem.y);
        elemPath.lineTo(next.x, next.y);

        QPen renderPen(QColor(0,0,0,0));
        renderPen.setWidthF(0);
        painter->setPen(renderPen);
        QPainterPathStroker stroker;
        stroker.setWidth(0.35);
        stroker.setCapStyle(Qt::RoundCap);
        stroker.setJoinStyle(Qt::RoundJoin);
        QPainterPath realPath = stroker.createStroke(elemPath);
        painter->drawPath(realPath);

        QLinearGradient grad(elemPath.pointAtPercent(0.5), elemPath.pointAtPercent(0.0));
        grad.setColorAt(0, color1);
        grad.setColorAt(1, color2);
        grad.setSpread(QGradient::ReflectSpread);

        painter->fillPath(realPath, QBrush(grad));
    }
}


CircleObject::CircleObject(float centerX, float centerY, float radius, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("CircleObject Constructor()");
    init(centerX, centerY, radius, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

CircleObject::CircleObject(CircleObject* obj, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("CircleObject Constructor()");
    if(obj)
    {
        QPointF p = obj->objectCenter();
        float r = obj->objectRadius();
        init(p.x(), p.y(), r, obj->objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setRotation(obj->rotation());
    }
}

CircleObject::~CircleObject()
{
    debug_message("CircleObject Destructor()");
}

void CircleObject::init(float centerX, float centerY, float radius, unsigned int rgb, Qt::PenStyle lineType)
{
    setData(OBJ_TYPE, type());
    setData(OBJ_NAME, obj_names[OBJ_TYPE_CIRCLE]);

    setFlag(QGraphicsItem::ItemIsSelectable, 1);

    setObjectRadius(radius);
    setPos(centerX, centerY);
    setObjectColor(rgb);
    setObjectLineType(lineType);
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objPen);
    updatePath();
}

void CircleObject::setObjectRadius(float radius)
{
    setObjectDiameter(radius*2.0);
}

void CircleObject::setObjectDiameter(float diameter)
{
    QRectF circRect;
    circRect.setWidth(diameter);
    circRect.setHeight(diameter);
    circRect.moveCenter(QPointF(0,0));
    setRect(circRect);
    updatePath();
}

void CircleObject::setObjectArea(float area)
{
    float radius = sqrt(area/embConstantPi);
    setObjectRadius(radius);
}

void CircleObject::setObjectCircumference(float circumference)
{
    float diameter = circumference/embConstantPi;
    setObjectDiameter(diameter);
}

void CircleObject::updatePath()
{
    QPainterPath path;
    QRectF r = rect();
    /* Add the center point */
    path.addRect(-0.00000001, -0.00000001, 0.00000002, 0.00000002);
    /* Add the circle */
    path.arcMoveTo(r, 0);
    path.arcTo(r, 0, 360);
    /* NOTE: Reverse the path so that the inside area isn't considered part of the circle. */
    path.arcTo(r, 0, -360);
    setObjectPath(path);
}

void CircleObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/)
{
    QGraphicsScene* objScene = scene();
    if(!objScene) return;

    QPen paintPen = pen();
    painter->setPen(paintPen);
    updateRubber(painter);
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen);

    painter->drawEllipse(rect());
}

void CircleObject::updateRubber(QPainter* painter)
{
    int rubberMode = objectRubberMode();
    if(rubberMode == OBJ_RUBBER_CIRCLE_1P_RAD)
    {
        QPointF sceneCenterPoint = objectRubberPoint("CIRCLE_CENTER");
        QPointF sceneQSnapPoint = objectRubberPoint("CIRCLE_RADIUS");
        QPointF itemCenterPoint = mapFromScene(sceneCenterPoint);
        QPointF itemQSnapPoint = mapFromScene(sceneQSnapPoint);
        QLineF itemLine(itemCenterPoint, itemQSnapPoint);
        setPos(sceneCenterPoint);
        QLineF sceneLine(sceneCenterPoint, sceneQSnapPoint);
        float radius = sceneLine.length();
        setObjectRadius(radius);
        if(painter) drawRubberLine(itemLine, painter, "VIEW_COLOR_CROSSHAIR");
        updatePath();
    }
    else if(rubberMode == OBJ_RUBBER_CIRCLE_1P_DIA)
    {
        QPointF sceneCenterPoint = objectRubberPoint("CIRCLE_CENTER");
        QPointF sceneQSnapPoint = objectRubberPoint("CIRCLE_DIAMETER");
        QPointF itemCenterPoint = mapFromScene(sceneCenterPoint);
        QPointF itemQSnapPoint = mapFromScene(sceneQSnapPoint);
        QLineF itemLine(itemCenterPoint, itemQSnapPoint);
        setPos(sceneCenterPoint);
        QLineF sceneLine(sceneCenterPoint, sceneQSnapPoint);
        float diameter = sceneLine.length();
        setObjectDiameter(diameter);
        if(painter) drawRubberLine(itemLine, painter, "VIEW_COLOR_CROSSHAIR");
        updatePath();
    }
    else if(rubberMode == OBJ_RUBBER_CIRCLE_2P)
    {
        QPointF sceneTan1Point = objectRubberPoint("CIRCLE_TAN1");
        QPointF sceneQSnapPoint = objectRubberPoint("CIRCLE_TAN2");
        QLineF sceneLine(sceneTan1Point, sceneQSnapPoint);
        setPos(sceneLine.pointAt(0.5));
        float diameter = sceneLine.length();
        setObjectDiameter(diameter);
        updatePath();
    }
    else if(rubberMode == OBJ_RUBBER_CIRCLE_3P)
    {
        QPointF sceneTan1Point = objectRubberPoint("CIRCLE_TAN1");
        QPointF sceneTan2Point = objectRubberPoint("CIRCLE_TAN2");
        QPointF sceneTan3Point = objectRubberPoint("CIRCLE_TAN3");

        EmbVector sceneCenter;
        EmbArc arc = embArcObject_make(sceneTan1Point.x(), sceneTan1Point.y(),
                             sceneTan2Point.x(), sceneTan2Point.y(),
                             sceneTan3Point.x(), sceneTan3Point.y()).arc;
        getArcCenter(arc, &sceneCenter);
        QPointF sceneCenterPoint(sceneCenter.x, sceneCenter.y);
        QLineF sceneLine(sceneCenterPoint, sceneTan3Point);
        setPos(sceneCenterPoint);
        float radius = sceneLine.length();
        setObjectRadius(radius);
        updatePath();
    }
    else if(rubberMode == OBJ_RUBBER_GRIP)
    {
        if(painter)
        {
            QPointF gripPoint = objectRubberPoint("GRIP_POINT");
            if(gripPoint == objectCenter())
            {
                painter->drawEllipse(rect().translated(mapFromScene(objectRubberPoint(QString()))-mapFromScene(gripPoint)));
            }
            else
            {
                float gripRadius = QLineF(objectCenter(), objectRubberPoint(QString())).length();
                painter->drawEllipse(QPointF(), gripRadius, gripRadius);
            }

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())));
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR");
        }
    }
}

void CircleObject::vulcanize()
{
    debug_message("CircleObject vulcanize()");
    updateRubber();

    setObjectRubberMode(OBJ_RUBBER_OFF);
}

/* Returns the closest snap point to the mouse point */
QPointF CircleObject::mouseSnapPoint(const QPointF& mousePoint)
{
    QPointF center = objectCenter();
    QPointF quad0 = objectQuadrant0();
    QPointF quad90 = objectQuadrant90();
    QPointF quad180 = objectQuadrant180();
    QPointF quad270 = objectQuadrant270();

    float cntrDist = QLineF(mousePoint, center).length();
    float q0Dist = QLineF(mousePoint, quad0).length();
    float q90Dist = QLineF(mousePoint, quad90).length();
    float q180Dist = QLineF(mousePoint, quad180).length();
    float q270Dist = QLineF(mousePoint, quad270).length();

    float minDist = qMin(qMin(qMin(q0Dist, q90Dist), qMin(q180Dist, q270Dist)), cntrDist);

    if     (minDist == cntrDist) return center;
    else if(minDist == q0Dist)   return quad0;
    else if(minDist == q90Dist)  return quad90;
    else if(minDist == q180Dist) return quad180;
    else if(minDist == q270Dist) return quad270;

    return scenePos();
}

QList<QPointF> CircleObject::allGripPoints()
{
    QList<QPointF> gripPoints;
    gripPoints << objectCenter() << objectQuadrant0() << objectQuadrant90() << objectQuadrant180() << objectQuadrant270();
    return gripPoints;
}

void CircleObject::gripEdit(const QPointF& before, const QPointF& after)
{
    if(before == objectCenter()) { QPointF delta = after-before; moveBy(delta.x(), delta.y()); }
    else                         { setObjectRadius(QLineF(objectCenter(), after).length()); }
}

QPainterPath CircleObject::objectSavePath() const
{
    QPainterPath path;
    QRectF r = rect();
    path.arcMoveTo(r, 0);
    path.arcTo(r, 0, 360);

    float s = scale();
    QTransform trans;
    trans.rotate(rotation());
    trans.scale(s,s);
    return trans.map(path);
}

DimLeaderObject::DimLeaderObject(float x1, float y1, float x2, float y2, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("DimLeaderObject Constructor()");
    init(x1, y1, x2, y2, rgb, Qt::SolidLine); /* TODO: getCurrentLineType */
}

DimLeaderObject::DimLeaderObject(DimLeaderObject* obj, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("DimLeaderObject Constructor()");
    if (obj) {
        EmbVector v1, v2;
        v1 = to_emb_vector(obj->objectEndPoint1());
        v2 = to_emb_vector(obj->objectEndPoint2());
        init(v1.x, v1.y, v2.x, v2.y, obj->objectColorRGB(), Qt::SolidLine);
        /* TODO: getCurrentLineType */
    }
}

DimLeaderObject::~DimLeaderObject()
{
    debug_message("DimLeaderObject Destructor()");
}

void DimLeaderObject::init(float x1, float y1, float x2, float y2, unsigned int rgb, Qt::PenStyle lineType)
{
    setData(OBJ_TYPE, type());
    setData(OBJ_NAME, obj_names[OBJ_TYPE_DIMLEADER]);

    setFlag(QGraphicsItem::ItemIsSelectable, 1);

    curved = 0;
    filled = 1;
    setObjectEndPoint1(to_emb_vector(QPointF(x1, y1)));
    setObjectEndPoint2(to_emb_vector(QPointF(x2, y2)));
    setObjectColor(rgb);
    setObjectLineType(lineType);
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objectPen());
}

void DimLeaderObject::setObjectEndPoint1(EmbVector p1)
{
    EmbVector diff;
    QPointF endPt2 = objectEndPoint2();
    float x2 = endPt2.x();
    float y2 = endPt2.y();
    diff.x = x2 - p1.x;
    diff.y = y2 - p1.y;
    setRotation(0);
    setLine(0, 0, diff.x, diff.y);
    setPos(p1.x, p1.y);
    updateLeader();
}

void DimLeaderObject::setObjectEndPoint2(EmbVector p2)
{
    EmbVector endPt1 = to_emb_vector(scenePos());
    setRotation(0);
    setLine(0, 0, p2.x - endPt1.x, p2.y - endPt1.y);
    setPos(endPt1.x, endPt1.y);
    updateLeader();
}

QPointF DimLeaderObject::objectEndPoint1() const
{
    return scenePos();
}

QPointF DimLeaderObject::objectEndPoint2() const
{
    EmbVector v;
    v.x = line().x2();
    v.y = line().y2();
    v = scale_and_rotate(v, scale(), radians(rotation()));

    return scenePos() + to_qpointf(v);
}

QPointF DimLeaderObject::objectMidPoint() const
{
    EmbVector v;
    v = to_emb_vector(line().pointAt(0.5));
    v = scale_and_rotate(v, scale(), radians(rotation()));

    return scenePos() + to_qpointf(v);
}

float DimLeaderObject::objectAngle() const
{
    float angle = line().angle() - rotation();
    return fmod(angle, 360.0);
}

void DimLeaderObject::updateLeader()
{
    int arrowStyle = Closed; /*TODO: Make this customizable*/
    float arrowStyleAngle = 15.0; /*TODO: Make this customizable*/
    float arrowStyleLength = 1.0; /*TODO: Make this customizable*/
    float lineStyleAngle = 45.0; /*TODO: Make this customizable*/
    float lineStyleLength = 1.0; /*TODO: Make this customizable*/

    QLineF lyne = line();
    float angle = lyne.angle();
    QPointF ap0 = lyne.p1();
    QPointF lp0 = lyne.p2();

    /*Arrow*/
    QLineF lynePerp(lyne.pointAt(arrowStyleLength/lyne.length()) ,lp0);
    lynePerp.setAngle(angle + 90);
    QLineF lyne1(ap0, lp0);
    QLineF lyne2(ap0, lp0);
    lyne1.setAngle(angle + arrowStyleAngle);
    lyne2.setAngle(angle - arrowStyleAngle);
    QPointF ap1;
    QPointF ap2;
    /* HACK: these need fixing
    lynePerp.intersects(lyne1, &ap1);
    lynePerp.intersects(lyne2, &ap2);
    */
    /* So they don't cause memory access problems */
    ap1 = lyne1.p1();
    ap2 = lyne2.p1();

    /* Math Diagram
     *                 .(ap1)                     .(lp1)
     *                /|                         /|
     *               / |                        / |
     *              /  |                       /  |
     *             /   |                      /   |
     *            /    |                     /    |
     *           /     |                    /     |
     *          /      |                   /      |
     *         /       |                  /       |
     *        /+(aSA)  |                 /+(lSA)  |
     * (ap0)./__(aSL)__|__________(lp0)./__(lSL)__|
     *       \ -(aSA)  |                \ -(lSA)  |
     *        \        |                 \        |
     *         \       |                  \       |
     *          \      |                   \      |
     *           \     |                    \     |
     *            \    |                     \    |
     *             \   |                      \   |
     *              \  |                       \  |
     *               \ |                        \ |
     *                \|                         \|
     *                 .(ap2)                     .(lp2)
     */

    if(arrowStyle == Open)
    {
        arrowStylePath = QPainterPath();
        arrowStylePath.moveTo(ap1);
        arrowStylePath.lineTo(ap0);
        arrowStylePath.lineTo(ap2);
        arrowStylePath.lineTo(ap0);
        arrowStylePath.lineTo(ap1);
    }
    else if(arrowStyle == Closed)
    {
        arrowStylePath = QPainterPath();
        arrowStylePath.moveTo(ap1);
        arrowStylePath.lineTo(ap0);
        arrowStylePath.lineTo(ap2);
        arrowStylePath.lineTo(ap1);
    }
    else if(arrowStyle == Dot)
    {
        arrowStylePath = QPainterPath();
        arrowStylePath.addEllipse(ap0, arrowStyleLength, arrowStyleLength);
    }
    else if(arrowStyle == Box)
    {
        arrowStylePath = QPainterPath();
        float side = QLineF(ap1, ap2).length();
        QRectF ar0(0, 0, side, side);
        ar0.moveCenter(ap0);
        arrowStylePath.addRect(ar0);
    }
    else if(arrowStyle == Tick)
    {
    }

    lineStylePath = QPainterPath();
    lineStylePath.moveTo(ap0);
    lineStylePath.lineTo(lp0);
}

void DimLeaderObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/)
{
    QGraphicsScene* objScene = scene();
    if(!objScene) return;

    QPen paintPen = pen();
    painter->setPen(paintPen);
    updateRubber(painter);
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen);

    painter->drawPath(lineStylePath);
    painter->drawPath(arrowStylePath);

    if(filled)
        painter->fillPath(arrowStylePath, objectColor());
}

void DimLeaderObject::updateRubber(QPainter* painter)
{
    int rubberMode = objectRubberMode();
    if(rubberMode == OBJ_RUBBER_DIMLEADER_LINE)
    {
        QPointF sceneStartPoint = objectRubberPoint("DIMLEADER_LINE_START");
        QPointF sceneQSnapPoint = objectRubberPoint("DIMLEADER_LINE_END");

        setObjectEndPoint1(to_emb_vector(sceneStartPoint));
        setObjectEndPoint2(to_emb_vector(sceneQSnapPoint));
    }
    else if(rubberMode == OBJ_RUBBER_GRIP)
    {
        if(painter)
        {
            QPointF gripPoint = objectRubberPoint("GRIP_POINT");
            if     (gripPoint == objectEndPoint1()) painter->drawLine(line().p2(), mapFromScene(objectRubberPoint(QString())));
            else if(gripPoint == objectEndPoint2()) painter->drawLine(line().p1(), mapFromScene(objectRubberPoint(QString())));
            else if(gripPoint == objectMidPoint())  painter->drawLine(line().translated(mapFromScene(objectRubberPoint(QString()))-mapFromScene(gripPoint)));
        }
    }
}

void DimLeaderObject::vulcanize()
{
    debug_message("DimLeaderObject vulcanize()");
    updateRubber();

    setObjectRubberMode(OBJ_RUBBER_OFF);
}

/* Returns the closest snap point to the mouse point. */
QPointF DimLeaderObject::mouseSnapPoint(const QPointF& mousePoint)
{
    QPointF endPoint1 = objectEndPoint1();
    QPointF endPoint2 = objectEndPoint2();
    QPointF midPoint = objectMidPoint();

    float end1Dist = QLineF(mousePoint, endPoint1).length();
    float end2Dist = QLineF(mousePoint, endPoint2).length();
    float midDist = QLineF(mousePoint, midPoint).length();

    float minDist = qMin(end1Dist, end2Dist);

    if(curved)
        minDist = qMin(minDist, midDist);

    if     (minDist == end1Dist) return endPoint1;
    else if(minDist == end2Dist) return endPoint2;
    else if(minDist == midDist)  return midPoint;

    return scenePos();
}

QList<QPointF> DimLeaderObject::allGripPoints()
{
    QList<QPointF> gripPoints;
    gripPoints << objectEndPoint1() << objectEndPoint2();
    if(curved)
        gripPoints << objectMidPoint();
    return gripPoints;
}

void DimLeaderObject::gripEdit(const QPointF& before, const QPointF& after)
{
    if     (before == objectEndPoint1()) { setObjectEndPoint1(to_emb_vector(after)); }
    else if(before == objectEndPoint2()) { setObjectEndPoint2(to_emb_vector(after)); }
    else if(before == objectMidPoint())  { QPointF delta = after-before; moveBy(delta.x(), delta.y()); }
}


EllipseObject::EllipseObject(float centerX, float centerY, float width, float height, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("EllipseObject Constructor()");
    init(centerX, centerY, width, height, rgb, Qt::SolidLine);
    /* TODO: getCurrentLineType */
}

EllipseObject::EllipseObject(EllipseObject* obj, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("EllipseObject Constructor()");
    if(obj)
    {
        init(obj->objectCenter().x(), obj->objectCenter().y(), obj->objectWidth(), obj->objectHeight(), obj->objectColorRGB(), Qt::SolidLine);
        /* TODO: getCurrentLineType */
        setRotation(obj->rotation());
    }
}

EllipseObject::~EllipseObject()
{
    debug_message("EllipseObject Destructor()");
}

void EllipseObject::init(float centerX, float centerY, float width, float height, unsigned int rgb, Qt::PenStyle lineType)
{
    setData(OBJ_TYPE, type());
    setData(OBJ_NAME, obj_names[OBJ_TYPE_ELLIPSE]);

    setFlag(QGraphicsItem::ItemIsSelectable, 1);

    setObjectSize(width, height);
    setPos(centerX, centerY);
    setObjectColor(rgb);
    setObjectLineType(lineType);
    setObjectLineWeight(0.35); /* TODO: pass in proper lineweight */
    setPen(objectPen());
    updatePath();
}

void EllipseObject::setObjectSize(float width, float height)
{
    QRectF elRect = rect();
    elRect.setWidth(width);
    elRect.setHeight(height);
    elRect.moveCenter(QPointF(0,0));
    setRect(elRect);
}

void EllipseObject::setObjectRadiusMajor(float radius)
{
    setObjectDiameterMajor(radius*2.0);
}

void EllipseObject::setObjectRadiusMinor(float radius)
{
    setObjectDiameterMinor(radius*2.0);
}

void EllipseObject::setObjectDiameterMajor(float diameter)
{
    QRectF elRect = rect();
    if (elRect.width() > elRect.height()) {
        elRect.setWidth(diameter);
    }
    else
        elRect.setHeight(diameter);
    elRect.moveCenter(QPointF(0,0));
    setRect(elRect);
}

void EllipseObject::setObjectDiameterMinor(float diameter)
{
    QRectF elRect = rect();
    if (elRect.width() < elRect.height()) {
        elRect.setWidth(diameter);
    }
    else
        elRect.setHeight(diameter);
    elRect.moveCenter(QPointF(0,0));
    setRect(elRect);
}

QPointF EllipseObject::objectQuadrant0() const
{
    EmbVector v;
    v.x = objectWidth()/2.0;
    v.y = 0.0;
    v = rotate_vector(v, radians(rotation()));
    return objectCenter() + to_qpointf(v);
}

QPointF EllipseObject::objectQuadrant90() const
{
    EmbVector v;
    v.x = objectHeight()/2.0;
    v.y = 0.0;
    v = rotate_vector(v, radians(rotation()+90.0));
    return objectCenter() + to_qpointf(v);
}

QPointF EllipseObject::objectQuadrant180() const
{
    EmbVector v;
    v.x = objectWidth()/2.0;
    v.y = 0.0;
    v = rotate_vector(v, radians(rotation()+180.0));
    return objectCenter() + to_qpointf(v);
}

QPointF EllipseObject::objectQuadrant270() const
{
    EmbVector v;
    v.x = objectHeight()/2.0;
    v.y = 0.0;
    v = rotate_vector(v, radians(rotation()+270.0));
    return objectCenter() + to_qpointf(v);
}

void EllipseObject::updatePath()
{
    QPainterPath path;
    QRectF r = rect();
    path.arcMoveTo(r, 0);
    path.arcTo(r, 0, 360);
    /* NOTE: Reverse the path so that the inside area isn't considered part of the ellipse. */
    path.arcTo(r, 0, -360);
    setObjectPath(path);
}

void EllipseObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/)
{
    QGraphicsScene* objScene = scene();
    if(!objScene) return;

    QPen paintPen = pen();
    painter->setPen(paintPen);
    updateRubber(painter);
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen);

    painter->drawEllipse(rect());
}

void EllipseObject::updateRubber(QPainter* painter)
{
    int rubberMode = objectRubberMode();
    if(rubberMode == OBJ_RUBBER_ELLIPSE_LINE)
    {
        QPointF sceneLinePoint1 = objectRubberPoint("ELLIPSE_LINE_POINT1");
        QPointF sceneLinePoint2 = objectRubberPoint("ELLIPSE_LINE_POINT2");
        QPointF itemLinePoint1 = mapFromScene(sceneLinePoint1);
        QPointF itemLinePoint2 = mapFromScene(sceneLinePoint2);
        QLineF itemLine(itemLinePoint1, itemLinePoint2);
        if(painter) drawRubberLine(itemLine, painter, "VIEW_COLOR_CROSSHAIR");
        updatePath();
    }
    else if(rubberMode == OBJ_RUBBER_ELLIPSE_MAJORDIAMETER_MINORRADIUS)
    {
        QPointF sceneAxis1Point1 = objectRubberPoint("ELLIPSE_AXIS1_POINT1");
        QPointF sceneAxis1Point2 = objectRubberPoint("ELLIPSE_AXIS1_POINT2");
        QPointF sceneCenterPoint = objectRubberPoint("ELLIPSE_CENTER");
        QPointF sceneAxis2Point2 = objectRubberPoint("ELLIPSE_AXIS2_POINT2");
        float ellipseWidth = objectRubberPoint("ELLIPSE_WIDTH").x();
        float ellipseRot = objectRubberPoint("ELLIPSE_ROT").x();

        /* TODO: incorporate perpendicularDistance() into libembroidery. */
        float px = sceneAxis2Point2.x();
        float py = sceneAxis2Point2.y();
        float x1 = sceneAxis1Point1.x();
        float y1 = sceneAxis1Point1.y();
        QLineF line(sceneAxis1Point1, sceneAxis1Point2);
        QLineF norm = line.normalVector();
        float dx = px-x1;
        float dy = py-y1;
        norm.translate(dx, dy);
        QPointF iPoint;
        /* HACK: this isn't in all versions of Qt 5 in the same place?
         * norm.intersects(line, &iPoint);
         */
        iPoint = line.p1();
        float ellipseHeight = QLineF(px, py, iPoint.x(), iPoint.y()).length()*2.0;

        setPos(sceneCenterPoint);
        setObjectSize(ellipseWidth, ellipseHeight);
        setRotation(-ellipseRot);

        QPointF itemCenterPoint = mapFromScene(sceneCenterPoint);
        QPointF itemAxis2Point2 = mapFromScene(sceneAxis2Point2);
        QLineF itemLine(itemCenterPoint, itemAxis2Point2);
        if(painter) drawRubberLine(itemLine, painter, "VIEW_COLOR_CROSSHAIR");
        updatePath();
    }
    else if(rubberMode == OBJ_RUBBER_ELLIPSE_MAJORRADIUS_MINORRADIUS)
    {
        QPointF sceneAxis1Point2 = objectRubberPoint("ELLIPSE_AXIS1_POINT2");
        QPointF sceneCenterPoint = objectRubberPoint("ELLIPSE_CENTER");
        QPointF sceneAxis2Point2 = objectRubberPoint("ELLIPSE_AXIS2_POINT2");
        float ellipseWidth = objectRubberPoint("ELLIPSE_WIDTH").x();
        float ellipseRot = objectRubberPoint("ELLIPSE_ROT").x();

        /* TODO: incorporate perpendicularDistance() into libembroidery. */
        float px = sceneAxis2Point2.x();
        float py = sceneAxis2Point2.y();
        float x1 = sceneCenterPoint.x();
        float y1 = sceneCenterPoint.y();
        QLineF line(sceneCenterPoint, sceneAxis1Point2);
        QLineF norm = line.normalVector();
        float dx = px-x1;
        float dy = py-y1;
        norm.translate(dx, dy);
        QPointF iPoint;
        /* HACK */
        /* norm.intersects(line, &iPoint); */
        iPoint = line.p1();
        float ellipseHeight = QLineF(px, py, iPoint.x(), iPoint.y()).length()*2.0;

        setPos(sceneCenterPoint);
        setObjectSize(ellipseWidth, ellipseHeight);
        setRotation(-ellipseRot);

        QPointF itemCenterPoint = mapFromScene(sceneCenterPoint);
        QPointF itemAxis2Point2 = mapFromScene(sceneAxis2Point2);
        QLineF itemLine(itemCenterPoint, itemAxis2Point2);
        if(painter) drawRubberLine(itemLine, painter, "VIEW_COLOR_CROSSHAIR");
        updatePath();
    }
    else if(rubberMode == OBJ_RUBBER_GRIP)
    {
        /* TODO: updateRubber() gripping for EllipseObject. */
    }
}

void EllipseObject::vulcanize()
{
    debug_message("EllipseObject vulcanize()");
    updateRubber();

    setObjectRubberMode(OBJ_RUBBER_OFF);
}

/* Returns the closest snap point to the mouse point. */
QPointF EllipseObject::mouseSnapPoint(const QPointF& mousePoint)
{
    QPointF center = objectCenter();
    QPointF quad0 = objectQuadrant0();
    QPointF quad90 = objectQuadrant90();
    QPointF quad180 = objectQuadrant180();
    QPointF quad270 = objectQuadrant270();

    float cntrDist = QLineF(mousePoint, center).length();
    float q0Dist = QLineF(mousePoint, quad0).length();
    float q90Dist = QLineF(mousePoint, quad90).length();
    float q180Dist = QLineF(mousePoint, quad180).length();
    float q270Dist = QLineF(mousePoint, quad270).length();

    float minDist = qMin(qMin(qMin(q0Dist, q90Dist), qMin(q180Dist, q270Dist)), cntrDist);

    if     (minDist == cntrDist) return center;
    else if(minDist == q0Dist)   return quad0;
    else if(minDist == q90Dist)  return quad90;
    else if(minDist == q180Dist) return quad180;
    else if(minDist == q270Dist) return quad270;

    return scenePos();
}

QList<QPointF> EllipseObject::allGripPoints()
{
    QList<QPointF> gripPoints;
    gripPoints << objectCenter() << objectQuadrant0() << objectQuadrant90() << objectQuadrant180() << objectQuadrant270();
    return gripPoints;
}

void EllipseObject::gripEdit(const QPointF& before, const QPointF& after)
{
    /*TODO: gripEdit() for EllipseObject*/
}

QPainterPath EllipseObject::objectSavePath() const
{
    QPainterPath path;
    QRectF r = rect();
    path.arcMoveTo(r, 0);
    path.arcTo(r, 0, 360);

    float s = scale();
    QTransform trans;
    trans.rotate(rotation());
    trans.scale(s,s);
    return trans.map(path);
}


ImageObject::ImageObject(float x, float y, float w, float h, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("ImageObject Constructor()");
    init(x, y, w, h, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

ImageObject::ImageObject(ImageObject* obj, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("ImageObject Constructor()");
    if(obj)
    {
        QPointF ptl = obj->objectTopLeft();
        init(ptl.x(), ptl.y(), obj->objectWidth(), obj->objectHeight(), obj->objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setRotation(obj->rotation());
    }
}

ImageObject::~ImageObject()
{
    debug_message("ImageObject Destructor()");
}

void ImageObject::init(float x, float y, float w, float h, unsigned int rgb, Qt::PenStyle lineType)
{
    setData(OBJ_TYPE, type());
    setData(OBJ_NAME, obj_names[OBJ_TYPE_IMAGE]);

    setFlag(QGraphicsItem::ItemIsSelectable, 1);

    setObjectRect(x, y, w, h);
    setObjectColor(rgb);
    setObjectLineType(lineType);
    setObjectLineWeight(0.35); /* TODO: pass in proper lineweight */
    setPen(objectPen());
}

void ImageObject::setObjectRect(float x, float y, float w, float h)
{
    setPos(x, y);
    setRect(0, 0, w, h);
    updatePath();
}

QPointF ImageObject::objectTopLeft() const
{
    EmbVector v = to_emb_vector(rect().topLeft());
    v = scale_and_rotate(v, scale(), radians(rotation()));

    return scenePos() + to_qpointf(v);
}

QPointF ImageObject::objectTopRight() const
{
    EmbVector v = to_emb_vector(rect().topRight());
    v = scale_and_rotate(v, scale(), radians(rotation()));

    return scenePos() + to_qpointf(v);
}

QPointF ImageObject::objectBottomLeft() const
{
    EmbVector v = to_emb_vector(rect().bottomLeft());
    v = scale_and_rotate(v, scale(), radians(rotation()));

    return scenePos() + to_qpointf(v);
}

QPointF ImageObject::objectBottomRight() const
{
    EmbVector v = to_emb_vector(rect().bottomRight());
    v = scale_and_rotate(v, scale(), radians(rotation()));

    return scenePos() + to_qpointf(v);
}

void ImageObject::updatePath()
{
    QPainterPath path;
    QRectF r = rect();
    path.moveTo(r.bottomLeft());
    path.lineTo(r.bottomRight());
    path.lineTo(r.topRight());
    path.lineTo(r.topLeft());
    path.lineTo(r.bottomLeft());
    /*NOTE: Reverse the path so that the inside area isn't considered part of the rectangle*/
    path.lineTo(r.topLeft());
    path.lineTo(r.topRight());
    path.lineTo(r.bottomRight());
    path.moveTo(r.bottomLeft());
    setObjectPath(path);
}

void ImageObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/)
{
    QGraphicsScene* objScene = scene();
    if(!objScene) return;

    QPen paintPen = pen();
    painter->setPen(paintPen);
    updateRubber(painter);
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen);

    painter->drawRect(rect());
}

void ImageObject::updateRubber(QPainter* painter)
{
    int rubberMode = objectRubberMode();
    if(rubberMode == OBJ_RUBBER_IMAGE)
    {
        QPointF sceneStartPoint = objectRubberPoint("IMAGE_START");
        QPointF sceneEndPoint = objectRubberPoint("IMAGE_END");
        float x = sceneStartPoint.x();
        float y = sceneStartPoint.y();
        float w = sceneEndPoint.x() - sceneStartPoint.x();
        float h = sceneEndPoint.y() - sceneStartPoint.y();
        setObjectRect(x,y,w,h);
        updatePath();
    }
    else if(rubberMode == OBJ_RUBBER_GRIP)
    {
        /*TODO: updateRubber() gripping for ImageObject*/
    }
}

void ImageObject::vulcanize()
{
    debug_message("ImageObject vulcanize()");
    updateRubber();

    setObjectRubberMode(OBJ_RUBBER_OFF);
}

/* Returns the closest snap point to the mouse point*/
QPointF ImageObject::mouseSnapPoint(const QPointF& mousePoint)
{
    QPointF ptl = objectTopLeft();     /* Top Left Corner QSnap */
    QPointF ptr = objectTopRight();    /* Top Right Corner QSnap */
    QPointF pbl = objectBottomLeft();  /*Bottom Left Corner QSnap*/
    QPointF pbr = objectBottomRight(); /*Bottom Right Corner QSnap*/

    float ptlDist = QLineF(mousePoint, ptl).length();
    float ptrDist = QLineF(mousePoint, ptr).length();
    float pblDist = QLineF(mousePoint, pbl).length();
    float pbrDist = QLineF(mousePoint, pbr).length();

    float minDist = qMin(qMin(ptlDist, ptrDist), qMin(pblDist, pbrDist));

    if     (minDist == ptlDist) return ptl;
    else if(minDist == ptrDist) return ptr;
    else if(minDist == pblDist) return pbl;
    else if(minDist == pbrDist) return pbr;

    return scenePos();
}

QList<QPointF> ImageObject::allGripPoints()
{
    QList<QPointF> gripPoints;
    gripPoints << objectTopLeft() << objectTopRight() << objectBottomLeft() << objectBottomRight();
    return gripPoints;
}

void ImageObject::gripEdit(const QPointF& before, const QPointF& after)
{
    /*TODO: gripEdit() for ImageObject*/
}

LineObject::LineObject(float x1, float y1, float x2, float y2, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("LineObject Constructor()");
    init(x1, y1, x2, y2, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

LineObject::LineObject(LineObject* obj, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("LineObject Constructor()");
    if(obj)
    {
        init(obj->objectX1(), obj->objectY1(), obj->objectX2(), obj->objectY2(), obj->objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
    }
}

LineObject::~LineObject()
{
    debug_message("LineObject Destructor()");
}

void LineObject::init(float x1, float y1, float x2, float y2, unsigned int rgb, Qt::PenStyle lineType)
{
    setData(OBJ_TYPE, type());
    setData(OBJ_NAME, obj_names[OBJ_TYPE_LINE]);

    setFlag(QGraphicsItem::ItemIsSelectable, 1);

    setObjectEndPoint1(x1, y1);
    setObjectEndPoint2(x2, y2);
    setObjectColor(rgb);
    setObjectLineType(lineType);
    /* TODO: pass in proper lineweight */
    setObjectLineWeight(0.35);
    setPen(objectPen());
}

void LineObject::setObjectEndPoint1(const QPointF& endPt1)
{
    setObjectEndPoint1(endPt1.x(), endPt1.y());
}

void LineObject::setObjectEndPoint1(float x1, float y1)
{
    EmbVector delta, endPt2;
    endPt2 = to_emb_vector(objectEndPoint2());
    delta.x = endPt2.x - x1;
    delta.y = endPt2.y - y1;
    setRotation(0);
    setScale(1);
    setLine(0, 0, delta.x, delta.y);
    setPos(x1, y1);
}

void LineObject::setObjectEndPoint2(const QPointF& endPt2)
{
    setObjectEndPoint2(endPt2.x(), endPt2.y());
}

void LineObject::setObjectEndPoint2(float x2, float y2)
{
    EmbVector delta, endPt1;
    endPt1 = to_emb_vector(scenePos());
    delta.x = x2 - endPt1.x;
    delta.y = y2 - endPt1.y;
    setRotation(0);
    setScale(1);
    setLine(0, 0, delta.x, delta.y);
    setPos(endPt1.x, endPt1.y);
}

QPointF LineObject::objectEndPoint2() const
{
    EmbVector v;
    v.x = line().x2();
    v.y = line().y2();
    v = scale_and_rotate(v, scale(), radians(rotation()));

    return scenePos() + to_qpointf(v);
}

QPointF LineObject::objectMidPoint() const
{
    EmbVector v;
    v = to_emb_vector(line().pointAt(0.5));
    v = scale_and_rotate(v, scale(), radians(rotation()));

    return scenePos() + to_qpointf(v);
}

float LineObject::objectAngle() const
{
    float angle = line().angle() - rotation();
    return fmod(angle, 360.0);
}

void LineObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/)
{
    QGraphicsScene* objScene = scene();
    if(!objScene) return;

    QPen paintPen = pen();
    painter->setPen(paintPen);
    updateRubber(painter);
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen);

    if(objectRubberMode() != OBJ_RUBBER_LINE) painter->drawLine(line());

    if(objScene->property("ENABLE_LWT").toBool() && objScene->property("ENABLE_REAL").toBool()) { realRender(painter, path()); }
}

void LineObject::updateRubber(QPainter* painter)
{
    int rubberMode = objectRubberMode();
    if(rubberMode == OBJ_RUBBER_LINE)
    {
        QPointF sceneStartPoint = objectRubberPoint("LINE_START");
        QPointF sceneQSnapPoint = objectRubberPoint("LINE_END");

        setObjectEndPoint1(sceneStartPoint);
        setObjectEndPoint2(sceneQSnapPoint);

        drawRubberLine(line(), painter, "VIEW_COLOR_CROSSHAIR");
    }
    else if(rubberMode == OBJ_RUBBER_GRIP)
    {
        if(painter)
        {
            QPointF gripPoint = objectRubberPoint("GRIP_POINT");
            if     (gripPoint == objectEndPoint1()) painter->drawLine(line().p2(), mapFromScene(objectRubberPoint(QString())));
            else if(gripPoint == objectEndPoint2()) painter->drawLine(line().p1(), mapFromScene(objectRubberPoint(QString())));
            else if(gripPoint == objectMidPoint())  painter->drawLine(line().translated(mapFromScene(objectRubberPoint(QString()))-mapFromScene(gripPoint)));

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())));
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR");
        }
    }
}

void LineObject::vulcanize()
{
    debug_message("LineObject vulcanize()");
    updateRubber();

    setObjectRubberMode(OBJ_RUBBER_OFF);
}

/* Returns the closest snap point to the mouse point*/
QPointF LineObject::mouseSnapPoint(const QPointF& mousePoint)
{
    QPointF endPoint1 = objectEndPoint1();
    QPointF endPoint2 = objectEndPoint2();
    QPointF midPoint = objectMidPoint();

    float end1Dist = QLineF(mousePoint, endPoint1).length();
    float end2Dist = QLineF(mousePoint, endPoint2).length();
    float midDist = QLineF(mousePoint, midPoint).length();

    float minDist = qMin(qMin(end1Dist, end2Dist), midDist);

    if     (minDist == end1Dist) return endPoint1;
    else if(minDist == end2Dist) return endPoint2;
    else if(minDist == midDist)  return midPoint;

    return scenePos();
}

QList<QPointF> LineObject::allGripPoints()
{
    QList<QPointF> gripPoints;
    gripPoints << objectEndPoint1() << objectEndPoint2() << objectMidPoint();
    return gripPoints;
}

void LineObject::gripEdit(const QPointF& before, const QPointF& after)
{
    if     (before == objectEndPoint1()) { setObjectEndPoint1(after.x(), after.y()); }
    else if(before == objectEndPoint2()) { setObjectEndPoint2(after.x(), after.y()); }
    else if(before == objectMidPoint())  { QPointF delta = after-before; moveBy(delta.x(), delta.y()); }
}

QPainterPath LineObject::objectSavePath() const
{
    QPainterPath path;
    path.lineTo(objectDeltaX(), objectDeltaY());
    return path;
}


PathObject::PathObject(float x, float y, const QPainterPath p, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("PathObject Constructor()");
    init(x, y, p, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

PathObject::PathObject(PathObject* obj, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("PathObject Constructor()");
    if (obj) {
        init(obj->objectX(), obj->objectY(), obj->objectCopyPath(), obj->objPen.color().rgb(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setRotation(obj->rotation());
        setScale(obj->scale());
    }
}

PathObject::~PathObject()
{
    debug_message("PathObject Destructor()");
}

void PathObject::init(float x, float y, const QPainterPath& p, unsigned int rgb, Qt::PenStyle lineType)
{
    setData(OBJ_TYPE, type());
    setData(OBJ_NAME, obj_names[OBJ_TYPE_PATH]);

    setFlag(QGraphicsItem::ItemIsSelectable, 1);

    updatePath(p);
    setObjectPos(x,y);
    setObjectColor(rgb);
    setObjectLineType(lineType);
    /* TODO: pass in proper lineweight */
    setObjectLineWeight(0.35);
    setPen(objectPen());
}

void PathObject::updatePath(const QPainterPath& p)
{
    normalPath = p;
    QPainterPath reversePath = normalPath.toReversed();
    reversePath.connectPath(normalPath);
    setObjectPath(reversePath);
}

void PathObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/)
{
    QGraphicsScene* objScene = scene();
    if(!objScene) return;

    QPen paintPen = pen();
    painter->setPen(paintPen);
    updateRubber(painter);
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen);

    painter->drawPath(objectPath());
}

void PathObject::updateRubber(QPainter* painter)
{
    /*TODO: Path Rubber Modes*/

    /*TODO: updateRubber() gripping for PathObject*/

}

void PathObject::vulcanize()
{
    debug_message("PathObject vulcanize()");
    updateRubber();

    setObjectRubberMode(OBJ_RUBBER_OFF);

    if(!normalPath.elementCount())
        QMessageBox::critical(0, QObject::tr("Empty Path Error"), QObject::tr("The path added contains no points. The command that created this object has flawed logic."));
}

/* Returns the closest snap point to the mouse point*/
QPointF PathObject::mouseSnapPoint(const QPointF& mousePoint)
{
    return scenePos();
}

QList<QPointF> PathObject::allGripPoints()
{
    QList<QPointF> gripPoints;
    gripPoints << scenePos(); /*TODO: loop thru all path Elements and return their points*/
    return gripPoints;
}

void PathObject::gripEdit(const QPointF& before, const QPointF& after)
{
    /*TODO: gripEdit() for PathObject*/
}

QPainterPath PathObject::objectCopyPath() const
{
    return normalPath;
}

QPainterPath PathObject::objectSavePath() const
{
    float s = scale();
    QTransform trans;
    trans.rotate(rotation());
    trans.scale(s,s);
    return trans.map(normalPath);
}


PointObject::PointObject(float x, float y, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("PointObject Constructor()");
    init(x, y, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

PointObject::PointObject(PointObject* obj, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("PointObject Constructor()");
    if(obj)
    {
        init(obj->objectX(), obj->objectY(), obj->objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setRotation(obj->rotation());
    }
}

PointObject::~PointObject()
{
    debug_message("PointObject Destructor()");
}

void PointObject::init(float x, float y, unsigned int rgb, Qt::PenStyle lineType)
{
    setData(OBJ_TYPE, type());
    setData(OBJ_NAME, obj_names[OBJ_TYPE_POINT]);

    setFlag(QGraphicsItem::ItemIsSelectable, 1);

    setRect(-0.00000001, -0.00000001, 0.00000002, 0.00000002);
    setObjectPos(x,y);
    setObjectColor(rgb);
    setObjectLineType(lineType);
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objectPen());
}

void PointObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/)
{
    QGraphicsScene* objScene = scene();
    if(!objScene) return;

    QPen paintPen = pen();
    painter->setPen(paintPen);
    updateRubber(painter);
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen);

    painter->drawPoint(0,0);
}

void PointObject::updateRubber(QPainter* painter)
{
    int rubberMode = objectRubberMode();
    if(rubberMode == OBJ_RUBBER_GRIP)
    {
        if(painter)
        {
            QPointF gripPoint = objectRubberPoint("GRIP_POINT");
            if(gripPoint == scenePos())
            {
                QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())));
                drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR");
            }
        }
    }
}

void PointObject::vulcanize()
{
    debug_message("PointObject vulcanize()");
    updateRubber();

    setObjectRubberMode(OBJ_RUBBER_OFF);
}

/* Returns the closest snap point to the mouse point*/
QPointF PointObject::mouseSnapPoint(const QPointF& mousePoint)
{
    return scenePos();
}

QList<QPointF> PointObject::allGripPoints()
{
    QList<QPointF> gripPoints;
    gripPoints << scenePos();
    return gripPoints;
}

void PointObject::gripEdit(const QPointF& before, const QPointF& after)
{
    if(before == scenePos()) { QPointF delta = after-before; moveBy(delta.x(), delta.y()); }
}

QPainterPath PointObject::objectSavePath() const
{
    QPainterPath path;
    path.addRect(-0.00000001, -0.00000001, 0.00000002, 0.00000002);
    return path;
}


PolygonObject::PolygonObject(float x, float y, const QPainterPath& p, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("PolygonObject Constructor()");
    init(x, y, p, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

PolygonObject::PolygonObject(PolygonObject* obj, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("PolygonObject Constructor()");
    if(obj)
    {
        init(obj->objectX(), obj->objectY(), obj->objectCopyPath(), obj->objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setRotation(obj->rotation());
        setScale(obj->scale());
    }
}

PolygonObject::~PolygonObject()
{
    debug_message("PolygonObject Destructor()");
}

void PolygonObject::init(float x, float y, const QPainterPath& p, unsigned int rgb, Qt::PenStyle lineType)
{
    setData(OBJ_TYPE, type());
    setData(OBJ_NAME, obj_names[OBJ_TYPE_POLYGON]);

    setFlag(QGraphicsItem::ItemIsSelectable, 1);

    gripIndex = -1;
    updatePath(p);
    setObjectPos(x,y);
    setObjectColor(rgb);
    setObjectLineType(lineType);
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objectPen());
}

void PolygonObject::updatePath(const QPainterPath& p)
{
    normalPath = p;
    QPainterPath closedPath = normalPath;
    closedPath.closeSubpath();
    QPainterPath reversePath = closedPath.toReversed();
    reversePath.connectPath(closedPath);
    setObjectPath(reversePath);
}

void PolygonObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/)
{
    QGraphicsScene* objScene = scene();
    if(!objScene) return;

    QPen paintPen = pen();
    painter->setPen(paintPen);
    updateRubber(painter);
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen);

    if(normalPath.elementCount())
    {
        painter->drawPath(normalPath);
        QPainterPath::Element zero = normalPath.elementAt(0);
        QPainterPath::Element last = normalPath.elementAt(normalPath.elementCount()-1);
        painter->drawLine(QPointF(zero.x, zero.y), QPointF(last.x, last.y));
    }
}

void PolygonObject::updateRubber(QPainter* painter)
{
    int rubberMode = objectRubberMode();
    if (rubberMode == OBJ_RUBBER_POLYGON) {
        setObjectPos(objectRubberPoint("POLYGON_POINT_0"));

        bool ok = 0;
        QString numStr = objectRubberText("POLYGON_NUM_POINTS");
        if(numStr.isNull()) return;
        int num = numStr.toInt(&ok);
        if(!ok) return;

        QString appendStr;
        QPainterPath rubberPath;
        rubberPath.moveTo(mapFromScene(objectRubberPoint("POLYGON_POINT_0")));
        for(int i = 1; i <= num; i++)
        {
            appendStr = "POLYGON_POINT_" + QString().setNum(i);
            QPointF appendPoint = mapFromScene(objectRubberPoint(appendStr));
            rubberPath.lineTo(appendPoint);
        }
        /*rubberPath.lineTo(0,0);*/
        updatePath(rubberPath);

        /*Ensure the path isn't updated until the number of points is changed again*/
        setObjectRubberText("POLYGON_NUM_POINTS", QString());
    }
    else if(rubberMode == OBJ_RUBBER_POLYGON_INSCRIBE) {
        setObjectPos(objectRubberPoint("POLYGON_CENTER"));

        unsigned short numSides = objectRubberPoint("POLYGON_NUM_SIDES").x();

        QPointF inscribePoint = mapFromScene(objectRubberPoint("POLYGON_INSCRIBE_POINT"));
        QLineF inscribeLine = QLineF(QPointF(0,0), inscribePoint);
        float inscribeAngle = inscribeLine.angle();
        float inscribeInc = 360.0/numSides;

        if(painter) drawRubberLine(inscribeLine, painter, "VIEW_COLOR_CROSSHAIR");

        QPainterPath inscribePath;
        /*First Point*/
        inscribePath.moveTo(inscribePoint);
        /*Remaining Points*/
        for (int i = 1; i < numSides; i++) {
            inscribeLine.setAngle(inscribeAngle + inscribeInc*i);
            inscribePath.lineTo(inscribeLine.p2());
        }
        updatePath(inscribePath);
    }
    else if (rubberMode == OBJ_RUBBER_POLYGON_CIRCUMSCRIBE) {
        setObjectPos(objectRubberPoint("POLYGON_CENTER"));

        unsigned short numSides = objectRubberPoint("POLYGON_NUM_SIDES").x();

        QPointF circumscribePoint = mapFromScene(objectRubberPoint("POLYGON_CIRCUMSCRIBE_POINT"));
        QLineF circumscribeLine = QLineF(QPointF(0,0), circumscribePoint);
        float circumscribeAngle = circumscribeLine.angle();
        float circumscribeInc = 360.0/numSides;

        if(painter) drawRubberLine(circumscribeLine, painter, "VIEW_COLOR_CROSSHAIR");

        QPainterPath circumscribePath;
        /*First Point*/
        QLineF prev(circumscribeLine.p2(), QPointF(0,0));
        prev = prev.normalVector();
        circumscribeLine.setAngle(circumscribeAngle + circumscribeInc);
        QLineF perp(circumscribeLine.p2(), QPointF(0,0));
        perp = perp.normalVector();
        QPointF iPoint;
        /* HACK perp.intersects(prev, &iPoint); */
        iPoint = perp.p1();
        circumscribePath.moveTo(iPoint);
        /*Remaining Points*/
        for(int i = 2; i <= numSides; i++)
        {
            prev = perp;
            circumscribeLine.setAngle(circumscribeAngle + circumscribeInc*i);
            perp = QLineF(circumscribeLine.p2(), QPointF(0,0));
            perp = perp.normalVector();
            /* HACK perp.intersects(prev, &iPoint); */
            iPoint = perp.p1();
            circumscribePath.lineTo(iPoint);
        }
        updatePath(circumscribePath);
    }
    else if(rubberMode == OBJ_RUBBER_GRIP) {
        if(painter) {
            int elemCount = normalPath.elementCount();
            QPointF gripPoint = objectRubberPoint("GRIP_POINT");
            if(gripIndex == -1) gripIndex = findIndex(gripPoint);
            if(gripIndex == -1) return;

            int m = 0;
            int n = 0;

            if(!gripIndex)                    { m = elemCount-1; n = 1; }
            else if(gripIndex == elemCount-1) { m = elemCount-2; n = 0; }
            else                              { m = gripIndex-1; n = gripIndex+1; }
            QPainterPath::Element em = normalPath.elementAt(m);
            QPainterPath::Element en = normalPath.elementAt(n);
            QPointF emPoint = QPointF(em.x, em.y);
            QPointF enPoint = QPointF(en.x, en.y);
            painter->drawLine(emPoint, mapFromScene(objectRubberPoint(QString())));
            painter->drawLine(enPoint, mapFromScene(objectRubberPoint(QString())));

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())));
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR");
        }
    }
}

void PolygonObject::vulcanize()
{
    debug_message("PolygonObject vulcanize()");
    updateRubber();

    setObjectRubberMode(OBJ_RUBBER_OFF);

    if(!normalPath.elementCount())
        QMessageBox::critical(0, QObject::tr("Empty Polygon Error"), QObject::tr("The polygon added contains no points. The command that created this object has flawed logic."));
}

/* Returns the closest snap point to the mouse point*/
QPointF PolygonObject::mouseSnapPoint(const QPointF& mousePoint)
{
    QPainterPath::Element element = normalPath.elementAt(0);
    QPointF closestPoint = mapToScene(QPointF(element.x, element.y));
    float closestDist = QLineF(mousePoint, closestPoint).length();
    int elemCount = normalPath.elementCount();
    for(int i = 0; i < elemCount; ++i)
    {
        element = normalPath.elementAt(i);
        QPointF elemPoint = mapToScene(element.x, element.y);
        float elemDist = QLineF(mousePoint, elemPoint).length();
        if(elemDist < closestDist)
        {
            closestPoint = elemPoint;
            closestDist = elemDist;
        }
    }
    return closestPoint;
}

QList<QPointF> PolygonObject::allGripPoints()
{
    QList<QPointF> gripPoints;
    QPainterPath::Element element;
    for(int i = 0; i < normalPath.elementCount(); ++i)
    {
        element = normalPath.elementAt(i);
        gripPoints << mapToScene(element.x, element.y);
    }
    return gripPoints;
}

int PolygonObject::findIndex(const QPointF& point)
{
    int i = 0;
    int elemCount = normalPath.elementCount();
    /*NOTE: Points here are in item coordinates*/
    QPointF itemPoint = mapFromScene(point);
    for(i = 0; i < elemCount; i++)
    {
        QPainterPath::Element e = normalPath.elementAt(i);
        QPointF elemPoint = QPointF(e.x, e.y);
        if(itemPoint == elemPoint) return i;
    }
    return -1;
}

void PolygonObject::gripEdit(const QPointF& before, const QPointF& after)
{
    gripIndex = findIndex(before);
    if(gripIndex == -1) return;
    QPointF a = mapFromScene(after);
    normalPath.setElementPositionAt(gripIndex, a.x(), a.y());
    updatePath(normalPath);
    gripIndex = -1;
}

QPainterPath PolygonObject::objectCopyPath() const
{
    return normalPath;
}

QPainterPath PolygonObject::objectSavePath() const
{
    QPainterPath closedPath = normalPath;
    closedPath.closeSubpath();
    float s = scale();
    QTransform trans;
    trans.rotate(rotation());
    trans.scale(s,s);
    return trans.map(closedPath);
}


PolylineObject::PolylineObject(float x, float y, const QPainterPath& p, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("PolylineObject Constructor()");
    init(x, y, p, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

PolylineObject::PolylineObject(PolylineObject* obj, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("PolylineObject Constructor()");
    if(obj)
    {
        init(obj->objectX(), obj->objectY(), obj->objectCopyPath(), obj->objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setRotation(obj->rotation());
        setScale(obj->scale());
    }
}

PolylineObject::~PolylineObject()
{
    debug_message("PolylineObject Destructor()");
}

void PolylineObject::init(float x, float y, const QPainterPath& p, unsigned int rgb, Qt::PenStyle lineType)
{
    setData(OBJ_TYPE, PolylineObject::Type);
    setData(OBJ_NAME, obj_names[OBJ_TYPE_POLYLINE]);

    setFlag(QGraphicsItem::ItemIsSelectable, 1);

    gripIndex = -1;
    updatePath(p);
    setObjectPos(x,y);
    setObjectColor(rgb);
    setObjectLineType(lineType);
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objectPen());
}

void PolylineObject::updatePath(const QPainterPath& p)
{
    normalPath = p;
    QPainterPath reversePath = normalPath.toReversed();
    reversePath.connectPath(normalPath);
    setObjectPath(reversePath);
}

void PolylineObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/)
{
    QGraphicsScene* objScene = scene();
    if(!objScene) return;

    QPen paintPen = pen();
    painter->setPen(paintPen);
    updateRubber(painter);
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen);

    painter->drawPath(normalPath);

    if(objScene->property("ENABLE_LWT").toBool() && objScene->property("ENABLE_REAL").toBool()) { realRender(painter, normalPath); }
}

void PolylineObject::updateRubber(QPainter* painter)
{
    int rubberMode = objectRubberMode();
    if(rubberMode == OBJ_RUBBER_POLYLINE)
    {
        setObjectPos(objectRubberPoint("POLYLINE_POINT_0"));

        QLineF rubberLine(normalPath.currentPosition(), mapFromScene(objectRubberPoint(QString())));
        if(painter) drawRubberLine(rubberLine, painter, "VIEW_COLOR_CROSSHAIR");

        bool ok = 0;
        QString numStr = objectRubberText("POLYLINE_NUM_POINTS");
        if(numStr.isNull()) return;
        int num = numStr.toInt(&ok);
        if(!ok) return;

        QString appendStr;
        QPainterPath rubberPath;
        for(int i = 1; i <= num; i++)
        {
            appendStr = "POLYLINE_POINT_" + QString().setNum(i);
            QPointF appendPoint = mapFromScene(objectRubberPoint(appendStr));
            rubberPath.lineTo(appendPoint);
        }
        updatePath(rubberPath);

        /*Ensure the path isn't updated until the number of points is changed again*/
        setObjectRubberText("POLYLINE_NUM_POINTS", QString());
    }
    else if(rubberMode == OBJ_RUBBER_GRIP)
    {
        if(painter)
        {
            int elemCount = normalPath.elementCount();
            QPointF gripPoint = objectRubberPoint("GRIP_POINT");
            if(gripIndex == -1) gripIndex = findIndex(gripPoint);
            if(gripIndex == -1) return;

            if(!gripIndex) /*First*/
            {
                QPainterPath::Element ef = normalPath.elementAt(1);
                QPointF efPoint = QPointF(ef.x, ef.y);
                painter->drawLine(efPoint, mapFromScene(objectRubberPoint(QString())));
            }
            else if(gripIndex == elemCount-1) /*Last*/
            {
                QPainterPath::Element el = normalPath.elementAt(gripIndex-1);
                QPointF elPoint = QPointF(el.x, el.y);
                painter->drawLine(elPoint, mapFromScene(objectRubberPoint(QString())));
            }
            else /*Middle*/
            {
                QPainterPath::Element em = normalPath.elementAt(gripIndex-1);
                QPainterPath::Element en = normalPath.elementAt(gripIndex+1);
                QPointF emPoint = QPointF(em.x, em.y);
                QPointF enPoint = QPointF(en.x, en.y);
                painter->drawLine(emPoint, mapFromScene(objectRubberPoint(QString())));
                painter->drawLine(enPoint, mapFromScene(objectRubberPoint(QString())));
            }

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())));
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR");
        }
    }
}

void PolylineObject::vulcanize()
{
    debug_message("PolylineObject vulcanize()");
    updateRubber();

    setObjectRubberMode(OBJ_RUBBER_OFF);

    if(!normalPath.elementCount())
        QMessageBox::critical(0, QObject::tr("Empty Polyline Error"), QObject::tr("The polyline added contains no points. The command that created this object has flawed logic."));
}

/* Returns the closest snap point to the mouse point*/
QPointF PolylineObject::mouseSnapPoint(const QPointF& mousePoint)
{
    QPainterPath::Element element = normalPath.elementAt(0);
    QPointF closestPoint = mapToScene(QPointF(element.x, element.y));
    float closestDist = QLineF(mousePoint, closestPoint).length();
    int elemCount = normalPath.elementCount();
    for(int i = 0; i < elemCount; ++i)
    {
        element = normalPath.elementAt(i);
        QPointF elemPoint = mapToScene(element.x, element.y);
        float elemDist = QLineF(mousePoint, elemPoint).length();
        if(elemDist < closestDist)
        {
            closestPoint = elemPoint;
            closestDist = elemDist;
        }
    }
    return closestPoint;
}

QList<QPointF> PolylineObject::allGripPoints()
{
    QList<QPointF> gripPoints;
    QPainterPath::Element element;
    for(int i = 0; i < normalPath.elementCount(); ++i)
    {
        element = normalPath.elementAt(i);
        gripPoints << mapToScene(element.x, element.y);
    }
    return gripPoints;
}

int PolylineObject::findIndex(const QPointF& point)
{
    int elemCount = normalPath.elementCount();
    /*NOTE: Points here are in item coordinates*/
    QPointF itemPoint = mapFromScene(point);
    for (int i = 0; i < elemCount; i++) {
        QPainterPath::Element e = normalPath.elementAt(i);
        QPointF elemPoint = QPointF(e.x, e.y);
        if(itemPoint == elemPoint) return i;
    }
    return -1;
}

void PolylineObject::gripEdit(const QPointF& before, const QPointF& after)
{
    gripIndex = findIndex(before);
    if(gripIndex == -1) return;
    QPointF a = mapFromScene(after);
    normalPath.setElementPositionAt(gripIndex, a.x(), a.y());
    updatePath(normalPath);
    gripIndex = -1;
}

QPainterPath PolylineObject::objectCopyPath() const
{
    return normalPath;
}

QPainterPath PolylineObject::objectSavePath() const
{
    float s = scale();
    QTransform trans;
    trans.rotate(rotation());
    trans.scale(s,s);
    return trans.map(normalPath);
}


RectObject::RectObject(float x, float y, float w, float h, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("RectObject Constructor()");
    init(x, y, w, h, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

RectObject::RectObject(RectObject* obj, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("RectObject Constructor()");
    if(obj)
    {
        QPointF ptl = obj->objectTopLeft();
        init(ptl.x(), ptl.y(), obj->objectWidth(), obj->objectHeight(), obj->objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setRotation(obj->rotation());
    }
}

RectObject::~RectObject()
{
    debug_message("RectObject Destructor()");
}

void RectObject::init(float x, float y, float w, float h, unsigned int rgb, Qt::PenStyle lineType)
{
    setData(OBJ_TYPE, type());
    setData(OBJ_NAME, obj_names[OBJ_TYPE_RECTANGLE]);

    setFlag(QGraphicsItem::ItemIsSelectable, 1);

    setObjectRect(x, y, w, h);
    setObjectColor(rgb);
    setObjectLineType(lineType);
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objectPen());
}

void RectObject::setObjectRect(float x, float y, float w, float h)
{
    setPos(x, y);
    setRect(0, 0, w, h);
    updatePath();
}

QPointF RectObject::objectTopLeft() const
{
    EmbVector v;
    v = to_emb_vector(rect().topLeft());
    v = scale_and_rotate(v, scale(), radians(rotation()));

    return scenePos() + to_qpointf(v);
}

QPointF RectObject::objectTopRight() const
{
    EmbVector v;
    v = to_emb_vector(rect().topRight());
    v = scale_and_rotate(v, scale(), radians(rotation()));

    return scenePos() + to_qpointf(v);
}

QPointF RectObject::objectBottomLeft() const
{
    EmbVector v;
    v = to_emb_vector(rect().bottomLeft());
    v = scale_and_rotate(v, scale(), radians(rotation()));

    return scenePos() + to_qpointf(v);
}

QPointF RectObject::objectBottomRight() const
{
    EmbVector v;
    v = to_emb_vector(rect().bottomRight());
    v = scale_and_rotate(v, scale(), radians(rotation()));

    return scenePos() + to_qpointf(v);
}

void RectObject::updatePath()
{
    QPainterPath path;
    QRectF r = rect();
    path.moveTo(r.bottomLeft());
    path.lineTo(r.bottomRight());
    path.lineTo(r.topRight());
    path.lineTo(r.topLeft());
    path.lineTo(r.bottomLeft());
    /*NOTE: Reverse the path so that the inside area isn't considered part of the rectangle*/
    path.lineTo(r.topLeft());
    path.lineTo(r.topRight());
    path.lineTo(r.bottomRight());
    path.moveTo(r.bottomLeft());
    setObjectPath(path);
}

void RectObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/)
{
    QGraphicsScene* objScene = scene();
    if(!objScene) return;

    QPen paintPen = pen();
    painter->setPen(paintPen);
    updateRubber(painter);
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen);

    painter->drawRect(rect());
}

void RectObject::updateRubber(QPainter* painter)
{
    int rubberMode = objectRubberMode();
    if(rubberMode == OBJ_RUBBER_RECTANGLE)
    {
        QPointF sceneStartPoint = objectRubberPoint("RECTANGLE_START");
        QPointF sceneEndPoint = objectRubberPoint("RECTANGLE_END");
        float x = sceneStartPoint.x();
        float y = sceneStartPoint.y();
        float w = sceneEndPoint.x() - sceneStartPoint.x();
        float h = sceneEndPoint.y() - sceneStartPoint.y();
        setObjectRect(x,y,w,h);
        updatePath();
    }
    else if(rubberMode == OBJ_RUBBER_GRIP)
    {
        if(painter)
        {
            /* TODO: Make this work with rotation & scaling. */
            /*
            QPointF gripPoint = objectRubberPoint("GRIP_POINT");
            QPointF after = objectRubberPoint(QString());
            QPointF delta = after-gripPoint;
            if     (gripPoint == objectTopLeft())     { painter->drawPolygon(mapFromScene(QRectF(after.x(), after.y(), objectWidth()-delta.x(), objectHeight()-delta.y()))); }
            else if(gripPoint == objectTopRight())    { painter->drawPolygon(mapFromScene(QRectF(objectTopLeft().x(), objectTopLeft().y()+delta.y(), objectWidth()+delta.x(), objectHeight()-delta.y()))); }
            else if(gripPoint == objectBottomLeft())  { painter->drawPolygon(mapFromScene(QRectF(objectTopLeft().x()+delta.x(), objectTopLeft().y(), objectWidth()-delta.x(), objectHeight()+delta.y()))); }
            else if(gripPoint == objectBottomRight()) { painter->drawPolygon(mapFromScene(QRectF(objectTopLeft().x(), objectTopLeft().y(), objectWidth()+delta.x(), objectHeight()+delta.y()))); }

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())));
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR");
            */

            QPointF gripPoint = objectRubberPoint("GRIP_POINT");
            QPointF after = objectRubberPoint(QString());
            QPointF delta = after-gripPoint;

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())));
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR");
        }
    }
}

void RectObject::vulcanize()
{
    debug_message("RectObject vulcanize()");
    updateRubber();

    setObjectRubberMode(OBJ_RUBBER_OFF);
}

/* Returns the closest snap point to the mouse point*/
QPointF RectObject::mouseSnapPoint(const QPointF& mousePoint)
{
    QPointF ptl = objectTopLeft();     /*Top Left Corner QSnap*/
    QPointF ptr = objectTopRight();    /*Top Right Corner QSnap*/
    QPointF pbl = objectBottomLeft();  /*Bottom Left Corner QSnap*/
    QPointF pbr = objectBottomRight(); /*Bottom Right Corner QSnap*/

    float ptlDist = QLineF(mousePoint, ptl).length();
    float ptrDist = QLineF(mousePoint, ptr).length();
    float pblDist = QLineF(mousePoint, pbl).length();
    float pbrDist = QLineF(mousePoint, pbr).length();

    float minDist = qMin(qMin(ptlDist, ptrDist), qMin(pblDist, pbrDist));

    if     (minDist == ptlDist) return ptl;
    else if(minDist == ptrDist) return ptr;
    else if(minDist == pblDist) return pbl;
    else if(minDist == pbrDist) return pbr;

    return scenePos();
}

QList<QPointF> RectObject::allGripPoints()
{
    QList<QPointF> gripPoints;
    gripPoints << objectTopLeft() << objectTopRight() << objectBottomLeft() << objectBottomRight();
    return gripPoints;
}

void RectObject::gripEdit(const QPointF& before, const QPointF& after)
{
    QPointF delta = after-before;
    if     (before == objectTopLeft())     { setObjectRect(after.x(), after.y(), objectWidth()-delta.x(), objectHeight()-delta.y()); }
    else if(before == objectTopRight())    { setObjectRect(objectTopLeft().x(), objectTopLeft().y()+delta.y(), objectWidth()+delta.x(), objectHeight()-delta.y()); }
    else if(before == objectBottomLeft())  { setObjectRect(objectTopLeft().x()+delta.x(), objectTopLeft().y(), objectWidth()-delta.x(), objectHeight()+delta.y()); }
    else if(before == objectBottomRight()) { setObjectRect(objectTopLeft().x(), objectTopLeft().y(), objectWidth()+delta.x(), objectHeight()+delta.y()); }
}

QPainterPath RectObject::objectSavePath() const
{
    QPainterPath path;
    QRectF r = rect();
    path.moveTo(r.bottomLeft());
    path.lineTo(r.bottomRight());
    path.lineTo(r.topRight());
    path.lineTo(r.topLeft());
    path.lineTo(r.bottomLeft());

    float s = scale();
    QTransform trans;
    trans.rotate(rotation());
    trans.scale(s,s);
    return trans.map(path);
}


TextSingleObject::TextSingleObject(const QString& str, float x, float y, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("TextSingleObject Constructor()");
    init(str, x, y, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

TextSingleObject::TextSingleObject(TextSingleObject* obj, QGraphicsItem* parent) : BaseObject(parent)
{
    debug_message("TextSingleObject Constructor()");
    if (obj) {
        objTextFont = obj->objTextFont;
        obj_text = obj->obj_text;
        setRotation(obj->rotation());
        setObjectText(obj->objText);
        init(obj->objText, obj->objectX(), obj->objectY(), obj->objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setScale(obj->scale());
    }
}

TextSingleObject::~TextSingleObject()
{
    debug_message("TextSingleObject Destructor()");
}

void TextSingleObject::init(const QString& str, float x, float y, unsigned int rgb, Qt::PenStyle lineType)
{
    setData(OBJ_TYPE, type());
    setData(OBJ_NAME, obj_names[OBJ_TYPE_TEXTSINGLE]);

    setFlag(QGraphicsItem::ItemIsSelectable, 1);

    objTextJustify = "Left"; /*TODO: set the justification properly*/

    setObjectText(str);
    setObjectPos(x,y);
    setObjectColor(rgb);
    setObjectLineType(lineType);
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objectPen());
}

QStringList TextSingleObject::objectTextJustifyList() const
{
    QStringList justifyList;
    justifyList << "Left" << "Center" << "Right" /* TODO: << "Aligned" */ << "Middle" /* TODO: << "Fit" */ ;
    justifyList << "Top Left" << "Top Center" << "Top Right";
    justifyList << "Middle Left" << "Middle Center" << "Middle Right";
    justifyList << "Bottom Left" << "Bottom Center" << "Bottom Right";
    return justifyList;
}

void TextSingleObject::setObjectText(const QString& str)
{
    objText = str;
    QPainterPath textPath;
    QFont font;
    font.setFamily(objTextFont);
    font.setPointSizeF(obj_text.size);
    font.setBold(obj_text.bold);
    font.setItalic(obj_text.italic);
    font.setUnderline(obj_text.underline);
    font.setStrikeOut(obj_text.strikeout);
    font.setOverline(obj_text.overline);
    textPath.addText(0, 0, font, str);

    /*Translate the path based on the justification*/
    QRectF jRect = textPath.boundingRect();
    if     (objTextJustify == "Left")          { textPath.translate(-jRect.left(), 0); }
    else if(objTextJustify == "Center")        { textPath.translate(-jRect.center().x(), 0); }
    else if(objTextJustify == "Right")         { textPath.translate(-jRect.right(), 0); }
    else if(objTextJustify == "Aligned")       { } /*TODO: TextSingleObject Aligned Justification*/
    else if(objTextJustify == "Middle")        { textPath.translate(-jRect.center()); }
    else if(objTextJustify == "Fit")           { } /*TODO: TextSingleObject Fit Justification*/
    else if(objTextJustify == "Top Left")      { textPath.translate(-jRect.topLeft()); }
    else if(objTextJustify == "Top Center")    { textPath.translate(-jRect.center().x(), -jRect.top()); }
    else if(objTextJustify == "Top Right")     { textPath.translate(-jRect.topRight()); }
    else if(objTextJustify == "Middle Left")   { textPath.translate(-jRect.left(), -jRect.top()/2.0); }
    else if(objTextJustify == "Middle Center") { textPath.translate(-jRect.center().x(), -jRect.top()/2.0); }
    else if(objTextJustify == "Middle Right")  { textPath.translate(-jRect.right(), -jRect.top()/2.0); }
    else if(objTextJustify == "Bottom Left")   { textPath.translate(-jRect.bottomLeft()); }
    else if(objTextJustify == "Bottom Center") { textPath.translate(-jRect.center().x(), -jRect.bottom()); }
    else if(objTextJustify == "Bottom Right")  { textPath.translate(-jRect.bottomRight()); }

    /*Backward or Upside Down*/
    if(obj_text.backward || obj_text.upsidedown)
    {
        float horiz = 1.0;
        float vert = 1.0;
        if(obj_text.backward) horiz = -1.0;
        if(obj_text.upsidedown) vert = -1.0;

        QPainterPath flippedPath;

        QPainterPath::Element element;
        QPainterPath::Element P2;
        QPainterPath::Element P3;
        QPainterPath::Element P4;
        for(int i = 0; i < textPath.elementCount(); ++i)
        {
            element = textPath.elementAt(i);
            if(element.isMoveTo())
            {
                flippedPath.moveTo(horiz * element.x, vert * element.y);
            }
            else if(element.isLineTo())
            {
                flippedPath.lineTo(horiz * element.x, vert * element.y);
            }
            else if(element.isCurveTo())
            {
                                              /* start point P1 is not needed*/
                P2 = textPath.elementAt(i);   /* control point*/
                P3 = textPath.elementAt(i+1); /* control point*/
                P4 = textPath.elementAt(i+2); /* end point*/

                flippedPath.cubicTo(horiz * P2.x, vert * P2.y,
                                    horiz * P3.x, vert * P3.y,
                                    horiz * P4.x, vert * P4.y);
            }
        }
        objTextPath = flippedPath;
    }
    else
        objTextPath = textPath;

    /*Add the grip point to the shape path*/
    QPainterPath gripPath = objTextPath;
    gripPath.connectPath(objTextPath);
    gripPath.addRect(-0.00000001, -0.00000001, 0.00000002, 0.00000002);
    setObjectPath(gripPath);
}

void TextSingleObject::setObjectTextFont(const QString& font)
{
    objTextFont = font;
    setObjectText(objText);
}

void TextSingleObject::setObjectTextJustify(const QString& justify)
{
    /*Verify the string is a valid option*/
    if (justify == "Left") {
        objTextJustify = justify;
    }
    else if(justify == "Center")        { objTextJustify = justify; }
    else if(justify == "Right")         { objTextJustify = justify; }
    else if(justify == "Aligned")       { objTextJustify = justify; }
    else if(justify == "Middle")        { objTextJustify = justify; }
    else if(justify == "Fit")           { objTextJustify = justify; }
    else if(justify == "Top Left")      { objTextJustify = justify; }
    else if(justify == "Top Center")    { objTextJustify = justify; }
    else if(justify == "Top Right")     { objTextJustify = justify; }
    else if(justify == "Middle Left")   { objTextJustify = justify; }
    else if(justify == "Middle Center") { objTextJustify = justify; }
    else if(justify == "Middle Right")  { objTextJustify = justify; }
    else if(justify == "Bottom Left")   { objTextJustify = justify; }
    else if(justify == "Bottom Center") { objTextJustify = justify; }
    else if(justify == "Bottom Right")  { objTextJustify = justify; }
    else                                { objTextJustify = "Left";  } /*Default*/
    setObjectText(objText);
}

void TextSingleObject::setObjectTextSize(float size)
{
    obj_text.size = size;
    setObjectText(objText);
}

void TextSingleObject::setObjectTextBold(int val)
{
    obj_text.bold = val;
    setObjectText(objText);
}

void TextSingleObject::setObjectTextItalic(int val)
{
    obj_text.italic = val;
    setObjectText(objText);
}

void TextSingleObject::setObjectTextUnderline(int val)
{
    obj_text.underline = val;
    setObjectText(objText);
}

void TextSingleObject::setObjectTextStrikeOut(int val)
{
    obj_text.strikeout = val;
    setObjectText(objText);
}

void TextSingleObject::setObjectTextOverline(int val)
{
    obj_text.overline = val;
    setObjectText(objText);
}

void TextSingleObject::setObjectTextBackward(int val)
{
    obj_text.backward = val;
    setObjectText(objText);
}

void TextSingleObject::setObjectTextUpsideDown(int val)
{
    obj_text.upsidedown = val;
    setObjectText(objText);
}

void TextSingleObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/)
{
    QGraphicsScene* objScene = scene();
    if(!objScene) return;

    QPen paintPen = pen();
    painter->setPen(paintPen);
    updateRubber(painter);
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen);

    painter->drawPath(objTextPath);
}

void TextSingleObject::updateRubber(QPainter* painter)
{
    int rubberMode = objectRubberMode();
    if (rubberMode == OBJ_RUBBER_TEXTSINGLE) {
        setObjectTextFont(objectRubberText("TEXT_FONT"));
        setObjectTextJustify(objectRubberText("TEXT_JUSTIFY"));
        setObjectPos(objectRubberPoint("TEXT_POINT"));
        QPointF hr = objectRubberPoint("TEXT_HEIGHT_ROTATION");
        setObjectTextSize(hr.x());
        setRotation(hr.y());
        setObjectText(objectRubberText("TEXT_RAPID"));
    }
    else if(rubberMode == OBJ_RUBBER_GRIP) {
        if (painter) {
            QPointF gripPoint = objectRubberPoint("GRIP_POINT");
            if (gripPoint == scenePos()) {
                painter->drawPath(objectPath().translated(mapFromScene(objectRubberPoint(QString()))-mapFromScene(gripPoint)));
            }

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())));
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR");
        }
    }
}

void TextSingleObject::vulcanize()
{
    debug_message("TextSingleObject vulcanize()");
    updateRubber();

    setObjectRubberMode(OBJ_RUBBER_OFF);
}

/* Returns the closest snap point to the mouse point*/
QPointF TextSingleObject::mouseSnapPoint(const QPointF& mousePoint)
{
    return scenePos();
}

QList<QPointF> TextSingleObject::allGripPoints()
{
    QList<QPointF> gripPoints;
    gripPoints << scenePos();
    return gripPoints;
}

void TextSingleObject::gripEdit(const QPointF& before, const QPointF& after)
{
    if(before == scenePos()) { QPointF delta = after-before; moveBy(delta.x(), delta.y()); }
}

QList<QPainterPath> TextSingleObject::subPathList() const
{
    float s = scale();
    QTransform trans;
    trans.rotate(rotation());
    trans.scale(s,s);

    QList<QPainterPath> pathList;

    QPainterPath path = objTextPath;

    QPainterPath::Element element;
    QList<int> pathMoves;
    int numMoves = 0;

    for(int i = 0; i < path.elementCount(); i++)
    {
        element = path.elementAt(i);
        if(element.isMoveTo())
        {
            pathMoves << i;
            numMoves++;
        }
    }

    pathMoves << path.elementCount();

    for (int p = 0; p < pathMoves.size()-1 && p < numMoves; p++) {
        QPainterPath subPath;
        for (int i = pathMoves.value(p); i < pathMoves.value(p+1); i++) {
            element = path.elementAt(i);
            if (element.isMoveTo()) {
                subPath.moveTo(element.x, element.y);
            }
            else if (element.isLineTo()) {
                subPath.lineTo(element.x, element.y);
            }
            else if (element.isCurveTo()) {
                subPath.cubicTo(path.elementAt(i  ).x, path.elementAt(i  ).y, /*control point 1*/
                                path.elementAt(i+1).x, path.elementAt(i+1).y, /*control point 2*/
                                path.elementAt(i+2).x, path.elementAt(i+2).y); /*end point*/
            }
        }
        pathList.append(trans.map(subPath));
    }

    return pathList;
}

void MainWindow::stub_testing()
{
    QMessageBox::warning(this, tr("Testing Feature"), tr("<b>This feature is in testing.</b>"));
}

void MainWindow::checkForUpdates()
{
    debug_message("checkForUpdates()");
    /*TODO: Check website for new versions, commands, etc...*/
}

void MainWindow::selectAll()
{
    debug_message("selectAll()");
    View* gview = activeView();
    if(gview) { gview->selectAll(); }
}

QString MainWindow::platformString()
{
    /*TODO: Append QSysInfo to string where applicable.*/
    QString os;
    
#if defined(__unix__) || defined(__linux__)
    struct utsname unameData;
    uname(&unameData);
    os = QString(unameData.sysname);
#else
    /* Get windows version. */
    os = QString("Windows");
#endif
    debug_message("Platform: %s", qPrintable(os));
    return os;
}

void MainWindow::designDetails()
{
    QGraphicsScene* scene = activeScene();
    if(scene)
    {
        EmbDetailsDialog dialog(scene, this);
        dialog.exec();
    }
}

void MainWindow::whatsThisContextHelp()
{
    debug_message("whatsThisContextHelp()");
    QWhatsThis::enterWhatsThisMode();
}

void MainWindow::print()
{
    debug_message("print()");
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow());
    if(mdiWin) { mdiWin->print(); }
}

void MainWindow::tipOfTheDay()
{
    debug_message("tipOfTheDay()");

    QString appDir = qApp->applicationDirPath();
    wizardTipOfTheDay = new QDialog();
    QToolButton *button1 = new QToolButton(wizardTipOfTheDay);
    QToolButton *button2 = new QToolButton(wizardTipOfTheDay);
    QToolButton *button3 = new QToolButton(wizardTipOfTheDay);

    ImageWidget* imgBanner = new ImageWidget(appDir + "/images/did-you-know.png", wizardTipOfTheDay);

    QCheckBox* checkBoxTipOfTheDay = new QCheckBox(tr("&Show tips on startup"), wizardTipOfTheDay);
    checkBoxTipOfTheDay->setChecked(settings.general_tip_of_the_day);
    connect(checkBoxTipOfTheDay, SIGNAL(stateChanged(int)), this, SLOT(checkBoxTipOfTheDayStateChanged(int)));

    if (strlen(tips[settings.general_current_tip])==0) {
        settings.general_current_tip = 0;
    }
    labelTipOfTheDay = new QLabel(tips[settings.general_current_tip], wizardTipOfTheDay);
    labelTipOfTheDay->setWordWrap(1);

    button1->setText("&Previous");
    button2->setText("&Next");
    button3->setText("&Close");
    connect(button1, SIGNAL(triggered()), wizardTipOfTheDay, SLOT(wizardTipOfTheDay.close()));
    connect(button2, SIGNAL(triggered()), wizardTipOfTheDay, SLOT(wizardTipOfTheDay.close()));
    connect(button3, SIGNAL(triggered()), wizardTipOfTheDay, SLOT(wizardTipOfTheDay.close()));

    QVBoxLayout* layout = new QVBoxLayout(wizardTipOfTheDay);
    layout->addWidget(imgBanner);
    layout->addStrut(1);
    layout->addWidget(labelTipOfTheDay);
    layout->addStretch(1);
    layout->addWidget(checkBoxTipOfTheDay);
    layout->addStrut(1);
    layout->addWidget(button1);
    layout->addStrut(1);
    layout->addWidget(button2);
    layout->addStrut(1);
    layout->addWidget(button3);

    wizardTipOfTheDay->setLayout(layout);
    wizardTipOfTheDay->setWindowTitle("Tip of the Day");
    wizardTipOfTheDay->setMinimumSize(550, 400);
    wizardTipOfTheDay->exec();
}

void MainWindow::buttonTipOfTheDayClicked(int button)
{
    /*
    debug_message("buttonTipOfTheDayClicked(%d)", button);
    if(button == QWizard::CustomButton1)
    {
        if(settings.general_current_tip > 0)
            settings.general_current_tip--;
        else
            settings.general_current_tip = listTipOfTheDay.size()-1;
        labelTipOfTheDay->setText(listTipOfTheDay.value(settings.general_current_tip));
    }
    else if(button == QWizard::CustomButton2)
    {
        settings.general_current_tip++;
        if(settings.general_current_tip >= listTipOfTheDay.size())
            settings.general_current_tip = 0;
        labelTipOfTheDay->setText(listTipOfTheDay.value(settings.general_current_tip));
    }
    else if(button == QWizard::CustomButton3)
    {
        wizardTipOfTheDay->close();
    }
    */
}

void MainWindow::help()
{
    debug_message("help()");

    /* display in a custom widget instead */
    /* Open the HTML Help in the default browser
    QUrl helpURL("file:///" + qApp->applicationDirPath() + "/help/doc-index.html");
    QDesktopServices::openUrl(helpURL);
    */

    /*TODO: This is how to start an external program. Use this elsewhere...*/
    /*QString program = "firefox";*/
    /*QStringList arguments;*/
    /*arguments << "help/commands.html";*/
    /*QProcess *myProcess = new QProcess(this);*/
    /*myProcess->start(program, arguments);*/
}

/* this wrapper connects the signal to the C-style actuator */
void MainWindow::actions()
{
    int i;
    char call[100];
    QObject *obj = sender();
    QString caller = obj->objectName();
    for (i=0; action_list[i].abbreviation[0]; i++) {
        if (caller == action_list[i].abbreviation) {
            call[0] = (char)i;
            call[1] = 0;
            actuator(call);
            return;
        }
    }
}

void main_undo(void)
{
    debug_message("undo()");
    if (undo_history_position > 0) {
        char *last = undo_history[undo_history_position];
        undo_history_position--;
        printf("undo_history_position = %d\n", undo_history_position);
        printf("undo_history_length = %d\n", undo_history_length);
        
        /* Create the reverse action from the last action and apply with
         * the main actuator.
         */
        switch (last[0]) {
        case ACTION_donothing:
        default:
            debug_message("The last action has no undo candidate.");
            break;
        }
        actuator(last);
    }
}

void main_redo(void)
{
    char undo_call[100];
    debug_message("redo()");
    if (undo_history_position < undo_history_length) {
        undo_history_position++;
        printf("undo_history_position = %d\n", undo_history_position);
        printf("undo_history_length = %d\n", undo_history_length);
        strcpy(undo_call, undo_history[undo_history_position]);
        /* set reverse flag */
        strcat(undo_call, " -r");
        actuator(undo_call);
    }
}

int MainWindow::isShiftPressed()
{
    return settings.shiftKeyPressedState;
}

void MainWindow::setShiftPressed()
{
    settings.shiftKeyPressedState = 1;
}

void MainWindow::setShiftReleased()
{
    settings.shiftKeyPressedState = 0;
}

/* Icons */
void MainWindow::iconResize(int iconSize)
{
    this->setIconSize(QSize(iconSize, iconSize));
    layerSelector->     setIconSize(QSize(iconSize*4, iconSize));
    colorSelector->     setIconSize(QSize(iconSize, iconSize));
    linetypeSelector->  setIconSize(QSize(iconSize*4, iconSize));
    lineweightSelector->setIconSize(QSize(iconSize*4, iconSize));
    /*set the minimum combobox width so the text is always readable*/
    layerSelector->     setMinimumWidth(iconSize*4);
    colorSelector->     setMinimumWidth(iconSize*2);
    linetypeSelector->  setMinimumWidth(iconSize*4);
    lineweightSelector->setMinimumWidth(iconSize*4);

    /* TODO: low-priority:
     * open app with iconSize set to 128. resize the icons to a smaller size. */

    settings.general_icon_size = iconSize;
}

MdiWindow* MainWindow::activeMdiWindow()
{
    debug_message("activeMdiWindow()");
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow());
    return mdiWin;
}

View* MainWindow::activeView()
{
    debug_message("activeView()");
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow());
    if(mdiWin)
    {
        View* v = mdiWin->getView();
        return v;
    }
    return 0;
}

QGraphicsScene* MainWindow::activeScene()
{
    debug_message("activeScene()");
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow());
    if(mdiWin)
    {
        QGraphicsScene* s = mdiWin->getScene();
        return s;
    }
    return 0;
}

void MainWindow::updateAllViewScrollBars(int val)
{
    QList<QMdiSubWindow*> windowList = mdiArea->subWindowList();
    for(int i = 0; i < windowList.count(); ++i)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i));
        if(mdiWin) { mdiWin->showViewScrollBars(val); }
    }
}

void MainWindow::updateAllViewCrossHairColors(unsigned int color)
{
    QList<QMdiSubWindow*> windowList = mdiArea->subWindowList();
    for(int i = 0; i < windowList.count(); ++i)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i));
        if(mdiWin) { mdiWin->setViewCrossHairColor(color); }
    }
}

void MainWindow::updateAllViewBackgroundColors(unsigned int color)
{
    QList<QMdiSubWindow*> windowList = mdiArea->subWindowList();
    for(int i = 0; i < windowList.count(); ++i)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i));
        if(mdiWin) { mdiWin->setViewBackgroundColor(color); }
    }
}

void MainWindow::updateAllViewSelectBoxColors(unsigned int colorL, unsigned int fillL, unsigned int colorR, unsigned int fillR, int alpha)
{
    QList<QMdiSubWindow*> windowList = mdiArea->subWindowList();
    for(int i = 0; i < windowList.count(); ++i)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i));
        if(mdiWin) { mdiWin->setViewSelectBoxColors(colorL, fillL, colorR, fillR, alpha); }
    }
}

void MainWindow::updateAllViewGridColors(unsigned int color)
{
    QList<QMdiSubWindow*> windowList = mdiArea->subWindowList();
    for(int i = 0; i < windowList.count(); ++i)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i));
        if(mdiWin) { mdiWin->setViewGridColor(color); }
    }
}

void MainWindow::updateAllViewRulerColors(unsigned int color)
{
    QList<QMdiSubWindow*> windowList = mdiArea->subWindowList();
    for(int i = 0; i < windowList.count(); ++i)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i));
        if(mdiWin) { mdiWin->setViewRulerColor(color); }
    }
}

void MainWindow::updatePickAddMode(int val)
{
    settings.selection_mode_pickadd = val;
    dockPropEdit->updatePickAddModeButton(val);
}

void MainWindow::pickAddModeToggled()
{
    int val = !settings.selection_mode_pickadd;
    updatePickAddMode(val);
}

void MainWindow::layerSelectorIndexChanged(int index)
{
    debug_message("layerSelectorIndexChanged(%d)", index);
}

void MainWindow::colorSelectorIndexChanged(int index)
{
    debug_message("colorSelectorIndexChanged(%d)", index);

    QComboBox* comboBox = qobject_cast<QComboBox*>(sender());
    unsigned int newColor;
    if(comboBox)
    {
        bool ok = 0;
        /*TODO: Handle ByLayer and ByBlock and Other...*/
        newColor = comboBox->itemData(index).toUInt(&ok);
        if(!ok)
            QMessageBox::warning(this, tr("Color Selector Conversion Error"), tr("<b>An error has occurred while changing colors.</b>"));
    }
    else
        QMessageBox::warning(this, tr("Color Selector Pointer Error"), tr("<b>An error has occurred while changing colors.</b>"));

    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow());
    if(mdiWin) { mdiWin->currentColorChanged(newColor); }
}

void MainWindow::linetypeSelectorIndexChanged(int index)
{
    debug_message("linetypeSelectorIndexChanged(%d)", index);
}

void MainWindow::lineweightSelectorIndexChanged(int index)
{
    debug_message("lineweightSelectorIndexChanged(%d)", index);
}

void MainWindow::textFontSelectorCurrentFontChanged(const QFont& font)
{
    debug_message("textFontSelectorCurrentFontChanged()");
    textFontSelector->setCurrentFont(QFont(font.family()));
    strcpy(settings.text_font, font.family().toLocal8Bit().constData());
}

void MainWindow::textSizeSelectorIndexChanged(int index)
{
    debug_message("textSizeSelectorIndexChanged(%d)", index);
    settings.text_style.size = fabs(textSizeSelector->itemData(index).toReal()); /*TODO: check that the toReal() conversion is ok*/
}

QString MainWindow::textFont()
{
    return settings.text_font;
}

void MainWindow::setTextSize(float num)
{
    settings.text_style.size = fabs(num);
    int index = textSizeSelector->findText("Custom", Qt::MatchContains);
    if(index != -1)
        textSizeSelector->removeItem(index);
    textSizeSelector->addItem("Custom " + QString().setNum(num, 'f', 2) + " pt", num);
    index = textSizeSelector->findText("Custom", Qt::MatchContains);
    if(index != -1)
        textSizeSelector->setCurrentIndex(index);
}

QString MainWindow::getCurrentLayer()
{
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow());
    if(mdiWin) { return mdiWin->getCurrentLayer(); }
    return "0";
}

unsigned int MainWindow::getCurrentColor()
{
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow());
    if(mdiWin) { return mdiWin->getCurrentColor(); }
    return 0; /*TODO: return color ByLayer*/
}

QString MainWindow::getCurrentLineType()
{
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow());
    if(mdiWin) { return mdiWin->getCurrentLineType(); }
    return "ByLayer";
}

QString MainWindow::getCurrentLineWeight()
{
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow());
    if(mdiWin) { return mdiWin->getCurrentLineWeight(); }
    return "ByLayer";
}

void MainWindow::deletePressed()
{
    debug_message("deletePressed()");
    QApplication::setOverrideCursor(Qt::WaitCursor);
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow());
    if(mdiWin) { mdiWin->deletePressed(); }
    QApplication::restoreOverrideCursor();
}

void MainWindow::escapePressed()
{
    debug_message("escapePressed()");
    QApplication::setOverrideCursor(Qt::WaitCursor);
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow());
    if(mdiWin) { mdiWin->escapePressed(); }
    QApplication::restoreOverrideCursor();

    View* gview = activeView();
    if(gview)
    {
        gview->clearRubberRoom();
        gview->previewOff();
        gview->disableMoveRapidFire();
    }
}

void toggleGrid()
{
    debug_message("toggleGrid()");
    status_bar[STATUS_GRID]->toggle();
}

void toggleRuler()
{
    debug_message("toggleRuler()");
    status_bar[STATUS_RULER]->toggle();
}

void toggleLwt()
{
    debug_message("toggleLwt()");
    status_bar[STATUS_LWT]->toggle();
}

void MainWindow::enableMoveRapidFire()
{
    View* gview = activeView();
    if (gview) gview->enableMoveRapidFire();
}

void MainWindow::disableMoveRapidFire()
{
    View* gview = activeView();
    if(gview) gview->disableMoveRapidFire();
}

void MainWindow::nativeAddTextSingle(const QString& str, float x, float y, float rot, int fill, int rubberMode)
{
    View* gview = activeView();
    QGraphicsScene* gscene = gview->scene();
    if(gview && gscene)
    {
        TextSingleObject* obj = new TextSingleObject(str, x, -y, getCurrentColor());
        obj->objTextFont = settings.text_font;
        obj->obj_text = settings.text_style;
        obj->setObjectText(obj->objText);
        obj->setRotation(-rot);
        /*TODO: single line text fill*/
        obj->setObjectRubberMode(rubberMode);
        if (rubberMode) {
            gview->addToRubberRoom(obj);
            gscene->addItem(obj);
            gscene->update();
        }
        else {
        }
    }
}

void MainWindow::nativeAddLine(float x1, float y1, float x2, float y2, float rot, int rubberMode)
{
    View* gview = activeView();
    QGraphicsScene* gscene = gview->scene();
    if(gview && gscene)
    {
        LineObject* obj = new LineObject(x1, -y1, x2, -y2, getCurrentColor());
        obj->setRotation(-rot);
        obj->setObjectRubberMode(rubberMode);
        if(rubberMode)
        {
            gview->addToRubberRoom(obj);
            gscene->addItem(obj);
            gscene->update();
        }
        else
        {
        }
    }
}

void MainWindow::nativeAddRectangle(float x, float y, float w, float h, float rot, int fill, int rubberMode)
{
    View* gview = activeView();
    QGraphicsScene* gscene = gview->scene();
    if(gview && gscene)
    {
        RectObject* obj = new RectObject(x, -y, w, -h, getCurrentColor());
        obj->setRotation(-rot);
        obj->setObjectRubberMode(rubberMode);
        /*TODO: rect fill*/
        if (rubberMode) {
            gview->addToRubberRoom(obj);
            gscene->addItem(obj);
            gscene->update();
        }
        else {
        }
    }
}

void MainWindow::nativeAddArc(float startX, float startY, float midX, float midY, float endX, float endY, int rubberMode)
{
    View* gview = activeView();
    QGraphicsScene* scene = activeScene();
    if(gview && scene)
    {
        ArcObject* arcObj = new ArcObject(startX, -startY, midX, -midY, endX, -endY, getCurrentColor());
        arcObj->setObjectRubberMode(rubberMode);
        if(rubberMode) gview->addToRubberRoom(arcObj);
        scene->addItem(arcObj);
        scene->update();
    }
}

void MainWindow::nativeAddCircle(float centerX, float centerY, float radius, int fill, int rubberMode)
{
    View* gview = activeView();
    QGraphicsScene* gscene = gview->scene();
    if (gview && gscene) {
        CircleObject* obj = new CircleObject(centerX, -centerY, radius, getCurrentColor());
        obj->setObjectRubberMode(rubberMode);
        /*TODO: circle fill*/
        if(rubberMode)
        {
            gview->addToRubberRoom(obj);
            gscene->addItem(obj);
            gscene->update();
        }
        else
        {
        }
    }
}

void MainWindow::nativeAddEllipse(float centerX, float centerY, float width, float height, float rot, int fill, int rubberMode)
{
    View* gview = activeView();
    QGraphicsScene* gscene = gview->scene();
    if (gview && gscene) {
        EllipseObject* obj = new EllipseObject(centerX, -centerY, width, height, getCurrentColor());
        obj->setRotation(-rot);
        obj->setObjectRubberMode(rubberMode);
        /*TODO: ellipse fill*/
        if(rubberMode)
        {
            gview->addToRubberRoom(obj);
            gscene->addItem(obj);
            gscene->update();
        }
        else
        {
        }
    }
}

void MainWindow::nativeAddPoint(float x, float y)
{
    View* gview = activeView();
    if (gview) {
        PointObject* obj = new PointObject(x, -y, getCurrentColor());
    }
}

/*NOTE: This native is different than the rest in that the Y+ is down (scripters need not worry about this)*/
void MainWindow::nativeAddPolygon(float startX, float startY, const QPainterPath& p, int rubberMode)
{
    View* gview = activeView();
    QGraphicsScene* gscene = gview->scene();
    if (gview && gscene) {
        PolygonObject* obj = new PolygonObject(startX, startY, p, getCurrentColor());
        obj->setObjectRubberMode(rubberMode);
        if(rubberMode)
        {
            gview->addToRubberRoom(obj);
            gscene->addItem(obj);
            gscene->update();
        }
        else
        {
        }
    }
}

/*NOTE: This native is different than the rest in that the Y+ is down (scripters need not worry about this)*/
void MainWindow::nativeAddPolyline(float startX, float startY, const QPainterPath& p, int rubberMode)
{
    View* gview = activeView();
    QGraphicsScene* gscene = gview->scene();
    if(gview && gscene)
    {
        PolylineObject* obj = new PolylineObject(startX, startY, p, getCurrentColor());
        obj->setObjectRubberMode(rubberMode);
        if(rubberMode)
        {
            gview->addToRubberRoom(obj);
            gscene->addItem(obj);
            gscene->update();
        }
        else
        {
        }
    }
}

void MainWindow::nativeAddDimLeader(float x1, float y1, float x2, float y2, float rot, int rubberMode)
{
    View* gview = activeView();
    QGraphicsScene* gscene = gview->scene();
    if(gview && gscene) {
        DimLeaderObject* obj = new DimLeaderObject(x1, -y1, x2, -y2, getCurrentColor());
        obj->setRotation(-rot);
        obj->setObjectRubberMode(rubberMode);
        if(rubberMode)
        {
            gview->addToRubberRoom(obj);
            gscene->addItem(obj);
            gscene->update();
        }
        else
        {
        }
    }
}

float MainWindow::nativeCalculateAngle(float x1, float y1, float x2, float y2)
{
    return QLineF(x1, -y1, x2, -y2).angle();
}

float MainWindow::nativeCalculateDistance(float x1, float y1, float x2, float y2)
{
    return QLineF(x1, y1, x2, y2).length();
}

void MainWindow::fill_menu(int menu_id)
{
    int i;
    debug_message("MainWindow creating %s", menu_label[menu_id]);
    menuBar()->addMenu(menu[menu_id]);
    for (i=0; menus[menu_id][i]>=-1; i++) {
        if (menus[menu_id][i] >= 0) {
            menu[menu_id]->addAction(actionHash.value(menus[menu_id][i]));
        }
        else {
            menu[menu_id]->addSeparator();
        }
    }
}

/* nativePerpendicularDistance
    This is currently causing a bug and is going to be replaced with a libembroidery function.
    QLineF line(x1, y1, x2, y2);
    QLineF norm = line.normalVector();
    float dx = px-x1;
    float dy = py-y1;
    norm.translate(dx, dy);
    QPointF iPoint;
    norm.intersects(line, &iPoint);
    return QLineF(px, py, iPoint.x(), iPoint.y()).length();
*/

MainWindow::MainWindow() : QMainWindow(0)
{
    char current_path[1000];
    int i;

    QString appDir = qApp->applicationDirPath();
    readSettings();

    for (i=0; i<nFolders; i++) {
        app_dir(current_path, i);
        if (!file_exists) {
            QMessageBox::critical(this, tr("Path Error"), tr("Cannot locate: ") + current_path);
        }
    }

    QString lang = settings.general_language;
    qDebug("language: %s", qPrintable(lang));
    if(lang == "system")
        lang = QLocale::system().languageToString(QLocale::system().language()).toLower();

    /*Load translations for the Embroidermodder 2 GUI*/
    QTranslator translatorEmb;
    app_dir(current_path, translations_folder);
    translatorEmb.load(QString(current_path) + "/embroidermodder2_" + lang);
    qApp->installTranslator(&translatorEmb);

    /*Load translations for the commands*/
    QTranslator translatorCmd;
    translatorCmd.load(QDir::toNativeSeparators(QString(current_path) + lang + "/commands_" + lang));
    qApp->installTranslator(&translatorCmd);

    /*Load translations provided by Qt - this covers dialog buttons and other common things.*/
    QTranslator translatorQt;
    translatorQt.load("qt_" + QLocale::system().name(), QLibraryInfo::location(QLibraryInfo::TranslationsPath)); /*TODO: ensure this always loads, ship a copy of this with the app*/
    qApp->installTranslator(&translatorQt);

    /*Init*/
    mainWin = this;
    for (i=0; i<N_MENUS; i++) {
        menu[i] = new QMenu(tr(menu_label[i]), this);
    }
    for (i=0; i<N_TOOLBARS; i++) {
        toolbar[i] = addToolBar(tr(toolbar_label[i]));
    }
    /*Selectors*/
    layerSelector = new QComboBox(this);
    colorSelector = new QComboBox(this);
    linetypeSelector = new QComboBox(this);
    lineweightSelector = new QComboBox(this);
    textFontSelector = new QFontComboBox(this);
    textSizeSelector = new QComboBox(this);

    numOfDocs = 0;
    docIndex = 0;

    settings.shiftKeyPressedState = 0;

    setWindowIcon(loadIcon(icon_app));
    setMinimumSize(800, 480); /*Require Minimum WVGA*/

    loadFormats();

    /*create the mdiArea*/
    QFrame* vbox = new QFrame(this);
    QVBoxLayout* layout = new QVBoxLayout(vbox);
    layout->setContentsMargins(QMargins());
    vbox->setFrameStyle(QFrame::StyledPanel | QFrame::Sunken);
    mdiArea = new MdiArea(this, vbox);
    mdiArea->useBackgroundLogo(settings.general_mdi_bg_use_logo);
    mdiArea->useBackgroundTexture(settings.general_mdi_bg_use_texture);
    mdiArea->useBackgroundColor(settings.general_mdi_bg_use_color);
    mdiArea->setBackgroundLogo(settings.general_mdi_bg_logo);
    mdiArea->setBackgroundTexture(settings.general_mdi_bg_texture);
    mdiArea->setBackgroundColor(QColor(settings.general_mdi_bg_color));
    mdiArea->setViewMode(QMdiArea::TabbedView);
    mdiArea->setHorizontalScrollBarPolicy(Qt::ScrollBarAsNeeded);
    mdiArea->setVerticalScrollBarPolicy(Qt::ScrollBarAsNeeded);
    mdiArea->setActivationOrder(QMdiArea::ActivationHistoryOrder);
    layout->addWidget(mdiArea);
    setCentralWidget(vbox);

    /*setDockOptions(QMainWindow::AnimatedDocks | QMainWindow::AllowTabbedDocks | QMainWindow::VerticalTabs);*/
    /* TODO: Load these from settings */
    /* tabifyDockWidget(dockPropEdit, dockUndoEdit); */
    /* TODO: load this from settings */

    statusbar = new StatusBar(this, this);
    this->setStatusBar(statusbar);

    debug_message("Creating All Actions...");
    QString appName = QApplication::applicationName();

    for (i=0; action_list[i].abbreviation[0]; i++) {
        QAction *ACTION = new QAction(loadIcon(action_list[i].icon), action_list[i].menu_name, this);
        /* TODO: Set What's This Context Help to statusTip for now so there is some infos there.*/
        /* Make custom What's This Context Help popup with more descriptive help than just*/
        /* the status bar/tip one liner(short but not real long) with a hyperlink in the custom popup*/
        /* at the bottom to open full help file description. Ex: like wxPython AGW's SuperToolTip.*/
        /* TODO: Finish All Commands ... <.<*/

        /*
        if(icon == "windowcascade") {
            connect(ACTION, SIGNAL(triggered()), mdiArea, SLOT(cascade()));
        }
        else if(icon == "windowtile") {
            connect(ACTION, SIGNAL(triggered()), mdiArea, SLOT(tile()));
        }
        else if(icon == "windowclose") {
            ACTION->setShortcut(QKeySequence::Close);
            connect(ACTION, SIGNAL(triggered()), this, SLOT(onCloseWindow()));
        }
        else if(icon == "windowcloseall") {
            connect(ACTION, SIGNAL(triggered()), mdiArea, SLOT(closeAllSubWindows()));
        }
        else if(icon == "windownext") {
            connect(ACTION, SIGNAL(triggered()), mdiArea, SLOT(activateNextSubWindow()));
        }
        else if(icon == "windowprevious") {
            connect(ACTION, SIGNAL(triggered()), mdiArea, SLOT(activatePreviousSubWindow()));
        }
        else if(icon == "textbold" || icon == "textitalic"
            || icon == "textunderline" || icon == "textstrikeout"
            || icon == "textoverline") {
            ACTION->setCheckable(1);
        }
        */

        if (strlen(action_list[i].shortcut)>0) {
            ACTION->setShortcut(QKeySequence(action_list[i].shortcut));
        }
        ACTION->setStatusTip(action_list[i].description);
        ACTION->setObjectName(action_list[i].abbreviation);
        ACTION->setWhatsThis(action_list[i].description);
        connect(ACTION, SIGNAL(triggered()), this, SLOT(actions()));
        actionHash.insert(i, ACTION);
    }

    actionHash.value(ACTION_windowclose)->setEnabled(numOfDocs > 0);
    actionHash.value(ACTION_designdetails)->setEnabled(numOfDocs > 0);

    /* ---------------------------------------------------------------------- */

    debug_message("MainWindow createAllMenus()");
    
    debug_message("MainWindow createFileMenu()");
    menuBar()->addMenu(menu[FILE_MENU]);
    menu[FILE_MENU]->addAction(actionHash.value(ACTION_new));
    menu[FILE_MENU]->addSeparator();
    menu[FILE_MENU]->addAction(actionHash.value(ACTION_open));

    menu[FILE_MENU]->addMenu(menu[RECENT_MENU]);
    connect(menu[RECENT_MENU], SIGNAL(aboutToShow()), this, SLOT(recentMenuAboutToShow()));
    /* Do not allow the Recent Menu to be torn off. It's a pain in the ass to maintain. */
    menu[RECENT_MENU]->setTearOffEnabled(0);

    menu[FILE_MENU]->addSeparator();
    menu[FILE_MENU]->addAction(actionHash.value(ACTION_save));
    menu[FILE_MENU]->addAction(actionHash.value(ACTION_saveas));
    menu[FILE_MENU]->addSeparator();
    menu[FILE_MENU]->addAction(actionHash.value(ACTION_print));
    menu[FILE_MENU]->addSeparator();
    menu[FILE_MENU]->addAction(actionHash.value(ACTION_windowclose));
    menu[FILE_MENU]->addSeparator();
    menu[FILE_MENU]->addAction(actionHash.value(ACTION_designdetails));
    menu[FILE_MENU]->addSeparator();

    menu[FILE_MENU]->addAction(actionHash.value(ACTION_exit));
    menu[FILE_MENU]->setTearOffEnabled(0);

    /* ---------------------------------------------------------------------- */

    debug_message("MainWindow createmenu[EDIT_MENU]()");
    menuBar()->addMenu(menu[EDIT_MENU]);
    menu[EDIT_MENU]->addAction(actionHash.value(ACTION_undo));
    menu[EDIT_MENU]->addAction(actionHash.value(ACTION_redo));
    menu[EDIT_MENU]->addSeparator();
    menu[EDIT_MENU]->addAction(actionHash.value(ACTION_cut));
    menu[EDIT_MENU]->addAction(actionHash.value(ACTION_copy));
    menu[EDIT_MENU]->addAction(actionHash.value(ACTION_paste));
    menu[EDIT_MENU]->addSeparator();
    menu[EDIT_MENU]->setTearOffEnabled(1);

    /* ---------------------------------------------------------------------- */

    debug_message("MainWindow createmenu[VIEW_MENU]()");

    menuBar()->addMenu(menu[VIEW_MENU]);
    menu[VIEW_MENU]->addSeparator();
    menu[VIEW_MENU]->addMenu(menu[ZOOM_MENU]);
    menu[ZOOM_MENU]->setIcon(loadIcon(icon_zoom));
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomrealtime));
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomprevious));
    menu[ZOOM_MENU]->addSeparator();
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomwindow));
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomdynamic));
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomscale));
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomcenter));
    menu[ZOOM_MENU]->addSeparator();
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomin));
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomout));
    menu[ZOOM_MENU]->addSeparator();
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomselected));
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomall));
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomextents));
    menu[VIEW_MENU]->addMenu(menu[PAN_MENU]);
    menu[PAN_MENU]->setIcon(loadIcon(icon_pan));
    menu[PAN_MENU]->addAction(actionHash.value(ACTION_panrealtime));
    menu[PAN_MENU]->addAction(actionHash.value(ACTION_panpoint));
    menu[PAN_MENU]->addSeparator();
    menu[PAN_MENU]->addAction(actionHash.value(ACTION_panleft));
    menu[PAN_MENU]->addAction(actionHash.value(ACTION_panright));
    menu[PAN_MENU]->addAction(actionHash.value(ACTION_panup));
    menu[PAN_MENU]->addAction(actionHash.value(ACTION_pandown));
    menu[VIEW_MENU]->addSeparator();
    menu[VIEW_MENU]->addAction(actionHash.value(ACTION_day));
    menu[VIEW_MENU]->addAction(actionHash.value(ACTION_night));
    menu[VIEW_MENU]->addSeparator();

    menu[VIEW_MENU]->setTearOffEnabled(1);
    menu[ZOOM_MENU]->setTearOffEnabled(1);
    menu[PAN_MENU]->setTearOffEnabled(1);

    /* ---------------------------------------------------------------------- */

    debug_message("MainWindow createSettingsMenu()");
    menuBar()->addMenu(menu[SETTINGS_MENU]);
    menu[SETTINGS_MENU]->addAction(actionHash.value(ACTION_settingsdialog));
    menu[SETTINGS_MENU]->addSeparator();
    menu[SETTINGS_MENU]->setTearOffEnabled(1);

    /* ---------------------------------------------------------------------- */

    debug_message("MainWindow createWindowMenu()");
    menuBar()->addMenu(menu[WINDOW_MENU]);
    connect(menu[WINDOW_MENU], SIGNAL(aboutToShow()), this, SLOT(windowMenuAboutToShow()));
    /*Do not allow the Window Menu to be torn off. It's a pain in the ass to maintain.*/
    menu[WINDOW_MENU]->setTearOffEnabled(0);

    /* ---------------------------------------------------------------------- */

    debug_message("MainWindow createHelpMenu()");
    menuBar()->addMenu(menu[HELP_MENU]);
    menu[HELP_MENU]->addAction(actionHash.value(ACTION_help));
    menu[HELP_MENU]->addSeparator();
    menu[HELP_MENU]->addAction(actionHash.value(ACTION_changelog));
    menu[HELP_MENU]->addSeparator();
    menu[HELP_MENU]->addAction(actionHash.value(ACTION_tipoftheday));
    menu[HELP_MENU]->addSeparator();
    menu[HELP_MENU]->addAction(actionHash.value(ACTION_about));
    menu[HELP_MENU]->addSeparator();
    menu[HELP_MENU]->addAction(actionHash.value(ACTION_whatsthis));
    menu[HELP_MENU]->setTearOffEnabled(1);

    /* ---------------------------------------------------------------------- */

    debug_message("MainWindow createAllToolbars()");

    for (i=0; i<N_TOOLBARS; i++) {
        int j;
        char message[100];
        sprintf(message, "MainWindow creating %s\n", toolbar_label[i]);
        debug_message(message);

        toolbar[i]->setObjectName(toolbar_label[i]);

        for (j=0; toolbars[i][j]!=-2; j++) {
            if (toolbars[i][j] >= 0) {
                toolbar[i]->addAction(actionHash.value(toolbars[i][j]));
            }
            else {
                toolbar[i]->addSeparator();
            }
        }

        connect(toolbar[i], SIGNAL(topLevelChanged(int)), this, SLOT(floatingChangedToolBar(int)));
    }

    /* ---------------------------------------------------------------- */
    
    debug_message("MainWindow createLayerToolbar()");

    toolbar[TOOLBAR_LAYER]->setObjectName("toolbarLayer");
    toolbar[TOOLBAR_LAYER]->addAction(actionHash.value(ACTION_makelayercurrent));
    toolbar[TOOLBAR_LAYER]->addAction(actionHash.value(ACTION_layers));

    /*NOTE: Qt4.7 wont load icons without an extension...*/
    /*TODO: Create layer pixmaps by concatenating several icons*/
    layerSelector->addItem(loadIcon(icon_linetypebylayer), "0");
    layerSelector->addItem(loadIcon(icon_linetypebylayer), "1");
    layerSelector->addItem(loadIcon(icon_linetypebylayer), "2");
    layerSelector->addItem(loadIcon(icon_linetypebylayer), "3");
    layerSelector->addItem(loadIcon(icon_linetypebylayer), "4");
    layerSelector->addItem(loadIcon(icon_linetypebylayer), "5");
    layerSelector->addItem(loadIcon(icon_linetypebylayer), "6");
    layerSelector->addItem(loadIcon(icon_linetypebylayer), "7");
    layerSelector->addItem(loadIcon(icon_linetypebylayer), "8");
    layerSelector->addItem(loadIcon(icon_linetypebylayer), "9");
    toolbar[TOOLBAR_LAYER]->addWidget(layerSelector);
    connect(layerSelector, SIGNAL(currentIndexChanged(int)), this, SLOT(layerSelectorIndexChanged(int)));

    toolbar[TOOLBAR_LAYER]->addAction(actionHash.value(ACTION_layerprevious));

    connect(toolbar[TOOLBAR_LAYER], SIGNAL(topLevelChanged(int)), this, SLOT(floatingChangedToolBar(int)));
    
    /* ----------------- */

    debug_message("MainWindow createPropertiesToolbar()");

    toolbar[TOOLBAR_PROPERTIES]->setObjectName("toolbarProperties");

    colorSelector->setFocusProxy(menu[FILE_MENU]);
    /*NOTE: Qt4.7 wont load icons without an extension...*/
    colorSelector->addItem(loadIcon(icon_colorbylayer), "ByLayer");
    colorSelector->addItem(loadIcon(icon_colorbyblock), "ByBlock");
    colorSelector->addItem(loadIcon(icon_colorred), tr("Red"), qRgb(255, 0, 0));
    colorSelector->addItem(loadIcon(icon_coloryellow), tr("Yellow"), qRgb(255,255, 0));
    colorSelector->addItem(loadIcon(icon_colorgreen), tr("Green"), qRgb(0, 255, 0));
    colorSelector->addItem(loadIcon(icon_colorcyan), tr("Cyan"), qRgb(  0,255,255));
    colorSelector->addItem(loadIcon(icon_colorblue), tr("Blue"), qRgb(  0, 0,255));
    colorSelector->addItem(loadIcon(icon_colormagenta), tr("Magenta"), qRgb(255, 0,255));
    colorSelector->addItem(loadIcon(icon_colorwhite), tr("White"), qRgb(255,255,255));
    colorSelector->addItem(loadIcon(icon_colorother), tr("Other..."));
    toolbar[TOOLBAR_PROPERTIES]->addWidget(colorSelector);
    connect(colorSelector, SIGNAL(currentIndexChanged(int)), this, SLOT(colorSelectorIndexChanged(int)));

    toolbar[TOOLBAR_PROPERTIES]->addSeparator();
    linetypeSelector->setFocusProxy(menu[FILE_MENU]);
    /*NOTE: Qt4.7 wont load icons without an extension...*/
    linetypeSelector->addItem(loadIcon(icon_linetypebylayer), "ByLayer");
    linetypeSelector->addItem(loadIcon(icon_linetypebyblock), "ByBlock");
    linetypeSelector->addItem(loadIcon(icon_linetypecontinuous), "Continuous");
    linetypeSelector->addItem(loadIcon(icon_linetypehidden), "Hidden");
    linetypeSelector->addItem(loadIcon(icon_linetypecenter), "Center");
    linetypeSelector->addItem(loadIcon(icon_linetypeother), "Other...");
    toolbar[TOOLBAR_PROPERTIES]->addWidget(linetypeSelector);
    connect(linetypeSelector, SIGNAL(currentIndexChanged(int)), this, SLOT(linetypeSelectorIndexChanged(int)));

    toolbar[TOOLBAR_PROPERTIES]->addSeparator();
    lineweightSelector->setFocusProxy(menu[FILE_MENU]);
    /*NOTE: Qt4.7 wont load icons without an extension...*/
    lineweightSelector->addItem(loadIcon(icon_lineweightbylayer), "ByLayer", -2.00);
    lineweightSelector->addItem(loadIcon(icon_lineweightbyblock), "ByBlock", -1.00);
    lineweightSelector->addItem(loadIcon(icon_lineweightdefault), "Default", 0.00);
    /* TODO: Thread weight is weird. See http://en.wikipedia.org/wiki/Thread_(yarn)#Weight */
    lineweightSelector->addItem(loadIcon(icon_lineweight01), "0.00 mm", 0.00);
    lineweightSelector->addItem(loadIcon(icon_lineweight02), "0.05 mm", 0.05);
    lineweightSelector->addItem(loadIcon(icon_lineweight03), "0.15 mm", 0.15);
    lineweightSelector->addItem(loadIcon(icon_lineweight04), "0.20 mm", 0.20);
    lineweightSelector->addItem(loadIcon(icon_lineweight05), "0.25 mm", 0.25);
    lineweightSelector->addItem(loadIcon(icon_lineweight06), "0.30 mm", 0.30);
    lineweightSelector->addItem(loadIcon(icon_lineweight07), "0.35 mm", 0.35);
    lineweightSelector->addItem(loadIcon(icon_lineweight08), "0.40 mm", 0.40);
    lineweightSelector->addItem(loadIcon(icon_lineweight09), "0.45 mm", 0.45);
    lineweightSelector->addItem(loadIcon(icon_lineweight10), "0.50 mm", 0.50);
    lineweightSelector->addItem(loadIcon(icon_lineweight11), "0.55 mm", 0.55);
    lineweightSelector->addItem(loadIcon(icon_lineweight12), "0.60 mm", 0.60);
    lineweightSelector->addItem(loadIcon(icon_lineweight13), "0.65 mm", 0.65);
    lineweightSelector->addItem(loadIcon(icon_lineweight14), "0.70 mm", 0.70);
    lineweightSelector->addItem(loadIcon(icon_lineweight15), "0.75 mm", 0.75);
    lineweightSelector->addItem(loadIcon(icon_lineweight16), "0.80 mm", 0.80);
    lineweightSelector->addItem(loadIcon(icon_lineweight17), "0.85 mm", 0.85);
    lineweightSelector->addItem(loadIcon(icon_lineweight18), "0.90 mm", 0.90);
    lineweightSelector->addItem(loadIcon(icon_lineweight19), "0.95 mm", 0.95);
    lineweightSelector->addItem(loadIcon(icon_lineweight20), "1.00 mm", 1.00);
    lineweightSelector->addItem(loadIcon(icon_lineweight21), "1.05 mm", 1.05);
    lineweightSelector->addItem(loadIcon(icon_lineweight22), "1.10 mm", 1.10);
    lineweightSelector->addItem(loadIcon(icon_lineweight23), "1.15 mm", 1.15);
    lineweightSelector->addItem(loadIcon(icon_lineweight24), "1.20 mm", 1.20);
    lineweightSelector->setMinimumContentsLength(8);
    /* Prevent dropdown text readability being squish...d. */
    toolbar[TOOLBAR_PROPERTIES]->addWidget(lineweightSelector);
    connect(lineweightSelector, SIGNAL(currentIndexChanged(int)), this, SLOT(lineweightSelectorIndexChanged(int)));

    connect(toolbar[TOOLBAR_PROPERTIES], SIGNAL(topLevelChanged(int)), this, SLOT(floatingChangedToolBar(int)));

    /* ------------------------------------------------------------- */

    debug_message("MainWindow createTextToolbar()");

    toolbar[TOOLBAR_TEXT]->setObjectName("toolbarText");

    toolbar[TOOLBAR_TEXT]->addWidget(textFontSelector);
    textFontSelector->setCurrentFont(QFont(settings.text_font));
    connect(textFontSelector, SIGNAL(currentFontChanged(const QFont&)), this, SLOT(textFontSelectorCurrentFontChanged(const QFont&)));

/* TODO: SEGFAULTING FOR SOME REASON 
    toolbar[TOOLBAR_TEXT]->addAction(actionHash.value(ACTION_textbold));
    actionHash.value(ACTION_textbold)->setChecked(settings.text_style_bold);
    toolbar[TOOLBAR_TEXT]->addAction(actionHash.value(ACTION_textitalic));
    actionHash.value(ACTION_textitalic)->setChecked(settings.text_style_italic);
    toolbar[TOOLBAR_TEXT]->addAction(actionHash.value(ACTION_textunderline));
    actionHash.value(ACTION_textunderline)->setChecked(settings.text_style_underline);
    toolbar[TOOLBAR_TEXT]->addAction(actionHash.value(ACTION_textstrikeout));
    actionHash.value(ACTION_textstrikeout)->setChecked(settings.text_style_strikeout);
    toolbar[TOOLBAR_TEXT]->addAction(actionHash.value(ACTION_textoverline));
    actionHash.value(ACTION_textoverline)->setChecked(settings.text_style_overline);

    textSizeSelector->setFocusProxy(menu[FILE_MENU]);
    textSizeSelector->addItem("6 pt", 6);
    textSizeSelector->addItem("8 pt", 8);
    textSizeSelector->addItem("9 pt", 9);
    textSizeSelector->addItem("10 pt", 10);
    textSizeSelector->addItem("11 pt", 11);
    textSizeSelector->addItem("12 pt", 12);
    textSizeSelector->addItem("14 pt", 14);
    textSizeSelector->addItem("18 pt", 18);
    textSizeSelector->addItem("24 pt", 24);
    textSizeSelector->addItem("30 pt", 30);
    textSizeSelector->addItem("36 pt", 36);
    textSizeSelector->addItem("48 pt", 48);
    textSizeSelector->addItem("60 pt", 60);
    textSizeSelector->addItem("72 pt", 72);
    setTextSize(settings.text_size);
    toolbar[TOOLBAR_TEXT]->addWidget(textSizeSelector);
    connect(textSizeSelector, SIGNAL(currentIndexChanged(int)), this, SLOT(textSizeSelectorIndexChanged(int)));
    */

    connect(toolbar[TOOLBAR_TEXT], SIGNAL(topLevelChanged(int)), this, SLOT(floatingChangedToolBar(int)));

    /* ------------------------------------------------------------ */

    /* Horizontal*/
    toolbar[TOOLBAR_VIEW]->setOrientation(Qt::Horizontal);
    toolbar[TOOLBAR_ZOOM]->setOrientation(Qt::Horizontal);
    toolbar[TOOLBAR_LAYER]->setOrientation(Qt::Horizontal);
    toolbar[TOOLBAR_PROPERTIES]->setOrientation(Qt::Horizontal);
    toolbar[TOOLBAR_TEXT]->setOrientation(Qt::Horizontal);
    /* Top*/
    addToolBarBreak(Qt::TopToolBarArea);
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_FILE]);
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_EDIT]);
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_HELP]);
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_ICON]);
    addToolBarBreak(Qt::TopToolBarArea);
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_ZOOM]);
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_PAN]);
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_VIEW]);
    addToolBarBreak(Qt::TopToolBarArea);
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_LAYER]);
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_PROPERTIES]);
    addToolBarBreak(Qt::TopToolBarArea);
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_TEXT]);

    /*zoomToolBar->setToolButtonStyle(Qt::ToolButtonTextOnly);*/
    /* ---------------------------------------------------------------------- */

    iconResize(settings.general_icon_size);
    updateMenuToolbarStatusbar();

    /*Show date in statusbar after it has been updated*/
    QDate date = QDate::currentDate();
    QString datestr = date.toString("MMMM d, yyyy");
    statusbar->showMessage(datestr);

    showNormal();

    if (settings.general_tip_of_the_day) {
        tipOfTheDay();
    }
}

MainWindow::~MainWindow()
{
    debug_message("MainWindow::Destructor()");

    /*Prevent memory leaks by deleting any unpasted objects*/
    qDeleteAll(cutCopyObjectList.begin(), cutCopyObjectList.end());
    cutCopyObjectList.clear();
}

void MainWindow::recentMenuAboutToShow()
{
    debug_message("MainWindow::recentMenuAboutToShow()");
    menu[RECENT_MENU]->clear();

    QFileInfo recentFileInfo;
    QString recentValue;
    for(int i = 0; i < opensave_recent_list_of_files.size(); ++i)
    {
        /*If less than the max amount of entries add to menu*/
        if(i < settings.opensave_recent_max_files)
        {
            recentFileInfo = QFileInfo(opensave_recent_list_of_files.at(i));
            if(recentFileInfo.exists() && validFileFormat(recentFileInfo.fileName()))
            {
                recentValue.setNum(i+1);
                QAction* rAction;
                if     (recentValue.toInt() >= 1 && recentValue.toInt() <= 9) rAction = new QAction("&" + recentValue + " " + recentFileInfo.fileName(), this);
                else if(recentValue.toInt() == 10)                            rAction = new QAction("1&0 "                  + recentFileInfo.fileName(), this);
                else                                                          rAction = new QAction(      recentValue + " " + recentFileInfo.fileName(), this);
                rAction->setCheckable(0);
                rAction->setData(opensave_recent_list_of_files.at(i));
                menu[RECENT_MENU]->addAction(rAction);
                connect(rAction, SIGNAL(triggered()), this, SLOT(openrecentfile()));
            }
        }
    }
    /*Ensure the list only has max amount of entries*/
    while(opensave_recent_list_of_files.size() > settings.opensave_recent_max_files) {
        opensave_recent_list_of_files.removeLast();
    }
}

void MainWindow::windowMenuAboutToShow()
{
    debug_message("MainWindow::windowMenuAboutToShow()");
    menu[WINDOW_MENU]->clear();
    menu[WINDOW_MENU]->addAction(actionHash.value(ACTION_windowclose));
    menu[WINDOW_MENU]->addAction(actionHash.value(ACTION_windowcloseall));
    menu[WINDOW_MENU]->addSeparator();
    menu[WINDOW_MENU]->addAction(actionHash.value(ACTION_windowcascade));
    menu[WINDOW_MENU]->addAction(actionHash.value(ACTION_windowtile));
    menu[WINDOW_MENU]->addSeparator();
    menu[WINDOW_MENU]->addAction(actionHash.value(ACTION_windownext));
    menu[WINDOW_MENU]->addAction(actionHash.value(ACTION_windowprevious));

    menu[WINDOW_MENU]->addSeparator();
    QList<QMdiSubWindow*> windows = mdiArea->subWindowList();
    for(int i = 0; i < windows.count(); ++i)
    {
        QAction* aAction = new QAction(windows.at(i)->windowTitle(), this);
        aAction->setCheckable(1);
        aAction->setData(i);
        menu[WINDOW_MENU]->addAction(aAction);
        connect(aAction, SIGNAL(toggled(int)), this, SLOT(windowMenuActivated(int)));
        aAction->setChecked(mdiArea->activeSubWindow() == windows.at(i));
    }
}

void MainWindow::windowMenuActivated(int checked)
{
    debug_message("MainWindow::windowMenuActivated()");
    QAction* aSender = qobject_cast<QAction*>(sender());
    if(!aSender)
        return;
    QWidget* w = mdiArea->subWindowList().at(aSender->data().toInt());
    if(w && checked)
        w->setFocus();
}

void MainWindow::newFile()
{
    debug_message("MainWindow::newFile()");
    docIndex++;
    numOfDocs++;
    MdiWindow* mdiWin = new MdiWindow(docIndex, mainWin, mdiArea, Qt::SubWindow);
    connect(mdiWin, SIGNAL(sendCloseMdiWin(MdiWindow*)), this, SLOT(onCloseMdiWin(MdiWindow*)));
    connect(mdiArea, SIGNAL(subWindowActivated(QMdiSubWindow*)), this, SLOT(onWindowActivated(QMdiSubWindow*)));

    updateMenuToolbarStatusbar();
    windowMenuAboutToShow();

    View* v = mdiWin->getView();
    if(v)
    {
        v->recalculateLimits();
        v->zoomExtents();
    }
}

void MainWindow::openFile(int recent, const QString& recentFile)
{
    debug_message("MainWindow::openFile()");

    QApplication::setOverrideCursor(Qt::ArrowCursor);

    QStringList files;
    int preview = settings.opensave_open_thumbnail;
    openFilesPath = settings.opensave_recent_directory;

    /*Check to see if this from the recent files list*/
    if(recent)
    {
        files.append(recentFile);
        openFilesSelected(files);
    }
    else if(!preview)
    {
        /*TODO: set getOpenFileNames' selectedFilter parameter from settings.opensave_open_format*/
        files = QFileDialog::getOpenFileNames(this, tr("Open"), openFilesPath, formatFilterOpen);
        openFilesSelected(files);
    }
    else if(preview)
    {
        PreviewDialog* openDialog = new PreviewDialog(this, tr("Open w/Preview"), openFilesPath, formatFilterOpen);
        /*TODO: set openDialog->selectNameFilter(const QString& filter) from settings.opensave_open_format*/
        connect(openDialog, SIGNAL(filesSelected(const QStringList&)), this, SLOT(openFilesSelected(const QStringList&)));
        openDialog->exec();
    }

    QApplication::restoreOverrideCursor();
}

void MainWindow::openFilesSelected(const QStringList& filesToOpen)
{
    int doOnce = 1;

    if(filesToOpen.count())
    {
        for(int i = 0; i < filesToOpen.count(); i++)
        {
            if(!validFileFormat(filesToOpen[i]))
                continue;

            QMdiSubWindow* existing = findMdiWindow(filesToOpen[i]);
            if(existing)
            {
                mdiArea->setActiveSubWindow(existing);
                continue;
            }

            /*The docIndex doesn't need increased as it is only used for unnamed files*/
            numOfDocs++;
            MdiWindow* mdiWin = new MdiWindow(docIndex, mainWin, mdiArea, Qt::SubWindow);
            connect(mdiWin, SIGNAL(sendCloseMdiWin(MdiWindow*)), this, SLOT(onCloseMdiWin(MdiWindow*)));
            connect(mdiArea, SIGNAL(subWindowActivated(QMdiSubWindow*)), this, SLOT(onWindowActivated(QMdiSubWindow*)));

            /* Make sure the toolbars/etc... are shown before doing their zoomExtents */
            if (doOnce) {
                updateMenuToolbarStatusbar();
                doOnce = 0;
            }

            if (mdiWin->loadFile(filesToOpen.at(i))) {
                statusbar->showMessage(tr("File(s) loaded"), 2000);
                mdiWin->show();
                mdiWin->showMaximized();
                /*Prevent duplicate entries in the recent files list*/
                if(!opensave_recent_list_of_files.contains(filesToOpen.at(i), Qt::CaseInsensitive)) {
                    opensave_recent_list_of_files.prepend(filesToOpen.at(i));
                }
                /*Move the recent file to the top of the list*/
                else {
                    opensave_recent_list_of_files.removeAll(filesToOpen.at(i));
                    opensave_recent_list_of_files.prepend(filesToOpen.at(i));
                }
                strcpy(settings.opensave_recent_directory, QFileInfo(filesToOpen.at(i)).absolutePath().toLocal8Bit().constData());

                View* v = mdiWin->getView();
                if (v) {
                    v->recalculateLimits();
                    v->zoomExtents();
                }
            }
            else {
                mdiWin->close();
            }
        }
    }

    windowMenuAboutToShow();
}

void MainWindow::openrecentfile()
{
    debug_message("MainWindow::openrecentfile()");

    /*Check to see if this from the recent files list*/
    QAction* recentSender = qobject_cast<QAction*>(sender());
    if (recentSender) {
        openFile(1, recentSender->data().toString());
    }
}

void MainWindow::savefile()
{
    debug_message("MainWindow::savefile()");
}

void MainWindow::saveasfile()
{
    debug_message("MainWindow::saveasfile()");
    /* need to find the activeSubWindow before it loses focus to the FileDialog*/
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow());
    if(!mdiWin)
        return;

    QString file;
    openFilesPath = settings.opensave_recent_directory;
    file = QFileDialog::getSaveFileName(this, tr("Save As"), openFilesPath, formatFilterSave);

    mdiWin->saveFile(file);
}

QMdiSubWindow* MainWindow::findMdiWindow(const QString& fileName)
{
    debug_message("MainWindow::findMdiWindow(%s)", qPrintable(fileName));
    QString canonicalFilePath = QFileInfo(fileName).canonicalFilePath();

    foreach(QMdiSubWindow* subWindow, mdiArea->subWindowList())
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(subWindow);
        if(mdiWin)
        {
            if(mdiWin->getCurrentFile() == canonicalFilePath)
            {
                return subWindow;
            }
        }
    }
    return 0;
}

void MainWindow::closeEvent(QCloseEvent* event)
{
    mdiArea->closeAllSubWindows();
    writeSettings();
    event->accept();
}

void MainWindow::onCloseWindow()
{
    debug_message("MainWindow::onCloseWindow()");
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow());
    if(mdiWin)
    {
        onCloseMdiWin(mdiWin);
    }
}

void MainWindow::onCloseMdiWin(MdiWindow* theMdiWin)
{
    debug_message("MainWindow::onCloseMdiWin()");
    numOfDocs--;

    int keepMaximized;
    if(theMdiWin) { keepMaximized = theMdiWin->isMaximized(); }

    mdiArea->removeSubWindow(theMdiWin);
    theMdiWin->deleteLater();

    updateMenuToolbarStatusbar();
    windowMenuAboutToShow();

    if(keepMaximized)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow());
        if(mdiWin) { mdiWin->showMaximized(); }
    }
}

void MainWindow::onWindowActivated(QMdiSubWindow* w)
{
    debug_message("MainWindow::onWindowActivated()");
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(w);
    if(mdiWin) { mdiWin->onWindowActivated(); }
}

void MainWindow::resizeEvent(QResizeEvent* e)
{
    debug_message("MainWindow::resizeEvent()");
    QMainWindow::resizeEvent(e);
    statusBar()->setSizeGripEnabled(!isMaximized());
}

QAction* MainWindow::getFileSeparator()
{
    debug_message("MainWindow::getFileSeparator()");
    return myFileSeparator;
}

void MainWindow::updateMenuToolbarStatusbar()
{
    int i;
    debug_message("MainWindow::updateMenuToolbarStatusbar()");

    actionHash.value(ACTION_print)->setEnabled(numOfDocs > 0);
    actionHash.value(ACTION_windowclose)->setEnabled(numOfDocs > 0);
    actionHash.value(ACTION_designdetails)->setEnabled(numOfDocs > 0);

    if (numOfDocs) {
        int i;
        /*Toolbars*/
        for (i=0; i<N_TOOLBARS; i++) {
            toolbar[i]->show();
        }

        foreach(QToolBar* tb, toolbarHash)
        {
            tb->show();
        }

        /*DockWidgets*/
        /*
        dockPropEdit->show();
        dockUndoEdit->show();
        */

        /*Menus*/
        menuBar()->clear();
        menuBar()->addMenu(menu[FILE_MENU]);
        menuBar()->addMenu(menu[EDIT_MENU]);
        menuBar()->addMenu(menu[VIEW_MENU]);

        foreach(QMenu* menu_, menuHash)
        {
            menuBar()->addMenu(menu_);
        }

        menuBar()->addMenu(menu[SETTINGS_MENU]);
        menuBar()->addMenu(menu[WINDOW_MENU]);
        menuBar()->addMenu(menu[HELP_MENU]);

        menu[WINDOW_MENU]->setEnabled(1);

        /* Statusbar */
        statusbar->clearMessage();
        statusBarMouseCoord->show();
        status_bar[STATUS_SNAP]->show();
        status_bar[STATUS_GRID]->show();
        status_bar[STATUS_RULER]->show();
        status_bar[STATUS_ORTHO]->show();
        status_bar[STATUS_POLAR]->show();
        status_bar[STATUS_QSNAP]->show();
        status_bar[STATUS_QTRACK]->show();
        status_bar[STATUS_LWT]->show();
    }
    else
    {
        /* Toolbars */
        toolbar[TOOLBAR_VIEW]->hide();
        toolbar[TOOLBAR_ZOOM]->hide();
        toolbar[TOOLBAR_PAN]->hide();
        toolbar[TOOLBAR_ICON]->hide();
        toolbar[TOOLBAR_HELP]->hide();
        toolbar[TOOLBAR_LAYER]->hide();
        toolbar[TOOLBAR_TEXT]->hide();
        toolbar[TOOLBAR_PROPERTIES]->hide();
        foreach(QToolBar* tb, toolbarHash)
        {
            tb->hide();
        }

        /*DockWidgets*/
        /*
        dockPropEdit->hide();
        dockUndoEdit->hide();
        */
        
        /*Menus*/
        menuBar()->clear();
        menuBar()->addMenu(menu[FILE_MENU]);
        menuBar()->addMenu(menu[EDIT_MENU]);
        menuBar()->addMenu(menu[SETTINGS_MENU]);
        menuBar()->addMenu(menu[WINDOW_MENU]);
        menuBar()->addMenu(menu[HELP_MENU]);

        menu[WINDOW_MENU]->setEnabled(0);

        /*Statusbar*/
        statusbar->clearMessage();
        statusBarMouseCoord->hide();
        for (i=0; i<N_STATUS; i++) {
            status_bar[i]->hide();
        }
    }
}

int MainWindow::validFileFormat(const QString& fileName)
{
    if(fileName.length() == 0) {
        return 0;
    }
    const char *fname;
    fname = qPrintable(fileName);
    if (emb_identify_format(fname) >= 0) {
        return 1;
    }
    return 0;
}

void MainWindow::loadFormats()
{
    char stable, unstable;
    QString supportedReaders = "All Supported Files (";
    QString individualReaders = "All Files (*);;";
    QString supportedWriters = "All Supported Files (";
    QString individualWriters = "All Files (*);;";
    QString supportedStr;
    QString individualStr;

    /*TODO: Stable Only (Settings Option)*/
    /*stable = 'S'; unstable = 'S';*/

    /*Stable + Unstable*/
    stable = 'S'; unstable = 'U';

    const char* extension = 0;
    const char* description = 0;
    char readerState;
    char writerState;

    EmbFormatList* curFormat = 0;
    for(int i=0; i < numberOfFormats; i++)
    {
        extension = formatTable[i].extension;
        description = formatTable[i].description;
        readerState = formatTable[i].reader_state;
        writerState = formatTable[i].writer_state;

        QString upperExt = QString(extension).toUpper();
        supportedStr = "*" + upperExt + " ";
        individualStr = upperExt.replace(".", "") + " - " + description + " (*" + extension + ");;";
        if(readerState == stable || readerState == unstable)
        {
            /*Exclude color file formats from open dialogs*/
            if(upperExt != "COL" && upperExt != "EDR" && upperExt != "INF" && upperExt != "RGB")
            {
                supportedReaders.append(supportedStr);
                individualReaders.append(individualStr);
            }
        }
        if(writerState == stable || writerState == unstable)
        {
            supportedWriters.append(supportedStr);
            individualWriters.append(individualStr);
        }

    }

    supportedReaders.append(");;");
    supportedWriters.append(");;");

    formatFilterOpen = supportedReaders + individualReaders;
    formatFilterSave = supportedWriters + individualWriters;

    /*TODO: Fixup custom filter*/
    /*
    QString custom = settings.custom_filter;
    if(custom.contains("supported", Qt::CaseInsensitive))
        custom = ""; //This will hide it
    else if(!custom.contains("*", Qt::CaseInsensitive))
        custom = ""; //This will hide it
    else
        custom = "Custom Filter(" + custom + ");;";

    return tr(qPrintable(custom + supported + all));
    */
}

void MainWindow::closeToolBar(QAction* action)
{
    if (action->objectName() == "toolbarclose") {
        QToolBar* tb = qobject_cast<QToolBar*>(sender());
        if(tb)
        {
            debug_message("%s closed.", qPrintable(tb->objectName()));
            tb->hide();
        }
    }
}

void MainWindow::floatingChangedToolBar(int isFloating)
{
    QToolBar* tb = qobject_cast<QToolBar*>(sender());
    if(tb)
    {
        if(isFloating)
        {
            /*
            //TODO: Determine best suited close button on various platforms.
            QStyle::SP_DockWidgetCloseButton
            QStyle::SP_TitleBarCloseButton
            QStyle::SP_DialogCloseButton
            */
            QAction *ACTION = new QAction(tb->style()->standardIcon(QStyle::SP_DialogCloseButton), "Close", this);
            ACTION->setStatusTip("Close the " + tb->windowTitle() + " Toolbar");
            ACTION->setObjectName("toolbarclose");
            tb->addAction(ACTION);
            connect(tb, SIGNAL(actionTriggered(QAction*)), this, SLOT(closeToolBar(QAction*)));
        }
        else
        {
            QList<QAction*> actList = tb->actions();
            for(int i = 0; i < actList.size(); ++i)
            {
                QAction* ACTION = actList.value(i);
                if(ACTION->objectName() == "toolbarclose")
                {
                    tb->removeAction(ACTION);
                    disconnect(tb, SIGNAL(actionTriggered(QAction*)), this, SLOT(closeToolBar(QAction*)));
                    delete ACTION;
                }
            }
        }
    }
}

EmbDetailsDialog::EmbDetailsDialog(QGraphicsScene* theScene, QWidget* parent) : QDialog(parent)
{
    setMinimumSize(750,550);

    getInfo();
    mainWidget = createMainWidget();

    buttonBox = new QDialogButtonBox(QDialogButtonBox::Ok);
    connect(buttonBox, SIGNAL(accepted()), this, SLOT(accept()));

    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(this);
    vboxLayoutMain->addWidget(mainWidget);
    vboxLayoutMain->addWidget(buttonBox);
    setLayout(vboxLayoutMain);

    setWindowTitle(tr("Embroidery Design Details"));

    QApplication::setOverrideCursor(Qt::ArrowCursor);
}

EmbDetailsDialog::~EmbDetailsDialog()
{
    QApplication::restoreOverrideCursor();
}

void EmbDetailsDialog::getInfo()
{
    /*TODO: generate a temporary pattern from the scene data.*/

    /*TODO: grab this information from the pattern*/
    stitchesTotal = 5; /*TODO: embStitchList_count(pattern->stitchList, TOTAL);*/
    stitchesReal = 4; /*TODO: embStitchList_count(pattern->stitchList, NORMAL);*/
    stitchesJump = 3; /*TODO: embStitchList_count(pattern->stitchList, JUMP);*/
    stitchesTrim = 2; /*TODO: embStitchList_count(pattern->stitchList, TRIM);*/
    colorTotal = 1; /*TODO: embThreadList_count(pattern->threadList, TOTAL);*/
    colorChanges = 0; /*TODO: embThreadList_count(pattern->threadList, CHANGES);*/

    boundingRect.setRect(0, 0, 50, 100); /*TODO: embPattern_calcBoundingBox(pattern);*/
}

extern char *details_label_text[];

QWidget* EmbDetailsDialog::createMainWidget()
{
    QWidget* widget = new QWidget(this);

    /*Misc*/
    QGroupBox* groupBoxMisc = new QGroupBox(tr("General Information"), widget);

    QLabel* labels[12];
    QLabel* fields[12];

    int i;
    for (i=0; i<12; i++) {
        labels[i] = new QLabel(tr(details_label_text[i]), this);
    }

    fields[0] = new QLabel(QString::number(stitchesTotal), this);
    fields[1] = new QLabel(QString::number(stitchesReal), this);
    fields[2] = new QLabel(QString::number(stitchesJump), this);
    fields[3] = new QLabel(QString::number(stitchesTrim), this);
    fields[4] = new QLabel(QString::number(colorTotal), this);
    fields[5] = new QLabel(QString::number(colorChanges), this);
    fields[6] = new QLabel(QString::number(boundingRect.left()) + " mm", this);
    fields[7] = new QLabel(QString::number(boundingRect.top()) + " mm", this);
    fields[8] = new QLabel(QString::number(boundingRect.right()) + " mm", this);
    fields[9] = new QLabel(QString::number(boundingRect.bottom()) + " mm", this);
    fields[10] = new QLabel(QString::number(boundingRect.width()) + " mm", this);
    fields[11] = new QLabel(QString::number(boundingRect.height()) + " mm", this);

    QGridLayout* gridLayoutMisc = new QGridLayout(groupBoxMisc);
    for (i=0; i<12; i++) {
        gridLayoutMisc->addWidget(labels[i], i, 0, Qt::AlignLeft);
        gridLayoutMisc->addWidget(fields[i], i, 1, Qt::AlignLeft);
    }
    gridLayoutMisc->setColumnStretch(1,1);
    groupBoxMisc->setLayout(gridLayoutMisc);

    /* TODO: Color Histogram */

    /*Stitch Distribution*/
    /*QGroupBox* groupBoxDist = new QGroupBox(tr("Stitch Distribution"), widget);*/

    /* TODO: Stitch Distribution Histogram */

    /*Widget Layout*/
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget);
    vboxLayoutMain->addWidget(groupBoxMisc);
    /*vboxLayoutMain->addWidget(groupBoxDist);*/
    vboxLayoutMain->addStretch(1);
    widget->setLayout(vboxLayoutMain);

    QScrollArea* scrollArea = new QScrollArea(this);
    scrollArea->setWidgetResizable(1);
    scrollArea->setWidget(widget);
    return scrollArea;
}

bool Application::event(QEvent *event)
{
    switch (event->type()) {
    case QEvent::FileOpen:
        if (_mainWin) {
            _mainWin->openFilesSelected(QStringList(static_cast<QFileOpenEvent *>(event)->file()));
            return 1;
        }
        /* Fall through*/
    default:
        return QApplication::event(event);
    }
}

ImageWidget::ImageWidget(const QString &filename, QWidget* parent) : QWidget(parent)
{
    debug_message("ImageWidget Constructor");

    img.load(filename);

    setMinimumWidth(img.width());
    setMinimumHeight(img.height());
    setMaximumWidth(img.width());
    setMaximumHeight(img.height());

    this->show();
}

int ImageWidget::load(const QString &fileName)
{
    img.load(fileName);
    return 1;
}

int ImageWidget::save(const QString &fileName)
{
    img.save(fileName, "PNG");
    return 1;
}

ImageWidget::~ImageWidget()
{
    debug_message("ImageWidget Destructor");
}

void ImageWidget::paintEvent(QPaintEvent*)
{
    QPainter painter(this);
    painter.setViewport(0, 0, width(), height());
    painter.setWindow(0, 0, width(), height());
    painter.drawImage(0, 0, img);
}


LayerManager::LayerManager(MainWindow* mw, QWidget* parent) : QDialog(parent)
{
    layerModel = new QStandardItemModel(0, 8, this);

    layerModelSorted = new QSortFilterProxyModel;
    layerModelSorted->setDynamicSortFilter(1);
    layerModelSorted->setSourceModel(layerModel);

    treeView = new QTreeView;
    treeView->setRootIsDecorated(0);
    treeView->setAlternatingRowColors(1);
    treeView->setModel(layerModelSorted);
    treeView->setSortingEnabled(1);
    treeView->sortByColumn(0, Qt::AscendingOrder);

    QVBoxLayout *mainLayout = new QVBoxLayout;
    mainLayout->addWidget(treeView);
    setLayout(mainLayout);

    setWindowTitle(tr("Layer Manager"));
    setMinimumSize(750, 550);

    layerModel->setHeaderData(0, Qt::Horizontal, tr("Name"));
    layerModel->setHeaderData(1, Qt::Horizontal, tr("Visible"));
    layerModel->setHeaderData(2, Qt::Horizontal, tr("Frozen"));
    layerModel->setHeaderData(3, Qt::Horizontal, tr("Z Value"));
    layerModel->setHeaderData(4, Qt::Horizontal, tr("Color"));
    layerModel->setHeaderData(5, Qt::Horizontal, tr("Linetype"));
    layerModel->setHeaderData(6, Qt::Horizontal, tr("Lineweight"));
    layerModel->setHeaderData(7, Qt::Horizontal, tr("Print"));

    addLayer("0", 1, 0, 0.0, qRgb(0,0,0), "Continuous", "Default", 1);
    addLayer("1", 1, 0, 1.0, qRgb(0,0,0), "Continuous", "Default", 1);
    addLayer("2", 1, 0, 2.0, qRgb(0,0,0), "Continuous", "Default", 1);
    addLayer("3", 1, 0, 3.0, qRgb(0,0,0), "Continuous", "Default", 1);
    addLayer("4", 1, 0, 4.0, qRgb(0,0,0), "Continuous", "Default", 1);
    addLayer("5", 1, 0, 5.0, qRgb(0,0,0), "Continuous", "Default", 1);
    addLayer("6", 1, 0, 6.0, qRgb(0,0,0), "Continuous", "Default", 1);
    addLayer("7", 1, 0, 7.0, qRgb(0,0,0), "Continuous", "Default", 1);
    addLayer("8", 1, 0, 8.0, qRgb(0,0,0), "Continuous", "Default", 1);
    addLayer("9", 1, 0, 9.0, qRgb(0,0,0), "Continuous", "Default", 1);

    for(int i = 0; i < layerModel->columnCount(); ++i)
        treeView->resizeColumnToContents(i);

    QApplication::setOverrideCursor(Qt::ArrowCursor);
}

LayerManager::~LayerManager()
{
    QApplication::restoreOverrideCursor();
}

void LayerManager::addLayer(const QString& name,
                            const int visible,
                            const int frozen,
                            const float zValue,
                            const unsigned int color,
                            const QString& lineType,
                            const QString& lineWeight,
                            const int print)
{
    layerModel->insertRow(0);
    layerModel->setData(layerModel->index(0, 0), name);
    layerModel->setData(layerModel->index(0, 1), visible);
    layerModel->setData(layerModel->index(0, 2), frozen);
    layerModel->setData(layerModel->index(0, 3), zValue);

    QPixmap colorPix(QSize(16,16));
    colorPix.fill(QColor(color));
    layerModel->itemFromIndex(layerModel->index(0, 4))->setIcon(QIcon(colorPix));
    layerModel->setData(layerModel->index(0, 4), QColor(color));

    layerModel->setData(layerModel->index(0, 5), lineType);
    layerModel->setData(layerModel->index(0, 6), lineWeight);
    layerModel->setData(layerModel->index(0, 7), print);
}

int main(int argc, char* argv[])
{
    if (argc > 1) {
        main_tex_example(argc, argv);
        return 0;
    }

#if defined(Q_OS_MAC)
    Application app(argc, argv);
#else
    QApplication app(argc, argv);
#endif
    app.setApplicationName(_appName_);
    app.setApplicationVersion(_appVer_);

    QStringList filesToOpen;

    for (int i = 1; i < argc; i++) {
        if (!strcmp(argv[i], "-d") || !strcmp(argv[i], "--debug")) {  }
        else if(!strcmp(argv[i], "-h") || !strcmp(argv[i], "--help")   ) { usage(); }
        else if(!strcmp(argv[i], "-v") || !strcmp(argv[i], "--version")) { version(); }
        else if(QFile::exists(argv[i]) && MainWindow::validFileFormat(argv[i])) {
            filesToOpen << argv[i];
        }
        else
        {
            usage();
        }
    }

    if(exitApp)
        return 1;

    _mainWin = new MainWindow();
#if defined(Q_OS_MAC)
    app.setMainWin(_mainWin);
#endif

    QObject::connect(&app, SIGNAL(lastWindowClosed()), _mainWin, SLOT(quit()));

    _mainWin->setWindowTitle(app.applicationName() + " " + app.applicationVersion());
    _mainWin->show();

    /*NOTE: If openFilesSelected() is called from within the mainWin constructor, slot commands wont work and the window menu will be screwed*/
    if(!filesToOpen.isEmpty())
        _mainWin->openFilesSelected(filesToOpen);

    return app.exec();
}

MdiArea::MdiArea(MainWindow* mw, QWidget *parent) : QMdiArea(parent), mainWin(mw)
{
    setTabsClosable(1);

    useLogo = 0;
    useTexture = 0;
    useColor = 0;
}

MdiArea::~MdiArea()
{
}

void MdiArea::useBackgroundLogo(int use)
{
    useLogo = use;
    forceRepaint();
}

void MdiArea::useBackgroundTexture(int use)
{
    useTexture = use;
    forceRepaint();
}

void MdiArea::useBackgroundColor(int use)
{
    useColor = use;
    forceRepaint();
}

void MdiArea::setBackgroundLogo(const QString& fileName)
{
    bgLogo.load(fileName);

    forceRepaint();
}

void MdiArea::setBackgroundTexture(const QString& fileName)
{
    bgTexture.load(fileName);

    forceRepaint();
}

void MdiArea::setBackgroundColor(const QColor& color)
{
    if(!color.isValid())
        bgColor = background().color();
    else
        bgColor = color;

    forceRepaint();
}

void MdiArea::mouseDoubleClickEvent(QMouseEvent* /*e*/)
{
    mainWin->openFile();
}

void MdiArea::paintEvent(QPaintEvent* /*e*/)
{
    QWidget* vport = viewport();
    QRect rect = vport->rect();

    QPainter painter(vport);
    painter.setRenderHint(QPainter::SmoothPixmapTransform);

    /*Always fill with a solid color first*/
    if(useColor) painter.fillRect(rect, bgColor);
    else         painter.fillRect(rect, background());

    /*Then overlay the texture*/
    if(useTexture)
    {
        QBrush bgBrush(bgTexture);
        painter.fillRect(rect, bgBrush);
    }

    /*Overlay the logo last*/
    if(useLogo)
    {
        /*Center the pixmap*/
        int dx = (rect.width()-bgLogo.width())/2;
        int dy = (rect.height()-bgLogo.height())/2;
        painter.drawPixmap(dx, dy, bgLogo.width(), bgLogo.height(), bgLogo);
    }
}

void MdiArea::cascade()
{
    cascadeSubWindows();
    zoomExtentsAllSubWindows();
}

void MdiArea::tile()
{
    tileSubWindows();
    zoomExtentsAllSubWindows();
}

void MdiArea::zoomExtentsAllSubWindows()
{
    foreach(QMdiSubWindow* window, subWindowList())
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(window);
        if(mdiWin)
        {
            View* v = mdiWin->getView();
            if(v)
            {
                v->recalculateLimits();
                v->zoomExtents();
            }
        }
    }
}

void MdiArea::forceRepaint()
{
    /* HACK: Take that QMdiArea! */
    QSize hack = size();
    resize(hack + QSize(1,1));
    resize(hack);
}

MdiWindow::MdiWindow(const int theIndex, MainWindow* mw, QMdiArea* parent, Qt::WindowFlags wflags) : QMdiSubWindow(parent, wflags)
{
    mainWin = mw;
    mdiArea = parent;

    myIndex = theIndex;

    fileWasLoaded = 0;

    setAttribute(Qt::WA_DeleteOnClose);

    QString aName;
    curFile = aName.asprintf("Untitled%d.dst", myIndex);
    this->setWindowTitle(curFile);

    this->setWindowIcon(QIcon("icons/app.png"));

    gscene = new QGraphicsScene(0,0,0,0, this);
    gview = new View(mainWin, gscene, this);

    setWidget(gview);

    /*
     * WARNING:
     * DO NOT SET THE QMDISUBWINDOW (this) FOCUSPROXY TO THE PROMPT
     * AS IT WILL CAUSE THE WINDOW MENU TO NOT SWITCH WINDOWS PROPERLY!
     * ALTHOUGH IT SEEMS THAT SETTING INTERNAL WIDGETS FOCUSPROXY IS OK.
     */
/*    gview->setFocusProxy(mainWin->prompt);*/

    resize(sizeHint());

    curLayer = "0";
    curColor = 0; /*TODO: color ByLayer*/
    curLineType = "ByLayer";
    curLineWeight = "ByLayer";

    /* Due to strange Qt4.2.3 feature the child window icon is not drawn*/
    /* in the main menu if showMaximized() is called for a non-visible child window*/
    /* Therefore calling show() first...*/
    show();
    showMaximized();

    setFocusPolicy(Qt::WheelFocus);
    setFocus();

    onWindowActivated();
}

MdiWindow::~MdiWindow()
{
    debug_message("MdiWindow Destructor()");
}

int MdiWindow::saveFile(const QString &fileName)
{
    debug_message("SaveObject save(%s)", qPrintable(fileName));

    /* TODO: Before saving to a stitch only format, Embroidermodder needs
     *       to calculate the optimal path to minimize jump stitches. Also
     *       based upon which layer needs to be stitched first,
     *       the path to the next object needs to be hidden beneath fills
     *       that will come later. When finding the optimal path, we need
     *       to take into account the color of the thread, as we do not want
     *       to try to hide dark colored stitches beneath light colored fills.
     */
    int formatType = EMBFORMAT_UNSUPPORTED;
    int writeSuccessful = 0;
    int i;

    formatType = emb_identify_format((char*)qPrintable(fileName));
    if (formatType == EMBFORMAT_UNSUPPORTED) {
        return 0;
    }

    EmbPattern* pattern = 0;

    pattern = embPattern_create();
    if(!pattern) { debug_message("Could not allocate memory for embroidery pattern"); }

    /* Write */
    int writer = emb_identify_format((char*)qPrintable(fileName));
    if (writer<0) {
        debug_message("Unsupported write file type: %s", qPrintable(fileName));
    }
    else {
        foreach(QGraphicsItem* item, _mainWin->activeScene()->items(Qt::AscendingOrder))
        {
            int objType = item->data(OBJ_TYPE).toInt();

            if (objType == OBJ_TYPE_ARC) {
                /* addArc */
            }
            else if (objType == OBJ_TYPE_BLOCK) {
                /* addBlock(pattern, item); */
            }
            else if(objType == OBJ_TYPE_CIRCLE) {
                CircleObject* obj = static_cast<CircleObject*>(item);
                if (obj) {
                    if (formatType == EMBFORMAT_STITCHONLY) {
                        QPainterPath path = obj->objectSavePath();
            toPolyline(pattern, obj->objectCenter(), path.simplified(), "0", obj->objectColor(), "CONTINUOUS", "BYLAYER"); /*TODO: proper layer/lineType/lineWeight //TODO: Improve precision, replace simplified*/
        }
        else {
            QPointF p = obj->objectCenter();
            float r = obj->objectRadius();
            embPattern_addCircleObjectAbs(pattern, (double)p.x(), (double)p.y(), (double)r);
        }
    }
            }
            else if(objType == OBJ_TYPE_DIMALIGNED) {
                /* addDimAligned(pattern, item); */
            }
            else if(objType == OBJ_TYPE_DIMANGULAR) {
                /* addDimAngular(pattern, item); */
            }
            else if(objType == OBJ_TYPE_DIMARCLENGTH) {
                /* addDimArcLength(pattern, item); */
            }
            else if(objType == OBJ_TYPE_DIMDIAMETER) {
                /* addDimDiameter(pattern, item); */
            }
            else if(objType == OBJ_TYPE_DIMLEADER) {
                /* addDimLeader(pattern, item); */
            }
            else if(objType == OBJ_TYPE_DIMLINEAR) {
                /* addDimLinear(pattern, item); */
            }
            else if(objType == OBJ_TYPE_DIMORDINATE)  {
                /* addDimOrdinate(pattern, item); */
            }
            else if(objType == OBJ_TYPE_DIMRADIUS)    {
                /* addDimRadius(pattern, item); */
            }
            else if(objType == OBJ_TYPE_ELLIPSE) {
    EllipseObject* obj = static_cast<EllipseObject*>(item);
    if(obj)
    {
        if(formatType == EMBFORMAT_STITCHONLY)
        {
            QPainterPath path = obj->objectSavePath();
            toPolyline(pattern, obj->objectCenter(), path.simplified(), "0", obj->objectColor(), "CONTINUOUS", "BYLAYER"); /*TODO: proper layer/lineType/lineWeight //TODO: Improve precision, replace simplified*/
        }
        else
        {
            /*TODO: ellipse rotation*/
            embPattern_addEllipseObjectAbs(pattern, (double)obj->objectCenter().x(), (double)obj->objectCenter().y(), (double)obj->objectWidth()/2.0, (double)obj->objectHeight()/2.0);
        }
    }
            }
            else if(objType == OBJ_TYPE_ELLIPSEARC)   { /* addEllipseArc(pattern, item);  */ }
            else if(objType == OBJ_TYPE_GRID)         { /* addGrid(pattern, item);     */    }
            else if(objType == OBJ_TYPE_HATCH)        { /* addHatch(pattern, item);       */ }
            else if(objType == OBJ_TYPE_IMAGE)        { /* addImage(pattern, item);       */ }
            else if(objType == OBJ_TYPE_INFINITELINE) { /* addInfiniteLine(pattern, item); */ }
            else if(objType == OBJ_TYPE_LINE)         { 
    LineObject* obj = static_cast<LineObject*>(item);
    if(obj)
    {
        if(formatType == EMBFORMAT_STITCHONLY)
        {
            toPolyline(pattern, obj->objectEndPoint1(), obj->objectSavePath(), "0", obj->objectColor(), "CONTINUOUS", "BYLAYER"); /*TODO: proper layer/lineType/lineWeight*/
        }
        else
        {
            embPattern_addLineObjectAbs(pattern, (double)obj->objectX1(), (double)obj->objectY1(), (double)obj->objectX2(), (double)obj->objectY2());
        }
    }
      }
            else if (objType == OBJ_TYPE_PATH) {
    /*TODO: Reimplement addPolyline() using the libembroidery C API*/
    /*
    debug_message("addPolyline()");
    QGraphicsPathItem* polylineItem = (QGraphicsPathItem*)item;
    if(polylineItem)
    {
        QPainterPath path = polylineItem->path();
        QPointF pos = polylineItem->pos();
        float startX = pos.x();
        float startY = pos.y();

        QPainterPath::Element element;
        QPainterPath::Element P1;
        QPainterPath::Element P2;
        QPainterPath::Element P3;
        QPainterPath::Element P4;

        for(int i = 0; i < path.elementCount()-1; ++i)
        {
            element = path.elementAt(i);
            if(element.isMoveTo())
            {
                pattern.AddStitchAbs((element.x + startX), -(element.y + startY), TRIM);
            }
            else if(element.isLineTo())
            {
                pattern.AddStitchAbs((element.x + startX), -(element.y + startY), NORMAL);
            }
            else if(element.isCurveTo())
            {
                P1 = path.elementAt(i-1); // start point
                P2 = path.elementAt(i);   // control point
                P3 = path.elementAt(i+1); // control point
                P4 = path.elementAt(i+2); // end point

                pattern.AddStitchAbs(P4.x, -P4.y, NORMAL); //TODO: This is temporary
                //TODO: Curved Polyline segments are always arcs
            }
        }
        pattern.AddStitchRel(0, 0, STOP);
        QColor c= polylineItem->pen().color();
        pattern.AddColor(c.red(), c.green(), c.blue(), "", "");
    }
    */
            }
            else if(objType == OBJ_TYPE_POINT)        { 
    PointObject* obj = static_cast<PointObject*>(item);
    if(obj)
    {
        if(formatType == EMBFORMAT_STITCHONLY)
        {
            toPolyline(pattern, obj->objectPos(), obj->objectSavePath(), "0", obj->objectColor(), "CONTINUOUS", "BYLAYER"); /*TODO: proper layer/lineType/lineWeight*/
        }
        else
        {
            embPattern_addPointObjectAbs(pattern, (double)obj->objectX(), (double)obj->objectY());
        }
    }
             }
            else if(objType == OBJ_TYPE_POLYGON) {
    PolygonObject* obj = static_cast<PolygonObject*>(item);
    if(obj)
    {
        toPolyline(pattern, obj->objectPos(), obj->objectSavePath(), "0", obj->objectColor(), "CONTINUOUS", "BYLAYER"); /*TODO: proper layer/lineType/lineWeight*/
    }
            }
            else if(objType == OBJ_TYPE_POLYLINE) { 
                PolylineObject* obj = static_cast<PolylineObject*>(item);
                if (obj)  {
                    toPolyline(pattern, obj->objectPos(), obj->objectSavePath(), "0", obj->objectColor(), "CONTINUOUS", "BYLAYER"); /*TODO: proper layer/lineType/lineWeight*/
                }
            }
            else if(objType == OBJ_TYPE_RAY) {
                /* addRay(pattern, item);       */
            }
            else if(objType == OBJ_TYPE_RECTANGLE) { 
    RectObject* obj = static_cast<RectObject*>(item);
    if(obj)
    {
        if(formatType == EMBFORMAT_STITCHONLY)
        {
            toPolyline(pattern, obj->objectPos(), obj->objectSavePath(), "0", obj->objectColor(), "CONTINUOUS", "BYLAYER"); /*TODO: proper layer/lineType/lineWeight*/
        }
        else
        {
            /*TODO: Review this at some point*/
            QPointF topLeft = obj->objectTopLeft();
            embPattern_addRectObjectAbs(pattern, (double)topLeft.x(), (double)topLeft.y(), (double)obj->objectWidth(), (double)obj->objectHeight());
        }
    }
            }
            else if(objType == OBJ_TYPE_SLOT) {
            }
            else if(objType == OBJ_TYPE_SPLINE)       { 
    /*TODO: abstract bezier into geom-bezier... cubicBezierMagic(P1, P2, P3, P4, 0.0, 1.0, tPoints);*/
    }
            else if(objType == OBJ_TYPE_TEXTMULTI)    { 
    /*TODO: saving polygons, polylines and paths must be stable before we go here.*/
       }
            else if (objType == OBJ_TYPE_TEXTSINGLE) {
    /*TODO: saving polygons, polylines and paths must be stable before we go here.*/

    /*TODO: This needs to work like a path, not a polyline. Improve this*/
    TextSingleObject* obj = static_cast<TextSingleObject*>(item);
    if(obj)
    {
        if(formatType == EMBFORMAT_STITCHONLY)
        {
            QList<QPainterPath> pathList = obj->objectSavePathList();
            foreach(QPainterPath path, pathList)
            {
                toPolyline(pattern, obj->objectPos(), path.simplified(), "0", obj->objectColor(), "CONTINUOUS", "BYLAYER"); /*TODO: proper layer/lineType/lineWeight //TODO: Improve precision, replace simplified*/
            }
        }
        else
        {

        }
    }  }
        }

        /*TODO: handle EMBFORMAT_STCHANDOBJ also*/
        if(formatType == EMBFORMAT_STITCHONLY)
            embPattern_movePolylinesToStitchList(pattern); /*TODO: handle all objects like this*/

        writeSuccessful = embPattern_writeAuto(pattern, qPrintable(fileName));
        if(!writeSuccessful) { debug_message("Writing file %s was unsuccessful", qPrintable(fileName)); }
    }

    /*TODO: check the embLog for errors and if any exist, report them.*/
    embPattern_free(pattern);

    return writeSuccessful;
}

int MdiWindow::loadFile(const QString &fileName)
{
    debug_message("MdiWindow loadFile()");

    unsigned int tmpColor = getCurrentColor();

    QFile file(fileName);
    if(!file.open(QFile::ReadOnly | QFile::Text))
    {
        QMessageBox::warning(this, tr("Error reading file"),
                             tr("Cannot read file %1:\n%2.")
                             .arg(fileName)
                             .arg(file.errorString()));
        return 0;
    }

    QApplication::setOverrideCursor(Qt::WaitCursor);

    QString ext = fileExtension(fileName);
    debug_message("ext: %s", qPrintable(ext));

    /* Read*/
    EmbPattern* p = embPattern_create();
    if (!p) {
        printf("Could not allocate memory for embroidery pattern\n");
        exit(1);
    }
    if (!embPattern_readAuto(p, qPrintable(fileName))) {
        debug_message("Reading file was unsuccessful: %s\n", qPrintable(fileName));
        QApplication::restoreOverrideCursor();
        QMessageBox::warning(this, tr("Error reading pattern"), tr("Reading file was unsuccessful: ") + fileName);
    }
    else {
        embPattern_moveStitchListToPolylines(p); /*TODO: Test more*/
        int stitchCount = p->stitchList->count;
        QPainterPath path;

        if (p->circles) {
            for (int i = 0; i < p->circles->count; i++) {
                EmbCircle c = p->circles->circle[i].circle;
                EmbColor thisColor = p->circles->circle[i].color;
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b));
                /* NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed.*/
                mainWin->nativeAddCircle(c.center.x, c.center.y, c.radius, 0, OBJ_RUBBER_OFF); /*TODO: fill*/
            }
        }
        if (p->ellipses) {
            for (int i = 0; i < p->ellipses->count; i++) {
                EmbEllipse e = p->ellipses->ellipse[i].ellipse;
                EmbColor thisColor = p->ellipses->ellipse[i].color;
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b));
                /* NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed. */
                mainWin->nativeAddEllipse(e.centerX, e.centerY, e.radiusX, e.radiusY, 0, 0, OBJ_RUBBER_OFF); /*TODO: rotation and fill*/
            }
        }
        if (p->lines) {
            for (int i = 0; i < p->lines->count; i++) {
                EmbLine li = p->lines->line[i].line;
                EmbColor thisColor = p->lines->line[i].color;
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b));
                /* NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed. */
                mainWin->nativeAddLine(li.start.x, li.start.y, li.end.x, li.end.y, 0, OBJ_RUBBER_OFF); /*TODO: rotation*/
            }
        }
        if (p->paths) {
            /* TODO: This is unfinished. It needs more work*/
            for (int i=0; i < p->paths->count; i++) {
                EmbArray* curPointList = p->paths->path[i]->pointList;
                QPainterPath pathPath;
                EmbColor thisColor = p->paths->path[i]->color;
                if (curPointList->count > 0) {
                    EmbVector pp = curPointList[0].point->point;
                    pathPath.moveTo(pp.x, -pp.y); /*NOTE: Qt Y+ is down and libembroidery Y+ is up, so inverting the Y is needed.*/
                }
                for (int j = 1; j < curPointList->count; j++) {
                    EmbVector pp = curPointList[j].point->point;
                    pathPath.lineTo(pp.x, -pp.y); /*NOTE: Qt Y+ is down and libembroidery Y+ is up, so inverting the Y is needed.*/
                }
                QPen loadPen(qRgb(thisColor.r, thisColor.g, thisColor.b));
                loadPen.setWidthF(0.35);
                loadPen.setCapStyle(Qt::RoundCap);
                loadPen.setJoinStyle(Qt::RoundJoin);

                PathObject* obj = new PathObject(0,0, pathPath, loadPen.color().rgb());
                obj->setObjectRubberMode(OBJ_RUBBER_OFF);
                _mainWin->activeScene()->addItem(obj);
            }
        }
        if (p->points) {
            for (int i = 0; i < p->points->count; i++) {
                EmbVector po = p->points->point[i].point;
                EmbColor thisColor = p->points->point[i].color;
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b));
                /* NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed.*/
                mainWin->nativeAddPoint(po.x, po.y);
            }
        }
        if (p->polygons) {
            for (int i = 0; i < p->polygons->count; i++) {
                EmbArray *curPointList = p->polygons->polygon[i]->pointList;
                QPainterPath polygonPath;
                int firstPoint = 0;
                float startX = 0, startY = 0;
                float x = 0, y = 0;
                EmbColor thisColor = p->polygons->polygon[i]->color;
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b));
                for (int j=0; j<curPointList->count; j++) {
                    EmbVector pp = curPointList->point[j].point;
                    x = pp.x;
                    y = -pp.y; /*NOTE: Qt Y+ is down and libembroidery Y+ is up, so inverting the Y is needed.*/

                    if (firstPoint) {
                        polygonPath.lineTo(x,y);
                    } else {
                        polygonPath.moveTo(x,y);
                        firstPoint = 1;
                        startX = x;
                        startY = y;
                    }
                }
                polygonPath.translate(-startX, -startY);
                mainWin->nativeAddPolygon(startX, startY, polygonPath, OBJ_RUBBER_OFF);
            }
        }
        /* NOTE: Polylines should only contain NORMAL stitches. */
        if (p->polylines) {
            for (int i=0; i<p->polylines->count; i++) {
                EmbArray* curPointList = p->polylines->polyline[i]->pointList;
                QPainterPath polylinePath;
                int firstPoint = 0;
                float startX = 0, startY = 0;
                float x = 0, y = 0;
                EmbColor thisColor = p->polylines->polyline[i]->color;
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b));
                for (int j=0; j<curPointList->count; j++) {
                    EmbVector pp = curPointList->point[j].point;
                    x = pp.x;
                    y = -pp.y; /*NOTE: Qt Y+ is down and libembroidery Y+ is up, so inverting the Y is needed.*/
                    if (firstPoint) {
                        polylinePath.lineTo(x,y);
                    } else {
                        polylinePath.moveTo(x,y);
                        firstPoint = 1;
                        startX = x;
                        startY = y;
                    }
                }

                polylinePath.translate(-startX, -startY);
                mainWin->nativeAddPolyline(startX, startY, polylinePath, OBJ_RUBBER_OFF);
            }
        }
        if (p->rects) {
            for (int i=0; i<p->rects->count; i++) {
                EmbRect r = p->rects->rect[i].rect;
                EmbColor thisColor = p->rects->rect[i].color;
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b));
                /*NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed.*/
                mainWin->nativeAddRectangle(embRect_x(r), embRect_y(r), embRect_width(r), embRect_height(r), 0, 0, OBJ_RUBBER_OFF); /*TODO: rotation and fill*/
            }
        }
        setCurrentFile(fileName);
        mainWin->statusbar->showMessage("File loaded.");
        QString stitches;
        stitches.setNum(stitchCount);

        if(settings.grid_load_from_file) {
            /*TODO: Josh, provide me a hoop size and/or grid spacing from the pattern.*/
        }
        QApplication::restoreOverrideCursor();
    }
    embPattern_free(p);

    /* Clear the undo stack so it is not possible to undo past this point. */
    undo_history_length = 0;

    setCurrentColor(tmpColor);
    return 1;
}

void MdiWindow::print()
{
    /*
    QPrintDialog dialog(&printer, this);
    if (dialog.exec() == QDialog::Accepted) {
        QPainter painter(&printer);
        if (settings.printing_disable_bg) {
            // Save current bg
            QBrush brush = gview->backgroundBrush();
            // Save ink by not printing the bg at all
            gview->setBackgroundBrush(Qt::NoBrush);
            // Print, fitting the viewport contents into a full page
            gview->render(&painter);
            // Restore the bg
            gview->setBackgroundBrush(brush);
        } else {
            // Print, fitting the viewport contents into a full page
            gview->render(&painter);
        }
    }
    */
}

/* TODO: Save a Brother PEL image (An 8bpp, 130x113 pixel monochromatic? bitmap image) Why 8bpp when only 1bpp is needed?*/

/* TODO: Should BMC be limited to ~32KB or is this a mix up with Bitmap Cache?*/
/* TODO: Is there/should there be other embedded data in the bitmap besides the image itself?*/
/* NOTE: Can save a Singer BMC image (An 8bpp, 130x113 pixel colored bitmap image)*/
void MdiWindow::saveBMC()
{
    /* TODO: figure out how to center the image, right now it just plops it to the left side.*/
    QImage img(150, 150, QImage::Format_ARGB32_Premultiplied);
    img.fill(qRgb(255,255,255));
    QRectF extents = gscene->itemsBoundingRect();

    QPainter painter(&img);
    QRectF targetRect(0,0,150,150);
    if (settings.printing_disable_bg) { /*TODO: Make BMC background into it's own setting? */
        QBrush brush = gscene->backgroundBrush();
        gscene->setBackgroundBrush(Qt::NoBrush);
        gscene->update();
        gscene->render(&painter, targetRect, extents, Qt::KeepAspectRatio);
        gscene->setBackgroundBrush(brush);
    } else {
        gscene->update();
        gscene->render(&painter, targetRect, extents, Qt::KeepAspectRatio);
    }
    img.convertToFormat(QImage::Format_Indexed8, Qt::ThresholdDither|Qt::AvoidDither).save("test.bmc", "BMP");
}

void MdiWindow::setCurrentFile(const QString &fileName)
{
    curFile = QFileInfo(fileName).canonicalFilePath();
    setWindowModified(0);
    setWindowTitle(getShortCurrentFile());
}

QString MdiWindow::getShortCurrentFile()
{
    return QFileInfo(curFile).fileName();
}

QString MdiWindow::fileExtension(const QString& fileName)
{
    return QFileInfo(fileName).suffix().toLower();
}

void MdiWindow::closeEvent(QCloseEvent* /*e*/)
{
    debug_message("MdiWindow closeEvent()");
    emit sendCloseMdiWin(this);
}

void MdiWindow::onWindowActivated()
{
    debug_message("MdiWindow onWindowActivated()");
    status_bar[STATUS_SNAP]->setChecked(gscene->property("ENABLE_SNAP").toBool());
    status_bar[STATUS_GRID]->setChecked(gscene->property("ENABLE_GRID").toBool());
    status_bar[STATUS_RULER]->setChecked(gscene->property("ENABLE_RULER").toBool());
    status_bar[STATUS_ORTHO]->setChecked(gscene->property("ENABLE_ORTHO").toBool());
    status_bar[STATUS_POLAR]->setChecked(gscene->property("ENABLE_POLAR").toBool());
    status_bar[STATUS_QSNAP]->setChecked(gscene->property("ENABLE_QSNAP").toBool());
    status_bar[STATUS_QTRACK]->setChecked(gscene->property("ENABLE_QTRACK").toBool());
    status_bar[STATUS_LWT]->setChecked(gscene->property("ENABLE_LWT").toBool());
    /*mainWin->prompt->setHistory(promptHistory);*/
}

QSize MdiWindow::sizeHint() const
{
    debug_message("MdiWindow sizeHint()");
    return QSize(450, 300);
}

void MdiWindow::currentLayerChanged(const QString& layer)
{
    curLayer = layer;
}

void MdiWindow::currentColorChanged(const unsigned int& color)
{
    curColor = color;
}

void MdiWindow::currentLinetypeChanged(const QString& type)
{
    curLineType = type;
}

void MdiWindow::currentLineweightChanged(const QString& weight)
{
    curLineWeight = weight;
}

void MdiWindow::updateColorLinetypeLineweight()
{
}

void MdiWindow::deletePressed()
{
    gview->deletePressed();
}

void MdiWindow::escapePressed()
{
    gview->escapePressed();
}

void MdiWindow::showViewScrollBars(int val)
{
    gview->showScrollBars(val);
}

void MdiWindow::setViewCrossHairColor(unsigned int color)
{
    gview->setCrossHairColor(color);
}

void MdiWindow::setViewBackgroundColor(unsigned int color)
{
    gview->setBackgroundColor(color);
}

void MdiWindow::setViewSelectBoxColors(unsigned int colorL, unsigned int fillL, unsigned int colorR, unsigned int fillR, int alpha)
{
    gview->setSelectBoxColors(colorL, fillL, colorR, fillR, alpha);
}

void MdiWindow::setViewGridColor(unsigned int color)
{
    gview->setGridColor(color);
}

void MdiWindow::setViewRulerColor(unsigned int color)
{
    gview->setRulerColor(color);
}

PreviewDialog::PreviewDialog(QWidget* parent,
                             const QString& caption,
                             const QString& dir,
                             const QString& filter) : QFileDialog(parent, caption, dir, filter)
{
    debug_message("PreviewDialog Constructor");

    /*TODO: get actual thumbnail image from file, lets also use a size of 128x128 for now...*/
    /*TODO: make thumbnail size adjustable thru settings dialog*/
    imgWidget = new ImageWidget("icons/default/nopreview.png", this);

    QLayout* lay = layout();
    if(qobject_cast<QGridLayout*>(lay))
    {
        QGridLayout* grid = qobject_cast<QGridLayout*>(lay);
        grid->addWidget(imgWidget, 0, grid->columnCount(), grid->rowCount(), 1);
    }

    setModal(1);
    setOption(QFileDialog::DontUseNativeDialog);
    setViewMode(QFileDialog::Detail);
    setFileMode(QFileDialog::ExistingFiles);

    /*TODO: connect the currentChanged signal to update the preview imgWidget.*/
}

PreviewDialog::~PreviewDialog()
{
    debug_message("PreviewDialog Destructor");
}

SelectBox::SelectBox(Shape s, QWidget* parent) : QRubberBand(s, parent)
{
    /*Default values*/
    setColors(QColor(Qt::darkGreen), QColor(Qt::green), QColor(Qt::darkBlue), QColor(Qt::blue), 32);
}

void SelectBox::setDirection(int dir)
{
    if(!dir) { dirPen = leftPen;  dirBrush = leftBrush;  }
    else     { dirPen = rightPen; dirBrush = rightBrush; }
    boxDir = dir;
}

void SelectBox::setColors(const QColor& colorL, const QColor& fillL, const QColor& colorR, const QColor& fillR, int newAlpha)
{
    debug_message("SelectBox setColors()");
    alpha = newAlpha;

    leftPenColor = colorL; /*TODO: allow customization*/
    leftBrushColor = to_emb_color(QColor(fillL.red(), fillL.green(), fillL.blue(), alpha));
    rightPenColor = colorR; /*TODO: allow customization*/
    rightBrushColor = QColor(fillR.red(), fillR.green(), fillR.blue(), alpha);

    leftPen.setColor(leftPenColor);
    leftPen.setStyle(Qt::DashLine);
    leftBrush.setStyle(Qt::SolidPattern);
    leftBrush.setColor(to_qcolor(leftBrushColor));

    rightPen.setColor(rightPenColor);
    rightPen.setStyle(Qt::SolidLine);
    rightBrush.setStyle(Qt::SolidPattern);
    rightBrush.setColor(rightBrushColor);

    if(!boxDir) { dirPen = leftPen;  dirBrush = leftBrush;  }
    else        { dirPen = rightPen; dirBrush = rightBrush; }

    forceRepaint();
}

void SelectBox::paintEvent(QPaintEvent*)
{
    QPainter painter(this);
    painter.setPen(dirPen);
    painter.fillRect(0,0,width()-1, height()-1, dirBrush);
    painter.drawRect(0,0,width()-1, height()-1);
}

void SelectBox::forceRepaint()
{
    /*HACK: Take that QRubberBand!*/
    QSize hack = size();
    resize(hack + QSize(1,1));
    resize(hack);
}

StatusBarButton::StatusBarButton(QString buttonText, MainWindow* mw, StatusBar* statbar, QWidget *parent) : QToolButton(parent)
{
    statusbar = statbar;

    this->setObjectName("StatusBarButton" + buttonText);

    this->setText(buttonText);
    this->setAutoRaise(1);
    this->setCheckable(1);

    if (objectName() == "StatusBarButtonSNAP") {
        connect(this, SIGNAL(toggled(int)), this, SLOT(toggleSnap(int)));
    }
    else if (objectName() == "StatusBarButtonGRID") {
        connect(this, SIGNAL(toggled(int)), this, SLOT(toggleGrid(int)));
    }
    else if(objectName() == "StatusBarButtonRULER") {
        connect(this, SIGNAL(toggled(int)), this, SLOT(toggleRuler(int)));
    }
    else if(objectName() == "StatusBarButtonORTHO")  { connect(this, SIGNAL(toggled(int)), this, SLOT(toggleOrtho(int))); }
    else if(objectName() == "StatusBarButtonPOLAR")  { connect(this, SIGNAL(toggled(int)), this, SLOT(togglePolar(int))); }
    else if(objectName() == "StatusBarButtonQSNAP")  { connect(this, SIGNAL(toggled(int)), this, SLOT(toggleQSnap(int))); }
    else if(objectName() == "StatusBarButtonQTRACK") { connect(this, SIGNAL(toggled(int)), this, SLOT(toggleQTrack(int))); }
    else if(objectName() == "StatusBarButtonLWT")    { connect(this, SIGNAL(toggled(int)), this, SLOT(toggleLwt(int))); }
}

void StatusBarButton::contextMenuEvent(QContextMenuEvent *event)
{
    QApplication::setOverrideCursor(Qt::ArrowCursor);
    QMenu menu_(this);
    if (objectName() == "StatusBarButtonSNAP") {
        QAction* settingsSnapAction = new QAction(loadIcon(icon_gridsnapsettings), "&Settings...", &menu_);
        connect(settingsSnapAction, SIGNAL(triggered()), this, SLOT(settingsSnap()));
        menu_.addAction(settingsSnapAction);
    }
    else if (objectName() == "StatusBarButtonGRID") {
        QAction* settingsGridAction = new QAction(loadIcon(icon_gridsettings), "&Settings...", &menu_);
        connect(settingsGridAction, SIGNAL(triggered()), this, SLOT(settingsGrid()));
        menu_.addAction(settingsGridAction);
    }
    else if (objectName() == "StatusBarButtonRULER") {
        QAction* settingsRulerAction = new QAction(QIcon("icons/rulersettings.png"), "&Settings...", &menu_);
        connect(settingsRulerAction, SIGNAL(triggered()), this, SLOT(settingsRuler()));
        menu_.addAction(settingsRulerAction);
    }
    else if (objectName() == "StatusBarButtonORTHO") {
        QAction* settingsOrthoAction = new QAction(QIcon("icons/orthosettings.png"), "&Settings...", &menu_);
        connect(settingsOrthoAction, SIGNAL(triggered()), this, SLOT(settingsOrtho()));
        menu_.addAction(settingsOrthoAction);
    }
    else if (objectName() == "StatusBarButtonPOLAR") {
        QAction* settingsPolarAction = new QAction(QIcon("icons/polarsettings.png"), "&Settings...", &menu_);
        connect(settingsPolarAction, SIGNAL(triggered()), this, SLOT(settingsPolar()));
        menu_.addAction(settingsPolarAction);
    }
    else if(objectName() == "StatusBarButtonQSNAP")
    {
        QAction* settingsQSnapAction = new QAction(QIcon("icons/qsnapsettings.png"), "&Settings...", &menu_);
        connect(settingsQSnapAction, SIGNAL(triggered()), this, SLOT(settingsQSnap()));
        menu_.addAction(settingsQSnapAction);
    }
    else if(objectName() == "StatusBarButtonQTRACK")
    {
        QAction* settingsQTrackAction = new QAction(QIcon("icons/qtracksettings.png"), "&Settings...", &menu_);
        connect(settingsQTrackAction, SIGNAL(triggered()), this, SLOT(settingsQTrack()));
        menu_.addAction(settingsQTrackAction);
    }
    else if(objectName() == "StatusBarButtonLWT") {
        View* gview = _mainWin->activeView();
        if (gview) {
            QAction* enableRealAction = new QAction(QIcon("icons/realrender.png"), "&RealRender On", &menu_);
            enableRealAction->setEnabled(!gview->isRealEnabled());
            connect(enableRealAction, SIGNAL(triggered()), this, SLOT(enableReal()));
            menu_.addAction(enableRealAction);

            QAction* disableRealAction = new QAction(QIcon("icons/realrender.png"), "&RealRender Off", &menu_);
            disableRealAction->setEnabled(gview->isRealEnabled());
            connect(disableRealAction, SIGNAL(triggered()), this, SLOT(disableReal()));
            menu_.addAction(disableRealAction);
        }

        QAction* settingsLwtAction = new QAction(loadIcon(icon_lineweightsettings), "&Settings...", &menu_);
        connect(settingsLwtAction, SIGNAL(triggered()), this, SLOT(settingsLwt()));
        menu_.addAction(settingsLwtAction);
    }
    menu_.exec(event->globalPos());
    QApplication::restoreOverrideCursor();
    statusbar->clearMessage();
}

StatusBar::StatusBar(MainWindow* mw, QWidget *parent) : QStatusBar(parent)
{
    int i;
    this->setObjectName("StatusBar");

    for (i=0; i<N_STATUS; i++) {
        status_bar[i] = new StatusBarButton(status_bar_label[i], _mainWin, this, this);
    }
    statusBarMouseCoord = new QLabel(this);

    statusBarMouseCoord->setMinimumWidth(300); /* Must fit this text always*/
    statusBarMouseCoord->setMaximumWidth(300); /* "+1.2345E+99, +1.2345E+99, +1.2345E+99"*/

    this->addWidget(statusBarMouseCoord);
    for (i=0; i<N_STATUS; i++) {
        this->addWidget(status_bar[i]);
    }
}

void StatusBar::setMouseCoord(float x, float y)
{
    /* TODO: set format from settings (Architectural, Decimal, Engineering, Fractional, Scientific) */

    /* Decimal */
    statusBarMouseCoord->setText(QString().setNum(x, 'F', 4) + ", " + QString().setNum(y, 'F', 4)); /*TODO: use precision from unit settings*/

    /* Scientific */
    /* statusBarMouseCoord->setText(QString().setNum(x, 'E', 4) + ", " + QString().setNum(y, 'E', 4)); */
    /* TODO: use precision from unit settings */
}

