#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENSE for licensing terms.

    ------------------------------------------------------------

    Classes for geometry objects.
    
    One class per object. There needs to be a class for every
    object type that is part of the SVG spec that we support.
"""

import math
import libembroidery

class Vector():
    def __init__(self, x, y):
        self.x = 0.0
        self.y = 0.0
        return self

def unit_vector(angle):
    r"""
    Unit vector in the direction defined by angle, measured
    anti-clockwise from the x axis.
    """
    x = math.cos(angle)
    y = math.sin(angle)
    return Vector(x, y)

class Base_Object():
    r"""
    BaseObject(QGraphicsItem* parent = 0)
    ~BaseObject()

    enum  Type = OBJ_TYPE_BASE ]
    int type() const  return Type

    QPen objectPen()   const  return objPen
    QColor   objectColor() const  return objPen.color()
    unsigned int objectColorRGB()  const  return objPen.color().rgb()
    Qt::PenStyle objectLineType()  const  return objPen.style()
       objectLineWeight()    const  return lwtPen.widthF()
    QPainterPath objectPath()  const  return path()
    int  objectRubberMode()    const  return objRubberMode
     objectRubberPoint(const QString& key) const
    QString  objectRubberText(const QString& key) const
    """
    def __init__(self):
        self.color = "#FFFFFF"
        self.lineType = "solid"
        self.lineWeight = 1.0
        return self

    QRectF rect() const  return path().boundingRect()
    def setRect(const QRectF& r)  QPainterPath p; p.addRect(r); setPath(p)
    def setRect(x, y, w, h)  QPainterPath p; p.addRect(x,y,w,h); setPath(p)
    QLineF line() const  return objLine
    def setLine(const QLineF& li)  QPainterPath p; p.moveTo(li.p1()); p.lineTo(li.p2()); setPath(p); objLine = li
    def setLine(x1, y1, x2, y2)  QPainterPath p; p.moveTo(x1,y1); p.lineTo(x2,y2); setPath(p); objLine.setLine(x1,y1,x2,y2)

    def setObjectPath(const QPainterPath& p)  setPath(p)
    def setObjectRubberMode(int mode)  objRubberMode = mode
    def setObjectRubberPoint(const QString& key, const QPointF& point)  objRubberPoints.insert(key, point)
    def setObjectRubberText(const QString& key, const QString& txt)  objRubberTexts.insert(key, txt)

    QRectF boundingRect() const
    QPainterPath shape() const  return path()

    def drawRubberLine(const QLineF& rubLine, QPainter* painter = 0, const char* colorFromScene = 0)

    def vulcanize() = 0
    mouseSnapPoint(const QPointF& mousePoint) = 0
    QList<QPointF> allGripPoints() = 0
    def gripEdit(const QPointF& before, const QPointF& after) = 0
    
    QPen objPen
    QPen lwtPen
    QLineF objLine
    int objRubberMode
    QHash<QString, QPointF> objRubberPoints
    QHash<QString, QString> objRubberTexts
    int objID
protected:
    QPen lineWeightPen() const  return lwtPen
    def realRender(QPainter* painter, const QPainterPath& renderPath)
]

class Arc(Base_Object):
    r"""
public:
    ArcObject(startX, startY, midX, midY, endX, endY, unsigned int rgb, QGraphicsItem* parent = 0)
    ArcObject(ArcObject* obj, QGraphicsItem* parent = 0)
    ~ArcObject()

    enum  Type = OBJ_TYPE_ARC ]
    int type() const  return Type

    objectCenter()    const  return scenePos()
      objectRadius()    const  return rect().width()/2.0*scale()
      objectStartAngle()    const
      objectEndAngle()  const
    objectStartPoint()    const
    objectMidPoint()  const
    objectEndPoint()  const
      objectArea()  const
      objectArcLength() const
      objectChord() const
      objectIncludedAngle() const
    int    objectClockwise() const
    """
    def __init__(self):
        super.__init__(self)
        self.start = Vector(0.0, 0.0)
        self.middle = Vector(0.0, 0.0)
        self.end = Vector(0.0, 0.0)
        return self

    def setObjectRadius(radius)
        return

    def setObjectStartAngle(angle)
        return

    def setObjectEndAngle(angle)
        return

    def setObjectStartPoint(pointX, pointY)
        return

    def setObjectMidPoint(const QPointF& point)
        return

    def setObjectMidPoint(pointX, pointY)
        return

    def setObjectEndPoint(const QPointF& point)
        return

    def setObjectEndPoint(pointX, pointY)
        return

    def updateRubber(QPainter* painter = 0):
        return

    def vulcanize():
        return

    mouseSnapPoint(const QPointF& mousePoint)
    QList<QPointF> allGripPoints()
    def gripEdit(const QPointF& before, const QPointF& after)
protected:
    def paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    def init(startX, startY, midX, midY, endX, endY, unsigned int rgb, Qt::PenStyle lineType)
    def updatePath()

    def calculateArcData(startX, startY, midX, midY, endX, endY)
    def updateArcRect(radius)


class Circle():
    def __init__(self):
        return self

public:
    CircleObject(centerX, centerY, radius, unsigned int rgb, QGraphicsItem* parent = 0)
    CircleObject(CircleObject* obj, QGraphicsItem* parent = 0)
    ~CircleObject()

    enum  Type = OBJ_TYPE_CIRCLE ]
    int type() const  return Type

    QPainterPath objectSavePath() const

    objectCenter()    const  return scenePos()
      objectRadius()    const  return rect().width()/2.0*scale()
      objectDiameter()  const  return rect().width()*scale()
      objectArea()  const  return embConstantPi*objectRadius()*objectRadius()
      objectCircumference() const  return embConstantPi*objectDiameter()
    objectQuadrant0() const  return objectCenter() + QPointF(objectRadius(), 0)
    objectQuadrant90()    const  return objectCenter() + QPointF(0,-objectRadius())
    objectQuadrant180()   const  return objectCenter() + QPointF(-objectRadius(),0)
    objectQuadrant270()   const  return objectCenter() + QPointF(0, objectRadius())

    def setObjectRadius(radius)
    def setObjectDiameter(diameter)
    def setObjectArea(area)
    def setObjectCircumference(circumference)

    def updateRubber(QPainter* painter = 0)
    def vulcanize()
    mouseSnapPoint(const QPointF& mousePoint)
    QList<QPointF> allGripPoints()
    def gripEdit(const QPointF& before, const QPointF& after)
protected:
    def paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    def init(centerX, centerY, radius, unsigned int rgb, Qt::PenStyle lineType)
    def updatePath()
]

class DimLeaderObject(Base_Object):
    def __init__(self):
        super().__init__()
        return self

public:
    DimLeaderObject(x1, y1, x2, y2, unsigned int rgb, QGraphicsItem* parent = 0)
    DimLeaderObject(DimLeaderObject* obj, QGraphicsItem* parent = 0)
    ~DimLeaderObject()

    # NOTE: Allow this enum to evaluate false.
    ArrowStyle = ["NoArrow", "Open", "Closed", "Dot", "Box", "Tick"]
    # NOTE: Allow this enum to evaluate false.
    lineStyle = ["NoLine", "Flared", "Fletching"]

    enum  Type = OBJ_TYPE_DIMLEADER ]
    int type() const  return Type

    objectEndPoint1() const
    objectEndPoint2() const
    objectMidPoint()  const
      objectX1()    const  return objectEndPoint1().x()
      objectY1()    const  return objectEndPoint1().y()
      objectX2()    const  return objectEndPoint2().x()
      objectY2()    const  return objectEndPoint2().y()
      objectDeltaX()    const  return (objectEndPoint2().x() - objectEndPoint1().x())
      objectDeltaY()    const  return (objectEndPoint2().y() - objectEndPoint1().y())
      objectAngle() const
      objectLength()    const  return line().length()

    def setObjectEndPoint1(EmbVector v)
    def setObjectEndPoint2(EmbVector v)

    def updateRubber(QPainter* painter = 0)
    def vulcanize()
    mouseSnapPoint(const QPointF& mousePoint)
    QList<QPointF> allGripPoints()
    def gripEdit(const QPointF& before, const QPointF& after)
protected:
    def paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    def init(x1, y1, x2, y2, unsigned int rgb, Qt::PenStyle lineType)

    int curved
    int filled
    def updateLeader()
    QPainterPath lineStylePath
    QPainterPath arrowStylePath
    arrowStyleAngle
    arrowStyleLength
    lineStyleAngle
    lineStyleLength
]

class EllipseObject : public BaseObject:
public:
    EllipseObject(centerX, centerY, width, height, unsigned int rgb, QGraphicsItem* parent = 0)
    EllipseObject(EllipseObject* obj, QGraphicsItem* parent = 0)
    ~EllipseObject()

    enum  Type = OBJ_TYPE_ELLIPSE ]
    int type() const  return Type

    QPainterPath objectSavePath() const

    objectCenter() const  return scenePos()
      objectRadiusMajor()   const  return qMax(rect().width(), rect().height())/2.0*scale()
      objectRadiusMinor()   const  return qMin(rect().width(), rect().height())/2.0*scale()
      objectDiameterMajor() const  return qMax(rect().width(), rect().height())*scale()
      objectDiameterMinor() const  return qMin(rect().width(), rect().height())*scale()
      objectWidth() const  return rect().width()*scale()
      objectHeight()    const  return rect().height()*scale()
    objectQuadrant0() const
    objectQuadrant90()    const
    objectQuadrant180()   const
    objectQuadrant270()   const

    def setObjectSize(width, height)
    def setObjectRadiusMajor(radius)
    def setObjectRadiusMinor(radius)
    def setObjectDiameterMajor(diameter)
    def setObjectDiameterMinor(diameter)

    def updateRubber(QPainter* painter = 0)
    def vulcanize()
    mouseSnapPoint(const QPointF& mousePoint)
    QList<QPointF> allGripPoints()
    def gripEdit(const QPointF& before, const QPointF& after)
protected:
    def paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    def init(centerX, centerY, width, height, unsigned int rgb, Qt::PenStyle lineType)
    def updatePath()
]

class ImageObject : public BaseObject:
public:
    ImageObject(x, y, w, h, unsigned int rgb, QGraphicsItem* parent = 0)
    ImageObject(ImageObject* obj, QGraphicsItem* parent = 0)
    ~ImageObject()

    enum  Type = OBJ_TYPE_IMAGE ]
    int type() const  return Type

    objectTopLeft() const
    objectTopRight()    const
    objectBottomLeft()  const
    objectBottomRight() const
      objectWidth()   const  return rect().width()*scale()
      objectHeight()  const  return rect().height()*scale()
      objectArea()    const  return qAbs(objectWidth()*objectHeight())

    def setObjectRect(x, y, w, h)

    def updateRubber(QPainter* painter = 0)
    def vulcanize()
    mouseSnapPoint(const QPointF& mousePoint)
    QList<QPointF> allGripPoints()
    def gripEdit(const QPointF& before, const QPointF& after)
protected:
    def paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    def init(x, y, w, h, unsigned int rgb, Qt::PenStyle lineType)
    def updatePath()
]


class LineObject : public BaseObject:
public:
    LineObject(x1, y1, x2, y2, unsigned int rgb, QGraphicsItem* parent = 0)
    LineObject(LineObject* obj, QGraphicsItem* parent = 0)
    ~LineObject()

    enum  Type = OBJ_TYPE_LINE ]
    int type() const  return Type

    QPainterPath objectSavePath() const

    objectEndPoint1() const  return scenePos()
    objectEndPoint2() const
    objectMidPoint()  const
      objectX1()    const  return objectEndPoint1().x()
      objectY1()    const  return objectEndPoint1().y()
      objectX2()    const  return objectEndPoint2().x()
      objectY2()    const  return objectEndPoint2().y()
      objectDeltaX()    const  return (objectEndPoint2().x() - objectEndPoint1().x())
      objectDeltaY()    const  return (objectEndPoint2().y() - objectEndPoint1().y())
      objectAngle() const
      objectLength()    const  return line().length()*scale()

    def setObjectEndPoint1(const QPointF& endPt1)
    def setObjectEndPoint1(x1, y1)
    def setObjectEndPoint2(const QPointF& endPt2)
    def setObjectEndPoint2(x2, y2)
    def setObjectX1(x)  setObjectEndPoint1(x, objectEndPoint1().y())
    def setObjectY1(y)  setObjectEndPoint1(objectEndPoint1().x(), y)
    def setObjectX2(x)  setObjectEndPoint2(x, objectEndPoint2().y())
    def setObjectY2(y)  setObjectEndPoint2(objectEndPoint2().x(), y)

    def updateRubber(QPainter* painter = 0)
    def vulcanize()
    mouseSnapPoint(const QPointF& mousePoint)
    QList<QPointF> allGripPoints()
    def gripEdit(const QPointF& before, const QPointF& after)
protected:
    def paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    def init(x1, y1, x2, y2, unsigned int rgb, Qt::PenStyle lineType)
]

class PathObject : public BaseObject:
public:
    PathObject(x, y, const QPainterPath p, unsigned int rgb, QGraphicsItem* parent = 0)
    PathObject(PathObject* obj, QGraphicsItem* parent = 0)
    ~PathObject()

    enum  Type = OBJ_TYPE_PATH ]
    int type() const  return Type

    QPainterPath objectCopyPath() const
    QPainterPath objectSavePath() const

    objectPos() const  return scenePos()
      objectX()   const  return scenePos().x()
      objectY()   const  return scenePos().y()

    def setObjectPos(const QPointF& point)  setPos(point.x(), point.y())
        return

    def setObjectPos(x, y)  setPos(x, y)
        return

    def setObjectX(x)  setObjectPos(x, objectY())
        return

    def setObjectY(y)  setObjectPos(objectX(), y)
        return

    def updateRubber(QPainter* painter = 0)
        return

    def vulcanize()
        return

    mouseSnapPoint(const QPointF& mousePoint)
        return

    QList<QPointF> allGripPoints()
    def gripEdit(const QPointF& before, const QPointF& after)
protected:
    def paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    def init(x, y, const QPainterPath& p, unsigned int rgb, Qt::PenStyle lineType)
    def updatePath(const QPainterPath& p)
    QPainterPath normalPath
    /*TODO: make paths similar to polylines. Review and implement any missing functions/members.*/
]

class PointObject : public BaseObject:
public:
    PointObject(x, y, unsigned int rgb, QGraphicsItem* parent = 0)
    PointObject(PointObject* obj, QGraphicsItem* parent = 0)
    ~PointObject()

    enum  Type = OBJ_TYPE_POINT ]
    int type() const  return Type

    QPainterPath objectSavePath() const

    objectPos() const  return scenePos()
      objectX()   const  return scenePos().x()
      objectY()   const  return scenePos().y()

    def setObjectPos(const QPointF& point)  setPos(point.x(), point.y())
    def setObjectPos(x, y)  setPos(x, y)
    def setObjectX(x)  setObjectPos(x, objectY())
    def setObjectY(y)  setObjectPos(objectX(), y)

    def updateRubber(QPainter* painter = 0)
    def vulcanize()
    mouseSnapPoint(const QPointF& mousePoint)
    QList<QPointF> allGripPoints()
    def gripEdit(const QPointF& before, const QPointF& after)
protected:
    def paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    def init(x, y, unsigned int rgb, Qt::PenStyle lineType)
]


class PolygonObject : public BaseObject:
public:
    PolygonObject(x, y, const QPainterPath& p, unsigned int rgb, QGraphicsItem* parent = 0)
    PolygonObject(PolygonObject* obj, QGraphicsItem* parent = 0)
    ~PolygonObject()

    enum  Type = OBJ_TYPE_POLYGON ]
    int type() const  return Type

    QPainterPath objectCopyPath() const
    QPainterPath objectSavePath() const

    def objectPos(self):
        return scenePos()

    def objectX(self):
        return self.scenePos().x

    def objectY(self):
        return self.scenePos().y

    def setObjectPos(const QPointF& point)  setPos(point.x(), point.y())
    def setObjectPos(x, y)  setPos(x, y)
    def setObjectX(x)  setObjectPos(x, objectY())
    def setObjectY(y)  setObjectPos(objectX(), y)

    def updateRubber(QPainter* painter = 0)
    def vulcanize()
    mouseSnapPoint(const QPointF& mousePoint)
    QList<QPointF> allGripPoints()
    def gripEdit(const QPointF& before, const QPointF& after)
protected:
    def paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    def init(x, y, const QPainterPath& p, unsigned int rgb, Qt::PenStyle lineType)
    def updatePath(const QPainterPath& p)
    QPainterPath normalPath
    int findIndex(const QPointF& point)
    int gripIndex


class PolylineObject():
    r""" : public BaseObject:
public:
    PolylineObject(x, y, const QPainterPath& p, unsigned int rgb, QGraphicsItem* parent = 0)
    PolylineObject(PolylineObject* obj, QGraphicsItem* parent = 0)
    ~PolylineObject()

    enum  Type = OBJ_TYPE_POLYLINE ]
    int type() const  return Type

    QPainterPath objectCopyPath() const
    QPainterPath objectSavePath() const

    objectPos() const  return scenePos()
      objectX()   const  return scenePos().x()
      objectY()   const  return scenePos().y()

    def set_pos_by_point(point):
        self.x = point.x
        self.y = point.y

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def updateRubber(QPainter* painter = 0):
        return

    def vulcanize()
        return

    mouseSnapPoint(const QPointF& mousePoint)
        return

    QList<QPointF> allGripPoints()
        return

    def gripEdit(const QPointF& before, const QPointF& after)
protected:
        return

    def paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
        return

    def init(x, y, const QPainterPath& p, unsigned int rgb, Qt::PenStyle lineType)
        return

    def updatePath(const QPainterPath& p)
        return

    QPainterPath normalPath
    int findIndex(const QPointF& point)
    int gripIndex
]
    """
    def __init__(self):
        return self

class Rect():
    r""" : public BaseObject:
public:
    RectObject(x, y, w, h, unsigned int rgb, QGraphicsItem* parent = 0)
    RectObject(RectObject* obj, QGraphicsItem* parent = 0)
    ~RectObject()

    enum  Type = OBJ_TYPE_RECTANGLE ]
    int type() const  return Type

    QPainterPath objectSavePath() const

    objectPos() const  return scenePos()

    objectTopLeft() const
    objectTopRight()    const
    objectBottomLeft()  const
    objectBottomRight() const
      objectWidth()   const  return rect().width()*scale()
      objectHeight()  const  return rect().height()*scale()
      objectArea()    const  return qAbs(objectWidth()*objectHeight())

    def setObjectRect(x, y, w, h)

    def updateRubber(QPainter* painter = 0)
    def vulcanize()
    mouseSnapPoint(const QPointF& mousePoint)
    QList<QPointF> allGripPoints()
    def gripEdit(const QPointF& before, const QPointF& after)
protected:
    def paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    def init(x, y, w, h, unsigned int rgb, Qt::PenStyle lineType)
    def updatePath()
]
    """
    def __init__(self):
        return self


class TextSingle():
    """
public:
    TextSingleObject(const QString& str, x, y, unsigned int rgb, QGraphicsItem* parent = 0)
    TextSingleObject(TextSingleObject* obj, QGraphicsItem* parent = 0)
    ~TextSingleObject()

    enum  Type = OBJ_TYPE_TEXTSINGLE ]
    int type() const  return Type

    QList<QPainterPath> objectSavePathList() const  return subPathList()
    QList<QPainterPath> subPathList() const

    objectPos()    const  return scenePos()
      objectX()  const  return scenePos().x()
      objectY()  const  return scenePos().y()

    QStringList objectTextJustifyList() const

    def setObjectText(const QString& str)
    def setObjectTextFont(const QString& font)
    def setObjectTextJustify(const QString& justify)
    def setObjectTextSize(size)
    def setObjectTextStyle(int bold, int italic, int under, int strike, int over)
    def setObjectTextBold(val):
        return

    def setObjectTextItalic(int val):
        return

    def setObjectTextUnderline(int val):
        return

    def setObjectTextStrikeOut(int val):
        return

    def setObjectTextOverline(int val):
        return

    def setObjectTextBackward(int val):
        return

    def setObjectTextUpsideDown(int val):
        return

    def setObjectPos(const QPointF& point)  setPos(point.x(), point.y())
    def setObjectPos(x, y)  setPos(x, y)
    def setObjectX(x)  setObjectPos(x, objectY())
    def setObjectY(y)  setObjectPos(objectX(), y)

    def updateRubber(QPainter* painter = 0)
    def vulcanize()
    mouseSnapPoint(const QPointF& mousePoint)
    QList<QPointF> allGripPoints()
    def gripEdit(const QPointF& before, const QPointF& after)

    QString objText
    QString objTextFont
    QString objTextJustify
    text_properties obj_text
    QPainterPath objTextPath
