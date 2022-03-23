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


class BaseObject : public QGraphicsPathItem:
public:
    BaseObject(QGraphicsItem* parent = 0)
    virtual ~BaseObject()

    enum { Type = OBJ_TYPE_BASE ]
    virtual int type() const { return Type; }

    QPen objectPen()   const { return objPen; }
    QColor   objectColor() const { return objPen.color(); }
    unsigned int objectColorRGB()  const { return objPen.color().rgb(); }
    Qt::PenStyle objectLineType()  const { return objPen.style(); }
    float    objectLineWeight()    const { return lwtPen.widthF(); }
    QPainterPath objectPath()  const { return path(); }
    int  objectRubberMode()    const { return objRubberMode; }
    QPointF  objectRubberPoint(const QString& key) const
    QString  objectRubberText(const QString& key) const

    QRectF rect() const { return path().boundingRect(); }
    void setRect(const QRectF& r) { QPainterPath p; p.addRect(r); setPath(p); }
    void setRect(float x, float y, float w, float h) { QPainterPath p; p.addRect(x,y,w,h); setPath(p); }
    QLineF line() const { return objLine; }
    void setLine(const QLineF& li) { QPainterPath p; p.moveTo(li.p1()); p.lineTo(li.p2()); setPath(p); objLine = li; }
    void setLine(float x1, float y1, float x2, float y2) { QPainterPath p; p.moveTo(x1,y1); p.lineTo(x2,y2); setPath(p); objLine.setLine(x1,y1,x2,y2); }

    void setObjectColor(const QColor& color)
    void setObjectColorRGB(unsigned int rgb)
    void setObjectLineType(Qt::PenStyle lineType)
    void setObjectLineWeight(float lineWeight)
    void setObjectPath(const QPainterPath& p) { setPath(p); }
    void setObjectRubberMode(int mode) { objRubberMode = mode; }
    void setObjectRubberPoint(const QString& key, const QPointF& point) { objRubberPoints.insert(key, point); }
    void setObjectRubberText(const QString& key, const QString& txt) { objRubberTexts.insert(key, txt); }

    virtual QRectF boundingRect() const
    virtual QPainterPath shape() const { return path(); }

    void drawRubberLine(const QLineF& rubLine, QPainter* painter = 0, const char* colorFromScene = 0)

    virtual void vulcanize() = 0
    virtual QPointF mouseSnapPoint(const QPointF& mousePoint) = 0
    virtual QList<QPointF> allGripPoints() = 0
    virtual void gripEdit(const QPointF& before, const QPointF& after) = 0
    
    QPen objPen
    QPen lwtPen
    QLineF objLine
    int objRubberMode
    QHash<QString, QPointF> objRubberPoints
    QHash<QString, QString> objRubberTexts
    int objID
protected:
    QPen lineWeightPen() const { return lwtPen; }
    void realRender(QPainter* painter, const QPainterPath& renderPath)
]

class ArcObject : public BaseObject:
public:
    ArcObject(float startX, float startY, float midX, float midY, float endX, float endY, unsigned int rgb, QGraphicsItem* parent = 0)
    ArcObject(ArcObject* obj, QGraphicsItem* parent = 0)
    ~ArcObject()

    enum { Type = OBJ_TYPE_ARC ]
    virtual int type() const { return Type; }

    QPointF objectCenter()    const { return scenePos(); }
    float   objectRadius()    const { return rect().width()/2.0*scale(); }
    float   objectStartAngle()    const
    float   objectEndAngle()  const
    QPointF objectStartPoint()    const
    QPointF objectMidPoint()  const
    QPointF objectEndPoint()  const
    float   objectArea()  const
    float   objectArcLength() const
    float   objectChord() const
    float   objectIncludedAngle() const
    int    objectClockwise() const

    void setObjectRadius(float radius)
    void setObjectStartAngle(float angle)
    void setObjectEndAngle(float angle)
    void setObjectStartPoint(float pointX, float pointY)
    void setObjectMidPoint(const QPointF& point)
    void setObjectMidPoint(float pointX, float pointY)
    void setObjectEndPoint(const QPointF& point)
    void setObjectEndPoint(float pointX, float pointY)

    void updateRubber(QPainter* painter = 0)
    virtual void vulcanize()
    virtual QPointF mouseSnapPoint(const QPointF& mousePoint)
    virtual QList<QPointF> allGripPoints()
    virtual void gripEdit(const QPointF& before, const QPointF& after)
protected:
    void paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    void init(float startX, float startY, float midX, float midY, float endX, float endY, unsigned int rgb, Qt::PenStyle lineType)
    void updatePath()

    void calculateArcData(float startX, float startY, float midX, float midY, float endX, float endY)
    void updateArcRect(float radius)

    QPointF arcStartPoint
    QPointF arcMidPoint
    QPointF arcEndPoint
]

class CircleObject : public BaseObject:
public:
    CircleObject(float centerX, float centerY, float radius, unsigned int rgb, QGraphicsItem* parent = 0)
    CircleObject(CircleObject* obj, QGraphicsItem* parent = 0)
    ~CircleObject()

    enum { Type = OBJ_TYPE_CIRCLE ]
    virtual int type() const { return Type; }

    QPainterPath objectSavePath() const

    QPointF objectCenter()    const { return scenePos(); }
    float   objectRadius()    const { return rect().width()/2.0*scale(); }
    float   objectDiameter()  const { return rect().width()*scale(); }
    float   objectArea()  const { return embConstantPi*objectRadius()*objectRadius(); }
    float   objectCircumference() const { return embConstantPi*objectDiameter(); }
    QPointF objectQuadrant0() const { return objectCenter() + QPointF(objectRadius(), 0); }
    QPointF objectQuadrant90()    const { return objectCenter() + QPointF(0,-objectRadius()); }
    QPointF objectQuadrant180()   const { return objectCenter() + QPointF(-objectRadius(),0); }
    QPointF objectQuadrant270()   const { return objectCenter() + QPointF(0, objectRadius()); }

    void setObjectRadius(float radius)
    void setObjectDiameter(float diameter)
    void setObjectArea(float area)
    void setObjectCircumference(float circumference)

    void updateRubber(QPainter* painter = 0)
    virtual void vulcanize()
    virtual QPointF mouseSnapPoint(const QPointF& mousePoint)
    virtual QList<QPointF> allGripPoints()
    virtual void gripEdit(const QPointF& before, const QPointF& after)
protected:
    void paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    void init(float centerX, float centerY, float radius, unsigned int rgb, Qt::PenStyle lineType)
    void updatePath()
]

class DimLeaderObject : public BaseObject:
public:
    DimLeaderObject(float x1, float y1, float x2, float y2, unsigned int rgb, QGraphicsItem* parent = 0)
    DimLeaderObject(DimLeaderObject* obj, QGraphicsItem* parent = 0)
    ~DimLeaderObject()

    enum ArrowStyle
    {
    NoArrow, /* NOTE: Allow this enum to evaluate false. */
    Open,
    Closed,
    Dot,
    Box,
    Tick
    ]

    enum lineStyle
    {
    NoLine, /* NOTE: Allow this enum to evaluate false. */
    Flared,
    Fletching
    ]

    enum { Type = OBJ_TYPE_DIMLEADER ]
    virtual int type() const { return Type; }

    QPointF objectEndPoint1() const
    QPointF objectEndPoint2() const
    QPointF objectMidPoint()  const
    float   objectX1()    const { return objectEndPoint1().x(); }
    float   objectY1()    const { return objectEndPoint1().y(); }
    float   objectX2()    const { return objectEndPoint2().x(); }
    float   objectY2()    const { return objectEndPoint2().y(); }
    float   objectDeltaX()    const { return (objectEndPoint2().x() - objectEndPoint1().x()); }
    float   objectDeltaY()    const { return (objectEndPoint2().y() - objectEndPoint1().y()); }
    float   objectAngle() const
    float   objectLength()    const { return line().length(); }

    void setObjectEndPoint1(EmbVector v)
    void setObjectEndPoint2(EmbVector v)

    void updateRubber(QPainter* painter = 0)
    virtual void vulcanize()
    virtual QPointF mouseSnapPoint(const QPointF& mousePoint)
    virtual QList<QPointF> allGripPoints()
    virtual void gripEdit(const QPointF& before, const QPointF& after)
protected:
    void paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    void init(float x1, float y1, float x2, float y2, unsigned int rgb, Qt::PenStyle lineType)

    int curved
    int filled
    void updateLeader()
    QPainterPath lineStylePath
    QPainterPath arrowStylePath
    float arrowStyleAngle
    float arrowStyleLength
    float lineStyleAngle
    float lineStyleLength
]

class EllipseObject : public BaseObject:
public:
    EllipseObject(float centerX, float centerY, float width, float height, unsigned int rgb, QGraphicsItem* parent = 0)
    EllipseObject(EllipseObject* obj, QGraphicsItem* parent = 0)
    ~EllipseObject()

    enum { Type = OBJ_TYPE_ELLIPSE ]
    virtual int type() const { return Type; }

    QPainterPath objectSavePath() const

    QPointF objectCenter() const { return scenePos(); }
    float   objectRadiusMajor()   const { return qMax(rect().width(), rect().height())/2.0*scale(); }
    float   objectRadiusMinor()   const { return qMin(rect().width(), rect().height())/2.0*scale(); }
    float   objectDiameterMajor() const { return qMax(rect().width(), rect().height())*scale(); }
    float   objectDiameterMinor() const { return qMin(rect().width(), rect().height())*scale(); }
    float   objectWidth() const { return rect().width()*scale(); }
    float   objectHeight()    const { return rect().height()*scale(); }
    QPointF objectQuadrant0() const
    QPointF objectQuadrant90()    const
    QPointF objectQuadrant180()   const
    QPointF objectQuadrant270()   const

    void setObjectSize(float width, float height)
    void setObjectRadiusMajor(float radius)
    void setObjectRadiusMinor(float radius)
    void setObjectDiameterMajor(float diameter)
    void setObjectDiameterMinor(float diameter)

    void updateRubber(QPainter* painter = 0)
    virtual void vulcanize()
    virtual QPointF mouseSnapPoint(const QPointF& mousePoint)
    virtual QList<QPointF> allGripPoints()
    virtual void gripEdit(const QPointF& before, const QPointF& after)
protected:
    void paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    void init(float centerX, float centerY, float width, float height, unsigned int rgb, Qt::PenStyle lineType)
    void updatePath()
]

class ImageObject : public BaseObject:
public:
    ImageObject(float x, float y, float w, float h, unsigned int rgb, QGraphicsItem* parent = 0)
    ImageObject(ImageObject* obj, QGraphicsItem* parent = 0)
    ~ImageObject()

    enum { Type = OBJ_TYPE_IMAGE ]
    virtual int type() const { return Type; }

    QPointF objectTopLeft() const
    QPointF objectTopRight()    const
    QPointF objectBottomLeft()  const
    QPointF objectBottomRight() const
    float   objectWidth()   const { return rect().width()*scale(); }
    float   objectHeight()  const { return rect().height()*scale(); }
    float   objectArea()    const { return qAbs(objectWidth()*objectHeight()); }

    void setObjectRect(float x, float y, float w, float h)

    void updateRubber(QPainter* painter = 0)
    virtual void vulcanize()
    virtual QPointF mouseSnapPoint(const QPointF& mousePoint)
    virtual QList<QPointF> allGripPoints()
    virtual void gripEdit(const QPointF& before, const QPointF& after)
protected:
    void paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    void init(float x, float y, float w, float h, unsigned int rgb, Qt::PenStyle lineType)
    void updatePath()
]


class LineObject : public BaseObject:
public:
    LineObject(float x1, float y1, float x2, float y2, unsigned int rgb, QGraphicsItem* parent = 0)
    LineObject(LineObject* obj, QGraphicsItem* parent = 0)
    ~LineObject()

    enum { Type = OBJ_TYPE_LINE ]
    virtual int type() const { return Type; }

    QPainterPath objectSavePath() const

    QPointF objectEndPoint1() const { return scenePos(); }
    QPointF objectEndPoint2() const
    QPointF objectMidPoint()  const
    float   objectX1()    const { return objectEndPoint1().x(); }
    float   objectY1()    const { return objectEndPoint1().y(); }
    float   objectX2()    const { return objectEndPoint2().x(); }
    float   objectY2()    const { return objectEndPoint2().y(); }
    float   objectDeltaX()    const { return (objectEndPoint2().x() - objectEndPoint1().x()); }
    float   objectDeltaY()    const { return (objectEndPoint2().y() - objectEndPoint1().y()); }
    float   objectAngle() const
    float   objectLength()    const { return line().length()*scale(); }

    void setObjectEndPoint1(const QPointF& endPt1)
    void setObjectEndPoint1(float x1, float y1)
    void setObjectEndPoint2(const QPointF& endPt2)
    void setObjectEndPoint2(float x2, float y2)
    void setObjectX1(float x) { setObjectEndPoint1(x, objectEndPoint1().y()); }
    void setObjectY1(float y) { setObjectEndPoint1(objectEndPoint1().x(), y); }
    void setObjectX2(float x) { setObjectEndPoint2(x, objectEndPoint2().y()); }
    void setObjectY2(float y) { setObjectEndPoint2(objectEndPoint2().x(), y); }

    void updateRubber(QPainter* painter = 0)
    virtual void vulcanize()
    virtual QPointF mouseSnapPoint(const QPointF& mousePoint)
    virtual QList<QPointF> allGripPoints()
    virtual void gripEdit(const QPointF& before, const QPointF& after)
