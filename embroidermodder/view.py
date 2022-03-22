#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENCE for licensing terms.

    ------------------------------------------------------------

    Another attempt at a graphical user interface that runs on
    lots of machines without a complex build or fragile dependencies.

    This is a translation of some of the ideas we came up with for other
    attempts.
"""

import libembroidery


class View():
    """
    There are 4 regions managed as views, .

    We don't have a seperate window for the pop-ups like the file
    browser for opening or saving a file. Instead, a view will
    be created 
    """

    def __init__(self):
        return self


class View : public QGraphicsView:
    Q_OBJECT

public:
    View(MainWindow* mw, QGraphicsScene* theScene, QWidget* parent)
    ~View()

    int allowZoomIn()
    int allowZoomOut()

    void recalculateLimits()
    void zoomToPoint(const QPoint& mousePoint, int zoomDir)
    void centerAt(const QPointF& centerPoint)
    QPointF center() { return mapToScene(rect().center()); }

    void addObject(BaseObject* obj)
    void deleteObject(BaseObject* obj)
    void vulcanizeObject(BaseObject* obj)

public slots:
    void zoomIn()
    void zoomOut()
    void zoomWindow()
    void zoomSelected()
    void zoomExtents()
    void panRealTime()
    void panPoint()
    void panLeft()
    void panRight()
    void panUp()
    void panDown()
    void selectAll()
    void selectionChanged()
    void clearSelection()
    void deleteSelected()
    void moveSelected(float dx, float dy)
    void cut()
    void copy()
    void paste()
    void repeatAction()
    void moveAction()
    void scaleAction()
    void scaleSelected(float x, float y, float factor)
    void rotateAction()
    void rotateSelected(float x, float y, float rot)
    void mirrorSelected(float x1, float y1, float x2, float y2)
    int  numSelected()

    void deletePressed()
    void escapePressed()

    void cornerButtonClicked()

    void showScrollBars(int val)
    void setCornerButton()
    void setCrossHairColor(unsigned int color)
    void setCrossHairSize(unsigned char percent)
    void setBackgroundColor(unsigned int color)
    void setSelectBoxColors(unsigned int colorL, unsigned int fillL, unsigned int colorR, unsigned int fillR, int alpha)
    void toggleSnap(int on)
    void toggleGrid(int on)
    void toggleRuler(int on)
    void toggleOrtho(int on)
    void togglePolar(int on)
    void toggleQSnap(int on)
    void toggleQTrack(int on)
    void toggleLwt(int on)
    void toggleReal(int on)
    int isLwtEnabled()
    int isRealEnabled()

    void setGridColor(unsigned int color)
    void createGrid(const QString& gridType)
    void setRulerColor(unsigned int color)

    void previewOn(int clone, int mode, float x, float y, float data)
    void previewOff()

    void enableMoveRapidFire()
    void disableMoveRapidFire()

    int allowRubber()
    void addToRubberRoom(QGraphicsItem* item)
    void vulcanizeRubberRoom()
    void clearRubberRoom()
    void spareRubber(int id)
    void setRubberMode(int mode)
    void setRubberPoint(const QString& key, const QPointF& point)
    void setRubberText(const QString& key, const QString& txt)

protected:
    void mouseDoubleClickEvent(QMouseEvent* event)
    void mousePressEvent(QMouseEvent* event)
    void mouseMoveEvent(QMouseEvent* event)
    void mouseReleaseEvent(QMouseEvent* event)
    void wheelEvent(QWheelEvent* event)
    void contextMenuEvent(QContextMenuEvent* event)
    void drawBackground(QPainter* painter, const QRectF& rect)
    void drawForeground(QPainter* painter, const QRectF& rect)
    void enterEvent(QEvent* event)

private:
    QHash<int, QGraphicsItem*> hashDeletedObjects

    QList<int> spareRubberList

    QColor gridColor
    QPainterPath gridPath
    void createGridRect()
    void createGridPolar()
    void createGridIso()
    QPainterPath originPath
    void createOrigin()

    void loadRulerSettings()

    int willUnderflowInt32(int a, int b)
    int willOverflowInt32(int a, int b)
    int roundToMultiple(int roundUp, int numToRound, int multiple)
    QPainterPath createRulerTextPath(float x, float y, QString str, float height)

    QList<QGraphicsItem*> previewObjectList
    QGraphicsItemGroup* previewObjectItemGroup
    QPointF previewPoint
    float previewData
    int previewMode

    QList<QGraphicsItem*> createObjectList(QList<QGraphicsItem*> list)
    QPointF cutCopyMousePoint
    QGraphicsItemGroup* pasteObjectItemGroup

    QList<QGraphicsItem*> rubberRoomList

    void copySelected()

    void startGripping(BaseObject* obj)
    void stopGripping(int accept = false)

    BaseObject* gripBaseObj
    BaseObject* tempBaseObj

    MainWindow* mainWin
    QGraphicsScene* gscene

    SelectBox* selectBox

    void updateMouseCoords(int x, int y)

    void panStart(const QPoint& point)
    int panDistance
    int panStartX
    int panStartY

    void alignScenePointWithViewPoint(const QPointF& scenePoint, const QPoint& viewPoint)
]


View::~View():
    /*Prevent memory leaks by deleting any objects that were removed from the scene*/
    qDeleteAll(hashDeletedObjects.begin(), hashDeletedObjects.end())
    hashDeletedObjects.clear()

    /*Prevent memory leaks by deleting any unused instances*/
    qDeleteAll(previewObjectList.begin(), previewObjectList.end())
    previewObjectList.clear()

def View::enterEvent(QEvent* /*event*/):
    QMdiSubWindow* mdiWin = qobject_cast<QMdiSubWindow*>(parent())
    if(mdiWin) mainWin->mdiArea->setActiveSubWindow(mdiWin)

def View::addObject(BaseObject* obj):
    gscene->addItem(obj)
    gscene->update()
    hashDeletedObjects.remove(obj->objID)

def View::deleteObject(BaseObject* obj):
    /*NOTE: We really just remove the objects from the scene. deletion actually occurs in the destructor.*/
    obj->setSelected(0)
    gscene->removeItem(obj)
    gscene->update()
    hashDeletedObjects.insert(obj->objID, obj)

def View::previewOn(int clone, int mode, float x, float y, float data):
    debug_message("View previewOn()")
    previewOff(); /*Free the old objects before creating new ones*/

    previewMode = mode

    /*Create new objects and add them to the scene in an item group.*/
    if     (clone == PREVIEW_CLONE_SELECTED) previewObjectList = createObjectList(gscene->selectedItems())
    else if(clone == PREVIEW_CLONE_RUBBER)   previewObjectList = createObjectList(rubberRoomList)
    else return
    previewObjectItemGroup = gscene->createItemGroup(previewObjectList)

    if(previewMode == PREVIEW_MODE_MOVE   ||
       previewMode == PREVIEW_MODE_ROTATE ||
       previewMode == PREVIEW_MODE_SCALE)
    {
        previewPoint = QPointF(x, y); /*NOTE: Move: basePt; Rotate: basePt;   Scale: basePt;*/
        previewData = data;           /*NOTE: Move: unused; Rotate: refAngle; Scale: refFactor;*/
        settings.previewActive = 1
    }
    else
    {
        previewMode = PREVIEW_MODE_NULL
        previewPoint = QPointF()
        previewData = 0
        settings.previewActive = 0
    }

    gscene->update()

def View::previewOff():
    /*Prevent memory leaks by deleting any unused instances*/
    qDeleteAll(previewObjectList.begin(), previewObjectList.end())
    previewObjectList.clear()

    if(previewObjectItemGroup)
    {
        gscene->removeItem(previewObjectItemGroup)
        delete previewObjectItemGroup
        previewObjectItemGroup = 0
    }

    settings.previewActive = 0

    gscene->update()

def View::enableMoveRapidFire():
    settings.rapidMoveActive = 1

def View::disableMoveRapidFire():
    settings.rapidMoveActive = 0

int View::allowRubber():
    /*if(!rubberRoomList.size()) //TODO: this check should be removed later*/
        return 1
    return 0

def View::addToRubberRoom(QGraphicsItem* item):
    rubberRoomList.append(item)
    item->show()
    gscene->update()

def View::vulcanizeRubberRoom():
    foreach(QGraphicsItem* item, rubberRoomList)
    {
        BaseObject* base = static_cast<BaseObject*>(item)
        if(base) vulcanizeObject(base)
    }
    rubberRoomList.clear()
    gscene->update()

def View::vulcanizeObject(BaseObject* obj):
    if(!obj) return
    gscene->removeItem(obj)
    /* Prevent Qt Runtime Warning, QGraphicsScene::addItem:
     * item has already been added to this scene.
     */
    obj->vulcanize()

def View::clearRubberRoom():
    foreach(QGraphicsItem* item, rubberRoomList)
    {
        BaseObject* base = static_cast<BaseObject*>(item)
        if(base)
        {
            int type = base->type()
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
  "The object will be deleted."))
                    gscene->removeItem(item)
                    delete item
                }
                else
                    vulcanizeObject(base)
            }
            else
            {
                gscene->removeItem(item)
                delete item
            }
        }
    }

    rubberRoomList.clear()
    spareRubberList.clear()
    gscene->update()

def View::spareRubber(int id):
    spareRubberList.append(id)

def View::setRubberMode(int mode):
    foreach(QGraphicsItem* item, rubberRoomList)
    {
        BaseObject* base = static_cast<BaseObject*>(item)
        if(base) { base->setObjectRubberMode(mode); }
    }
    gscene->update()

def View::setRubberPoint(const QString& key, const QPointF& point):
    foreach(QGraphicsItem* item, rubberRoomList)
    {
        BaseObject* base = static_cast<BaseObject*>(item)
        if(base) { base->setObjectRubberPoint(key, point); }
    }
    gscene->update()

def View::setRubberText(const QString& key, const QString& txt):
    foreach(QGraphicsItem* item, rubberRoomList)
    {
        BaseObject* base = static_cast<BaseObject*>(item)
        if(base) { base->setObjectRubberText(key, txt); }
    }
    gscene->update()

def View::setGridColor(unsigned int color):
    gridColor = QColor(color)
    gscene->setProperty("VIEW_COLOR_GRID", color)
    if(gscene) gscene->update()

def View::setRulerColor(unsigned int color):
    rulerColor = QColor(color)
    gscene->update()

def View::createGrid(const QString& gridType):
    if (gridType == "Rectangular") {
        createGridRect()
        gscene->setProperty("ENABLE_GRID", 1)
    }
    else if(gridType == "Circular") {
        createGridPolar()
        gscene->setProperty("ENABLE_GRID", 1)
    }
    else if(gridType == "Isometric") {
        createGridIso()
        gscene->setProperty("ENABLE_GRID", 1)
    }
    else {
        gridPath = QPainterPath()
        gscene->setProperty("ENABLE_GRID", 0)
    }

    createOrigin()

    /* EXPERIMENT
     * Tagging experiments with the path system to the origin.
     */

    float position[] = {10.0, 0.0]
    float scale[] = {1.0, 1.0]
    add_list_to_path(&originPath, origin_string, position, scale)

    gscene->update()

def View::createOrigin() /* TODO: Make Origin Customizable */:
    originPath = QPainterPath()

    if (settings.grid_show_origin) {
        /* originPath.addEllipse(QPointF(0,0), 0.5, 0.5);*/
        /* TODO: Make Origin Customizable */
        float position[] = {0.0, 0.0]
        float scale[] = {1.0, 1.0]
        add_list_to_path(&originPath, origin_string, position, scale)
    }
}

def View::createGridRect():
    float xSpacing = settings.grid_spacing.x
    float ySpacing = settings.grid_spacing.y

    QRectF gr(0, 0, settings.grid_size.x, -settings.grid_size.y)
    /*Ensure the loop will work correctly with negative numbers*/
    float x1 = embMinDouble(gr.left(), gr.right())
    float y1 = embMinDouble(gr.top(), gr.bottom())
    float x2 = embMaxDouble(gr.left(), gr.right())
    float y2 = embMaxDouble(gr.top(), gr.bottom())

    gridPath = QPainterPath()
    gridPath.addRect(gr)
    for (float gx = x1; gx < x2; gx += xSpacing) {
        for (float gy = y1; gy < y2; gy += ySpacing) {
            gridPath.moveTo(x1,gy)
            gridPath.lineTo(x2,gy)
            gridPath.moveTo(gx,y1)
            gridPath.lineTo(gx,y2)
        }
    }

    /*Center the Grid*/
    QRectF gridRect = gridPath.boundingRect()
    float bx = gridRect.width()/2.0
    float by = -gridRect.height()/2.0
    float cx = settings.grid_center.x
    float cy = -settings.grid_center.y
    float dx = cx - bx
    float dy = cy - by

    if(settings.grid_center_on_origin)
        gridPath.translate(-bx, -by)
    else
        gridPath.translate(dx, dy)

def View::createGridPolar():
    float radSpacing = settings.grid_spacing_radius
    float angSpacing = settings.grid_spacing_angle

    float rad = settings.grid_size_radius

    gridPath = QPainterPath()
    gridPath.addEllipse(QPointF(0,0), rad, rad)
    for(float r = 0; r < rad; r += radSpacing) {
        gridPath.addEllipse(QPointF(0,0), r, r)
    }
    for(float ang = 0; ang < 360; ang += angSpacing) {
        gridPath.moveTo(0,0)
        gridPath.lineTo(QLineF::fromPolar(rad, ang).p2())
    }

    if(!settings.grid_center_on_origin)
        gridPath.translate(settings.grid_center.x, -settings.grid_center.y)

def View::createGridIso():
    /* Ensure the loop will work correctly with negative numbers */
    float isoW = fabs(settings.grid_size.x)
    float isoH = fabs(settings.grid_size.y)

    QPointF p1 = QPointF(0,0)
    QPointF p2 = QLineF::fromPolar(isoW, 30).p2()
    QPointF p3 = QLineF::fromPolar(isoH, 150).p2()
    QPointF p4 = p2 + p3

    gridPath = QPainterPath()
    gridPath.moveTo(p1)
    gridPath.lineTo(p2)
    gridPath.lineTo(p4)
    gridPath.lineTo(p3)
    gridPath.lineTo(p1)

    for (float x = 0; x < isoW; x += settings.grid_spacing.x) {
        for (float y = 0; y < isoH; y += settings.grid_spacing.y) {
            QPointF px = QLineF::fromPolar(x, 30).p2()
            QPointF py = QLineF::fromPolar(y, 150).p2()

            gridPath.moveTo(px)
            gridPath.lineTo(px+p3)
            gridPath.moveTo(py)
            gridPath.lineTo(py+p2)
        }
    }

    /*Center the Grid*/

    QRectF gridRect = gridPath.boundingRect()
    /* bx is unused*/
    float by = -gridRect.height()/2.0
    float cx = settings.grid_center.x
    float cy = -settings.grid_center.y

    if (settings.grid_center_on_origin) {
        gridPath.translate(0, -by)
    }
    else {
        gridPath.translate(0, -by)
        gridPath.translate(cx, cy)
    }
}

def View::toggleSnap(int on):
    debug_message("View toggleSnap()")
    QApplication::setOverrideCursor(Qt::WaitCursor)
    /*TODO: finish this*/
    gscene->setProperty("ENABLE_SNAP", on)
    gscene->update()
    QApplication::restoreOverrideCursor()

def View::toggleGrid(int on):
    debug_message("View toggleGrid()")
    QApplication::setOverrideCursor(Qt::WaitCursor)
    if(on) { createGrid(settings.grid_type); }
    else   { createGrid(""); }
    QApplication::restoreOverrideCursor()

def View::toggleRuler(int on):
    debug_message("View toggleRuler()")
    QApplication::setOverrideCursor(Qt::WaitCursor)
    gscene->setProperty("ENABLE_RULER", on)
    settings.rulerMetric = settings.ruler_metric
    rulerColor = QColor(settings.ruler_color)
    settings.rulerPixelSize = settings.ruler_pixel_size
    gscene->update()
    QApplication::restoreOverrideCursor()

def View::toggleOrtho(int on):
    debug_message("View toggleOrtho()")
    QApplication::setOverrideCursor(Qt::WaitCursor)
    /*TODO: finish this*/
    gscene->setProperty("ENABLE_ORTHO", on)
    gscene->update()
    QApplication::restoreOverrideCursor()

def View::togglePolar(int on):
    debug_message("View togglePolar()")
    QApplication::setOverrideCursor(Qt::WaitCursor)
    /*TODO: finish this*/
    gscene->setProperty("ENABLE_POLAR", on)
    gscene->update()
    QApplication::restoreOverrideCursor()

def View::toggleQSnap(int on):
    debug_message("View toggleQSnap()")
    QApplication::setOverrideCursor(Qt::WaitCursor)
    settings.qSnapToggle = on
    gscene->setProperty("ENABLE_QSNAP", on)
    gscene->update()
    QApplication::restoreOverrideCursor()

def View::toggleQTrack(int on):
    debug_message("View toggleQTrack()")
    QApplication::setOverrideCursor(Qt::WaitCursor)
    /*TODO: finish this*/
    gscene->setProperty("ENABLE_QTRACK", on)
    gscene->update()
    QApplication::restoreOverrideCursor()

def View::toggleLwt(int on):
    debug_message("View toggleLwt()")
    QApplication::setOverrideCursor(Qt::WaitCursor)
    gscene->setProperty("ENABLE_LWT", on)
    gscene->update()
    QApplication::restoreOverrideCursor()

def View::toggleReal(int on):
    debug_message("View toggleReal()")
    QApplication::setOverrideCursor(Qt::WaitCursor)
    gscene->setProperty("ENABLE_REAL", on)
    gscene->update()
    QApplication::restoreOverrideCursor()

int View::isLwtEnabled():
    return gscene->property("ENABLE_LWT").toBool()

int View::isRealEnabled():
    return gscene->property("ENABLE_REAL").toBool()

def View::drawBackground(QPainter* painter, const QRectF& rect):
    painter->fillRect(rect, backgroundBrush())

    /* HACK int a = rect.intersects(gridPath.controlPointRect(); */
    int a = 1
    if (gscene->property("ENABLE_GRID").toBool() && a)
    {
        QPen gridPen(gridColor)
        gridPen.setJoinStyle(Qt::MiterJoin)
        gridPen.setCosmetic(1)
        painter->setPen(gridPen)
        painter->drawPath(gridPath)
        painter->drawPath(originPath)
        painter->fillPath(originPath, gridColor)
    }
}

/*
float little = 0.20, medium = 0.40
float tic_metric_lengths[] = {
    0.0, little, little, little, little, middle,
    little, little, little, little
]
float tic_imperial_lengths[] = {
    0.0, little, little, little, medium,
    little, little, little, medium,
    little, little, little, medium,
    little, little, little
]
*/

def View::drawForeground(QPainter* painter, const QRectF& rect):
    /* ==================================================
     * Draw grip points for all selected objects
     * ================================================== */

    QPen gripPen(QColor::fromRgb(gripColorCool))
    gripPen.setWidth(2)
    gripPen.setJoinStyle(Qt::MiterJoin)
    gripPen.setCosmetic(1)
    painter->setPen(gripPen)
    QPoint gripOffset(settings.selection_grip_size, settings.selection_grip_size)

    QList<QPointF> selectedGripPoints
    QList<QGraphicsItem*> selectedItemList = gscene->selectedItems()
    if (selectedItemList.size() <= 100) {
        foreach(QGraphicsItem* item, selectedItemList) {
            if(item->type() >= OBJ_TYPE_BASE) {
                tempBaseObj = static_cast<BaseObject*>(item)
                if(tempBaseObj) { selectedGripPoints = tempBaseObj->allGripPoints(); }

                foreach(QPointF ssp, selectedGripPoints) {
                    QPoint p1 = mapFromScene(ssp) - gripOffset
                    QPoint q1 = mapFromScene(ssp) + gripOffset

                    if(ssp == sceneGripPoint)
                        painter->fillRect(QRectF(mapToScene(p1), mapToScene(q1)), QColor::fromRgb(gripColorHot))
                    else
                        painter->drawRect(QRectF(mapToScene(p1), mapToScene(q1)))
                }
            }
        }
    }

    /* ==================================================
     * Draw the closest qsnap point
     * ================================================== */

    if(!settings.selectingActive) /*TODO: && findClosestSnapPoint == 1*/
    {
        QPen qsnapPen(QColor::fromRgb(qsnapLocatorColor))
        qsnapPen.setWidth(2)
        qsnapPen.setJoinStyle(Qt::MiterJoin)
        qsnapPen.setCosmetic(1)
        painter->setPen(qsnapPen)
        QPoint qsnapOffset(settings.qsnap_locator_size, settings.qsnap_locator_size)

        QList<QPointF> apertureSnapPoints
        QList<QGraphicsItem *> apertureItemList = items(viewMousePoint.x()-settings.qsnap_aperture_size,
                                                        viewMousePoint.y()-settings.qsnap_aperture_size,
                                                        settings.qsnap_aperture_size*2,
                                                        settings.qsnap_aperture_size*2)
        foreach (QGraphicsItem* item, apertureItemList) {
            if (item->type() >= OBJ_TYPE_BASE) {
                tempBaseObj = static_cast<BaseObject*>(item)
                if(tempBaseObj) { apertureSnapPoints << tempBaseObj->mouseSnapPoint(to_qpointf(sceneMousePoint)); }
            }
        }
        /*TODO: Check for intersection snap points and add them to the list*/
        foreach(QPointF asp, apertureSnapPoints)
        {
            QPoint p1 = mapFromScene(asp) - qsnapOffset
            QPoint q1 = mapFromScene(asp) + qsnapOffset
            painter->drawRect(QRectF(mapToScene(p1), mapToScene(q1)))
        }
    }

    /* ==================================================
     * Draw horizontal and vertical rulers
     * ================================================== */

    if (gscene->property("ENABLE_RULER").toBool()) {
        int proceed = 1

        int vw = width();  /*View Width*/
        int vh = height(); /*View Height*/
        QPointF origin = mapToScene(0,0)
        QPointF rulerHoriz = mapToScene(vw, settings.rulerPixelSize)
        QPointF rulerVert = mapToScene(settings.rulerPixelSize, vh)

        float ox = origin.x()
        float oy = origin.y()

        float rhx = rulerHoriz.x()
        float rhy = rulerHoriz.y()
        float rhw = rhx - ox
        float rhh = rhy - oy

        float rvx = rulerVert.x()
        float rvy = rulerVert.y()
        float rvw = rvx - ox
        float rvh = rvy - oy

        /*
         * NOTE:
         * Drawing ruler if zoomed out too far will cause an assertion failure.
         * We will limit the maximum size the ruler can be shown at.
         */

        unsigned short maxSize = -1; /*Intentional underflow*/
        if(rhw >= maxSize || rvh >= maxSize) proceed = 0

        if (proceed) {
            int distance = mapToScene(settings.rulerPixelSize*3, 0).x() - ox
            QString distStr = QString().setNum(distance)
            int distStrSize = distStr.size()
            int msd = distStr.at(0).digitValue(); /*Most Significant Digit*/

            if(msd != -1)
            {

                msd++
                if(msd == 10)
                {
                    msd = 1
                    distStr.resize(distStrSize+1)
                    distStrSize++
                }

                distStr.replace(0, 1, QString().setNum(msd))
                for(int i = 1; i < distStrSize; ++i)
                {
                    distStr.replace(i, 1, '0')
                }
                int unit = distStr.toInt()
                float fraction
                int feet = 1
                if (settings.rulerMetric) {
                    if(unit < 10) unit = 10
                    fraction = unit/10
                }
                else {
                    if (unit <= 1) {
                        unit = 1
                        feet = 0
                        fraction = (float)(unit/16)
                    }
                    else
                    {
                        unit = roundToMultiple(1, unit, 12)
                        fraction = unit/12
                    }
                }

                float little = 0.20
                float medium = 0.40
                float rhTextOffset = mapToScene(3, 0).x() - ox
                float rvTextOffset = mapToScene(0, 3).y() - oy
                float textHeight = rhh*medium

                QVector<QLineF> lines
                lines.append(QLineF(ox, rhy, rhx, rhy))
                lines.append(QLineF(rvx, oy, rvx, rvy))

                float mx = sceneMousePoint.x
                float my = sceneMousePoint.y
                lines.append(QLineF(mx, rhy, mx, oy))
                lines.append(QLineF(rvx, my, ox, my))

                QTransform transform

                QPen rulerPen(QColor(0,0,0))
                rulerPen.setCosmetic(1)
                painter->setPen(rulerPen)
                painter->fillRect(QRectF(ox, oy, rhw, rhh), rulerColor)
                painter->fillRect(QRectF(ox, oy, rvw, rvh), rulerColor)

                int xFlow, xStart, yFlow, yStart
                if (willUnderflowInt32(ox, unit)) {
                    proceed = 0
                }
                else {
                    xFlow = roundToMultiple(0, ox, unit)
                }
                if (willUnderflowInt32(xFlow, unit)) {
                    proceed = 0
                }
                else { xStart = xFlow - unit; }
                if (willUnderflowInt32(oy, unit)) { proceed = 0; }
                else { yFlow = roundToMultiple(0, oy, unit); }
                if(willUnderflowInt32(yFlow, unit)) { proceed = 0; }
                else                             { yStart = yFlow - unit; }

                if (proceed) {
                    for (int x = xStart; x < rhx; x += unit) {
                        transform.translate(x+rhTextOffset, rhy-rhh/2)
                        QPainterPath rulerTextPath
                        if (settings.rulerMetric) {
                            rulerTextPath = transform.map(createRulerTextPath(0, 0, QString().setNum(x), textHeight))
                        }
                        else {
                            if(feet)
                                rulerTextPath = transform.map(createRulerTextPath(0, 0, QString().setNum(x/12).append('\''), textHeight))
                            else
                                rulerTextPath = transform.map(createRulerTextPath(0, 0, QString().setNum(x).append('\"'), textHeight))
                        }
                        transform.reset()
                        painter->drawPath(rulerTextPath)

                        lines.append(QLineF(x, rhy, x, oy))
                        if (settings.rulerMetric) {
                            lines.append(QLineF(x, rhy, x, oy))
                            lines.append(QLineF(x+fraction  , rhy, x+fraction, rhy-rhh*little))
                            lines.append(QLineF(x+fraction*2, rhy, x+fraction*2, rhy-rhh*little))
                            lines.append(QLineF(x+fraction*3, rhy, x+fraction*3, rhy-rhh*little))
                            lines.append(QLineF(x+fraction*4, rhy, x+fraction*4, rhy-rhh*little))
                            lines.append(QLineF(x+fraction*5, rhy, x+fraction*5, rhy-rhh*medium)); /*Half*/
                            lines.append(QLineF(x+fraction*6, rhy, x+fraction*6, rhy-rhh*little))
                            lines.append(QLineF(x+fraction*7, rhy, x+fraction*7, rhy-rhh*little))
                            lines.append(QLineF(x+fraction*8, rhy, x+fraction*8, rhy-rhh*little))
                            lines.append(QLineF(x+fraction*9, rhy, x+fraction*9, rhy-rhh*little))
                        }
                        else {
                            if (feet) {
                                for (int i = 0; i < 12; ++i) {
                                    lines.append(QLineF(x+fraction*i, rhy, x+fraction*i, rhy-rhh*medium))
                                }
                            }
                            else
                            {
                                lines.append(QLineF(x+fraction   , rhy, x+fraction, rhy-rhh*little))
                                lines.append(QLineF(x+fraction* 2, rhy, x+fraction* 2, rhy-rhh*little))
                                lines.append(QLineF(x+fraction* 3, rhy, x+fraction* 3, rhy-rhh*little))
                                lines.append(QLineF(x+fraction* 4, rhy, x+fraction* 4, rhy-rhh*medium)); /*Quarter*/
                                lines.append(QLineF(x+fraction* 5, rhy, x+fraction* 5, rhy-rhh*little))
                                lines.append(QLineF(x+fraction* 6, rhy, x+fraction* 6, rhy-rhh*little))
                                lines.append(QLineF(x+fraction* 7, rhy, x+fraction* 7, rhy-rhh*little))
                                lines.append(QLineF(x+fraction* 8, rhy, x+fraction* 8, rhy-rhh*medium)); /*Half*/
                                lines.append(QLineF(x+fraction* 9, rhy, x+fraction* 9, rhy-rhh*little))
                                lines.append(QLineF(x+fraction*10, rhy, x+fraction*10, rhy-rhh*little))
                                lines.append(QLineF(x+fraction*11, rhy, x+fraction*11, rhy-rhh*little))
                                lines.append(QLineF(x+fraction*12, rhy, x+fraction*12, rhy-rhh*medium)); /*Quarter*/
                                lines.append(QLineF(x+fraction*13, rhy, x+fraction*13, rhy-rhh*little))
                                lines.append(QLineF(x+fraction*14, rhy, x+fraction*14, rhy-rhh*little))
                                lines.append(QLineF(x+fraction*15, rhy, x+fraction*15, rhy-rhh*little))
                            }
                        }
                    }
                    for (int y = yStart; y < rvy; y += unit) {
                        transform.translate(rvx-rvw/2, y-rvTextOffset)
                        transform.rotate(-90)
                        QPainterPath rulerTextPath
                        if (settings.rulerMetric) {
                            rulerTextPath = transform.map(createRulerTextPath(0, 0, QString().setNum(-y), textHeight))
                        }
                        else {
                            if(feet)
                                rulerTextPath = transform.map(createRulerTextPath(0, 0, QString().setNum(-y/12).append('\''), textHeight))
                            else
                                rulerTextPath = transform.map(createRulerTextPath(0, 0, QString().setNum(-y).append('\"'), textHeight))
                        }
                        transform.reset()
                        painter->drawPath(rulerTextPath)

                        lines.append(QLineF(rvx, y, ox, y))
                        if (settings.rulerMetric) {
                            lines.append(QLineF(rvx, y+fraction  , rvx-rvw*little, y+fraction))
                            lines.append(QLineF(rvx, y+fraction*2, rvx-rvw*little, y+fraction*2))
                            lines.append(QLineF(rvx, y+fraction*3, rvx-rvw*little, y+fraction*3))
                            lines.append(QLineF(rvx, y+fraction*4, rvx-rvw*little, y+fraction*4))
                            lines.append(QLineF(rvx, y+fraction*5, rvx-rvw*medium, y+fraction*5)); /*Half*/
                            lines.append(QLineF(rvx, y+fraction*6, rvx-rvw*little, y+fraction*6))
                            lines.append(QLineF(rvx, y+fraction*7, rvx-rvw*little, y+fraction*7))
                            lines.append(QLineF(rvx, y+fraction*8, rvx-rvw*little, y+fraction*8))
                            lines.append(QLineF(rvx, y+fraction*9, rvx-rvw*little, y+fraction*9))
                        }
                        else {
                            if (feet) {
                                for (int i = 0; i < 12; ++i) {
                                    lines.append(QLineF(rvx, y+fraction*i, rvx-rvw*medium, y+fraction*i))
                                }
                            }
                            else {
                                lines.append(QLineF(rvx, y+fraction   , rvx-rvw*little, y+fraction))
                                lines.append(QLineF(rvx, y+fraction* 2, rvx-rvw*little, y+fraction* 2))
                                lines.append(QLineF(rvx, y+fraction* 3, rvx-rvw*little, y+fraction* 3))
                                lines.append(QLineF(rvx, y+fraction* 4, rvx-rvw*medium, y+fraction* 4)); /*Quarter*/
                                lines.append(QLineF(rvx, y+fraction* 5, rvx-rvw*little, y+fraction* 5))
                                lines.append(QLineF(rvx, y+fraction* 6, rvx-rvw*little, y+fraction* 6))
                                lines.append(QLineF(rvx, y+fraction* 7, rvx-rvw*little, y+fraction* 7))
                                lines.append(QLineF(rvx, y+fraction* 8, rvx-rvw*medium, y+fraction* 8)); /*Half*/
                                lines.append(QLineF(rvx, y+fraction* 9, rvx-rvw*little, y+fraction* 9))
                                lines.append(QLineF(rvx, y+fraction*10, rvx-rvw*little, y+fraction*10))
                                lines.append(QLineF(rvx, y+fraction*11, rvx-rvw*little, y+fraction*11))
                                lines.append(QLineF(rvx, y+fraction*12, rvx-rvw*medium, y+fraction*12)); /*Quarter*/
                                lines.append(QLineF(rvx, y+fraction*13, rvx-rvw*little, y+fraction*13))
                                lines.append(QLineF(rvx, y+fraction*14, rvx-rvw*little, y+fraction*14))
                                lines.append(QLineF(rvx, y+fraction*15, rvx-rvw*little, y+fraction*15))
                            }
                        }
                    }
                }

                painter->drawLines(lines)
                painter->fillRect(QRectF(ox, oy, rvw, rhh), rulerColor)

    # Draw the crosshair
    if (!settings.selectingActive) {
        /*painter->setBrush(Qt::NoBrush);*/
        QPen crosshairPen(QColor::fromRgb(crosshairColor))
        crosshairPen.setCosmetic(1)
        painter->setPen(crosshairPen)
        painter->drawLine(QLineF(mapToScene(viewMousePoint.x(), viewMousePoint.y()-settings.crosshairSize),
                                 mapToScene(viewMousePoint.x(), viewMousePoint.y()+settings.crosshairSize)))
        painter->drawLine(QLineF(mapToScene(viewMousePoint.x()-settings.crosshairSize, viewMousePoint.y()),
                                 mapToScene(viewMousePoint.x()+settings.crosshairSize, viewMousePoint.y())))
        painter->drawRect(QRectF(
            mapToScene(viewMousePoint.x()-settings.selection_pickbox_size,
                viewMousePoint.y()-settings.selection_pickbox_size),
            mapToScene(viewMousePoint.x()+settings.selection_pickbox_size,
                viewMousePoint.y()+settings.selection_pickbox_size)))
    }
        QPixmap p = QPixmap::grabWindow(winId())
        p.save(QString("test.bmp"), "bmp")



int View::willUnderflowInt32(int a, int b):
    int c
    Q_ASSERT(LLONG_MAX>INT_MAX)
    c = (int)a-b
    return (c < INT_MIN || c > INT_MAX)

int View::willOverflowInt32(int a, int b):
    int c
    Q_ASSERT(LLONG_MAX>INT_MAX)
    c = (int)a+b
    return (c < INT_MIN || c > INT_MAX)


QPainterPath View::createRulerTextPath(float x, float y, QString str, float height):
    QPainterPath path

    float xScale = height
    float yScale = height
    float scale[2]
    float pos[2]
    pos[0] = x
    pos[1] = y
    scale[0] = 0.01*height
    scale[1] = 0.01*height

    int len = str.length()
    for (int i = 0; i < len; ++i) {
        if (str[i] == QChar('1')) {
            add_to_path(&path, symbol_list[SYMBOL_one], pos, scale)
        }
        else if(str[i] == QChar('2')) {
            path.moveTo(x+0.00*xScale, y-0.75*yScale)
            path.arcTo(x+0.00*xScale, y-1.00*yScale, 0.50*xScale, 0.50*yScale, 180.00, -216.87)
            path.lineTo(x+0.00*xScale, y-0.00*yScale)
            path.lineTo(x+0.50*xScale, y-0.00*yScale)
        }
        else if(str[i] == QChar('3'))
        {
            path.arcMoveTo(x+0.00*xScale, y-0.50*yScale, 0.50*xScale, 0.50*yScale, 195.00)
            path.arcTo(x+0.00*xScale, y-0.50*yScale, 0.50*xScale, 0.50*yScale, 195.00, 255.00)
            path.arcTo(x+0.00*xScale, y-1.00*yScale, 0.50*xScale, 0.50*yScale, 270.00, 255.00)
        }
        else if(str[i] == QChar('4'))
        {
            path.moveTo(x+0.50*xScale, y-0.00*yScale)
            path.lineTo(x+0.50*xScale, y-1.00*yScale)
            path.lineTo(x+0.00*xScale, y-0.50*yScale)
            path.lineTo(x+0.50*xScale, y-0.50*yScale)
        }
        else if(str[i] == QChar('5'))
        {
            path.moveTo(x+0.50*xScale, y-1.00*yScale)
            path.lineTo(x+0.00*xScale, y-1.00*yScale)
            path.lineTo(x+0.00*xScale, y-0.50*yScale)
            path.lineTo(x+0.25*xScale, y-0.50*yScale)
            path.arcTo(x+0.00*xScale, y-0.50*yScale, 0.50*xScale, 0.50*yScale, 90.00, -180.00)
            path.lineTo(x+0.00*xScale, y-0.00*yScale)
        }
        else if(str[i] == QChar('6'))
        {
            path.addEllipse(QPointF(x+0.25*xScale, y-0.25*yScale), 0.25*xScale, 0.25*yScale)
            path.moveTo(x+0.00*xScale, y-0.25*yScale)
            path.lineTo(x+0.00*xScale, y-0.75*yScale)
            path.arcTo(x+0.00*xScale, y-1.00*yScale, 0.50*xScale, 0.50*yScale, 180.00, -140.00)
        }
        else if(str[i] == QChar('7'))
        {
            path.moveTo(x+0.00*xScale, y-1.00*yScale)
            path.lineTo(x+0.50*xScale, y-1.00*yScale)
            path.lineTo(x+0.25*xScale, y-0.25*yScale)
            path.lineTo(x+0.25*xScale, y-0.00*yScale)
        }
        else if(str[i] == QChar('8'))
        {
            path.addEllipse(QPointF(x+0.25*xScale, y-0.25*yScale), 0.25*xScale, 0.25*yScale)
            path.addEllipse(QPointF(x+0.25*xScale, y-0.75*yScale), 0.25*xScale, 0.25*yScale)
        }
        else if(str[i] == QChar('9'))
        {
            path.addEllipse(QPointF(x+0.25*xScale, y-0.75*yScale), 0.25*xScale, 0.25*yScale)
            path.moveTo(x+0.50*xScale, y-0.75*yScale)
            path.lineTo(x+0.50*xScale, y-0.25*yScale)
            path.arcTo(x+0.00*xScale, y-0.50*yScale, 0.50*xScale, 0.50*yScale, 0.00, -140.00)
        }
        else if(str[i] == QChar('0'))
        {
            /*path.addEllipse(QPointF(x+0.25*xScale, y-0.50*yScale), 0.25*xScale, 0.50*yScale);*/

            path.moveTo(x+0.00*xScale, y-0.75*yScale)
            path.lineTo(x+0.00*xScale, y-0.25*yScale)
            path.arcTo(x+0.00*xScale, y-0.50*yScale, 0.50*xScale, 0.50*yScale, 180.00, 180.00)
            path.lineTo(x+0.50*xScale, y-0.75*yScale)
            path.arcTo(x+0.00*xScale, y-1.00*yScale, 0.50*xScale, 0.50*yScale, 0.00, 180.00)
        }
        else if(str[i] == QChar('-'))
        {
            path.moveTo(x+0.00*xScale, y-0.50*yScale)
            path.lineTo(x+0.50*xScale, y-0.50*yScale)
        }
        else if(str[i] == QChar('\''))
        {
            path.moveTo(x+0.25*xScale, y-1.00*yScale)
            path.lineTo(x+0.25*xScale, y-0.75*yScale)
        }
        else if(str[i] == QChar('\"'))
        {
            path.moveTo(x+0.10*xScale, y-1.00*yScale)
            path.lineTo(x+0.10*xScale, y-0.75*yScale)
            path.moveTo(x+0.40*xScale, y-1.00*yScale)
            path.lineTo(x+0.40*xScale, y-0.75*yScale)
        }

        x += 0.75*xScale
        pos[0] = x
    }

    return path

int View::roundToMultiple(int roundUp, int numToRound, int multiple):
    if(multiple == 0)
        return numToRound
    int remainder = numToRound % multiple
    if(remainder == 0)
        return numToRound

    if(numToRound < 0 && roundUp)
        return numToRound - remainder
    if(roundUp)
        return numToRound + multiple - remainder
    /*else round down*/
    if(numToRound < 0 && !roundUp)
        return numToRound - multiple - remainder
    return numToRound - remainder

def View::updateMouseCoords(int x, int y):
    viewMousePoint = QPoint(x, y)
    sceneMousePoint = to_emb_vector(mapToScene(viewMousePoint))
    gscene->setProperty("SCENE_QSNAP_POINT", to_qpointf(sceneMousePoint)); /*TODO: if qsnap functionality is enabled, use it rather than the mouse point*/
    gscene->setProperty("SCENE_MOUSE_POINT", to_qpointf(sceneMousePoint))
    gscene->setProperty("VIEW_MOUSE_POINT", viewMousePoint)
    mainWin->statusbar->setMouseCoord(sceneMousePoint.x, -sceneMousePoint.y)

def View::setCrossHairSize(unsigned char percent):
    /*NOTE: crosshairSize is in pixels and is a percentage of your screen width*/
    /*NOTE: Example: (1280*0.05)/2 = 32, thus 32 + 1 + 32 = 65 pixel wide crosshair*/
    unsigned int screenWidth = qApp->screens()[0]->geometry().width()
    if(percent > 0 && percent < 100) {
        settings.crosshairSize = (screenWidth*(percent/100.0))/2
    }
    else {
        settings.crosshairSize = screenWidth
    }
}

def View::setCornerButton():
    int num = settings.display_scrollbar_widget_num
    if (num) {
        QPushButton* cornerButton = new QPushButton(this)
        cornerButton->setFlat(1)
        QAction* act = mainWin->actionHash.value(num)
        /*NOTE: Prevent crashing if the action is NULL.*/
        if (!act) {
            QMessageBox::information(this, tr("Corner Widget Error"), tr("There are unused enum values in COMMAND_ACTIONS. Please report this as a bug."))
            setCornerWidget(0)
        }
        else {
            cornerButton->setIcon(act->icon())
            connect(cornerButton, SIGNAL(clicked()), this, SLOT(cornerButtonClicked()))
            setCornerWidget(cornerButton)
            cornerButton->setCursor(Qt::ArrowCursor)
        }
    }
    else {
        setCornerWidget(0)
    }
}

def View::cornerButtonClicked():
    debug_message("Corner Button Clicked.")
    mainWin->actionHash.value(settings.display_scrollbar_widget_num)->trigger()

def View::zoomIn():
    debug_message("View zoomIn()")
    if (!allowZoomIn()) {
        return
    }
    QApplication::setOverrideCursor(Qt::WaitCursor)
    QPointF cntr = mapToScene(QPoint(width()/2,height()/2))
    float s = settings.display_zoomscale_in
    scale(s, s)

    centerOn(cntr)
    QApplication::restoreOverrideCursor()

def View::zoomOut():
    debug_message("View zoomOut()")
    if(!allowZoomOut()) { return; }
    QApplication::setOverrideCursor(Qt::WaitCursor)
    QPointF cntr = mapToScene(QPoint(width()/2,height()/2))
    float s = settings.display_zoomscale_out
    scale(s, s)

    centerOn(cntr)
    QApplication::restoreOverrideCursor()

def View::zoomWindow():
    settings.zoomWindowActive = 1
    settings.selectingActive = 0
    clearSelection()

def View::zoomSelected():
    QApplication::setOverrideCursor(Qt::WaitCursor)
    QList<QGraphicsItem*> itemList = gscene->selectedItems()
    QPainterPath selectedRectPath
    foreach(QGraphicsItem* item, itemList) {
        selectedRectPath.addPolygon(item->mapToScene(item->boundingRect()))
    }
    QRectF selectedRect = selectedRectPath.boundingRect()
    if (selectedRect.isNull()) {
        QMessageBox::information(this, tr("ZoomSelected Preselect"), tr("Preselect objects before invoking the zoomSelected command."))
        /*TODO: Support Post selection of objects*/
    }
    fitInView(selectedRect, Qt::KeepAspectRatio)
    QApplication::restoreOverrideCursor()

def View::zoomExtents():
    QApplication::setOverrideCursor(Qt::WaitCursor)
    QRectF extents = gscene->itemsBoundingRect()
    if (extents.isNull()) {
        extents.setWidth(settings.grid_size.x)
        extents.setHeight(settings.grid_size.y)
        extents.moveCenter(QPointF(0,0))
    }
    fitInView(extents, Qt::KeepAspectRatio)
    QApplication::restoreOverrideCursor()

def View::panRealTime():
    settings.panningRealTimeActive = 1

def View::panPoint():
    settings.panningPointActive = 1

def View::panLeft():
    horizontalScrollBar()->setValue(horizontalScrollBar()->value() + panDistance)
    updateMouseCoords(viewMousePoint.x(), viewMousePoint.y())
    gscene->update()

def View::panRight():
    horizontalScrollBar()->setValue(horizontalScrollBar()->value() - panDistance)
    updateMouseCoords(viewMousePoint.x(), viewMousePoint.y())
    gscene->update()

def View::panUp():
    verticalScrollBar()->setValue(verticalScrollBar()->value() + panDistance)
    updateMouseCoords(viewMousePoint.x(), viewMousePoint.y())
    gscene->update()

def View::panDown():
    verticalScrollBar()->setValue(verticalScrollBar()->value() - panDistance)
    updateMouseCoords(viewMousePoint.x(), viewMousePoint.y())
    gscene->update()

def View::selectAll():
    QPainterPath allPath
    allPath.addRect(gscene->sceneRect())
    gscene->setSelectionArea(allPath, Qt::ReplaceSelection, Qt::IntersectsItemShape, this->transform())

def View::selectionChanged():
    if(mainWin->dockPropEdit->isVisible())
    {
        mainWin->dockPropEdit->setSelectedItems(gscene->selectedItems())
    }
}

def View::mouseDoubleClickEvent(QMouseEvent* event):
    if(event->button() == Qt::LeftButton)
    {
        QGraphicsItem* item = gscene->itemAt(mapToScene(event->pos()), QTransform())
        if(item)
        {
            mainWin->dockPropEdit->show()
        }
    }
}

def View::mousePressEvent(QMouseEvent* event):
    updateMouseCoords(event->x(), event->y())
    if(event->button() == Qt::LeftButton)
    {
        QPainterPath path
        QList<QGraphicsItem*> pickList = gscene->items(QRectF(mapToScene(viewMousePoint.x()-settings.pickBoxSize, viewMousePoint.y()-settings.pickBoxSize),
                                                              mapToScene(viewMousePoint.x()+settings.pickBoxSize, viewMousePoint.y()+settings.pickBoxSize)))

        int itemsInPickBox = pickList.size()
        if(itemsInPickBox && !settings.selectingActive && !settings.grippingActive)
        {
            int itemsAlreadySelected = pickList.at(0)->isSelected()
            if (!itemsAlreadySelected) {
                pickList.at(0)->setSelected(1)
            }
            else {
                int foundGrip = 0
                BaseObject* base = static_cast<BaseObject*>(pickList.at(0)); /*TODO: Allow multiple objects to be gripped at once*/
                if(!base) return

                QPoint qsnapOffset(settings.qsnap_locator_size, settings.qsnap_locator_size)
                QPointF gripPoint = base->mouseSnapPoint(to_qpointf(sceneMousePoint))
                QPoint p1 = mapFromScene(gripPoint) - qsnapOffset
                QPoint q1 = mapFromScene(gripPoint) + qsnapOffset
                QRectF gripRect = QRectF(mapToScene(p1), mapToScene(q1))
                QRectF pickRect = QRectF(mapToScene(viewMousePoint.x()-settings.pickBoxSize, viewMousePoint.y()-settings.pickBoxSize),
                                        mapToScene(viewMousePoint.x()+settings.pickBoxSize, viewMousePoint.y()+settings.pickBoxSize))
                if(gripRect.intersects(pickRect))
                    foundGrip = 1

                /*If the pick point is within the item's grip box, start gripping*/
                if(foundGrip)
                {
                    startGripping(base)
                }
                else /*start moving*/
                {
                    settings.movingActive = 1
                    pressPoint = event->pos()
                    scenePressPoint = mapToScene(pressPoint)
                }
            }
        }
        else if (settings.grippingActive) {
            stopGripping(1)
        }
        else if (!settings.selectingActive) {
            settings.selectingActive = 1
            pressPoint = event->pos()
            scenePressPoint = mapToScene(pressPoint)

            if(!selectBox)
                selectBox = new SelectBox(QRubberBand::Rectangle, this)
            selectBox->setGeometry(QRect(pressPoint, pressPoint))
            selectBox->show()
        }
        else
        {
            settings.selectingActive = 0
            selectBox->hide()
            releasePoint = event->pos()
            sceneReleasePoint = mapToScene(releasePoint)

            /*Start SelectBox Code*/
            path.addPolygon(mapToScene(selectBox->geometry()))
            if(sceneReleasePoint.x() > scenePressPoint.x())
            {
                if (settings.selection_mode_pickadd) {
                    if(mainWin->isShiftPressed())
                    {
                        QList<QGraphicsItem*> itemList = gscene->items(path, Qt::ContainsItemShape)
                        foreach(QGraphicsItem* item, itemList)
                            item->setSelected(0)
                    }
                    else
                    {
                        QList<QGraphicsItem*> itemList = gscene->items(path, Qt::ContainsItemShape)
                        foreach(QGraphicsItem* item, itemList)
                            item->setSelected(1)
                    }
                }
                else {
                    if (mainWin->isShiftPressed()) {
                        QList<QGraphicsItem*> itemList = gscene->items(path, Qt::ContainsItemShape)
                        if(!itemList.size())
                            clearSelection()
                        else {
                            foreach(QGraphicsItem* item, itemList)
                                item->setSelected(!item->isSelected()); /*Toggle selected*/
                        }
                    }
                    else {
                        clearSelection()
                        QList<QGraphicsItem*> itemList = gscene->items(path, Qt::ContainsItemShape)
                        foreach(QGraphicsItem* item, itemList)
                            item->setSelected(1)
                    }
                }
            }
            else {
                if (settings.selection_mode_pickadd) {
                    if(mainWin->isShiftPressed()) {
                        QList<QGraphicsItem*> itemList = gscene->items(path, Qt::IntersectsItemShape)
                        foreach(QGraphicsItem* item, itemList)
                            item->setSelected(0)
                    }
                    else {
                        QList<QGraphicsItem*> itemList = gscene->items(path, Qt::IntersectsItemShape)
                        foreach(QGraphicsItem* item, itemList)
                            item->setSelected(1)
                    }
                }
                else {
                    if (mainWin->isShiftPressed()) {
                        QList<QGraphicsItem*> itemList = gscene->items(path, Qt::IntersectsItemShape)
                        if (!itemList.size()) {
                            clearSelection()
                        }
                        else {
                            foreach(QGraphicsItem* item, itemList)
                                item->setSelected(!item->isSelected()); /*Toggle selected*/
                        }
                    }
                    else
                    {
                        clearSelection()
                        QList<QGraphicsItem*> itemList = gscene->items(path, Qt::IntersectsItemShape)
                        foreach(QGraphicsItem* item, itemList)
                            item->setSelected(1)
            /*End SelectBox Code*/

        if (settings.pastingActive) {
            QList<QGraphicsItem*> itemList = pasteObjectItemGroup->childItems()
            gscene->destroyItemGroup(pasteObjectItemGroup)
            foreach(QGraphicsItem* item, itemList) {
                gscene->removeItem(item); /*Prevent Qt Runtime Warning, QGraphicsScene::addItem: item has already been added to this scene*/
            }

            foreach(QGraphicsItem* item, itemList) {
                BaseObject* base = static_cast<BaseObject*>(item)
                if (base) {

            settings.pastingActive = 0
            settings.selectingActive = 0
        if (settings.zoomWindowActive) {
            fitInView(path.boundingRect(), Qt::KeepAspectRatio)
            clearSelection()

    if (event->button() == Qt::MiddleButton) {
        panStart(event->pos())
        /*The Undo command will record the spot where the pan started.*/
        event->accept()

    gscene->update()

def View::panStart(const QPoint& point):
    recalculateLimits()

    alignScenePointWithViewPoint(mapToScene(point), point)

    settings.panningActive = 1
    panStartX = point.x()
    panStartY = point.y()

def View::recalculateLimits():
    /*NOTE: Increase the sceneRect limits if the point we want to go to lies outside of sceneRect's limits*/
    /*      If the sceneRect limits aren't increased, you cannot pan past its limits*/
    QRectF  viewRect(mapToScene(rect().topLeft()), mapToScene(rect().bottomRight()))
    QRectF  sceneRect(gscene->sceneRect())
    QRectF  newRect = viewRect.adjusted(-viewRect.width(), -viewRect.height(), viewRect.width(), viewRect.height())
    if (!sceneRect.contains(newRect.topLeft()) || !sceneRect.contains(newRect.bottomRight())) {
        gscene->setSceneRect(sceneRect.adjusted(-viewRect.width(),
                                                -viewRect.height(),
                                                viewRect.width(),
                                                viewRect.height()))


def View::centerAt(const QPointF& centerPoint):
    /*centerOn also updates the scrollbars, which shifts things out of wack o_O*/
    centerOn(centerPoint)
    /*Reshift to the new center*/
    QPointF offset = centerPoint - center()
    QPointF newCenter = centerPoint + offset
    centerOn(newCenter)

def View::alignScenePointWithViewPoint(const QPointF& scenePoint, const QPoint& viewPoint):
    QPointF viewCenter = center()
    QPointF pointBefore = scenePoint
    /*centerOn also updates the scrollbars, which shifts things out of wack o_O*/
    centerOn(viewCenter)
    /*Reshift to the new center so the scene and view points align*/
    QPointF pointAfter = mapToScene(viewPoint)
    QPointF offset = pointBefore - pointAfter
    QPointF newCenter = viewCenter + offset
    centerOn(newCenter)

def View::mouseMoveEvent(QMouseEvent* event):
    QPoint mouse = QCursor::pos()
    updateMouseCoords(mouse.x(), mouse.y())
    movePoint = event->pos()
    sceneMovePoint = mapToScene(movePoint)

    if (settings.previewActive) {
        if (previewMode == PREVIEW_MODE_MOVE) {
            previewObjectItemGroup->setPos(to_qpointf(sceneMousePoint) - previewPoint)
        }
        else if (previewMode == PREVIEW_MODE_ROTATE) {
            EmbVector rot, p
            float x = previewPoint.x()
            float y = previewPoint.y()
            float mouseAngle = QLineF(x, y, sceneMousePoint.x, sceneMousePoint.y).angle()

            float rad = radians(previewData-mouseAngle)
            p.x = -x
            p.y = -y
            rot = rotate_vector(p, rad)
            rot.x += x
            rot.y += y

            previewObjectItemGroup->setPos(rot.x, rot.y)
            previewObjectItemGroup->setRotation(previewData-mouseAngle)
        }
        else if (previewMode == PREVIEW_MODE_SCALE) {
            float x = previewPoint.x()
            float y = previewPoint.y()
            float scaleFactor = previewData

            float factor = QLineF(x, y, sceneMousePoint.x, sceneMousePoint.y).length()/scaleFactor

            previewObjectItemGroup->setScale(1)
            previewObjectItemGroup->setPos(0,0)

            if(scaleFactor <= 0.0) {
                QMessageBox::critical(this, QObject::tr("ScaleFactor Error"),
                                    QObject::tr("Hi there. If you are not a developer, report this as a bug. "
  "If you are a developer, your code needs examined, and possibly your head too."))
            }
            else {
                /*Calculate the offset*/
                float oldX = 0
                float oldY = 0
                QLineF scaleLine(x, y, oldX, oldY)
                scaleLine.setLength(scaleLine.length()*factor)
                float newX = scaleLine.x2()
                float newY = scaleLine.y2()

                float dx = newX - oldX
                float dy = newY - oldY

                previewObjectItemGroup->setScale(previewObjectItemGroup->scale()*factor)
                previewObjectItemGroup->moveBy(dx, dy)
            }
        }
    }
    if (settings.pastingActive) {
        EmbVector v
        embVector_subtract(sceneMousePoint, pasteDelta, &v)
        pasteObjectItemGroup->setPos(to_qpointf(v))
    }
    if (settings.movingActive) {
        /*Ensure that the preview is only shown if the mouse has moved.*/
        if (!settings.previewActive) {
            previewOn(PREVIEW_CLONE_SELECTED, PREVIEW_MODE_MOVE, scenePressPoint.x(), scenePressPoint.y(), 0)
        }
    }
    if (settings.selectingActive) {
        if (sceneMovePoint.x() >= scenePressPoint.x()) {
            selectBox->setDirection(1)
        }
        else { selectBox->setDirection(0); }
        selectBox->setGeometry(QRect(mapFromScene(scenePressPoint), event->pos()).normalized())
        event->accept()
    }
    if (settings.panningActive) {
        horizontalScrollBar()->setValue(horizontalScrollBar()->value() - (event->x() - panStartX))
        verticalScrollBar()->setValue(verticalScrollBar()->value() - (event->y() - panStartY))
        panStartX = event->x()
        panStartY = event->y()
        event->accept()
    }
    gscene->update()

def View::mouseReleaseEvent(QMouseEvent* event):
    updateMouseCoords(event->x(), event->y())
    if (event->button() == Qt::LeftButton) {
        if (settings.movingActive) {
            previewOff()
            float dx = sceneMousePoint.x-scenePressPoint.x()
            float dy = sceneMousePoint.y-scenePressPoint.y()
            /*Ensure that moving only happens if the mouse has moved.*/
            if(dx || dy) moveSelected(dx, dy)
            settings.movingActive = 0
        }
        event->accept()
    }
    if (event->button() == Qt::MiddleButton) {
        settings.panningActive = 0
        /*The Undo command will record the spot where the pan completed.*/
        event->accept()
    }
    if (event->button() == Qt::XButton1) {
        debug_message("XButton1")
        main_undo(); /* TODO: Make this customizable */
        event->accept()
    }
    if (event->button() == Qt::XButton2) {
        debug_message("XButton2")
        main_redo(); /* TODO: Make this customizable */
        event->accept()
    }
    gscene->update()

int View::allowZoomIn():
    QPointF origin = mapToScene(0,0)
    QPointF corner = mapToScene(width(), height())
    float maxWidth = corner.x() - origin.x()
    float maxHeight = corner.y() - origin.y()

    float zoomInLimit = 0.0000000001
    if(qMin(maxWidth, maxHeight) < zoomInLimit)
    {
        debug_message("ZoomIn limit reached. (limit=%.10f)", zoomInLimit)
        return 0
    }

    return 1

int View::allowZoomOut():
    QPointF origin = mapToScene(0,0)
    QPointF corner = mapToScene(width(), height())
    float maxWidth = corner.x() - origin.x()
    float maxHeight = corner.y() - origin.y()

    float zoomOutLimit = 10000000000000.0
    if (embMaxDouble(maxWidth, maxHeight) > zoomOutLimit) {
        debug_message("ZoomOut limit reached. (limit=%.1f)", zoomOutLimit)
        return 0

    return 1

def View::wheelEvent(QWheelEvent* event):
    int zoomDir = event->pixelDelta().y(); /* TODO: double check this*/
    QPointF mousePoint = event->globalPos(); /* TODO: this is causing weird versioning errors, this appears to be supported on Qt5.12. */

    updateMouseCoords(mousePoint.x(), mousePoint.y())
    if (zoomDir > 0) {
    else {


def View::zoomToPoint(const QPoint& mousePoint, int zoomDir):
    QPointF pointBeforeScale(mapToScene(mousePoint))

    /*Do The zoom*/
    float s
    if(zoomDir > 0) {
        if(!allowZoomIn()) { return; }
        s = settings.display_zoomscale_in
    }
    else {
        if(!allowZoomOut()) { return; }
        s = settings.display_zoomscale_out
    }

    scale(s, s)
    alignScenePointWithViewPoint(pointBeforeScale, mousePoint)
    recalculateLimits()
    alignScenePointWithViewPoint(pointBeforeScale, mousePoint)

    updateMouseCoords(mousePoint.x(), mousePoint.y())
    if (settings.pastingActive) {
        EmbVector v
        embVector_subtract(sceneMousePoint, pasteDelta, &v)
        pasteObjectItemGroup->setPos(to_qpointf(v))
    }
    if (settings.selectingActive) {
        selectBox->setGeometry(QRect(mapFromScene(scenePressPoint), mousePoint).normalized())
    }
    gscene->update()

def View::contextMenuEvent(QContextMenuEvent* event):
    QString iconTheme = settings.general_icon_theme

    QMenu menu
    QList<QGraphicsItem*> itemList = gscene->selectedItems()
    int selectionEmpty = itemList.isEmpty()

    for (int i = 0; i < itemList.size(); i++) {
        if (itemList.at(i)->data(OBJ_TYPE) != OBJ_TYPE_NULL) {
            selectionEmpty = 0
            break
        }
    }

    if (settings.pastingActive) {
        return
    }
    if (settings.zoomWindowActive) {
        QAction* cancelZoomWinAction = new QAction("&Cancel (ZoomWindow)", this)
        cancelZoomWinAction->setStatusTip("Cancels the ZoomWindow Command.")
        connect(cancelZoomWinAction, SIGNAL(triggered()), this, SLOT(escapePressed()))
        menu.addAction(cancelZoomWinAction)
    }

    menu.addSeparator()
    menu.addAction(mainWin->actionHash.value(ACTION_cut))
    menu.addAction(mainWin->actionHash.value(ACTION_copy))
    menu.addAction(mainWin->actionHash.value(ACTION_paste))
    menu.addSeparator()

    if (!selectionEmpty) {
        QAction* deleteAction = new QAction(loadIcon(erase_xpm), "D&elete", this)
        deleteAction->setStatusTip("Removes objects from a drawing.")
        connect(deleteAction, SIGNAL(triggered()), this, SLOT(deleteSelected()))
        menu.addAction(deleteAction)

        QAction* moveAction = new QAction(loadIcon(move_xpm), "&Move", this)
        moveAction->setStatusTip("Displaces objects a specified distance in a specified direction.")
        connect(moveAction, SIGNAL(triggered()), this, SLOT(moveAction()))
        menu.addAction(moveAction)

        QAction* scaleAction = new QAction(loadIcon(scale_xpm), "Sca&le", this)
        scaleAction->setStatusTip("Enlarges or reduces objects proportionally in the X, Y, and Z directions.")
        connect(scaleAction, SIGNAL(triggered()), this, SLOT(scaleAction()))
        menu.addAction(scaleAction)

        QAction* rotateAction = new QAction(loadIcon(rotate_xpm), "R&otate", this)
        rotateAction->setStatusTip("Rotates objects about a base point.")
        connect(rotateAction, SIGNAL(triggered()), this, SLOT(rotateAction()))
        menu.addAction(rotateAction)

        menu.addSeparator()

        QAction* clearAction = new QAction("Cle&ar Selection", this)
        clearAction->setStatusTip("Removes all objects from the selection set.")
        connect(clearAction, SIGNAL(triggered()), this, SLOT(clearSelection()))
        menu.addAction(clearAction)
    }

    menu.exec(event->globalPos())

def View::deletePressed():
    debug_message("View deletePressed()")
    if (settings.pastingActive) {
        gscene->removeItem(pasteObjectItemGroup)
        delete pasteObjectItemGroup
    }
    settings.pastingActive = 0
    settings.zoomWindowActive = 0
    settings.selectingActive = 0
    selectBox->hide()
    stopGripping(0)
    deleteSelected()

def View::escapePressed():
    debug_message("View escapePressed()")
    if (settings.pastingActive) {
        gscene->removeItem(pasteObjectItemGroup)
        delete pasteObjectItemGroup
    }
    settings.pastingActive = 0
    settings.zoomWindowActive = 0
    settings.selectingActive = 0
    selectBox->hide()
    if(settings.grippingActive) stopGripping(0)
    else clearSelection()

def View::startGripping(BaseObject* obj):
    if(!obj) return
    settings.grippingActive = 1
    gripBaseObj = obj
    sceneGripPoint = gripBaseObj->mouseSnapPoint(to_qpointf(sceneMousePoint))
    gripBaseObj->setObjectRubberPoint("GRIP_POINT", sceneGripPoint)
    gripBaseObj->setObjectRubberMode(OBJ_RUBBER_GRIP)

def View::stopGripping(int accept):
    settings.grippingActive = 0
    if(gripBaseObj)
    {
        gripBaseObj->vulcanize()
        if(accept)
        {
            selectionChanged(); /*Update the Property Editor*/
        }
        gripBaseObj = 0
    }
    /*Move the sceneGripPoint to a place where it will never be hot*/
    sceneGripPoint = sceneRect().topLeft()

def View::clearSelection():
    gscene->clearSelection()

def View::deleteSelected():
    QList<QGraphicsItem*> itemList = gscene->selectedItems()
    int numSelected = itemList.size()
    
    for(int i = 0; i < itemList.size(); i++)
        if(itemList.at(i)->data(OBJ_TYPE) != OBJ_TYPE_NULL)
            BaseObject* base = static_cast<BaseObject*>(itemList.at(i))
            if(base)

def View::cut():
    if(gscene->selectedItems().isEmpty())
        QMessageBox::information(this, tr("Cut Preselect"), tr("Preselect objects before invoking the cut command."))
        return; /*TODO: Prompt to select objects if nothing is preselected*/

    copySelected()
    deleteSelected()

def View::copy():
    if(gscene->selectedItems().isEmpty())
    {
        QMessageBox::information(this, tr("Copy Preselect"), tr("Preselect objects before invoking the copy command."))
        return; /* TODO: Prompt to select objects if nothing is preselected */
    }

    copySelected()
    clearSelection()

def View::copySelected():
    QList<QGraphicsItem*> selectedList = gscene->selectedItems()

    /* Prevent memory leaks by deleting any unpasted instances */
    qDeleteAll(mainWin->cutCopyObjectList.begin(), mainWin->cutCopyObjectList.end())
    mainWin->cutCopyObjectList.clear()

    /*
     * Create new objects but do not add them to the scene just yet.
     * By creating them now, ensures that pasting will still work
     * if the original objects are deleted before the paste occurs.
     */
    mainWin->cutCopyObjectList = createObjectList(selectedList)

def View::paste():
    if (settings.pastingActive) {
        gscene->removeItem(pasteObjectItemGroup)
        delete pasteObjectItemGroup
    }

    pasteObjectItemGroup = gscene->createItemGroup(mainWin->cutCopyObjectList)
    pasteDelta = to_emb_vector(pasteObjectItemGroup->boundingRect().bottomLeft())
    EmbVector v
    embVector_subtract(sceneMousePoint, pasteDelta, &v)
    pasteObjectItemGroup->setPos(to_qpointf(v))
    settings.pastingActive = 1

    /* Re-create the list in case of multiple pastes */
    mainWin->cutCopyObjectList = createObjectList(mainWin->cutCopyObjectList)

QList<QGraphicsItem*> View::createObjectList(QList<QGraphicsItem*> list):
    QList<QGraphicsItem*> copyList

    for (int i = 0; i < list.size(); i++) {
        QGraphicsItem* item = list.at(i)
        if (!item)
            continue

        int objType = item->data(OBJ_TYPE).toInt()

        if (objType == OBJ_TYPE_ARC) {
            ArcObject* arcObj = static_cast<ArcObject*>(item)
            if(arcObj)
            {
                ArcObject* copyArcObj = new ArcObject(arcObj)
                copyList.append(copyArcObj)
            }
        }
        else if(objType == OBJ_TYPE_BLOCK)
        {
            /*TODO: cut/copy blocks*/
        }
        else if(objType == OBJ_TYPE_CIRCLE)
        {
            CircleObject* circObj = static_cast<CircleObject*>(item)
            if(circObj)
            {
                CircleObject* copyCircObj = new CircleObject(circObj)
                copyList.append(copyCircObj)
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
            DimLeaderObject* dimLeaderObj = static_cast<DimLeaderObject*>(item)
            if(dimLeaderObj)
            {
                DimLeaderObject* copyDimLeaderObj = new DimLeaderObject(dimLeaderObj)
                copyList.append(copyDimLeaderObj)
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
            EllipseObject* elipObj = static_cast<EllipseObject*>(item)
            if(elipObj)
            {
                EllipseObject* copyElipObj = new EllipseObject(elipObj)
                copyList.append(copyElipObj)
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
            LineObject* lineObj = static_cast<LineObject*>(item)
            if(lineObj)
            {
                LineObject* copyLineObj = new LineObject(lineObj)
                copyList.append(copyLineObj)
            }
        }
        else if(objType == OBJ_TYPE_PATH)
        {
            PathObject* pathObj = static_cast<PathObject*>(item)
            if(pathObj)
            {
                PathObject* copyPathObj = new PathObject(pathObj)
                copyList.append(copyPathObj)
            }
        }
        else if(objType == OBJ_TYPE_POINT)
        {
            PointObject* pointObj = static_cast<PointObject*>(item)
            if(pointObj)
            {
                PointObject* copyPointObj = new PointObject(pointObj)
                copyList.append(copyPointObj)
            }
        }
        else if(objType == OBJ_TYPE_POLYGON)
        {
            PolygonObject* pgonObj = static_cast<PolygonObject*>(item)
            if(pgonObj)
            {
                PolygonObject* copyPgonObj = new PolygonObject(pgonObj)
                copyList.append(copyPgonObj)
            }
        }
        else if(objType == OBJ_TYPE_POLYLINE)
        {
            PolylineObject* plineObj = static_cast<PolylineObject*>(item)
            if(plineObj)
            {
                PolylineObject* copyPlineObj = new PolylineObject(plineObj)
                copyList.append(copyPlineObj)
            }
        }
        else if(objType == OBJ_TYPE_RAY)
        {
            /*TODO: cut/copy rays*/
        }
        else if(objType == OBJ_TYPE_RECTANGLE)
        {
            RectObject* rectObj = static_cast<RectObject*>(item)
            if(rectObj)
            {
                RectObject* copyRectObj = new RectObject(rectObj)
                copyList.append(copyRectObj)
            }
        }
        else if(objType == OBJ_TYPE_TEXTSINGLE)
        {
            TextSingleObject* textObj = static_cast<TextSingleObject*>(item)
            if(textObj)
            {
                TextSingleObject* copyTextObj = new TextSingleObject(textObj)
                copyList.append(copyTextObj)
            }
        }
    }

    return copyList

def View::repeatAction():
}

def View::moveAction():
}

def View::moveSelected(float dx, float dy):
    QList<QGraphicsItem*> itemList = gscene->selectedItems()
    int numSelected = itemList.size()
    
    foreach(QGraphicsItem* item, itemList)
    {
        BaseObject* base = static_cast<BaseObject*>(item)
        if(base)
        {
        }
    }

    /*Always clear the selection after a move*/
    gscene->clearSelection()

def View::rotateAction():
}

def View::rotateSelected(float x, float y, float rot):
    QList<QGraphicsItem*> itemList = gscene->selectedItems()
    int numSelected = itemList.size()
    foreach(QGraphicsItem* item, itemList)
    {
        BaseObject* base = static_cast<BaseObject*>(item)
        if(base)
        {
        }
    }

    /*Always clear the selection after a rotate*/
    gscene->clearSelection()

def View::mirrorSelected(float x1, float y1, float x2, float y2):
    QList<QGraphicsItem*> itemList = gscene->selectedItems()
    int numSelected = itemList.size()
    foreach(QGraphicsItem* item, itemList)
    {
        BaseObject* base = static_cast<BaseObject*>(item)
        if(base)
        {
        }
    }

    /*Always clear the selection after a mirror*/
    gscene->clearSelection()

def View::scaleAction():
}

def View::scaleSelected(float x, float y, float factor):
    QList<QGraphicsItem*> itemList = gscene->selectedItems()
    int numSelected = itemList.size()
    for item in itemList:
        BaseObject* base = static_cast<BaseObject*>(item)
        if base:

    /*Always clear the selection after a scale*/
    gscene->clearSelection()

int View::numSelected():
    return gscene->selectedItems().size()

def View::showScrollBars(int val):
    if(val)
        setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOn)
        setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOn)
    else
        setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff)
        setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff)

def View::setCrossHairColor(unsigned int color):
    crosshairColor = color
    gscene->setProperty("VIEW_COLOR_CROSSHAIR", color)
    if(gscene) gscene->update()

def View::setBackgroundColor(unsigned int color):
    setBackgroundBrush(QColor(color))
    gscene->setProperty("VIEW_COLOR_BACKGROUND", color)
    if(gscene) gscene->update()

def View::setSelectBoxColors(unsigned int colorL, unsigned int fillL, unsigned int colorR, unsigned int fillR, int alpha):
    selectBox->setColors(QColor(colorL), QColor(fillL), QColor(colorR), QColor(fillR), alpha)