protected:
    def paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    def init(const QString& str, x, y, unsigned int rgb, Qt::PenStyle lineType)
    """

    def __init__(self):
        return self


class Arc():
    r"""
    """
    def __init__(self):
        return self

    ArcObject(startX, startY, midX, midY, endX, endY, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
        debug_message("ArcObject Constructor()")
        init(startX, startY, midX, midY, endX, endY, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
    }

    ArcObject(ArcObject* obj, QGraphicsItem* parent) : BaseObject(parent):
        debug_message("ArcObject Constructor()")
        if obj)

            init(obj.objectStartPoint().x(), obj.objectStartPoint().y(), obj.objectMidPoint().x(), obj.objectMidPoint().y(), obj.objectEndPoint().x(), obj.objectEndPoint().y(), obj.objectColorRGB(), Qt::SolidLine)
            /* TODO: getCurrentLineType */
            setRotation(obj.rotation())

    def init(startX, startY, midX, midY, endX, endY, unsigned int rgb, Qt::PenStyle lineType):
        setData(OBJ_TYPE, type())
        setData(OBJ_NAME, obj_names[OBJ_TYPE_ARC])

        setFlag(QGraphicsItem::ItemIsSelectable, 1)

        calculateArcData(startX, startY, midX, midY, endX, endY)

        setObjectColor(rgb)
        setObjectLineType(lineType)
        setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
        setPen(objPen)

    def calculateArcData(startX, startY, midX, midY, endX, endY):
        EmbArc arc = embArcObject_make(startX, startY,
                    midX, midY,
                    endX, endY).arc
        EmbVector center
        getArcCenter(arc, &center)
        arcStartPoint = QPointF(startX - center.x, startY - center.y)
        arcMidPoint = QPointF(midX   - center.x, midY   - center.y)
        arcEndPoint = QPointF(endX   - center.x, endY   - center.y)

        setPos(center.x, center.y)

        radius = QLineF(center.x, center.y, midX, midY).length()
        updateArcRect(radius)
        updatePath()
        setRotation(0)
        setScale(1)

    def updateArcRect(radius):
        QRectF arcRect
        arcRect.setWidth(radius*2.0)
        arcRect.setHeight(radius*2.0)
        arcRect.moveCenter(QPointF(0,0))
        setRect(arcRect)

    def setObjectRadius(radius):
        if radius <= 0:
            radius = 0.0000001

        center = scenePos()
        QLineF startLine = QLineF(center, objectStartPoint())
        QLineF midLine = QLineF(center, objectMidPoint())
        QLineF endLine = QLineF(center, objectEndPoint())
        startLine.setLength(radius)
        midLine.setLength(radius)
        endLine.setLength(radius)
        arcStartPoint = startLine.p2()
        arcMidPoint = midLine.p2()
        arcEndPoint = endLine.p2()

        calculateArcData(arcStartPoint.x(), arcStartPoint.y(), arcMidPoint.x(), arcMidPoint.y(), arcEndPoint.x(), arcEndPoint.y())

    def setObjectStartAngle(angle):
        "TODO: ArcObject setObjectStartAngle"

    def setObjectEndAngle(angle):
        "TODO: ArcObject setObjectEndAngle"

    def setObjectStartPoint(pointX, pointY):
        calculateArcData(pointX, pointY, arcMidPoint.x(), arcMidPoint.y(), arcEndPoint.x(), arcEndPoint.y())

    def setObjectMidPoint(const QPointF& point):
        setObjectMidPoint(point.x(), point.y())

    def setObjectMidPoint(pointX, pointY):
        calculateArcData(arcStartPoint.x(), arcStartPoint.y(), pointX, pointY, arcEndPoint.x(), arcEndPoint.y())

    def setObjectEndPoint(const QPointF& point):
        setObjectEndPoint(point.x(), point.y())

    def setObjectEndPoint(pointX, pointY):
        calculateArcData(arcStartPoint.x(), arcStartPoint.y(), arcMidPoint.x(), arcMidPoint.y(), pointX, pointY)

    objectStartAngle()
        angle = QLineF(scenePos(), objectStartPoint()).angle()
        return fmod(angle, 360.0)

    objectEndAngle()
        angle = QLineF(scenePos(), objectEndPoint()).angle()
        return fmod(angle, 360.0)

    objectStartPoint()
        EmbVector v = to_emb_vector(arcStartPoint)
        EmbVector rot = scale_and_rotate(v, scale(), radians(rotation()))

        return scenePos() + to_qpointf(rot)

    objectMidPoint()
        EmbVector v = to_emb_vector(arcMidPoint)
        EmbVector rot = scale_and_rotate(v, scale(), radians(rotation()))

        return scenePos() + to_qpointf(rot)

    objectEndPoint()
        EmbVector v = to_emb_vector(arcEndPoint)
        EmbVector rot = scale_and_rotate(v, scale(), radians(rotation()))

        return scenePos() + to_qpointf(rot)

    def objectArea():
        /*Area of a circular segment*/
        r = objectRadius()
        theta = radians(objectIncludedAngle())
        return ((r*r)/2)*(theta - sin(theta))

    def objectArcLength():
        return radians(objectIncludedAngle())*objectRadius()

    def objectChord():
        return QLineF(objectStartPoint().x(), objectStartPoint().y(), objectEndPoint().x(), objectEndPoint().y()).length()

    def objectIncludedAngle():
        chord = objectChord()
        rad = objectRadius()
        if chord <= 0 || rad <= 0) return 0
        /* Prevents division by zero and non-existent circles */

        /* NOTE:
        * Due to floating point rounding errors, we need to clamp the
        * quotient so it is in the range [-1, 1].
        * If the quotient is out of that range, then the result of asin()
        * will be NaN.
        */
        quotient = chord/(2.0*rad)
        if quotient > 1.0) quotient = 1.0
        if quotient < 0.0) quotient = 0.0
        /* NOTE: 0 rather than -1 since we are enforcing a positive chord
        * and radius.
        */
        return degrees(2.0*asin(quotient))
        /* Properties of a Circle - Get the Included Angle - Reference: ASD9 */
    }

    def objectClockwise():
        EmbVector start = to_emb_vector(objectStartPoint())
        EmbVector mid = to_emb_vector(objectMidPoint())
        EmbVector end = to_emb_vector(objectEndPoint())
        EmbArc arc = embArcObject_make(start.x, -start.y, mid.x, -mid.y, end.x, -end.y).arc
        /* NOTE: Y values are inverted here on purpose */
        return isArcClockwise(arc)

    def updatePath():
        startAngle = (objectStartAngle() + rotation())
        spanAngle = objectIncludedAngle()

        if objectClockwise())
            spanAngle = -spanAngle

        QPainterPath path
        path.arcMoveTo(rect(), startAngle)
        path.arcTo(rect(), startAngle, spanAngle)
        /*NOTE: Reverse the path so that the inside area isn't considered part of the arc*/
        path.arcTo(rect(), startAngle+spanAngle, -spanAngle)
        setObjectPath(path)

    def paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
        QGraphicsScene* objScene = scene()
        if !objScene) return

        QPen paintPen = pen()
        painter.setPen(paintPen)
        updateRubber(painter)
        if option.state & QStyle::State_Selected)   paintPen.setStyle(Qt::DashLine)
        if objScene.property("ENABLE_LWT").toBool())  paintPen = lineWeightPen()
        painter.setPen(paintPen)

        startAngle = (objectStartAngle() + rotation())*16
        spanAngle = objectIncludedAngle()*16

        if objectClockwise())
            spanAngle = -spanAngle

        rad = objectRadius()
        QRectF paintRect(-rad, -rad, rad*2.0, rad*2.0)
        painter.drawArc(paintRect, startAngle, spanAngle)

    def updateRubber(QPainter* painter):
        /*TODO: Arc Rubber Modes*/

        /*TODO: updateRubber() gripping for ArcObject*/

    }

    def vulcanize():
        debug_message("ArcObject vulcanize()")
        updateRubber()

        setObjectRubberMode(OBJ_RUBBER_OFF)

    def mouseSnapPoint(const QPointF& mousePoint):
        " Returns the closest snap point to the mouse point. "
        center = objectCenter()
        start = objectStartPoint()
        mid = objectMidPoint()
        end = objectEndPoint()

        cntrDist = QLineF(mousePoint, center).length()
        startDist = QLineF(mousePoint, start).length()
        midDist = QLineF(mousePoint, mid).length()
        endDist = QLineF(mousePoint, end).length()

        minDist = qMin(qMin(cntrDist, startDist), qMin(midDist, endDist))

        if     (minDist == cntrDist)  return center
        elif minDist == startDist) return start
        elif minDist == midDist)   return mid
        elif minDist == endDist)   return end

        return scenePos()

    QList<QPointF> allGripPoints():
        QList<QPointF> gripPoints
        gripPoints << objectCenter() << objectStartPoint() << objectMidPoint() << objectEndPoint()
        return gripPoints

    def gripEdit(const QPointF& before, const QPointF& after):
        /*TODO: gripEdit() for ArcObject*/

class Base_Object():
    def __init__(self):
        return self

    BaseObject(QGraphicsItem* parent) : QGraphicsPathItem(parent):
        debug_message("BaseObject Constructor()")

        objPen.setCapStyle(Qt::RoundCap)
        objPen.setJoinStyle(Qt::RoundJoin)
        lwtPen.setCapStyle(Qt::RoundCap)
        lwtPen.setJoinStyle(Qt::RoundJoin)

        objID = QDateTime::currentMSecsSinceEpoch()

    def setObjectColor(const QColor& color):
        objPen.setColor(color)
        lwtPen.setColor(color)

    def setObjectColorRGB(unsigned int rgb):
        objPen.setColor(QColor(rgb))
        lwtPen.setColor(QColor(rgb))

    def setObjectLineType(Qt::PenStyle lineType):
        objPen.setStyle(lineType)
        lwtPen.setStyle(lineType)

    def setObjectLineWeight(lineWeight):
        "NOTE: The objPen will always be cosmetic. "
        objPen.setWidthF(0)

        if lineWeight < 0:
            if lineWeight == OBJ_LWT_BYLAYER:
                lwtPen.setWidthF(0.35); /*TODO: getLayerLineWeight*/

            elif lineWeight == OBJ_LWT_BYBLOCK:
                lwtPen.setWidthF(0.35); /*TODO: getBlockLineWeight*/

            else:
                QMessageBox::warning(0, QObject::tr("Error - Negative Lineweight"),
                                        QObject::tr("Lineweight: %1")
                                        .arg(QString().setNum(lineWeight)))
                debug_message("Lineweight cannot be negative! Inverting sign.")
                lwtPen.setWidthF(-lineWeight)

        else:
            lwtPen.setWidthF(lineWeight)

    def objectRubberPoint(const QString& key):
        if objRubberPoints.contains(key))
            return objRubberPoints.value(key)

        QGraphicsScene* gscene = scene()
        if gscene)
            return scene().property("SCENE_QSNAP_POINT").toPointF()
        return QPointF()

    def objectRubberText(key):
        if objRubberTexts.contains(key))
            return objRubberTexts.value(key)
        return QString()

    def boundingRect():
        /*If gripped, force this object to be drawn even if it is offscreen*/
        if objectRubberMode() == OBJ_RUBBER_GRIP)
            return scene().sceneRect()
        return path().boundingRect()

    def drawRubberLine(const QLineF& rubLine, QPainter* painter, const char* colorFromScene):
        if painter:
            QGraphicsScene* objScene = scene()
            if !objScene) return
            QPen colorPen = objPen
            colorPen.setColor(QColor(objScene.property(colorFromScene).toUInt()))
            painter.setPen(colorPen)
            painter.drawLine(rubLine)
            painter.setPen(objPen)

    def realRender(QPainter* painter, const QPainterPath& renderPath):
        "lighter color"
        color1 = objectColor();       
        color2 = color1.darker(150); /*darker color*/

        # If we have a dark color, lighten it.
        darkness = color1.lightness()
        threshold = 32
        "TODO: This number may need adjusted or maybe just add it to settings."
        if (darkness < threshold) 
            color2 = color1
            if not darkness:
                color1 = QColor(threshold, threshold, threshold)
    /*lighter() does not affect pure black*/
            else:
                color1 = color2.lighter(100 + threshold)

        int count = renderPath.elementCount()
        for(int i = 0; i < count-1; ++i)

            QPainterPath::Element elem = renderPath.elementAt(i)
            QPainterPath::Element next = renderPath.elementAt(i+1)

            if next.isMoveTo()) continue

            QPainterPath elemPath
            elemPath.moveTo(elem.x, elem.y)
            elemPath.lineTo(next.x, next.y)

            QPen renderPen(QColor(0,0,0,0))
            renderPen.setWidthF(0)
            painter.setPen(renderPen)
            QPainterPathStroker stroker
            stroker.setWidth(0.35)
            stroker.setCapStyle(Qt::RoundCap)
            stroker.setJoinStyle(Qt::RoundJoin)
            QPainterPath realPath = stroker.createStroke(elemPath)
            painter.drawPath(realPath)

            QLinearGradient grad(elemPath.pointAtPercent(0.5), elemPath.pointAtPercent(0.0))
            grad.setColorAt(0, color1)
            grad.setColorAt(1, color2)
            grad.setSpread(QGradient::ReflectSpread)

            painter.fillPath(realPath, QBrush(grad))

class Dim_Leader(Base_Object):
    def __init__(self, x1, y1, x2, y2, rgb="Black", lineType="solid"):
        self.super().__init__()
        self.point1 = Vector(x1, y1)
        self.point2 = Vector(x2, y2)
        setData(OBJ_TYPE, type())
        setData(OBJ_NAME, obj_names[OBJ_TYPE_DIMLEADER])

        setFlag(QGraphicsItem::ItemIsSelectable, 1)

        curved = 0
        filled = 1
        setObjectEndPoint1(to_emb_vector(QPointF(x1, y1)))
        setObjectEndPoint2(to_emb_vector(QPointF(x2, y2)))
        setObjectColor(rgb)
        setObjectLineType(lineType)
        setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
        setPen(objectPen())
        return self

    def DimLeaderObject(x1, y1, x2, y2, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
        debug_message("DimLeaderObject Constructor()")
        init(x1, y1, x2, y2, rgb, Qt::SolidLine)
        " TODO: getCurrentLineType "

    def DimLeaderObject(DimLeaderObject* obj, QGraphicsItem* parent) : BaseObject(parent):
        debug_message("DimLeaderObject Constructor()")
        if obj:
            v1 = to_emb_vector(obj.objectEndPoint1())
            v2 = to_emb_vector(obj.objectEndPoint2())
            init(v1.x, v1.y, v2.x, v2.y, obj.objectColorRGB(), Qt::SolidLine)
            " TODO: getCurrentLineType "

    def setObjectEndPoint1(p1):
        endPt2 = objectEndPoint2()
        x2 = endPt2.x()
        y2 = endPt2.y()
        diff.x = x2 - p1.x
        diff.y = y2 - p1.y
        setRotation(0)
        setLine(0, 0, diff.x, diff.y)
        setPos(p1.x, p1.y)
        updateLeader()

    def setObjectEndPoint2(p2):
        endPt1 = to_emb_vector(scenePos())
        setRotation(0)
        setLine(0, 0, p2.x - endPt1.x, p2.y - endPt1.y)
        setPos(endPt1.x, endPt1.y)
        updateLeader()

    def objectEndPoint1():
        return scenePos()

    def objectEndPoint2():
        v.x = line().x2()
        v.y = line().y2()
        v = scale_and_rotate(v, scale(), radians(rotation()))

        return scenePos() + to_qpointf(v)

    def objectMidPoint():
        v = to_emb_vector(line().pointAt(0.5))
        v = scale_and_rotate(v, scale(), radians(rotation()))

        return scenePos() + to_qpointf(v)

    def objectAngle():
        angle = line().angle() - rotation()
        return fmod(angle, 360.0)

    def updateLeader():
        int arrowStyle = Closed; /*TODO: Make this customizable*/
        arrowStyleAngle = 15.0; /*TODO: Make this customizable*/
        arrowStyleLength = 1.0; /*TODO: Make this customizable*/
        lineStyleAngle = 45.0; /*TODO: Make this customizable*/
        lineStyleLength = 1.0; /*TODO: Make this customizable*/

        lyne = line()
        angle = lyne.angle()
        ap0 = lyne.p1()
        lp0 = lyne.p2()

        # Arrow
        QLineF lynePerp(lyne.pointAt(arrowStyleLength/lyne.length()) ,lp0)
        lynePerp.setAngle(angle + 90)
        QLineF lyne1(ap0, lp0)
        QLineF lyne2(ap0, lp0)
        lyne1.setAngle(angle + arrowStyleAngle)
        lyne2.setAngle(angle - arrowStyleAngle)
        ap1
        ap2
        # HACK: these need fixing
        # lynePerp.intersects(lyne1, &ap1)
        # lynePerp.intersects(lyne2, &ap2)

        # So they don't cause memory access problems.
        ap1 = lyne1.p1()
        ap2 = lyne2.p1()

        """
        Math Diagram
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
        """

        if arrowStyle == Open)
    
            arrowStylePath = QPainterPath()
            arrowStylePath.moveTo(ap1)
            arrowStylePath.lineTo(ap0)
            arrowStylePath.lineTo(ap2)
            arrowStylePath.lineTo(ap0)
            arrowStylePath.lineTo(ap1)

        elif arrowStyle == Closed)
    
            arrowStylePath = QPainterPath()
            arrowStylePath.moveTo(ap1)
            arrowStylePath.lineTo(ap0)
            arrowStylePath.lineTo(ap2)
            arrowStylePath.lineTo(ap1)

        elif arrowStyle == "Dot":
            arrowStylePath = QPainterPath()
            arrowStylePath.addEllipse(ap0, arrowStyleLength, arrowStyleLength)

        elif arrowStyle == "Box":
            arrowStylePath = QPainterPath()
            side = QLineF(ap1, ap2).length()
            QRectF ar0(0, 0, side, side)
            ar0.moveCenter(ap0)
            arrowStylePath.addRect(ar0)

        elif arrowStyle == "Tick":
    


            lineStylePath = QPainterPath()
            lineStylePath.moveTo(ap0)
            lineStylePath.lineTo(lp0)

        def paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
            QGraphicsScene* objScene = scene()
            if !objScene) return

            QPen paintPen = pen()
            painter.setPen(paintPen)
            updateRubber(painter)
            if option.state & QStyle::State_Selected)   paintPen.setStyle(Qt::DashLine)
            if objScene.property("ENABLE_LWT").toBool())  paintPen = lineWeightPen()
            painter.setPen(paintPen)

            painter.drawPath(lineStylePath)
            painter.drawPath(arrowStylePath)

            if filled)
                painter.fillPath(arrowStylePath, objectColor())

        def updateRubber(QPainter* painter):
            int rubberMode = objectRubberMode()
            if rubberMode == OBJ_RUBBER_DIMLEADER_LINE)
        
                sceneStartPoint = objectRubberPoint("DIMLEADER_LINE_START")
                sceneQSnapPoint = objectRubberPoint("DIMLEADER_LINE_END")

                setObjectEndPoint1(to_emb_vector(sceneStartPoint))
                setObjectEndPoint2(to_emb_vector(sceneQSnapPoint))

            elif rubberMode == OBJ_RUBBER_GRIP)
        
                if painter)
            
                    gripPoint = objectRubberPoint("GRIP_POINT")
                    if     (gripPoint == objectEndPoint1()) painter.drawLine(line().p2(), mapFromScene(objectRubberPoint(QString())))
                    elif gripPoint == objectEndPoint2()) painter.drawLine(line().p1(), mapFromScene(objectRubberPoint(QString())))
                    elif gripPoint == objectMidPoint())  painter.drawLine(line().translated(mapFromScene(objectRubberPoint(QString()))-mapFromScene(gripPoint)))

        def vulcanize():
            debug_message("DimLeaderObject vulcanize()")
            updateRubber()

            setObjectRubberMode(OBJ_RUBBER_OFF)

        def mouseSnapPoint(const QPointF& mousePoint):
            " Returns the closest snap point to the mouse point. "
            endPoint1 = objectEndPoint1()
            endPoint2 = objectEndPoint2()
            midPoint = objectMidPoint()

            end1Dist = QLineF(mousePoint, endPoint1).length()
            end2Dist = QLineF(mousePoint, endPoint2).length()
            midDist = QLineF(mousePoint, midPoint).length()

            minDist = min(end1Dist, end2Dist)

            if curved:
                minDist = min(minDist, midDist)

            if     (minDist == end1Dist) return endPoint1
            elif minDist == end2Dist) return endPoint2
            elif minDist == midDist)  return midPoint

            return scenePos()

        QList<QPointF> allGripPoints():
            QList<QPointF> gripPoints
            gripPoints << objectEndPoint1() << objectEndPoint2()
            if curved)
                gripPoints << objectMidPoint()
            return gripPoints

        def gripEdit(const QPointF& before, const QPointF& after):
            if before == objectEndPoint1():
                setObjectEndPoint1(to_emb_vector(after))
            elif before == objectEndPoint2())
                setObjectEndPoint2(to_emb_vector(after))
            elif before == objectMidPoint())     delta = after-before; moveBy(delta.x(), delta.y())

class Ellipse(Base_Object):
    def __init__(self, centerX, centerY, width, height, unsigned int rgb, Qt::PenStyle lineType):
        setData(OBJ_TYPE, type())
        setData(OBJ_NAME, obj_names[OBJ_TYPE_ELLIPSE])

        setFlag(QGraphicsItem::ItemIsSelectable, 1)

        setObjectSize(width, height)
        setPos(centerX, centerY)
        setObjectColor(rgb)
        setObjectLineType(lineType)
        setObjectLineWeight(0.35); /* TODO: pass in proper lineweight */
        setPen(objectPen())
        updatePath()
        return self

    def EllipseObject(centerX, centerY, width, height, rgb, parent):
        "TODO: getCurrentLineType"
        debug_message("EllipseObject Constructor()")
        init(centerX, centerY, width, height, rgb, Qt::SolidLine)

    def EllipseObject(obj, parent):
        " TODO: getCurrentLineType "
        debug_message("EllipseObject Constructor()")
        if obj:
            init(obj.objectCenter().x(), obj.objectCenter().y(), obj.objectWidth(), obj.objectHeight(), obj.objectColorRGB(), Qt::SolidLine)
            setRotation(obj.rotation())

    def def setObjectSize(width, height):
        QRectF elRect = rect()
        elRect.setWidth(width)
        elRect.setHeight(height)
        elRect.moveCenter(QPointF(0,0))
        setRect(elRect)

    def def setObjectRadiusMajor(radius):
        setObjectDiameterMajor(radius*2.0)

    def def setObjectRadiusMinor(radius):
        setObjectDiameterMinor(radius*2.0)

    def def setObjectDiameterMajor(diameter):
        QRectF elRect = rect()
        if (elRect.width() > elRect.height()) 
            elRect.setWidth(diameter)

        else
            elRect.setHeight(diameter)
        elRect.moveCenter(QPointF(0,0))
        setRect(elRect)

    def def setObjectDiameterMinor(diameter):
        QRectF elRect = rect()
        if elRect.width() < elRect.height():
            elRect.setWidth(diameter)
        else:
            elRect.setHeight(diameter)
        elRect.moveCenter(QPointF(0,0))
        setRect(elRect)

    def objectQuadrant0():
        v.x = objectWidth()/2.0
        v.y = 0.0
        v = rotate_vector(v, radians(rotation()))
        return objectCenter() + to_qpointf(v)

    def objectQuadrant90():
        v.x = objectHeight()/2.0
        v.y = 0.0
        v = rotate_vector(v, radians(rotation()+90.0))
        return objectCenter() + to_qpointf(v)

    def objectQuadrant180():
        v.x = objectWidth()/2.0
        v.y = 0.0
        v = rotate_vector(v, radians(rotation()+180.0))
        return objectCenter() + to_qpointf(v)

    def objectQuadrant270():
        v.x = objectHeight()/2.0
        v.y = 0.0
        v = rotate_vector(v, radians(rotation()+270.0))
        return objectCenter() + to_qpointf(v)

    def def updatePath():
        QPainterPath path
        QRectF r = rect()
        path.arcMoveTo(r, 0)
        path.arcTo(r, 0, 360)
        /* NOTE: Reverse the path so that the inside area isn't considered part of the ellipse. */
        path.arcTo(r, 0, -360)
        setObjectPath(path)

    def def paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
        QGraphicsScene* objScene = scene()
        if !objScene) return

        QPen paintPen = pen()
        painter.setPen(paintPen)
        updateRubber(painter)
        if option.state & QStyle::State_Selected)   paintPen.setStyle(Qt::DashLine)
        if objScene.property("ENABLE_LWT").toBool())  paintPen = lineWeightPen()
        painter.setPen(paintPen)

        painter.drawEllipse(rect())

    def updateRubber(QPainter* painter):
        int rubberMode = objectRubberMode()
        if rubberMode == OBJ_RUBBER_ELLIPSE_LINE)
    
            sceneLinePoint1 = objectRubberPoint("ELLIPSE_LINE_POINT1")
            sceneLinePoint2 = objectRubberPoint("ELLIPSE_LINE_POINT2")
            itemLinePoint1 = mapFromScene(sceneLinePoint1)
            itemLinePoint2 = mapFromScene(sceneLinePoint2)
            QLineF itemLine(itemLinePoint1, itemLinePoint2)
            if painter) drawRubberLine(itemLine, painter, "VIEW_COLOR_CROSSHAIR")
            updatePath()

        elif rubberMode == OBJ_RUBBER_ELLIPSE_MAJORDIAMETER_MINORRADIUS)
    
            sceneAxis1Point1 = objectRubberPoint("ELLIPSE_AXIS1_POINT1")
            sceneAxis1Point2 = objectRubberPoint("ELLIPSE_AXIS1_POINT2")
            sceneCenterPoint = objectRubberPoint("ELLIPSE_CENTER")
            sceneAxis2Point2 = objectRubberPoint("ELLIPSE_AXIS2_POINT2")
            ellipseWidth = objectRubberPoint("ELLIPSE_WIDTH").x()
            ellipseRot = objectRubberPoint("ELLIPSE_ROT").x()

            /* TODO: incorporate perpendicularDistance() into libembroidery. */
            px = sceneAxis2Point2.x()
            py = sceneAxis2Point2.y()
            x1 = sceneAxis1Point1.x()
            y1 = sceneAxis1Point1.y()
            QLineF line(sceneAxis1Point1, sceneAxis1Point2)
            QLineF norm = line.normalVector()
            dx = px-x1
            dy = py-y1
            norm.translate(dx, dy)
            /* HACK: this isn't in all versions of Qt 5 in the same place?
            * norm.intersects(line, &iPoint)
            */
            iPoint = line.p1()
            ellipseHeight = QLineF(px, py, iPoint.x(), iPoint.y()).length()*2.0

            setPos(sceneCenterPoint)
            setObjectSize(ellipseWidth, ellipseHeight)
            setRotation(-ellipseRot)

            itemCenterPoint = mapFromScene(sceneCenterPoint)
            itemAxis2Point2 = mapFromScene(sceneAxis2Point2)
            QLineF itemLine(itemCenterPoint, itemAxis2Point2)
            if painter) drawRubberLine(itemLine, painter, "VIEW_COLOR_CROSSHAIR")
            updatePath()

        elif rubberMode == OBJ_RUBBER_ELLIPSE_MAJORRADIUS_MINORRADIUS":
            sceneAxis1Point2 = objectRubberPoint("ELLIPSE_AXIS1_POINT2")
            sceneCenterPoint = objectRubberPoint("ELLIPSE_CENTER")
            sceneAxis2Point2 = objectRubberPoint("ELLIPSE_AXIS2_POINT2")
            ellipseWidth = objectRubberPoint("ELLIPSE_WIDTH").x()
            ellipseRot = objectRubberPoint("ELLIPSE_ROT").x()

            /* TODO: incorporate perpendicularDistance() into libembroidery. */
            px = sceneAxis2Point2.x()
            py = sceneAxis2Point2.y()
            x1 = sceneCenterPoint.x()
            y1 = sceneCenterPoint.y()
            QLineF line(sceneCenterPoint, sceneAxis1Point2)
            QLineF norm = line.normalVector()
            dx = px-x1
            dy = py-y1
            norm.translate(dx, dy)
            iPoint
            /* HACK */
            /* norm.intersects(line, &iPoint); */
            iPoint = line.p1()
            ellipseHeight = QLineF(px, py, iPoint.x(), iPoint.y()).length()*2.0

            setPos(sceneCenterPoint)
            setObjectSize(ellipseWidth, ellipseHeight)
            setRotation(-ellipseRot)

            itemCenterPoint = mapFromScene(sceneCenterPoint)
            itemAxis2Point2 = mapFromScene(sceneAxis2Point2)
            QLineF itemLine(itemCenterPoint, itemAxis2Point2)
            if painter) drawRubberLine(itemLine, painter, "VIEW_COLOR_CROSSHAIR")
            updatePath()

        elif rubberMode == OBJ_RUBBER_GRIP)
    
            /* TODO: updateRubber() gripping for EllipseObject. */

    def vulcanize():
        debug_message("EllipseObject vulcanize()")
        updateRubber()

        setObjectRubberMode(OBJ_RUBBER_OFF)

    def mouseSnapPoint(const QPointF& mousePoint):
        " Returns the closest snap point to the mouse point. "
        center = objectCenter()
        quad0 = objectQuadrant0()
        quad90 = objectQuadrant90()
        quad180 = objectQuadrant180()
        quad270 = objectQuadrant270()

        cntrDist = QLineF(mousePoint, center).length()
        q0Dist = QLineF(mousePoint, quad0).length()
        q90Dist = QLineF(mousePoint, quad90).length()
        q180Dist = QLineF(mousePoint, quad180).length()
        q270Dist = QLineF(mousePoint, quad270).length()

        minDist = qMin(qMin(qMin(q0Dist, q90Dist), qMin(q180Dist, q270Dist)), cntrDist)

        if     (minDist == cntrDist) return center
        elif minDist == q0Dist)   return quad0
        elif minDist == q90Dist)  return quad90
        elif minDist == q180Dist) return quad180
        elif minDist == q270Dist) return quad270

        return scenePos()

    def allGripPoints():
        QList<QPointF> gripPoints
        gripPoints << objectCenter() << objectQuadrant0() << objectQuadrant90() << objectQuadrant180() << objectQuadrant270()
        return gripPoints

    def gripEdit(const QPointF& before, const QPointF& after):
        "/*TODO: gripEdit() for EllipseObject*/"

    def objectSavePath():
        r = Rect()
        path.arcMoveTo(r, 0)
        path.arcTo(r, 0, 360)

        s = scale()
        QTransform trans
        trans.rotate(rotation())
        trans.scale(s,s)
        return trans.map(path)

class Image(Base_Object):
    def __init__(self):
        return self

    def ImageObject(x, y, w, h, unsigned int rgb, QGraphicsItem* parent):
        debug_message("ImageObject Constructor()")
        init(x, y, w, h, rgb, Qt::SolidLine)
        "/*TODO: getCurrentLineType*/"

    def ImageObject(ImageObject* obj, QGraphicsItem* parent) : BaseObject(parent):
        debug_message("ImageObject Constructor()")
        if obj:
            ptl = obj.objectTopLeft()
            init(ptl.x(), ptl.y(), obj.objectWidth(), obj.objectHeight(), obj.objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
            setRotation(obj.rotation())

    def init(x, y, w, h, unsigned int rgb, Qt::PenStyle lineType):
        setData(OBJ_TYPE, type())
        setData(OBJ_NAME, obj_names[OBJ_TYPE_IMAGE])

        setFlag(QGraphicsItem::ItemIsSelectable, 1)

        setObjectRect(x, y, w, h)
        setObjectColor(rgb)
        setObjectLineType(lineType)
        setObjectLineWeight(0.35); /* TODO: pass in proper lineweight */
        setPen(objectPen())

    def setObjectRect(x, y, w, h):
        setPos(x, y)
        setRect(0, 0, w, h)
        updatePath()

    def objectTopLeft()
        EmbVector v = to_emb_vector(rect().topLeft())
        v = scale_and_rotate(v, scale(), radians(rotation()))

        return scenePos() + to_qpointf(v)

    def objectTopRight()
        EmbVector v = to_emb_vector(rect().topRight())
        v = scale_and_rotate(v, scale(), radians(rotation()))

        return scenePos() + to_qpointf(v)

    def objectBottomLeft()
        EmbVector v = to_emb_vector(rect().bottomLeft())
        v = scale_and_rotate(v, scale(), radians(rotation()))

        return scenePos() + to_qpointf(v)

    def objectBottomRight()
        EmbVector v = to_emb_vector(rect().bottomRight())
        v = scale_and_rotate(v, scale(), radians(rotation()))

        return scenePos() + to_qpointf(v)

    def updatePath():
        " NOTE: Reverse the path so that the inside area isn't considered part of the rectangle. "
        r = rect()
        path.moveTo(r.bottomLeft())
        path.lineTo(r.bottomRight())
        path.lineTo(r.topRight())
        path.lineTo(r.topLeft())
        path.lineTo(r.bottomLeft())
        path.lineTo(r.topLeft())
        path.lineTo(r.topRight())
        path.lineTo(r.bottomRight())
        path.moveTo(r.bottomLeft())
        setObjectPath(path)

    def paint(painter, option, QWidget* /*widget*/):
        QGraphicsScene* objScene = scene()
        if !objScene) return

        QPen paintPen = pen()
        painter.setPen(paintPen)
        updateRubber(painter)
        if option.state & QStyle::State_Selected)   paintPen.setStyle(Qt::DashLine)
        if objScene.property("ENABLE_LWT").toBool())  paintPen = lineWeightPen()
        painter.setPen(paintPen)

        painter.drawRect(rect())

    def updateRubber(painter):
        int rubberMode = objectRubberMode()
        if rubberMode == OBJ_RUBBER_IMAGE)
    
            sceneStartPoint = objectRubberPoint("IMAGE_START")
            sceneEndPoint = objectRubberPoint("IMAGE_END")
            x = sceneStartPoint.x()
            y = sceneStartPoint.y()
            w = sceneEndPoint.x() - sceneStartPoint.x()
            h = sceneEndPoint.y() - sceneStartPoint.y()
            setObjectRect(x,y,w,h)
            updatePath()

        elif rubberMode == OBJ_RUBBER_GRIP:
            " TODO: updateRubber() gripping for ImageObject. "

    def vulcanize():
        debug_message("ImageObject vulcanize()")
        updateRubber()

        setObjectRubberMode(OBJ_RUBBER_OFF)

    def mouseSnapPoint(const QPointF& mousePoint):
        " Returns the closest snap point to the mouse point. "
        ptl = objectTopLeft();     /* Top Left Corner QSnap */
        ptr = objectTopRight();    /* Top Right Corner QSnap */
        pbl = objectBottomLeft();  /*Bottom Left Corner QSnap*/
        pbr = objectBottomRight(); /*Bottom Right Corner QSnap*/

        ptlDist = QLineF(mousePoint, ptl).length()
        ptrDist = QLineF(mousePoint, ptr).length()
        pblDist = QLineF(mousePoint, pbl).length()
        pbrDist = QLineF(mousePoint, pbr).length()

        minDist = min(min(ptlDist, ptrDist), min(pblDist, pbrDist))

        if minDist == ptlDist:
            return ptl
        elif minDist == ptrDist:
            return ptr
        elif minDist == pblDist:
            return pbl
        elif minDist == pbrDist:
            return pbr

        return scenePos()

    QList<QPointF> def allGripPoints():
        QList<QPointF> gripPoints
        gripPoints << objectTopLeft() << objectTopRight() << objectBottomLeft() << objectBottomRight()
        return gripPoints

    def gripEdit(before, after):
        " TODO: gripEdit() for ImageObject "
        return

class Line(Base_Object):
    def __init__(self):
        return self

    def LineObject(x1, y1, x2, y2, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
        debug_message("LineObject Constructor()")
        init(x1, y1, x2, y2, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/

    def LineObject(LineObject* obj, QGraphicsItem* parent) : BaseObject(parent):
        debug_message("LineObject Constructor()")
        if obj:
            init(obj.objectX1(), obj.objectY1(), obj.objectX2(), obj.objectY2(), obj.objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/

    def init(x1, y1, x2, y2, unsigned int rgb, Qt::PenStyle lineType):
        setData(OBJ_TYPE, type())
        setData(OBJ_NAME, obj_names[OBJ_TYPE_LINE])

        setFlag(QGraphicsItem::ItemIsSelectable, 1)

        setObjectEndPoint1(x1, y1)
        setObjectEndPoint2(x2, y2)
        setObjectColor(rgb)
        setObjectLineType(lineType)
        /* TODO: pass in proper lineweight */
        setObjectLineWeight(0.35)
        setPen(objectPen())

    def setObjectEndPoint1(const QPointF& endPt1):
        setObjectEndPoint1(endPt1.x(), endPt1.y())

    def setObjectEndPoint1(x1, y1):
        EmbVector delta, endPt2
        endPt2 = to_emb_vector(objectEndPoint2())
        delta.x = endPt2.x - x1
        delta.y = endPt2.y - y1
        setRotation(0)
        setScale(1)
        setLine(0, 0, delta.x, delta.y)
        setPos(x1, y1)

    def setObjectEndPoint2(const QPointF& endPt2):
        setObjectEndPoint2(endPt2.x(), endPt2.y())

    def setObjectEndPoint2(x2, y2):
        EmbVector delta, endPt1
        endPt1 = to_emb_vector(scenePos())
        delta.x = x2 - endPt1.x
        delta.y = y2 - endPt1.y
        setRotation(0)
        setScale(1)
        setLine(0, 0, delta.x, delta.y)
        setPos(endPt1.x, endPt1.y)

    objectEndPoint2()
        EmbVector v
        v.x = line().x2()
        v.y = line().y2()
        v = scale_and_rotate(v, scale(), radians(rotation()))

        return scenePos() + to_qpointf(v)

    objectMidPoint()
        EmbVector v
        v = to_emb_vector(line().pointAt(0.5))
        v = scale_and_rotate(v, scale(), radians(rotation()))

        return scenePos() + to_qpointf(v)

    objectAngle()
        angle = line().angle() - rotation()
        return fmod(angle, 360.0)

    def paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
        QGraphicsScene* objScene = scene()
        if !objScene) return

        QPen paintPen = pen()
        painter.setPen(paintPen)
        updateRubber(painter)
        if option.state & QStyle::State_Selected)   paintPen.setStyle(Qt::DashLine)
        if objScene.property("ENABLE_LWT").toBool())  paintPen = lineWeightPen()
        painter.setPen(paintPen)

        if objectRubberMode() != OBJ_RUBBER_LINE) painter.drawLine(line())

        if objScene.property("ENABLE_LWT").toBool() and objScene.property("ENABLE_REAL").toBool())  realRender(painter, path())

    def updateRubber(painter):
        int rubberMode = objectRubberMode()
        if rubberMode == OBJ_RUBBER_LINE:
            sceneStartPoint = objectRubberPoint("LINE_START")
            sceneQSnapPoint = objectRubberPoint("LINE_END")

            setObjectEndPoint1(sceneStartPoint)
            setObjectEndPoint2(sceneQSnapPoint)

            drawRubberLine(line(), painter, "VIEW_COLOR_CROSSHAIR")

        elif rubberMode == OBJ_RUBBER_GRIP:
            if painter:
                gripPoint = objectRubberPoint("GRIP_POINT")
                if     (gripPoint == objectEndPoint1()) painter.drawLine(line().p2(), mapFromScene(objectRubberPoint(QString())))
                elif gripPoint == objectEndPoint2()) painter.drawLine(line().p1(), mapFromScene(objectRubberPoint(QString())))
                elif gripPoint == objectMidPoint())  painter.drawLine(line().translated(mapFromScene(objectRubberPoint(QString()))-mapFromScene(gripPoint)))

                QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
                drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")

    def vulcanize():
        debug_message("LineObject vulcanize()")
        updateRubber()

        setObjectRubberMode(OBJ_RUBBER_OFF)

    def mouseSnapPoint(mousePoint):
        " Returns the closest snap point to the mouse point. "
        endPoint1 = objectEndPoint1()
        endPoint2 = objectEndPoint2()
        midPoint = objectMidPoint()

        end1Dist = QLineF(mousePoint, endPoint1).length()
        end2Dist = QLineF(mousePoint, endPoint2).length()
        midDist = QLineF(mousePoint, midPoint).length()

        minDist = qMin(qMin(end1Dist, end2Dist), midDist)

        if     (minDist == end1Dist) return endPoint1
        elif minDist == end2Dist) return endPoint2
        elif minDist == midDist)  return midPoint

        return scenePos()

    def allGripPoints():
        QList<QPointF> gripPoints
        gripPoints << objectEndPoint1() << objectEndPoint2() << objectMidPoint()
        return gripPoints

    def gripEdit(const QPointF& before, const QPointF& after):
        if     (before == objectEndPoint1())  setObjectEndPoint1(after.x(), after.y())
        elif before == objectEndPoint2())  setObjectEndPoint2(after.x(), after.y())
        elif before == objectMidPoint())   delta = after-before; moveBy(delta.x(), delta.y())

    def objectSavePath():
        QPainterPath path
        path.lineTo(objectDeltaX(), objectDeltaY())
        return path

class Path(Base_Object):
    def __init__(self, x, y, p, rgb, lineType):
        "TODO: pass in proper lineweight."
        self.super().__init__()
        self.OBJ_TYPE = "OBJ_TYPE_PATH"
        setData(OBJ_NAME, obj_names[OBJ_TYPE_PATH])

        setFlag(QGraphicsItem::ItemIsSelectable, 1)

        updatePath(p)
        setObjectPos(x,y)
        setObjectColor(rgb)
        setObjectLineType(lineType)
        setObjectLineWeight(0.35)
        setPen(objectPen())
        return self

    def PathObject(x, y, const QPainterPath p, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
        " TODO: getCurrentLineType "
        debug_message("PathObject Constructor()")
        init(x, y, p, rgb, Qt::SolidLine)

    def PathObject(PathObject* obj, QGraphicsItem* parent) : BaseObject(parent):
        debug_message("PathObject Constructor()")
        if obj:
            init(obj.objectX(), obj.objectY(), obj.objectCopyPath(), obj.objPen.color().rgb(), Qt::SolidLine); /*TODO: getCurrentLineType*/
            setRotation(obj.rotation())
            setScale(obj.scale())

    def PathObject::updatePath(self, p):
        normalPath = p
        QPainterPath reversePath = normalPath.toReversed()
        reversePath.connectPath(normalPath)
        setObjectPath(reversePath)

    def PathObject::paint(self, painter, option, widget):
        QGraphicsScene* objScene = scene()
        if !objScene) return

        QPen paintPen = pen()
        painter.setPen(paintPen)
        updateRubber(painter)
        if option.state & QStyle::State_Selected)   paintPen.setStyle(Qt::DashLine)
        if objScene.property("ENABLE_LWT").toBool())  paintPen = lineWeightPen()
        painter.setPen(paintPen)

        painter.drawPath(objectPath())

    def PathObject::updateRubber(self, painter):
        """
        TODO: Path Rubber Modes.

        TODO: updateRubber() gripping for PathObject.
        """

    def PathObject::vulcanize(self):
        debug_message("PathObject vulcanize()")
        updateRubber()

        setObjectRubberMode(OBJ_RUBBER_OFF)

        if !normalPath.elementCount())
            QMessageBox::critical(0, QObject::tr("Empty Path Error"), QObject::tr("The path added contains no points. The command that created this object has flawed logic."))

    PathObject::mouseSnapPoint(const QPointF& mousePoint):
        " Returns the closest snap point to the mouse point. "
        return scenePos()

    def allGripPoints():
        " TODO: loop thru all path Elements and return their points. "
        QList<QPointF> gripPoints
        gripPoints << scenePos()
        return gripPoints

    def gripEdit(before, after):
        " TODO: gripEdit() for PathObject."
        return

    def objectCopyPath(self):
        return normalPath

    def objectSavePath(self):
        s = scale()
        QTransform trans
        trans.rotate(rotation())
        trans.scale(s,s)
        return trans.map(normalPath)

class Point(Base_Object):
    def __init__(self, x, y, unsigned int rgb, Qt::PenStyle lineType):
        " TODO: pass in proper lineweight. "
        setData(OBJ_TYPE, type())
        setData(OBJ_NAME, obj_names[OBJ_TYPE_POINT])

        setFlag(QGraphicsItem::ItemIsSelectable, 1)

        setRect(-0.00000001, -0.00000001, 0.00000002, 0.00000002)
        setObjectPos(x,y)
        setObjectColor(rgb)
        setObjectLineType(lineType)
        setObjectLineWeight(0.35); 
        setPen(objectPen())
        return self

    def PointObject(x, y, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
        debug_message("PointObject Constructor()")
        init(x, y, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/

    def PointObject(PointObject* obj, QGraphicsItem* parent) : BaseObject(parent):
        debug_message("PointObject Constructor()")
        if obj:
            init(obj.objectX(), obj.objectY(), obj.objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
            setRotation(obj.rotation())

    def paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
        QGraphicsScene* objScene = scene()
        if !objScene) return

        QPen paintPen = pen()
        painter.setPen(paintPen)
        updateRubber(painter)
        if option.state & QStyle::State_Selected)   paintPen.setStyle(Qt::DashLine)
        if objScene.property("ENABLE_LWT").toBool())  paintPen = lineWeightPen()
        painter.setPen(paintPen)

        painter.drawPoint(0,0)

    def PointObject::updateRubber(painter):
        rubberMode = objectRubberMode()
        if rubberMode == "GRIP":
            if painter:
                gripPoint = objectRubberPoint("GRIP_POINT")
                if gripPoint == scenePos():
                    QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
                    drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")

    def vulcanize():
        debug_message("PointObject vulcanize()")
        updateRubber()

        setObjectRubberMode(OBJ_RUBBER_OFF)

    def mouseSnapPoint(const QPointF& mousePoint):
        " Returns the closest snap point to the mouse point. "
        return scenePos()

    def allGripPoints():
        QList<QPointF> gripPoints
        gripPoints << scenePos()
        return gripPoints

    def gripEdit(const QPointF& before, const QPointF& after):
        if before == scenePos():
            delta = after-before
            moveBy(delta.x(), delta.y())

    def objectSavePath():
        QPainterPath path
        path.addRect(-0.00000001, -0.00000001, 0.00000002, 0.00000002)
        return path


class Polygon():
    def __init__(self, x, y, path=0, rgb="#FFFFFF", line_type="solid",
                 line_weight=0.35):
        self.x = x
        self.y = y
        self.path = path
        self.color = rgb
        self.line_type = line_type
        self.rotation = 0.0
        self.scale = 1.0
        self.type = "polygon"
        self.selectable = True
        self.grip_index = -1
        self.line_weight = line_weight
        self.pen = Pen()
        self.updatePath(path)
        return self

    def updatePath(const QPainterPath& p):
        normalPath = p
        QPainterPath closedPath = normalPath
        closedPath.closeSubpath()
        QPainterPath reversePath = closedPath.toReversed()
        reversePath.connectPath(closedPath)
        setObjectPath(reversePath)

def PolygonObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
    QGraphicsScene* objScene = scene()
    if !objScene) return

    QPen paintPen = pen()
    painter.setPen(paintPen)
    updateRubber(painter)
    if option.state & QStyle::State_Selected)   paintPen.setStyle(Qt::DashLine)
    if objScene.property("ENABLE_LWT").toBool())  paintPen = lineWeightPen()
    painter.setPen(paintPen)

    if normalPath.elementCount():
        painter.drawPath(normalPath)
        QPainterPath::Element zero = normalPath.elementAt(0)
        QPainterPath::Element last = normalPath.elementAt(normalPath.elementCount()-1)
        painter.drawLine(QPointF(zero.x, zero.y), QPointF(last.x, last.y))

def PolygonObject::updateRubber(QPainter* painter):
    int rubberMode = objectRubberMode()
    if (rubberMode == OBJ_RUBBER_POLYGON) 
        setObjectPos(objectRubberPoint("POLYGON_POINT_0"))

        bool ok = 0
        QString numStr = objectRubberText("POLYGON_NUM_POINTS")
        if numStr.isNull()) return
        int num = numStr.toInt(&ok)
        if !ok) return

        QString appendStr
        QPainterPath rubberPath
        rubberPath.moveTo(mapFromScene(objectRubberPoint("POLYGON_POINT_0")))
        for(int i = 1; i <= num; i++)
    
            appendStr = "POLYGON_POINT_" + QString().setNum(i)
            appendPoint = mapFromScene(objectRubberPoint(appendStr))
            rubberPath.lineTo(appendPoint)

        /*rubberPath.lineTo(0,0);*/
        updatePath(rubberPath)

        /*Ensure the path isn't updated until the number of points is changed again*/
        setObjectRubberText("POLYGON_NUM_POINTS", QString())
    }
    elif rubberMode == OBJ_RUBBER_POLYGON_INSCRIBE) 
        setObjectPos(objectRubberPoint("POLYGON_CENTER"))

        unsigned short numSides = objectRubberPoint("POLYGON_NUM_SIDES").x()

        inscribePoint = mapFromScene(objectRubberPoint("POLYGON_INSCRIBE_POINT"))
        QLineF inscribeLine = QLineF(QPointF(0,0), inscribePoint)
        inscribeAngle = inscribeLine.angle()
        inscribeInc = 360.0/numSides

        if painter) drawRubberLine(inscribeLine, painter, "VIEW_COLOR_CROSSHAIR")

        QPainterPath inscribePath
        /*First Point*/
        inscribePath.moveTo(inscribePoint)
        /*Remaining Points*/
        for (int i = 1; i < numSides; i++) 
            inscribeLine.setAngle(inscribeAngle + inscribeInc*i)
            inscribePath.lineTo(inscribeLine.p2())

        updatePath(inscribePath)
    }
    elif (rubberMode == OBJ_RUBBER_POLYGON_CIRCUMSCRIBE) 
        setObjectPos(objectRubberPoint("POLYGON_CENTER"))

        unsigned short numSides = objectRubberPoint("POLYGON_NUM_SIDES").x()

        circumscribePoint = mapFromScene(objectRubberPoint("POLYGON_CIRCUMSCRIBE_POINT"))
        QLineF circumscribeLine = QLineF(QPointF(0,0), circumscribePoint)
        circumscribeAngle = circumscribeLine.angle()
        circumscribeInc = 360.0/numSides

        if painter) drawRubberLine(circumscribeLine, painter, "VIEW_COLOR_CROSSHAIR")

        QPainterPath circumscribePath
        /*First Point*/
        QLineF prev(circumscribeLine.p2(), QPointF(0,0))
        prev = prev.normalVector()
        circumscribeLine.setAngle(circumscribeAngle + circumscribeInc)
        QLineF perp(circumscribeLine.p2(), QPointF(0,0))
        perp = perp.normalVector()
        iPoint
        /* HACK perp.intersects(prev, &iPoint); */
        iPoint = perp.p1()
        circumscribePath.moveTo(iPoint)
        /*Remaining Points*/
        for i in range(2, numSides+1):
            prev = perp
            circumscribeLine.setAngle(circumscribeAngle + circumscribeInc*i)
            perp = QLineF(circumscribeLine.p2(), QPointF(0,0))
            perp = perp.normalVector()
            /* HACK perp.intersects(prev, &iPoint); */
            iPoint = perp.p1()
            circumscribePath.lineTo(iPoint)
        updatePath(circumscribePath)

    elif rubberMode == "GRIP":
        if painter:
            int elemCount = normalPath.elementCount()
            gripPoint = objectRubberPoint("GRIP_POINT")
            if gripIndex == -1) gripIndex = findIndex(gripPoint)
            if gripIndex == -1) return

            int m = 0
            int n = 0

            if !gripIndex)                 m = elemCount-1; n = 1
            elif gripIndex == elemCount-1)  m = elemCount-2; n = 0
            else                           m = gripIndex-1; n = gripIndex+1
            QPainterPath::Element em = normalPath.elementAt(m)
            QPainterPath::Element en = normalPath.elementAt(n)
            emPoint = QPointF(em.x, em.y)
            enPoint = QPointF(en.x, en.y)
            painter.drawLine(emPoint, mapFromScene(objectRubberPoint(QString())))
            painter.drawLine(enPoint, mapFromScene(objectRubberPoint(QString())))

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")


def PolygonObject::vulcanize():
    debug_message("PolygonObject vulcanize()")
    updateRubber()

    setObjectRubberMode(OBJ_RUBBER_OFF)

    if !normalPath.elementCount())
        QMessageBox::critical(0, QObject::tr("Empty Polygon Error"), QObject::tr("The polygon added contains no points. The command that created this object has flawed logic."))

/* Returns the closest snap point to the mouse point*/
PolygonObject::mouseSnapPoint(const QPointF& mousePoint):
    QPainterPath::Element element = normalPath.elementAt(0)
    closestPoint = mapToScene(QPointF(element.x, element.y))
    closestDist = QLineF(mousePoint, closestPoint).length()
    int elemCount = normalPath.elementCount()
    for i in range(elemCount):
        element = normalPath.elementAt(i)
        elemPoint = mapToScene(element.x, element.y)
        elemDist = QLineF(mousePoint, elemPoint).length()
        if elemDist < closestDist:
            closestPoint = elemPoint
            closestDist = elemDist

    return closestPoint

QList<QPointF> PolygonObject::allGripPoints():
    QList<QPointF> gripPoints
    QPainterPath::Element element
    for(int i = 0; i < normalPath.elementCount(); ++i)

        element = normalPath.elementAt(i)
        gripPoints << mapToScene(element.x, element.y)
    }
    return gripPoints

def PolygonObject::findIndex(const QPointF& point):
    int i = 0
    int elemCount = normalPath.elementCount()
    /*NOTE: Points here are in item coordinates*/
    itemPoint = mapFromScene(point)
    for(i = 0; i < elemCount; i++)

        QPainterPath::Element e = normalPath.elementAt(i)
        elemPoint = QPointF(e.x, e.y)
        if itemPoint == elemPoint) return i
    }
    return -1

def PolygonObject::gripEdit(const QPointF& before, const QPointF& after):
    gripIndex = findIndex(before)
    if gripIndex == -1) return
    a = mapFromScene(after)
    normalPath.setElementPositionAt(gripIndex, a.x(), a.y())
    updatePath(normalPath)
    gripIndex = -1

QPainterPath PolygonObject::objectCopyPath()
    return normalPath

QPainterPath PolygonObject::objectSavePath()
    QPainterPath closedPath = normalPath
    closedPath.closeSubpath()
    s = scale()
    QTransform trans
    trans.rotate(rotation())
    trans.scale(s,s)
    return trans.map(closedPath)


class Polyline():
    r"""
    This is necessarily a class because we need the same
    functions for other geometry objects and supporting SVG means
    supporting every geometry object supported natively by it.
    
    We should be able to initialise using an existing one, maybe
    a copy() function?
    """
    def __init__(self, x, y, rgb="black", p=0, line_weight=0.35):
        r"""
        Needs to work with the libembroidery polyline, if that's wrapped
        in a class then this class extends that one and we call
        
        super().__init__()
        
        here.
        
        Some of the functions here can then be ported to libembroidery.
        """
        debug_message("Polyline.__init__()")
        self.x = x
        self.y = y
        self.path = p
        self.color = rgb
        self.line_type = "solid line"
        # Perhaps pen should be an object?
        self.pen = "solid line"
        self.rotation = 0.0
        self.scale = 1.0
        self.type = "polyline"
        self.selectable = 1
        self.grip_index = -1
        self.line_weight = line_weight
        self.updatePath(p)
        return self

    def updatePath(self, p):
        r"""
        This is a straight translation and I'm not sure what
        it's doing -- Robin
        """
        self.normal_path = p
        self.reverse_path = self.normal_path.reverse()
        self.reverse_path.connect(self.normal_path)
        self.path = self.reverse_path

    def paint(self, painter, option, widget):
        r"""
        """
        obj_scene = scene()
        if not obj_scene:
            return
        paintPen = pen()
        painter.pen = paintPen
        painter.updateRubber()

        if option.state & QStyle::State_Selected)   paintPen.setStyle(Qt::DashLine)
        if objScene.property("ENABLE_LWT").toBool())  paintPen = lineWeightPen()
        painter.setPen(paintPen)

        painter.drawPath(normalPath)

        if objScene.property("ENABLE_LWT").toBool() and objScene.property("ENABLE_REAL").toBool())  realRender(painter, normalPath)


    def PolyupdateRubber(QPainter* painter):
        int rubberMode = objectRubberMode()
        if rubberMode == OBJ_RUBBER_POLYLINE)

            setObjectPos(objectRubberPoint("POLYLINE_POINT_0"))

            QLineF rubberLine(normalPath.currentPosition(), mapFromScene(objectRubberPoint(QString())))
            if painter) drawRubberLine(rubberLine, painter, "VIEW_COLOR_CROSSHAIR")

            bool ok = 0
            QString numStr = objectRubberText("POLYLINE_NUM_POINTS")
            if numStr.isNull()) return
            int num = numStr.toInt(&ok)
            if !ok) return

            QString appendStr
            QPainterPath rubberPath
            for(int i = 1; i <= num; i++)
        
                appendStr = "POLYLINE_POINT_" + QString().setNum(i)
                appendPoint = mapFromScene(objectRubberPoint(appendStr))
                rubberPath.lineTo(appendPoint)

            updatePath(rubberPath)

            /*Ensure the path isn't updated until the number of points is changed again*/
            setObjectRubberText("POLYLINE_NUM_POINTS", QString())

        elif rubberMode == OBJ_RUBBER_GRIP)

            if painter:
                elemCount = normalPath.elementCount()
                gripPoint = objectRubberPoint("GRIP_POINT")
                if gripIndex == -1) gripIndex = findIndex(gripPoint)
                if gripIndex == -1) return

                if not gripIndex:
                    # First
                    QPainterPath::Element ef = normalPath.elementAt(1)
                    efPoint = QPointF(ef.x, ef.y)
                    painter.drawLine(efPoint, mapFromScene(objectRubberPoint(QString())))
        
                elif gripIndex == elemCount-1:
                    # Last
                    QPainterPath::Element el = normalPath.elementAt(gripIndex-1)
                    elPoint = QPointF(el.x, el.y)
                    painter.drawLine(elPoint, mapFromScene(objectRubberPoint(QString())))
        
                else:
                    # Middle
                    QPainterPath::Element em = normalPath.elementAt(gripIndex-1)
                    QPainterPath::Element en = normalPath.elementAt(gripIndex+1)
                    emPoint = QPointF(em.x, em.y)
                    enPoint = QPointF(en.x, en.y)
                    painter.drawLine(emPoint, mapFromScene(objectRubberPoint(QString())))
                    painter.drawLine(enPoint, mapFromScene(objectRubberPoint(QString())))
        

                QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
                drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")

    def vulcanize():
        debug_message("PolylineObject vulcanize()")
        updateRubber()

        setObjectRubberMode(OBJ_RUBBER_OFF)

        if not normalPath.elementCount():
            QMessageBox::critical(0, QObject::tr("Empty Polyline Error"), QObject::tr("The polyline added contains no points. The command that created this object has flawed logic."))

    /* Returns the closest snap point to the mouse point*/
    PolymouseSnapPoint(const QPointF& mousePoint):
        QPainterPath::Element element = normalPath.elementAt(0)
        closestPoint = mapToScene(QPointF(element.x, element.y))
        closestDist = QLineF(mousePoint, closestPoint).length()
        int elemCount = normalPath.elementCount()
        for(int i = 0; i < elemCount; ++i)

            element = normalPath.elementAt(i)
            elemPoint = mapToScene(element.x, element.y)
            elemDist = QLineF(mousePoint, elemPoint).length()
            if elemDist < closestDist)
        
                closestPoint = elemPoint
                closestDist = elemDist

        }
        return closestPoint

    QList<QPointF> PolyallGripPoints():
        QList<QPointF> gripPoints
        QPainterPath::Element element
        for(int i = 0; i < normalPath.elementCount(); ++i)

            element = normalPath.elementAt(i)
            gripPoints << mapToScene(element.x, element.y)
        }
        return gripPoints

    def PolyfindIndex(const QPointF& point):
        int elemCount = normalPath.elementCount()
        /*NOTE: Points here are in item coordinates*/
        itemPoint = mapFromScene(point)
        for (int i = 0; i < elemCount; i++) 
            QPainterPath::Element e = normalPath.elementAt(i)
            elemPoint = QPointF(e.x, e.y)
            if itemPoint == elemPoint) return i
        }
        return -1

    def PolygripEdit(const QPointF& before, const QPointF& after):
        gripIndex = findIndex(before)
        if gripIndex == -1) return
        a = mapFromScene(after)
        normalPath.setElementPositionAt(gripIndex, a.x(), a.y())
        updatePath(normalPath)
        gripIndex = -1

    QPainterPath PolyobjectCopyPath()
        return normalPath

    QPainterPath PolyobjectSavePath()
        s = scale()
        QTransform trans
        trans.rotate(rotation())
        trans.scale(s,s)
        return trans.map(normalPath)

class Rect():
    def __init__(self):
        return self

RectObject::RectObject(x, y, w, h, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("RectObject Constructor()")
    init(x, y, w, h, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

RectObject::RectObject(RectObject* obj, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("RectObject Constructor()")
    if obj)

        ptl = obj.objectTopLeft()
        init(ptl.x(), ptl.y(), obj.objectWidth(), obj.objectHeight(), obj.objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setRotation(obj.rotation())
    }
}

RectObject::~RectObject():
    debug_message("RectObject Destructor()")

def RectObject::init(x, y, w, h, unsigned int rgb, Qt::PenStyle lineType):
    setData(OBJ_TYPE, type())
    setData(OBJ_NAME, obj_names[OBJ_TYPE_RECTANGLE])

    setFlag(QGraphicsItem::ItemIsSelectable, 1)

    setObjectRect(x, y, w, h)
    setObjectColor(rgb)
    setObjectLineType(lineType)
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objectPen())

def RectObject::setObjectRect(x, y, w, h):
    setPos(x, y)
    setRect(0, 0, w, h)
    updatePath()

RectObject::objectTopLeft()
    EmbVector v
    v = to_emb_vector(rect().topLeft())
    v = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(v)

RectObject::objectTopRight()
    EmbVector v
    v = to_emb_vector(rect().topRight())
    v = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(v)

RectObject::objectBottomLeft()
    EmbVector v
    v = to_emb_vector(rect().bottomLeft())
    v = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(v)

RectObject::objectBottomRight()
    EmbVector v
    v = to_emb_vector(rect().bottomRight())
    v = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(v)

def RectObject::updatePath():
    QPainterPath path
    QRectF r = rect()
    path.moveTo(r.bottomLeft())
    path.lineTo(r.bottomRight())
    path.lineTo(r.topRight())
    path.lineTo(r.topLeft())
    path.lineTo(r.bottomLeft())
    /*NOTE: Reverse the path so that the inside area isn't considered part of the rectangle*/
    path.lineTo(r.topLeft())
    path.lineTo(r.topRight())
    path.lineTo(r.bottomRight())
    path.moveTo(r.bottomLeft())
    setObjectPath(path)

def RectObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
    QGraphicsScene* objScene = scene()
    if not objScene:
        return

    QPen paintPen = pen()
    painter.setPen(paintPen)
    updateRubber(painter)
    if option.state & QStyle::State_Selected)   paintPen.setStyle(Qt::DashLine)
    if objScene.property("ENABLE_LWT").toBool())  paintPen = lineWeightPen()
    painter.setPen(paintPen)

    painter.drawRect(rect())

def RectObject::updateRubber(painter):
    rubberMode = objectRubberMode()
    if rubberMode == OBJ_RUBBER_RECTANGLE:

        sceneStartPoint = objectRubberPoint("RECTANGLE_START")
        sceneEndPoint = objectRubberPoint("RECTANGLE_END")
        x = sceneStartPoint.x()
        y = sceneStartPoint.y()
        w = sceneEndPoint.x() - sceneStartPoint.x()
        h = sceneEndPoint.y() - sceneStartPoint.y()
        setObjectRect(x,y,w,h)
        updatePath()

    elif rubberMode == OBJ_RUBBER_GRIP:
        if painter:
            /* TODO: Make this work with rotation & scaling. */

            gripPoint = objectRubberPoint("GRIP_POINT")
            after = objectRubberPoint(QString())
            delta = after-gripPoint
            if gripPoint == objectTopLeft():
                painter.drawPolygon(mapFromScene(QRectF(after.x(), after.y(), objectWidth()-delta.x(), objectHeight()-delta.y())))
            elif gripPoint == objectTopRight():
                painter.drawPolygon(mapFromScene(QRectF(objectTopLeft().x(), objectTopLeft().y()+delta.y(), objectWidth()+delta.x(), objectHeight()-delta.y())))
            elif gripPoint == objectBottomLeft():
                painter.drawPolygon(mapFromScene(QRectF(objectTopLeft().x()+delta.x(), objectTopLeft().y(), objectWidth()-delta.x(), objectHeight()+delta.y())))
            elif gripPoint == objectBottomRight():
                painter.drawPolygon(mapFromScene(QRectF(objectTopLeft().x(), objectTopLeft().y(), objectWidth()+delta.x(), objectHeight()+delta.y())))

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")

            gripPoint = objectRubberPoint("GRIP_POINT")
            after = objectRubberPoint(QString())
            delta = after-gripPoint

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")

def RectObject::vulcanize():
    debug_message("RectObject vulcanize()")
    updateRubber()

    setObjectRubberMode(OBJ_RUBBER_OFF)

def RectObject::mouseSnapPoint(const QPointF& mousePoint):
    " Returns the closest snap point to the mouse point"
    ptl = objectTopLeft();     /*Top Left Corner QSnap*/
    ptr = objectTopRight();    /*Top Right Corner QSnap*/
    pbl = objectBottomLeft();  /*Bottom Left Corner QSnap*/
    pbr = objectBottomRight(); /*Bottom Right Corner QSnap*/

    ptlDist = QLineF(mousePoint, ptl).length()
    ptrDist = QLineF(mousePoint, ptr).length()
    pblDist = QLineF(mousePoint, pbl).length()
    pbrDist = QLineF(mousePoint, pbr).length()

    minDist = qMin(qMin(ptlDist, ptrDist), qMin(pblDist, pbrDist))

    if     (minDist == ptlDist) return ptl
    elif minDist == ptrDist) return ptr
    elif minDist == pblDist) return pbl
    elif minDist == pbrDist) return pbr

    return scenePos()

QList<QPointF> RectObject::allGripPoints():
    QList<QPointF> gripPoints
    gripPoints << objectTopLeft() << objectTopRight() << objectBottomLeft() << objectBottomRight()
    return gripPoints

def RectObject::gripEdit(const QPointF& before, const QPointF& after):
    delta = after-before
    if     (before == objectTopLeft())  setObjectRect(after.x(), after.y(), objectWidth()-delta.x(), objectHeight()-delta.y())
    elif before == objectTopRight()) setObjectRect(objectTopLeft().x(), objectTopLeft().y()+delta.y(), objectWidth()+delta.x(), objectHeight()-delta.y())
    elif before == objectBottomLeft())   setObjectRect(objectTopLeft().x()+delta.x(), objectTopLeft().y(), objectWidth()-delta.x(), objectHeight()+delta.y())
    elif before == objectBottomRight())  setObjectRect(objectTopLeft().x(), objectTopLeft().y(), objectWidth()+delta.x(), objectHeight()+delta.y())
}

QPainterPath RectObject::objectSavePath()
    QPainterPath path
    QRectF r = rect()
    path.moveTo(r.bottomLeft())
    path.lineTo(r.bottomRight())
    path.lineTo(r.topRight())
    path.lineTo(r.topLeft())
    path.lineTo(r.bottomLeft())

    s = scale()
    QTransform trans
    trans.rotate(rotation())
    trans.scale(s,s)
    return trans.map(path)


class TextSingle():
    def __init__(self):
        return self

TextSingleObject::TextSingleObject(const QString& str, x, y, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("TextSingleObject Constructor()")
    init(str, x, y, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

TextSingleObject::TextSingleObject(TextSingleObject* obj, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("TextSingleObject Constructor()")
    if obj:
        objTextFont = obj.objTextFont
        obj_text = obj.obj_text
        setRotation(obj.rotation())
        setObjectText(obj.objText)
        init(obj.objText, obj.objectX(), obj.objectY(), obj.objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setScale(obj.scale())

TextSingleObject::~TextSingleObject():
    debug_message("TextSingleObject Destructor()")

def TextSingleObject::init(const QString& str, x, y, unsigned int rgb, Qt::PenStyle lineType):
    setData(OBJ_TYPE, type())
    setData(OBJ_NAME, obj_names[OBJ_TYPE_TEXTSINGLE])

    setFlag(QGraphicsItem::ItemIsSelectable, 1)

    objTextJustify = "Left"; /*TODO: set the justification properly*/

    setObjectText(cmd)
    setObjectPos(x,y)
    setObjectColor(rgb)
    setObjectLineType(lineType)
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objectPen())

QStringList TextSingleObject::objectTextJustifyList()
    QStringList justifyList
    justifyList << "Left" << "Center" << "Right" /* TODO: << "Aligned" */ << "Middle" /* TODO: << "Fit" */ 
    justifyList << "Top Left" << "Top Center" << "Top Right"
    justifyList << "Middle Left" << "Middle Center" << "Middle Right"
    justifyList << "Bottom Left" << "Bottom Center" << "Bottom Right"
    return justifyList

def TextSingleObject::setObjectText(const QString& str):
    objText = str
    QPainterPath textPath
    QFont font
    font.setFamily(objTextFont)
    font.setPointSizeF(obj_text.size)
    font.setBold(obj_text.bold)
    font.setItalic(obj_text.italic)
    font.setUnderline(obj_text.underline)
    font.setStrikeOut(obj_text.strikeout)
    font.setOverline(obj_text.overline)
    textPath.addText(0, 0, font, str)

    /*Translate the path based on the justification*/
    QRectF jRect = textPath.boundingRect()
    if objTextJustify == "Left":
        textPath.translate(-jRect.left(), 0)
    elif objTextJustify == "Center":
        textPath.translate(-jRect.center().x(), 0)
    elif objTextJustify == "Right")      textPath.translate(-jRect.right(), 0)
    elif objTextJustify == "Aligned")    } /*TODO: TextSingleObject Aligned Justification*/
    elif objTextJustify == "Middle")     textPath.translate(-jRect.center())
    elif objTextJustify == "Fit") /*TODO: TextSingleObject Fit Justification*/
    elif objTextJustify == "Top Left")   textPath.translate(-jRect.topLeft())
    elif objTextJustify == "Top Center") textPath.translate(-jRect.center().x(), -jRect.top())
    elif objTextJustify == "Top Right")  textPath.translate(-jRect.topRight())
    elif objTextJustify == "Middle Left")    textPath.translate(-jRect.left(), -jRect.top()/2.0)
    elif objTextJustify == "Middle Center")  textPath.translate(-jRect.center().x(), -jRect.top()/2.0)
    elif objTextJustify == "Middle Right")   textPath.translate(-jRect.right(), -jRect.top()/2.0)
    elif objTextJustify == "Bottom Left")    textPath.translate(-jRect.bottomLeft())
    elif objTextJustify == "Bottom Center")  textPath.translate(-jRect.center().x(), -jRect.bottom())
    elif objTextJustify == "Bottom Right")   textPath.translate(-jRect.bottomRight())

    /*Backward or Upside Down*/
    if obj_text.backward || obj_text.upsidedown)

        horiz = 1.0
        vert = 1.0
        if obj_text.backward) horiz = -1.0
        if obj_text.upsidedown) vert = -1.0

        QPainterPath flippedPath

        QPainterPath::Element element
        QPainterPath::Element P2
        QPainterPath::Element P3
        QPainterPath::Element P4
        for(int i = 0; i < textPath.elementCount(); ++i)
    
            element = textPath.elementAt(i)
            if element.isMoveTo())
        
                flippedPath.moveTo(horiz * element.x, vert * element.y)
    
            elif element.isLineTo())
        
                flippedPath.lineTo(horiz * element.x, vert * element.y)
    
            elif element.isCurveTo())
        
                                              /* start point P1 is not needed*/
                P2 = textPath.elementAt(i);   /* control point*/
                P3 = textPath.elementAt(i+1); /* control point*/
                P4 = textPath.elementAt(i+2); /* end point*/

                flippedPath.cubicTo(horiz * P2.x, vert * P2.y,
                                    horiz * P3.x, vert * P3.y,
                                    horiz * P4.x, vert * P4.y)
    

        objTextPath = flippedPath
    }
    else
        objTextPath = textPath

    /*Add the grip point to the shape path*/
    QPainterPath gripPath = objTextPath
    gripPath.connectPath(objTextPath)
    gripPath.addRect(-0.00000001, -0.00000001, 0.00000002, 0.00000002)
    setObjectPath(gripPath)

def TextSingleObject::setObjectTextFont(const QString& font):
    objTextFont = font
    setObjectText(objText)

def TextSingleObject::setObjectTextJustify(const QString& justify):
    /*Verify the string is a valid option*/
    if justify == "Left":
        objTextJustify = justify
    elif justify == "Center":
        objTextJustify = justify
    elif justify == "Right")      objTextJustify = justify
    elif justify == "Aligned")    objTextJustify = justify
    elif justify == "Middle")     objTextJustify = justify
    elif justify == "Fit")        objTextJustify = justify
    elif justify == "Top Left")   objTextJustify = justify
    elif justify == "Top Center") objTextJustify = justify
    elif justify == "Top Right")  objTextJustify = justify
    elif justify == "Middle Left")    objTextJustify = justify
    elif justify == "Middle Center")  objTextJustify = justify
    elif justify == "Middle Right")   objTextJustify = justify
    elif justify == "Bottom Left")    objTextJustify = justify
    elif justify == "Bottom Center")  objTextJustify = justify
    elif justify == "Bottom Right")   objTextJustify = justify
    else                             objTextJustify = "Left";  } /*Default*/
    setObjectText(objText)

def TextSingleObject::setObjectTextSize(size):
    obj_text.size = size
    setObjectText(objText)

def TextSingleObject::setObjectTextBold(int val):
    obj_text.bold = val
    setObjectText(objText)

def TextSingleObject::setObjectTextItalic(int val):
    obj_text.italic = val
    setObjectText(objText)

def TextSingleObject::setObjectTextUnderline(int val):
    obj_text.underline = val
    setObjectText(objText)

def TextSingleObject::setObjectTextStrikeOut(int val):
    obj_text.strikeout = val
    setObjectText(objText)

def TextSingleObject::setObjectTextOverline(int val):
    obj_text.overline = val
    setObjectText(objText)

def TextSingleObject::setObjectTextBackward(int val):
    obj_text.backward = val
    setObjectText(objText)

def TextSingleObject::setObjectTextUpsideDown(int val):
    obj_text.upsidedown = val
    setObjectText(objText)

def TextSingleObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
    QGraphicsScene* objScene = scene()
    if !objScene) return

    QPen paintPen = pen()
    painter.setPen(paintPen)
    updateRubber(painter)
    if option.state & QStyle::State_Selected)   paintPen.setStyle(Qt::DashLine)
    if objScene.property("ENABLE_LWT").toBool())  paintPen = lineWeightPen()
    painter.setPen(paintPen)

    painter.drawPath(objTextPath)

def TextSingleObject::updateRubber(QPainter* painter):
    int rubberMode = objectRubberMode()
    if (rubberMode == OBJ_RUBBER_TEXTSINGLE) 
        setObjectTextFont(objectRubberText("TEXT_FONT"))
        setObjectTextJustify(objectRubberText("TEXT_JUSTIFY"))
        setObjectPos(objectRubberPoint("TEXT_POINT"))
        hr = objectRubberPoint("TEXT_HEIGHT_ROTATION")
        setObjectTextSize(hr.x())
        setRotation(hr.y())
        setObjectText(objectRubberText("TEXT_RAPID"))
    }
    elif rubberMode == OBJ_RUBBER_GRIP) 
        if (painter) 
            gripPoint = objectRubberPoint("GRIP_POINT")
            if (gripPoint == scenePos()) 
                painter.drawPath(objectPath().translated(mapFromScene(objectRubberPoint(QString()))-mapFromScene(gripPoint)))
    

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")

    }
}

def TextSingleObject::vulcanize():
    debug_message("TextSingleObject vulcanize()")
    updateRubber()

    setObjectRubberMode(OBJ_RUBBER_OFF)

def TextSingleObject::mouseSnapPoint(const QPointF& mousePoint):
    " Returns the closest snap point to the mouse point. "
    return scenePos()

def TextSingleObject::allGripPoints():
    QList<QPointF> gripPoints
    gripPoints << scenePos()
    return gripPoints

def TextSingleObject::gripEdit(before, after):
    if before == scenePos():
        delta = after-before
        moveBy(delta.x(), delta.y())

def TextSingleObject::subPathList():
    s = scale()
    QTransform trans
    trans.rotate(rotation())
    trans.scale(s,s)

    QList<QPainterPath> pathList

    QPainterPath path = objTextPath

    QPainterPath::Element element
    QList<int> pathMoves
    int numMoves = 0

    for(int i = 0; i < path.elementCount(); i++)

        element = path.elementAt(i)
        if element.isMoveTo())
    
            pathMoves << i
            numMoves++

    pathMoves << path.elementCount()

    for (int p = 0; p < pathMoves.size()-1 and p < numMoves; p++):
        for (int i = pathMoves.value(p); i < pathMoves.value(p+1); i++):
            element = path.elementAt(i)
            if (element.isMoveTo()) :
                subPath.moveTo(element.x, element.y)
    
            elif element.isLineTo()) :
                subPath.lineTo(element.x, element.y)
    
            elif element.isCurveTo():
                subPath.cubicTo(path.elementAt(i  ).x, path.elementAt(i  ).y, /*control point 1*/
                                path.elementAt(i+1).x, path.elementAt(i+1).y, /*control point 2*/
                                path.elementAt(i+2).x, path.elementAt(i+2).y); /*end point*/

        pathList.append(trans.map(subPath))

    return pathList

class Circle():
    def __init__(self):
        return self

CircleObject::CircleObject(centerX, centerY, radius, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("CircleObject Constructor()")
    init(centerX, centerY, radius, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

CircleObject::CircleObject(CircleObject* obj, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("CircleObject Constructor()")
    if obj)

        p = obj.objectCenter()
        r = obj.objectRadius()
        init(p.x(), p.y(), r, obj.objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setRotation(obj.rotation())
    }
}

CircleObject::~CircleObject():
    debug_message("CircleObject Destructor()")

def CircleObject::init(centerX, centerY, radius, unsigned int rgb, Qt::PenStyle lineType):
    setData(OBJ_TYPE, type())
    setData(OBJ_NAME, obj_names[OBJ_TYPE_CIRCLE])

    setFlag(QGraphicsItem::ItemIsSelectable, 1)

    setObjectRadius(radius)
    setPos(centerX, centerY)
    setObjectColor(rgb)
    setObjectLineType(lineType)
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objPen)
    updatePath()

def CircleObject::setObjectRadius(radius):
    setObjectDiameter(radius*2.0)

def CircleObject::setObjectDiameter(diameter):
    QRectF circRect
    circRect.setWidth(diameter)
    circRect.setHeight(diameter)
    circRect.moveCenter(QPointF(0,0))
    setRect(circRect)
    updatePath()

def CircleObject::setObjectArea(area):
    radius = sqrt(area/embConstantPi)
    setObjectRadius(radius)

def CircleObject::setObjectCircumference(circumference):
    diameter = circumference/embConstantPi
    setObjectDiameter(diameter)

def CircleObject::updatePath():
    QPainterPath path
    QRectF r = rect()
    /* Add the center point */
    path.addRect(-0.00000001, -0.00000001, 0.00000002, 0.00000002)
    /* Add the circle */
    path.arcMoveTo(r, 0)
    path.arcTo(r, 0, 360)
    /* NOTE: Reverse the path so that the inside area isn't considered part of the circle. */
    path.arcTo(r, 0, -360)
    setObjectPath(path)

def CircleObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
    QGraphicsScene* objScene = scene()
    if !objScene) return

    QPen paintPen = pen()
    painter.setPen(paintPen)
    updateRubber(painter)
    if option.state & QStyle::State_Selected)   paintPen.setStyle(Qt::DashLine)
    if objScene.property("ENABLE_LWT").toBool())  paintPen = lineWeightPen()
    painter.setPen(paintPen)

    painter.drawEllipse(rect())

def CircleObject::updateRubber(QPainter* painter):
    int rubberMode = objectRubberMode()
    if rubberMode == OBJ_RUBBER_CIRCLE_1P_RAD)

        sceneCenterPoint = objectRubberPoint("CIRCLE_CENTER")
        sceneQSnapPoint = objectRubberPoint("CIRCLE_RADIUS")
        itemCenterPoint = mapFromScene(sceneCenterPoint)
        itemQSnapPoint = mapFromScene(sceneQSnapPoint)
        QLineF itemLine(itemCenterPoint, itemQSnapPoint)
        setPos(sceneCenterPoint)
        QLineF sceneLine(sceneCenterPoint, sceneQSnapPoint)
        radius = sceneLine.length()
        setObjectRadius(radius)
        if painter) drawRubberLine(itemLine, painter, "VIEW_COLOR_CROSSHAIR")
        updatePath()
    }
    elif rubberMode == OBJ_RUBBER_CIRCLE_1P_DIA)

        sceneCenterPoint = objectRubberPoint("CIRCLE_CENTER")
        sceneQSnapPoint = objectRubberPoint("CIRCLE_DIAMETER")
        itemCenterPoint = mapFromScene(sceneCenterPoint)
        itemQSnapPoint = mapFromScene(sceneQSnapPoint)
        QLineF itemLine(itemCenterPoint, itemQSnapPoint)
        setPos(sceneCenterPoint)
        QLineF sceneLine(sceneCenterPoint, sceneQSnapPoint)
        diameter = sceneLine.length()
        setObjectDiameter(diameter)
        if painter) drawRubberLine(itemLine, painter, "VIEW_COLOR_CROSSHAIR")
        updatePath()
    }
    elif rubberMode == OBJ_RUBBER_CIRCLE_2P)

        sceneTan1Point = objectRubberPoint("CIRCLE_TAN1")
        sceneQSnapPoint = objectRubberPoint("CIRCLE_TAN2")
        QLineF sceneLine(sceneTan1Point, sceneQSnapPoint)
        setPos(sceneLine.pointAt(0.5))
        diameter = sceneLine.length()
        setObjectDiameter(diameter)
        updatePath()
    }
    elif rubberMode == OBJ_RUBBER_CIRCLE_3P)

        sceneTan1Point = objectRubberPoint("CIRCLE_TAN1")
        sceneTan2Point = objectRubberPoint("CIRCLE_TAN2")
        sceneTan3Point = objectRubberPoint("CIRCLE_TAN3")

        EmbVector sceneCenter
        EmbArc arc = embArcObject_make(sceneTan1Point.x(), sceneTan1Point.y(),
                             sceneTan2Point.x(), sceneTan2Point.y(),
                             sceneTan3Point.x(), sceneTan3Point.y()).arc
        getArcCenter(arc, &sceneCenter)
        sceneCenterPoint(sceneCenter.x, sceneCenter.y)
        QLineF sceneLine(sceneCenterPoint, sceneTan3Point)
        setPos(sceneCenterPoint)
        radius = sceneLine.length()
        setObjectRadius(radius)
        updatePath()
    }
    elif rubberMode == OBJ_RUBBER_GRIP)

        if painter)
    
            gripPoint = objectRubberPoint("GRIP_POINT")
            if gripPoint == objectCenter())
        
                painter.drawEllipse(rect().translated(mapFromScene(objectRubberPoint(QString()))-mapFromScene(gripPoint)))
    
            else
        
                gripRadius = QLineF(objectCenter(), objectRubberPoint(QString())).length()
                painter.drawEllipse(QPointF(), gripRadius, gripRadius)
    

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")

    }
}

def CircleObject::vulcanize():
    debug_message("CircleObject vulcanize()")
    updateRubber()

    setObjectRubberMode(OBJ_RUBBER_OFF)

/* Returns the closest snap point to the mouse point */
CircleObject::mouseSnapPoint(const QPointF& mousePoint):
    center = objectCenter()
    quad0 = objectQuadrant0()
    quad90 = objectQuadrant90()
    quad180 = objectQuadrant180()
    quad270 = objectQuadrant270()

    cntrDist = QLineF(mousePoint, center).length()
    q0Dist = QLineF(mousePoint, quad0).length()
    q90Dist = QLineF(mousePoint, quad90).length()
    q180Dist = QLineF(mousePoint, quad180).length()
    q270Dist = QLineF(mousePoint, quad270).length()

    minDist = qMin(qMin(qMin(q0Dist, q90Dist), qMin(q180Dist, q270Dist)), cntrDist)

    if     (minDist == cntrDist) return center
    elif minDist == q0Dist)   return quad0
    elif minDist == q90Dist)  return quad90
    elif minDist == q180Dist) return quad180
    elif minDist == q270Dist) return quad270

    return scenePos()

QList<QPointF> CircleObject::allGripPoints():
    QList<QPointF> gripPoints
    gripPoints << objectCenter() << objectQuadrant0() << objectQuadrant90() << objectQuadrant180() << objectQuadrant270()
    return gripPoints

def CircleObject::gripEdit(const QPointF& before, const QPointF& after):
    if before == objectCenter())  delta = after-before; moveBy(delta.x(), delta.y())
    else                      setObjectRadius(QLineF(objectCenter(), after).length())
}

QPainterPath CircleObject::objectSavePath()
    QPainterPath path
    QRectF r = rect()
    path.arcMoveTo(r, 0)
    path.arcTo(r, 0, 360)

    s = scale()
    QTransform trans
    trans.rotate(rotation())
    trans.scale(s,s)
    return trans.map(path)



class Circle():
    def __init__(self):
        " . "
        clearSelection()
        self.mode = "1P_RAD"
        self.x1 = MAX_DISTANCE+1.0
        self.y1 = MAX_DISTANCE+1.0
        self.x2 = MAX_DISTANCE+1.0
        self.y2 = MAX_DISTANCE+1.0
        self.x3 = MAX_DISTANCE+1.0
        self.y3 = MAX_DISTANCE+1.0
        setPromptPrefix(translate("Specify center point for circle or [3P/2P/Ttr (tan tan radius)]: "))
        return self

    def mouse_callback(self, button, state, x, y):
        if button==GLUT_LEFT_BUTTON:
            if state==GLUT_DOWN:
                pos_x = x/(0.5*window_width) - 1.0
                pos_y = -y/(0.5*window_height) + 1.0
                mouse_x = x
                mouse_y = y
                for (i=0; i<2; i++) 
                    widget *leaf = root.leaves[i]
                    if ((leaf.left < pos_x) and (pos_x < leaf.right))
                    if ((leaf.top < pos_y) and (pos_y < leaf.bottom)) 
                        action_id = i
                        break


def click(self, x, y):
    if self.mode == "1P_RAD":
        if isNaN(self.x1):
            self.x1 = x
            self.y1 = y
            self.cx = x
            self.cy = y
            addRubber("CIRCLE")
            setRubberMode("CIRCLE_1P_RAD")
            setRubberPoint("CIRCLE_CENTER", self.cx, self.cy)
            appendPromptHistory()
            setPromptPrefix(translate("Specify radius of circle or [Diameter]: "))
        else:
            self.x2 = x
            self.y2 = y
            setRubberPoint("CIRCLE_RADIUS", self.x2, self.y2)
            vulcanize()
            appendPromptHistory()
            return

    elif self.mode == "1P_DIA":
        if isNaN(self.x1):
            error("CIRCLE", translate("This should never happen."))
        else:
            self.x2 = x
            self.y2 = y
            setRubberPoint("CIRCLE_DIAMETER", self.x2, self.y2)
            vulcanize()
            appendPromptHistory()
            return

    elif self.mode == self.mode_2P) 
        if isNaN(self.x1)) 
            self.x1 = x
            self.y1 = y
            addRubber("CIRCLE")
            setRubberMode("CIRCLE_2P")
            setRubberPoint("CIRCLE_TAN1", self.x1, self.y1)
            appendPromptHistory()
            setPromptPrefix(translate("Specify second end point of circle's diameter: "))

        elif isNaN(self.x2)) 
            self.x2 = x
            self.y2 = y
            setRubberPoint("CIRCLE_TAN2", self.x2, self.y2)
            vulcanize()
            appendPromptHistory()
            return
        else:
            error("CIRCLE", translate("This should never happen."))

    elif self.mode == "3P":
        if isNaN(self.x1):
            self.x1 = x
            self.y1 = y
            appendPromptHistory()
            setPromptPrefix(translate("Specify second point on circle: "))
        elif isNaN(self.x2):
            self.x2 = x
            self.y2 = y
            addRubber("CIRCLE")
            setRubberMode("CIRCLE_3P")
            setRubberPoint("CIRCLE_TAN1", self.x1, self.y1)
            setRubberPoint("CIRCLE_TAN2", self.x2, self.y2)
            appendPromptHistory()
            setPromptPrefix(translate("Specify third point on circle: "))

        elif isNaN(self.x3)) 
            self.x3 = x
            self.y3 = y
            setRubberPoint("CIRCLE_TAN3", self.x3, self.y3)
            vulcanize()
            appendPromptHistory()
            return

        else 
            error("CIRCLE", translate("This should never happen."))

    elif self.mode == self.mode_TTR:
        if (isNaN(self.x1)) 
            self.x1 = x
            self.y1 = y
            appendPromptHistory()
            setPromptPrefix(translate("Specify point on object for second tangent of circle: "))

        elif (isNaN(self.x2)) 
            self.x2 = x
            self.y2 = y
            appendPromptHistory()
            setPromptPrefix(translate("Specify radius of circle: "))

        elif (isNaN(self.x3)) 
            self.x3 = x
            self.y3 = y
            appendPromptHistory()
            setPromptPrefix(translate("Specify second point: "))

        else 
            todo("CIRCLE", "click() for TTR")

    }
    return 0

def circle_prompt(circle_args args, char *str):
    if (self.mode == self.mode_1P_RAD) 
        if (isNaN(self.x1)) 
            # TODO: Probably should add additional qsTr calls here.
            if (!strcmp(str, "2P")) 
                self.mode = self.mode_2P
                setPromptPrefix(translate("Specify first end point of circle's diameter: "))
    
            # TODO: Probably should add additional qsTr calls here.
            elif (!strcmp(str, "3P")) 
                self.mode = self.mode_3P
                setPromptPrefix(translate("Specify first point of circle: "))
    
            # TODO: Probably should add additional qsTr calls here.
            elif (!strcmp(str, "T") or !strcmp(str, "TTR")) 
                self.mode = self.mode_TTR
                setPromptPrefix(translate("Specify point on object for first tangent of circle: "))
    
            else 
                strList = str.split(",")
                if (isNaN(strList[0]) or isNaN(strList[1])) 
                    alert(translate("Point or option keyword required."))
                    setPromptPrefix(translate("Specify center point for circle or [3P/2P/Ttr (tan tan radius)]: "))
        
                else 
                    self.x1 = Number(strList[0])
                    self.y1 = Number(strList[1])
                    self.cx = self.x1
                    self.cy = self.y1
                    addRubber("CIRCLE")
                    setRubberMode("CIRCLE_1P_RAD")
                    setRubberPoint("CIRCLE_CENTER", self.cx, self.cy)
                    setPromptPrefix(translate("Specify radius of circle or [Diameter]: "))

        else:
            # TODO: Probably should add additional qsTr calls here.
            if (!strcmp(str, "D") or !strcmp(str, "DIAMETER")) 
                self.mode = circle_mode_1P_DIA
                setRubberMode("CIRCLE_1P_DIA")
                setPromptPrefix(translate("Specify diameter of circle: "))
    
            else:
                num = Number(cmd)
                if (isNaN(num)) 
                    alert(translate("Requires numeric radius, point on circumference, or \"D\"."))
                    setPromptPrefix(translate("Specify radius of circle or [Diameter]: "))
        
                else 
                    self.rad = num
                    self.x2 = self.x1 + self.rad
                    self.y2 = self.y1
                    setRubberPoint("CIRCLE_RADIUS", self.x2, self.y2)
                    vulcanize()
                    return

    elif (self.mode == circle_mode_1P_DIA:
        if (isNaN(self.x1)) 
            error("CIRCLE", translate("This should never happen."))

        if (isNaN(self.x2)) 
            num = Number(cmd)
            if isNaN(num))
        
                alert(translate("Requires numeric distance or second point."))
                setPromptPrefix(translate("Specify diameter of circle: "))
    
            else
        
                self.dia = num
                self.x2 = self.x1 + self.dia
                self.y2 = self.y1
                setRubberPoint("CIRCLE_DIAMETER", self.x2, self.y2)
                vulcanize()
                return
        else:
            error("CIRCLE", translate("This should never happen."))

    elif self.mode == self.mode_2P:
        if isNaN(self.x1))
    
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1])):
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify first end point of circle's diameter: "))
            else:
                self.x1 = Number(strList[0])
                self.y1 = Number(strList[1])
                addRubber("CIRCLE")
                setRubberMode("CIRCLE_2P")
                setRubberPoint("CIRCLE_TAN1", self.x1, self.y1)
                setPromptPrefix(translate("Specify second end point of circle's diameter: "))
        elif isNaN(self.x2)):
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1]):
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify second end point of circle's diameter: "))
            else:
                self.x2 = Number(strList[0])
                self.y2 = Number(strList[1])
                setRubberPoint("CIRCLE_TAN2", self.x2, self.y2)
                vulcanize()
                return
        else:
            error("CIRCLE", translate("This should never happen."))

    elif self.mode == self.mode_3P):
        if isNaN(self.x1)):
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1])):
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify first point of circle: "))
            else:
                self.x1 = Number(strList[0])
                self.y1 = Number(strList[1])
                setPromptPrefix(translate("Specify second point of circle: "))

        elif isNaN(self.x2)):
    
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1]))
        
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify second point of circle: "))
    
            else
        
                self.x2 = Number(strList[0])
                self.y2 = Number(strList[1])
                addRubber("CIRCLE")
                setRubberMode("CIRCLE_3P")
                setRubberPoint("CIRCLE_TAN1", self.x1, self.y1)
                setRubberPoint("CIRCLE_TAN2", self.x2, self.y2)
                setPromptPrefix(translate("Specify third point of circle: "))
    

        elif isNaN(self.x3):
            strList = cmd.split(",")
            if isNaN(strList[0]) or isNaN(strList[1]):
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify third point of circle: "))
            else:
                self.x3 = Number(strList[0])
                self.y3 = Number(strList[1])
                setRubberPoint("CIRCLE_TAN3", self.x3, self.y3)
                vulcanize()
                return
        else:
            error("CIRCLE", translate("This should never happen."))

    elif self.mode == self.mode_TTR) 
        todo("CIRCLE", "prompt() for TTR")

    return 0

class line():
    def __init__(self):
        clearSelection()
        self.x1 = MAX_DISTANCE+1.0
        self.y1 = MAX_DISTANCE+1.0
        self.x2 = MAX_DISTANCE+1.0
        self.y2 = MAX_DISTANCE+1.0
        setPromptPrefix(translate("Specify first point: "))

    def click(self, x, y):
        if isNaN(self.x1):
            self.x1 = x
            self.y1 = y
            addRubber("LINE")
            setRubberMode("LINE")
            setRubberPoint("LINE_START", self.x1, self.y1)
            appendPromptHistory()
            setPromptPrefix(translate("Specify second point: "))
        else:
            appendPromptHistory()
            self.x2 = x
            self.y2 = y
            reportDistance()

    def prompt(self, cmd):
        strList = cmd.split(",")
        if isNaN(self.x1):
            if isNaN(strList[0]) or isNaN(strList[1]):
                alert(translate("Requires numeric distance or two points."))
                setPromptPrefix(translate("Specify first point: "))
            else:
                self.x1 = Number(strList[0])
                self.y1 = Number(strList[1])
                addRubber("LINE")
                setRubberMode("LINE")
                setRubberPoint("LINE_START", self.x1, self.y1)
                setPromptPrefix(translate("Specify second point: "))

        else:
            if isNaN(strList[0]) or isNaN(strList[1]):
                alert(translate("Requires numeric distance or two points."))
                setPromptPrefix(translate("Specify second point: "))
            else:
                self.x2 = Number(strList[0])
                self.y2 = Number(strList[1])
                reportDistance()

    def reportDistance(self):
        r"""
        Cartesian Coordinate System reported:

                 (+)
                 90
                 |
        (-) 180__|__0 (+)
                 |
                270
                (-)
        """
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1

        dist = calculateDistance(self.x1,self.y1,self.x2, self.y2)
        angle = calculateAngle(self.x1,self.y1,self.x2, self.y2)

        setPromptPrefix(translate("Distance") + " = " + dist.toString()
            + ", " + translate("Angle") + " = " + angle.toString())
        appendPromptHistory()
        setPromptPrefix(translate("Delta X") + " = " + dx.toString() + ", "
            + translate("Delta Y") + " = " + dy.toString())
        appendPromptHistory()


class Dolphin():
    def __init__(self):
        clearSelection()
        self.numPoints = 512
        # min:64 max:8192
        self.cx = MAX_DISTANCE+1.0
        self.cy = MAX_DISTANCE+1.0
        self.sx = 0.04
        self.sy = 0.04
        self.mode = "NUM_POINTS"

        addRubber("POLYGON")
        setRubberMode("POLYGON")
        self.update(self.numPoints, self.sx, self.sy)
        spareRubber("POLYGON")
        return self

    def basis_func(A, B, C, D, E):
        return (A/B)*math.sin(C*t+(D/E))

    def update(self, numPts, xScale, yScale):

        for i in range(numPts+1):
            t = (2*embConstantPi)/numPts*i;

            xx = self.basis_func(4, 23, -58, 62, 33)
            xx += (
        8/11*sin(10/9-56*t)+
        17/24*sin(38/35-55*t)+
        30/89*sin(81/23-54*t)+
        3/17*sin(53/18-53*t)+
        21/38*sin(29/19-52*t)+
        11/35*sin(103/40-51*t)+
        7/16*sin(79/18-50*t)+
        4/15*sin(270/77-49*t)+
        19/35*sin(59/27-48*t)+
        37/43*sin(71/17-47*t)+
        sin(18/43-45*t)+
        21/26*sin(37/26-44*t)+
        27/19*sin(111/32-42*t)+
        8/39*sin(13/25-41*t)+
        23/30*sin(27/8-40*t)+
        23/21*sin(32/35-37*t)+
        18/37*sin(91/31-36*t)+
        45/22*sin(29/37-35*t)+
        56/45*sin(11/8-33*t)+
        4/7*sin(32/19-32*t)+
        54/23*sin(74/29-31*t)+
        28/19*sin(125/33-30*t)+
        19/9*sin(73/27-29*t)+
        16/17*sin(737/736-28*t)+
        52/33*sin(130/29-27*t)+
        41/23*sin(43/30-25*t)+
        29/20*sin(67/26-24*t)+
        64/25*sin(136/29-23*t)+
        162/37*sin(59/34-21*t)+
        871/435*sin(199/51-20*t)+
        61/42*sin(58/17-19*t)+
        159/25*sin(77/31-17*t)+
        241/15*sin(94/31-13*t)+
        259/18*sin(114/91-12*t)+
        356/57*sin(23/25-11*t)+
        2283/137*sin(23/25-10*t)+
        1267/45*sin(139/42-9*t)+
        613/26*sin(41/23-8*t)+
        189/16*sin(122/47-6*t)+
        385/6*sin(151/41-5*t)+
        2551/38*sin(106/35-4*t)+
        1997/18*sin(6/5-2*t)+
        43357/47*sin(81/26-t)-
        4699/35*sin(3*t+25/31)-
        1029/34*sin(7*t+20/21)-
        250/17*sin(14*t+7/40)-
        140/17*sin(15*t+14/25)-
        194/29*sin(16*t+29/44)-
        277/52*sin(18*t+37/53)-
        94/41*sin(22*t+33/31)-
        57/28*sin(26*t+44/45)-
        128/61*sin(34*t+11/14)-
        111/95*sin(38*t+55/37)-
        85/71*sin(39*t+4/45)-
        25/29*sin(43*t+129/103)-
        7/37*sin(46*t+9/20)-
        17/32*sin(57*t+11/28)-
        5/16*sin(59*t+32/39))

            yy = (5/11*sin(163/37-59*t)+
        7/22*sin(19/41-58*t)+
        30/41*sin(1-57*t)+
        37/29*sin(137/57-56*t)+
        5/7*sin(17/6-55*t)+
        11/39*sin(46/45-52*t)+
        25/28*sin(116/83-51*t)+
        25/34*sin(11/20-47*t)+
        8/27*sin(81/41-46*t)+
        44/39*sin(78/37-45*t)+
        11/25*sin(107/37-44*t)+
        7/20*sin(7/16-41*t)+
        30/31*sin(19/5-40*t)+
        37/27*sin(148/59-39*t)+
        44/39*sin(17/27-38*t)+
        13/11*sin(7/11-37*t)+
        28/33*sin(119/39-36*t)+
        27/13*sin(244/81-35*t)+
        13/23*sin(113/27-34*t)+
        47/38*sin(127/32-33*t)+
        155/59*sin(173/45-29*t)+
        105/37*sin(22/43-27*t)+
        106/27*sin(23/37-26*t)+
        97/41*sin(53/29-25*t)+
        83/45*sin(109/31-24*t)+
        81/31*sin(96/29-23*t)+
        56/37*sin(29/10-22*t)+
        44/13*sin(29/19-19*t)+
        18/5*sin(34/31-18*t)+
        163/51*sin(75/17-17*t)+
        152/31*sin(61/18-16*t)+
        146/19*sin(47/20-15*t)+
        353/35*sin(55/48-14*t)+
        355/28*sin(102/25-12*t)+
        1259/63*sin(71/18-11*t)+
        17/35*sin(125/52-10*t)+
        786/23*sin(23/26-6*t)+
        2470/41*sin(77/30-5*t)+
        2329/47*sin(47/21-4*t)+
        2527/33*sin(23/14-3*t)+
        9931/33*sin(51/35-2*t)-
        11506/19*sin(t+56/67)-
        2081/42*sin(7*t+9/28)-
        537/14*sin(8*t+3/25)-
        278/29*sin(9*t+23/33)-
        107/15*sin(13*t+35/26)-
        56/19*sin(20*t+5/9)-
        5/9*sin(21*t+1/34)-
        17/24*sin(28*t+36/23)-
        21/11*sin(30*t+27/37)-
        138/83*sin(31*t+1/7)-
        10/17*sin(32*t+29/48)-
        31/63*sin(42*t+27/28)-
        4/27*sin(43*t+29/43)-
        13/24*sin(48*t+5/21)-
        4/7*sin(49*t+29/23)-
        26/77*sin(50*t+29/27)-
        19/14*sin(53*t+61/48)+
        34/25*sin(54*t+37/26))

            # setRubberPoint("POLYGON_POINT_" + i.toString(), xx*xScale, yy*yScale)

        setRubberText("POLYGON_NUM_POINTS", numPts.toString())
        return 0


class Ellipse():
    def __init__(self):
        clearSelection()
        self.mode = "MAJORDIAMETER_MINORRADIUS"
        self.point1 = [NaN, NaN]
        self.point2 = [NaN, NaN]
        self.point3 = [NaN, NaN]
        setPromptPrefix(translate("Specify first axis start point or [Center]: "))
        return args

    def click(self, point):
    if (self.mode == ELLIPSE_MAJORDIAMETER_MINORRADIUS) 
        if (isNaN(self.x1)) 
            self.point1 = point
            addRubber("ELLIPSE")
            setRubberMode("ELLIPSE_LINE")
            setRubberPoint("ELLIPSE_LINE_POINT1", self.x1, self.y1)
            appendPromptHistory()
            setPromptPrefix(translate("Specify first axis end point: "))

        elif isNaN(self.x2):
            self.point2 = point
            self.cx = (self.x1 + self.x2)/2.0
            self.cy = (self.y1 + self.y2)/2.0
            self.width = calculateDistance(self.x1, self.y1, self.x2, self.y2)
            self.rot = calculateAngle(self.x1, self.y1, self.x2, self.y2)
            setRubberMode("ELLIPSE_MAJORDIAMETER_MINORRADIUS")
            setRubberPoint("ELLIPSE_AXIS1_POINT1", self.x1, self.y1)
            setRubberPoint("ELLIPSE_AXIS1_POINT2", self.x2, self.y2)
            setRubberPoint("ELLIPSE_CENTER", self.cx, self.cy)
            setRubberPoint("ELLIPSE_WIDTH", self.width, 0)
            setRubberPoint("ELLIPSE_ROT", self.rot, 0)
            appendPromptHistory()
            setPromptPrefix(translate("Specify second axis end point or [Rotation]: "))

        elif isNaN(self.x3):
            self.x3 = x
            self.y3 = y
            self.height = perpendicularDistance(self.x3, self.y3, self.x1, self.y1, self.x2, self.y2)*2.0
            setRubberPoint("ELLIPSE_AXIS2_POINT2", self.x3, self.y3)
            vulcanize()
            appendPromptHistory()
            return

        else:
            error("ELLIPSE", translate("This should never happen."))

    elif self.mode == "MAJORRADIUS_MINORRADIUS":
        if (isNaN(self.x1)) 
            self.x1 = x
            self.y1 = y
            self.cx = self.x1
            self.cy = self.y1
            addRubber("ELLIPSE")
            setRubberMode("ELLIPSE_LINE")
            setRubberPoint("ELLIPSE_LINE_POINT1", self.x1, self.y1)
            setRubberPoint("ELLIPSE_CENTER", self.cx, self.cy)
            appendPromptHistory()
            setPromptPrefix(translate("Specify first axis end point: "))

        elif isNaN(self.x2)) 
            self.x2 = x
            self.y2 = y
            self.width = calculateDistance(self.cx, self.cy, self.x2, self.y2)*2.0
            self.rot = calculateAngle(self.x1, self.y1, self.x2, self.y2)
            setRubberMode("ELLIPSE_MAJORRADIUS_MINORRADIUS")
            setRubberPoint("ELLIPSE_AXIS1_POINT2", self.x2, self.y2)
            setRubberPoint("ELLIPSE_WIDTH", self.width, 0)
            setRubberPoint("ELLIPSE_ROT", self.rot, 0)
            appendPromptHistory()
            setPromptPrefix(translate("Specify second axis end point or [Rotation]: "))

        elif isNaN(self.x3)) 
            self.x3 = x
            self.y3 = y
            self.height = perpendicularDistance(self.x3, self.y3, self.cx, self.cy, self.x2, self.y2)*2.0
            setRubberPoint("ELLIPSE_AXIS2_POINT2", self.x3, self.y3)
            vulcanize()
            appendPromptHistory()
            return

        else:
            error("ELLIPSE", translate("This should never happen."))

    elif self.mode == self.mode_ELLIPSE_ROTATION) 
        if (isNaN(self.x1)) 
            error("ELLIPSE", translate("This should never happen."))

        elif (isNaN(self.x2)) 
            error("ELLIPSE", translate("This should never happen."))

        elif isNaN(self.x3)) 
            angle = calculateAngle(self.cx, self.cy, x, y)
            self.height = cos(angle*embConstantPi/180.0)*self.width
            addEllipse(self.cx, self.cy, self.width, self.height, self.rot, false)
            appendPromptHistory()
            return

def ellipse_prompt(cmd):
    if self.mode == "MAJORDIAMETER_MINORRADIUS":
        if isNaN(self.x1):
            if str == "C" or cmd == "CENTER":
                #TODO: Probably should add additional qsTr calls here.
                self.mode = self.mode_MAJORRADIUS_MINORRADIUS
                setPromptPrefix(translate("Specify center point: "))
            else:
                strList = str.split(",")
                if isNaN(strList[0]) or isNaN(strList[1]):
                    alert(translate("Point or option keyword required."))
                    setPromptPrefix(translate("Specify first axis start point or [Center]: "))
        
                else
            
                    self.x1 = Number(strList[0])
                    self.y1 = Number(strList[1])
                    addRubber("ELLIPSE")
                    setRubberMode("ELLIPSE_LINE")
                    setRubberPoint("ELLIPSE_LINE_POINT1", self.x1, self.y1)
                    setPromptPrefix(translate("Specify first axis end point: "))
        
    

        elif isNaN(self.x2):
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1]))
        
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify first axis end point: "))
    
            else
        
                self.x2 = Number(strList[0])
                self.y2 = Number(strList[1])
                self.cx = (self.x1 + self.x2)/2.0
                self.cy = (self.y1 + self.y2)/2.0
                self.width = calculateDistance(self.x1, self.y1, self.x2, self.y2)
                self.rot = calculateAngle(self.x1, self.y1, self.x2, self.y2)
                setRubberMode("ELLIPSE_MAJORDIAMETER_MINORRADIUS")
                setRubberPoint("ELLIPSE_AXIS1_POINT1", self.x1, self.y1)
                setRubberPoint("ELLIPSE_AXIS1_POINT2", self.x2, self.y2)
                setRubberPoint("ELLIPSE_CENTER", self.cx, self.cy)
                setRubberPoint("ELLIPSE_WIDTH", self.width, 0)
                setRubberPoint("ELLIPSE_ROT", self.rot, 0)
                setPromptPrefix(translate("Specify second axis end point or [Rotation]: "))

        elif isNaN(self.x3))
            if str == "R" or cmd == "ROTATION") #TODO: Probably should add additional qsTr calls here.
                self.mode = self.mode_ELLIPSE_ROTATION
                setPromptPrefix(translate("Specify rotation: "))
            else:
                strList = str.split(",")
                if isNaN(strList[0]) or isNaN(strList[1]))
            
                    alert(translate("Point or option keyword required."))
                    setPromptPrefix(translate("Specify second axis end point or [Rotation]: "))
        
                else
            
                    self.x3 = Number(strList[0])
                    self.y3 = Number(strList[1])
                    self.height = perpendicularDistance(self.x3, self.y3, self.x1, self.y1, self.x2, self.y2)*2.0
                    setRubberPoint("ELLIPSE_AXIS2_POINT2", self.x3, self.y3)
                    vulcanize()
                    return

    elif self.mode == self.mode_MAJORRADIUS_MINORRADIUS)
        if isNaN(self.x1))
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1])):
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify center point: "))
            else:
                self.x1 = Number(strList[0])
                self.y1 = Number(strList[1])
                self.cx = self.x1
                self.cy = self.y1
                addRubber("ELLIPSE")
                setRubberMode("ELLIPSE_LINE")
                setRubberPoint("ELLIPSE_LINE_POINT1", self.x1, self.y1)
                setRubberPoint("ELLIPSE_CENTER", self.cx, self.cy)
                setPromptPrefix(translate("Specify first axis end point: "))
        elif isNaN(self.x2)):
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1]))
        
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify first axis end point: "))
    
            else
        
                self.x2 = Number(strList[0])
                self.y2 = Number(strList[1])
                self.width = calculateDistance(self.x1, self.y1, self.x2, self.y2)*2.0
                self.rot = calculateAngle(self.x1, self.y1, self.x2, self.y2)
                setRubberMode("ELLIPSE_MAJORRADIUS_MINORRADIUS")
                setRubberPoint("ELLIPSE_AXIS1_POINT2", self.x2, self.y2)
                setRubberPoint("ELLIPSE_WIDTH", self.width, 0)
                setRubberPoint("ELLIPSE_ROT", self.rot, 0)
                setPromptPrefix(translate("Specify second axis end point or [Rotation]: "))

        elif isNaN(self.x3))
            if str == "R" or cmd == "ROTATION") #TODO: Probably should add additional qsTr calls here.
                self.mode = self.mode_ELLIPSE_ROTATION
                setPromptPrefix(translate("Specify ellipse rotation: "))
            else
                strList = str.split(",")
                if isNaN(strList[0]) or isNaN(strList[1]))
                    alert(translate("Point or option keyword required."))
                    setPromptPrefix(translate("Specify second axis end point or [Rotation]: "))
                else
                    self.x3 = Number(strList[0])
                    self.y3 = Number(strList[1])
                    self.height = perpendicularDistance(self.x3, self.y3, self.x1, self.y1, self.x2, self.y2)*2.0
                    setRubberPoint("ELLIPSE_AXIS2_POINT2", self.x3, self.y3)
                    vulcanize()
                    return

    elif self.mode == self.mode_ELLIPSE_ROTATION):
        if isNaN(self.x1)):
            error("ELLIPSE", translate("This should never happen."))
        elif isNaN(self.x2)):
            error("ELLIPSE", translate("This should never happen."))
        elif isNaN(self.x3)):
            if isNaN(cmd))
                alert(translate("Invalid angle. Input a numeric angle or pick a point."))
                setPromptPrefix(translate("Specify rotation: "))
            else:
                angle = Number(cmd)
                self.height = cos(angle*embConstantPi/180.0)*self.width
                addEllipse(self.cx, self.cy, self.width, self.height, self.rot, false)
                return

---

class Heart():
var global = }; #Required
self.numPoints = 512; #Default //TODO: min:64 max:8192
self.cx
self.cy
self.sx = 1.0
self.sy = 1.0
self.numPoints
self.mode

#enums
self.mode_NUM_POINTS = 0
self.mode_STYLE      = 1
self.mode_XSCALE     = 2
self.mode_YSCALE     = 3

def __init__(self):
    clearSelection()
    self.cx = MAX_DISTANCE+1.0
    self.cy = MAX_DISTANCE+1.0
    self.mode = self.mode_NUM_POINTS

    #Heart4: 10.0 / 512
    #Heart5: 1.0 / 512

    addRubber("POLYGON")
    setRubberMode("POLYGON")
    updateHeart("HEART5", self.numPoints, self.sx, self.sy)
    spareRubber("POLYGON")
    return

def updateHeart(style, numPts, xScale, yScale):
    i
    t
    xx = MAX_DISTANCE+1.0
    yy = MAX_DISTANCE+1.0
    two_pi = 2*embConstantPi

    for(i = 0; i <= numPts; i++)

        t = two_pi/numPts*i;

        if style == "HEART4")
    
            xx = cos(t)*((sin(t)*sqrt(abs(cos(t))))/(sin(t)+7/5) - 2*sin(t) + 2)
            yy = sin(t)*((sin(t)*sqrt(abs(cos(t))))/(sin(t)+7/5) - 2*sin(t) + 2)

        elif style == "HEART5")
    
            xx = 16*pow(sin(t), 3)
            yy = 13*cos(t) - 5*cos(2*t) - 2*cos(3*t) - cos(4*t)


        setRubberPoint("POLYGON_POINT_" + i.toString(), xx*xScale, yy*yScale)
    }

    setRubberText("POLYGON_NUM_POINTS", numPts.toString())

---


#Command: Line

var global = }; #Required
self.firstRun
self.firstX
self.firstY
self.prevX
self.prevY

def __init__(self):
    clearSelection()
    self.firstRun = true
    self.firstX = MAX_DISTANCE+1.0
    self.firstY = MAX_DISTANCE+1.0
    self.prevX = MAX_DISTANCE+1.0
    self.prevY = MAX_DISTANCE+1.0
    setPromptPrefix(translate("Specify first point: "))

def click(x, y):
    if self.firstRun)

        self.firstRun = false
        self.firstX = x
        self.firstY = y
        self.prevX = x
        self.prevY = y
        addRubber("LINE")
        setRubberMode("LINE")
        setRubberPoint("LINE_START", self.firstX, self.firstY)
        appendPromptHistory()
        setPromptPrefix(translate("Specify next point or [Undo]: "))
    }
    else

        setRubberPoint("LINE_END", x, y)
        vulcanize()
        addRubber("LINE")
        setRubberMode("LINE")
        setRubberPoint("LINE_START", x, y)
        appendPromptHistory()
        self.prevX = x
        self.prevY = y
    }
}

def prompt(cmd):
    if self.firstRun:
        strList = str.split(",")
        if isNaN(strList[0]) or isNaN(strList[1]):
            alert(translate("Invalid point."))
            setPromptPrefix(translate("Specify first point: "))
        else:
            self.firstRun = false
            self.firstX = Number(strList[0])
            self.firstY = Number(strList[1])
            self.prevX = self.firstX
            self.prevY = self.firstY
            addRubber("LINE")
            setRubberMode("LINE")
            setRubberPoint("LINE_START", self.firstX, self.firstY)
            setPromptPrefix(translate("Specify next point or [Undo]: "))
    else:
        if cmd == "U" or cmd == "UNDO":
            # TODO: Probably should add additional qsTr calls here.
            todo("LINE", "prompt() for UNDO")
        else:
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1]):
                alert(translate("Point or option keyword required."))
                setPromptPrefix(translate("Specify next point or [Undo]: "))
            else:
                x = Number(strList[0])
                y = Number(strList[1])
                setRubberPoint("LINE_END", x, y)
                vulcanize()
                addRubber("LINE")
                setRubberMode("LINE")
                setRubberPoint("LINE_START", x, y)
                self.prevX = x
                self.prevY = y
                setPromptPrefix(translate("Specify next point or [Undo]: "))

---

def __init__(self):
    clearSelection()
    setPromptPrefix(translate("Specify point: "))

def click(x, y):
    appendPromptHistory()
    setPromptPrefix("X = " + x.toString() + ", Y = " + y.toString())
    appendPromptHistory()

def prompt(cmd):
    strList = str.split(",")
    if isNaN(strList[0]) or isNaN(strList[1]):
        alert(translate("Invalid point."))
        setPromptPrefix(translate("Specify point: "))
    else:
        appendPromptHistory()
        setPromptPrefix("X = " + strList[0].toString() + ", Y = " + strList[1].toString())
        appendPromptHistory()

---

def __init__(self):
    self.firstRun = true
    self.baseX  = MAX_DISTANCE+1.0
    self.baseY  = MAX_DISTANCE+1.0
    self.destX  = MAX_DISTANCE+1.0
    self.destY  = MAX_DISTANCE+1.0
    self.deltaX = MAX_DISTANCE+1.0
    self.deltaY = MAX_DISTANCE+1.0

    if numSelected() <= 0:
        #TODO: Prompt to select objects if nothing is preselected
        alert(translate("Preselect objects before invoking the move command."))
        return
        messageBox("information", translate("Move Preselect"), translate("Preselect objects before invoking the move command."))
    else:
        setPromptPrefix(translate("Specify base point: "))

def click(x, y):
    if self.firstRun:
        self.firstRun = false
        self.baseX = x
        self.baseY = y
        addRubber("LINE")
        setRubberMode("LINE")
        setRubberPoint("LINE_START", self.baseX, self.baseY)
        previewOn("SELECTED", "MOVE", self.baseX, self.baseY, 0)
        appendPromptHistory()
        setPromptPrefix(translate("Specify destination point: "))
    else:
        self.destX = x
        self.destY = y
        self.deltaX = self.destX - self.baseX
        self.deltaY = self.destY - self.baseY
        moveSelected(self.deltaX, self.deltaY)
        previewOff()
        return


    def prompt(self, str):
        if self.firstRun:
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1])):
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify base point: "))
            else:
                self.firstRun = false
                self.baseX = Number(strList[0])
                self.baseY = Number(strList[1])
                addRubber("LINE")
                setRubberMode("LINE")
                setRubberPoint("LINE_START", self.baseX, self.baseY)
                previewOn("SELECTED", "MOVE", self.baseX, self.baseY, 0)
                setPromptPrefix(translate("Specify destination point: "))

        else:
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1])):
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify destination point: "))
            else:
                self.destX = Number(strList[0])
                self.destY = Number(strList[1])
                self.deltaX = self.destX - self.baseX
                self.deltaY = self.destY - self.baseY
                moveSelected(self.deltaX, self.deltaY)
                previewOff()
                return

---

#TODO: The path command is currently broken

var global = }; #Required
self.firstRun
self.firstX
self.firstY
self.prevX
self.prevY

def __init__(self):
    clearSelection()
    self.firstRun = true
    self.firstX = MAX_DISTANCE+1.0
    self.firstY = MAX_DISTANCE+1.0
    self.prevX = MAX_DISTANCE+1.0
    self.prevY = MAX_DISTANCE+1.0
    setPromptPrefix(translate("Specify start point: "))

def click(x, y):
    if self.firstRun:
        self.firstRun = false
        self.firstX = x
        self.firstY = y
        self.prevX = x
        self.prevY = y
        addPath(x,y)
        appendPromptHistory()
        setPromptPrefix(translate("Specify next point or [Arc/Undo]: "))
    else:
        appendPromptHistory()
        appendLineToPath(x,y)
        self.prevX = x
        self.prevY = y

def prompt(cmd):
    if str == "A" or cmd == "ARC")#TODO: Probably should add additional qsTr calls here.

        todo("PATH", "prompt() for ARC")
    }
    elif str == "U" or cmd == "UNDO") #TODO: Probably should add additional qsTr calls here.

        todo("PATH", "prompt() for UNDO")
    }
    else

        strList = str.split(",")
        if isNaN(strList[0]) or isNaN(strList[1]))
    
            alert(translate("Point or option keyword required."))
            setPromptPrefix(translate("Specify next point or [Arc/Undo]: "))

        else
    
            x = Number(strList[0])
            y = Number(strList[1])
            if self.firstRun)
        
                self.firstRun = false
                self.firstX = x
                self.firstY = y
                self.prevX = x
                self.prevY = y
                addPath(x,y)
                setPromptPrefix(translate("Specify next point or [Arc/Undo]: "))
            else
                appendLineToPath(x,y)
                self.prevX = x
                self.prevY = y


def __init__(self):
    clearSelection()
    reportPlatform()
    return

def reportPlatform():
    setPromptPrefix(translate("Platform") + " = " + platformString())
    appendPromptHistory()

# -------

class Point():
    def __init__(self):
        " TODO: translate needed here when complete. "
        clearSelection()
        self.firstRun = True
        setPromptPrefix("TODO: Current point settings: PDMODE=?  PDSIZE=?")
        appendPromptHistory()
        setPromptPrefix(translate("Specify first point: "))
        return self

    def click(self, x, y):
        if self.firstRun:
            self.firstRun = False
            appendPromptHistory()
            setPromptPrefix(translate("Specify next point: "))
            addPoint(x,y)
        else:
            appendPromptHistory()
            addPoint(x,y)

def prompt(self, str):
    if self.firstRun:
        if str == "M" or cmd == "MODE") 
            #TODO: Probably should add additional qsTr calls here.
            todo("POINT", "prompt() for PDMODE")

        elif str == "S" or cmd == "SIZE") 
            #TODO: Probably should add additional qsTr calls here.
            todo("POINT", "prompt() for PDSIZE")

        strList = str.split(",")
        if isNaN(strList[0]) or isNaN(strList[1]):
            alert(translate("Invalid point."))
            setPromptPrefix(translate("Specify first point: "))
        else:
            self.firstRun = false
            x = Number(strList[0])
            y = Number(strList[1])
            setPromptPrefix(translate("Specify next point: "))
            addPoint(x,y)

    else:
        strList = str.split(",")
        if isNaN(strList[0]) or isNaN(strList[1]):
            alert(translate("Invalid point."))
            setPromptPrefix(translate("Specify next point: "))
        else:
            x = Number(strList[0])
            y = Number(strList[1])
            setPromptPrefix(translate("Specify next point: "))
            addPoint(x,y)


class Polygon():
    r"""
    
    """
    def __init__(self):
        clearSelection()
        self.center.x = MAX_DISTANCE+1.0
        self.center.y = MAX_DISTANCE+1.0
        self.sideX1  = MAX_DISTANCE+1.0
        self.sideY1  = MAX_DISTANCE+1.0
        self.sideX2  = MAX_DISTANCE+1.0
        self.sideY2  = MAX_DISTANCE+1.0
        self.pointIX = MAX_DISTANCE+1.0
        self.pointIY = MAX_DISTANCE+1.0
        self.pointCX = MAX_DISTANCE+1.0
        self.pointCY = MAX_DISTANCE+1.0
        self.polyType = "Inscribed"
        self.numSides = 4
        self.mode = "NUM_SIDES"
        setPromptPrefix(translate("Enter number of sides")
            + " " + self.numSides.toString() + "}: ")
        return self

    def click(self, x, y):
        if self.mode == "NUM_SIDES":
            #Do nothing, the prompt controls this.

        elif self.mode == "CENTER_PT":
            self.centerX = x
            self.centerY = y
            self.mode = self.mode_POLYTYPE
            appendPromptHistory()
            setPromptPrefix(translate("Specify polygon type [Inscribed in circle/Circumscribed around circle]") + " " + self.polyType + "}: ")

        elif self.mode == "POLYTYPE":
            #Do nothing, the prompt controls this.

        elif self.mode == "INSCRIBE":
            self.pointIX = x
            self.pointIY = y
            setRubberPoint("POLYGON_INSCRIBE_POINT", self.pointIX, self.pointIY)
            vulcanize()
            appendPromptHistory()
            return

        elif self.mode == "CIRCUMSCRIBE":
            self.pointCX = x
            self.pointCY = y
            setRubberPoint("POLYGON_CIRCUMSCRIBE_POINT", self.pointCX, self.pointCY)
            vulcanize()
            appendPromptHistory()
            return

        elif self.mode == "DISTANCE":
            # Do nothing, the prompt controls this.
            debug_message("mode DISTANCE")

        elif self.mode == "SIDE_LEN":
            todo("POLYGON", "Sidelength mode")
            debug_message("mode SIDE LEN")

def prompt(cmd):
    if self.mode == self.mode_NUM_SIDES:
        if str == "" and self.numSides >= 3 and self.numSides <= 1024)
    
            setPromptPrefix(translate("Specify center point or [Sidelength]: "))
            self.mode = self.mode_CENTER_PT

        else
    
            tmp = Number(cmd)
            if isNaN(tmp) or !isInt(tmp) or tmp < 3 or tmp > 1024)
        
                alert(translate("Requires an integer between 3 and 1024."))
                setPromptPrefix(translate("Enter number of sides") + " " + self.numSides.toString() + "}: ")
    
            else
        
                self.numSides = tmp
                setPromptPrefix(translate("Specify center point or [Sidelength]: "))
                self.mode = self.mode_CENTER_PT

    elif self.mode == self.mode_CENTER_PT:
        if str == "S" or cmd == "SIDELENGTH") #TODO: Probably should add additional qsTr calls here.
    
            self.mode = self.mode_SIDE_LEN
            setPromptPrefix(translate("Specify start point: "))

        else
    
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1]))
        
                alert(translate("Point or option keyword required."))
                setPromptPrefix(translate("Specify center point or [Sidelength]: "))
    
            else
        
                self.centerX = Number(strList[0])
                self.centerY = Number(strList[1])
                self.mode = self.mode_POLYTYPE
                setPromptPrefix(translate("Specify polygon type [Inscribed in circle/Circumscribed around circle]") + " " + self.polyType + "}: ")

    elif self.mode == "POLYTYPE":
        if cmd == "INSCRIBED"[len(cmd)]:
            # TODO: Probably should add additional translate calls here.
            self.mode = self.mode_INSCRIBE
            self.polyType = "Inscribed"
            setPromptPrefix(translate("Specify polygon corner point or [Distance]: "))
            addRubber("POLYGON")
            setRubberMode("POLYGON_INSCRIBE")
            setRubberPoint("POLYGON_CENTER", self.centerX, self.centerY)
            setRubberPoint("POLYGON_NUM_SIDES", self.numSides, 0)

        elif cmd == "CIRCUMSCRIBED"[len(cmd)]:
            # TODO: Probably should add additional translate calls here.
            self.mode = self.mode_CIRCUMSCRIBE
            self.polyType = "Circumscribed"
            setPromptPrefix(translate("Specify polygon side point or [Distance]: "))
            addRubber("POLYGON")
            setRubberMode("POLYGON_CIRCUMSCRIBE")
            setRubberPoint("POLYGON_CENTER", self.centerX, self.centerY)
            setRubberPoint("POLYGON_NUM_SIDES", self.numSides, 0)

        elif str == "")
    
            if self.polyType == "Inscribed")
        
                self.mode = self.mode_INSCRIBE
                setPromptPrefix(translate("Specify polygon corner point or [Distance]: "))
                addRubber("POLYGON")
                setRubberMode("POLYGON_INSCRIBE")
                setRubberPoint("POLYGON_CENTER", self.centerX, self.centerY)
                setRubberPoint("POLYGON_NUM_SIDES", self.numSides, 0)
    
            elif self.polyType == "Circumscribed")
        
                self.mode = self.mode_CIRCUMSCRIBE
                setPromptPrefix(translate("Specify polygon side point or [Distance]: "))
                addRubber("POLYGON")
                setRubberMode("POLYGON_CIRCUMSCRIBE")
                setRubberPoint("POLYGON_CENTER", self.centerX, self.centerY)
                setRubberPoint("POLYGON_NUM_SIDES", self.numSides, 0)
    
            else
        
                error("POLYGON", translate("Polygon type is not Inscribed or Circumscribed."))
    

        else
    
            alert(translate("Invalid option keyword."))
            setPromptPrefix(translate("Specify polygon type [Inscribed in circle/Circumscribed around circle]") + " " + self.polyType + "}: ")

    elif self.mode == self.mode_INSCRIBE):
        if str == "D" or cmd == "DISTANCE") #TODO: Probably should add additional qsTr calls here.
    
            self.mode = self.mode_DISTANCE
            setPromptPrefix(translate("Specify distance: "))

        else
    
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1]))
        
                alert(translate("Point or option keyword required."))
                setPromptPrefix(translate("Specify polygon corner point or [Distance]: "))
    
            else
        
                self.pointIX = Number(strList[0])
                self.pointIY = Number(strList[1])
                setRubberPoint("POLYGON_INSCRIBE_POINT", self.pointIX, self.pointIY)
                vulcanize()
                return

    elif self.mode == "CIRCUMSCRIBE":
        if cmd == "D" or cmd == "DISTANCE":
            # TODO: Probably should add additional qsTr calls here.
            self.mode = self.mode_DISTANCE
            setPromptPrefix(translate("Specify distance: "))
        else:
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1]))
        
                alert(translate("Point or option keyword required."))
                setPromptPrefix(translate("Specify polygon side point or [Distance]: "))
    
            else:
                self.pointCX = Number(strList[0])
                self.pointCY = Number(strList[1])
                setRubberPoint("POLYGON_CIRCUMSCRIBE_POINT", self.pointCX, self.pointCY)
                vulcanize()
                return

    elif self.mode == self.mode_DISTANCE):
        if isNaN(cmd)):
            alert(translate("Requires valid numeric distance."))
            setPromptPrefix(translate("Specify distance: "))
        else:
            if self.polyType == "Inscribed")
        
                self.pointIX = self.centerX
                self.pointIY = self.centerY + Number(cmd)
                setRubberPoint("POLYGON_INSCRIBE_POINT", self.pointIX, self.pointIY)
                vulcanize()
                return
    
            elif self.polyType == "Circumscribed"):
                self.pointCX = self.centerX
                self.pointCY = self.centerY + Number(cmd)
                setRubberPoint("POLYGON_CIRCUMSCRIBE_POINT", self.pointCX, self.pointCY)
                vulcanize()
                return
            else:
                error("POLYGON", translate("Polygon type is not Inscribed or Circumscribed."))

    elif self.mode == self.mode_SIDE_LEN):
        todo("POLYGON", "Sidelength mode")

---

class Polyline():
    def __init__(self):
        clearSelection()
        self.firstRun = True
        self.firstX = MAX_DISTANCE+1.0
        self.firstY = MAX_DISTANCE+1.0
        self.prevX = MAX_DISTANCE+1.0
        self.prevY = MAX_DISTANCE+1.0
        self.num = 0
        setPromptPrefix(translate("Specify first point: "))

    def click(self, x, y):
        if self.firstRun):
            self.firstRun = false
            self.firstX = x
            self.firstY = y
            self.prevX = x
            self.prevY = y
            addRubber("POLYLINE")
            setRubberMode("POLYLINE")
            setRubberPoint("POLYLINE_POINT_0", self.firstX, self.firstY)
            appendPromptHistory()
            setPromptPrefix(translate("Specify next point or [Undo]: "))
        else:
            self.num += 1
            setRubberPoint("POLYLINE_POINT_" + self.num.toString(), x, y)
            setRubberText("POLYLINE_NUM_POINTS", self.num.toString())
            spareRubber("POLYLINE")
            appendPromptHistory()
            self.prevX = x
            self.prevY = y

    def prompt(self, str):
        if self.firstRun:
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1]):
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify first point: "))
            else:
                self.firstRun = false
                self.firstX = Number(strList[0])
                self.firstY = Number(strList[1])
                self.prevX = self.firstX
                self.prevY = self.firstY
                addRubber("POLYLINE")
                setRubberMode("POLYLINE")
                setRubberPoint("POLYLINE_POINT_0", self.firstX, self.firstY)
                setPromptPrefix(translate("Specify next point or [Undo]: "))

        else:
            if cmd == "U" or cmd == "UNDO":
                #TODO: Probably should add additional qsTr calls here.
                todo("POLYLINE", "prompt() for UNDO")
            else:
                strList = str.split(",")
                if isNaN(strList[0]) or isNaN(strList[1]):
                    alert(translate("Point or option keyword required."))
                    setPromptPrefix(translate("Specify next point or [Undo]: "))
                else:
                    x = Number(strList[0])
                    y = Number(strList[1])
                    self.num++
                    setRubberPoint("POLYLINE_POINT_" + self.num.toString(), x, y)    
                    setRubberText("POLYLINE_NUM_POINTS", self.num.toString())
                    spareRubber("POLYLINE")
                    self.prevX = x
                    self.prevY = y
                    setPromptPrefix(translate("Specify next point or [Undo]: "))

---

class DimLeader():
    " TODO: Adding the text is not complete yet. "

    def __init__(self):
        clearSelection()
        self.x1 = MAX_DISTANCE+1.0
        self.y1 = MAX_DISTANCE+1.0
        self.x2 = MAX_DISTANCE+1.0
        self.y2 = MAX_DISTANCE+1.0
        setPromptPrefix(translate("Specify first point: "))
        return self

    def click(self, x, y):
        if isNaN(self.x1):
            self.x1 = x
            self.y1 = y
            addRubber("DIMLEADER")
            setRubberMode("DIMLEADER_LINE")
            setRubberPoint("DIMLEADER_LINE_START", self.x1, self.y1)
            appendPromptHistory()
            setPromptPrefix(translate("Specify second point: "))
        else:
            self.x2 = x
            self.y2 = y
            setRubberPoint("DIMLEADER_LINE_END", self.x2, self.y2)
            vulcanize()
            appendPromptHistory()

    def prompt(cmd):
        strList = str.split(",")
        if isNaN(self.x1))

        if isNaN(strList[0]) or isNaN(strList[1]))
    
            alert(translate("Requires two points."))
            setPromptPrefix(translate("Specify first point: "))

        else:
            self.x1 = Number(strList[0])
            self.y1 = Number(strList[1])
            addRubber("DIMLEADER")
            setRubberMode("DIMLEADER_LINE")
            setRubberPoint("DIMLEADER_LINE_START", self.x1, self.y1)
            setPromptPrefix(translate("Specify second point: "))

    else:
        if isNaN(strList[0]) or isNaN(strList[1]):
            alert(translate("Requires two points."))
            setPromptPrefix(translate("Specify second point: "))
        else:
            self.x2 = Number(strList[0])
            self.y2 = Number(strList[1])
            setRubberPoint("DIMLEADER_LINE_END", self.x2, self.y2)
            vulcanize()
            return

---

var global = }; #Required
self.newRect
self.x1
self.y1
self.x2
self.y2

def __init__(self):
    clearSelection()
    self.newRect = true
    self.x1 = MAX_DISTANCE+1.0
    self.y1 = MAX_DISTANCE+1.0
    self.x2 = MAX_DISTANCE+1.0
    self.y2 = MAX_DISTANCE+1.0
    setPromptPrefix(translate("Specify first corner point or [Chamfer/Fillet]: "))

def click(self, x, y):
    if self.newRect:
        self.newRect = false
        self.x1 = x
        self.y1 = y
        addRubber("RECTANGLE")
        setRubberMode("RECTANGLE")
        setRubberPoint("RECTANGLE_START", x, y)
        setPromptPrefix(translate("Specify other corner point or [Dimensions]: "))
    else:
        self.newRect = true
        self.x2 = x
        self.y2 = y
        setRubberPoint("RECTANGLE_END", x, y)
        vulcanize()
        return

def prompt(self, cmd):
    if cmd == "C" or cmd == "CHAMFER":
        # TODO: Probably should add additional qsTr calls here.
        todo("RECTANGLE", "prompt() for CHAMFER")
    elif cmd == "D" or cmd == "DIMENSIONS":
        # TODO: Probably should add additional qsTr calls here.
        todo("RECTANGLE", "prompt() for DIMENSIONS")
    elif cmd == "F" or cmd == "FILLET":
        # TODO: Probably should add additional qsTr calls here.
        todo("RECTANGLE", "prompt() for FILLET")
    else:
        strList = str.split(",")
        if isNaN(strList[0]) or isNaN(strList[1]):
            alert(translate("Invalid point."))
            setPromptPrefix(translate("Specify first point: "))
        else:
            x = Number(strList[0])
            y = Number(strList[1])
            if self.newRect:
                self.newRect = false
                self.x1 = x
                self.y1 = y
                addRubber("RECTANGLE")
                setRubberMode("RECTANGLE")
                setRubberPoint("RECTANGLE_START", x, y)
                setPromptPrefix(translate("Specify other corner point or [Dimensions]: "))
            else:
                self.newRect = true
                self.x2 = x
                self.y2 = y
                setRubberPoint("RECTANGLE_END", x, y)
                vulcanize()
                return

----

var global = }; #Required
self.mode

#enums
self.mode_BACKGROUND = 0
self.mode_CROSSHAIR  = 1
self.mode_GRID       = 2

def __init__(self):
    clearSelection()
    self.mode = self.mode_BACKGROUND
    setPromptPrefix(translate("Enter RED,GREEN,BLUE values for background or [Crosshair/Grid]: "))

def prompt(cmd):
    if self.mode == self.mode_BACKGROUND:
        if str == "C" or cmd == "CROSSHAIR":
            # TODO: Probably should add additional qsTr calls here.
            self.mode = self.mode_CROSSHAIR
            setPromptPrefix(translate("Specify crosshair color: "))
        elif str == "G" or cmd == "GRID":
            #TODO: Probably should add additional qsTr calls here.
            self.mode = self.mode_GRID
            setPromptPrefix(translate("Specify grid color: "))
        else:
            strList = str.split(",")
            r = Number(strList[0])
            g = Number(strList[1])
            b = Number(strList[2])
            if !validRGB(r,g,b))
        
                alert(translate("Invalid color. R,G,B values must be in the range of 0-255."))
                setPromptPrefix(translate("Specify background color: "))
    
            else
        
                setBackgroundColor(r,g,b)
                return

    elif self.mode == "CROSSHAIR":
        strList = str.split(",")
        r = Number(strList[0])
        g = Number(strList[1])
        b = Number(strList[2])
        if not validRGB(r,g,b):
            alert(translate("Invalid color. R,G,B values must be in the range of 0-255."))
            setPromptPrefix(translate("Specify crosshair color: "))
        else:
            setCrossHairColor(r,g,b)
            return

    elif self.mode == "GRID":
        strList = str.split(",")
        r = Number(strList[0])
        g = Number(strList[1])
        b = Number(strList[2])
        if not validRGB(r,g,b):
            alert(translate("Invalid color. R,G,B values must be in the range of 0-255."))
            setPromptPrefix(translate("Specify grid color: "))
        else:
            setGridColor(r,g,b)
            return


def validRGB(r, g, b):
    if isNaN(r): return False
    if isNaN(g): return False
    if isNaN(b): return False
    if r < 0 or r > 255: return False
    if g < 0 or g > 255: return False
    if b < 0 or b > 255: return False
    return True

---

def __init__(self):
    self.mode = "NORMAL"
    self.modes = ["NORMAL", "REFERENCE"]
    self.firstRun = true
    self.baseX = MAX_DISTANCE+1.0
    self.baseY = MAX_DISTANCE+1.0
    self.destX = MAX_DISTANCE+1.0
    self.destY = MAX_DISTANCE+1.0
    self.angle = MAX_DISTANCE+1.0

    self.baseRX   = MAX_DISTANCE+1.0
    self.baseRY   = MAX_DISTANCE+1.0
    self.destRX   = MAX_DISTANCE+1.0
    self.destRY   = MAX_DISTANCE+1.0
    self.angleRef = MAX_DISTANCE+1.0
    self.angleNew = MAX_DISTANCE+1.0

    if numSelected() <= 0)

        #TODO: Prompt to select objects if nothing is preselected
        alert(translate("Preselect objects before invoking the rotate command."))
        return
        messageBox("information", translate("Rotate Preselect"), translate("Preselect objects before invoking the rotate command."))
    }
    else

        setPromptPrefix(translate("Specify base point: "))
    }

def click(x, y):
    if self.mode == "NORMAL":
        if self.firstRun:
            self.firstRun = False
            self.baseX = x
            self.baseY = y
            addRubber("LINE")
            setRubberMode("LINE")
            setRubberPoint("LINE_START", self.baseX, self.baseY)
            previewOn("SELECTED", "ROTATE", self.baseX, self.baseY, 0)
            appendPromptHistory()
            setPromptPrefix(translate("Specify rotation angle or [Reference]: "))
        else:
            self.destX = x
            self.destY = y
            self.angle = calculateAngle(self.baseX, self.baseY, self.destX, self.destY)
            appendPromptHistory()
            rotateSelected(self.baseX, self.baseY, self.angle)
            previewOff()
            return

    elif self.mode == "REFERENCE":
        if isNaN(self.baseRX))
            self.baseRX = x
            self.baseRY = y
            appendPromptHistory()
            addRubber("LINE")
            setRubberMode("LINE")
            setRubberPoint("LINE_START", self.baseRX, self.baseRY)
            setPromptPrefix(translate("Specify second point: "))
        elif isNaN(self.destRX))
            self.destRX = x
            self.destRY = y
            self.angleRef = calculateAngle(self.baseRX, self.baseRY, self.destRX, self.destRY)
            setRubberPoint("LINE_START", self.baseX, self.baseY)
            previewOn("SELECTED", "ROTATE", self.baseX, self.baseY, self.angleRef)
            appendPromptHistory()
            setPromptPrefix(translate("Specify the new angle: "))

        elif isNaN(self.angleNew))
    
            self.angleNew = calculateAngle(self.baseX, self.baseY, x, y)
            rotateSelected(self.baseX, self.baseY, self.angleNew - self.angleRef)
            previewOff()
            return

def prompt(cmd):
    if self.mode == self.mode_NORMAL:
        if self.firstRun:
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1]):
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify base point: "))
            else:
                self.firstRun = false
                self.baseX = Number(strList[0])
                self.baseY = Number(strList[1])
                addRubber("LINE")
                setRubberMode("LINE")
                setRubberPoint("LINE_START", self.baseX, self.baseY)
                previewOn("SELECTED", "ROTATE", self.baseX, self.baseY, 0)
                setPromptPrefix(translate("Specify rotation angle or [Reference]: "))

        else:
            if str == "R" or cmd == "REFERENCE"):
                # TODO: Probably should add additional qsTr calls here.
                self.mode = self.mode_REFERENCE
                setPromptPrefix(translate("Specify the reference angle") + " 0.00}: ")
                clearRubber()
                previewOff()
            else:
                if isNaN(cmd):
                    alert(translate("Requires valid numeric angle, second point, or option keyword."))
                    setPromptPrefix(translate("Specify rotation angle or [Reference]: "))
                else:
                    self.angle = Number(cmd)
                    rotateSelected(self.baseX, self.baseY, self.angle)
                    previewOff()
                    return

    elif self.mode == "REFERENCE":
        if isNaN(self.baseRX):
            if isNaN(cmd):
                strList = str.split(",")
                if isNaN(strList[0]) or isNaN(strList[1]):
                    alert(translate("Requires valid numeric angle or two points."))
                    setPromptPrefix(translate("Specify the reference angle") + " 0.00}: ")
                else:
                    self.baseRX = Number(strList[0])
                    self.baseRY = Number(strList[1])
                    addRubber("LINE")
                    setRubberMode("LINE")
                    setRubberPoint("LINE_START", self.baseRX, self.baseRY)
                    setPromptPrefix(translate("Specify second point: "))
          
            else:
                # The base and dest values are only set here to advance the command.
                self.baseRX = 0.0
                self.baseRY = 0.0
                self.destRX = 0.0
                self.destRY = 0.0
                # The reference angle is what we will use later.
                self.angleRef = Number(cmd)
                addRubber("LINE")
                setRubberMode("LINE")
                setRubberPoint("LINE_START", self.baseX, self.baseY)
                previewOn("SELECTED", "ROTATE", self.baseX, self.baseY, self.angleRef)
                setPromptPrefix(translate("Specify the new angle: "))

        elif isNaN(self.destRX)):
            if isNaN(cmd)):
                strList = str.split(",")
                if isNaN(strList[0]) or isNaN(strList[1])):
                    alert(translate("Requires valid numeric angle or two points."))
                    setPromptPrefix(translate("Specify second point: "))
                else:
                    self.destRX = Number(strList[0])
                    self.destRY = Number(strList[1])
                    self.angleRef = calculateAngle(self.baseRX, self.baseRY, self.destRX, self.destRY)
                    previewOn("SELECTED", "ROTATE", self.baseX, self.baseY, self.angleRef)
                    setRubberPoint("LINE_START", self.baseX, self.baseY)
                    setPromptPrefix(translate("Specify the new angle: "))

            else:
                #The base and dest values are only set here to advance the command.
                self.baseRX = 0.0
                self.baseRY = 0.0
                self.destRX = 0.0
                self.destRY = 0.0
                #The reference angle is what we will use later.
                self.angleRef = Number(cmd)
                previewOn("SELECTED", "ROTATE", self.baseX, self.baseY, self.angleRef)
                setPromptPrefix(translate("Specify the new angle: "))

        elif isNaN(self.angleNew):
            if isNaN(cmd):
                strList = str.split(",")
                if isNaN(strList[0]) or isNaN(strList[1]):
                    alert(translate("Requires valid numeric angle or second point."))
                    setPromptPrefix(translate("Specify the new angle: "))
                else:
                    x = Number(strList[0])
                    y = Number(strList[1])
                    self.angleNew = calculateAngle(self.baseX, self.baseY, x, y)
                    rotateSelected(self.baseX, self.baseY, self.angleNew - self.angleRef)
                    previewOff()
                    return

            else
                self.angleNew = Number(cmd)
                rotateSelected(self.baseX, self.baseY, self.angleNew - self.angleRef)
                previewOff()
                return


---

var global = }; #Required
self.test1
self.test2

def __init__(self):
    #Report number of pre-selected objects
    setPromptPrefix("Number of Objects Selected: " + numSelected().toString())
    appendPromptHistory()

    mirrorSelected(0,0,0,1)

    #selectAll();
    #rotateSelected(0,0,90);

    #Polyline & Polygon Testing

    offsetX = 0.0
    offsetY = 0.0

    polylineArray = []
    polylineArray.push(1.0 + offsetX)
    polylineArray.push(1.0 + offsetY)
    polylineArray.push(1.0 + offsetX)
    polylineArray.push(2.0 + offsetY)
    polylineArray.push(2.0 + offsetX)
    polylineArray.push(2.0 + offsetY)
    polylineArray.push(2.0 + offsetX)
    polylineArray.push(3.0 + offsetY)
    polylineArray.push(3.0 + offsetX)
    polylineArray.push(3.0 + offsetY)
    polylineArray.push(3.0 + offsetX)
    polylineArray.push(2.0 + offsetY)
    polylineArray.push(4.0 + offsetX)
    polylineArray.push(2.0 + offsetY)
    polylineArray.push(4.0 + offsetX)
    polylineArray.push(1.0 + offsetY)
    addPolyline(polylineArray)

    offsetX = 5.0
    offsetY = 0.0

    polygonArray = []
    polygonArray.push(1.0 + offsetX)
    polygonArray.push(1.0 + offsetY)
    polygonArray.push(1.0 + offsetX)
    polygonArray.push(2.0 + offsetY)
    polygonArray.push(2.0 + offsetX)
    polygonArray.push(2.0 + offsetY)
    polygonArray.push(2.0 + offsetX)
    polygonArray.push(3.0 + offsetY)
    polygonArray.push(3.0 + offsetX)
    polygonArray.push(3.0 + offsetY)
    polygonArray.push(3.0 + offsetX)
    polygonArray.push(2.0 + offsetY)
    polygonArray.push(4.0 + offsetX)
    polygonArray.push(2.0 + offsetY)
    polygonArray.push(4.0 + offsetX)
    polygonArray.push(1.0 + offsetY)
    addPolygon(polygonArray)


    return

---

var global = }; #Required
self.firstRun
self.baseX
self.baseY
self.destX
self.destY
self.factor

self.baseRX
self.baseRY
self.destRX
self.destRY
self.factorRef
self.factorNew

self.mode

#enums
self.mode_NORMAL    = 0
self.mode_REFERENCE = 1

def __init__():
    self.mode = self.mode_NORMAL
    self.firstRun = true
    self.baseX  = MAX_DISTANCE+1.0
    self.baseY  = MAX_DISTANCE+1.0
    self.destX  = MAX_DISTANCE+1.0
    self.destY  = MAX_DISTANCE+1.0
    self.factor = MAX_DISTANCE+1.0

    self.baseRX    = MAX_DISTANCE+1.0
    self.baseRY    = MAX_DISTANCE+1.0
    self.destRX    = MAX_DISTANCE+1.0
    self.destRY    = MAX_DISTANCE+1.0
    self.factorRef = MAX_DISTANCE+1.0
    self.factorNew = MAX_DISTANCE+1.0

    if numSelected() <= 0)

        #TODO: Prompt to select objects if nothing is preselected
        alert(translate("Preselect objects before invoking the scale command."))
        return
        messageBox("information", translate("Scale Preselect"), translate("Preselect objects before invoking the scale command."))
    }
    else

        setPromptPrefix(translate("Specify base point: "))
    }

def click(x, y):
    if self.mode == self.mode_NORMAL)

        if self.firstRun)
    
            self.firstRun = false
            self.baseX = x
            self.baseY = y
            addRubber("LINE")
            setRubberMode("LINE")
            setRubberPoint("LINE_START", self.baseX, self.baseY)
            previewOn("SELECTED", "SCALE", self.baseX, self.baseY, 1)
            appendPromptHistory()
            setPromptPrefix(translate("Specify scale factor or [Reference]: "))

        else
    
            self.destX = x
            self.destY = y
            self.factor = calculateDistance(self.baseX, self.baseY, self.destX, self.destY)
            appendPromptHistory()
            scaleSelected(self.baseX, self.baseY, self.factor)
            previewOff()
            return

    }
    elif self.mode == self.mode_REFERENCE)

        if isNaN(self.baseRX))
    
            self.baseRX = x
            self.baseRY = y
            appendPromptHistory()
            addRubber("LINE")
            setRubberMode("LINE")
            setRubberPoint("LINE_START", self.baseRX, self.baseRY)
            setPromptPrefix(translate("Specify second point: "))

        elif isNaN(self.destRX))
    
            self.destRX = x
            self.destRY = y
            self.factorRef = calculateDistance(self.baseRX, self.baseRY, self.destRX, self.destRY)
            if self.factorRef <= 0.0)
        
                self.destRX    = MAX_DISTANCE+1.0
                self.destRY    = MAX_DISTANCE+1.0
                self.factorRef = MAX_DISTANCE+1.0
                alert(translate("Value must be positive and nonzero."))
                setPromptPrefix(translate("Specify second point: "))
    
            else
        
                appendPromptHistory()
                setRubberPoint("LINE_START", self.baseX, self.baseY)
                previewOn("SELECTED", "SCALE", self.baseX, self.baseY, self.factorRef)
                setPromptPrefix(translate("Specify new length: "))

        elif isNaN(self.factorNew))

            self.factorNew = calculateDistance(self.baseX, self.baseY, x, y)
            if self.factorNew <= 0.0)
        
                self.factorNew = MAX_DISTANCE+1.0
                alert(translate("Value must be positive and nonzero."))
                setPromptPrefix(translate("Specify new length: "))
            else:
                appendPromptHistory()
                scaleSelected(self.baseX, self.baseY, self.factorNew/self.factorRef)
                previewOff()
                return

def prompt(cmd):
    if self.mode == self.mode_NORMAL:
        if self.firstRun:
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1]):
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify base point: "))
    
            else
        
                self.firstRun = false
                self.baseX = Number(strList[0])
                self.baseY = Number(strList[1])
                addRubber("LINE")
                setRubberMode("LINE")
                setRubberPoint("LINE_START", self.baseX, self.baseY)
                previewOn("SELECTED", "SCALE", self.baseX, self.baseY, 1)
                setPromptPrefix(translate("Specify scale factor or [Reference]: "))
    

        else
    
            if str == "R" or cmd == "REFERENCE") #TODO: Probably should add additional qsTr calls here.
        
                self.mode = self.mode_REFERENCE
                setPromptPrefix(translate("Specify reference length") + " 1}: ")
                clearRubber()
                previewOff()
    
            else
        
                if isNaN(cmd))
            
                    alert(translate("Requires valid numeric distance, second point, or option keyword."))
                    setPromptPrefix(translate("Specify scale factor or [Reference]: "))
        
                else
            
                    self.factor = Number(cmd)
                    scaleSelected(self.baseX, self.baseY, self.factor)
                    previewOff()
                    return

    elif self.mode == self.mode_REFERENCE)
        if isNaN(self.baseRX))
            if isNaN(cmd))
                strList = str.split(",")
                if isNaN(strList[0]) or isNaN(strList[1]))
                    alert(translate("Requires valid numeric distance or two points."))
                    setPromptPrefix(translate("Specify reference length") + " 1}: ")
                else:
                    self.baseRX = Number(strList[0])
                    self.baseRY = Number(strList[1])
                    addRubber("LINE")
                    setRubberMode("LINE")
                    setRubberPoint("LINE_START", self.baseRX, self.baseRY)
                    setPromptPrefix(translate("Specify second point: "))
            else:
                #The base and dest values are only set here to advance the command.
                self.baseRX = 0.0
                self.baseRY = 0.0
                self.destRX = 0.0
                self.destRY = 0.0
                #The reference length is what we will use later.
                self.factorRef = Number(cmd)
                if self.factorRef <= 0.0:
                    self.baseRX    = MAX_DISTANCE+1.0
                    self.baseRY    = MAX_DISTANCE+1.0
                    self.destRX    = MAX_DISTANCE+1.0
                    self.destRY    = MAX_DISTANCE+1.0
                    self.factorRef = MAX_DISTANCE+1.0
                    alert(translate("Value must be positive and nonzero."))
                    setPromptPrefix(translate("Specify reference length") + " 1}: ")
                else:
                    addRubber("LINE")
                    setRubberMode("LINE")
                    setRubberPoint("LINE_START", self.baseX, self.baseY)
                    previewOn("SELECTED", "SCALE", self.baseX, self.baseY, self.factorRef)
                    setPromptPrefix(translate("Specify new length: "))

        elif isNaN(self.destRX):
            if isNaN(cmd):
                strList = str.split(",")
                if isNaN(strList[0]) or isNaN(strList[1]))
                    alert(translate("Requires valid numeric distance or two points."))
                    setPromptPrefix(translate("Specify second point: "))
                else:
                    self.destRX = Number(strList[0])
                    self.destRY = Number(strList[1])
                    self.factorRef = calculateDistance(self.baseRX, self.baseRY, self.destRX, self.destRY)
                    if self.factorRef <= 0.0)
                
                        self.destRX    = MAX_DISTANCE+1.0
                        self.destRY    = MAX_DISTANCE+1.0
                        self.factorRef = MAX_DISTANCE+1.0
                        alert(translate("Value must be positive and nonzero."))
                        setPromptPrefix(translate("Specify second point: "))
            
                    else
                
                        setRubberPoint("LINE_START", self.baseX, self.baseY)
                        previewOn("SELECTED", "SCALE", self.baseX, self.baseY, self.factorRef)
                        setPromptPrefix(translate("Specify new length: "))

            else:
                #The base and dest values are only set here to advance the command.
                self.baseRX = 0.0
                self.baseRY = 0.0
                self.destRX = 0.0
                self.destRY = 0.0
                #The reference length is what we will use later.
                self.factorRef = Number(cmd)
                if self.factorRef <= 0.0:
                    self.destRX    = MAX_DISTANCE+1.0
                    self.destRY    = MAX_DISTANCE+1.0
                    self.factorRef = MAX_DISTANCE+1.0
                    alert(translate("Value must be positive and nonzero."))
                    setPromptPrefix(translate("Specify second point: "))
                else:
                    setRubberPoint("LINE_START", self.baseX, self.baseY)
                    previewOn("SELECTED", "SCALE", self.baseX, self.baseY, self.factorRef)
                    setPromptPrefix(translate("Specify new length: "))

        elif isNaN(self.factorNew):
            if isNaN(cmd):
                strList = str.split(",")
                if isNaN(strList[0]) or isNaN(strList[1]):
                    alert(translate("Requires valid numeric distance or second point."))
                    setPromptPrefix(translate("Specify new length: "))
                else:
                    x = Number(strList[0])
                    y = Number(strList[1])
                    self.factorNew = calculateDistance(self.baseX, self.baseY, x, y)
                    if self.factorNew <= 0.0)
                
                        self.factorNew = MAX_DISTANCE+1.0
                        alert(translate("Value must be positive and nonzero."))
                        setPromptPrefix(translate("Specify new length: "))
            
                    else
                
                        scaleSelected(self.baseX, self.baseY, self.factorNew/self.factorRef)
                        previewOff()
                        return

            else:
                self.factorNew = Number(cmd)
                if self.factorNew <= 0.0:
                    self.factorNew = MAX_DISTANCE+1.0
                    alert(translate("Value must be positive and nonzero."))
                    setPromptPrefix(translate("Specify new length: "))
        
                else:
                    scaleSelected(self.baseX, self.baseY, self.factorNew/self.factorRef)
                    previewOff()
                    return


class Text(Base_Object):
    r"""
    .
    """
    def __init__(self):
        clearSelection()
        self.modes = ["JUSTIFY", "SETFONT", "SETGEOM", "RAPID"]
        self.text = ""
        self.textX = MAX_DISTANCE+1.0
        self.textY = MAX_DISTANCE+1.0
        self.textJustify = "Left"
        self.textFont = textFont()
        self.textHeight = MAX_DISTANCE+1.0
        self.textRotation = MAX_DISTANCE+1.0
        self.mode = self.mode_SETGEOM
        setPromptPrefix(translate("Current font: ") + "" + self.textFont + "} " + translate("Text height: ") + "" +  textSize() + "}")
        appendPromptHistory()
        setPromptPrefix(translate("Specify start point of text or [Justify/Setfont]: "))
        return self

def click(x, y):
    if self.mode == "SETGEOM":
        if isNaN(self.textX):
            self.textX = x
            self.textY = y
            addRubber("LINE")
            setRubberMode("LINE")
            setRubberPoint("LINE_START", self.textX, self.textY)
            appendPromptHistory()
            setPromptPrefix(translate("Specify text height") + " " + textSize() + "}: ")
        elif isNaN(self.textHeight):
            self.textHeight = calculateDistance(self.textX, self.textY, x, y)
            setTextSize(self.textHeight)
            appendPromptHistory()
            setPromptPrefix(translate("Specify text angle") + " " + textAngle() + "}: ")

        elif isNaN(self.textRotation))
    
            self.textRotation = calculateAngle(self.textX, self.textY, x, y)
            setTextAngle(self.textRotation)
            appendPromptHistory()
            setPromptPrefix(translate("Enter text: "))
            self.mode = self.mode_RAPID
            enablePromptRapidFire()
            clearRubber()
            addRubber("TEXTSINGLE")
            setRubberMode("TEXTSINGLE")
            setRubberPoint("TEXT_POINT", self.textX, self.textY)
            setRubberPoint("TEXT_HEIGHT_ROTATION", self.textHeight, self.textRotation)
            setRubberText("TEXT_FONT", self.textFont)
            setRubberText("TEXT_JUSTIFY", self.textJustify)
            setRubberText("TEXT_RAPID", self.text)

        else:
            #Do nothing, as we are in rapidFire mode now.


def prompt(cmd):
    if self.mode == "JUSTIFY":
        if cmd == "C" or cmd == "CENTER":
            #TODO: Probably should add additional qsTr calls here.
            self.mode = "SETGEOM"
            self.textJustify = "Center"
            setRubberText("TEXT_JUSTIFY", self.textJustify)
            setPromptPrefix(translate("Specify center point of text or [Justify/Setfont]: "))
        elif cmd == "R" or cmd == "RIGHT":
            #TODO: Probably should add additional qsTr calls here.
            self.mode = "SETGEOM"
            self.textJustify = "Right"
            setRubberText("TEXT_JUSTIFY", self.textJustify)
            setPromptPrefix(translate("Specify right-end point of text or [Justify/Setfont]: "))
        elif str == "A" or cmd == "ALIGN") #TODO: Probably should add additional qsTr calls here.
    
            self.mode = self.mode_SETGEOM
            self.textJustify = "Aligned"
            setRubberText("TEXT_JUSTIFY", self.textJustify)
            setPromptPrefix(translate("Specify start point of text or [Justify/Setfont]: "))

        elif str == "M" or cmd == "MIDDLE") #TODO: Probably should add additional qsTr calls here.
    
            self.mode = self.mode_SETGEOM
            self.textJustify = "Middle"
            setRubberText("TEXT_JUSTIFY", self.textJustify)
            setPromptPrefix(translate("Specify middle point of text or [Justify/Setfont]: "))

        elif str == "F" or cmd == "FIT") #TODO: Probably should add additional qsTr calls here.
    
            self.mode = self.mode_SETGEOM
            self.textJustify = "Fit"
            setRubberText("TEXT_JUSTIFY", self.textJustify)
            setPromptPrefix(translate("Specify start point of text or [Justify/Setfont]: "))

        elif str == "TL" or cmd == "TOPLEFT") #TODO: Probably should add additional qsTr calls here.
    
            self.mode = self.mode_SETGEOM
            self.textJustify = "Top Left"
            setRubberText("TEXT_JUSTIFY", self.textJustify)
            setPromptPrefix(translate("Specify top-left point of text or [Justify/Setfont]: "))

        elif str == "TC" or cmd == "TOPCENTER") #TODO: Probably should add additional qsTr calls here.
    
            self.mode = self.mode_SETGEOM
            self.textJustify = "Top Center"
            setRubberText("TEXT_JUSTIFY", self.textJustify)
            setPromptPrefix(translate("Specify top-center point of text or [Justify/Setfont]: "))

        elif str == "TR" or cmd == "TOPRIGHT") #TODO: Probably should add additional qsTr calls here.
    
            self.mode = self.mode_SETGEOM
            self.textJustify = "Top Right"
            setRubberText("TEXT_JUSTIFY", self.textJustify)
            setPromptPrefix(translate("Specify top-right point of text or [Justify/Setfont]: "))

        elif str == "ML" or cmd == "MIDDLELEFT") #TODO: Probably should add additional qsTr calls here.
    
            self.mode = self.mode_SETGEOM
            self.textJustify = "Middle Left"
            setRubberText("TEXT_JUSTIFY", self.textJustify)
            setPromptPrefix(translate("Specify middle-left point of text or [Justify/Setfont]: "))

        elif str == "MC" or cmd == "MIDDLECENTER") #TODO: Probably should add additional qsTr calls here.
    
            self.mode = self.mode_SETGEOM
            self.textJustify = "Middle Center"
            setRubberText("TEXT_JUSTIFY", self.textJustify)
            setPromptPrefix(translate("Specify middle-center point of text or [Justify/Setfont]: "))

        elif str == "MR" or cmd == "MIDDLERIGHT") #TODO: Probably should add additional qsTr calls here.
    
            self.mode = self.mode_SETGEOM
            self.textJustify = "Middle Right"
            setRubberText("TEXT_JUSTIFY", self.textJustify)
            setPromptPrefix(translate("Specify middle-right point of text or [Justify/Setfont]: "))

        elif str == "BL" or cmd == "BOTTOMLEFT") #TODO: Probably should add additional qsTr calls here.
    
            self.mode = self.mode_SETGEOM
            self.textJustify = "Bottom Left"
            setRubberText("TEXT_JUSTIFY", self.textJustify)
            setPromptPrefix(translate("Specify bottom-left point of text or [Justify/Setfont]: "))

        elif str == "BC" or cmd == "BOTTOMCENTER") #TODO: Probably should add additional qsTr calls here.
    
            self.mode = self.mode_SETGEOM
            self.textJustify = "Bottom Center"
            setRubberText("TEXT_JUSTIFY", self.textJustify)
            setPromptPrefix(translate("Specify bottom-center point of text or [Justify/Setfont]: "))

        elif str == "BR" or cmd == "BOTTOMRIGHT") #TODO: Probably should add additional qsTr calls here.
    
            self.mode = self.mode_SETGEOM
            self.textJustify = "Bottom Right"
            setRubberText("TEXT_JUSTIFY", self.textJustify)
            setPromptPrefix(translate("Specify bottom-right point of text or [Justify/Setfont]: "))

        else:
            alert(translate("Invalid option keyword."))
            setPromptPrefix(translate("Text Justification Options [Center/Right/Align/Middle/Fit/TL/TC/TR/ML/MC/MR/BL/BC/BR]: "))

    elif self.mode == self.mode_SETFONT:
        self.mode = self.mode_SETGEOM
        self.textFont = str
        setRubberText("TEXT_FONT", self.textFont)
        setTextFont(self.textFont)
        setPromptPrefix(translate("Specify start point of text or [Justify/Setfont]: "))

    elif self.mode == "SETGEOM":
        if isNaN(self.textX):
            if str == "J" or cmd == "JUSTIFY":
                #TODO: Probably should add additional qsTr calls here.
                self.mode = self.mode_JUSTIFY
                setPromptPrefix(translate("Text Justification Options [Center/Right/Align/Middle/Fit/TL/TC/TR/ML/MC/MR/BL/BC/BR]: "))
    
            elif str == "S" or cmd == "SETFONT") #TODO: Probably should add additional qsTr calls here.
        
                self.mode = self.mode_SETFONT
                setPromptPrefix(translate("Specify font name: "))
    
            else
        
                strList = str.split(",")
                if isNaN(strList[0]) or isNaN(strList[1]))
            
                    alert(translate("Point or option keyword required."))
                    setPromptPrefix(translate("Specify start point of text or [Justify/Setfont]: "))
        
                else
            
                    self.textX = Number(strList[0])
                    self.textY = Number(strList[1])
                    addRubber("LINE")
                    setRubberMode("LINE")
                    setRubberPoint("LINE_START", self.textX, self.textY)
                    setPromptPrefix(translate("Specify text height") + " " + textSize() + "}: ")

        elif isNaN(self.textHeight))
    
            if str == "")
        
                self.textHeight = textSize()
                setPromptPrefix(translate("Specify text angle") + " " + textAngle() + "}: ")
    
            elif isNaN(cmd))
        
                alert(translate("Requires valid numeric distance or second point."))
                setPromptPrefix(translate("Specify text height") + " " + textSize() + "}: ")
    
            else
        
                self.textHeight = Number(cmd)
                setTextSize(self.textHeight)
                setPromptPrefix(translate("Specify text angle") + " " + textAngle() + "}: ")
    

        elif isNaN(self.textRotation))
    
            if str == "")
        
                self.textRotation = textAngle()
                setPromptPrefix(translate("Enter text: "))
                self.mode = self.mode_RAPID
                enablePromptRapidFire()
                clearRubber()
                addRubber("TEXTSINGLE")
                setRubberMode("TEXTSINGLE")
                setRubberPoint("TEXT_POINT", self.textX, self.textY)
                setRubberPoint("TEXT_HEIGHT_ROTATION", self.textHeight, self.textRotation)
                setRubberText("TEXT_FONT", self.textFont)
                setRubberText("TEXT_JUSTIFY", self.textJustify)
                setRubberText("TEXT_RAPID", self.text)
    
            elif isNaN(cmd))
        
                alert(translate("Requires valid numeric angle or second point."))
                setPromptPrefix(translate("Specify text angle") + " " + textAngle() + "}: ")
    
            else
        
                self.textRotation = Number(cmd)
                setTextAngle(self.textRotation)
                setPromptPrefix(translate("Enter text: "))
                self.mode = self.mode_RAPID
                enablePromptRapidFire()
                clearRubber()
                addRubber("TEXTSINGLE")
                setRubberMode("TEXTSINGLE")
                setRubberPoint("TEXT_POINT", self.textX, self.textY)
                setRubberPoint("TEXT_HEIGHT_ROTATION", self.textHeight, self.textRotation)
                setRubberText("TEXT_FONT", self.textFont)
                setRubberText("TEXT_JUSTIFY", self.textJustify)
                setRubberText("TEXT_RAPID", self.text)
    

        else
    
            #Do nothing, as we are in rapidFire mode now.

    }
    elif self.mode == "RAPID":
        if cmd == "RAPID_ENTER":
            if self.text == "":
                return
            else:
                # TODO: Rather than ending the command,
                # calculate where the next line would be and
                # modify the x/y to the new point.
                vulcanize()
                return
        else:
            self.text = str
            setRubberText("TEXT_RAPID", self.text)

class Snowflake():
    def __init__(self):
        clearSelection()
        self.numPoints = 2048; #Default //TODO: min:64 max:8192
        self.sx = 0.04
        self.sy = 0.04
        self.modes = ["NUM_POINTS", "XSCALE", "YSCALE"]
        self.cx = MAX_DISTANCE+1.0
        self.cy = MAX_DISTANCE+1.0
        self.mode = "NUM_POINTS"

        addRubber("POLYGON")
        setRubberMode("POLYGON")
        self.update()
        spareRubber("POLYGON")
        return self

    def update(self):
        r" Snowflake Curve with t in [0, 2pi]. "
        xx = MAX_DISTANCE+1.0
        yy = MAX_DISTANCE+1.0

        for i in range(self.numPts + 1):
            t = ((2.0*math.pi)/self.numPts)*i;


xx = 4/7*sin(20/11-318*t)+
3/13*sin(19/11-317*t)+
3/5*sin(21/16-316*t)+
1/6*sin(17/5-315*t)+
2/9*sin(20/19-314*t)+
5/9*sin(35/9-313*t)+
7/12*sin(9/8-310*t)+
5/16*sin(33/8-309*t)+
5/11*sin(31/11-308*t)+
4/7*sin(3/8-307*t)+
4/11*sin(9/8-306*t)+
7/8*sin(21/11-305*t)+
2/3*sin(55/13-304*t)+
5/9*sin(17/7-303*t)+
3/10*sin(3/13-302*t)+
4/11*sin(60/17-301*t)+
6/11*sin(48/11-300*t)+
9/19*sin(1/6-299*t)+
4/5*sin(19/11-298*t)+
7/13*sin(25/8-297*t)+
7/11*sin(19/7-296*t)+
1/2*sin(1-295*t)+
4/9*sin(24/11-294*t)+
1/3*sin(7/2-291*t)+
6/17*sin(15/13-290*t)+
11/17*sin(32/7-288*t)+
3/8*sin(33/8-287*t)+
4/7*sin(15/7-286*t)+
4/5*sin(48/11-284*t)+
6/7*sin(10/7-283*t)+
6/7*sin(20/11-282*t)+
3/8*sin(11/7-281*t)+
5/7*sin(23/6-280*t)+
1/21*sin(19/12-279*t)+
4/9*sin(1/5-278*t)+
5/8*sin(5/9-276*t)+
9/10*sin(2/3-274*t)+
5/8*sin(5/11-273*t)+
1/6*sin(9/2-272*t)+
12/25*sin(29/12-271*t)+
7/13*sin(59/15-270*t)+
5/7*sin(23/9-269*t)+
3/4*sin(9/2-268*t)+
5/11*sin(37/9-267*t)+
10/11*sin(11/7-266*t)+
1/3*sin(3/7-264*t)+
7/9*sin(33/17-262*t)+
5/8*sin(9/8-261*t)+
5/8*sin(38/13-260*t)+
11/21*sin(36/13-259*t)+
3/11*sin(1/29-258*t)+
8/15*sin(31/8-257*t)+
2/5*sin(3/13-256*t)+
1/2*sin(47/10-255*t)+
1/10*sin(33/10-254*t)+
2/5*sin(1/2-253*t)+
4/7*sin(33/7-252*t)+
6/17*sin(3/8-250*t)+
5/7*sin(25/9-249*t)+
7/9*sin(35/8-248*t)+
2/7*sin(81/20-247*t)+
5/8*sin(25/6-244*t)+
5/16*sin(11/21-243*t)+
11/13*sin(167/42-242*t)+
11/15*sin(18/5-241*t)+
13/14*sin(37/11-240*t)+
1/4*sin(20/9-239*t)+
9/14*sin(52/15-238*t)+
9/14*sin(17/14-237*t)+
6/13*sin(69/17-236*t)+
5/8*sin(74/21-235*t)+
7/15*sin(76/25-234*t)+
10/11*sin(15/8-232*t)+
5/11*sin(5/9-230*t)+
1/8*sin(8/3-229*t)+
5/9*sin(2/7-227*t)+
4/13*sin(32/9-226*t)+
2/3*sin(45/11-225*t)+
1/30*sin(53/15-223*t)+
7/11*sin(4/11-222*t)+
10/19*sin(31/13-221*t)+
sin(13/7-219*t)+
9/14*sin(33/7-216*t)+
2/3*sin(19/9-215*t)+
3/5*sin(27/11-214*t)+
9/11*sin(43/10-210*t)+
5/7*sin(13/8-209*t)+
5/9*sin(21/5-208*t)+
2/7*sin(14/9-206*t)+
9/8*sin(23/7-205*t)+
18/13*sin(11/9-203*t)+
7/4*sin(47/12-201*t)+
10/7*sin(8/9-200*t)+
7/10*sin(6/11-199*t)+
5/3*sin(7/6-198*t)+
19/11*sin(11/6-196*t)+
15/8*sin(9/8-195*t)+
8/17*sin(9/7-192*t)+
8/3*sin(39/10-191*t)+
23/10*sin(2/7-188*t)+
3/4*sin(3/5-187*t)+
7/12*sin(50/11-185*t)+
57/29*sin(4-184*t)+
9/8*sin(6/7-183*t)+
9/7*sin(15/13-182*t)+
5/13*sin(16/7-181*t)+
18/7*sin(5/14-180*t)+
17/9*sin(35/12-179*t)+
5/4*sin(5/7-178*t)+
22/23*sin(3/4-176*t)+
3/8*sin(48/13-175*t)+
15/11*sin(13/11-174*t)+
25/17*sin(23/5-173*t)+
18/11*sin(19/8-172*t)+
11/16*sin(5/3-170*t)+
39/38*sin(15/7-169*t)+
7/6*sin(36/11-166*t)+
15/11*sin(11/6-163*t)+
17/13*sin(3-162*t)+
11/9*sin(20/7-161*t)+
9/7*sin(35/9-160*t)+
7/6*sin(3/2-159*t)+
8/7*sin(9/10-158*t)+
12/25*sin(13/5-156*t)+
6/13*sin(25/13-154*t)+
9/13*sin(7/8-152*t)+
23/10*sin(33/14-151*t)+
8/11*sin(36/11-150*t)+
15/7*sin(26/7-149*t)+
6/5*sin(53/12-148*t)+
14/11*sin(3/2-147*t)+
9/8*sin(4/3-146*t)+
5/8*sin(18/13-145*t)+
15/7*sin(3/8-143*t)+
5/8*sin(5/6-142*t)+
6/7*sin(35/9-139*t)+
16/13*sin(1/2-138*t)+
9/4*sin(7/2-137*t)+
20/9*sin(15/8-135*t)+
11/8*sin(9/4-134*t)+
sin(19/10-133*t)+
22/7*sin(48/11-132*t)+
23/14*sin(1-131*t)+
19/9*sin(27/8-130*t)+
19/5*sin(20/7-129*t)+
18/5*sin(76/25-128*t)+
27/8*sin(4/5-126*t)+
37/8*sin(3/8-125*t)+
62/11*sin(11/3-124*t)+
49/11*sin(7/6-123*t)+
21/22*sin(23/12-122*t)+
223/74*sin(11/3-121*t)+
11/5*sin(19/5-120*t)+
13/4*sin(33/13-119*t)+
27/8*sin(22/5-117*t)+
24/7*sin(13/7-114*t)+
69/17*sin(18/17-113*t)+
10/9*sin(2/7-112*t)+
133/66*sin(12/7-111*t)+
2/5*sin(47/24-110*t)+
13/5*sin(11/6-108*t)+
16/7*sin(39/11-105*t)+
11/5*sin(25/9-104*t)+
151/50*sin(19/7-103*t)+
19/7*sin(12/5-101*t)+
26/7*sin(101/25-99*t)+
43/21*sin(41/14-98*t)+
13/3*sin(31/9-97*t)+
10/13*sin(1-95*t)+
17/7*sin(39/10-93*t)+
145/48*sin(3-92*t)+
37/6*sin(47/13-91*t)+
5/6*sin(36/13-89*t)+
9/4*sin(3/7-87*t)+
48/13*sin(26/17-86*t)+
7/3*sin(28/19-82*t)+
31/6*sin(8/7-81*t)+
36/7*sin(12/7-80*t)+
38/9*sin(25/9-79*t)+
17/2*sin(37/14-76*t)+
16/3*sin(19/20-75*t)+
81/16*sin(4/5-74*t)+
67/10*sin(19/15-73*t)+
40/11*sin(32/11-72*t)+
71/13*sin(21/20-71*t)+
68/15*sin(46/15-70*t)+
52/15*sin(27/10-69*t)+
57/14*sin(7/8-67*t)+
7/4*sin(42/13-66*t)+
39/11*sin(43/21-65*t)+
30/11*sin(33/8-64*t)+
7/5*sin(20/7-63*t)+
4/7*sin(13/14-62*t)+
39/10*sin(16/9-61*t)+
7/6*sin(137/34-59*t)+
16/13*sin(107/27-58*t)+
26/27*sin(17/5-57*t)+
4/3*sin(9/14-56*t)+
46/11*sin(5/3-55*t)+
11/6*sin(13/4-54*t)+
19/4*sin(17/5-53*t)+
19/7*sin(43/11-52*t)+
25/12*sin(30/7-51*t)+
15/7*sin(5/11-50*t)+
53/5*sin(21/13-49*t)+
62/13*sin(67/15-48*t)+
122/9*sin(48/13-47*t)+
20/13*sin(1-46*t)+
7/6*sin(32/7-43*t)+
12/7*sin(13/25-42*t)+
11/17*sin(9/10-40*t)+
11/9*sin(2-39*t)+
4/3*sin(19/7-38*t)+
12/5*sin(47/11-37*t)+
10/7*sin(12/7-36*t)+
108/17*sin(3/4-35*t)+
25/9*sin(19/5-34*t)+
7/13*sin(22/5-33*t)+
9/4*sin(13/11-32*t)+
181/15*sin(25/11-31*t)+
202/11*sin(57/13-29*t)+
2/11*sin(26/7-28*t)+
129/13*sin(38/15-25*t)+
13/6*sin(1/8-24*t)+
77/13*sin(11/8-23*t)+
19/6*sin(15/7-22*t)+
18/7*sin(29/10-21*t)+
9*sin(13/5-18*t)+
342/7*sin(11/6-17*t)+
3/5*sin(49/11-15*t)+
38/3*sin(19/7-14*t)+
994/9*sin(25/8-13*t)+
22/9*sin(49/12-10*t)+
97/9*sin(1/14-8*t)+
559/7*sin(47/14-7*t)+
19/13*sin(5/6-6*t)+
3*sin(57/17-4*t)+
28/5*sin(1-3*t)+
10/3*sin(22/7-2*t)+
1507/3*sin(29/8-t)-
1407/13*sin(5*t+8/11)-
15/2*sin(9*t+2/5)-
1193/9*sin(11*t+28/27)-
209/15*sin(12*t+2/5)-
116/15*sin(16*t+40/39)-
1105/33*sin(19*t+1/3)-
45/13*sin(20*t+7/6)-
91/46*sin(26*t+4/7)-
43/16*sin(27*t+12/11)-
46/13*sin(30*t+14/9)-
29/10*sin(41*t+3/14)-
31/11*sin(44*t+15/14)-
22/7*sin(45*t+10/7)-
7/8*sin(60*t+22/15)-
54/53*sin(68*t+5/4)-
214/15*sin(77*t+5/9)-
54/11*sin(78*t+1/13)-
47/6*sin(83*t+5/11)-
1/2*sin(84*t+8/7)-
2/3*sin(85*t+4/9)-
7/3*sin(88*t+7/6)-
15/4*sin(90*t+1/6)-
35/6*sin(94*t+17/18)-
77/26*sin(96*t+2/7)-
64/11*sin(100*t+34/23)-
13/6*sin(102*t+14/11)-
19/7*sin(106*t+5/6)-
13/6*sin(107*t+10/11)-
42/13*sin(109*t+8/7)-
69/35*sin(115*t+10/21)-
12/7*sin(116*t+17/16)-
8/3*sin(118*t+5/9)-
1/6*sin(127*t+17/12)-
13/7*sin(136*t+8/7)-
7/10*sin(140*t+7/5)-
15/7*sin(141*t+19/14)-
6/11*sin(144*t+5/16)-
3/2*sin(153*t+9/14)-
6/5*sin(155*t+3/10)-
3/8*sin(157*t+10/11)-
20/11*sin(164*t+19/14)-
7/5*sin(165*t+7/6)-
8/13*sin(167*t+20/13)-
7/8*sin(168*t+3/7)-
5/14*sin(171*t+16/13)-
22/7*sin(177*t+3/13)-
23/8*sin(186*t+7/8)-
13/7*sin(189*t+11/9)-
9/5*sin(190*t+32/21)-
27/28*sin(193*t+1)-
5/12*sin(194*t+1/2)-
44/43*sin(197*t+6/5)-
5/11*sin(202*t+1/5)-
8/7*sin(204*t+1/23)-
16/15*sin(207*t+7/10)-
1/2*sin(211*t+2/5)-
5/8*sin(212*t+3/5)-
10/13*sin(213*t+6/5)-
21/16*sin(217*t+4/3)-
11/5*sin(218*t+24/25)-
2/3*sin(220*t+5/9)-
13/10*sin(224*t+7/8)-
17/8*sin(228*t+1/9)-
3/7*sin(231*t+14/9)-
5/12*sin(233*t+9/11)-
3/5*sin(245*t+4/7)-
2/3*sin(246*t+15/11)-
3/8*sin(251*t+4/7)-
2/9*sin(263*t+19/20)-
1/2*sin(265*t+13/11)-
3/8*sin(275*t+3/2)-
17/35*sin(277*t+9/13)-
3/7*sin(285*t+3/11)-
9/10*sin(289*t+25/19)-
4/9*sin(292*t+20/13)-
12/25*sin(293*t+5/4)-
3/5*sin(311*t+9/8)-
33/32*sin(312*t+1/2)

yy = 3/7*sin(24/11-318*t)+
5/12*sin(3-317*t)+
5/14*sin(21/16-316*t)+
9/19*sin(31/9-315*t)+
2/9*sin(13/6-314*t)+
3/5*sin(9/7-312*t)+
2/5*sin(49/12-311*t)+
1/13*sin(30/7-310*t)+
4/13*sin(19/12-309*t)+
1/3*sin(32/7-307*t)+
5/8*sin(22/5-306*t)+
4/11*sin(25/11-305*t)+
8/15*sin(9/8-304*t)+
1/8*sin(35/9-303*t)+
3/5*sin(51/25-302*t)+
2/5*sin(9/8-301*t)+
4/7*sin(2/7-300*t)+
2/7*sin(50/11-299*t)+
3/13*sin(35/8-297*t)+
5/14*sin(14/5-295*t)+
8/13*sin(47/14-294*t)+
2/9*sin(25/8-293*t)+
8/17*sin(136/45-291*t)+
2/7*sin(17/7-290*t)+
3/5*sin(8/7-288*t)+
3/13*sin(19/8-286*t)+
6/11*sin(10/19-285*t)+
9/10*sin(121/40-283*t)+
8/5*sin(21/5-282*t)+
1/10*sin(87/25-281*t)+
7/13*sin(22/7-279*t)+
3/7*sin(8/5-278*t)+
4/5*sin(3/14-277*t)+
7/10*sin(19/13-276*t)+
1/5*sin(6/13-274*t)+
7/10*sin(20/9-273*t)+
1/3*sin(9/4-272*t)+
4/13*sin(47/11-271*t)+
18/17*sin(22/7-269*t)+
1/7*sin(31/9-268*t)+
7/10*sin(43/17-267*t)+
8/11*sin(24/7-266*t)+
5/8*sin(13/6-264*t)+
9/10*sin(17/13-262*t)+
4/11*sin(31/8-261*t)+
1/5*sin(66/19-260*t)+
1/10*sin(23/5-259*t)+
3/10*sin(66/19-255*t)+
1/8*sin(6/7-253*t)+
9/13*sin(16/5-252*t)+
3/7*sin(8/9-251*t)+
4/11*sin(30/13-250*t)+
7/11*sin(66/19-247*t)+
1/19*sin(2-246*t)+
1/4*sin(16/7-245*t)+
8/17*sin(41/10-244*t)+
15/16*sin(2/11-240*t)+
5/7*sin(19/18-239*t)+
1/6*sin(5/12-238*t)+
5/11*sin(16/17-236*t)+
3/10*sin(25/12-235*t)+
8/17*sin(16/7-233*t)+
5/8*sin(47/12-231*t)+
9/11*sin(11/8-230*t)+
3/11*sin(33/7-229*t)+
9/10*sin(20/7-226*t)+
4/9*sin(39/14-225*t)+
4/9*sin(10/9-224*t)+
6/7*sin(19/13-222*t)+
7/9*sin(29/7-221*t)+
8/11*sin(33/8-220*t)+
16/9*sin(2/7-219*t)+
25/14*sin(1/8-218*t)+
8/11*sin(5/9-217*t)+
9/11*sin(11/10-216*t)+
21/13*sin(27/7-215*t)+
3/7*sin(1/12-213*t)+
13/9*sin(15/16-212*t)+
23/8*sin(1/8-210*t)+
sin(32/11-209*t)+
9/13*sin(1/9-208*t)+
7/9*sin(33/10-206*t)+
2/3*sin(9/4-205*t)+
3/4*sin(1/2-204*t)+
3/13*sin(11/17-203*t)+
3/7*sin(31/12-202*t)+
19/12*sin(17/8-201*t)+
7/8*sin(75/19-200*t)+
6/5*sin(21/10-198*t)+
3/2*sin(7/5-194*t)+
28/27*sin(3/2-193*t)+
4/9*sin(16/5-192*t)+
22/13*sin(13/6-189*t)+
18/11*sin(19/10-188*t)+
sin(7/6-187*t)+
16/7*sin(13/11-186*t)+
9/5*sin(11/9-184*t)+
16/11*sin(2/5-183*t)+
10/13*sin(10/3-182*t)+
9/7*sin(38/9-181*t)+
45/13*sin(8/9-180*t)+
7/9*sin(35/8-179*t)+
2/3*sin(35/8-176*t)+
10/7*sin(6/19-175*t)+
40/13*sin(15/7-174*t)+
20/13*sin(1/2-173*t)+
3/11*sin(20/7-171*t)+
17/16*sin(50/11-169*t)+
2/9*sin(1/31-168*t)+
4/9*sin(7/2-165*t)+
1/12*sin(26/17-164*t)+
21/22*sin(27/26-163*t)+
13/12*sin(17/8-162*t)+
19/14*sin(39/10-160*t)+
18/11*sin(5/7-159*t)+
3/5*sin(15/14-158*t)+
11/9*sin(35/8-157*t)+
5/8*sin(30/7-156*t)+
3/2*sin(28/11-155*t)+
4/5*sin(5/11-151*t)+
25/19*sin(11/10-150*t)+
10/11*sin(11/14-148*t)+
13/9*sin(7/4-147*t)+
7/13*sin(19/6-146*t)+
1/5*sin(37/14-145*t)+
11/8*sin(42/13-144*t)+
20/11*sin(32/9-143*t)+
2/3*sin(22/5-141*t)+
10/11*sin(9/7-140*t)+
8/7*sin(23/9-138*t)+
5/2*sin(9/19-137*t)+
7/5*sin(193/48-136*t)+
5/8*sin(67/66-135*t)+
8/7*sin(7/15-134*t)+
13/6*sin(13/7-133*t)+
19/7*sin(16/5-132*t)+
16/7*sin(39/11-131*t)+
28/17*sin(69/35-130*t)+
84/17*sin(7/8-129*t)+
114/23*sin(10/9-128*t)+
29/11*sin(1/7-127*t)+
63/10*sin(65/32-124*t)+
74/17*sin(37/16-121*t)+
31/16*sin(35/11-120*t)+
19/5*sin(23/12-119*t)+
82/27*sin(27/7-118*t)+
49/11*sin(8/3-117*t)+
29/14*sin(63/16-116*t)+
9/13*sin(35/8-114*t)+
29/19*sin(5/4-113*t)+
13/7*sin(20/7-112*t)+
9/7*sin(11/23-111*t)+
19/8*sin(27/26-110*t)+
sin(4/7-109*t)+
119/40*sin(22/5-108*t)+
7/5*sin(47/46-107*t)+
5/3*sin(1/6-106*t)+
2*sin(14/5-105*t)+
7/3*sin(10/3-104*t)+
3/2*sin(15/4-103*t)+
19/11*sin(3/4-102*t)+
74/17*sin(13/10-99*t)+
98/33*sin(26/11-98*t)+
36/11*sin(13/3-97*t)+
43/12*sin(26/25-96*t)+
13/2*sin(3/13-95*t)+
6/7*sin(24/7-94*t)+
16/5*sin(6/5-93*t)+
5/7*sin(9/14-92*t)+
55/12*sin(27/14-90*t)+
15/11*sin(14/3-88*t)+
7/3*sin(7/10-87*t)+
11/4*sin(2/9-86*t)+
13/4*sin(35/12-84*t)+
26/9*sin(38/9-83*t)+
7/2*sin(5/7-82*t)+
31/8*sin(27/8-78*t)+
91/6*sin(35/8-77*t)+
37/5*sin(7/10-76*t)+
70/13*sin(17/11-73*t)+
76/25*sin(56/19-70*t)+
19/8*sin(17/8-68*t)+
59/13*sin(42/17-67*t)+
28/17*sin(49/13-64*t)+
9/7*sin(79/17-63*t)+
1/8*sin(7/11-62*t)+
39/8*sin(49/15-61*t)+
53/18*sin(33/8-59*t)+
9/7*sin(41/9-58*t)+
8/7*sin(65/14-57*t)+
10/11*sin(16/7-56*t)+
68/13*sin(42/13-55*t)+
21/10*sin(7/8-54*t)+
6/7*sin(41/14-53*t)+
31/11*sin(55/12-51*t)+
59/17*sin(27/7-50*t)+
124/9*sin(37/11-49*t)+
24/11*sin(3/5-48*t)+
65/6*sin(12/5-47*t)+
11/7*sin(49/11-45*t)+
13/25*sin(11/13-42*t)+
7/4*sin(5/8-40*t)+
43/42*sin(2/5-39*t)+
20/9*sin(4/7-38*t)+
19/8*sin(4/11-37*t)+
5/4*sin(15/4-36*t)+
1/5*sin(11/13-34*t)+
12/7*sin(23/5-32*t)+
409/34*sin(39/10-31*t)+
10/7*sin(5/2-30*t)+
180/11*sin(3-29*t)+
23/8*sin(53/12-26*t)+
71/8*sin(56/13-25*t)+
12/5*sin(10/21-24*t)+
10/3*sin(34/9-22*t)+
27/16*sin(12/11-21*t)+
49/6*sin(13/7-20*t)+
69/2*sin(19/14-19*t)+
475/9*sin(3/10-17*t)+
68/13*sin(57/28-16*t)+
40/17*sin(1/6-15*t)+
77/13*sin(29/11-12*t)+
4954/39*sin(15/4-11*t)+
1075/11*sin(4-5*t)+
191/24*sin(5/4-4*t)+
84/17*sin(2/7-3*t)-
12/5*sin(74*t)-
4/5*sin(166*t)-
1523/3*sin(t+12/11)-
25/3*sin(2*t+17/18)-
13/8*sin(6*t+1/9)-
5333/62*sin(7*t+9/7)-
56/9*sin(8*t+5/12)-
65/8*sin(9*t+2/5)-
106/9*sin(10*t+1/8)-
1006/9*sin(13*t+11/7)-
67/8*sin(14*t+6/5)-
25/8*sin(18*t+15/11)-
40/11*sin(23*t+1/16)-
4/7*sin(27*t+6/5)-
41/8*sin(28*t+7/12)-
8/5*sin(33*t+5/6)-
137/17*sin(35*t+4/5)-
29/12*sin(41*t+22/15)-
25/9*sin(43*t+6/7)-
12/25*sin(44*t+16/11)-
31/6*sin(46*t+4/3)-
19/5*sin(52*t+16/13)-
19/11*sin(60*t+8/17)-
16/7*sin(65*t+6/13)-
25/12*sin(66*t+11/13)-
8/9*sin(69*t+4/11)-
25/7*sin(71*t+7/5)-
11/10*sin(72*t+3/2)-
14/5*sin(75*t+7/9)-
107/14*sin(79*t+3/4)-
67/8*sin(80*t+2/11)-
161/27*sin(81*t+5/11)-
55/18*sin(85*t+3/7)-
161/40*sin(89*t+1/21)-
32/7*sin(91*t+38/25)-
sin(100*t+19/20)-
27/5*sin(101*t+2/13)-
26/9*sin(115*t+1/44)-
17/11*sin(122*t+1/16)-
87/22*sin(123*t+2/3)-
37/8*sin(125*t+9/11)-
10/7*sin(126*t+8/7)-
7/8*sin(139*t+3/5)-
3/7*sin(142*t+5/6)-
71/36*sin(149*t+5/16)-
7/6*sin(152*t+1/9)-
63/25*sin(153*t+29/19)-
27/20*sin(154*t+8/15)-
8/15*sin(161*t+12/13)-
5/3*sin(167*t+13/10)-
17/25*sin(170*t+3/5)-
10/9*sin(172*t+3/8)-
5/7*sin(177*t+5/8)-
1/2*sin(178*t+7/6)-
34/13*sin(185*t+5/8)-
11/13*sin(190*t+38/39)-
25/19*sin(191*t+11/8)-
11/12*sin(195*t+18/19)-
51/26*sin(196*t+2/7)-
14/9*sin(197*t+4/11)-
19/12*sin(199*t+1)-
19/11*sin(207*t+11/8)-
6/11*sin(211*t+1/20)-
11/7*sin(214*t+1/14)-
7/13*sin(223*t+8/11)-
3/5*sin(227*t+12/13)-
4/5*sin(228*t+29/19)-
11/10*sin(232*t+2/7)-
1/6*sin(234*t+7/11)-
sin(237*t+60/59)-
5/11*sin(241*t+7/8)-
1/2*sin(242*t+8/7)-
7/15*sin(243*t+15/16)-
5/8*sin(248*t+2/3)-
1/3*sin(249*t+4/11)-
2/3*sin(254*t+8/7)-
10/19*sin(256*t+14/11)-
4/9*sin(257*t+8/11)-
3/4*sin(258*t+3/7)-
sin(263*t+2/7)-
3/10*sin(265*t+1/28)-
1/2*sin(270*t+1)-
12/13*sin(275*t+5/8)-
1/4*sin(280*t+16/13)-
1/10*sin(284*t+5/8)-
13/25*sin(287*t+3/7)-
9/13*sin(289*t+3/5)-
22/23*sin(292*t+17/13)-
9/11*sin(296*t+17/11)-
3/7*sin(298*t+12/11)-
5/6*sin(308*t+1/2)-
7/15*sin(313*t+1/3)

        setRubberPoint("POLYGON_POINT_" + i.toString(), xx*xScale, yy*yScale)
    }

    setRubberText("POLYGON_NUM_POINTS", numPts.toString())


class Star():
    r"""
    """
    def __init__(self):
        clearSelection()
        self.numPoints = 5
        self.modes = ["NUM_POINTS", "CENTER_PT", "RAD_OUTER", "RAD_INNER"]
        self.cx = MAX_DISTANCE+1.0
        self.cy = MAX_DISTANCE+1.0
        self.x1 = MAX_DISTANCE+1.0
        self.y1 = MAX_DISTANCE+1.0
        self.x2 = MAX_DISTANCE+1.0
        self.y2 = MAX_DISTANCE+1.0
        self.mode = self.mode_NUM_POINTS
        setPromptPrefix(translate("Enter number of star points")
            + " " + self.numPoints.toString() + "}: ")
        return self

def click(self, x, y):
    if self.mode == self.mode_NUM_POINTS:
        #Do nothing, the prompt controls this.
    elif self.mode == self.mode_CENTER_PT:
        self.cx = x
        self.cy = y
        self.mode = self.mode_RAD_OUTER
        setPromptPrefix(translate("Specify outer radius of star: "))
        addRubber("POLYGON")
        setRubberMode("POLYGON")
        updateStar(self.cx, self.cy)
        enableMoveRapidFire()
    elif self.mode == self.mode_RAD_OUTER:
        self.x1 = x
        self.y1 = y
        self.mode = self.mode_RAD_INNER
        setPromptPrefix(translate("Specify inner radius of star: "))
        updateStar(self.x1, self.y1)
    elif self.mode == self.mode_RAD_INNER:
        self.x2 = x
        self.y2 = y
        disableMoveRapidFire()
        updateStar(self.x2, self.y2)
        spareRubber("POLYGON")

    def move(self, x, y):
        if self.mode == "NUM_POINTS":
            #Do nothing, the prompt controls this.
        elif self.mode == "CENTER_PT":
            #Do nothing, prompt and click controls this.
        elif self.mode == "RAD_OUTER" or self.mode == "RAD_INNER":
            self.updateStar(x, y)

def prompt(cmd):
    if self.mode == "NUM_POINTS":
        if str == "" and self.numPoints >= 3 and self.numPoints <= 1024:
            setPromptPrefix(translate("Specify center point: "))
            self.mode = self.mode_CENTER_PT
        else:
            tmp = Number(cmd)
            if isNaN(tmp) or !isInt(tmp) or tmp < 3 or tmp > 1024:
                alert(translate("Requires an integer between 3 and 1024."))
                setPromptPrefix(translate("Enter number of star points")
                    + " " + self.numPoints.toString() + "}: ")
            else:
                self.numPoints = tmp
                setPromptPrefix(translate("Specify center point: "))
                self.mode = "CENTER_PT"

    elif self.mode == "CENTER_PT":
        strList = str.split(",")
        if isNaN(strList[0]) or isNaN(strList[1]):
            alert(translate("Invalid point."))
            setPromptPrefix(translate("Specify center point: "))
        else:
            self.cx = Number(strList[0])
            self.cy = Number(strList[1])
            self.mode = "RAD_OUTER"
            setPromptPrefix(translate("Specify outer radius of star: "))
            addRubber("POLYGON")
            setRubberMode("POLYGON")
            updateStar(qsnapX(), qsnapY())
            enableMoveRapidFire()

    elif self.mode == "RAD_OUTER":
        strList = str.split(",")
        if isNaN(strList[0]) or isNaN(strList[1]):
            alert(translate("Invalid point."))
            setPromptPrefix(translate("Specify outer radius of star: "))
        else:
            self.x1 = Number(strList[0])
            self.y1 = Number(strList[1])
            self.mode = self.mode_RAD_INNER
            setPromptPrefix(translate("Specify inner radius of star: "))
            updateStar(qsnapX(), qsnapY())

    elif self.mode == self.mode_RAD_INNER:
        strList = str.split(",")
        if isNaN(strList[0]) or isNaN(strList[1]):
            alert(translate("Invalid point."))
            setPromptPrefix(translate("Specify inner radius of star: "))
        else:
            self.x2 = Number(strList[0])
            self.y2 = Number(strList[1])
            disableMoveRapidFire()
            updateStar(self.x2, self.y2)
            spareRubber("POLYGON")


def updateStar(self, x, y):
    distOuter
    distInner
    angOuter

    if self.mode == self.mode_RAD_OUTER:
        angOuter = calculateAngle(self.cx, self.cy, x, y)
        distOuter = calculateDistance(self.cx, self.cy, x, y)
        distInner = distOuter/2.0
    elif self.mode == self.mode_RAD_INNER:
        angOuter = calculateAngle(self.cx, self.cy, self.x1, self.y1)
        distOuter = calculateDistance(self.cx, self.cy, self.x1, self.y1)
        distInner = calculateDistance(self.cx, self.cy, x, y)

    #Calculate the Star Points
    angInc = 360.0/(self.numPoints*2)
    for i in range(self.numPoints*2):
        # if odd
        if i%2 == 1:
            xx = distOuter*cos((angOuter+(angInc*i))*math.pi/180.0)
            yy = distOuter*sin((angOuter+(angInc*i))*math.pi/180.0)
        else:
            xx = distInner*cos((angOuter+(angInc*i))*embConstantPi/180.0)
            yy = distInner*sin((angOuter+(angInc*i))*embConstantPi/180.0)
        setRubberPoint("POLYGON_POINT_" + i.toString(), self.cx + xx, self.cy + yy)
    setRubberText("POLYGON_NUM_POINTS", (self.numPoints*2 - 1).toString())


class SysWindows():
    r"""
    "menu-name": "None",
    "menu-position": 0,
    "toolbar-name": "None",
    "toolbar-position": 0,
    "tooltip": "&SysWindows",
    "statustip": "Arrange the windows:  SYSWINDOWS",
    "alias": "WINDOWS, SYSWINDOWS"
    """
    def __init__(self):
        clearSelection()
        setPromptPrefix(translate("Enter an option [Cascade/Tile]: "))

    def prompt(self, cmd):
        if cmd == "C" or cmd == "CASCADE":
            # TODO: Probably should add additional qsTr calls here.
            windowCascade()
        elif cmd == "T" or cmd == "TILE":
            #TODO: Probably should add additional qsTr calls here.
            windowTile()
        else
            alert(translate("Invalid option keyword."))
            setPromptPrefix(translate("Enter an option [Cascade/Tile]: "))


class Treble_Clef(Base_Object):
    r"""
    """
    def __init__(self):
        " Default //TODO: min:64 max:8192 ."
        clearSelection()
        self.cx = MAX_DISTANCE+1.0
        self.cy = MAX_DISTANCE+1.0
        self.numPoints = 1024
        self.sx = 0.04
        self.sy = 0.04
        self.mode = TREBLE_CLEF_MODE_NUM_POINTS

        addRubber("POLYGON")
        setRubberMode("POLYGON")
        updateClef(self.numPoints, self.sx, self.sy)
        spareRubber("POLYGON")
        return self

    def updateClef(self, numPts, xScale, yScale):

        for i in range(numPts+1):
            t = (16*embConstantPi)/numPts*i

            xx = ((-1/12*sin(215/214-18*t)-
        9/17*sin(23/17-12*t)-
        15/22*sin(34/33-10*t)-
        10/13*sin(11/13-8*t)-
        22/29*sin(23/19-6*t)+
        1777/23*sin(t+52/21)+
        279/16*sin(2*t+113/26)+
        97/12*sin(3*t+43/20)+
        35/13*sin(4*t+93/22)+
        34/11*sin(5*t+47/26)+
        29/19*sin(7*t+29/19)+
        23/34*sin(9*t+13/10)+
        2/9*sin(11*t+369/185)+
        1/6*sin(13*t+38/15)+
        4/11*sin(14*t+37/8)+
        7/23*sin(15*t+44/21)+
        2/19*sin(16*t+132/29)+
        5/16*sin(17*t+58/27)+2121/22)*
        theta(15*embConstantPi-t)*
        theta(t-11*embConstantPi)+
        (-21/23*sin(3/19-18*t)-
        18/55*sin(34/25-15*t)-
        47/16*sin(19/33-13*t)-
        2094/53*sin(29/28-3*t)+
        2692/27*sin(t+89/41)+
        2331/22*sin(2*t+17/16)+
        2226/73*sin(4*t+7/20)+
        257/19*sin(5*t+53/20)+
        128/11*sin(6*t+40/11)+
        101/11*sin(7*t+85/22)+
        163/30*sin(8*t+50/11)+
        24/13*sin(9*t+11/14)+
        77/23*sin(10*t+34/15)+
        8/47*sin(11*t+41/14)+
        1/112*sin(12*t+29/26)+
        31/11*sin(14*t+12/19)+
        5/19*sin(16*t+11/19)+
        48/29*sin(17*t+46/11)+
        35/44*sin(19*t+191/82)+
        13/15*sin(20*t+62/33)+
        29/25*sin(21*t+27/10)+
        11/45*sin(22*t+104/25)+
        42/85*sin(23*t+3/16)+
        1/2*sin(24*t+29/28)-2503/17)*
        theta(11*embConstantPi-t)*
        theta(t-7*embConstantPi)+
        (-3/4*sin(13/14-6*t)-
        29/14*sin(23/40-4*t)-
        693/65*sin(7/17-2*t)+
        1869/20*sin(t+137/38)+
        79/11*sin(3*t+36/11)+
        38/15*sin(5*t+28/9)+
        79/63*sin(7*t+41/14)+
        16/63*sin(8*t+275/61)-1053/43)*
        theta(7*embConstantPi-t)*
        theta(t-3*embConstantPi)+
        (-7/11*sin(34/31-38*t)-
        199/99*sin(3/13-32*t)-
        26/23*sin(2/25-26*t)-
        127/39*sin(130/87-17*t)-
        49/13*sin(15/13-16*t)-
        231/37*sin(7/15-14*t)-
        113/10*sin(3/29-12*t)-
        1242/29*sin(12/25-6*t)-
        1433/32*sin(12/11-4*t)-
        1361/10*sin(22/21-3*t)-
        577/7*sin(1/9-2*t)+
        6392/35*sin(t+87/28)+
        3316/67*sin(5*t+26/9)+
        864/29*sin(7*t+13/18)+
        376/11*sin(8*t+19/16)+
        13/9*sin(9*t+14/15)+
        187/18*sin(10*t+35/34)+
        1826/203*sin(11*t+10/19)+
        317/36*sin(13*t+14/23)+
        221/59*sin(15*t+47/11)+
        43/27*sin(18*t+16/13)+
        47/21*sin(19*t+44/13)+
        26/7*sin(20*t+57/13)+
        35/27*sin(21*t+47/12)+
        57/29*sin(22*t+77/17)+
        53/37*sin(23*t+51/19)+
        41/22*sin(24*t+30/19)+
        47/28*sin(25*t+52/15)+
        13/16*sin(27*t+15/16)+
        11/54*sin(28*t+61/49)+
        31/20*sin(29*t+16/17)+
        12/25*sin(30*t+17/13)+
        11/20*sin(31*t+59/14)+
        5/21*sin(33*t+7/3)+
        7/25*sin(34*t+397/99)+
        7/19*sin(35*t+61/14)+
        12/19*sin(36*t+65/23)+
        12/25*sin(37*t+77/17)+
        9/13*sin(39*t+383/128)+
        7/13*sin(40*t+41/11)+
        7/10*sin(41*t+22/7)+
        1/13*sin(42*t+7/4)+
        4/21*sin(43*t+9/2)+
        13/35*sin(44*t+63/34)+
        3/16*sin(45*t+137/68)+
        2/23*sin(46*t+237/59)+
        2/7*sin(47*t+43/21)-727/14)*
        theta(3*embConstantPi-t)*
        theta(t+embConstantPi))*
        theta(sqrt(sgn(sin(t/2))))

            yy = ((-1/43*sin(21/17-14*t)-
        7/20*sin(2/11-12*t)-
        15/22*sin(53/40-11*t)-
        37/73*sin(11/21-9*t)+
        2072/13*sin(t+109/25)+
        47/7*sin(2*t+83/26)+
        193/17*sin(3*t+91/24)+
        203/45*sin(4*t+61/28)+
        52/23*sin(5*t+233/78)+
        37/13*sin(6*t+47/30)+
        8/17*sin(7*t+17/10)+
        11/7*sin(8*t+28/29)+
        5/6*sin(10*t+11/27)+
        2/3*sin(13*t+84/19)+
        22/45*sin(15*t+82/21)+
        5/21*sin(16*t+25/12)+
        8/25*sin(17*t+37/11)+
        10/29*sin(18*t+18/11)-2967/17)*
        theta(15*embConstantPi-t)*
        theta(t-11*embConstantPi)+
        (-14/17*sin(3/11-15*t)-
        123/44*sin(9/7-11*t)-
        97/34*sin(4/13-10*t)-
        157/23*sin(22/15-7*t)+
        4709/23*sin(t+122/27)+
        3533/21*sin(2*t+105/52)+
        1400/27*sin(3*t+65/24)+
        1141/39*sin(4*t+55/19)+
        150/11*sin(5*t+266/59)+
        205/39*sin(6*t+28/19)+
        18/7*sin(8*t+11/9)+
        124/17*sin(9*t+131/28)+
        11/6*sin(12*t+13/17)+
        35/27*sin(13*t+58/15)+
        15/26*sin(14*t+10/13)+
        87/43*sin(16*t+33/29)+
        17/24*sin(17*t+32/25)+
        38/31*sin(18*t+31/17)+
        25/29*sin(19*t+193/42)+
        11/17*sin(20*t+21/23)+
        6/11*sin(21*t+67/15)+
        24/29*sin(22*t+36/19)+
        61/51*sin(23*t+80/21)+
        1/5*sin(24*t+37/11)-1831/17)*
        theta(11*embConstantPi-t)*
        theta(t-7*embConstantPi)+
        (2588/15*sin(t+14/3)+
        101/26*sin(2*t+65/23)+
        6273/392*sin(3*t+101/24)+
        65/33*sin(4*t+27/8)+
        201/40*sin(5*t+89/23)+
        31/26*sin(6*t+31/10)+
        17/7*sin(7*t+97/28)+
        17/19*sin(8*t+161/54)+6478/9)*
        theta(7*embConstantPi-t)*
        theta(t-3*embConstantPi)+
        (-21/52*sin(13/14-45*t)-
        11/20*sin(20/19-44*t)-
        9/35*sin(5/18-41*t)-
        13/66*sin(18/23-39*t)-
        5/16*sin(3/28-38*t)-
        3/23*sin(29/26-35*t)-
        19/47*sin(5/16-32*t)-
        6/17*sin(134/89-31*t)-
        39/49*sin(21/23-25*t)-
        47/23*sin(19/22-19*t)-
        23/10*sin(11/38-13*t)-
        1229/25*sin(17/21-3*t)+
        11043/13*sin(t+61/13)+
        1837/12*sin(2*t+25/18)+
        1030/13*sin(4*t+41/25)+
        1425/37*sin(5*t+22/9)+
        1525/28*sin(6*t+5/3)+
        796/31*sin(7*t+35/26)+
        803/43*sin(8*t+11/7)+
        267/28*sin(9*t+51/11)+
        108/17*sin(10*t+23/18)+
        196/31*sin(11*t+83/34)+
        123/26*sin(12*t+33/16)+
        124/33*sin(14*t+41/29)+
        39/10*sin(15*t+47/12)+
        18/37*sin(16*t+21/17)+
        77/27*sin(17*t+47/22)+
        64/23*sin(18*t+52/25)+
        28/9*sin(20*t+21/62)+
        7/12*sin(21*t+93/29)+
        8/41*sin(22*t+23/15)+
        12/29*sin(23*t+29/25)+
        29/20*sin(24*t+5/4)+
        46/27*sin(26*t+7/36)+
        21/41*sin(27*t+62/17)+
        29/33*sin(28*t+70/19)+
        15/19*sin(29*t+61/15)+
        29/39*sin(30*t+17/15)+
        33/41*sin(33*t+76/21)+
        17/30*sin(34*t+56/17)+
        9/10*sin(36*t+33/29)+
        2/13*sin(37*t+21/8)+
        1/65*sin(40*t+11/20)+
        3/4*sin(42*t+14/15)+
        1/12*sin(43*t+59/58)+
        2/9*sin(46*t+50/21)+
        8/39*sin(47*t+56/17)-1223/15)*
        theta(3*embConstantPi-t)*
        theta(t+embConstantPi))*
        theta(sqrt(sgn(sin(t/2))))

            setRubberPoint("POLYGON_POINT_" + i.toString(), xx*xScale, yy*yScale)

    setRubberText("POLYGON_NUM_POINTS", numPts.toString())