protected:
    void paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    void init(float x1, float y1, float x2, float y2, unsigned int rgb, Qt::PenStyle lineType)
]

class PathObject : public BaseObject:
public:
    PathObject(float x, float y, const QPainterPath p, unsigned int rgb, QGraphicsItem* parent = 0)
    PathObject(PathObject* obj, QGraphicsItem* parent = 0)
    ~PathObject()

    enum { Type = OBJ_TYPE_PATH ]
    virtual int type() const { return Type; }

    QPainterPath objectCopyPath() const
    QPainterPath objectSavePath() const

    QPointF objectPos() const { return scenePos(); }
    float   objectX()   const { return scenePos().x(); }
    float   objectY()   const { return scenePos().y(); }

    void setObjectPos(const QPointF& point) { setPos(point.x(), point.y()); }
    void setObjectPos(float x, float y) { setPos(x, y); }
    void setObjectX(float x) { setObjectPos(x, objectY()); }
    void setObjectY(float y) { setObjectPos(objectX(), y); }

    void updateRubber(QPainter* painter = 0)
    virtual void vulcanize()
    virtual QPointF mouseSnapPoint(const QPointF& mousePoint)
    virtual QList<QPointF> allGripPoints()
    virtual void gripEdit(const QPointF& before, const QPointF& after)
protected:
    void paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    void init(float x, float y, const QPainterPath& p, unsigned int rgb, Qt::PenStyle lineType)
    void updatePath(const QPainterPath& p)
    QPainterPath normalPath
    /*TODO: make paths similar to polylines. Review and implement any missing functions/members.*/
]

class PointObject : public BaseObject:
public:
    PointObject(float x, float y, unsigned int rgb, QGraphicsItem* parent = 0)
    PointObject(PointObject* obj, QGraphicsItem* parent = 0)
    ~PointObject()

    enum { Type = OBJ_TYPE_POINT ]
    virtual int type() const { return Type; }

    QPainterPath objectSavePath() const

    QPointF objectPos() const { return scenePos(); }
    float   objectX()   const { return scenePos().x(); }
    float   objectY()   const { return scenePos().y(); }

    void setObjectPos(const QPointF& point) { setPos(point.x(), point.y()); }
    void setObjectPos(float x, float y) { setPos(x, y); }
    void setObjectX(float x) { setObjectPos(x, objectY()); }
    void setObjectY(float y) { setObjectPos(objectX(), y); }

    void updateRubber(QPainter* painter = 0)
    virtual void vulcanize()
    virtual QPointF mouseSnapPoint(const QPointF& mousePoint)
    virtual QList<QPointF> allGripPoints()
    virtual void gripEdit(const QPointF& before, const QPointF& after)
protected:
    void paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    void init(float x, float y, unsigned int rgb, Qt::PenStyle lineType)
]


class PolygonObject : public BaseObject:
public:
    PolygonObject(float x, float y, const QPainterPath& p, unsigned int rgb, QGraphicsItem* parent = 0)
    PolygonObject(PolygonObject* obj, QGraphicsItem* parent = 0)
    ~PolygonObject()

    enum { Type = OBJ_TYPE_POLYGON ]
    virtual int type() const { return Type; }

    QPainterPath objectCopyPath() const
    QPainterPath objectSavePath() const

    QPointF objectPos() const { return scenePos(); }
    float   objectX()   const { return scenePos().x(); }
    float   objectY()   const { return scenePos().y(); }

    void setObjectPos(const QPointF& point) { setPos(point.x(), point.y()); }
    void setObjectPos(float x, float y) { setPos(x, y); }
    void setObjectX(float x) { setObjectPos(x, objectY()); }
    void setObjectY(float y) { setObjectPos(objectX(), y); }

    void updateRubber(QPainter* painter = 0)
    virtual void vulcanize()
    virtual QPointF mouseSnapPoint(const QPointF& mousePoint)
    virtual QList<QPointF> allGripPoints()
    virtual void gripEdit(const QPointF& before, const QPointF& after)
protected:
    void paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    void init(float x, float y, const QPainterPath& p, unsigned int rgb, Qt::PenStyle lineType)
    void updatePath(const QPainterPath& p)
    QPainterPath normalPath
    int findIndex(const QPointF& point)
    int gripIndex
]


class PolylineObject : public BaseObject:
public:
    PolylineObject(float x, float y, const QPainterPath& p, unsigned int rgb, QGraphicsItem* parent = 0)
    PolylineObject(PolylineObject* obj, QGraphicsItem* parent = 0)
    ~PolylineObject()

    enum { Type = OBJ_TYPE_POLYLINE ]
    virtual int type() const { return Type; }

    QPainterPath objectCopyPath() const
    QPainterPath objectSavePath() const

    QPointF objectPos() const { return scenePos(); }
    float   objectX()   const { return scenePos().x(); }
    float   objectY()   const { return scenePos().y(); }

    void setObjectPos(const QPointF& point) { setPos(point.x(), point.y()); }
    void setObjectPos(float x, float y) { setPos(x, y); }
    void setObjectX(float x) { setObjectPos(x, objectY()); }
    void setObjectY(float y) { setObjectPos(objectX(), y); }

    void updateRubber(QPainter* painter = 0)
    virtual void vulcanize()
    virtual QPointF mouseSnapPoint(const QPointF& mousePoint)
    virtual QList<QPointF> allGripPoints()
    virtual void gripEdit(const QPointF& before, const QPointF& after)
protected:
    void paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    void init(float x, float y, const QPainterPath& p, unsigned int rgb, Qt::PenStyle lineType)
    void updatePath(const QPainterPath& p)
    QPainterPath normalPath
    int findIndex(const QPointF& point)
    int gripIndex
]


class RectObject : public BaseObject:
public:
    RectObject(float x, float y, float w, float h, unsigned int rgb, QGraphicsItem* parent = 0)
    RectObject(RectObject* obj, QGraphicsItem* parent = 0)
    ~RectObject()

    enum { Type = OBJ_TYPE_RECTANGLE ]
    virtual int type() const { return Type; }

    QPainterPath objectSavePath() const

    QPointF objectPos() const { return scenePos(); }

    QPointF objectTopLeft() const
    QPointF objectTopRight()    const
    QPointF objectBottomLeft()  const
    QPointF objectBottomRight() const
    float   objectWidth()   const { return rect().width()*scale(); }
    float   objectHeight()  const { return rect().height()*scale(); }
    float   objectArea()    const { return qAbs(objectWidth()*objectHeight()); }

    void setObjectRect(float x, float y, float w, float h)

    void updateRubber(QPainter* painter = 0)
    virtual void vulcanize()
    virtual QPointF mouseSnapPoint(const QPointF& mousePoint)
    virtual QList<QPointF> allGripPoints()
    virtual void gripEdit(const QPointF& before, const QPointF& after)
protected:
    void paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    void init(float x, float y, float w, float h, unsigned int rgb, Qt::PenStyle lineType)
    void updatePath()
]


class TextSingleObject : public BaseObject:
public:
    TextSingleObject(const QString& str, float x, float y, unsigned int rgb, QGraphicsItem* parent = 0)
    TextSingleObject(TextSingleObject* obj, QGraphicsItem* parent = 0)
    ~TextSingleObject()

    enum { Type = OBJ_TYPE_TEXTSINGLE ]
    virtual int type() const { return Type; }

    QList<QPainterPath> objectSavePathList() const { return subPathList(); }
    QList<QPainterPath> subPathList() const

    QPointF objectPos()    const { return scenePos(); }
    float   objectX()  const { return scenePos().x(); }
    float   objectY()  const { return scenePos().y(); }

    QStringList objectTextJustifyList() const

    void setObjectText(const QString& str)
    void setObjectTextFont(const QString& font)
    void setObjectTextJustify(const QString& justify)
    void setObjectTextSize(float size)
    void setObjectTextStyle(int bold, int italic, int under, int strike, int over)
    void setObjectTextBold(int val)
    void setObjectTextItalic(int val)
    void setObjectTextUnderline(int val)
    void setObjectTextStrikeOut(int val)
    void setObjectTextOverline(int val)
    void setObjectTextBackward(int val)
    void setObjectTextUpsideDown(int val)
    void setObjectPos(const QPointF& point) { setPos(point.x(), point.y()); }
    void setObjectPos(float x, float y) { setPos(x, y); }
    void setObjectX(float x) { setObjectPos(x, objectY()); }
    void setObjectY(float y) { setObjectPos(objectX(), y); }

    void updateRubber(QPainter* painter = 0)
    virtual void vulcanize()
    virtual QPointF mouseSnapPoint(const QPointF& mousePoint)
    virtual QList<QPointF> allGripPoints()
    virtual void gripEdit(const QPointF& before, const QPointF& after)

    QString objText
    QString objTextFont
    QString objTextJustify
    text_properties obj_text
    QPainterPath objTextPath
protected:
    void paint(QPainter*, const QStyleOptionGraphicsItem*, QWidget*)
private:
    void init(const QString& str, float x, float y, unsigned int rgb, Qt::PenStyle lineType)
]


ArcObject::ArcObject(float startX, float startY, float midX, float midY, float endX, float endY, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("ArcObject Constructor()")
    init(startX, startY, midX, midY, endX, endY, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

ArcObject::ArcObject(ArcObject* obj, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("ArcObject Constructor()")
    if(obj)
    {
        init(obj->objectStartPoint().x(), obj->objectStartPoint().y(), obj->objectMidPoint().x(), obj->objectMidPoint().y(), obj->objectEndPoint().x(), obj->objectEndPoint().y(), obj->objectColorRGB(), Qt::SolidLine)
        /* TODO: getCurrentLineType */
        setRotation(obj->rotation())
    }
}

ArcObject::~ArcObject():
    debug_message("ArcObject Destructor()")

def ArcObject::init(float startX, float startY, float midX, float midY, float endX, float endY, unsigned int rgb, Qt::PenStyle lineType):
    setData(OBJ_TYPE, type())
    setData(OBJ_NAME, obj_names[OBJ_TYPE_ARC])

    setFlag(QGraphicsItem::ItemIsSelectable, 1)

    calculateArcData(startX, startY, midX, midY, endX, endY)

    setObjectColor(rgb)
    setObjectLineType(lineType)
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objPen)

def ArcObject::calculateArcData(float startX, float startY, float midX, float midY, float endX, float endY):
    EmbArc arc = embArcObject_make(startX, startY,
                 midX, midY,
                 endX, endY).arc
    EmbVector center
    getArcCenter(arc, &center)
    arcStartPoint = QPointF(startX - center.x, startY - center.y)
    arcMidPoint = QPointF(midX   - center.x, midY   - center.y)
    arcEndPoint = QPointF(endX   - center.x, endY   - center.y)

    setPos(center.x, center.y)

    float radius = QLineF(center.x, center.y, midX, midY).length()
    updateArcRect(radius)
    updatePath()
    setRotation(0)
    setScale(1)

def ArcObject::updateArcRect(float radius):
    QRectF arcRect
    arcRect.setWidth(radius*2.0)
    arcRect.setHeight(radius*2.0)
    arcRect.moveCenter(QPointF(0,0))
    setRect(arcRect)

def ArcObject::setObjectRadius(float radius):
    if (radius <= 0) {
        radius = 0.0000001
    }

    QPointF center = scenePos()
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

def ArcObject::setObjectStartAngle(float angle):
    /*TODO: ArcObject setObjectStartAngle*/
}

def ArcObject::setObjectEndAngle(float angle):
    /*TODO: ArcObject setObjectEndAngle*/
}

def ArcObject::setObjectStartPoint(float pointX, float pointY):
    calculateArcData(pointX, pointY, arcMidPoint.x(), arcMidPoint.y(), arcEndPoint.x(), arcEndPoint.y())

def ArcObject::setObjectMidPoint(const QPointF& point):
    setObjectMidPoint(point.x(), point.y())

def ArcObject::setObjectMidPoint(float pointX, float pointY):
    calculateArcData(arcStartPoint.x(), arcStartPoint.y(), pointX, pointY, arcEndPoint.x(), arcEndPoint.y())

def ArcObject::setObjectEndPoint(const QPointF& point):
    setObjectEndPoint(point.x(), point.y())

def ArcObject::setObjectEndPoint(float pointX, float pointY):
    calculateArcData(arcStartPoint.x(), arcStartPoint.y(), arcMidPoint.x(), arcMidPoint.y(), pointX, pointY)

float ArcObject::objectStartAngle() const:
    float angle = QLineF(scenePos(), objectStartPoint()).angle()
    return fmod(angle, 360.0)

float ArcObject::objectEndAngle() const:
    float angle = QLineF(scenePos(), objectEndPoint()).angle()
    return fmod(angle, 360.0)

QPointF ArcObject::objectStartPoint() const:
    EmbVector v = to_emb_vector(arcStartPoint)
    EmbVector rot = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(rot)

QPointF ArcObject::objectMidPoint() const:
    EmbVector v = to_emb_vector(arcMidPoint)
    EmbVector rot = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(rot)

QPointF ArcObject::objectEndPoint() const:
    EmbVector v = to_emb_vector(arcEndPoint)
    EmbVector rot = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(rot)

float ArcObject::objectArea() const:
    /*Area of a circular segment*/
    float r = objectRadius()
    float theta = radians(objectIncludedAngle())
    return ((r*r)/2)*(theta - sin(theta))

float ArcObject::objectArcLength() const:
    return radians(objectIncludedAngle())*objectRadius()

float ArcObject::objectChord() const:
    return QLineF(objectStartPoint().x(), objectStartPoint().y(), objectEndPoint().x(), objectEndPoint().y()).length()

float ArcObject::objectIncludedAngle() const:
    float chord = objectChord()
    float rad = objectRadius()
    if(chord <= 0 || rad <= 0) return 0
    /* Prevents division by zero and non-existent circles */

    /* NOTE:
     * Due to floating point rounding errors, we need to clamp the
     * quotient so it is in the range [-1, 1].
     * If the quotient is out of that range, then the result of asin()
     * will be NaN.
     */
    float quotient = chord/(2.0*rad)
    if(quotient > 1.0) quotient = 1.0
    if(quotient < 0.0) quotient = 0.0
    /* NOTE: 0 rather than -1 since we are enforcing a positive chord
     * and radius.
     */
    return degrees(2.0*asin(quotient))
    /* Properties of a Circle - Get the Included Angle - Reference: ASD9 */
}

int ArcObject::objectClockwise() const:
    EmbVector start = to_emb_vector(objectStartPoint())
    EmbVector mid = to_emb_vector(objectMidPoint())
    EmbVector end = to_emb_vector(objectEndPoint())
    EmbArc arc = embArcObject_make(start.x, -start.y, mid.x, -mid.y, end.x, -end.y).arc
    /* NOTE: Y values are inverted here on purpose */
    return isArcClockwise(arc)

def ArcObject::updatePath():
    float startAngle = (objectStartAngle() + rotation())
    float spanAngle = objectIncludedAngle()

    if(objectClockwise())
        spanAngle = -spanAngle

    QPainterPath path
    path.arcMoveTo(rect(), startAngle)
    path.arcTo(rect(), startAngle, spanAngle)
    /*NOTE: Reverse the path so that the inside area isn't considered part of the arc*/
    path.arcTo(rect(), startAngle+spanAngle, -spanAngle)
    setObjectPath(path)

def ArcObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
    QGraphicsScene* objScene = scene()
    if(!objScene) return

    QPen paintPen = pen()
    painter->setPen(paintPen)
    updateRubber(painter)
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen)

    float startAngle = (objectStartAngle() + rotation())*16
    float spanAngle = objectIncludedAngle()*16

    if(objectClockwise())
        spanAngle = -spanAngle

    float rad = objectRadius()
    QRectF paintRect(-rad, -rad, rad*2.0, rad*2.0)
    painter->drawArc(paintRect, startAngle, spanAngle)

def ArcObject::updateRubber(QPainter* painter):
    /*TODO: Arc Rubber Modes*/

    /*TODO: updateRubber() gripping for ArcObject*/

}

def ArcObject::vulcanize():
    debug_message("ArcObject vulcanize()")
    updateRubber()

    setObjectRubberMode(OBJ_RUBBER_OFF)

/* Returns the closest snap point to the mouse point*/
QPointF ArcObject::mouseSnapPoint(const QPointF& mousePoint):
    QPointF center = objectCenter()
    QPointF start = objectStartPoint()
    QPointF mid = objectMidPoint()
    QPointF end = objectEndPoint()

    float cntrDist = QLineF(mousePoint, center).length()
    float startDist = QLineF(mousePoint, start).length()
    float midDist = QLineF(mousePoint, mid).length()
    float endDist = QLineF(mousePoint, end).length()

    float minDist = qMin(qMin(cntrDist, startDist), qMin(midDist, endDist))

    if     (minDist == cntrDist)  return center
    elif(minDist == startDist) return start
    elif(minDist == midDist)   return mid
    elif(minDist == endDist)   return end

    return scenePos()

QList<QPointF> ArcObject::allGripPoints():
    QList<QPointF> gripPoints
    gripPoints << objectCenter() << objectStartPoint() << objectMidPoint() << objectEndPoint()
    return gripPoints

def ArcObject::gripEdit(const QPointF& before, const QPointF& after):
    /*TODO: gripEdit() for ArcObject*/
}


BaseObject::BaseObject(QGraphicsItem* parent) : QGraphicsPathItem(parent):
    debug_message("BaseObject Constructor()")

    objPen.setCapStyle(Qt::RoundCap)
    objPen.setJoinStyle(Qt::RoundJoin)
    lwtPen.setCapStyle(Qt::RoundCap)
    lwtPen.setJoinStyle(Qt::RoundJoin)

    objID = QDateTime::currentMSecsSinceEpoch()

BaseObject::~BaseObject():
    debug_message("BaseObject Destructor()")

def BaseObject::setObjectColor(const QColor& color):
    objPen.setColor(color)
    lwtPen.setColor(color)

def BaseObject::setObjectColorRGB(unsigned int rgb):
    objPen.setColor(QColor(rgb))
    lwtPen.setColor(QColor(rgb))

def BaseObject::setObjectLineType(Qt::PenStyle lineType):
    objPen.setStyle(lineType)
    lwtPen.setStyle(lineType)

def BaseObject::setObjectLineWeight(float lineWeight):
    objPen.setWidthF(0); /*NOTE: The objPen will always be cosmetic*/

    if(lineWeight < 0)
    {
        if(lineWeight == OBJ_LWT_BYLAYER)
        {
            lwtPen.setWidthF(0.35); /*TODO: getLayerLineWeight*/
        }
        elif(lineWeight == OBJ_LWT_BYBLOCK)
        {
            lwtPen.setWidthF(0.35); /*TODO: getBlockLineWeight*/
        }
        else
        {
            QMessageBox::warning(0, QObject::tr("Error - Negative Lineweight"),
                                    QObject::tr("Lineweight: %1")
                                    .arg(QString().setNum(lineWeight)))
            debug_message("Lineweight cannot be negative! Inverting sign.")
            lwtPen.setWidthF(-lineWeight)
        }
    }
    else
    {
        lwtPen.setWidthF(lineWeight)
    }
}

QPointF BaseObject::objectRubberPoint(const QString& key) const:
    if(objRubberPoints.contains(key))
        return objRubberPoints.value(key)

    QGraphicsScene* gscene = scene()
    if(gscene)
        return scene()->property("SCENE_QSNAP_POINT").toPointF()
    return QPointF()

QString BaseObject::objectRubberText(const QString& key) const:
    if(objRubberTexts.contains(key))
        return objRubberTexts.value(key)
    return QString()

QRectF BaseObject::boundingRect() const:
    /*If gripped, force this object to be drawn even if it is offscreen*/
    if(objectRubberMode() == OBJ_RUBBER_GRIP)
        return scene()->sceneRect()
    return path().boundingRect()

def BaseObject::drawRubberLine(const QLineF& rubLine, QPainter* painter, const char* colorFromScene):
    if(painter)
    {
        QGraphicsScene* objScene = scene()
        if(!objScene) return
        QPen colorPen = objPen
        colorPen.setColor(QColor(objScene->property(colorFromScene).toUInt()))
        painter->setPen(colorPen)
        painter->drawLine(rubLine)
        painter->setPen(objPen)
    }
}

def BaseObject::realRender(QPainter* painter, const QPainterPath& renderPath):
    QColor color1 = objectColor();       /*lighter color*/
    QColor color2 = color1.darker(150); /*darker color*/

    /*If we have a dark color, lighten it*/
    int darkness = color1.lightness()
    int threshold = 32
    /*TODO: This number may need adjusted or maybe just add it to settings.*/
    if (darkness < threshold) {
        color2 = color1
        if (!darkness) {
            color1 = QColor(threshold, threshold, threshold)
        } /*lighter() does not affect pure black*/
        else {
            color1 = color2.lighter(100 + threshold)
        }
    }

    int count = renderPath.elementCount()
    for(int i = 0; i < count-1; ++i)
    {
        QPainterPath::Element elem = renderPath.elementAt(i)
        QPainterPath::Element next = renderPath.elementAt(i+1)

        if(next.isMoveTo()) continue

        QPainterPath elemPath
        elemPath.moveTo(elem.x, elem.y)
        elemPath.lineTo(next.x, next.y)

        QPen renderPen(QColor(0,0,0,0))
        renderPen.setWidthF(0)
        painter->setPen(renderPen)
        QPainterPathStroker stroker
        stroker.setWidth(0.35)
        stroker.setCapStyle(Qt::RoundCap)
        stroker.setJoinStyle(Qt::RoundJoin)
        QPainterPath realPath = stroker.createStroke(elemPath)
        painter->drawPath(realPath)

        QLinearGradient grad(elemPath.pointAtPercent(0.5), elemPath.pointAtPercent(0.0))
        grad.setColorAt(0, color1)
        grad.setColorAt(1, color2)
        grad.setSpread(QGradient::ReflectSpread)

        painter->fillPath(realPath, QBrush(grad))
    }
}


DimLeaderObject::DimLeaderObject(float x1, float y1, float x2, float y2, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("DimLeaderObject Constructor()")
    init(x1, y1, x2, y2, rgb, Qt::SolidLine); /* TODO: getCurrentLineType */
}

DimLeaderObject::DimLeaderObject(DimLeaderObject* obj, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("DimLeaderObject Constructor()")
    if (obj) {
        EmbVector v1, v2
        v1 = to_emb_vector(obj->objectEndPoint1())
        v2 = to_emb_vector(obj->objectEndPoint2())
        init(v1.x, v1.y, v2.x, v2.y, obj->objectColorRGB(), Qt::SolidLine)
        /* TODO: getCurrentLineType */
    }
}

DimLeaderObject::~DimLeaderObject():
    debug_message("DimLeaderObject Destructor()")

def DimLeaderObject::init(float x1, float y1, float x2, float y2, unsigned int rgb, Qt::PenStyle lineType):
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

def DimLeaderObject::setObjectEndPoint1(EmbVector p1):
    EmbVector diff
    QPointF endPt2 = objectEndPoint2()
    float x2 = endPt2.x()
    float y2 = endPt2.y()
    diff.x = x2 - p1.x
    diff.y = y2 - p1.y
    setRotation(0)
    setLine(0, 0, diff.x, diff.y)
    setPos(p1.x, p1.y)
    updateLeader()

def DimLeaderObject::setObjectEndPoint2(EmbVector p2):
    EmbVector endPt1 = to_emb_vector(scenePos())
    setRotation(0)
    setLine(0, 0, p2.x - endPt1.x, p2.y - endPt1.y)
    setPos(endPt1.x, endPt1.y)
    updateLeader()

QPointF DimLeaderObject::objectEndPoint1() const:
    return scenePos()

QPointF DimLeaderObject::objectEndPoint2() const:
    EmbVector v
    v.x = line().x2()
    v.y = line().y2()
    v = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(v)

QPointF DimLeaderObject::objectMidPoint() const:
    EmbVector v
    v = to_emb_vector(line().pointAt(0.5))
    v = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(v)

float DimLeaderObject::objectAngle() const:
    float angle = line().angle() - rotation()
    return fmod(angle, 360.0)

def DimLeaderObject::updateLeader():
    int arrowStyle = Closed; /*TODO: Make this customizable*/
    float arrowStyleAngle = 15.0; /*TODO: Make this customizable*/
    float arrowStyleLength = 1.0; /*TODO: Make this customizable*/
    float lineStyleAngle = 45.0; /*TODO: Make this customizable*/
    float lineStyleLength = 1.0; /*TODO: Make this customizable*/

    QLineF lyne = line()
    float angle = lyne.angle()
    QPointF ap0 = lyne.p1()
    QPointF lp0 = lyne.p2()

    /*Arrow*/
    QLineF lynePerp(lyne.pointAt(arrowStyleLength/lyne.length()) ,lp0)
    lynePerp.setAngle(angle + 90)
    QLineF lyne1(ap0, lp0)
    QLineF lyne2(ap0, lp0)
    lyne1.setAngle(angle + arrowStyleAngle)
    lyne2.setAngle(angle - arrowStyleAngle)
    QPointF ap1
    QPointF ap2
    /* HACK: these need fixing
    lynePerp.intersects(lyne1, &ap1)
    lynePerp.intersects(lyne2, &ap2)
    */
    /* So they don't cause memory access problems */
    ap1 = lyne1.p1()
    ap2 = lyne2.p1()

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
        arrowStylePath = QPainterPath()
        arrowStylePath.moveTo(ap1)
        arrowStylePath.lineTo(ap0)
        arrowStylePath.lineTo(ap2)
        arrowStylePath.lineTo(ap0)
        arrowStylePath.lineTo(ap1)
    }
    elif(arrowStyle == Closed)
    {
        arrowStylePath = QPainterPath()
        arrowStylePath.moveTo(ap1)
        arrowStylePath.lineTo(ap0)
        arrowStylePath.lineTo(ap2)
        arrowStylePath.lineTo(ap1)
    }
    elif(arrowStyle == Dot)
    {
        arrowStylePath = QPainterPath()
        arrowStylePath.addEllipse(ap0, arrowStyleLength, arrowStyleLength)
    }
    elif(arrowStyle == Box)
    {
        arrowStylePath = QPainterPath()
        float side = QLineF(ap1, ap2).length()
        QRectF ar0(0, 0, side, side)
        ar0.moveCenter(ap0)
        arrowStylePath.addRect(ar0)
    }
    elif(arrowStyle == Tick)
    {
    }

    lineStylePath = QPainterPath()
    lineStylePath.moveTo(ap0)
    lineStylePath.lineTo(lp0)

def DimLeaderObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
    QGraphicsScene* objScene = scene()
    if(!objScene) return

    QPen paintPen = pen()
    painter->setPen(paintPen)
    updateRubber(painter)
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen)

    painter->drawPath(lineStylePath)
    painter->drawPath(arrowStylePath)

    if(filled)
        painter->fillPath(arrowStylePath, objectColor())

def DimLeaderObject::updateRubber(QPainter* painter):
    int rubberMode = objectRubberMode()
    if(rubberMode == OBJ_RUBBER_DIMLEADER_LINE)
    {
        QPointF sceneStartPoint = objectRubberPoint("DIMLEADER_LINE_START")
        QPointF sceneQSnapPoint = objectRubberPoint("DIMLEADER_LINE_END")

        setObjectEndPoint1(to_emb_vector(sceneStartPoint))
        setObjectEndPoint2(to_emb_vector(sceneQSnapPoint))
    }
    elif(rubberMode == OBJ_RUBBER_GRIP)
    {
        if(painter)
        {
            QPointF gripPoint = objectRubberPoint("GRIP_POINT")
            if     (gripPoint == objectEndPoint1()) painter->drawLine(line().p2(), mapFromScene(objectRubberPoint(QString())))
            elif(gripPoint == objectEndPoint2()) painter->drawLine(line().p1(), mapFromScene(objectRubberPoint(QString())))
            elif(gripPoint == objectMidPoint())  painter->drawLine(line().translated(mapFromScene(objectRubberPoint(QString()))-mapFromScene(gripPoint)))
        }
    }
}

def DimLeaderObject::vulcanize():
    debug_message("DimLeaderObject vulcanize()")
    updateRubber()

    setObjectRubberMode(OBJ_RUBBER_OFF)

/* Returns the closest snap point to the mouse point. */
QPointF DimLeaderObject::mouseSnapPoint(const QPointF& mousePoint):
    QPointF endPoint1 = objectEndPoint1()
    QPointF endPoint2 = objectEndPoint2()
    QPointF midPoint = objectMidPoint()

    float end1Dist = QLineF(mousePoint, endPoint1).length()
    float end2Dist = QLineF(mousePoint, endPoint2).length()
    float midDist = QLineF(mousePoint, midPoint).length()

    float minDist = qMin(end1Dist, end2Dist)

    if(curved)
        minDist = qMin(minDist, midDist)

    if     (minDist == end1Dist) return endPoint1
    elif(minDist == end2Dist) return endPoint2
    elif(minDist == midDist)  return midPoint

    return scenePos()

QList<QPointF> DimLeaderObject::allGripPoints():
    QList<QPointF> gripPoints
    gripPoints << objectEndPoint1() << objectEndPoint2()
    if(curved)
        gripPoints << objectMidPoint()
    return gripPoints

def DimLeaderObject::gripEdit(const QPointF& before, const QPointF& after):
    if     (before == objectEndPoint1()) { setObjectEndPoint1(to_emb_vector(after)); }
    elif(before == objectEndPoint2()) { setObjectEndPoint2(to_emb_vector(after)); }
    elif(before == objectMidPoint())  { QPointF delta = after-before; moveBy(delta.x(), delta.y()); }
}


EllipseObject::EllipseObject(float centerX, float centerY, float width, float height, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("EllipseObject Constructor()")
    init(centerX, centerY, width, height, rgb, Qt::SolidLine)
    /* TODO: getCurrentLineType */
}

EllipseObject::EllipseObject(EllipseObject* obj, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("EllipseObject Constructor()")
    if(obj)
    {
        init(obj->objectCenter().x(), obj->objectCenter().y(), obj->objectWidth(), obj->objectHeight(), obj->objectColorRGB(), Qt::SolidLine)
        /* TODO: getCurrentLineType */
        setRotation(obj->rotation())
    }
}

EllipseObject::~EllipseObject():
    debug_message("EllipseObject Destructor()")

def EllipseObject::init(float centerX, float centerY, float width, float height, unsigned int rgb, Qt::PenStyle lineType):
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

def EllipseObject::setObjectSize(float width, float height):
    QRectF elRect = rect()
    elRect.setWidth(width)
    elRect.setHeight(height)
    elRect.moveCenter(QPointF(0,0))
    setRect(elRect)

def EllipseObject::setObjectRadiusMajor(float radius):
    setObjectDiameterMajor(radius*2.0)

def EllipseObject::setObjectRadiusMinor(float radius):
    setObjectDiameterMinor(radius*2.0)

def EllipseObject::setObjectDiameterMajor(float diameter):
    QRectF elRect = rect()
    if (elRect.width() > elRect.height()) {
        elRect.setWidth(diameter)
    }
    else
        elRect.setHeight(diameter)
    elRect.moveCenter(QPointF(0,0))
    setRect(elRect)

def EllipseObject::setObjectDiameterMinor(float diameter):
    QRectF elRect = rect()
    if (elRect.width() < elRect.height()) {
        elRect.setWidth(diameter)
    }
    else
        elRect.setHeight(diameter)
    elRect.moveCenter(QPointF(0,0))
    setRect(elRect)

QPointF EllipseObject::objectQuadrant0() const:
    EmbVector v
    v.x = objectWidth()/2.0
    v.y = 0.0
    v = rotate_vector(v, radians(rotation()))
    return objectCenter() + to_qpointf(v)

QPointF EllipseObject::objectQuadrant90() const:
    EmbVector v
    v.x = objectHeight()/2.0
    v.y = 0.0
    v = rotate_vector(v, radians(rotation()+90.0))
    return objectCenter() + to_qpointf(v)

QPointF EllipseObject::objectQuadrant180() const:
    EmbVector v
    v.x = objectWidth()/2.0
    v.y = 0.0
    v = rotate_vector(v, radians(rotation()+180.0))
    return objectCenter() + to_qpointf(v)

QPointF EllipseObject::objectQuadrant270() const:
    EmbVector v
    v.x = objectHeight()/2.0
    v.y = 0.0
    v = rotate_vector(v, radians(rotation()+270.0))
    return objectCenter() + to_qpointf(v)

def EllipseObject::updatePath():
    QPainterPath path
    QRectF r = rect()
    path.arcMoveTo(r, 0)
    path.arcTo(r, 0, 360)
    /* NOTE: Reverse the path so that the inside area isn't considered part of the ellipse. */
    path.arcTo(r, 0, -360)
    setObjectPath(path)

def EllipseObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
    QGraphicsScene* objScene = scene()
    if(!objScene) return

    QPen paintPen = pen()
    painter->setPen(paintPen)
    updateRubber(painter)
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen)

    painter->drawEllipse(rect())

def EllipseObject::updateRubber(QPainter* painter):
    int rubberMode = objectRubberMode()
    if(rubberMode == OBJ_RUBBER_ELLIPSE_LINE)
    {
        QPointF sceneLinePoint1 = objectRubberPoint("ELLIPSE_LINE_POINT1")
        QPointF sceneLinePoint2 = objectRubberPoint("ELLIPSE_LINE_POINT2")
        QPointF itemLinePoint1 = mapFromScene(sceneLinePoint1)
        QPointF itemLinePoint2 = mapFromScene(sceneLinePoint2)
        QLineF itemLine(itemLinePoint1, itemLinePoint2)
        if(painter) drawRubberLine(itemLine, painter, "VIEW_COLOR_CROSSHAIR")
        updatePath()
    }
    elif(rubberMode == OBJ_RUBBER_ELLIPSE_MAJORDIAMETER_MINORRADIUS)
    {
        QPointF sceneAxis1Point1 = objectRubberPoint("ELLIPSE_AXIS1_POINT1")
        QPointF sceneAxis1Point2 = objectRubberPoint("ELLIPSE_AXIS1_POINT2")
        QPointF sceneCenterPoint = objectRubberPoint("ELLIPSE_CENTER")
        QPointF sceneAxis2Point2 = objectRubberPoint("ELLIPSE_AXIS2_POINT2")
        float ellipseWidth = objectRubberPoint("ELLIPSE_WIDTH").x()
        float ellipseRot = objectRubberPoint("ELLIPSE_ROT").x()

        /* TODO: incorporate perpendicularDistance() into libembroidery. */
        float px = sceneAxis2Point2.x()
        float py = sceneAxis2Point2.y()
        float x1 = sceneAxis1Point1.x()
        float y1 = sceneAxis1Point1.y()
        QLineF line(sceneAxis1Point1, sceneAxis1Point2)
        QLineF norm = line.normalVector()
        float dx = px-x1
        float dy = py-y1
        norm.translate(dx, dy)
        QPointF iPoint
        /* HACK: this isn't in all versions of Qt 5 in the same place?
         * norm.intersects(line, &iPoint)
         */
        iPoint = line.p1()
        float ellipseHeight = QLineF(px, py, iPoint.x(), iPoint.y()).length()*2.0

        setPos(sceneCenterPoint)
        setObjectSize(ellipseWidth, ellipseHeight)
        setRotation(-ellipseRot)

        QPointF itemCenterPoint = mapFromScene(sceneCenterPoint)
        QPointF itemAxis2Point2 = mapFromScene(sceneAxis2Point2)
        QLineF itemLine(itemCenterPoint, itemAxis2Point2)
        if(painter) drawRubberLine(itemLine, painter, "VIEW_COLOR_CROSSHAIR")
        updatePath()
    }
    elif(rubberMode == OBJ_RUBBER_ELLIPSE_MAJORRADIUS_MINORRADIUS)
    {
        QPointF sceneAxis1Point2 = objectRubberPoint("ELLIPSE_AXIS1_POINT2")
        QPointF sceneCenterPoint = objectRubberPoint("ELLIPSE_CENTER")
        QPointF sceneAxis2Point2 = objectRubberPoint("ELLIPSE_AXIS2_POINT2")
        float ellipseWidth = objectRubberPoint("ELLIPSE_WIDTH").x()
        float ellipseRot = objectRubberPoint("ELLIPSE_ROT").x()

        /* TODO: incorporate perpendicularDistance() into libembroidery. */
        float px = sceneAxis2Point2.x()
        float py = sceneAxis2Point2.y()
        float x1 = sceneCenterPoint.x()
        float y1 = sceneCenterPoint.y()
        QLineF line(sceneCenterPoint, sceneAxis1Point2)
        QLineF norm = line.normalVector()
        float dx = px-x1
        float dy = py-y1
        norm.translate(dx, dy)
        QPointF iPoint
        /* HACK */
        /* norm.intersects(line, &iPoint); */
        iPoint = line.p1()
        float ellipseHeight = QLineF(px, py, iPoint.x(), iPoint.y()).length()*2.0

        setPos(sceneCenterPoint)
        setObjectSize(ellipseWidth, ellipseHeight)
        setRotation(-ellipseRot)

        QPointF itemCenterPoint = mapFromScene(sceneCenterPoint)
        QPointF itemAxis2Point2 = mapFromScene(sceneAxis2Point2)
        QLineF itemLine(itemCenterPoint, itemAxis2Point2)
        if(painter) drawRubberLine(itemLine, painter, "VIEW_COLOR_CROSSHAIR")
        updatePath()
    }
    elif(rubberMode == OBJ_RUBBER_GRIP)
    {
        /* TODO: updateRubber() gripping for EllipseObject. */
    }
}

def EllipseObject::vulcanize():
    debug_message("EllipseObject vulcanize()")
    updateRubber()

    setObjectRubberMode(OBJ_RUBBER_OFF)

/* Returns the closest snap point to the mouse point. */
QPointF EllipseObject::mouseSnapPoint(const QPointF& mousePoint):
    QPointF center = objectCenter()
    QPointF quad0 = objectQuadrant0()
    QPointF quad90 = objectQuadrant90()
    QPointF quad180 = objectQuadrant180()
    QPointF quad270 = objectQuadrant270()

    float cntrDist = QLineF(mousePoint, center).length()
    float q0Dist = QLineF(mousePoint, quad0).length()
    float q90Dist = QLineF(mousePoint, quad90).length()
    float q180Dist = QLineF(mousePoint, quad180).length()
    float q270Dist = QLineF(mousePoint, quad270).length()

    float minDist = qMin(qMin(qMin(q0Dist, q90Dist), qMin(q180Dist, q270Dist)), cntrDist)

    if     (minDist == cntrDist) return center
    elif(minDist == q0Dist)   return quad0
    elif(minDist == q90Dist)  return quad90
    elif(minDist == q180Dist) return quad180
    elif(minDist == q270Dist) return quad270

    return scenePos()

QList<QPointF> EllipseObject::allGripPoints():
    QList<QPointF> gripPoints
    gripPoints << objectCenter() << objectQuadrant0() << objectQuadrant90() << objectQuadrant180() << objectQuadrant270()
    return gripPoints

def EllipseObject::gripEdit(const QPointF& before, const QPointF& after):
    /*TODO: gripEdit() for EllipseObject*/
}

QPainterPath EllipseObject::objectSavePath() const:
    QPainterPath path
    QRectF r = rect()
    path.arcMoveTo(r, 0)
    path.arcTo(r, 0, 360)

    float s = scale()
    QTransform trans
    trans.rotate(rotation())
    trans.scale(s,s)
    return trans.map(path)


ImageObject::ImageObject(float x, float y, float w, float h, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("ImageObject Constructor()")
    init(x, y, w, h, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

ImageObject::ImageObject(ImageObject* obj, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("ImageObject Constructor()")
    if(obj)
    {
        QPointF ptl = obj->objectTopLeft()
        init(ptl.x(), ptl.y(), obj->objectWidth(), obj->objectHeight(), obj->objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setRotation(obj->rotation())
    }
}

ImageObject::~ImageObject():
    debug_message("ImageObject Destructor()")

def ImageObject::init(float x, float y, float w, float h, unsigned int rgb, Qt::PenStyle lineType):
    setData(OBJ_TYPE, type())
    setData(OBJ_NAME, obj_names[OBJ_TYPE_IMAGE])

    setFlag(QGraphicsItem::ItemIsSelectable, 1)

    setObjectRect(x, y, w, h)
    setObjectColor(rgb)
    setObjectLineType(lineType)
    setObjectLineWeight(0.35); /* TODO: pass in proper lineweight */
    setPen(objectPen())

def ImageObject::setObjectRect(float x, float y, float w, float h):
    setPos(x, y)
    setRect(0, 0, w, h)
    updatePath()

QPointF ImageObject::objectTopLeft() const:
    EmbVector v = to_emb_vector(rect().topLeft())
    v = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(v)

QPointF ImageObject::objectTopRight() const:
    EmbVector v = to_emb_vector(rect().topRight())
    v = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(v)

QPointF ImageObject::objectBottomLeft() const:
    EmbVector v = to_emb_vector(rect().bottomLeft())
    v = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(v)

QPointF ImageObject::objectBottomRight() const:
    EmbVector v = to_emb_vector(rect().bottomRight())
    v = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(v)

def ImageObject::updatePath():
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

def ImageObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
    QGraphicsScene* objScene = scene()
    if(!objScene) return

    QPen paintPen = pen()
    painter->setPen(paintPen)
    updateRubber(painter)
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen)

    painter->drawRect(rect())

def ImageObject::updateRubber(QPainter* painter):
    int rubberMode = objectRubberMode()
    if(rubberMode == OBJ_RUBBER_IMAGE)
    {
        QPointF sceneStartPoint = objectRubberPoint("IMAGE_START")
        QPointF sceneEndPoint = objectRubberPoint("IMAGE_END")
        float x = sceneStartPoint.x()
        float y = sceneStartPoint.y()
        float w = sceneEndPoint.x() - sceneStartPoint.x()
        float h = sceneEndPoint.y() - sceneStartPoint.y()
        setObjectRect(x,y,w,h)
        updatePath()
    }
    elif(rubberMode == OBJ_RUBBER_GRIP)
    {
        /*TODO: updateRubber() gripping for ImageObject*/
    }
}

def ImageObject::vulcanize():
    debug_message("ImageObject vulcanize()")
    updateRubber()

    setObjectRubberMode(OBJ_RUBBER_OFF)

/* Returns the closest snap point to the mouse point*/
QPointF ImageObject::mouseSnapPoint(const QPointF& mousePoint):
    QPointF ptl = objectTopLeft();     /* Top Left Corner QSnap */
    QPointF ptr = objectTopRight();    /* Top Right Corner QSnap */
    QPointF pbl = objectBottomLeft();  /*Bottom Left Corner QSnap*/
    QPointF pbr = objectBottomRight(); /*Bottom Right Corner QSnap*/

    float ptlDist = QLineF(mousePoint, ptl).length()
    float ptrDist = QLineF(mousePoint, ptr).length()
    float pblDist = QLineF(mousePoint, pbl).length()
    float pbrDist = QLineF(mousePoint, pbr).length()

    float minDist = qMin(qMin(ptlDist, ptrDist), qMin(pblDist, pbrDist))

    if     (minDist == ptlDist) return ptl
    elif(minDist == ptrDist) return ptr
    elif(minDist == pblDist) return pbl
    elif(minDist == pbrDist) return pbr

    return scenePos()

QList<QPointF> ImageObject::allGripPoints():
    QList<QPointF> gripPoints
    gripPoints << objectTopLeft() << objectTopRight() << objectBottomLeft() << objectBottomRight()
    return gripPoints

def ImageObject::gripEdit(const QPointF& before, const QPointF& after):
    /*TODO: gripEdit() for ImageObject*/
}

LineObject::LineObject(float x1, float y1, float x2, float y2, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("LineObject Constructor()")
    init(x1, y1, x2, y2, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

LineObject::LineObject(LineObject* obj, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("LineObject Constructor()")
    if(obj)
    {
        init(obj->objectX1(), obj->objectY1(), obj->objectX2(), obj->objectY2(), obj->objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
    }
}

LineObject::~LineObject():
    debug_message("LineObject Destructor()")

def LineObject::init(float x1, float y1, float x2, float y2, unsigned int rgb, Qt::PenStyle lineType):
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

def LineObject::setObjectEndPoint1(const QPointF& endPt1):
    setObjectEndPoint1(endPt1.x(), endPt1.y())

def LineObject::setObjectEndPoint1(float x1, float y1):
    EmbVector delta, endPt2
    endPt2 = to_emb_vector(objectEndPoint2())
    delta.x = endPt2.x - x1
    delta.y = endPt2.y - y1
    setRotation(0)
    setScale(1)
    setLine(0, 0, delta.x, delta.y)
    setPos(x1, y1)

def LineObject::setObjectEndPoint2(const QPointF& endPt2):
    setObjectEndPoint2(endPt2.x(), endPt2.y())

def LineObject::setObjectEndPoint2(float x2, float y2):
    EmbVector delta, endPt1
    endPt1 = to_emb_vector(scenePos())
    delta.x = x2 - endPt1.x
    delta.y = y2 - endPt1.y
    setRotation(0)
    setScale(1)
    setLine(0, 0, delta.x, delta.y)
    setPos(endPt1.x, endPt1.y)

QPointF LineObject::objectEndPoint2() const:
    EmbVector v
    v.x = line().x2()
    v.y = line().y2()
    v = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(v)

QPointF LineObject::objectMidPoint() const:
    EmbVector v
    v = to_emb_vector(line().pointAt(0.5))
    v = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(v)

float LineObject::objectAngle() const:
    float angle = line().angle() - rotation()
    return fmod(angle, 360.0)

def LineObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
    QGraphicsScene* objScene = scene()
    if(!objScene) return

    QPen paintPen = pen()
    painter->setPen(paintPen)
    updateRubber(painter)
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen)

    if(objectRubberMode() != OBJ_RUBBER_LINE) painter->drawLine(line())

    if(objScene->property("ENABLE_LWT").toBool() && objScene->property("ENABLE_REAL").toBool()) { realRender(painter, path()); }
}

def LineObject::updateRubber(QPainter* painter):
    int rubberMode = objectRubberMode()
    if(rubberMode == OBJ_RUBBER_LINE)
    {
        QPointF sceneStartPoint = objectRubberPoint("LINE_START")
        QPointF sceneQSnapPoint = objectRubberPoint("LINE_END")

        setObjectEndPoint1(sceneStartPoint)
        setObjectEndPoint2(sceneQSnapPoint)

        drawRubberLine(line(), painter, "VIEW_COLOR_CROSSHAIR")
    }
    elif(rubberMode == OBJ_RUBBER_GRIP:
        if(painter:
            QPointF gripPoint = objectRubberPoint("GRIP_POINT")
            if     (gripPoint == objectEndPoint1()) painter->drawLine(line().p2(), mapFromScene(objectRubberPoint(QString())))
            elif(gripPoint == objectEndPoint2()) painter->drawLine(line().p1(), mapFromScene(objectRubberPoint(QString())))
            elif(gripPoint == objectMidPoint())  painter->drawLine(line().translated(mapFromScene(objectRubberPoint(QString()))-mapFromScene(gripPoint)))

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")


def LineObject::vulcanize():
    debug_message("LineObject vulcanize()")
    updateRubber()

    setObjectRubberMode(OBJ_RUBBER_OFF)

/* Returns the closest snap point to the mouse point*/
QPointF LineObject::mouseSnapPoint(const QPointF& mousePoint):
    QPointF endPoint1 = objectEndPoint1()
    QPointF endPoint2 = objectEndPoint2()
    QPointF midPoint = objectMidPoint()

    float end1Dist = QLineF(mousePoint, endPoint1).length()
    float end2Dist = QLineF(mousePoint, endPoint2).length()
    float midDist = QLineF(mousePoint, midPoint).length()

    float minDist = qMin(qMin(end1Dist, end2Dist), midDist)

    if     (minDist == end1Dist) return endPoint1
    elif(minDist == end2Dist) return endPoint2
    elif(minDist == midDist)  return midPoint

    return scenePos()

QList<QPointF> LineObject::allGripPoints():
    QList<QPointF> gripPoints
    gripPoints << objectEndPoint1() << objectEndPoint2() << objectMidPoint()
    return gripPoints

def LineObject::gripEdit(const QPointF& before, const QPointF& after):
    if     (before == objectEndPoint1()) { setObjectEndPoint1(after.x(), after.y()); }
    elif(before == objectEndPoint2()) { setObjectEndPoint2(after.x(), after.y()); }
    elif(before == objectMidPoint())  { QPointF delta = after-before; moveBy(delta.x(), delta.y()); }
}

QPainterPath LineObject::objectSavePath() const:
    QPainterPath path
    path.lineTo(objectDeltaX(), objectDeltaY())
    return path


PathObject::PathObject(float x, float y, const QPainterPath p, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("PathObject Constructor()")
    init(x, y, p, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

PathObject::PathObject(PathObject* obj, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("PathObject Constructor()")
    if (obj) {
        init(obj->objectX(), obj->objectY(), obj->objectCopyPath(), obj->objPen.color().rgb(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setRotation(obj->rotation())
        setScale(obj->scale())
    }
}

PathObject::~PathObject():
    debug_message("PathObject Destructor()")

def PathObject::init(float x, float y, const QPainterPath& p, unsigned int rgb, Qt::PenStyle lineType):
    setData(OBJ_TYPE, type())
    setData(OBJ_NAME, obj_names[OBJ_TYPE_PATH])

    setFlag(QGraphicsItem::ItemIsSelectable, 1)

    updatePath(p)
    setObjectPos(x,y)
    setObjectColor(rgb)
    setObjectLineType(lineType)
    /* TODO: pass in proper lineweight */
    setObjectLineWeight(0.35)
    setPen(objectPen())

def PathObject::updatePath(const QPainterPath& p):
    normalPath = p
    QPainterPath reversePath = normalPath.toReversed()
    reversePath.connectPath(normalPath)
    setObjectPath(reversePath)

def PathObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
    QGraphicsScene* objScene = scene()
    if(!objScene) return

    QPen paintPen = pen()
    painter->setPen(paintPen)
    updateRubber(painter)
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen)

    painter->drawPath(objectPath())

def PathObject::updateRubber(QPainter* painter):
    /*TODO: Path Rubber Modes*/

    /*TODO: updateRubber() gripping for PathObject*/

}

def PathObject::vulcanize():
    debug_message("PathObject vulcanize()")
    updateRubber()

    setObjectRubberMode(OBJ_RUBBER_OFF)

    if(!normalPath.elementCount())
        QMessageBox::critical(0, QObject::tr("Empty Path Error"), QObject::tr("The path added contains no points. The command that created this object has flawed logic."))

/* Returns the closest snap point to the mouse point*/
QPointF PathObject::mouseSnapPoint(const QPointF& mousePoint):
    return scenePos()

QList<QPointF> PathObject::allGripPoints():
    QList<QPointF> gripPoints
    gripPoints << scenePos(); /*TODO: loop thru all path Elements and return their points*/
    return gripPoints

def PathObject::gripEdit(const QPointF& before, const QPointF& after):
    /*TODO: gripEdit() for PathObject*/
}

QPainterPath PathObject::objectCopyPath() const:
    return normalPath

QPainterPath PathObject::objectSavePath() const:
    float s = scale()
    QTransform trans
    trans.rotate(rotation())
    trans.scale(s,s)
    return trans.map(normalPath)


PointObject::PointObject(float x, float y, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("PointObject Constructor()")
    init(x, y, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

PointObject::PointObject(PointObject* obj, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("PointObject Constructor()")
    if(obj)
    {
        init(obj->objectX(), obj->objectY(), obj->objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setRotation(obj->rotation())


PointObject::~PointObject():
    debug_message("PointObject Destructor()")

def PointObject::init(float x, float y, unsigned int rgb, Qt::PenStyle lineType):
    setData(OBJ_TYPE, type())
    setData(OBJ_NAME, obj_names[OBJ_TYPE_POINT])

    setFlag(QGraphicsItem::ItemIsSelectable, 1)

    setRect(-0.00000001, -0.00000001, 0.00000002, 0.00000002)
    setObjectPos(x,y)
    setObjectColor(rgb)
    setObjectLineType(lineType)
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objectPen())

def PointObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
    QGraphicsScene* objScene = scene()
    if(!objScene) return

    QPen paintPen = pen()
    painter->setPen(paintPen)
    updateRubber(painter)
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen)

    painter->drawPoint(0,0)


def PointObject::updateRubber(QPainter* painter):
    int rubberMode = objectRubberMode()
    if(rubberMode == OBJ_RUBBER_GRIP)
    {
        if(painter)
        {
            QPointF gripPoint = objectRubberPoint("GRIP_POINT")
            if(gripPoint == scenePos())
            {
                QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
                drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")


def PointObject::vulcanize():
    debug_message("PointObject vulcanize()")
    updateRubber()

    setObjectRubberMode(OBJ_RUBBER_OFF)

/* Returns the closest snap point to the mouse point*/
QPointF PointObject::mouseSnapPoint(const QPointF& mousePoint):
    return scenePos()

QList<QPointF> PointObject::allGripPoints():
    QList<QPointF> gripPoints
    gripPoints << scenePos()
    return gripPoints

def PointObject::gripEdit(const QPointF& before, const QPointF& after):
    if(before == scenePos()) { QPointF delta = after-before; moveBy(delta.x(), delta.y()); }
}

QPainterPath PointObject::objectSavePath() const:
    QPainterPath path
    path.addRect(-0.00000001, -0.00000001, 0.00000002, 0.00000002)
    return path


PolygonObject::PolygonObject(float x, float y, const QPainterPath& p, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("PolygonObject Constructor()")
    init(x, y, p, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

PolygonObject::PolygonObject(PolygonObject* obj, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("PolygonObject Constructor()")
    if(obj)
    {
        init(obj->objectX(), obj->objectY(), obj->objectCopyPath(), obj->objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setRotation(obj->rotation())
        setScale(obj->scale())
    }
}

PolygonObject::~PolygonObject():
    debug_message("PolygonObject Destructor()")

def PolygonObject::init(float x, float y, const QPainterPath& p, unsigned int rgb, Qt::PenStyle lineType):
    setData(OBJ_TYPE, type())
    setData(OBJ_NAME, obj_names[OBJ_TYPE_POLYGON])

    setFlag(QGraphicsItem::ItemIsSelectable, 1)

    gripIndex = -1
    updatePath(p)
    setObjectPos(x,y)
    setObjectColor(rgb)
    setObjectLineType(lineType)
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objectPen())

def PolygonObject::updatePath(const QPainterPath& p):
    normalPath = p
    QPainterPath closedPath = normalPath
    closedPath.closeSubpath()
    QPainterPath reversePath = closedPath.toReversed()
    reversePath.connectPath(closedPath)
    setObjectPath(reversePath)

def PolygonObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
    QGraphicsScene* objScene = scene()
    if(!objScene) return

    QPen paintPen = pen()
    painter->setPen(paintPen)
    updateRubber(painter)
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen)

    if(normalPath.elementCount())
    {
        painter->drawPath(normalPath)
        QPainterPath::Element zero = normalPath.elementAt(0)
        QPainterPath::Element last = normalPath.elementAt(normalPath.elementCount()-1)
        painter->drawLine(QPointF(zero.x, zero.y), QPointF(last.x, last.y))
    }
}

def PolygonObject::updateRubber(QPainter* painter):
    int rubberMode = objectRubberMode()
    if (rubberMode == OBJ_RUBBER_POLYGON) {
        setObjectPos(objectRubberPoint("POLYGON_POINT_0"))

        bool ok = 0
        QString numStr = objectRubberText("POLYGON_NUM_POINTS")
        if(numStr.isNull()) return
        int num = numStr.toInt(&ok)
        if(!ok) return

        QString appendStr
        QPainterPath rubberPath
        rubberPath.moveTo(mapFromScene(objectRubberPoint("POLYGON_POINT_0")))
        for(int i = 1; i <= num; i++)
        {
            appendStr = "POLYGON_POINT_" + QString().setNum(i)
            QPointF appendPoint = mapFromScene(objectRubberPoint(appendStr))
            rubberPath.lineTo(appendPoint)
        }
        /*rubberPath.lineTo(0,0);*/
        updatePath(rubberPath)

        /*Ensure the path isn't updated until the number of points is changed again*/
        setObjectRubberText("POLYGON_NUM_POINTS", QString())
    }
    elif(rubberMode == OBJ_RUBBER_POLYGON_INSCRIBE) {
        setObjectPos(objectRubberPoint("POLYGON_CENTER"))

        unsigned short numSides = objectRubberPoint("POLYGON_NUM_SIDES").x()

        QPointF inscribePoint = mapFromScene(objectRubberPoint("POLYGON_INSCRIBE_POINT"))
        QLineF inscribeLine = QLineF(QPointF(0,0), inscribePoint)
        float inscribeAngle = inscribeLine.angle()
        float inscribeInc = 360.0/numSides

        if(painter) drawRubberLine(inscribeLine, painter, "VIEW_COLOR_CROSSHAIR")

        QPainterPath inscribePath
        /*First Point*/
        inscribePath.moveTo(inscribePoint)
        /*Remaining Points*/
        for (int i = 1; i < numSides; i++) {
            inscribeLine.setAngle(inscribeAngle + inscribeInc*i)
            inscribePath.lineTo(inscribeLine.p2())
        }
        updatePath(inscribePath)
    }
    elif (rubberMode == OBJ_RUBBER_POLYGON_CIRCUMSCRIBE) {
        setObjectPos(objectRubberPoint("POLYGON_CENTER"))

        unsigned short numSides = objectRubberPoint("POLYGON_NUM_SIDES").x()

        QPointF circumscribePoint = mapFromScene(objectRubberPoint("POLYGON_CIRCUMSCRIBE_POINT"))
        QLineF circumscribeLine = QLineF(QPointF(0,0), circumscribePoint)
        float circumscribeAngle = circumscribeLine.angle()
        float circumscribeInc = 360.0/numSides

        if(painter) drawRubberLine(circumscribeLine, painter, "VIEW_COLOR_CROSSHAIR")

        QPainterPath circumscribePath
        /*First Point*/
        QLineF prev(circumscribeLine.p2(), QPointF(0,0))
        prev = prev.normalVector()
        circumscribeLine.setAngle(circumscribeAngle + circumscribeInc)
        QLineF perp(circumscribeLine.p2(), QPointF(0,0))
        perp = perp.normalVector()
        QPointF iPoint
        /* HACK perp.intersects(prev, &iPoint); */
        iPoint = perp.p1()
        circumscribePath.moveTo(iPoint)
        /*Remaining Points*/
        for(int i = 2; i <= numSides; i++)
        {
            prev = perp
            circumscribeLine.setAngle(circumscribeAngle + circumscribeInc*i)
            perp = QLineF(circumscribeLine.p2(), QPointF(0,0))
            perp = perp.normalVector()
            /* HACK perp.intersects(prev, &iPoint); */
            iPoint = perp.p1()
            circumscribePath.lineTo(iPoint)
        }
        updatePath(circumscribePath)
    }
    elif(rubberMode == OBJ_RUBBER_GRIP) {
        if(painter) {
            int elemCount = normalPath.elementCount()
            QPointF gripPoint = objectRubberPoint("GRIP_POINT")
            if(gripIndex == -1) gripIndex = findIndex(gripPoint)
            if(gripIndex == -1) return

            int m = 0
            int n = 0

            if(!gripIndex)                    { m = elemCount-1; n = 1; }
            elif(gripIndex == elemCount-1) { m = elemCount-2; n = 0; }
            else                              { m = gripIndex-1; n = gripIndex+1; }
            QPainterPath::Element em = normalPath.elementAt(m)
            QPainterPath::Element en = normalPath.elementAt(n)
            QPointF emPoint = QPointF(em.x, em.y)
            QPointF enPoint = QPointF(en.x, en.y)
            painter->drawLine(emPoint, mapFromScene(objectRubberPoint(QString())))
            painter->drawLine(enPoint, mapFromScene(objectRubberPoint(QString())))

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")
        }
    }
}

def PolygonObject::vulcanize():
    debug_message("PolygonObject vulcanize()")
    updateRubber()

    setObjectRubberMode(OBJ_RUBBER_OFF)

    if(!normalPath.elementCount())
        QMessageBox::critical(0, QObject::tr("Empty Polygon Error"), QObject::tr("The polygon added contains no points. The command that created this object has flawed logic."))

/* Returns the closest snap point to the mouse point*/
QPointF PolygonObject::mouseSnapPoint(const QPointF& mousePoint):
    QPainterPath::Element element = normalPath.elementAt(0)
    QPointF closestPoint = mapToScene(QPointF(element.x, element.y))
    float closestDist = QLineF(mousePoint, closestPoint).length()
    int elemCount = normalPath.elementCount()
    for(int i = 0; i < elemCount; ++i)
    {
        element = normalPath.elementAt(i)
        QPointF elemPoint = mapToScene(element.x, element.y)
        float elemDist = QLineF(mousePoint, elemPoint).length()
        if(elemDist < closestDist)
        {
            closestPoint = elemPoint
            closestDist = elemDist
        }
    }
    return closestPoint

QList<QPointF> PolygonObject::allGripPoints():
    QList<QPointF> gripPoints
    QPainterPath::Element element
    for(int i = 0; i < normalPath.elementCount(); ++i)
    {
        element = normalPath.elementAt(i)
        gripPoints << mapToScene(element.x, element.y)
    }
    return gripPoints

int PolygonObject::findIndex(const QPointF& point):
    int i = 0
    int elemCount = normalPath.elementCount()
    /*NOTE: Points here are in item coordinates*/
    QPointF itemPoint = mapFromScene(point)
    for(i = 0; i < elemCount; i++)
    {
        QPainterPath::Element e = normalPath.elementAt(i)
        QPointF elemPoint = QPointF(e.x, e.y)
        if(itemPoint == elemPoint) return i
    }
    return -1

def PolygonObject::gripEdit(const QPointF& before, const QPointF& after):
    gripIndex = findIndex(before)
    if(gripIndex == -1) return
    QPointF a = mapFromScene(after)
    normalPath.setElementPositionAt(gripIndex, a.x(), a.y())
    updatePath(normalPath)
    gripIndex = -1

QPainterPath PolygonObject::objectCopyPath() const:
    return normalPath

QPainterPath PolygonObject::objectSavePath() const:
    QPainterPath closedPath = normalPath
    closedPath.closeSubpath()
    float s = scale()
    QTransform trans
    trans.rotate(rotation())
    trans.scale(s,s)
    return trans.map(closedPath)


PolylineObject::PolylineObject(float x, float y, const QPainterPath& p, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("PolylineObject Constructor()")
    init(x, y, p, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

PolylineObject::PolylineObject(PolylineObject* obj, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("PolylineObject Constructor()")
    if(obj)
    {
        init(obj->objectX(), obj->objectY(), obj->objectCopyPath(), obj->objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setRotation(obj->rotation())
        setScale(obj->scale())
    }
}

PolylineObject::~PolylineObject():
    debug_message("PolylineObject Destructor()")

def PolylineObject::init(float x, float y, const QPainterPath& p, unsigned int rgb, Qt::PenStyle lineType):
    setData(OBJ_TYPE, PolylineObject::Type)
    setData(OBJ_NAME, obj_names[OBJ_TYPE_POLYLINE])

    setFlag(QGraphicsItem::ItemIsSelectable, 1)

    gripIndex = -1
    updatePath(p)
    setObjectPos(x,y)
    setObjectColor(rgb)
    setObjectLineType(lineType)
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objectPen())

def PolylineObject::updatePath(const QPainterPath& p):
    normalPath = p
    QPainterPath reversePath = normalPath.toReversed()
    reversePath.connectPath(normalPath)
    setObjectPath(reversePath)

def PolylineObject::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* /*widget*/):
    QGraphicsScene* objScene = scene()
    if(!objScene) return

    QPen paintPen = pen()
    painter->setPen(paintPen)
    updateRubber(painter)
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen)

    painter->drawPath(normalPath)

    if(objScene->property("ENABLE_LWT").toBool() && objScene->property("ENABLE_REAL").toBool()) { realRender(painter, normalPath); }
}

def PolylineObject::updateRubber(QPainter* painter):
    int rubberMode = objectRubberMode()
    if(rubberMode == OBJ_RUBBER_POLYLINE)
    {
        setObjectPos(objectRubberPoint("POLYLINE_POINT_0"))

        QLineF rubberLine(normalPath.currentPosition(), mapFromScene(objectRubberPoint(QString())))
        if(painter) drawRubberLine(rubberLine, painter, "VIEW_COLOR_CROSSHAIR")

        bool ok = 0
        QString numStr = objectRubberText("POLYLINE_NUM_POINTS")
        if(numStr.isNull()) return
        int num = numStr.toInt(&ok)
        if(!ok) return

        QString appendStr
        QPainterPath rubberPath
        for(int i = 1; i <= num; i++)
        {
            appendStr = "POLYLINE_POINT_" + QString().setNum(i)
            QPointF appendPoint = mapFromScene(objectRubberPoint(appendStr))
            rubberPath.lineTo(appendPoint)
        }
        updatePath(rubberPath)

        /*Ensure the path isn't updated until the number of points is changed again*/
        setObjectRubberText("POLYLINE_NUM_POINTS", QString())
    }
    elif(rubberMode == OBJ_RUBBER_GRIP)
    {
        if(painter)
        {
            int elemCount = normalPath.elementCount()
            QPointF gripPoint = objectRubberPoint("GRIP_POINT")
            if(gripIndex == -1) gripIndex = findIndex(gripPoint)
            if(gripIndex == -1) return

            if(!gripIndex) /*First*/
            {
                QPainterPath::Element ef = normalPath.elementAt(1)
                QPointF efPoint = QPointF(ef.x, ef.y)
                painter->drawLine(efPoint, mapFromScene(objectRubberPoint(QString())))
            }
            elif(gripIndex == elemCount-1) /*Last*/
            {
                QPainterPath::Element el = normalPath.elementAt(gripIndex-1)
                QPointF elPoint = QPointF(el.x, el.y)
                painter->drawLine(elPoint, mapFromScene(objectRubberPoint(QString())))
            }
            else /*Middle*/
            {
                QPainterPath::Element em = normalPath.elementAt(gripIndex-1)
                QPainterPath::Element en = normalPath.elementAt(gripIndex+1)
                QPointF emPoint = QPointF(em.x, em.y)
                QPointF enPoint = QPointF(en.x, en.y)
                painter->drawLine(emPoint, mapFromScene(objectRubberPoint(QString())))
                painter->drawLine(enPoint, mapFromScene(objectRubberPoint(QString())))
            }

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")
        }
    }
}

def PolylineObject::vulcanize():
    debug_message("PolylineObject vulcanize()")
    updateRubber()

    setObjectRubberMode(OBJ_RUBBER_OFF)

    if(!normalPath.elementCount())
        QMessageBox::critical(0, QObject::tr("Empty Polyline Error"), QObject::tr("The polyline added contains no points. The command that created this object has flawed logic."))

/* Returns the closest snap point to the mouse point*/
QPointF PolylineObject::mouseSnapPoint(const QPointF& mousePoint):
    QPainterPath::Element element = normalPath.elementAt(0)
    QPointF closestPoint = mapToScene(QPointF(element.x, element.y))
    float closestDist = QLineF(mousePoint, closestPoint).length()
    int elemCount = normalPath.elementCount()
    for(int i = 0; i < elemCount; ++i)
    {
        element = normalPath.elementAt(i)
        QPointF elemPoint = mapToScene(element.x, element.y)
        float elemDist = QLineF(mousePoint, elemPoint).length()
        if(elemDist < closestDist)
        {
            closestPoint = elemPoint
            closestDist = elemDist
        }
    }
    return closestPoint

QList<QPointF> PolylineObject::allGripPoints():
    QList<QPointF> gripPoints
    QPainterPath::Element element
    for(int i = 0; i < normalPath.elementCount(); ++i)
    {
        element = normalPath.elementAt(i)
        gripPoints << mapToScene(element.x, element.y)
    }
    return gripPoints

int PolylineObject::findIndex(const QPointF& point):
    int elemCount = normalPath.elementCount()
    /*NOTE: Points here are in item coordinates*/
    QPointF itemPoint = mapFromScene(point)
    for (int i = 0; i < elemCount; i++) {
        QPainterPath::Element e = normalPath.elementAt(i)
        QPointF elemPoint = QPointF(e.x, e.y)
        if(itemPoint == elemPoint) return i
    }
    return -1

def PolylineObject::gripEdit(const QPointF& before, const QPointF& after):
    gripIndex = findIndex(before)
    if(gripIndex == -1) return
    QPointF a = mapFromScene(after)
    normalPath.setElementPositionAt(gripIndex, a.x(), a.y())
    updatePath(normalPath)
    gripIndex = -1

QPainterPath PolylineObject::objectCopyPath() const:
    return normalPath

QPainterPath PolylineObject::objectSavePath() const:
    float s = scale()
    QTransform trans
    trans.rotate(rotation())
    trans.scale(s,s)
    return trans.map(normalPath)


RectObject::RectObject(float x, float y, float w, float h, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("RectObject Constructor()")
    init(x, y, w, h, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

RectObject::RectObject(RectObject* obj, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("RectObject Constructor()")
    if(obj)
    {
        QPointF ptl = obj->objectTopLeft()
        init(ptl.x(), ptl.y(), obj->objectWidth(), obj->objectHeight(), obj->objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setRotation(obj->rotation())
    }
}

RectObject::~RectObject():
    debug_message("RectObject Destructor()")

def RectObject::init(float x, float y, float w, float h, unsigned int rgb, Qt::PenStyle lineType):
    setData(OBJ_TYPE, type())
    setData(OBJ_NAME, obj_names[OBJ_TYPE_RECTANGLE])

    setFlag(QGraphicsItem::ItemIsSelectable, 1)

    setObjectRect(x, y, w, h)
    setObjectColor(rgb)
    setObjectLineType(lineType)
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objectPen())

def RectObject::setObjectRect(float x, float y, float w, float h):
    setPos(x, y)
    setRect(0, 0, w, h)
    updatePath()

QPointF RectObject::objectTopLeft() const:
    EmbVector v
    v = to_emb_vector(rect().topLeft())
    v = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(v)

QPointF RectObject::objectTopRight() const:
    EmbVector v
    v = to_emb_vector(rect().topRight())
    v = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(v)

QPointF RectObject::objectBottomLeft() const:
    EmbVector v
    v = to_emb_vector(rect().bottomLeft())
    v = scale_and_rotate(v, scale(), radians(rotation()))

    return scenePos() + to_qpointf(v)

QPointF RectObject::objectBottomRight() const:
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
    if(!objScene) return

    QPen paintPen = pen()
    painter->setPen(paintPen)
    updateRubber(painter)
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen)

    painter->drawRect(rect())

def RectObject::updateRubber(QPainter* painter):
    int rubberMode = objectRubberMode()
    if(rubberMode == OBJ_RUBBER_RECTANGLE)
    {
        QPointF sceneStartPoint = objectRubberPoint("RECTANGLE_START")
        QPointF sceneEndPoint = objectRubberPoint("RECTANGLE_END")
        float x = sceneStartPoint.x()
        float y = sceneStartPoint.y()
        float w = sceneEndPoint.x() - sceneStartPoint.x()
        float h = sceneEndPoint.y() - sceneStartPoint.y()
        setObjectRect(x,y,w,h)
        updatePath()
    }
    elif(rubberMode == OBJ_RUBBER_GRIP)
    {
        if(painter)
        {
            /* TODO: Make this work with rotation & scaling. */
            /*
            QPointF gripPoint = objectRubberPoint("GRIP_POINT")
            QPointF after = objectRubberPoint(QString())
            QPointF delta = after-gripPoint
            if     (gripPoint == objectTopLeft())     { painter->drawPolygon(mapFromScene(QRectF(after.x(), after.y(), objectWidth()-delta.x(), objectHeight()-delta.y()))); }
            elif(gripPoint == objectTopRight())    { painter->drawPolygon(mapFromScene(QRectF(objectTopLeft().x(), objectTopLeft().y()+delta.y(), objectWidth()+delta.x(), objectHeight()-delta.y()))); }
            elif(gripPoint == objectBottomLeft())  { painter->drawPolygon(mapFromScene(QRectF(objectTopLeft().x()+delta.x(), objectTopLeft().y(), objectWidth()-delta.x(), objectHeight()+delta.y()))); }
            elif(gripPoint == objectBottomRight()) { painter->drawPolygon(mapFromScene(QRectF(objectTopLeft().x(), objectTopLeft().y(), objectWidth()+delta.x(), objectHeight()+delta.y()))); }

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")
            */

            QPointF gripPoint = objectRubberPoint("GRIP_POINT")
            QPointF after = objectRubberPoint(QString())
            QPointF delta = after-gripPoint

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")
        }
    }
}

def RectObject::vulcanize():
    debug_message("RectObject vulcanize()")
    updateRubber()

    setObjectRubberMode(OBJ_RUBBER_OFF)

/* Returns the closest snap point to the mouse point*/
QPointF RectObject::mouseSnapPoint(const QPointF& mousePoint):
    QPointF ptl = objectTopLeft();     /*Top Left Corner QSnap*/
    QPointF ptr = objectTopRight();    /*Top Right Corner QSnap*/
    QPointF pbl = objectBottomLeft();  /*Bottom Left Corner QSnap*/
    QPointF pbr = objectBottomRight(); /*Bottom Right Corner QSnap*/

    float ptlDist = QLineF(mousePoint, ptl).length()
    float ptrDist = QLineF(mousePoint, ptr).length()
    float pblDist = QLineF(mousePoint, pbl).length()
    float pbrDist = QLineF(mousePoint, pbr).length()

    float minDist = qMin(qMin(ptlDist, ptrDist), qMin(pblDist, pbrDist))

    if     (minDist == ptlDist) return ptl
    elif(minDist == ptrDist) return ptr
    elif(minDist == pblDist) return pbl
    elif(minDist == pbrDist) return pbr

    return scenePos()

QList<QPointF> RectObject::allGripPoints():
    QList<QPointF> gripPoints
    gripPoints << objectTopLeft() << objectTopRight() << objectBottomLeft() << objectBottomRight()
    return gripPoints

def RectObject::gripEdit(const QPointF& before, const QPointF& after):
    QPointF delta = after-before
    if     (before == objectTopLeft())     { setObjectRect(after.x(), after.y(), objectWidth()-delta.x(), objectHeight()-delta.y()); }
    elif(before == objectTopRight())    { setObjectRect(objectTopLeft().x(), objectTopLeft().y()+delta.y(), objectWidth()+delta.x(), objectHeight()-delta.y()); }
    elif(before == objectBottomLeft())  { setObjectRect(objectTopLeft().x()+delta.x(), objectTopLeft().y(), objectWidth()-delta.x(), objectHeight()+delta.y()); }
    elif(before == objectBottomRight()) { setObjectRect(objectTopLeft().x(), objectTopLeft().y(), objectWidth()+delta.x(), objectHeight()+delta.y()); }
}

QPainterPath RectObject::objectSavePath() const:
    QPainterPath path
    QRectF r = rect()
    path.moveTo(r.bottomLeft())
    path.lineTo(r.bottomRight())
    path.lineTo(r.topRight())
    path.lineTo(r.topLeft())
    path.lineTo(r.bottomLeft())

    float s = scale()
    QTransform trans
    trans.rotate(rotation())
    trans.scale(s,s)
    return trans.map(path)


TextSingleObject::TextSingleObject(const QString& str, float x, float y, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("TextSingleObject Constructor()")
    init(str, x, y, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

TextSingleObject::TextSingleObject(TextSingleObject* obj, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("TextSingleObject Constructor()")
    if (obj) {
        objTextFont = obj->objTextFont
        obj_text = obj->obj_text
        setRotation(obj->rotation())
        setObjectText(obj->objText)
        init(obj->objText, obj->objectX(), obj->objectY(), obj->objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setScale(obj->scale())
    }
}

TextSingleObject::~TextSingleObject():
    debug_message("TextSingleObject Destructor()")

def TextSingleObject::init(const QString& str, float x, float y, unsigned int rgb, Qt::PenStyle lineType):
    setData(OBJ_TYPE, type())
    setData(OBJ_NAME, obj_names[OBJ_TYPE_TEXTSINGLE])

    setFlag(QGraphicsItem::ItemIsSelectable, 1)

    objTextJustify = "Left"; /*TODO: set the justification properly*/

    setObjectText(str)
    setObjectPos(x,y)
    setObjectColor(rgb)
    setObjectLineType(lineType)
    setObjectLineWeight(0.35); /*TODO: pass in proper lineweight*/
    setPen(objectPen())

QStringList TextSingleObject::objectTextJustifyList() const:
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
    if     (objTextJustify == "Left")          { textPath.translate(-jRect.left(), 0); }
    elif(objTextJustify == "Center")        { textPath.translate(-jRect.center().x(), 0); }
    elif(objTextJustify == "Right")         { textPath.translate(-jRect.right(), 0); }
    elif(objTextJustify == "Aligned")       { } /*TODO: TextSingleObject Aligned Justification*/
    elif(objTextJustify == "Middle")        { textPath.translate(-jRect.center()); }
    elif(objTextJustify == "Fit")           { } /*TODO: TextSingleObject Fit Justification*/
    elif(objTextJustify == "Top Left")      { textPath.translate(-jRect.topLeft()); }
    elif(objTextJustify == "Top Center")    { textPath.translate(-jRect.center().x(), -jRect.top()); }
    elif(objTextJustify == "Top Right")     { textPath.translate(-jRect.topRight()); }
    elif(objTextJustify == "Middle Left")   { textPath.translate(-jRect.left(), -jRect.top()/2.0); }
    elif(objTextJustify == "Middle Center") { textPath.translate(-jRect.center().x(), -jRect.top()/2.0); }
    elif(objTextJustify == "Middle Right")  { textPath.translate(-jRect.right(), -jRect.top()/2.0); }
    elif(objTextJustify == "Bottom Left")   { textPath.translate(-jRect.bottomLeft()); }
    elif(objTextJustify == "Bottom Center") { textPath.translate(-jRect.center().x(), -jRect.bottom()); }
    elif(objTextJustify == "Bottom Right")  { textPath.translate(-jRect.bottomRight()); }

    /*Backward or Upside Down*/
    if(obj_text.backward || obj_text.upsidedown)
    {
        float horiz = 1.0
        float vert = 1.0
        if(obj_text.backward) horiz = -1.0
        if(obj_text.upsidedown) vert = -1.0

        QPainterPath flippedPath

        QPainterPath::Element element
        QPainterPath::Element P2
        QPainterPath::Element P3
        QPainterPath::Element P4
        for(int i = 0; i < textPath.elementCount(); ++i)
        {
            element = textPath.elementAt(i)
            if(element.isMoveTo())
            {
                flippedPath.moveTo(horiz * element.x, vert * element.y)
            }
            elif(element.isLineTo())
            {
                flippedPath.lineTo(horiz * element.x, vert * element.y)
            }
            elif(element.isCurveTo())
            {
                                              /* start point P1 is not needed*/
                P2 = textPath.elementAt(i);   /* control point*/
                P3 = textPath.elementAt(i+1); /* control point*/
                P4 = textPath.elementAt(i+2); /* end point*/

                flippedPath.cubicTo(horiz * P2.x, vert * P2.y,
                                    horiz * P3.x, vert * P3.y,
                                    horiz * P4.x, vert * P4.y)
            }
        }
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
    if (justify == "Left") {
        objTextJustify = justify
    }
    elif(justify == "Center")        { objTextJustify = justify; }
    elif(justify == "Right")         { objTextJustify = justify; }
    elif(justify == "Aligned")       { objTextJustify = justify; }
    elif(justify == "Middle")        { objTextJustify = justify; }
    elif(justify == "Fit")           { objTextJustify = justify; }
    elif(justify == "Top Left")      { objTextJustify = justify; }
    elif(justify == "Top Center")    { objTextJustify = justify; }
    elif(justify == "Top Right")     { objTextJustify = justify; }
    elif(justify == "Middle Left")   { objTextJustify = justify; }
    elif(justify == "Middle Center") { objTextJustify = justify; }
    elif(justify == "Middle Right")  { objTextJustify = justify; }
    elif(justify == "Bottom Left")   { objTextJustify = justify; }
    elif(justify == "Bottom Center") { objTextJustify = justify; }
    elif(justify == "Bottom Right")  { objTextJustify = justify; }
    else                                { objTextJustify = "Left";  } /*Default*/
    setObjectText(objText)

def TextSingleObject::setObjectTextSize(float size):
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
    if(!objScene) return

    QPen paintPen = pen()
    painter->setPen(paintPen)
    updateRubber(painter)
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen)

    painter->drawPath(objTextPath)

def TextSingleObject::updateRubber(QPainter* painter):
    int rubberMode = objectRubberMode()
    if (rubberMode == OBJ_RUBBER_TEXTSINGLE) {
        setObjectTextFont(objectRubberText("TEXT_FONT"))
        setObjectTextJustify(objectRubberText("TEXT_JUSTIFY"))
        setObjectPos(objectRubberPoint("TEXT_POINT"))
        QPointF hr = objectRubberPoint("TEXT_HEIGHT_ROTATION")
        setObjectTextSize(hr.x())
        setRotation(hr.y())
        setObjectText(objectRubberText("TEXT_RAPID"))
    }
    elif(rubberMode == OBJ_RUBBER_GRIP) {
        if (painter) {
            QPointF gripPoint = objectRubberPoint("GRIP_POINT")
            if (gripPoint == scenePos()) {
                painter->drawPath(objectPath().translated(mapFromScene(objectRubberPoint(QString()))-mapFromScene(gripPoint)))
            }

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")
        }
    }
}

def TextSingleObject::vulcanize():
    debug_message("TextSingleObject vulcanize()")
    updateRubber()

    setObjectRubberMode(OBJ_RUBBER_OFF)

/* Returns the closest snap point to the mouse point*/
QPointF TextSingleObject::mouseSnapPoint(const QPointF& mousePoint):
    return scenePos()

QList<QPointF> TextSingleObject::allGripPoints():
    QList<QPointF> gripPoints
    gripPoints << scenePos()
    return gripPoints

def TextSingleObject::gripEdit(const QPointF& before, const QPointF& after):
    if(before == scenePos()) { QPointF delta = after-before; moveBy(delta.x(), delta.y()); }
}

QList<QPainterPath> TextSingleObject::subPathList() const:
    float s = scale()
    QTransform trans
    trans.rotate(rotation())
    trans.scale(s,s)

    QList<QPainterPath> pathList

    QPainterPath path = objTextPath

    QPainterPath::Element element
    QList<int> pathMoves
    int numMoves = 0

    for(int i = 0; i < path.elementCount(); i++)
    {
        element = path.elementAt(i)
        if(element.isMoveTo())
        {
            pathMoves << i
            numMoves++
        }
    }

    pathMoves << path.elementCount()

    for (int p = 0; p < pathMoves.size()-1 && p < numMoves; p++) {
        QPainterPath subPath
        for (int i = pathMoves.value(p); i < pathMoves.value(p+1); i++) {
            element = path.elementAt(i)
            if (element.isMoveTo()) {
                subPath.moveTo(element.x, element.y)
            }
            elif (element.isLineTo()) {
                subPath.lineTo(element.x, element.y)
            }
            elif (element.isCurveTo()) {
                subPath.cubicTo(path.elementAt(i  ).x, path.elementAt(i  ).y, /*control point 1*/
                                path.elementAt(i+1).x, path.elementAt(i+1).y, /*control point 2*/
                                path.elementAt(i+2).x, path.elementAt(i+2).y); /*end point*/
            }
        }
        pathList.append(trans.map(subPath))
    }

    return pathList
    
CircleObject::CircleObject(float centerX, float centerY, float radius, unsigned int rgb, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("CircleObject Constructor()")
    init(centerX, centerY, radius, rgb, Qt::SolidLine); /*TODO: getCurrentLineType*/
}

CircleObject::CircleObject(CircleObject* obj, QGraphicsItem* parent) : BaseObject(parent):
    debug_message("CircleObject Constructor()")
    if(obj)
    {
        QPointF p = obj->objectCenter()
        float r = obj->objectRadius()
        init(p.x(), p.y(), r, obj->objectColorRGB(), Qt::SolidLine); /*TODO: getCurrentLineType*/
        setRotation(obj->rotation())
    }
}

CircleObject::~CircleObject():
    debug_message("CircleObject Destructor()")

def CircleObject::init(float centerX, float centerY, float radius, unsigned int rgb, Qt::PenStyle lineType):
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

def CircleObject::setObjectRadius(float radius):
    setObjectDiameter(radius*2.0)

def CircleObject::setObjectDiameter(float diameter):
    QRectF circRect
    circRect.setWidth(diameter)
    circRect.setHeight(diameter)
    circRect.moveCenter(QPointF(0,0))
    setRect(circRect)
    updatePath()

def CircleObject::setObjectArea(float area):
    float radius = sqrt(area/embConstantPi)
    setObjectRadius(radius)

def CircleObject::setObjectCircumference(float circumference):
    float diameter = circumference/embConstantPi
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
    if(!objScene) return

    QPen paintPen = pen()
    painter->setPen(paintPen)
    updateRubber(painter)
    if(option->state & QStyle::State_Selected)  { paintPen.setStyle(Qt::DashLine); }
    if(objScene->property("ENABLE_LWT").toBool()) { paintPen = lineWeightPen(); }
    painter->setPen(paintPen)

    painter->drawEllipse(rect())

def CircleObject::updateRubber(QPainter* painter):
    int rubberMode = objectRubberMode()
    if(rubberMode == OBJ_RUBBER_CIRCLE_1P_RAD)
    {
        QPointF sceneCenterPoint = objectRubberPoint("CIRCLE_CENTER")
        QPointF sceneQSnapPoint = objectRubberPoint("CIRCLE_RADIUS")
        QPointF itemCenterPoint = mapFromScene(sceneCenterPoint)
        QPointF itemQSnapPoint = mapFromScene(sceneQSnapPoint)
        QLineF itemLine(itemCenterPoint, itemQSnapPoint)
        setPos(sceneCenterPoint)
        QLineF sceneLine(sceneCenterPoint, sceneQSnapPoint)
        float radius = sceneLine.length()
        setObjectRadius(radius)
        if(painter) drawRubberLine(itemLine, painter, "VIEW_COLOR_CROSSHAIR")
        updatePath()
    }
    elif(rubberMode == OBJ_RUBBER_CIRCLE_1P_DIA)
    {
        QPointF sceneCenterPoint = objectRubberPoint("CIRCLE_CENTER")
        QPointF sceneQSnapPoint = objectRubberPoint("CIRCLE_DIAMETER")
        QPointF itemCenterPoint = mapFromScene(sceneCenterPoint)
        QPointF itemQSnapPoint = mapFromScene(sceneQSnapPoint)
        QLineF itemLine(itemCenterPoint, itemQSnapPoint)
        setPos(sceneCenterPoint)
        QLineF sceneLine(sceneCenterPoint, sceneQSnapPoint)
        float diameter = sceneLine.length()
        setObjectDiameter(diameter)
        if(painter) drawRubberLine(itemLine, painter, "VIEW_COLOR_CROSSHAIR")
        updatePath()
    }
    elif(rubberMode == OBJ_RUBBER_CIRCLE_2P)
    {
        QPointF sceneTan1Point = objectRubberPoint("CIRCLE_TAN1")
        QPointF sceneQSnapPoint = objectRubberPoint("CIRCLE_TAN2")
        QLineF sceneLine(sceneTan1Point, sceneQSnapPoint)
        setPos(sceneLine.pointAt(0.5))
        float diameter = sceneLine.length()
        setObjectDiameter(diameter)
        updatePath()
    }
    elif(rubberMode == OBJ_RUBBER_CIRCLE_3P)
    {
        QPointF sceneTan1Point = objectRubberPoint("CIRCLE_TAN1")
        QPointF sceneTan2Point = objectRubberPoint("CIRCLE_TAN2")
        QPointF sceneTan3Point = objectRubberPoint("CIRCLE_TAN3")

        EmbVector sceneCenter
        EmbArc arc = embArcObject_make(sceneTan1Point.x(), sceneTan1Point.y(),
                             sceneTan2Point.x(), sceneTan2Point.y(),
                             sceneTan3Point.x(), sceneTan3Point.y()).arc
        getArcCenter(arc, &sceneCenter)
        QPointF sceneCenterPoint(sceneCenter.x, sceneCenter.y)
        QLineF sceneLine(sceneCenterPoint, sceneTan3Point)
        setPos(sceneCenterPoint)
        float radius = sceneLine.length()
        setObjectRadius(radius)
        updatePath()
    }
    elif(rubberMode == OBJ_RUBBER_GRIP)
    {
        if(painter)
        {
            QPointF gripPoint = objectRubberPoint("GRIP_POINT")
            if(gripPoint == objectCenter())
            {
                painter->drawEllipse(rect().translated(mapFromScene(objectRubberPoint(QString()))-mapFromScene(gripPoint)))
            }
            else
            {
                float gripRadius = QLineF(objectCenter(), objectRubberPoint(QString())).length()
                painter->drawEllipse(QPointF(), gripRadius, gripRadius)
            }

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")
        }
    }
}

def CircleObject::vulcanize():
    debug_message("CircleObject vulcanize()")
    updateRubber()

    setObjectRubberMode(OBJ_RUBBER_OFF)

/* Returns the closest snap point to the mouse point */
QPointF CircleObject::mouseSnapPoint(const QPointF& mousePoint):
    QPointF center = objectCenter()
    QPointF quad0 = objectQuadrant0()
    QPointF quad90 = objectQuadrant90()
    QPointF quad180 = objectQuadrant180()
    QPointF quad270 = objectQuadrant270()

    float cntrDist = QLineF(mousePoint, center).length()
    float q0Dist = QLineF(mousePoint, quad0).length()
    float q90Dist = QLineF(mousePoint, quad90).length()
    float q180Dist = QLineF(mousePoint, quad180).length()
    float q270Dist = QLineF(mousePoint, quad270).length()

    float minDist = qMin(qMin(qMin(q0Dist, q90Dist), qMin(q180Dist, q270Dist)), cntrDist)

    if     (minDist == cntrDist) return center
    elif(minDist == q0Dist)   return quad0
    elif(minDist == q90Dist)  return quad90
    elif(minDist == q180Dist) return quad180
    elif(minDist == q270Dist) return quad270

    return scenePos()

QList<QPointF> CircleObject::allGripPoints():
    QList<QPointF> gripPoints
    gripPoints << objectCenter() << objectQuadrant0() << objectQuadrant90() << objectQuadrant180() << objectQuadrant270()
    return gripPoints

def CircleObject::gripEdit(const QPointF& before, const QPointF& after):
    if(before == objectCenter()) { QPointF delta = after-before; moveBy(delta.x(), delta.y()); }
    else                         { setObjectRadius(QLineF(objectCenter(), after).length()); }
}

QPainterPath CircleObject::objectSavePath() const:
    QPainterPath path
    QRectF r = rect()
    path.arcMoveTo(r, 0)
    path.arcTo(r, 0, 360)

    float s = scale()
    QTransform trans
    trans.rotate(rotation())
    trans.scale(s,s)
    return trans.map(path)

