#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    -----

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENSE for licensing terms.

    -----

    Another attempt at a graphical user interface that runs on
    lots of machines without a complex build or fragile dependencies.

    This is a translation of some of the ideas we came up with for other
    attempts.
"""

import os
import libembroidery

from .data import layout, settings

preview = settings.copy()
dialog = settings.copy()
accept = settings.copy()
undo_history = []
undo_history_position = 0

def draw_pixmap(description):
    """
    This is similar to using an svg path, we can blend these systems
    later.
    char *ptr
    int_buffer[4]
    QPixmap *icon
    QPainter *painter
    QPen pen
    get_n_ints(description, int_buffer, 2)
    icon = new QPixmap(int_buffer[0], int_buffer[1])
    painter = new QPainter(icon)
    pen.setWidth(10)
    for (ptr=(char*)description; *ptr; ptr++) {
        # Other functions we can use are eraseRect, drawArc etc. https://doc.qt.io/qt-5/qpainter.html
        if (strncmp(ptr, "rect", 4)==0) {
            pen.setColor(QColor(QRgb(0x000000)))
            painter.setPen(pen)
            get_n_ints(ptr+5, int_buffer, 4)
            painter.fillRect(int_buffer[0], int_buffer[1],
                int_buffer[2], int_buffer[3], Qt::SolidPattern);

    """
    icon = ""
    return icon

def add_to_path(path, command, pos, scale):
    """
    out[10]
    for j in range(len(command)):
        if command[j] == "M":
            get_n_floats(command+j+2, out, 2)
            path.moveTo(pos[0]+out[0]*scale[0], pos[1]+out[1]*scale[1])
        elif command[j] == "L":
            get_n_floats(command+j+2, out, 2)
            path.lineTo(pos[0]+out[0]*scale[0], pos[1]+out[1]*scale[1])
        elif command[j] == "A":
            get_n_floats(command+j+2, out, 6)
            path.arcTo(pos[0]+out[0]*scale[0], pos[1]+out[1]*scale[1],
                        out[2], out[3], out[4], out[5])
        elif command[j] == "a":
            get_n_floats(command+j+2, out, 5)
            path.arcMoveTo(pos[0]+out[0]*scale[0], pos[1]+out[1]*scale[1],
                        out[2]*scale[0], out[3]*scale[1],
                        out[4])
        elif command[j] == "E":
            get_n_floats(command+j+2, out, 4)
            path.addEllipse(
                QPointF(pos[0]+out[0]*scale[0],  pos[1]+out[1]*scale[1]),
                out[2]*scale[0], out[3]*scale[1])
        elif command[j] == "Z":
            path.closeSubpath()
    """
    debug_message("add_to_path()")


def add_list_to_path(path, commands, pos, scale):
    for line in commands:
        add_to_path(path, line, pos, scale)


def toPolyline(pattern, objPos, objPath, layer, color, lineType, lineWeight):
    r"""
    NOTE: This function should be used to interpret various
    object types and save them as polylines for stitchOnly formats.
    """
    startX = objPos.x()
    startY = objPos.y()
    EmbArray* pointList = embArray_create(EMB_POINT)
    QPainterPath::Element element
    for(i = 0; i < objPath.elementCount(); ++i):
    {
        element = objPath.elementAt(i)
        EmbPointObject a
        a.point.x = element.x + startX
        a.point.y = -(element.y + startY)
        embArray_addPoint(pointList, &a)
    }
    EmbPolylineObject* polyObject
    polyObject = (EmbPolylineObject *) malloc(sizeof(EmbPolylineObject))
    polyObject.pointList = pointList
    polyObject.color = embColor_make(color.red(), color.green(), color.blue())
    polyObject.lineType = 1; #TODO: proper lineType
    embPattern_addPolylineObjectAbs(pattern, polyObject)

def app_dir(output, folder):
    r"""
    Constructs the users' folder path for keeping working drafts,
    any scripts the user writes, etc. in.

    All data required to run the program is contained in the
    site_packages folder. However this does not include, say, the
    samples folder.
    """
    separator = os.sep

    output = ''
    if os.name == 'posix':
        output = os.getenv("HOME")

        # On MacOS we set a system "HOME" manually if it is not set.
        if strlen(output)==0:
            pwd = os.getpwuid(os.getuid())
            if strlen(pwd)>0:
                output = pwd.pw_dir
            else:
                printf("ERROR: failed to set HOME.")
    else:
        output = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH")

    output += separator + ".embroidermodder2" + separator

    if folder >= 0 and folder < nFolders:
        output += folders[folder] + separator


def make_texture(output, icon, position):
    unsigned char data[128*128*3]
    # xpm-style drawing routine
    a, j, k, npalette, pixel
    npalette = strlen(palette_symbols)
    for a in range(128):
        for j in range(128):
            for k in range(npalette):
                if palette_symbols[k] == icon[1+npalette+a][j]:
                    break

            pixel = 3*(128*(127-a)+j)
            data[pixel+0] = ui_palette[3*k+0]
            data[pixel+1] = ui_palette[3*k+1]
            data[pixel+2] = ui_palette[3*k+2]

    output.width = ui_scale
    output.height = ui_scale
    output.left = position.x
    output.right = position.x+ui_scale
    output.top = position.y-ui_scale*aspect
    output.bottom = position.y
    output.texture_id = ntextures
    glBindTexture(GL_TEXTURE_2D, texture[ntextures])
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, 128, 128, 0,
        GL_RGB, GL_UNSIGNED_BYTE, data)
    ntextures++


def usage():
    puts(r"""
 ___ _____ ___  ___   __  _ ___  ___ ___   _____  __  ___  ___  ___ ___    ___ 
| __|     | _ \| _ \ /  \| |   \| __| _ \ |     |/  \|   \|   \| __| _ \  |__ \
| __| | | | _ <|   /| () | | |) | __|   / | | | | () | |) | |) | __|   /  / __/
|___|_|_|_|___/|_|\_\\__/|_|___/|___|_|\_\|_|_|_|\__/|___/|___/|___|_|\_\ |___|
 _____________________________________________________________________________ 
|                                                                             |
|                         http://embroidermodder.org                          |
|_____________________________________________________________________________|

Usage: embroidermodder [options] files ...

Options:
  -d, --debug      Print lots of debugging information.
  -h, --help       Print this message and exit.
  -v, --version    Print the version number of embroidermodder and exit.
""")
    exitApp = 1

def version():
    fprintf(stdout, "%s %s\n", _appName_, _appVer_)
    exitApp = 1

def clearSelection():

def rgb(red, green, blue):
    return blue + green*256 + blue*256*256

def load_settings():
    debug_message("Loading settings...")

    settings_fname = app_dir(0) + "settings.ini"

    # Step zero: load all of the ini file into a char buffer.
    try:
        with open(settings_fname, "rb") as f:
            settings = json.loads(f.read())

    # Sanitise data here
    settings.window_x = embClamp(0, settings.window_x, 1000)
    settings.window_y = embClamp(0, settings.window_y, 1000)


def save_settings():
    " This file needs to be read from the users home directory "
    " to ensure it is writable. "
    settings_fname = app_dir(0) + "settings.ini"
    try:
        with open(settings_fname, "rb") as f:
            f.write(json.dumps(settings))
    except:
        print("Cannot create settings file.")


def embClamp(lower, x, upper):
    x = min(upper, x)
    x = max(lower, x)
    return x

def checkBoxTipOfTheDayStateChanged(checked):
    dialog.general_tip_of_the_day = checked

def checkBoxUseOpenGLStateChanged(checked):
    dialog.display_use_opengl = checked

def checkBoxRenderHintAAStateChanged(checked):
    dialog.display_renderhint_aa = checked

def checkBoxRenderHintTextAAStateChanged(checked):
    dialog.display_renderhint_text_aa = checked

def checkBoxRenderHintSmoothPixStateChanged(checked):
    dialog.display_renderhint_smooth_pix = checked

def checkBoxRenderHintHighAAStateChanged(checked):
    dialog.display_renderhint_high_aa = checked

def checkBoxRenderHintNonCosmeticStateChanged(checked):
    dialog.display_renderhint_noncosmetic = checked

def comboBoxScrollBarWidgetCurrentIndexChanged(int index):
    dialog.display_scrollbar_widget_num = index

def spinBoxZoomScaleInValueChanged(value):
    dialog.display_zoomscale_in = value

def spinBoxZoomScaleOutValueChanged(value):
    dialog.display_zoomscale_out = value

def checkBoxDisableBGStateChanged(checked):
    dialog.printing_disable_bg = checked

def spinBoxRecentMaxFilesValueChanged(value):
    dialog.opensave_recent_max_files = value

def spinBoxTrimDstNumJumpsValueChanged(value):
    dialog.opensave_trim_dst_num_jumps = value

def checkBoxGridShowOnLoadStateChanged(checked):
    dialog.grid_show_on_load = checked

def checkBoxGridShowOriginStateChanged(checked):
    dialog.grid_show_origin = checked

def spinBoxRulerPixelSizeValueChanged(value):
    dialog.ruler_pixel_size = value

def checkBoxQSnapEndPointStateChanged(checked):
    dialog.qsnap_endpoint = checked

def checkBoxQSnapMidPointStateChanged(checked):
    dialog.qsnap_midpoint = checked

def checkBoxQSnapCenterStateChanged(checked):
    dialog.qsnap_center = checked

def checkBoxQSnapNodeStateChanged(checked):
    dialog.qsnap_node = checked

def checkBoxQSnapQuadrantStateChanged(checked):
    dialog.qsnap_quadrant = checked

def checkBoxQSnapIntersectionStateChanged(checked):
    dialog.qsnap_intersection = checked

def checkBoxQSnapExtensionStateChanged(checked):
    dialog.qsnap_extension = checked

def checkBoxQSnapInsertionStateChanged(checked):
    dialog.qsnap_insertion = checked

def checkBoxQSnapPerpendicularStateChanged(checked):
    dialog.qsnap_perpendicular = checked

def checkBoxQSnapTangentStateChanged(checked):
    dialog.qsnap_tangent = checked

def checkBoxQSnapNearestStateChanged(checked):
    dialog.qsnap_nearest = checked

def checkBoxQSnapApparentStateChanged(checked):
    dialog.qsnap_apparent = checked

def checkBoxQSnapParallelStateChanged(checked):
    dialog.qsnap_parallel = checked

def checkBoxSelectionModePickFirstStateChanged(checked):
    dialog["selection_mode_pickfirst"] = checked

def checkBoxSelectionModePickAddStateChanged(checked):
    dialog["selection_mode_pickadd"] = checked

def checkBoxSelectionModePickDragStateChanged(checked):
    dialog["selection_mode_pickdrag"] = checked

def sliderSelectionGripSizeValueChanged(value):
    dialog["selection_grip_size"] = value

def sliderSelectionPickBoxSizeValueChanged(value):
    dialog.selection_pickbox_size = value

def spinBoxGridCenterXValueChanged(value):
    dialog.grid_center.x = value

def spinBoxGridCenterYValueChanged(value):
    dialog.grid_center.y = value

def spinBoxGridSizeXValueChanged(value):
    dialog.grid_size.x = value

def spinBoxGridSizeYValueChanged(value):
    dialog.grid_size.y = value

def spinBoxGridSpacingXValueChanged(value):
    dialog.grid_spacing.x = value

def spinBoxGridSpacingYValueChanged(value):
    dialog.grid_spacing.y = value

def spinBoxGridSizeRadiusValueChanged(value):
    dialog.grid_size_radius = value

def spinBoxGridSpacingRadiusValueChanged(value):
    dialog.grid_spacing_radius = value

def spinBoxGridSpacingAngleValueChanged(value):
    dialog.grid_spacing_angle = value

def checkBoxRulerShowOnLoadStateChanged(checked):
    dialog.ruler_show_on_load = checked


class MainWindow
class BaseObject
class SelectBox
class StatusBar
class StatusBarButton
class View
class PropertyEditor
class ImageWidget

extern QStringList opensave_recent_list_of_files
extern MainWindow* _mainWin
extern QString opensave_custom_filter

QColor to_qcolor(EmbColor c)
EmbColor to_emb_color(QColor c)
QPointF to_qpointf(EmbVector c)
EmbVector to_emb_vector(QPointF c)
QIcon loadIcon(*icon)

def add_to_path(QPainterPath *path, command, pos[2], scale[2])
def add_list_to_path(QPainterPath *path, commands[], pos[2], scale[2])


class ImageWidget : public QWidget:
    Q_OBJECT

public:
    ImageWidget(const QString &filename, QWidget* parent = 0)
    ~ImageWidget()

    int load(const QString &fileName)
    int save(const QString &fileName)
    QImage img

protected:
    void paintEvent(QPaintEvent* event)
]

class MdiWindow: public QMdiSubWindow:
    Q_OBJECT

public:
    MdiWindow(const int theIndex, MainWindow* mw, QMdiArea* parent, Qt::WindowFlags wflags)
    ~MdiWindow()

    virtual QSize  sizeHint() const
    QString    getCurrentFile()   { return curFile; }
    QString    getShortCurrentFile()
    View*  getView() { return gview; }
    QGraphicsScene*    getScene() { return gscene; }
    QString    getCurrentLayer() { return curLayer; }
    unsigned int   getCurrentColor() { return curColor; }
    QString    getCurrentLineType() { return curLineType; }
    QString    getCurrentLineWeight() { return curLineWeight; }
    void   setCurrentLayer(const QString& layer) { curLayer = layer; }
    void   setCurrentColor(const unsigned int& color) { curColor = color; }
    void   setCurrentLineType(const QString& lineType) { curLineType = lineType; }
    void   setCurrentLineWeight(const QString& lineWeight) { curLineWeight = lineWeight; }
    void   designDetails()
    int   loadFile(const QString &fileName)
    int   saveFile(const QString &fileName)
signals:
    void   sendCloseMdiWin(MdiWindow*)


private:
    MainWindow*    mainWin
    QGraphicsScene*    gscene
    QMdiArea*  mdiArea
    View*  gview
    int fileWasLoaded

    # QPrinter   printer;

    QString curFile
    void setCurrentFile(const QString& fileName)
    QString fileExtension(const QString& fileName)

    int myIndex

    QString curLayer
    unsigned int curColor
    QString curLineType
    QString curLineWeight

public slots:
    void   closeEvent(QCloseEvent* e)
    void   onWindowActivated()

    void   currentLayerChanged(const QString& layer)
    void   currentColorChanged(const unsigned int& color)
    void   currentLinetypeChanged(const QString& type)
    void   currentLineweightChanged(const QString& weight)

    void   updateColorLinetypeLineweight()
    void   deletePressed()
    void   escapePressed()

    void   showViewScrollBars(int val)
    void   setViewCrossHairColor(unsigned int color)
    void   setViewBackgroundColor(unsigned int color)
    void   setViewSelectBoxColors(unsigned int colorL, unsigned int fillL, unsigned int colorR, unsigned int fillR, int alpha)
    void   setViewGridColor(unsigned int color)
    void   setViewRulerColor(unsigned int color)

    void   print()
    void   saveBMC()
]

class EmbDetailsDialog : public QDialog:
    Q_OBJECT

public:
    EmbDetailsDialog(QGraphicsScene* theScene, QWidget *parent = 0)
    ~EmbDetailsDialog()

    QWidget* mainWidget

    void getInfo()
    QWidget* createMainWidget()
    QWidget* createHistogram()

    QDialogButtonBox* buttonBox

    unsigned int stitchesTotal
    unsigned int stitchesReal
    unsigned int stitchesJump
    unsigned int stitchesTrim
    unsigned int colorTotal
    unsigned int colorChanges

    QRectF boundingRect
]

class MdiArea : public QMdiArea:
    Q_OBJECT

public:
    MdiArea(MainWindow* mw, QWidget* parent = 0)
    ~MdiArea()

    void useBackgroundLogo(use)
    void useBackgroundTexture(use)
    void useBackgroundColor(use)

    void setBackgroundLogo(const QString& fileName)
    void setBackgroundTexture(const QString& fileName)
    void setBackgroundColor(const QColor& color)

    MainWindow* mainWin

    int useLogo
    int useTexture
    int useColor

    QPixmap bgLogo
    QPixmap bgTexture
    QColor  bgColor

    void zoomExtentsAllSubWindows()
    void forceRepaint()

public slots:
    void cascade()
    void tile()
protected:
    virtual void mouseDoubleClickEvent(QMouseEvent* e)
    virtual void paintEvent(QPaintEvent* e)
]

class MainWindow: public QMainWindow:
    Q_OBJECT

public:
    MainWindow()
    ~MainWindow()

    MdiWindow*  activeMdiWindow()
    View*   activeView()
    QGraphicsScene* activeScene()

    virtual void    updateMenuToolbarStatusbar()

    MainWindow* mainWin
    MdiArea*    mdiArea
    PropertyEditor* dockPropEdit
    StatusBar*  statusbar

    QList<QGraphicsItem*> cutCopyObjectList

    QHash<int, QAction*>    actionHash
    QHash<QString, QToolBar*>   toolbarHash
    QHash<QString, QMenu*>  menuHash

    QString formatFilterOpen
    QString formatFilterSave

    QString platformString()

    QByteArray layoutState

    int numOfDocs
    int docIndex

    QList<MdiWindow*> listMdiWin
    QMdiSubWindow* findMdiWindow(const QString &fileName)
    QString openFilesPath

    QAction* myFileSeparator

    QDialog* wizardTipOfTheDay
    QLabel* labelTipOfTheDay
    QCheckBox*  checkBoxTipOfTheDay
    QStringList listTipOfTheDay

    QComboBox* layerSelector
    QComboBox* colorSelector
    QComboBox* linetypeSelector
    QComboBox* lineweightSelector
    QFontComboBox* textFontSelector
    QComboBox* textSizeSelector
    void createViewMenu()
    void createSettingsMenu()
    void createWindowMenu()
    void createHelpMenu()

    void enableMoveRapidFire()
    void disableMoveRapidFire()

    void onCloseWindow()
    virtual void    onCloseMdiWin(MdiWindow*)

    void recentMenuAboutToShow()

    void onWindowActivated (QMdiSubWindow* w)
    void windowMenuAboutToShow()
    void windowMenuActivated(int checked#int id )

    void updateAllViewScrollBars(int val)
    void updateAllViewCrossHairColors(unsigned int color)
    void updateAllViewBackgroundColors(unsigned int color)
    void updateAllViewSelectBoxColors(unsigned int colorL, unsigned int fillL, unsigned int colorR, unsigned int fillR, int alpha)
    void updateAllViewGridColors(unsigned int color)
    void updateAllViewRulerColors(unsigned int color)

    void updatePickAddMode(int val)
    void pickAddModeToggled()

    void    settingsDialog(const QString& showTab = QString())
    void    readSettings()
    void    writeSettings()

    static int    validFileFormat(const QString &fileName)

    void stub_testing()

    void fill_menu(int menu_id)
    void newFile()
    void openFile(int recent = false, const QString& recentFile = "")
    void openFilesSelected(const QStringList&)
    void openrecentfile()
    void savefile()
    void saveasfile()
    void print()
    void designDetails()
    void checkForUpdates()
    # Help Menu
    void tipOfTheDay()
    void buttonTipOfTheDayClicked(int)
    void help();
    void whatsThisContextHelp()

    void selectAll()

    void closeToolBar(QAction*)
    void floatingChangedToolBar(int)

    # Icons
    void iconResize(int iconSize)

    #Selectors
    void layerSelectorIndexChanged(int index)
    void colorSelectorIndexChanged(int index)
    void linetypeSelectorIndexChanged(int index)
    void lineweightSelectorIndexChanged(int index)
    void textFontSelectorCurrentFontChanged(const QFont& font)
    void textSizeSelectorIndexChanged(int index)

    QString textFont()

    QString getCurrentLayer()
    unsigned int getCurrentColor()
    QString getCurrentLineType()
    QString getCurrentLineWeight()

    # Standard Slots
    int isShiftPressed()
    void setShiftPressed()
    void setShiftReleased()

    void deletePressed()
    void escapePressed()

    void setTextSize(num)

    void nativeAddArc(float, float, float, float, float, float, int rubberMode)
    void nativeAddCircle(centerX, centerY, radius, int fill, int rubberMode)
    void nativeAddLine(float, float, float, float, float, int rubberMode)
    void nativeAddEllipse(centerX, centerY, width, height, rot, int fill, int rubberMode)
    void nativeAddPoint(x, y)
    void nativeAddPolygon(startX, startY, const QPainterPath& p, int rubberMode)
    void nativeAddTextSingle(const QString& str, x, y, rot, int fill, int rubberMode)
    void nativeAddPolyline(startX, startY, const QPainterPath& p, int rubberMode)
    void nativeAddRectangle(x, y, w, h, rot, int fill, int rubberMode)
    void nativeAddDimLeader(x1, y1, x2, y2, rot, int rubberMode)

    nativeCalculateAngle(x1, y1, x2, y2)
    nativeCalculateDistance(x1, y1, x2, y2)
    nativePerpendicularDistance(px, py, x1, y1, x2, y2)

    virtual void resizeEvent(QResizeEvent*)
    void closeEvent(QCloseEvent *event)
    QAction* getFileSeparator()
    void loadFormats()

public slots:
    void actions()
]

class PreviewDialog : public QFileDialog:
    Q_OBJECT

public:
    PreviewDialog(QWidget* parent = 0,
  const QString& caption = QString(),
  const QString& directory = QString(),
  const QString& filter = QString())
    ~PreviewDialog()

private:
    ImageWidget* imgWidget
]

def toPolyline(EmbPattern* pattern, const QPointF& objPos, const QPainterPath& objPath, const QString& layer, const QColor& color, const QString& lineType, const QString& lineWeight)

class PropertyEditor : public QDockWidget:
    Q_OBJECT

public:
    PropertyEditor(const QString& iconDirectory = QString(), int pickAddMode = true, QWidget* widgetToFocus = 0, QWidget* parent = 0, Qt::WindowFlags flags = Qt::Widget)
    ~PropertyEditor()

    QGroupBox* createGroupBoxGeometry(int objtype)
    QGroupBox*   createGroupBoxMiscImage()
    QGroupBox*   createGroupBoxGeneral()
    QGroupBox*   createGroupBoxMiscArc()
    QGroupBox*   createGroupBoxMiscPath()
    QGroupBox*   createGroupBoxMiscPolyline()
    QGroupBox*   createGroupBoxTextTextSingle()
    QGroupBox*   createGroupBoxMiscTextSingle()

    QWidget* focusWidget

    QString  iconDir
    int  iconSize
    Qt::ToolButtonStyle propertyEditorButtonStyle

    int pickAdd

    QList<QGraphicsItem*> selectedItemList

    #Helper functions
    QToolButton*   createToolButton(const QString& iconName, const QString& txt)
    QLineEdit* createLineEdit(const QString& validatorType = QString(), int readOnly = false)
    QComboBox* createComboBox(int disable = false)
    QFontComboBox* createFontComboBox(int disable = false)


    void updateLineEditStrIfVaries(QLineEdit* lineEdit, const QString& str)
    void updateLineEditNumIfVaries(QLineEdit* lineEdit, num, int useAnglePrecision)
    void updateFontComboBoxStrIfVaries(QFontComboBox* fontComboBox, const QString& str)
    void updateComboBoxStrIfVaries(QComboBox* comboBox, const QString& str, const QStringList& strList)
    void updateComboBoxintIfVaries(QComboBox* comboBox, int val, int yesOrNoText)

    QSignalMapper* signalMapper
    void mapSignal(QObject* fieldObj, const QString& name, QVariant value)

    QComboBox*   createComboBoxSelected()
    QToolButton* createToolButtonQSelect()
    QToolButton* createToolButtonPickAdd()

    QComboBox*   comboBoxSelected
    QToolButton* toolButtonQSelect
    QToolButton* toolButtonPickAdd

    #TODO: Alphabetic/Categorized TabWidget

protected:
    bool eventFilter(QObject *obj, QEvent *event)

signals:
    void pickAddModeToggled()

public slots:
    void setSelectedItems(QList<QGraphicsItem*> itemList)
    void updatePickAddModeButton(int pickAddMode)

private slots:
    void fieldEdited(QObject* fieldObj)
    void showGroups(int objType)
    void showOneType(int index)
    void hideAllGroups()
    void clearAllFields()
    void togglePickAddMode()
]

class SelectBox : public QRubberBand:
    Q_OBJECT

public:
    SelectBox(Shape s, QWidget* parent = 0)

    EmbColor leftBrushColor
    QColor rightBrushColor
    QColor leftPenColor
    QColor rightPenColor
    unsigned char alpha

    QBrush dirBrush
    QBrush leftBrush
    QBrush rightBrush

    QPen dirPen
    QPen leftPen
    QPen rightPen

    int boxDir

public slots:
    void setDirection(int dir)
    void setColors(const QColor& colorL, const QColor& fillL, const QColor& colorR, const QColor& fillR, int newAlpha)

protected:
    void paintEvent(QPaintEvent*)

private:
    void forceRepaint()
]

class Settings_Dialog : public QDialog:
    Q_OBJECT

public:
    Settings_Dialog(MainWindow* mw, const QString& showTab = QString(), QWidget *parent = 0)
    ~Settings_Dialog()

    MainWindow*   mainWin

    QTabWidget*   tabWidget

    QDialogButtonBox* buttonBox

    void addColorsToComboBox(QComboBox* comboBox)

    # Functions
    QWidget* createTabGeneral()
    QWidget* createTabFilesPaths()
    QWidget* createTabDisplay()
    QWidget* createTabOpenSave()
    QWidget* createTabPrinting()
    QWidget* createTabSnap()
    QWidget* createTabGridRuler()
    QWidget* createTabOrthoPolar()
    QWidget* createTabQuickSnap()
    QWidget* createTabQuickTrack()
    QWidget* createTabLineWeight()
    QWidget* createTabSelection()

private slots:
    void comboBoxLanguageCurrentIndexChanged(const QString&)
    void comboBoxIconThemeCurrentIndexChanged(const QString&)
    void comboBoxIconSizeCurrentIndexChanged(int)
    void checkBoxGeneralMdiBGUseLogoStateChanged(int)
    void chooseGeneralMdiBackgroundLogo()
    void checkBoxGeneralMdiBGUseTextureStateChanged(int)
    void chooseGeneralMdiBackgroundTexture()
    void checkBoxGeneralMdiBGUseColorStateChanged(int)
    void chooseGeneralMdiBackgroundColor()
    void currentGeneralMdiBackgroundColorChanged(const QColor&)
    void checkBoxShowScrollBarsStateChanged(int)
    void spinBoxZoomScaleInValueChanged(double)
    void spinBoxZoomScaleOutValueChanged(double)
    void checkBoxDisableBGStateChanged(int)
    void chooseDisplayCrossHairColor()
    void currentDisplayCrossHairColorChanged(const QColor&)
    void chooseDisplayBackgroundColor()
    void currentDisplayBackgroundColorChanged(const QColor&)
    void chooseDisplaySelectBoxLeftColor()
    void currentDisplaySelectBoxLeftColorChanged(const QColor&)
    void chooseDisplaySelectBoxLeftFill()
    void currentDisplaySelectBoxLeftFillChanged(const QColor&)
    void chooseDisplaySelectBoxRightColor()
    void currentDisplaySelectBoxRightColorChanged(const QColor&)
    void chooseDisplaySelectBoxRightFill()
    void currentDisplaySelectBoxRightFillChanged(const QColor&)
    void spinBoxDisplaySelectBoxAlphaValueChanged(int)
    void checkBoxCustomFilterStateChanged(int)
    void buttonCustomFilterSelectAllClicked()
    void buttonCustomFilterClearAllClicked()
    void chooseGridColor()
    void currentGridColorChanged(const QColor&)
    void checkBoxGridLoadFromFileStateChanged(int)
    void comboBoxGridTypeCurrentIndexChanged(const QString&)
    void chooseRulerColor()
    void currentRulerColorChanged(const QColor&)
    void buttonQSnapSelectAllClicked()
    void buttonQSnapClearAllClicked()
    void comboBoxQSnapLocatorColorCurrentIndexChanged(int)
    void sliderQSnapLocatorSizeValueChanged(int)
    void sliderQSnapApertureSizeValueChanged(int)
    void checkBoxLwtShowLwtStateChanged(int)
    void checkBoxLwtRealRenderStateChanged(int)
    void comboBoxSelectionCoolGripColorCurrentIndexChanged(int)
    void comboBoxSelectionHotGripColorCurrentIndexChanged(int)
    void checkBoxGridCenterOnOriginStateChanged(int)
    void comboBoxRulerMetricCurrentIndexChanged(int)
    void checkBoxGridColorMatchCrossHairStateChanged(int)

    void acceptChanges()
    void rejectChanges()

signals:
    void buttonCustomFilterSelectAll(int)
    void buttonCustomFilterClearAll(int)
    void buttonQSnapSelectAll(int)
    void buttonQSnapClearAll(int)
]

class StatusBarButton : public QToolButton:
    Q_OBJECT

public:
    StatusBarButton(QString buttonText, MainWindow* mw, StatusBar* statbar, QWidget *parent = 0)

    StatusBar*  statusbar

protected:
    void contextMenuEvent(QContextMenuEvent *event = 0)
]

class StatusBar : public QStatusBar:
    Q_OBJECT

public:
    StatusBar(MainWindow* mw, QWidget* parent = 0)

    void setMouseCoord(x, y)

]


QToolBar* toolbar[10]
QMenu* menu[10]
StatusBarButton* status_bar[8]
QToolButton* toolButton[PROPERTY_EDITORS]
QLineEdit* lineEdit[LINEEDIT_PROPERTY_EDITORS]
QComboBox* comboBox[COMBOBOX_PROPERTY_EDITORS]

QStringList opensave_recent_list_of_files
QString opensave_custom_filter

QToolButton* toolButtonTextSingleContents
QToolButton* toolButtonTextSingleFont
QToolButton* toolButtonTextSingleJustify
QToolButton* toolButtonTextSingleHeight
QToolButton* toolButtonTextSingleRotation

QLineEdit* lineEditTextSingleContents
QFontComboBox* comboBoxTextSingleFont
QComboBox* comboBoxTextSingleJustify
QLineEdit* lineEditTextSingleHeight
QLineEdit* lineEditTextSingleRotation

QToolButton* toolButtonGeneralLayer
QToolButton* toolButtonGeneralColor
QToolButton* toolButtonGeneralLineType
QToolButton* toolButtonGeneralLineWeight

QComboBox* comboBoxGeneralLayer
QComboBox* comboBoxGeneralColor
QComboBox* comboBoxGeneralLineType
QComboBox* comboBoxGeneralLineWeight

QToolButton* toolButtonImageX
QToolButton* toolButtonImageY
QToolButton* toolButtonImageWidth
QToolButton* toolButtonImageHeight

QLineEdit*   lineEditImageX
QLineEdit*   lineEditImageY
QLineEdit*   lineEditImageWidth
QLineEdit*   lineEditImageHeight

QGroupBox*   groupBoxMiscImage

QToolButton* toolButtonImageName
QToolButton* toolButtonImagePath

QLineEdit*   lineEditImageName
QLineEdit*   lineEditImagePath

QToolButton* toolButtonPolygonCenterX
QToolButton* toolButtonPolygonCenterY
QToolButton* toolButtonPolygonRadiusVertex
QToolButton* toolButtonPolygonRadiusSide
QToolButton* toolButtonPolygonDiameterVertex
QToolButton* toolButtonPolygonDiameterSide
QToolButton* toolButtonPolygonInteriorAngle

QLineEdit* lineEditPolygonCenterX
QLineEdit*   lineEditPolygonCenterY
QLineEdit*   lineEditPolygonRadiusVertex
QLineEdit*   lineEditPolygonRadiusSide
QLineEdit*   lineEditPolygonDiameterVertex
QLineEdit*   lineEditPolygonDiameterSide
QLineEdit*   lineEditPolygonInteriorAngle

EmbVector pasteDelta
QPointF scenePressPoint
QPoint pressPoint
QPointF sceneMovePoint
QPoint movePoint
QPointF sceneReleasePoint
QPoint releasePoint
QPointF sceneGripPoint

QColor rulerColor

QPoint  viewMousePoint
EmbVector sceneMousePoint
unsigned int qsnapLocatorColor
unsigned int gripColorCool
unsigned int gripColorHot
unsigned int crosshairColor
int precisionAngle
int precisionLength

QLabel* statusBarMouseCoord

QToolButton* toolButtonInfiniteLineX1
QToolButton* toolButtonInfiniteLineY1
QToolButton* toolButtonInfiniteLineX2
QToolButton* toolButtonInfiniteLineY2
QToolButton* toolButtonInfiniteLineVectorX
QToolButton* toolButtonInfiniteLineVectorY

QLineEdit*   lineEditInfiniteLineX1
QLineEdit*   lineEditInfiniteLineY1
QLineEdit*   lineEditInfiniteLineX2
QLineEdit*   lineEditInfiniteLineY2
QLineEdit*   lineEditInfiniteLineVectorX
QLineEdit*   lineEditInfiniteLineVectorY

#Used when checking if fields vary
QString fieldOldText
QString fieldNewText
QString fieldVariesText
QString fieldYesText
QString fieldNoText
QString fieldOnText
QString fieldOffText

QToolButton* toolButtonArcClockwise
QComboBox* comboBoxArcClockwise

QGroupBox* groupBoxGeometry[32]
QGroupBox* groupBoxGeneral
QGroupBox* groupBoxMiscArc
QGroupBox* groupBoxMiscPath
QGroupBox* groupBoxMiscPolyline
QGroupBox* groupBoxTextTextSingle
QGroupBox* groupBoxMiscTextSingle

QToolButton* toolButtonBlockX
QToolButton* toolButtonBlockY

QLineEdit* lineEditBlockX
QLineEdit* lineEditBlockY

QToolButton* toolButtonPathVertexNum
QToolButton* toolButtonPathVertexX
QToolButton* toolButtonPathVertexY
QToolButton* toolButtonPathArea
QToolButton* toolButtonPathLength

QComboBox*   comboBoxPathVertexNum
QLineEdit* lineEditPathVertexX
QLineEdit* lineEditPathVertexY
QLineEdit* lineEditPathArea
QLineEdit* lineEditPathLength

QToolButton* toolButtonPathClosed

QComboBox*   comboBoxPathClosed

QToolButton* toolButtonPolylineVertexNum
QToolButton* toolButtonPolylineVertexX
QToolButton* toolButtonPolylineVertexY
QToolButton* toolButtonPolylineArea
QToolButton* toolButtonPolylineLength

QComboBox*   comboBoxPolylineVertexNum
QLineEdit*   lineEditPolylineVertexX
QLineEdit*   lineEditPolylineVertexY
QLineEdit*   lineEditPolylineArea
QLineEdit*   lineEditPolylineLength

QToolButton* toolButtonPolylineClosed

QComboBox*   comboBoxPolylineClosed

QToolButton* toolButtonRayX1
QToolButton* toolButtonRayY1
QToolButton* toolButtonRayX2
QToolButton* toolButtonRayY2
QToolButton* toolButtonRayVectorX
QToolButton* toolButtonRayVectorY

QLineEdit*   lineEditRayX1
QLineEdit*   lineEditRayY1
QLineEdit*   lineEditRayX2
QLineEdit*   lineEditRayY2
QLineEdit*   lineEditRayVectorX
QLineEdit*   lineEditRayVectorY

QToolButton* toolButtonTextMultiX
QToolButton* toolButtonTextMultiY

QLineEdit*   lineEditTextMultiX
QLineEdit*   lineEditTextMultiY

QToolButton* toolButtonTextSingleX
QToolButton* toolButtonTextSingleY

QLineEdit*   lineEditTextSingleX
QLineEdit*   lineEditTextSingleY

QToolButton* toolButtonTextSingleBackward
QToolButton* toolButtonTextSingleUpsideDown

QComboBox*   comboBoxTextSingleBackward
QComboBox*   comboBoxTextSingleUpsideDown

MainWindow* _mainWin = 0


def MainWindow::readSettings():
    debug_message("Reading Settings...")

    # This file needs to be read from the users home directory to ensure it is writable.
    QPoint pos(settings.window_x, settings.window_y)
    QSize size(settings.window_width, settings.window_height)

    #
    layoutState = settings_file.value("LayoutState").toByteArray()
    if(!restoreState(layoutState)):
        debug_message("LayoutState NOT restored! Setting Default Layout...")
        //someToolBar.setVisible(1)


    load_settings()

    move(pos)
    resize(size)

def MainWindow::writeSettings():
    debug_message("Writing Settings...")

    settings.window_x = _mainWin.pos().x()
    settings.window_y = _mainWin.pos().y()
    settings.window_width = _mainWin.size().width()
    settings.window_height = _mainWin.size().height()

    save_settings()

def MainWindow::settingsDialog(const QString& showTab):
    Settings_Dialog dialog_(this, showTab, this)
    dialog_.exec()

View::View(MainWindow* mw, QGraphicsScene* theScene, QWidget* parent) : QGraphicsView(theScene, parent):
    mainWin = mw
    gscene = theScene

    setFrameShape(QFrame::NoFrame)

    # NOTE: This has to be done before setting mouse tracking.
    #TODO: Review OpenGL for Qt5 later
    #if (mainWin.settings.display_use_opengl) {
    #    debug_message("Using OpenGL...");
    #    setViewport(new QGLWidget(QGLFormat(QGL::DoubleBuffer)));
    #}

    #TODO: Review RenderHints later
    #setRenderHint(QPainter::Antialiasing, mainWin.settings.display_render_hintAA());
    #setRenderHint(QPainter::TextAntialiasing, mainWin.settings.display_render_hintTextAA());
    #setRenderHint(QPainter::SmoothPixmapTransform, mainWin.settings.display_render_hintSmoothPix());
    #setRenderHint(QPainter::HighQualityAntialiasing, mainWin.settings.display_render_hintHighAA());
    #setRenderHint(QPainter::NonCosmeticDefaultPen, mainWin.settings.display_render_hint_noncosmetic);

    # NOTE
    # ----
    # FullViewportUpdate MUST be used for both the GL and Qt renderers.
    # Qt renderer will not draw the foreground properly if it isnt set.

    setViewportUpdateMode(QGraphicsView::FullViewportUpdate)

    panDistance = 10; #TODO: should there be a setting for this???

    setCursor(Qt::BlankCursor)
    horizontalScrollBar().setCursor(Qt::ArrowCursor)
    verticalScrollBar().setCursor(Qt::ArrowCursor)
    qsnapLocatorColor = settings.qsnap_locator_color
    gripColorCool = settings.selection_coolgrip_color
    gripColorHot = settings.selection_hotgrip_color
    setCrossHairColor(settings.display_crosshair_color)
    setCrossHairSize(settings.display_crosshair_percent)
    setGridColor(settings.grid_color)

    if (settings.grid_show_on_load)
        createGrid(settings.grid_type)
    else
        createGrid("")

    toggleRuler(settings.ruler_show_on_load)
    toggleReal(1); #TODO: load this from file, else settings with default being 1

    settings.grippingActive = 0
    settings.rapidMoveActive = 0
    previewMode = PREVIEW_MODE_NULL
    previewData = 0
    previewObjectItemGroup = 0
    pasteObjectItemGroup = 0
    settings.previewActive = 0
    settings.pastingActive = 0
    settings.movingActive = 0
    settings.selectingActive = 0
    settings.zoomWindowActive = 0
    settings.panningRealTimeActive = 0
    settings.panningPointActive = 0
    settings.panningActive = 0
    settings.qSnapActive = 0
    settings.qSnapToggle = 0

    # Randomize the hot grip location initially so it's not located at (0,0).
    srand(1234)

    sceneGripPoint = QPointF((rand()%1000)*0.1, (rand()%1000)*0.1)

    gripBaseObj = 0
    tempBaseObj = 0

    selectBox = new SelectBox(QRubberBand::Rectangle, this)
    selectBox.setColors(QColor(settings.display_selectbox_left_color),
                         QColor(settings.display_selectbox_left_fill),
                         QColor(settings.display_selectbox_right_color),
                         QColor(settings.display_selectbox_right_fill),
                         settings.display_selectbox_alpha)

    showScrollBars(settings.display_show_scrollbars)
    setCornerButton()

    installEventFilter(this)

    setMouseTracking(1)
    setBackgroundColor(settings.display_bg_color)
    #TODO: wrap this with a setBackgroundPixmap() function: setBackgroundBrush(QPixmap("images/canvas));

    connect(gscene, SIGNAL(selectionChanged()), this, SLOT(selectionChanged()))

Settings_Dialog::Settings_Dialog(MainWindow* mw, const QString& showTab, QWidget* parent) : QDialog(parent):
    int i
    mainWin = mw
    setMinimumSize(750,550)

    tabWidget = new QTabWidget(this)

    #TODO: Add icons to tabs
    tabWidget.addTab(createTabGeneral(), tr("General"))
    tabWidget.addTab(createTabFilesPaths(), tr("Files/Paths"))
    tabWidget.addTab(createTabDisplay(), tr("Display"))
    tabWidget.addTab(createTabOpenSave(), tr("Open/Save"))
    tabWidget.addTab(createTabPrinting(), tr("Printing"))
    tabWidget.addTab(createTabSnap(), tr("Snap"))
    tabWidget.addTab(createTabGridRuler(), tr("Grid/Ruler"))
    tabWidget.addTab(createTabOrthoPolar(), tr("Ortho/Polar"))
    tabWidget.addTab(createTabQuickSnap(), tr("QuickSnap"))
    tabWidget.addTab(createTabQuickTrack(), tr("QuickTrack"))
    tabWidget.addTab(createTabLineWeight(), tr("LineWeight"))
    tabWidget.addTab(createTabSelection(), tr("Selection"))

    for i in range(12):
        if (showTab == settings_tab_label[i]) {
            tabWidget.setCurrentIndex(i)

    buttonBox = new QDialogButtonBox(QDialogButtonBox::Ok | QDialogButtonBox::Cancel)

    connect(buttonBox, SIGNAL(accepted()), this, SLOT(acceptChanges()))
    connect(buttonBox, SIGNAL(rejected()), this, SLOT(rejectChanges()))

    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(this)
    vboxLayoutMain.addWidget(tabWidget)
    vboxLayoutMain.addWidget(buttonBox)
    setLayout(vboxLayoutMain)

    setWindowTitle(tr("Settings"))

    QApplication::setOverrideCursor(Qt::ArrowCursor)

Settings_Dialog::~Settings_Dialog():
    QApplication::restoreOverrideCursor()

QWidget* Settings_Dialog::createTabGeneral():
    QWidget* widget = new QWidget(this)

    #Language
    QGroupBox* groupBoxLanguage = new QGroupBox(tr("Language"), widget)

    QLabel* labelLanguage = new QLabel(tr("Language (Requires Restart)"), groupBoxLanguage)
    QComboBox* comboBoxLanguage = new QComboBox(groupBoxLanguage)
    to_lower(dialog.general_language, settings.general_language)
    comboBoxLanguage.addItem("Default")
    comboBoxLanguage.addItem("System")
    comboBoxLanguage.insertSeparator(2)
    QDir trDir(qApp.applicationDirPath())
    trDir.cd("translations")
    foreach(QString dirName, trDir.entryList(QDir::Dirs | QDir::NoDotAndDotDot))
    {
        dirName[0] = dirName[0].toUpper()
        comboBoxLanguage.addItem(dirName)
    }
    QString current = dialog.general_language
    current[0] = current[0].toUpper()
    comboBoxLanguage.setCurrentIndex(comboBoxLanguage.findText(current))
    connect(comboBoxLanguage, SIGNAL(currentIndexChanged(const QString&)), this, SLOT(comboBoxLanguageCurrentIndexChanged(const QString&)))

    QVBoxLayout* vboxLayoutLanguage = new QVBoxLayout(groupBoxLanguage)
    vboxLayoutLanguage.addWidget(labelLanguage)
    vboxLayoutLanguage.addWidget(comboBoxLanguage)
    groupBoxLanguage.setLayout(vboxLayoutLanguage)

    #Icons
    QGroupBox* groupBoxIcon = new QGroupBox(tr("Icons"), widget)

    QLabel* labelIconTheme = new QLabel(tr("Icon Theme"), groupBoxIcon)
    QComboBox* comboBoxIconTheme = new QComboBox(groupBoxIcon)
    QDir dir(qApp.applicationDirPath())
    dir.cd("icons")
    strcpy(dialog.general_icon_theme, settings.general_icon_theme)
    foreach(QString dirName, dir.entryList(QDir::Dirs | QDir::NoDotAndDotDot))
    {
        comboBoxIconTheme.addItem(loadIcon(theme_xpm), dirName)
    }
    comboBoxIconTheme.setCurrentIndex(comboBoxIconTheme.findText(dialog.general_icon_theme))
    connect(comboBoxIconTheme, SIGNAL(currentIndexChanged(const QString&)), this, SLOT(comboBoxIconThemeCurrentIndexChanged(const QString&)))

    QLabel* labelIconSize = new QLabel(tr("Icon Size"), groupBoxIcon)
    QComboBox* comboBoxIconSize = new QComboBox(groupBoxIcon)
    comboBoxIconSize.addItem(loadIcon(icon16_xpm), "Very Small", 16)
    comboBoxIconSize.addItem(loadIcon(icon24_xpm), "Small", 24)
    comboBoxIconSize.addItem(loadIcon(icon32_xpm), "Medium", 32)
    comboBoxIconSize.addItem(loadIcon(icon48_xpm), "Large", 48)
    comboBoxIconSize.addItem(loadIcon(icon64_xpm), "Very Large", 64)
    comboBoxIconSize.addItem(loadIcon(icon128_xpm), "I'm Blind", 128)
    dialog.general_icon_size = settings.general_icon_size
    comboBoxIconSize.setCurrentIndex(comboBoxIconSize.findData(dialog.general_icon_size))
    connect(comboBoxIconSize, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxIconSizeCurrentIndexChanged(int)))

    QVBoxLayout* vboxLayoutIcon = new QVBoxLayout(groupBoxIcon)
    vboxLayoutIcon.addWidget(labelIconTheme)
    vboxLayoutIcon.addWidget(comboBoxIconTheme)
    vboxLayoutIcon.addWidget(labelIconSize)
    vboxLayoutIcon.addWidget(comboBoxIconSize)
    groupBoxIcon.setLayout(vboxLayoutIcon)

    #Mdi Background
    QGroupBox* groupBoxMdiBG = new QGroupBox(tr("Background"), widget)

    QCheckBox* checkBoxMdiBGUseLogo = new QCheckBox(tr("Use Logo"), groupBoxMdiBG)
    dialog.general_mdi_bg_use_logo = settings.general_mdi_bg_use_logo
    preview.general_mdi_bg_use_logo = dialog.general_mdi_bg_use_logo
    checkBoxMdiBGUseLogo.setChecked(preview.general_mdi_bg_use_logo)
    connect(checkBoxMdiBGUseLogo, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGeneralMdiBGUseLogoStateChanged(int)))

    QPushButton* buttonMdiBGLogo = new QPushButton(tr("Choose"), groupBoxMdiBG)
    buttonMdiBGLogo.setEnabled(dialog.general_mdi_bg_use_logo)
    strcpy(dialog.general_mdi_bg_logo, settings.general_mdi_bg_logo)
    strcpy(accept_.general_mdi_bg_logo, dialog.general_mdi_bg_logo)
    connect(buttonMdiBGLogo, SIGNAL(clicked()), this, SLOT(chooseGeneralMdiBackgroundLogo()))
    connect(checkBoxMdiBGUseLogo, SIGNAL(toggled(int)), buttonMdiBGLogo, SLOT(setEnabled(int)))

    QCheckBox* checkBoxMdiBGUseTexture = new QCheckBox(tr("Use Texture"), groupBoxMdiBG)
    dialog.general_mdi_bg_use_texture = settings.general_mdi_bg_use_texture
    preview.general_mdi_bg_use_texture = dialog.general_mdi_bg_use_texture
    checkBoxMdiBGUseTexture.setChecked(preview.general_mdi_bg_use_texture)
    connect(checkBoxMdiBGUseTexture, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGeneralMdiBGUseTextureStateChanged(int)))

    QPushButton* buttonMdiBGTexture = new QPushButton(tr("Choose"), groupBoxMdiBG)
    buttonMdiBGTexture.setEnabled(dialog.general_mdi_bg_use_texture)
    strcpy(dialog.general_mdi_bg_texture, settings.general_mdi_bg_texture)
    strcpy(accept_.general_mdi_bg_texture, dialog.general_mdi_bg_texture)
    connect(buttonMdiBGTexture, SIGNAL(clicked()), this, SLOT(chooseGeneralMdiBackgroundTexture()))
    connect(checkBoxMdiBGUseTexture, SIGNAL(toggled(int)), buttonMdiBGTexture, SLOT(setEnabled(int)))

    QCheckBox* checkBoxMdiBGUseColor = new QCheckBox(tr("Use Color"), groupBoxMdiBG)
    dialog.general_mdi_bg_use_color = settings.general_mdi_bg_use_color
    preview.general_mdi_bg_use_color = dialog.general_mdi_bg_use_color
    checkBoxMdiBGUseColor.setChecked(preview.general_mdi_bg_use_color)
    connect(checkBoxMdiBGUseColor, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGeneralMdiBGUseColorStateChanged(int)))

    QPushButton* buttonMdiBGColor = new QPushButton(tr("Choose"), groupBoxMdiBG)
    buttonMdiBGColor.setEnabled(dialog.general_mdi_bg_use_color)
    dialog.general_mdi_bg_color = settings.general_mdi_bg_color
    preview.general_mdi_bg_color = dialog.general_mdi_bg_color
    accept_.general_mdi_bg_color = dialog.general_mdi_bg_color
    QPixmap mdiBGPix(16,16)
    mdiBGPix.fill(QColor(preview.general_mdi_bg_color))
    buttonMdiBGColor.setIcon(QIcon(mdiBGPix))
    connect(buttonMdiBGColor, SIGNAL(clicked()), this, SLOT(chooseGeneralMdiBackgroundColor()))
    connect(checkBoxMdiBGUseColor, SIGNAL(toggled(int)), buttonMdiBGColor, SLOT(setEnabled(int)))

    QGridLayout* gridLayoutMdiBG = new QGridLayout(widget)
    gridLayoutMdiBG.addWidget(checkBoxMdiBGUseLogo, 0, 0, Qt::AlignLeft)
    gridLayoutMdiBG.addWidget(buttonMdiBGLogo, 0, 1, Qt::AlignRight)
    gridLayoutMdiBG.addWidget(checkBoxMdiBGUseTexture, 1, 0, Qt::AlignLeft)
    gridLayoutMdiBG.addWidget(buttonMdiBGTexture, 1, 1, Qt::AlignRight)
    gridLayoutMdiBG.addWidget(checkBoxMdiBGUseColor, 2, 0, Qt::AlignLeft)
    gridLayoutMdiBG.addWidget(buttonMdiBGColor, 2, 1, Qt::AlignRight)
    groupBoxMdiBG.setLayout(gridLayoutMdiBG)

    #Tips
    QGroupBox* groupBoxTips = new QGroupBox(tr("Tips"), widget)

    QCheckBox* checkBoxTipOfTheDay = new QCheckBox(tr("Show Tip of the Day on startup"), groupBoxTips)
    dialog.general_tip_of_the_day = settings.general_tip_of_the_day
    checkBoxTipOfTheDay.setChecked(dialog.general_tip_of_the_day)
    connect(checkBoxTipOfTheDay, SIGNAL(stateChanged(int)), this, SLOT(checkBoxTipOfTheDayStateChanged(int)))

    QVBoxLayout* vboxLayoutTips = new QVBoxLayout(groupBoxTips)
    vboxLayoutTips.addWidget(checkBoxTipOfTheDay)
    groupBoxTips.setLayout(vboxLayoutTips)

    #Help Browser
    QGroupBox* groupBoxHelpBrowser = new QGroupBox(tr("Help Browser"), widget)

    QRadioButton* radioButtonSystemHelpBrowser = new QRadioButton(tr("System"), groupBoxHelpBrowser)
    radioButtonSystemHelpBrowser.setChecked(settings.general_system_help_browser)
    QRadioButton* radioButtonCustomHelpBrowser = new QRadioButton(tr("Custom"), groupBoxHelpBrowser)
    radioButtonCustomHelpBrowser.setChecked(!settings.general_system_help_browser)
    radioButtonCustomHelpBrowser.setEnabled(0); #TODO: finish this

    QVBoxLayout* vboxLayoutHelpBrowser = new QVBoxLayout(groupBoxHelpBrowser)
    vboxLayoutHelpBrowser.addWidget(radioButtonSystemHelpBrowser)
    vboxLayoutHelpBrowser.addWidget(radioButtonCustomHelpBrowser)
    groupBoxHelpBrowser.setLayout(vboxLayoutHelpBrowser)

    #Widget Layout
    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(widget)
    vboxLayoutMain.addWidget(groupBoxLanguage)
    vboxLayoutMain.addWidget(groupBoxIcon)
    vboxLayoutMain.addWidget(groupBoxMdiBG)
    vboxLayoutMain.addWidget(groupBoxTips)
    vboxLayoutMain.addWidget(groupBoxHelpBrowser)
    vboxLayoutMain.addStretch(1)
    widget.setLayout(vboxLayoutMain)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea.setWidgetResizable(1)
    scrollArea.setWidget(widget)
    return scrollArea

QWidget* Settings_Dialog::createTabFilesPaths():
    QWidget* widget = new QWidget(this)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea.setWidgetResizable(1)
    scrollArea.setWidget(widget)
    return scrollArea

QWidget* Settings_Dialog::createTabDisplay():
    QWidget* widget = new QWidget(this)

    #Rendering
    #TODO: Review OpenGL and Rendering settings for future inclusion
    #
    QGroupBox* groupBoxRender = new QGroupBox(tr("Rendering"), widget)

    QCheckBox* checkBoxUseOpenGL = new QCheckBox(tr("Use OpenGL"), groupBoxRender)
    dialog.display_use_opengl = settings.display_use_open_gl
    checkBoxUseOpenGL.setChecked(dialog.display_use_opengl)
    connect(checkBoxUseOpenGL, SIGNAL(stateChanged(int)), this, SLOT(checkBoxUseOpenGLStateChanged(int)))

    QCheckBox* checkBoxRenderHintAA = new QCheckBox(tr("Antialias"), groupBoxRender)
    dialog.display_renderhint_aa = settings.display_render_hint_aa
    checkBoxRenderHintAA.setChecked(dialog.display_renderhint_aa)
    connect(checkBoxRenderHintAA, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRenderHintAAStateChanged(int)))

    QCheckBox* checkBoxRenderHintTextAA = new QCheckBox(tr("Antialias Text"), groupBoxRender)
    dialog.display_renderhint_text_aa = settings.display_render_hint_text_aa
    checkBoxRenderHintTextAA.setChecked(dialog.display_renderhint_text_aa)
    connect(checkBoxRenderHintTextAA, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRenderHintTextAAStateChanged(int)))

    QCheckBox* checkBoxRenderHintSmoothPix = new QCheckBox(tr("Smooth Pixmap"), groupBoxRender)
    dialog.display_renderhint_smooth_pix = settings.display_render_hint_smooth_pix
    checkBoxRenderHintSmoothPix.setChecked(dialog.display_renderhint_smooth_pix)
    connect(checkBoxRenderHintSmoothPix, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRenderHintSmoothPixStateChanged(int)))

    QCheckBox* checkBoxRenderHintHighAA = new QCheckBox(tr("High Quality Antialiasing (OpenGL)"), groupBoxRender)
    dialog.display_renderhint_high_aa = settings.display_render_hint_high_aa
    checkBoxRenderHintHighAA.setChecked(dialog.display_renderhint_high_aa)
    connect(checkBoxRenderHintHighAA, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRenderHintHighAAStateChanged(int)))

    QCheckBox* checkBoxRenderHintNonCosmetic = new QCheckBox(tr("Non Cosmetic"), groupBoxRender)
    dialog.display_renderhint_noncosmetic = settings.display_render_hint_non_cosmetic
    checkBoxRenderHintNonCosmetic.setChecked(dialog.display_renderhint_noncosmetic)
    connect(checkBoxRenderHintNonCosmetic, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRenderHintNonCosmeticStateChanged(int)))

    QVBoxLayout* vboxLayoutRender = new QVBoxLayout(groupBoxRender)
    vboxLayoutRender.addWidget(checkBoxUseOpenGL)
    vboxLayoutRender.addWidget(checkBoxRenderHintAA)
    vboxLayoutRender.addWidget(checkBoxRenderHintTextAA)
    vboxLayoutRender.addWidget(checkBoxRenderHintSmoothPix)
    vboxLayoutRender.addWidget(checkBoxRenderHintHighAA)
    vboxLayoutRender.addWidget(checkBoxRenderHintNonCosmetic)
    groupBoxRender.setLayout(vboxLayoutRender)


    #ScrollBars
    QGroupBox* groupBoxScrollBars = new QGroupBox(tr("ScrollBars"), widget)

    QCheckBox* checkBoxShowScrollBars = new QCheckBox(tr("Show ScrollBars"), groupBoxScrollBars)
    dialog.display_show_scrollbars = settings.display_show_scrollbars
    preview.display_show_scrollbars = dialog.display_show_scrollbars
    checkBoxShowScrollBars.setChecked(preview.display_show_scrollbars)
    connect(checkBoxShowScrollBars, SIGNAL(stateChanged(int)), this, SLOT(checkBoxShowScrollBarsStateChanged(int)))

    QLabel* labelScrollBarWidget = new QLabel(tr("Perform action when clicking corner widget"), groupBoxScrollBars)
    QComboBox* comboBoxScrollBarWidget = new QComboBox(groupBoxScrollBars)
    dialog.display_scrollbar_widget_num = settings.display_scrollbar_widget_num
    int numActions = mainWin.actionHash.size()
    for(int i = 0; i < numActions; i++)
    {
        QAction* action = mainWin.actionHash.value(i)
        if(action) comboBoxScrollBarWidget.addItem(action.icon(), action.text().replace("&", ""))
    }
    comboBoxScrollBarWidget.setCurrentIndex(dialog.display_scrollbar_widget_num)
    connect(comboBoxScrollBarWidget, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxScrollBarWidgetCurrentIndexChanged(int)))

    QVBoxLayout* vboxLayoutScrollBars = new QVBoxLayout(groupBoxScrollBars)
    vboxLayoutScrollBars.addWidget(checkBoxShowScrollBars)
    vboxLayoutScrollBars.addWidget(labelScrollBarWidget)
    vboxLayoutScrollBars.addWidget(comboBoxScrollBarWidget)
    groupBoxScrollBars.setLayout(vboxLayoutScrollBars)

    #Colors
    QGroupBox* groupBoxColor = new QGroupBox(tr("Colors"), widget)

    QLabel* labelCrossHairColor = new QLabel(tr("Crosshair Color"), groupBoxColor)
    QPushButton* buttonCrossHairColor = new QPushButton(tr("Choose"), groupBoxColor)
    dialog.display_crosshair_color = settings.display_crosshair_color
    preview.display_crosshair_color = dialog.display_crosshair_color
    accept_.display_crosshair_color = dialog.display_crosshair_color
    QPixmap crosshairPix(16,16)
    crosshairPix.fill(QColor(preview.display_crosshair_color))
    buttonCrossHairColor.setIcon(QIcon(crosshairPix))
    connect(buttonCrossHairColor, SIGNAL(clicked()), this, SLOT(chooseDisplayCrossHairColor()))

    QLabel* labelBGColor = new QLabel(tr("Background Color"), groupBoxColor)
    QPushButton* buttonBGColor = new QPushButton(tr("Choose"), groupBoxColor)
    dialog.display_bg_color = settings.display_bg_color
    preview.display_bg_color = dialog.display_bg_color
    accept_.display_bg_color = dialog.display_bg_color
    QPixmap bgPix(16,16)
    bgPix.fill(QColor(preview.display_bg_color))
    buttonBGColor.setIcon(QIcon(bgPix))
    connect(buttonBGColor, SIGNAL(clicked()), this, SLOT(chooseDisplayBackgroundColor()))

    QLabel* labelSelectBoxLeftColor = new QLabel(tr("Selection Box Color (Crossing)"), groupBoxColor)
    QPushButton* buttonSelectBoxLeftColor = new QPushButton(tr("Choose"), groupBoxColor)
    dialog.display_selectbox_left_color = settings.display_selectbox_left_color
    preview.display_selectbox_left_color = dialog.display_selectbox_left_color
    accept_.display_selectbox_left_color = dialog.display_selectbox_left_color
    QPixmap sBoxLCPix(16,16)
    sBoxLCPix.fill(QColor(preview.display_selectbox_left_color))
    buttonSelectBoxLeftColor.setIcon(QIcon(sBoxLCPix))
    connect(buttonSelectBoxLeftColor, SIGNAL(clicked()), this, SLOT(chooseDisplaySelectBoxLeftColor()))

    QLabel* labelSelectBoxLeftFill = new QLabel(tr("Selection Box Fill (Crossing)"), groupBoxColor)
    QPushButton* buttonSelectBoxLeftFill = new QPushButton(tr("Choose"), groupBoxColor)
    dialog.display_selectbox_left_fill = settings.display_selectbox_left_fill
    preview.display_selectbox_left_fill = dialog.display_selectbox_left_fill
    accept_.display_selectbox_left_fill = dialog.display_selectbox_left_fill
    QPixmap sBoxLFPix(16,16)
    sBoxLFPix.fill(QColor(preview.display_selectbox_left_fill))
    buttonSelectBoxLeftFill.setIcon(QIcon(sBoxLFPix))
    connect(buttonSelectBoxLeftFill, SIGNAL(clicked()), this, SLOT(chooseDisplaySelectBoxLeftFill()))

    QLabel* labelSelectBoxRightColor = new QLabel(tr("Selection Box Color (Window)"), groupBoxColor)
    QPushButton* buttonSelectBoxRightColor = new QPushButton(tr("Choose"), groupBoxColor)
    dialog.display_selectbox_right_color = settings.display_selectbox_right_color
    preview.display_selectbox_right_color = dialog.display_selectbox_right_color
    accept_.display_selectbox_right_color = dialog.display_selectbox_right_color
    QPixmap sBoxRCPix(16,16)
    sBoxRCPix.fill(QColor(preview.display_selectbox_right_color))
    buttonSelectBoxRightColor.setIcon(QIcon(sBoxRCPix))
    connect(buttonSelectBoxRightColor, SIGNAL(clicked()), this, SLOT(chooseDisplaySelectBoxRightColor()))

    QLabel* labelSelectBoxRightFill = new QLabel(tr("Selection Box Fill (Window)"), groupBoxColor)
    QPushButton* buttonSelectBoxRightFill = new QPushButton(tr("Choose"), groupBoxColor)
    dialog.display_selectbox_right_fill = settings.display_selectbox_right_fill
    preview.display_selectbox_right_fill = dialog.display_selectbox_right_fill
    accept_.display_selectbox_right_fill = dialog.display_selectbox_right_fill
    QPixmap sBoxRFPix(16,16)
    sBoxRFPix.fill(QColor(preview.display_selectbox_right_fill))
    buttonSelectBoxRightFill.setIcon(QIcon(sBoxRFPix))
    connect(buttonSelectBoxRightFill, SIGNAL(clicked()), this, SLOT(chooseDisplaySelectBoxRightFill()))

    QLabel* labelSelectBoxAlpha = new QLabel(tr("Selection Box Fill Alpha"), groupBoxColor)
    QSpinBox* spinBoxSelectBoxAlpha = new QSpinBox(groupBoxColor)
    spinBoxSelectBoxAlpha.setRange(0, 255)
    dialog.display_selectbox_alpha = settings.display_selectbox_alpha
    preview.display_selectbox_alpha = dialog.display_selectbox_alpha
    spinBoxSelectBoxAlpha.setValue(preview.display_selectbox_alpha)
    connect(spinBoxSelectBoxAlpha, SIGNAL(valueChanged(int)), this, SLOT(spinBoxDisplaySelectBoxAlphaValueChanged(int)))

    QGridLayout* gridLayoutColor = new QGridLayout(widget)
    gridLayoutColor.addWidget(labelCrossHairColor, 0, 0, Qt::AlignLeft)
    gridLayoutColor.addWidget(buttonCrossHairColor, 0, 1, Qt::AlignRight)
    gridLayoutColor.addWidget(labelBGColor, 1, 0, Qt::AlignLeft)
    gridLayoutColor.addWidget(buttonBGColor, 1, 1, Qt::AlignRight)
    gridLayoutColor.addWidget(labelSelectBoxLeftColor, 2, 0, Qt::AlignLeft)
    gridLayoutColor.addWidget(buttonSelectBoxLeftColor, 2, 1, Qt::AlignRight)
    gridLayoutColor.addWidget(labelSelectBoxLeftFill, 3, 0, Qt::AlignLeft)
    gridLayoutColor.addWidget(buttonSelectBoxLeftFill, 3, 1, Qt::AlignRight)
    gridLayoutColor.addWidget(labelSelectBoxRightColor, 4, 0, Qt::AlignLeft)
    gridLayoutColor.addWidget(buttonSelectBoxRightColor, 4, 1, Qt::AlignRight)
    gridLayoutColor.addWidget(labelSelectBoxRightFill, 5, 0, Qt::AlignLeft)
    gridLayoutColor.addWidget(buttonSelectBoxRightFill, 5, 1, Qt::AlignRight)
    gridLayoutColor.addWidget(labelSelectBoxAlpha, 6, 0, Qt::AlignLeft)
    gridLayoutColor.addWidget(spinBoxSelectBoxAlpha, 6, 1, Qt::AlignRight)
    groupBoxColor.setLayout(gridLayoutColor)

    #Zoom
    QGroupBox* groupBoxZoom = new QGroupBox(tr("Zoom"), widget)

    QLabel* labelZoomScaleIn = new QLabel(tr("Zoom In Scale"), groupBoxZoom)
    QDoubleSpinBox* spinBoxZoomScaleIn = new QDoubleSpinBox(groupBoxZoom)
    dialog.display_zoomscale_in = settings.display_zoomscale_in
    spinBoxZoomScaleIn.setValue(dialog.display_zoomscale_in)
    spinBoxZoomScaleIn.setSingleStep(0.01)
    spinBoxZoomScaleIn.setRange(1.01, 10.00)
    connect(spinBoxZoomScaleIn, SIGNAL(valueChanged(double)), this, SLOT(spinBoxZoomScaleInValueChanged(double)))

    QLabel* labelZoomScaleOut = new QLabel(tr("Zoom Out Scale"), groupBoxZoom)
    QDoubleSpinBox* spinBoxZoomScaleOut = new QDoubleSpinBox(groupBoxZoom)
    dialog.display_zoomscale_out = settings.display_zoomscale_out
    spinBoxZoomScaleOut.setValue(dialog.display_zoomscale_out)
    spinBoxZoomScaleOut.setSingleStep(0.01)
    spinBoxZoomScaleOut.setRange(0.01, 0.99)
    connect(spinBoxZoomScaleOut, SIGNAL(valueChanged(double)), this, SLOT(spinBoxZoomScaleOutValueChanged(double)))

    QGridLayout* gridLayoutZoom = new QGridLayout(groupBoxZoom)
    gridLayoutZoom.addWidget(labelZoomScaleIn, 0, 0, Qt::AlignLeft)
    gridLayoutZoom.addWidget(spinBoxZoomScaleIn, 0, 1, Qt::AlignRight)
    gridLayoutZoom.addWidget(labelZoomScaleOut, 1, 0, Qt::AlignLeft)
    gridLayoutZoom.addWidget(spinBoxZoomScaleOut, 1, 1, Qt::AlignRight)
    groupBoxZoom.setLayout(gridLayoutZoom)

    #Widget Layout
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget)
    #vboxLayoutMain.addWidget(groupBoxRender); //TODO: Review OpenGL and Rendering settings for future inclusion
    vboxLayoutMain.addWidget(groupBoxScrollBars)
    vboxLayoutMain.addWidget(groupBoxColor)
    vboxLayoutMain.addWidget(groupBoxZoom)
    vboxLayoutMain.addStretch(1)
    widget.setLayout(vboxLayoutMain)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea.setWidgetResizable(1)
    scrollArea.setWidget(widget)
    return scrollArea

# TODO: finish open/save options
QWidget* Settings_Dialog::createTabOpenSave():
    QWidget* widget = new QWidget(this)

    #Custom Filter
    QGroupBox* groupBoxCustomFilter = new QGroupBox(tr("Custom Filter"), widget)
    groupBoxCustomFilter.setEnabled(0); #TODO: Fixup custom filter

    QPushButton* buttonCustomFilterSelectAll = new QPushButton(tr("Select All"), groupBoxCustomFilter)
    connect(buttonCustomFilterSelectAll, SIGNAL(clicked()), this, SLOT(buttonCustomFilterSelectAllClicked()))
    QPushButton* buttonCustomFilterClearAll = new QPushButton("Clear All", groupBoxCustomFilter)
    connect(buttonCustomFilterClearAll, SIGNAL(clicked()), this, SLOT(buttonCustomFilterClearAllClicked()))
    QGridLayout* gridLayoutCustomFilter = new QGridLayout(groupBoxCustomFilter)

    int i
    for (i=0; i<numberOfFormats; i++) {
        QCheckBox* c = new QCheckBox(formatTable[i].extension, groupBoxCustomFilter)
        c.setChecked(opensave_custom_filter.contains(QString("*") + formatTable[i].extension, Qt::CaseInsensitive))
        connect(c, SIGNAL(stateChanged(int)), this, SLOT(checkBoxCustomFilterStateChanged(int)))
        connect(this, SIGNAL(buttonCustomFilterSelectAll(int)), c, SLOT(setChecked(int)))
        connect(this, SIGNAL(buttonCustomFilterClearAll(int)), c, SLOT(setChecked(int)))
        gridLayoutCustomFilter.addWidget(c, i%10, i/10, Qt::AlignLeft)
    }

    gridLayoutCustomFilter.addWidget(buttonCustomFilterSelectAll, 0, 7, Qt::AlignLeft)
    gridLayoutCustomFilter.addWidget(buttonCustomFilterClearAll, 1, 7, Qt::AlignLeft)
    gridLayoutCustomFilter.setColumnStretch(7,1)
    groupBoxCustomFilter.setLayout(gridLayoutCustomFilter)

    if(opensave_custom_filter.contains("supported", Qt::CaseInsensitive)) buttonCustomFilterSelectAllClicked()

    # Opening
    QGroupBox* groupBoxOpening = new QGroupBox(tr("File Open"), widget)

    QComboBox* comboBoxOpenFormat = new QComboBox(groupBoxOpening)

    QCheckBox* checkBoxOpenThumbnail = new QCheckBox(tr("Preview Thumbnails"), groupBoxOpening)
    checkBoxOpenThumbnail.setChecked(0)

    # TODO: Add a button to clear the recent history.

    QLabel* labelRecentMaxFiles = new QLabel(tr("Number of recently accessed files to show"), groupBoxOpening)
    QSpinBox* spinBoxRecentMaxFiles = new QSpinBox(groupBoxOpening)
    spinBoxRecentMaxFiles.setRange(0, 10)
    dialog.opensave_recent_max_files = settings.opensave_recent_max_files
    spinBoxRecentMaxFiles.setValue(dialog.opensave_recent_max_files)
    connect(spinBoxRecentMaxFiles, SIGNAL(valueChanged(int)), this, SLOT(spinBoxRecentMaxFilesValueChanged(int)))

    QFrame* frameRecent = new QFrame(groupBoxOpening)
    QGridLayout* gridLayoutRecent = new QGridLayout(frameRecent)
    gridLayoutRecent.addWidget(labelRecentMaxFiles, 0, 0, Qt::AlignLeft)
    gridLayoutRecent.addWidget(spinBoxRecentMaxFiles, 0, 1, Qt::AlignRight)
    frameRecent.setLayout(gridLayoutRecent)

    QVBoxLayout* vboxLayoutOpening = new QVBoxLayout(groupBoxOpening)
    vboxLayoutOpening.addWidget(comboBoxOpenFormat)
    vboxLayoutOpening.addWidget(checkBoxOpenThumbnail)
    vboxLayoutOpening.addWidget(frameRecent)
    groupBoxOpening.setLayout(vboxLayoutOpening)

    #Saving
    QGroupBox* groupBoxSaving = new QGroupBox(tr("File Save"), widget)

    QComboBox* comboBoxSaveFormat = new QComboBox(groupBoxSaving)

    QCheckBox* checkBoxSaveThumbnail = new QCheckBox(tr("Save Thumbnails"), groupBoxSaving)
    checkBoxSaveThumbnail.setChecked(0)

    QCheckBox* checkBoxAutoSave = new QCheckBox(tr("AutoSave"), groupBoxSaving)
    checkBoxAutoSave.setChecked(0)

    QVBoxLayout* vboxLayoutSaving = new QVBoxLayout(groupBoxSaving)
    vboxLayoutSaving.addWidget(comboBoxSaveFormat)
    vboxLayoutSaving.addWidget(checkBoxSaveThumbnail)
    vboxLayoutSaving.addWidget(checkBoxAutoSave)
    groupBoxSaving.setLayout(vboxLayoutSaving)

    #Trimming
    QGroupBox* groupBoxTrim = new QGroupBox(tr("Trimming"), widget)

    QLabel* labelTrimDstNumJumps = new QLabel(tr("DST Only: Minimum number of jumps to trim"), groupBoxTrim)
    QSpinBox* spinBoxTrimDstNumJumps = new QSpinBox(groupBoxTrim)
    spinBoxTrimDstNumJumps.setRange(1, 20)
    dialog.opensave_trim_dst_num_jumps = settings.opensave_trim_dst_num_jumps
    spinBoxTrimDstNumJumps.setValue(dialog.opensave_trim_dst_num_jumps)
    connect(spinBoxTrimDstNumJumps, SIGNAL(valueChanged(int)), this, SLOT(spinBoxTrimDstNumJumpsValueChanged(int)))

    QFrame* frameTrimDstNumJumps = new QFrame(groupBoxTrim)
    QGridLayout* gridLayoutTrimDstNumJumps = new QGridLayout(frameTrimDstNumJumps)
    gridLayoutTrimDstNumJumps.addWidget(labelTrimDstNumJumps, 0, 0, Qt::AlignLeft)
    gridLayoutTrimDstNumJumps.addWidget(spinBoxTrimDstNumJumps, 0, 1, Qt::AlignRight)
    frameTrimDstNumJumps.setLayout(gridLayoutTrimDstNumJumps)

    QVBoxLayout* vboxLayoutTrim = new QVBoxLayout(groupBoxTrim)
    vboxLayoutTrim.addWidget(frameTrimDstNumJumps)
    groupBoxTrim.setLayout(vboxLayoutTrim)

    #Widget Layout
    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(widget)
    vboxLayoutMain.addWidget(groupBoxCustomFilter)
    vboxLayoutMain.addWidget(groupBoxOpening)
    vboxLayoutMain.addWidget(groupBoxSaving)
    vboxLayoutMain.addWidget(groupBoxTrim)
    vboxLayoutMain.addStretch(1)
    widget.setLayout(vboxLayoutMain)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea.setWidgetResizable(1)
    scrollArea.setWidget(widget)
    return scrollArea

QWidget* Settings_Dialog::createTabPrinting():
    #
    QWidget* widget = new QWidget(this)

    //Default Printer
    QGroupBox* groupBoxDefaultPrinter = new QGroupBox(tr("Default Printer"), widget)

    QRadioButton* radioButtonUseSame = new QRadioButton(tr("Use as default device"), groupBoxDefaultPrinter)
    radioButtonUseSame.setChecked(!settings.printing_use_last_device)
    QRadioButton* radioButtonUseLast = new QRadioButton(tr("Use last used device"), groupBoxDefaultPrinter)
    radioButtonUseLast.setChecked(settings.printing_use_last_device)

    QComboBox* comboBoxDefaultDevice = new QComboBox(groupBoxDefaultPrinter)
    QList<QPrinterInfo> listAvailPrinters = QPrinterInfo::availablePrinters()
    foreach(QPrinterInfo info, listAvailPrinters)
    {
        comboBoxDefaultDevice.addItem(loadIcon(print_xpm), info.printerName())
    }

    QVBoxLayout* vboxLayoutDefaultPrinter = new QVBoxLayout(groupBoxDefaultPrinter)
    vboxLayoutDefaultPrinter.addWidget(radioButtonUseSame)
    vboxLayoutDefaultPrinter.addWidget(comboBoxDefaultDevice)
    vboxLayoutDefaultPrinter.addWidget(radioButtonUseLast)
    groupBoxDefaultPrinter.setLayout(vboxLayoutDefaultPrinter)

    //Save Ink
    QGroupBox* groupBoxSaveInk = new QGroupBox(tr("Save Ink"), widget)

    QCheckBox* checkBoxDisableBG = new QCheckBox(tr("Disable Background"), groupBoxSaveInk)
    dialog.printing_disable_bg = settings.printing_disable_bg
    checkBoxDisableBG.setChecked(dialog.printing_disable_bg)
    connect(checkBoxDisableBG, SIGNAL(stateChanged(int)), this, SLOT(checkBoxDisableBGStateChanged(int)))

    QVBoxLayout* vboxLayoutSaveInk = new QVBoxLayout(groupBoxSaveInk)
    vboxLayoutSaveInk.addWidget(checkBoxDisableBG)
    groupBoxSaveInk.setLayout(vboxLayoutSaveInk)

    //Widget Layout
    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(widget)
    vboxLayoutMain.addWidget(groupBoxDefaultPrinter)
    vboxLayoutMain.addWidget(groupBoxSaveInk)
    vboxLayoutMain.addStretch(1)
    widget.setLayout(vboxLayoutMain)


    QScrollArea* scrollArea = new QScrollArea(this)
    #scrollArea.setWidgetResizable(1)
    scrollArea.setWidget(widget);
    return scrollArea

QWidget* Settings_Dialog::createTabSnap():
    QWidget* widget = new QWidget(this)

    #TODO: finish this

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea.setWidgetResizable(1)
    scrollArea.setWidget(widget)
    return scrollArea

QWidget* Settings_Dialog::createTabGridRuler():
    QWidget* widget = new QWidget(this)

    #Grid Misc
    QGroupBox* groupBoxGridMisc = new QGroupBox(tr("Grid Misc"), widget)

    QCheckBox* checkBoxGridShowOnLoad = new QCheckBox(tr("Initially show grid when loading a file"), groupBoxGridMisc)
    dialog.grid_show_on_load = settings.grid_show_on_load
    checkBoxGridShowOnLoad.setChecked(dialog.grid_show_on_load)
    connect(checkBoxGridShowOnLoad, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGridShowOnLoadStateChanged(int)))

    QCheckBox* checkBoxGridShowOrigin = new QCheckBox(tr("Show the origin when the grid is enabled"), groupBoxGridMisc)
    dialog.grid_show_origin = settings.grid_show_origin
    checkBoxGridShowOrigin.setChecked(dialog.grid_show_origin)
    connect(checkBoxGridShowOrigin, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGridShowOriginStateChanged(int)))

    QGridLayout* gridLayoutGridMisc = new QGridLayout(widget)
    gridLayoutGridMisc.addWidget(checkBoxGridShowOnLoad, 0, 0, Qt::AlignLeft)
    gridLayoutGridMisc.addWidget(checkBoxGridShowOrigin, 1, 0, Qt::AlignLeft)
    groupBoxGridMisc.setLayout(gridLayoutGridMisc)

    #Grid Color
    QGroupBox* groupBoxGridColor = new QGroupBox(tr("Grid Color"), widget)

    QCheckBox* checkBoxGridColorMatchCrossHair = new QCheckBox(tr("Match grid color to crosshair color"), groupBoxGridColor)
    dialog.grid_color_match_crosshair = settings.grid_color_match_crosshair
    checkBoxGridColorMatchCrossHair.setChecked(dialog.grid_color_match_crosshair)
    connect(checkBoxGridColorMatchCrossHair, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGridColorMatchCrossHairStateChanged(int)))

    QLabel* labelGridColor = new QLabel(tr("Grid Color"), groupBoxGridColor)
    labelGridColor.setObjectName("labelGridColor")
    QPushButton* buttonGridColor = new QPushButton(tr("Choose"), groupBoxGridColor)
    buttonGridColor.setObjectName("buttonGridColor")
    if(dialog.grid_color_match_crosshair) { dialog.grid_color = settings.display_crosshair_color; }
    else                                  { dialog.grid_color = settings.grid_color;             }
    preview.grid_color = dialog.grid_color
    accept_.grid_color = dialog.grid_color
    QPixmap gridPix(16,16)
    gridPix.fill(QColor(preview.grid_color))
    buttonGridColor.setIcon(QIcon(gridPix))
    connect(buttonGridColor, SIGNAL(clicked()), this, SLOT(chooseGridColor()))

    labelGridColor.setEnabled(!dialog.grid_color_match_crosshair)
    buttonGridColor.setEnabled(!dialog.grid_color_match_crosshair)

    QGridLayout* gridLayoutGridColor = new QGridLayout(widget)
    gridLayoutGridColor.addWidget(checkBoxGridColorMatchCrossHair, 0, 0, Qt::AlignLeft)
    gridLayoutGridColor.addWidget(labelGridColor, 1, 0, Qt::AlignLeft)
    gridLayoutGridColor.addWidget(buttonGridColor, 1, 1, Qt::AlignRight)
    groupBoxGridColor.setLayout(gridLayoutGridColor)

    #Grid Geometry
    QGroupBox* groupBoxGridGeom = new QGroupBox(tr("Grid Geometry"), widget)

    QCheckBox* checkBoxGridLoadFromFile = new QCheckBox(tr("Set grid size from opened file"), groupBoxGridGeom)
    dialog.grid_load_from_file = settings.grid_load_from_file
    checkBoxGridLoadFromFile.setChecked(dialog.grid_load_from_file)
    connect(checkBoxGridLoadFromFile, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGridLoadFromFileStateChanged(int)))

    QLabel* labelGridType = new QLabel(tr("Grid Type"), groupBoxGridGeom)
    labelGridType.setObjectName("labelGridType")
    QComboBox* comboBoxGridType = new QComboBox(groupBoxGridGeom)
    comboBoxGridType.setObjectName("comboBoxGridType")
    comboBoxGridType.addItem("Rectangular")
    comboBoxGridType.addItem("Circular")
    comboBoxGridType.addItem("Isometric")
    strcpy(dialog.grid_type, settings.grid_type)
    comboBoxGridType.setCurrentIndex(comboBoxGridType.findText(dialog.grid_type))
    connect(comboBoxGridType, SIGNAL(currentIndexChanged(const QString&)), this, SLOT(comboBoxGridTypeCurrentIndexChanged(const QString&)))

    QCheckBox* checkBoxGridCenterOnOrigin = new QCheckBox(tr("Center the grid on the origin"), groupBoxGridGeom)
    checkBoxGridCenterOnOrigin.setObjectName("checkBoxGridCenterOnOrigin")
    dialog.grid_center_on_origin = settings.grid_center_on_origin
    checkBoxGridCenterOnOrigin.setChecked(dialog.grid_center_on_origin)
    connect(checkBoxGridCenterOnOrigin, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGridCenterOnOriginStateChanged(int)))

    QLabel* labelGridCenterX = new QLabel(tr("Grid Center X"), groupBoxGridGeom)
    labelGridCenterX.setObjectName("labelGridCenterX")
    QDoubleSpinBox* spinBoxGridCenterX = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridCenterX.setObjectName("spinBoxGridCenterX")
    dialog.grid_center.x = settings.grid_center.x
    spinBoxGridCenterX.setSingleStep(1.000)
    spinBoxGridCenterX.setRange(-1000.000, 1000.000)
    spinBoxGridCenterX.setValue(dialog.grid_center.x)
    connect(spinBoxGridCenterX, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridCenterXValueChanged(double)))

    QLabel* labelGridCenterY = new QLabel(tr("Grid Center Y"), groupBoxGridGeom)
    labelGridCenterY.setObjectName("labelGridCenterY")
    QDoubleSpinBox* spinBoxGridCenterY = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridCenterY.setObjectName("spinBoxGridCenterY")
    dialog.grid_center.y = settings.grid_center.y
    spinBoxGridCenterY.setSingleStep(1.000)
    spinBoxGridCenterY.setRange(-1000.000, 1000.000)
    spinBoxGridCenterY.setValue(dialog.grid_center.y)
    connect(spinBoxGridCenterY, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridCenterYValueChanged(double)))

    QLabel* labelGridSizeX = new QLabel(tr("Grid Size X"), groupBoxGridGeom)
    labelGridSizeX.setObjectName("labelGridSizeX")
    QDoubleSpinBox* spinBoxGridSizeX = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridSizeX.setObjectName("spinBoxGridSizeX")
    dialog.grid_size.x = settings.grid_size.x
    spinBoxGridSizeX.setSingleStep(1.000)
    spinBoxGridSizeX.setRange(1.000, 1000.000)
    spinBoxGridSizeX.setValue(dialog.grid_size.x)
    connect(spinBoxGridSizeX, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSizeXValueChanged(double)))

    QLabel* labelGridSizeY = new QLabel(tr("Grid Size Y"), groupBoxGridGeom)
    labelGridSizeY.setObjectName("labelGridSizeY")
    QDoubleSpinBox* spinBoxGridSizeY = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridSizeY.setObjectName("spinBoxGridSizeY")
    dialog.grid_size.y = settings.grid_size.y
    spinBoxGridSizeY.setSingleStep(1.000)
    spinBoxGridSizeY.setRange(1.000, 1000.000)
    spinBoxGridSizeY.setValue(dialog.grid_size.y)
    connect(spinBoxGridSizeY, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSizeYValueChanged(double)))

    QLabel* labelGridSpacingX = new QLabel(tr("Grid Spacing X"), groupBoxGridGeom)
    labelGridSpacingX.setObjectName("labelGridSpacingX")
    QDoubleSpinBox* spinBoxGridSpacingX = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridSpacingX.setObjectName("spinBoxGridSpacingX")
    dialog.grid_spacing.x = settings.grid_spacing.x
    spinBoxGridSpacingX.setSingleStep(1.000)
    spinBoxGridSpacingX.setRange(0.001, 1000.000)
    spinBoxGridSpacingX.setValue(dialog.grid_spacing.x)
    connect(spinBoxGridSpacingX, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSpacingXValueChanged(double)))

    QLabel* labelGridSpacingY = new QLabel(tr("Grid Spacing Y"), groupBoxGridGeom)
    labelGridSpacingY.setObjectName("labelGridSpacingY")
    QDoubleSpinBox* spinBoxGridSpacingY = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridSpacingY.setObjectName("spinBoxGridSpacingY")
    dialog.grid_spacing.y = settings.grid_spacing.y
    spinBoxGridSpacingY.setSingleStep(1.000)
    spinBoxGridSpacingY.setRange(0.001, 1000.000)
    spinBoxGridSpacingY.setValue(dialog.grid_spacing.y)
    connect(spinBoxGridSpacingY, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSpacingYValueChanged(double)))

    QLabel* labelGridSizeRadius = new QLabel(tr("Grid Size Radius"), groupBoxGridGeom)
    labelGridSizeRadius.setObjectName("labelGridSizeRadius")
    QDoubleSpinBox* spinBoxGridSizeRadius = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridSizeRadius.setObjectName("spinBoxGridSizeRadius")
    dialog.grid_size_radius = settings.grid_size_radius
    spinBoxGridSizeRadius.setSingleStep(1.000)
    spinBoxGridSizeRadius.setRange(1.000, 1000.000)
    spinBoxGridSizeRadius.setValue(dialog.grid_size_radius)
    connect(spinBoxGridSizeRadius, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSizeRadiusValueChanged(double)))

    QLabel* labelGridSpacingRadius = new QLabel(tr("Grid Spacing Radius"), groupBoxGridGeom)
    labelGridSpacingRadius.setObjectName("labelGridSpacingRadius")
    QDoubleSpinBox* spinBoxGridSpacingRadius = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridSpacingRadius.setObjectName("spinBoxGridSpacingRadius")
    dialog.grid_spacing_radius = settings.grid_spacing_radius
    spinBoxGridSpacingRadius.setSingleStep(1.000)
    spinBoxGridSpacingRadius.setRange(0.001, 1000.000)
    spinBoxGridSpacingRadius.setValue(dialog.grid_spacing_radius)
    connect(spinBoxGridSpacingRadius, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSpacingRadiusValueChanged(double)))

    QLabel* labelGridSpacingAngle = new QLabel(tr("Grid Spacing Angle"), groupBoxGridGeom)
    labelGridSpacingAngle.setObjectName("labelGridSpacingAngle")
    QDoubleSpinBox* spinBoxGridSpacingAngle = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridSpacingAngle.setObjectName("spinBoxGridSpacingAngle")
    dialog.grid_spacing_angle = settings.grid_spacing_angle
    spinBoxGridSpacingAngle.setSingleStep(1.000)
    spinBoxGridSpacingAngle.setRange(0.001, 1000.000)
    spinBoxGridSpacingAngle.setValue(dialog.grid_spacing_angle)
    connect(spinBoxGridSpacingAngle, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSpacingAngleValueChanged(double)))

    labelGridType.setEnabled(!dialog.grid_load_from_file)
    comboBoxGridType.setEnabled(!dialog.grid_load_from_file)
    checkBoxGridCenterOnOrigin.setEnabled(!dialog.grid_load_from_file)
    labelGridCenterX.setEnabled(!dialog.grid_load_from_file)
    spinBoxGridCenterX.setEnabled(!dialog.grid_load_from_file)
    labelGridCenterY.setEnabled(!dialog.grid_load_from_file)
    spinBoxGridCenterY.setEnabled(!dialog.grid_load_from_file)
    labelGridSizeX.setEnabled(!dialog.grid_load_from_file)
    spinBoxGridSizeX.setEnabled(!dialog.grid_load_from_file)
    labelGridSizeY.setEnabled(!dialog.grid_load_from_file)
    spinBoxGridSizeY.setEnabled(!dialog.grid_load_from_file)
    labelGridSpacingX.setEnabled(!dialog.grid_load_from_file)
    spinBoxGridSpacingX.setEnabled(!dialog.grid_load_from_file)
    labelGridSpacingY.setEnabled(!dialog.grid_load_from_file)
    spinBoxGridSpacingY.setEnabled(!dialog.grid_load_from_file)
    labelGridSizeRadius.setEnabled(!dialog.grid_load_from_file)
    spinBoxGridSizeRadius.setEnabled(!dialog.grid_load_from_file)
    labelGridSpacingRadius.setEnabled(!dialog.grid_load_from_file)
    spinBoxGridSpacingRadius.setEnabled(!dialog.grid_load_from_file)
    labelGridSpacingAngle.setEnabled(!dialog.grid_load_from_file)
    spinBoxGridSpacingAngle.setEnabled(!dialog.grid_load_from_file)

    int visibility = 0
    if(dialog.grid_type == "Circular") visibility = 1
    labelGridSizeX.setVisible(!visibility)
    spinBoxGridSizeX.setVisible(!visibility)
    labelGridSizeY.setVisible(!visibility)
    spinBoxGridSizeY.setVisible(!visibility)
    labelGridSpacingX.setVisible(!visibility)
    spinBoxGridSpacingX.setVisible(!visibility)
    labelGridSpacingY.setVisible(!visibility)
    spinBoxGridSpacingY.setVisible(!visibility)
    labelGridSizeRadius.setVisible(visibility)
    spinBoxGridSizeRadius.setVisible(visibility)
    labelGridSpacingRadius.setVisible(visibility)
    spinBoxGridSpacingRadius.setVisible(visibility)
    labelGridSpacingAngle.setVisible(visibility)
    spinBoxGridSpacingAngle.setVisible(visibility)

    QGridLayout* gridLayoutGridGeom = new QGridLayout(groupBoxGridGeom)
    gridLayoutGridGeom.addWidget(checkBoxGridLoadFromFile, 0, 0, Qt::AlignLeft)
    gridLayoutGridGeom.addWidget(labelGridType, 1, 0, Qt::AlignLeft)
    gridLayoutGridGeom.addWidget(comboBoxGridType, 1, 1, Qt::AlignRight)
    gridLayoutGridGeom.addWidget(checkBoxGridCenterOnOrigin, 2, 0, Qt::AlignLeft)
    gridLayoutGridGeom.addWidget(labelGridCenterX, 3, 0, Qt::AlignLeft)
    gridLayoutGridGeom.addWidget(spinBoxGridCenterX, 3, 1, Qt::AlignRight)
    gridLayoutGridGeom.addWidget(labelGridCenterY, 4, 0, Qt::AlignLeft)
    gridLayoutGridGeom.addWidget(spinBoxGridCenterY, 4, 1, Qt::AlignRight)
    gridLayoutGridGeom.addWidget(labelGridSizeX, 5, 0, Qt::AlignLeft)
    gridLayoutGridGeom.addWidget(spinBoxGridSizeX, 5, 1, Qt::AlignRight)
    gridLayoutGridGeom.addWidget(labelGridSizeY, 6, 0, Qt::AlignLeft)
    gridLayoutGridGeom.addWidget(spinBoxGridSizeY, 6, 1, Qt::AlignRight)
    gridLayoutGridGeom.addWidget(labelGridSpacingX, 7, 0, Qt::AlignLeft)
    gridLayoutGridGeom.addWidget(spinBoxGridSpacingX, 7, 1, Qt::AlignRight)
    gridLayoutGridGeom.addWidget(labelGridSpacingY, 8, 0, Qt::AlignLeft)
    gridLayoutGridGeom.addWidget(spinBoxGridSpacingY, 8, 1, Qt::AlignRight)
    gridLayoutGridGeom.addWidget(labelGridSizeRadius, 9, 0, Qt::AlignLeft)
    gridLayoutGridGeom.addWidget(spinBoxGridSizeRadius, 9, 1, Qt::AlignRight)
    gridLayoutGridGeom.addWidget(labelGridSpacingRadius, 10, 0, Qt::AlignLeft)
    gridLayoutGridGeom.addWidget(spinBoxGridSpacingRadius, 10, 1, Qt::AlignRight)
    gridLayoutGridGeom.addWidget(labelGridSpacingAngle, 11, 0, Qt::AlignLeft)
    gridLayoutGridGeom.addWidget(spinBoxGridSpacingAngle, 11, 1, Qt::AlignRight)
    groupBoxGridGeom.setLayout(gridLayoutGridGeom)

    #Ruler Misc
    QGroupBox* groupBoxRulerMisc = new QGroupBox(tr("Ruler Misc"), widget)

    QCheckBox* checkBoxRulerShowOnLoad = new QCheckBox(tr("Initially show ruler when loading a file"), groupBoxRulerMisc)
    dialog.ruler_show_on_load = settings.ruler_show_on_load
    checkBoxRulerShowOnLoad.setChecked(dialog.ruler_show_on_load)
    connect(checkBoxRulerShowOnLoad, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRulerShowOnLoadStateChanged(int)))

    QLabel* labelRulerMetric = new QLabel(tr("Ruler Units"), groupBoxRulerMisc)
    QComboBox* comboBoxRulerMetric = new QComboBox(groupBoxRulerMisc)
    comboBoxRulerMetric.addItem("Imperial", 0)
    comboBoxRulerMetric.addItem("Metric", 1)
    dialog.ruler_metric = settings.ruler_metric
    comboBoxRulerMetric.setCurrentIndex(comboBoxRulerMetric.findData(dialog.ruler_metric))
    connect(comboBoxRulerMetric, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxRulerMetricCurrentIndexChanged(int)))

    QGridLayout* gridLayoutRulerMisc = new QGridLayout(widget)
    gridLayoutRulerMisc.addWidget(checkBoxRulerShowOnLoad, 0, 0, Qt::AlignLeft)
    gridLayoutRulerMisc.addWidget(labelRulerMetric, 1, 0, Qt::AlignLeft)
    gridLayoutRulerMisc.addWidget(comboBoxRulerMetric, 1, 1, Qt::AlignRight)
    groupBoxRulerMisc.setLayout(gridLayoutRulerMisc)

    #Ruler Color
    QGroupBox* groupBoxRulerColor = new QGroupBox(tr("Ruler Color"), widget)

    QLabel* labelRulerColor = new QLabel(tr("Ruler Color"), groupBoxRulerColor)
    labelRulerColor.setObjectName("labelRulerColor")
    QPushButton* buttonRulerColor = new QPushButton(tr("Choose"), groupBoxRulerColor)
    buttonRulerColor.setObjectName("buttonRulerColor")
    dialog.ruler_color = settings.ruler_color
    preview.ruler_color = dialog.ruler_color
    accept_.ruler_color = dialog.ruler_color
    QPixmap rulerPix(16,16)
    rulerPix.fill(QColor(preview.ruler_color))
    buttonRulerColor.setIcon(QIcon(rulerPix))
    connect(buttonRulerColor, SIGNAL(clicked()), this, SLOT(chooseRulerColor()))

    QGridLayout* gridLayoutRulerColor = new QGridLayout(widget)
    gridLayoutRulerColor.addWidget(labelRulerColor, 1, 0, Qt::AlignLeft)
    gridLayoutRulerColor.addWidget(buttonRulerColor, 1, 1, Qt::AlignRight)
    groupBoxRulerColor.setLayout(gridLayoutRulerColor)

    #Ruler Geometry
    QGroupBox* groupBoxRulerGeom = new QGroupBox(tr("Ruler Geometry"), widget)

    QLabel* labelRulerPixelSize = new QLabel(tr("Ruler Pixel Size"), groupBoxRulerGeom)
    labelRulerPixelSize.setObjectName("labelRulerPixelSize")
    QDoubleSpinBox* spinBoxRulerPixelSize = new QDoubleSpinBox(groupBoxRulerGeom)
    spinBoxRulerPixelSize.setObjectName("spinBoxRulerPixelSize")
    dialog.ruler_pixel_size = settings.ruler_pixel_size
    spinBoxRulerPixelSize.setSingleStep(1.000)
    spinBoxRulerPixelSize.setRange(20.000, 100.000)
    spinBoxRulerPixelSize.setValue(dialog.ruler_pixel_size)
    connect(spinBoxRulerPixelSize, SIGNAL(valueChanged(double)), this, SLOT(spinBoxRulerPixelSizeValueChanged(double)))

    QGridLayout* gridLayoutRulerGeom = new QGridLayout(groupBoxRulerGeom)
    gridLayoutRulerGeom.addWidget(labelRulerPixelSize, 0, 0, Qt::AlignLeft)
    gridLayoutRulerGeom.addWidget(spinBoxRulerPixelSize, 0, 1, Qt::AlignRight)
    groupBoxRulerGeom.setLayout(gridLayoutRulerGeom)

    #Widget Layout
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget)
    vboxLayoutMain.addWidget(groupBoxGridMisc)
    vboxLayoutMain.addWidget(groupBoxGridColor)
    vboxLayoutMain.addWidget(groupBoxGridGeom)
    vboxLayoutMain.addWidget(groupBoxRulerMisc)
    vboxLayoutMain.addWidget(groupBoxRulerColor)
    vboxLayoutMain.addWidget(groupBoxRulerGeom)
    vboxLayoutMain.addStretch(1)
    widget.setLayout(vboxLayoutMain)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea.setWidgetResizable(1)
    scrollArea.setWidget(widget)
    return scrollArea

QWidget* Settings_Dialog::createTabOrthoPolar():
    QWidget* widget = new QWidget(this)

    #TODO: finish this

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea.setWidgetResizable(1)
    scrollArea.setWidget(widget)
    return scrollArea

#define make_check_box(label, checked, icon, f, x, y) \
    { \
        QCheckBox* c = new QCheckBox(tr(label), groupBoxQSnapLoc); \
        c.setChecked(settings.checked); \
        c.setIcon(loadIcon(icon)); \
        connect(c, SIGNAL(stateChanged(int)), this, SLOT(f(int))); \
        connect(this, SIGNAL(buttonQSnapSelectAll(int)), c, SLOT(setChecked(int))); \
        connect(this, SIGNAL(buttonQSnapClearAll(int)), c, SLOT(setChecked(int))); \
        gridLayoutQSnap.addWidget(c, x, y, Qt::AlignLeft); \
        dialog.checked = settings.checked; \
    }

QWidget* Settings_Dialog::createTabQuickSnap():
    QWidget* widget = new QWidget(this)

    #QSnap Locators
    QGroupBox* groupBoxQSnapLoc = new QGroupBox(tr("Locators Used"), widget)
    QPushButton* buttonQSnapSelectAll = new QPushButton(tr("Select All"), groupBoxQSnapLoc)
    QPushButton* buttonQSnapClearAll = new QPushButton(tr("Clear All"), groupBoxQSnapLoc)
    QGridLayout* gridLayoutQSnap = new QGridLayout(groupBoxQSnapLoc)

    connect(buttonQSnapSelectAll, SIGNAL(clicked()), this, SLOT(buttonQSnapSelectAllClicked()))
    connect(buttonQSnapClearAll, SIGNAL(clicked()), this, SLOT(buttonQSnapClearAllClicked()))

    make_check_box("Endpoint", qsnap_endpoint, locator_snaptoendpoint_xpm, checkBoxQSnapEndPointStateChanged, 0, 0)
    make_check_box("Midpoint", qsnap_midpoint, locator_snaptomidpoint_xpm, checkBoxQSnapMidPointStateChanged, 1, 0)
    make_check_box("Center", qsnap_center, locator_snaptocenter_xpm, checkBoxQSnapCenterStateChanged, 2, 0)
    make_check_box("Node", qsnap_node, locator_snaptonode_xpm, checkBoxQSnapNodeStateChanged, 3, 0)
    make_check_box("Quadrant", qsnap_quadrant, locator_snaptoquadrant_xpm, checkBoxQSnapQuadrantStateChanged, 4, 0)
    make_check_box("Intersection", qsnap_intersection, locator_snaptointersection_xpm, checkBoxQSnapIntersectionStateChanged, 5, 0)
    make_check_box("Extension", qsnap_extension, locator_snaptoextension_xpm, checkBoxQSnapExtensionStateChanged, 6, 0)
    make_check_box("Insertion", qsnap_insertion, locator_snaptoinsert_xpm, checkBoxQSnapInsertionStateChanged, 0, 1)
    make_check_box("Perpendicular", qsnap_perpendicular, locator_snaptoperpendicular_xpm, checkBoxQSnapPerpendicularStateChanged, 1, 1)
    make_check_box("Tangent", qsnap_tangent, locator_snaptotangent_xpm, checkBoxQSnapTangentStateChanged, 2, 1)
    make_check_box("Nearest", qsnap_nearest, locator_snaptonearest_xpm, checkBoxQSnapNearestStateChanged, 3, 1)
    make_check_box("Apparent Intersection", qsnap_apparent, locator_snaptoapparentintersection_xpm, checkBoxQSnapApparentIntersectionStateChanged, 4, 1)
    make_check_box("Parallel", qsnap_parallel, locator_snaptoparallel_xpm, checkBoxQSnapParallelStateChanged, 5, 1)

    gridLayoutQSnap.addWidget(buttonQSnapSelectAll, 0, 2, Qt::AlignLeft)
    gridLayoutQSnap.addWidget(buttonQSnapClearAll, 1, 2, Qt::AlignLeft)
    gridLayoutQSnap.setColumnStretch(2,1)
    groupBoxQSnapLoc.setLayout(gridLayoutQSnap)

    #QSnap Visual Config
    QGroupBox* groupBoxQSnapVisual = new QGroupBox(tr("Visual Configuration"), widget)

    QLabel* labelQSnapLocColor = new QLabel(tr("Locator Color"), groupBoxQSnapVisual)
    QComboBox* comboBoxQSnapLocColor = new QComboBox(groupBoxQSnapVisual)
    addColorsToComboBox(comboBoxQSnapLocColor)
    dialog.qsnap_locator_color = settings.qsnap_locator_color
    comboBoxQSnapLocColor.setCurrentIndex(comboBoxQSnapLocColor.findData(dialog.qsnap_locator_color))
    connect(comboBoxQSnapLocColor, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxQSnapLocatorColorCurrentIndexChanged(int)))

    QLabel* labelQSnapLocSize = new QLabel(tr("Locator Size"), groupBoxQSnapVisual)
    QSlider* sliderQSnapLocSize = new QSlider(Qt::Horizontal, groupBoxQSnapVisual)
    sliderQSnapLocSize.setRange(1,20)
    dialog.qsnap_locator_size = settings.qsnap_locator_size
    sliderQSnapLocSize.setValue(dialog.qsnap_locator_size)
    connect(sliderQSnapLocSize, SIGNAL(valueChanged(int)), this, SLOT(sliderQSnapLocatorSizeValueChanged(int)))

    QVBoxLayout* vboxLayoutQSnapVisual = new QVBoxLayout(groupBoxQSnapVisual)
    vboxLayoutQSnapVisual.addWidget(labelQSnapLocColor)
    vboxLayoutQSnapVisual.addWidget(comboBoxQSnapLocColor)
    vboxLayoutQSnapVisual.addWidget(labelQSnapLocSize)
    vboxLayoutQSnapVisual.addWidget(sliderQSnapLocSize)
    groupBoxQSnapVisual.setLayout(vboxLayoutQSnapVisual)

    #QSnap Sensitivity Config
    QGroupBox* groupBoxQSnapSensitivity = new QGroupBox(tr("Sensitivity"), widget)

    QLabel* labelQSnapApertureSize = new QLabel(tr("Aperture Size"), groupBoxQSnapSensitivity)
    QSlider* sliderQSnapApertureSize = new QSlider(Qt::Horizontal, groupBoxQSnapSensitivity)
    sliderQSnapApertureSize.setRange(1,20)
    dialog.qsnap_aperture_size = settings.qsnap_aperture_size
    sliderQSnapApertureSize.setValue(dialog.qsnap_aperture_size)
    connect(sliderQSnapApertureSize, SIGNAL(valueChanged(int)), this, SLOT(sliderQSnapApertureSizeValueChanged(int)))

    QVBoxLayout* vboxLayoutQSnapSensitivity = new QVBoxLayout(groupBoxQSnapSensitivity)
    vboxLayoutQSnapSensitivity.addWidget(labelQSnapApertureSize)
    vboxLayoutQSnapSensitivity.addWidget(sliderQSnapApertureSize)
    groupBoxQSnapSensitivity.setLayout(vboxLayoutQSnapSensitivity)

    #Widget Layout
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget)
    vboxLayoutMain.addWidget(groupBoxQSnapLoc)
    vboxLayoutMain.addWidget(groupBoxQSnapVisual)
    vboxLayoutMain.addWidget(groupBoxQSnapSensitivity)
    vboxLayoutMain.addStretch(1)
    widget.setLayout(vboxLayoutMain)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea.setWidgetResizable(1)
    scrollArea.setWidget(widget)
    return scrollArea

#undef make_check_box

QWidget* Settings_Dialog::createTabQuickTrack():
    QWidget* widget = new QWidget(this)

    # TODO: finish this

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea.setWidgetResizable(1)
    scrollArea.setWidget(widget)
    return scrollArea

QWidget* Settings_Dialog::createTabLineWeight():
    QWidget* widget = new QWidget(this)

    # TODO: finish this

    # Misc
    QGroupBox* groupBoxLwtMisc = new QGroupBox(tr("LineWeight Misc"), widget)

    QGraphicsScene* s = mainWin.activeScene()

    QCheckBox* checkBoxShowLwt = new QCheckBox(tr("Show LineWeight"), groupBoxLwtMisc)
    if (s) {
        dialog.lwt_show_lwt = s.property("ENABLE_LWT").toBool()
    }
    else {
        dialog.lwt_show_lwt = settings.lwt_show_lwt
    }
    preview.lwt_show_lwt = dialog.lwt_show_lwt
    checkBoxShowLwt.setChecked(preview.lwt_show_lwt)
    connect(checkBoxShowLwt, SIGNAL(stateChanged(int)), this, SLOT(checkBoxLwtShowLwtStateChanged(int)))

    QCheckBox* checkBoxRealRender = new QCheckBox(tr("RealRender"), groupBoxLwtMisc)
    checkBoxRealRender.setObjectName("checkBoxRealRender")
    if (s) {
        dialog.lwt_real_render = s.property("ENABLE_REAL").toBool()
    }
    else {
        dialog.lwt_real_render = settings.lwt_real_render
    }
    preview.lwt_real_render = dialog.lwt_real_render
    checkBoxRealRender.setChecked(preview.lwt_real_render)
    connect(checkBoxRealRender, SIGNAL(stateChanged(int)), this, SLOT(checkBoxLwtRealRenderStateChanged(int)))
    checkBoxRealRender.setEnabled(dialog.lwt_show_lwt)

    QLabel* labelDefaultLwt = new QLabel(tr("Default weight"), groupBoxLwtMisc)
    labelDefaultLwt.setEnabled(0); # TODO: remove later
    QComboBox* comboBoxDefaultLwt = new QComboBox(groupBoxLwtMisc)
    dialog.lwt_default_lwt = settings.lwt_default_lwt
    # TODO: populate the comboBox and set the initial value
    comboBoxDefaultLwt.addItem(QString().setNum(dialog.lwt_default_lwt, 'F', 2).append(" mm"), dialog.lwt_default_lwt)
    comboBoxDefaultLwt.setEnabled(0); # TODO: remove later

    QVBoxLayout* vboxLayoutLwtMisc = new QVBoxLayout(groupBoxLwtMisc)
    vboxLayoutLwtMisc.addWidget(checkBoxShowLwt)
    vboxLayoutLwtMisc.addWidget(checkBoxRealRender)
    vboxLayoutLwtMisc.addWidget(labelDefaultLwt)
    vboxLayoutLwtMisc.addWidget(comboBoxDefaultLwt)
    groupBoxLwtMisc.setLayout(vboxLayoutLwtMisc)

    #Widget Layout
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget)
    vboxLayoutMain.addWidget(groupBoxLwtMisc)
    vboxLayoutMain.addStretch(1)
    widget.setLayout(vboxLayoutMain)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea.setWidgetResizable(1)
    scrollArea.setWidget(widget)
    return scrollArea

QWidget* Settings_Dialog::createTabSelection():
    QWidget* widget = new QWidget(this)

    # Selection Modes
    QGroupBox* groupBoxSelectionModes = new QGroupBox(tr("Modes"), widget)

    QCheckBox* checkBoxSelectionModePickFirst = new QCheckBox(tr("Allow Preselection (PickFirst)"), groupBoxSelectionModes)
    dialog.selection_mode_pickfirst = settings.selection_mode_pickfirst
    checkBoxSelectionModePickFirst.setChecked(dialog.selection_mode_pickfirst)
    checkBoxSelectionModePickFirst.setChecked(1); checkBoxSelectionModePickFirst.setEnabled(0); # TODO: Remove this line when Post-selection is available
    connect(checkBoxSelectionModePickFirst, SIGNAL(stateChanged(int)), this, SLOT(checkBoxSelectionModePickFirstStateChanged(int)))

    QCheckBox* checkBoxSelectionModePickAdd = new QCheckBox(tr("Add to Selection (PickAdd)"), groupBoxSelectionModes)
    dialog.selection_mode_pickadd = settings.selection_mode_pickadd
    checkBoxSelectionModePickAdd.setChecked(dialog.selection_mode_pickadd)
    connect(checkBoxSelectionModePickAdd, SIGNAL(stateChanged(int)), this, SLOT(checkBoxSelectionModePickAddStateChanged(int)))

    QCheckBox* checkBoxSelectionModePickDrag = new QCheckBox(tr("Drag to Select (PickDrag)"), groupBoxSelectionModes)
    dialog.selection_mode_pickdrag = settings.selection_mode_pickdrag
    checkBoxSelectionModePickDrag.setChecked(dialog.selection_mode_pickdrag)
    checkBoxSelectionModePickDrag.setChecked(0); checkBoxSelectionModePickDrag.setEnabled(0); #TODO: Remove this line when this functionality is available
    connect(checkBoxSelectionModePickDrag, SIGNAL(stateChanged(int)), this, SLOT(checkBoxSelectionModePickDragStateChanged(int)))

    QVBoxLayout* vboxLayoutSelectionModes = new QVBoxLayout(groupBoxSelectionModes)
    vboxLayoutSelectionModes.addWidget(checkBoxSelectionModePickFirst)
    vboxLayoutSelectionModes.addWidget(checkBoxSelectionModePickAdd)
    vboxLayoutSelectionModes.addWidget(checkBoxSelectionModePickDrag)
    groupBoxSelectionModes.setLayout(vboxLayoutSelectionModes)

    #Selection Colors
    QGroupBox* groupBoxSelectionColors = new QGroupBox(tr("Colors"), widget)

    QLabel* labelCoolGripColor = new QLabel(tr("Cool Grip (Unselected)"), groupBoxSelectionColors)
    QComboBox* comboBoxCoolGripColor = new QComboBox(groupBoxSelectionColors)
    addColorsToComboBox(comboBoxCoolGripColor)
    dialog.selection_coolgrip_color = settings.selection_coolgrip_color
    comboBoxCoolGripColor.setCurrentIndex(comboBoxCoolGripColor.findData(dialog.selection_coolgrip_color))
    connect(comboBoxCoolGripColor, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxSelectionCoolGripColorCurrentIndexChanged(int)))

    QLabel* labelHotGripColor = new QLabel(tr("Hot Grip (Selected)"), groupBoxSelectionColors)
    QComboBox* comboBoxHotGripColor = new QComboBox(groupBoxSelectionColors)
    addColorsToComboBox(comboBoxHotGripColor)
    dialog.selection_hotgrip_color = settings.selection_hotgrip_color
    comboBoxHotGripColor.setCurrentIndex(comboBoxHotGripColor.findData(dialog.selection_hotgrip_color))
    connect(comboBoxHotGripColor, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxSelectionHotGripColorCurrentIndexChanged(int)))

    QVBoxLayout* vboxLayoutSelectionColors = new QVBoxLayout(groupBoxSelectionColors)
    vboxLayoutSelectionColors.addWidget(labelCoolGripColor)
    vboxLayoutSelectionColors.addWidget(comboBoxCoolGripColor)
    vboxLayoutSelectionColors.addWidget(labelHotGripColor)
    vboxLayoutSelectionColors.addWidget(comboBoxHotGripColor)
    groupBoxSelectionColors.setLayout(vboxLayoutSelectionColors)

    #Selection Sizes
    QGroupBox* groupBoxSelectionSizes = new QGroupBox(tr("Sizes"), widget)

    QLabel* labelSelectionGripSize = new QLabel(tr("Grip Size"), groupBoxSelectionSizes)
    QSlider* sliderSelectionGripSize = new QSlider(Qt::Horizontal, groupBoxSelectionSizes)
    sliderSelectionGripSize.setRange(1,20)
    dialog.selection_grip_size = settings.selection_grip_size
    sliderSelectionGripSize.setValue(dialog.selection_grip_size)
    connect(sliderSelectionGripSize, SIGNAL(valueChanged(int)), this, SLOT(sliderSelectionGripSizeValueChanged(int)))

    QLabel* labelSelectionPickBoxSize = new QLabel(tr("Pickbox Size"), groupBoxSelectionSizes)
    QSlider* sliderSelectionPickBoxSize = new QSlider(Qt::Horizontal, groupBoxSelectionSizes)
    sliderSelectionPickBoxSize.setRange(1,20)
    dialog.selection_pickbox_size = settings.selection_pickbox_size
    sliderSelectionPickBoxSize.setValue(dialog.selection_pickbox_size)
    connect(sliderSelectionPickBoxSize, SIGNAL(valueChanged(int)), this, SLOT(sliderSelectionPickBoxSizeValueChanged(int)))

    QVBoxLayout* vboxLayoutSelectionSizes = new QVBoxLayout(groupBoxSelectionSizes)
    vboxLayoutSelectionSizes.addWidget(labelSelectionGripSize)
    vboxLayoutSelectionSizes.addWidget(sliderSelectionGripSize)
    vboxLayoutSelectionSizes.addWidget(labelSelectionPickBoxSize)
    vboxLayoutSelectionSizes.addWidget(sliderSelectionPickBoxSize)
    groupBoxSelectionSizes.setLayout(vboxLayoutSelectionSizes)

    #Widget Layout
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget)
    vboxLayoutMain.addWidget(groupBoxSelectionModes)
    vboxLayoutMain.addWidget(groupBoxSelectionColors)
    vboxLayoutMain.addWidget(groupBoxSelectionSizes)
    vboxLayoutMain.addStretch(1)
    widget.setLayout(vboxLayoutMain)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea.setWidgetResizable(1)
    scrollArea.setWidget(widget)
    return scrollArea

def Settings_Dialog::addColorsToComboBox(QComboBox* comboBox):
    comboBox.addItem(loadIcon(colorred_xpm), tr("Red"), qRgb(255, 0, 0))
    comboBox.addItem(loadIcon(coloryellow_xpm), tr("Yellow"), qRgb(255,255, 0))
    comboBox.addItem(loadIcon(colorgreen_xpm), tr("Green"), qRgb(  0,255, 0))
    comboBox.addItem(loadIcon(colorcyan_xpm), tr("Cyan"), qRgb(  0,255,255))
    comboBox.addItem(loadIcon(colorblue_xpm), tr("Blue"), qRgb(  0, 0,255))
    comboBox.addItem(loadIcon(colormagenta_xpm), tr("Magenta"), qRgb(255, 0,255))
    comboBox.addItem(loadIcon(colorwhite_xpm), tr("White"), qRgb(255,255,255))
    # TODO: Add Other... so the user can select custom colors
}

def Settings_Dialog::comboBoxLanguageCurrentIndexChanged(const QString& lang):
    strcpy(dialog.general_language, lang.toLower().toLocal8Bit().constData())

def Settings_Dialog::comboBoxIconThemeCurrentIndexChanged(const QString& theme):
    strcpy(dialog.general_icon_theme, theme.toLocal8Bit().constData())

def Settings_Dialog::comboBoxIconSizeCurrentIndexChanged(int index):
    QComboBox* comboBox = qobject_cast<QComboBox*>(sender())
    if(comboBox)
    {
        bool ok = 0
        dialog.general_icon_size = comboBox.itemData(index).toUInt(&ok)
        if(!ok)
            dialog.general_icon_size = 16
    }
    else
        dialog.general_icon_size = 16

def Settings_Dialog::checkBoxGeneralMdiBGUseLogoStateChanged(checked):
    preview.general_mdi_bg_use_logo = checked
    mainWin.mdiArea.useBackgroundLogo(checked)

def Settings_Dialog::chooseGeneralMdiBackgroundLogo():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if(button)
    {
        QString selectedImage
        selectedImage = QFileDialog::getOpenFileName(this, tr("Open File"),
                        QStandardPaths::writableLocation(QStandardPaths::PicturesLocation),
                        tr("Images (*.bmp *.png *.jpg)"))

        if (!selectedImage.isNull())
            strcpy(accept_.general_mdi_bg_logo, selectedImage.toLocal8Bit().constData())

        #Update immediately so it can be previewed
        mainWin.mdiArea.setBackgroundLogo(accept_.general_mdi_bg_logo)
    }
}

def Settings_Dialog::checkBoxGeneralMdiBGUseTextureStateChanged(checked):
    preview.general_mdi_bg_use_texture = checked
    mainWin.mdiArea.useBackgroundTexture(checked)

def Settings_Dialog::chooseGeneralMdiBackgroundTexture():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QString selectedImage
        selectedImage = QFileDialog::getOpenFileName(this, tr("Open File"),
          QStandardPaths::writableLocation(QStandardPaths::PicturesLocation),
                        tr("Images (*.bmp *.png *.jpg)"))

        if (!selectedImage.isNull()) {
            strcpy(accept_.general_mdi_bg_texture, selectedImage.toLocal8Bit().constData())
        }

        #Update immediately so it can be previewed
        mainWin.mdiArea.setBackgroundTexture(accept_.general_mdi_bg_texture)
    }
}

def Settings_Dialog::checkBoxGeneralMdiBGUseColorStateChanged(checked):
    preview.general_mdi_bg_use_color = checked
    mainWin.mdiArea.useBackgroundColor(checked)

def Settings_Dialog::chooseGeneralMdiBackgroundColor():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.general_mdi_bg_color), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentGeneralMdiBackgroundColorChanged(const QColor&)))
        colorDialog.exec()

        if (colorDialog.result() == QDialog::Accepted) {
            accept_.general_mdi_bg_color = colorDialog.selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.general_mdi_bg_color))
            button.setIcon(QIcon(pix))
            mainWin.mdiArea.setBackgroundColor(QColor(accept_.general_mdi_bg_color))
        }
        else:
            mainWin.mdiArea.setBackgroundColor(QColor(dialog.general_mdi_bg_color))


def Settings_Dialog::currentGeneralMdiBackgroundColorChanged(const QColor& color):
    preview.general_mdi_bg_color = color.rgb()
    mainWin.mdiArea.setBackgroundColor(QColor(preview.general_mdi_bg_color))


#
check_func(checkBoxTipOfTheDayStateChanged, general_tip_of_the_day)
check_func(checkBoxUseOpenGLStateChanged, display_use_opengl)
check_func(checkBoxRenderHintAAStateChanged, display_renderhint_aa)
check_func(checkBoxRenderHintTextAAStateChanged, display_renderhint_text_aa)
check_func(checkBoxRenderHintSmoothPixStateChanged, display_renderhint_smooth_pix)
check_func(checkBoxRenderHintHighAAStateChanged, display_renderhint_high_aa)
check_func(checkBoxRenderHintNonCosmeticStateChanged, display_renderhint_noncosmetic)


def Settings_Dialog::checkBoxShowScrollBarsStateChanged(checked):
    preview.display_show_scrollbars = checked
    mainWin.updateAllViewScrollBars(preview.display_show_scrollbars)

def Settings_Dialog::spinBoxZoomScaleInValueChanged(value):
    dialog.display_zoomscale_in = value

def Settings_Dialog::spinBoxZoomScaleOutValueChanged(value):
    dialog.display_zoomscale_out = value

def Settings_Dialog::checkBoxDisableBGStateChanged(checked):
    dialog.printing_disable_bg = checked

def Settings_Dialog::chooseDisplayCrossHairColor():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_crosshair_color), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplayCrossHairColorChanged(const QColor&)))
        colorDialog.exec()

        if (colorDialog.result() == QDialog::Accepted) {
            accept_.display_crosshair_color = colorDialog.selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.display_crosshair_color))
            button.setIcon(QIcon(pix))
            mainWin.updateAllViewCrossHairColors(accept_.display_crosshair_color)
        }
        else {
            mainWin.updateAllViewCrossHairColors(dialog.display_crosshair_color)


def Settings_Dialog::currentDisplayCrossHairColorChanged(const QColor& color):
    preview.display_crosshair_color = color.rgb()
    mainWin.updateAllViewCrossHairColors(preview.display_crosshair_color)

def Settings_Dialog::chooseDisplayBackgroundColor():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_bg_color), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplayBackgroundColorChanged(const QColor&)))
        colorDialog.exec()

        if (colorDialog.result() == QDialog::Accepted) {
            accept_.display_bg_color = colorDialog.selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.display_bg_color))
            button.setIcon(QIcon(pix))
            mainWin.updateAllViewBackgroundColors(accept_.display_bg_color)
        }
        else:
            mainWin.updateAllViewBackgroundColors(dialog.display_bg_color)


def Settings_Dialog::currentDisplayBackgroundColorChanged(const QColor& color):
    preview.display_bg_color = color.rgb()
    mainWin.updateAllViewBackgroundColors(preview.display_bg_color)

def Settings_Dialog::chooseDisplaySelectBoxLeftColor():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if button:
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_selectbox_left_color), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplaySelectBoxLeftColorChanged(const QColor&)))
        colorDialog.exec()

        if colorDialog.result() == QDialog::Accepted:
            accept_.display_selectbox_left_color = colorDialog.selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.display_selectbox_left_color))
            button.setIcon(QIcon(pix))
            mainWin.updateAllViewSelectBoxColors(accept_.display_selectbox_left_color,
                accept_.display_selectbox_left_fill,
                accept_.display_selectbox_right_color,
                accept_.display_selectbox_right_fill,
                preview.display_selectbox_alpha)
        else:
            mainWin.updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                dialog.display_selectbox_left_fill,
                dialog.display_selectbox_right_color,
                dialog.display_selectbox_right_fill,
                                                  preview.display_selectbox_alpha)


def Settings_Dialog::currentDisplaySelectBoxLeftColorChanged(const QColor& color):
    preview.display_selectbox_left_color = color.rgb()
    mainWin.updateAllViewSelectBoxColors(preview.display_selectbox_left_color,
                                          preview.display_selectbox_left_fill,
                                          preview.display_selectbox_right_color,
                                          preview.display_selectbox_right_fill,
                                          preview.display_selectbox_alpha)

def Settings_Dialog::chooseDisplaySelectBoxLeftFill():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_selectbox_left_fill), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplaySelectBoxLeftFillChanged(const QColor&)))
        colorDialog.exec()

        if (colorDialog.result() == QDialog::Accepted) {
            accept_.display_selectbox_left_fill = colorDialog.selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.display_selectbox_left_fill))
            button.setIcon(QIcon(pix))
            mainWin.updateAllViewSelectBoxColors(
                accept_.display_selectbox_left_color,
                accept_.display_selectbox_left_fill,
                accept_.display_selectbox_right_color,
                accept_.display_selectbox_right_fill,
                preview.display_selectbox_alpha)
        }
        else {
            mainWin.updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                                                  dialog.display_selectbox_left_fill,
                                                  dialog.display_selectbox_right_color,
                                                  dialog.display_selectbox_right_fill,
                                                  preview.display_selectbox_alpha)


def Settings_Dialog::currentDisplaySelectBoxLeftFillChanged(const QColor& color):
    preview.display_selectbox_left_fill = color.rgb()
    mainWin.updateAllViewSelectBoxColors(preview.display_selectbox_left_color,
        preview.display_selectbox_left_fill,
        preview.display_selectbox_right_color,
        preview.display_selectbox_right_fill,
        preview.display_selectbox_alpha)

def Settings_Dialog::chooseDisplaySelectBoxRightColor():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_selectbox_right_color), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplaySelectBoxRightColorChanged(const QColor&)))
        colorDialog.exec()

        if (colorDialog.result() == QDialog::Accepted) {
            accept_.display_selectbox_right_color = colorDialog.selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.display_selectbox_right_color))
            button.setIcon(QIcon(pix))
            mainWin.updateAllViewSelectBoxColors(accept_.display_selectbox_left_color,
                                                  accept_.display_selectbox_left_fill,
                                                  accept_.display_selectbox_right_color,
                                                  accept_.display_selectbox_right_fill,
                                                  preview.display_selectbox_alpha)
        }
        else {
            mainWin.updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                                                  dialog.display_selectbox_left_fill,
                                                  dialog.display_selectbox_right_color,
                                                  dialog.display_selectbox_right_fill,
                                                  preview.display_selectbox_alpha)


def Settings_Dialog::currentDisplaySelectBoxRightColorChanged(const QColor& color):
    preview.display_selectbox_right_color = color.rgb()
    mainWin.updateAllViewSelectBoxColors(preview.display_selectbox_left_color,
        preview.display_selectbox_left_fill,
        preview.display_selectbox_right_color,
        preview.display_selectbox_right_fill,
        preview.display_selectbox_alpha)

def Settings_Dialog::chooseDisplaySelectBoxRightFill():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_selectbox_right_fill), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplaySelectBoxRightFillChanged(const QColor&)))
        colorDialog.exec()

        if (colorDialog.result() == QDialog::Accepted) {
            accept_.display_selectbox_right_fill = colorDialog.selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.display_selectbox_right_fill))
            button.setIcon(QIcon(pix))
            mainWin.updateAllViewSelectBoxColors(accept_.display_selectbox_left_color,
                 accept_.display_selectbox_left_fill,
                 accept_.display_selectbox_right_color,
                 accept_.display_selectbox_right_fill,
                 preview.display_selectbox_alpha)
        }
        else {
            mainWin.updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                                                  dialog.display_selectbox_left_fill,
                                                  dialog.display_selectbox_right_color,
                                                  dialog.display_selectbox_right_fill,
                                                  preview.display_selectbox_alpha)

def Settings_Dialog::currentDisplaySelectBoxRightFillChanged(const QColor& color):
    preview.display_selectbox_right_fill = color.rgb()
    mainWin.updateAllViewSelectBoxColors(preview.display_selectbox_left_color,
        preview.display_selectbox_left_fill,
        preview.display_selectbox_right_color,
        preview.display_selectbox_right_fill,
        preview.display_selectbox_alpha)

def Settings_Dialog::spinBoxDisplaySelectBoxAlphaValueChanged(value):
    preview.display_selectbox_alpha = value
    mainWin.updateAllViewSelectBoxColors(accept_.display_selectbox_left_color,
        accept_.display_selectbox_left_fill,
        accept_.display_selectbox_right_color,
        accept_.display_selectbox_right_fill,
        preview.display_selectbox_alpha)

def Settings_Dialog::checkBoxCustomFilterStateChanged(checked):
    QCheckBox* checkBox = qobject_cast<QCheckBox*>(sender())
    if(checkBox)
    {
        QString format = checkBox.text()
        debug_message("CustomFilter: %s %d", qPrintable(format), checked)
        if(checked)
            opensave_custom_filter.append(" *." + format.toLower())
        else
            opensave_custom_filter.remove("*." + format, Qt::CaseInsensitive)
        #dialog.opensave_custom_filter = checked; //TODO


def Settings_Dialog::buttonCustomFilterSelectAllClicked():
    emit buttonCustomFilterSelectAll(1)
    opensave_custom_filter = "supported"

def Settings_Dialog::buttonCustomFilterClearAllClicked():
    emit buttonCustomFilterClearAll(0)
    opensave_custom_filter.clear()

def Settings_Dialog::checkBoxGridColorMatchCrossHairStateChanged(checked):
    dialog.grid_color_match_crosshair = checked
    if (dialog.grid_color_match_crosshair) {
        mainWin.updateAllViewGridColors(accept_.display_crosshair_color)
    }
    else {
        mainWin.updateAllViewGridColors(accept_.grid_color)
    }

    QObject* senderObj = sender()
    if (senderObj) {
        QObject* parent = senderObj.parent()
        if (parent) {
            QLabel* labelGridColor = parent.findChild<QLabel*>("labelGridColor")
            if (labelGridColor)
                labelGridColor.setEnabled(!dialog.grid_color_match_crosshair)
            QPushButton* buttonGridColor = parent.findChild<QPushButton*>("buttonGridColor")
            if (buttonGridColor)
                buttonGridColor.setEnabled(!dialog.grid_color_match_crosshair)


def Settings_Dialog::chooseGridColor():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.grid_color), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentGridColorChanged(const QColor&)))
        colorDialog.exec()

        if (colorDialog.result() == QDialog::Accepted) {
            accept_.grid_color = colorDialog.selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.grid_color))
            button.setIcon(QIcon(pix))
            mainWin.updateAllViewGridColors(accept_.grid_color)
        }
        else {
            mainWin.updateAllViewGridColors(dialog.grid_color)


def Settings_Dialog::currentGridColorChanged(const QColor& color):
    preview.grid_color = color.rgb()
    mainWin.updateAllViewGridColors(preview.grid_color)

def Settings_Dialog::checkBoxGridLoadFromFileStateChanged(checked):
    dialog.grid_load_from_file = checked

    QObject* senderObj = sender()
    if (senderObj) {
        QObject* parent = senderObj.parent()
        if (parent) {
            QLabel* labelGridType = parent.findChild<QLabel*>("labelGridType")
            if(labelGridType) labelGridType.setEnabled(!dialog.grid_load_from_file)
            QComboBox* comboBoxGridType = parent.findChild<QComboBox*>("comboBoxGridType")
            if(comboBoxGridType) comboBoxGridType.setEnabled(!dialog.grid_load_from_file)
            QCheckBox* checkBoxGridCenterOnOrigin = parent.findChild<QCheckBox*>("checkBoxGridCenterOnOrigin")
            if(checkBoxGridCenterOnOrigin) checkBoxGridCenterOnOrigin.setEnabled(!dialog.grid_load_from_file)
            QLabel* labelGridCenterX = parent.findChild<QLabel*>("labelGridCenterX")
            if(labelGridCenterX) labelGridCenterX.setEnabled(!dialog.grid_load_from_file and !dialog.grid_center_on_origin)
            QDoubleSpinBox* spinBoxGridCenterX = parent.findChild<QDoubleSpinBox*>("spinBoxGridCenterX")
            if(spinBoxGridCenterX) spinBoxGridCenterX.setEnabled(!dialog.grid_load_from_file and !dialog.grid_center_on_origin)
            QLabel* labelGridCenterY = parent.findChild<QLabel*>("labelGridCenterY")
            if(labelGridCenterY) labelGridCenterY.setEnabled(!dialog.grid_load_from_file and !dialog.grid_center_on_origin)
            QDoubleSpinBox* spinBoxGridCenterY = parent.findChild<QDoubleSpinBox*>("spinBoxGridCenterY")
            if(spinBoxGridCenterY) spinBoxGridCenterY.setEnabled(!dialog.grid_load_from_file and !dialog.grid_center_on_origin)
            QLabel* labelGridSizeX = parent.findChild<QLabel*>("labelGridSizeX")
            if(labelGridSizeX) labelGridSizeX.setEnabled(!dialog.grid_load_from_file)
            QDoubleSpinBox* spinBoxGridSizeX = parent.findChild<QDoubleSpinBox*>("spinBoxGridSizeX")
            if(spinBoxGridSizeX) spinBoxGridSizeX.setEnabled(!dialog.grid_load_from_file)
            QLabel* labelGridSizeY = parent.findChild<QLabel*>("labelGridSizeY")
            if(labelGridSizeY) labelGridSizeY.setEnabled(!dialog.grid_load_from_file)
            QDoubleSpinBox* spinBoxGridSizeY = parent.findChild<QDoubleSpinBox*>("spinBoxGridSizeY")
            if(spinBoxGridSizeY) spinBoxGridSizeY.setEnabled(!dialog.grid_load_from_file)
            QLabel* labelGridSpacingX = parent.findChild<QLabel*>("labelGridSpacingX")
            if(labelGridSpacingX) labelGridSpacingX.setEnabled(!dialog.grid_load_from_file)
            QDoubleSpinBox* spinBoxGridSpacingX = parent.findChild<QDoubleSpinBox*>("spinBoxGridSpacingX")
            if(spinBoxGridSpacingX) spinBoxGridSpacingX.setEnabled(!dialog.grid_load_from_file)
            QLabel* labelGridSpacingY = parent.findChild<QLabel*>("labelGridSpacingY")
            if(labelGridSpacingY) labelGridSpacingY.setEnabled(!dialog.grid_load_from_file)
            QDoubleSpinBox* spinBoxGridSpacingY = parent.findChild<QDoubleSpinBox*>("spinBoxGridSpacingY")
            if(spinBoxGridSpacingY) spinBoxGridSpacingY.setEnabled(!dialog.grid_load_from_file)
            QLabel* labelGridSizeRadius = parent.findChild<QLabel*>("labelGridSizeRadius")
            if(labelGridSizeRadius) labelGridSizeRadius.setEnabled(!dialog.grid_load_from_file)
            QDoubleSpinBox* spinBoxGridSizeRadius = parent.findChild<QDoubleSpinBox*>("spinBoxGridSizeRadius")
            if(spinBoxGridSizeRadius) spinBoxGridSizeRadius.setEnabled(!dialog.grid_load_from_file)
            QLabel* labelGridSpacingRadius = parent.findChild<QLabel*>("labelGridSpacingRadius")
            if (labelGridSpacingRadius) {
                labelGridSpacingRadius.setEnabled(!dialog.grid_load_from_file)
            }
            QDoubleSpinBox* spinBoxGridSpacingRadius = parent.findChild<QDoubleSpinBox*>("spinBoxGridSpacingRadius")
            if (spinBoxGridSpacingRadius) {
                spinBoxGridSpacingRadius.setEnabled(!dialog.grid_load_from_file)
            }
            QLabel* labelGridSpacingAngle = parent.findChild<QLabel*>("labelGridSpacingAngle")
            if (labelGridSpacingAngle) {
                labelGridSpacingAngle.setEnabled(!dialog.grid_load_from_file)
            }
            QDoubleSpinBox* spinBoxGridSpacingAngle = parent.findChild<QDoubleSpinBox*>("spinBoxGridSpacingAngle")
            if(spinBoxGridSpacingAngle) spinBoxGridSpacingAngle.setEnabled(!dialog.grid_load_from_file)


def Settings_Dialog::comboBoxGridTypeCurrentIndexChanged(const QString& type):
    strcpy(dialog.grid_type, type.toLocal8Bit().constData())

    senderObj = sender()
    if senderObj:
        parent = senderObj.parent()
        if parent:
            int visibility = False
            if type == "Circular":
                visibility = True

            QLabel* labelGridSizeX = parent.findChild<QLabel*>("labelGridSizeX")
            if (labelGridSizeX) {
                labelGridSizeX.setVisible(!visibility)
            }
            QDoubleSpinBox* spinBoxGridSizeX = parent.findChild<QDoubleSpinBox*>("spinBoxGridSizeX")
            if (spinBoxGridSizeX) {
                spinBoxGridSizeX.setVisible(!visibility)
            }
            QLabel* labelGridSizeY = parent.findChild<QLabel*>("labelGridSizeY")
            if (labelGridSizeY) {
                labelGridSizeY.setVisible(!visibility)
            }
            QDoubleSpinBox* spinBoxGridSizeY = parent.findChild<QDoubleSpinBox*>("spinBoxGridSizeY")
            if (spinBoxGridSizeY) {
                spinBoxGridSizeY.setVisible(!visibility)
            }
            QLabel* labelGridSpacingX = parent.findChild<QLabel*>("labelGridSpacingX")
            if(labelGridSpacingX) labelGridSpacingX.setVisible(!visibility)
            QDoubleSpinBox* spinBoxGridSpacingX = parent.findChild<QDoubleSpinBox*>("spinBoxGridSpacingX")
            if(spinBoxGridSpacingX) spinBoxGridSpacingX.setVisible(!visibility)
            QLabel* labelGridSpacingY = parent.findChild<QLabel*>("labelGridSpacingY")
            if(labelGridSpacingY) labelGridSpacingY.setVisible(!visibility)
            spinBoxGridSpacingY = parent.findChild<QDoubleSpinBox*>("spinBoxGridSpacingY")
            if spinBoxGridSpacingY:
                spinBoxGridSpacingY.setVisible(not visibility)
            labelGridSizeRadius = parent.findChild<QLabel*>("labelGridSizeRadius")
            if labelGridSizeRadius:
                labelGridSizeRadius.setVisible(visibility)
            QDoubleSpinBox* spinBoxGridSizeRadius = parent.findChild<QDoubleSpinBox*>("spinBoxGridSizeRadius")
            if(spinBoxGridSizeRadius) spinBoxGridSizeRadius.setVisible(visibility)
            QLabel* labelGridSpacingRadius = parent.findChild<QLabel*>("labelGridSpacingRadius")
            if(labelGridSpacingRadius) labelGridSpacingRadius.setVisible(visibility)
            QDoubleSpinBox* spinBoxGridSpacingRadius = parent.findChild<QDoubleSpinBox*>("spinBoxGridSpacingRadius")
            if(spinBoxGridSpacingRadius) spinBoxGridSpacingRadius.setVisible(visibility)
            QLabel* labelGridSpacingAngle = parent.findChild<QLabel*>("labelGridSpacingAngle")
            if(labelGridSpacingAngle) labelGridSpacingAngle.setVisible(visibility)
            QDoubleSpinBox* spinBoxGridSpacingAngle = parent.findChild<QDoubleSpinBox*>("spinBoxGridSpacingAngle")
            if(spinBoxGridSpacingAngle) spinBoxGridSpacingAngle.setVisible(visibility)


def Settings_Dialog::checkBoxGridCenterOnOriginStateChanged(checked):
    dialog.grid_center_on_origin = checked

    QObject* senderObj = sender()
    if (senderObj) {
        QObject* parent = senderObj.parent()
        if (parent) {
            QLabel* labelGridCenterX = parent.findChild<QLabel*>("labelGridCenterX")
            if (labelGridCenterX) {
                labelGridCenterX.setEnabled(!dialog.grid_center_on_origin)
            }
            QDoubleSpinBox* spinBoxGridCenterX = parent.findChild<QDoubleSpinBox*>("spinBoxGridCenterX")
            if (spinBoxGridCenterX) {
                spinBoxGridCenterX.setEnabled(!dialog.grid_center_on_origin)
            }
            QLabel* labelGridCenterY = parent.findChild<QLabel*>("labelGridCenterY")
            if(labelGridCenterY) labelGridCenterY.setEnabled(!dialog.grid_center_on_origin)
            QDoubleSpinBox* spinBoxGridCenterY = parent.findChild<QDoubleSpinBox*>("spinBoxGridCenterY")
            if(spinBoxGridCenterY) spinBoxGridCenterY.setEnabled(!dialog.grid_center_on_origin)


def Settings_Dialog::comboBoxRulerMetricCurrentIndexChanged(int index):
    comboBox = qobject_cast<QComboBox*>(sender())
    if comboBox:
        ok = False
        dialog.ruler_metric = comboBox.itemData(index).toBool()
    else:
        dialog.ruler_metric = True

def Settings_Dialog::chooseRulerColor():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(
            QColor(accept_.ruler_color), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)),
            this, SLOT(currentRulerColorChanged(const QColor&)))
        colorDialog.exec()

        if (colorDialog.result() == QDialog::Accepted) {
            accept_.ruler_color = colorDialog.selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.ruler_color))
            button.setIcon(QIcon(pix))
            mainWin.updateAllViewRulerColors(accept_.ruler_color)
        }
        else {
            mainWin.updateAllViewRulerColors(dialog.ruler_color)

def Settings_Dialog::currentRulerColorChanged(const QColor& color):
    preview.ruler_color = color.rgb()
    mainWin.updateAllViewRulerColors(preview.ruler_color)

def Settings_Dialog::buttonQSnapSelectAllClicked():
    emit buttonQSnapSelectAll(1)

def Settings_Dialog::buttonQSnapClearAllClicked():
    emit buttonQSnapClearAll(0)

#
# TODO:
# Figure out how to abstract the slot in a way that it can be used for
# comboBoxes in general
# Currently comboBoxQSnapLocatorColorCurrentIndexChanged(int index)
#        comboBoxSelectionCoolGripColorCurrentIndexChanged(int index)
#        comboBoxSelectionHotGripColorCurrentIndexChanged(int index)
# are all similar except the dialog. variable being worked on and the
# QVariant.


def Settings_Dialog::comboBoxQSnapLocatorColorCurrentIndexChanged(int index):
    # TODO: Alert user if color matched the display bg color
    QComboBox* comboBox = qobject_cast<QComboBox*>(sender())
    unsigned int defaultColor = qRgb(255,255,0); # Yellow
    if comboBox:
        bool ok = 0
        dialog.qsnap_locator_color = comboBox.itemData(index).toUInt(&ok)
        if(!ok)
            dialog.qsnap_locator_color = defaultColor
    else:
        dialog.qsnap_locator_color = defaultColor

def Settings_Dialog::sliderQSnapLocatorSizeValueChanged(value):
    dialog.qsnap_locator_size = value

def Settings_Dialog::sliderQSnapApertureSizeValueChanged(value):
    dialog.qsnap_aperture_size = value

def Settings_Dialog::checkBoxLwtShowLwtStateChanged(checked):
    preview.lwt_show_lwt = checked
    if (preview.lwt_show_lwt) {
        enableLwt()
    }
    else {
        disableLwt()
    }

    QObject* senderObj = sender()
    if (senderObj) {
        QObject* parent = senderObj.parent()
        if (parent) {
            QCheckBox* checkBoxRealRender = parent.findChild<QCheckBox*>("checkBoxRealRender")
            if (checkBoxRealRender) {
                checkBoxRealRender.setEnabled(preview.lwt_show_lwt)

def Settings_Dialog::checkBoxLwtRealRenderStateChanged(checked):
    preview.lwt_real_render = checked
    if preview.lwt_real_render:
        enableReal()
    else:
        disableReal()

def Settings_Dialog::comboBoxSelectionCoolGripColorCurrentIndexChanged(int index):
    # TODO: Alert user if color matched the display bg color
    QComboBox* comboBox = qobject_cast<QComboBox*>(sender())
    unsigned int defaultColor = qRgb(0,0,255); #Blue
    if (comboBox) {
        bool ok = 0
        dialog.selection_coolgrip_color = comboBox.itemData(index).toUInt(&ok)
        if not ok:
            dialog.selection_coolgrip_color = defaultColor
    else {
        dialog.selection_coolgrip_color = defaultColor

def Settings_Dialog::comboBoxSelectionHotGripColorCurrentIndexChanged(int index):
    # TODO: Alert user if color matched the display bg color
    QComboBox* comboBox = qobject_cast<QComboBox*>(sender())
    unsigned int defaultColor = qRgb(255,0,0); # Red
    if (comboBox) {
        ok = False
        dialog.selection_hotgrip_color = comboBox.itemData(index).toUInt(&ok)
        if (!ok) {
            dialog.selection_hotgrip_color = defaultColor
    else:
        dialog.selection_hotgrip_color = defaultColor

def Settings_Dialog::acceptChanges():
    for k in preview.keys():
        dialog[k] = preview[k]
    for k in accept_.keys():
        dialog[k] = preview[k]

    if dialog["grid_color_match_crosshair"]:
        dialog["grid_color"] = accept_["display_crosshair_color"]

    # Make sure the user sees the changes applied immediately.
    mainWin.mdiArea.useBackgroundLogo(dialog.general_mdi_bg_use_logo)
    mainWin.mdiArea.useBackgroundTexture(dialog.general_mdi_bg_use_texture)
    mainWin.mdiArea.useBackgroundColor(dialog.general_mdi_bg_use_color)
    mainWin.mdiArea.setBackgroundLogo(dialog.general_mdi_bg_logo)
    mainWin.mdiArea.setBackgroundTexture(dialog.general_mdi_bg_texture)
    mainWin.mdiArea.setBackgroundColor(dialog.general_mdi_bg_color)
    mainWin.iconResize(dialog.general_icon_size)
    mainWin.updateAllViewScrollBars(dialog.display_show_scrollbars)
    mainWin.updateAllViewCrossHairColors(dialog.display_crosshair_color)
    mainWin.updateAllViewBackgroundColors(dialog.display_bg_color)
    mainWin.updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                                          dialog.display_selectbox_left_fill,
                                          dialog.display_selectbox_right_color,
                                          dialog.display_selectbox_right_fill,
                                          dialog.display_selectbox_alpha)
    mainWin.updateAllViewGridColors(dialog.grid_color)
    mainWin.updateAllViewRulerColors(dialog.ruler_color)
    if (dialog.lwt_show_lwt) {
        enableLwt()
    }
    else { disableLwt(); }
    if (dialog.lwt_real_render) { enableReal(); }
    else { disableReal(); }
    mainWin.updatePickAddMode(dialog.selection_mode_pickadd)

    mainWin.writeSettings()
    accept()

def Settings_Dialog::rejectChanges():
    #TODO: inform the user if they have changed settings

    #Update the view since the user must accept the preview
    mainWin.mdiArea.useBackgroundLogo(dialog.general_mdi_bg_use_logo)
    mainWin.mdiArea.useBackgroundTexture(dialog.general_mdi_bg_use_texture)
    mainWin.mdiArea.useBackgroundColor(dialog.general_mdi_bg_use_color)
    mainWin.mdiArea.setBackgroundLogo(dialog.general_mdi_bg_logo)
    mainWin.mdiArea.setBackgroundTexture(dialog.general_mdi_bg_texture)
    mainWin.mdiArea.setBackgroundColor(dialog.general_mdi_bg_color)
    mainWin.updateAllViewScrollBars(dialog.display_show_scrollbars)
    mainWin.updateAllViewCrossHairColors(dialog.display_crosshair_color)
    mainWin.updateAllViewBackgroundColors(dialog.display_bg_color)
    mainWin.updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                                          dialog.display_selectbox_left_fill,
                                          dialog.display_selectbox_right_color,
                                          dialog.display_selectbox_right_fill,
                                          dialog.display_selectbox_alpha)
    mainWin.updateAllViewGridColors(dialog.grid_color)
    mainWin.updateAllViewRulerColors(dialog.ruler_color)
    if(dialog.lwt_show_lwt) { enableLwt(); }
    else                    { disableLwt(); }
    if(dialog.lwt_real_render) { enableReal(); }
    else                       { disableReal(); }

    reject()



PropertyEditor::PropertyEditor(const QString& iconDirectory, int pickAddMode, QWidget* widgetToFocus, QWidget* parent, Qt::WindowFlags flags) : QDockWidget(parent, flags):
    int i
    iconDir = iconDirectory
    iconSize = 16
    propertyEditorButtonStyle = Qt::ToolButtonTextBesideIcon; #TODO: Make customizable
    setMinimumSize(100,100)

    pickAdd = pickAddMode

    precisionAngle = 0; #TODO: Load this from settings and provide function for updating from settings
    precisionLength = 4; #TODO: Load this from settings and provide function for updating from settings

    signalMapper = new QSignalMapper(this)

    fieldOldText = ""
    fieldNewText = ""
    fieldVariesText = "*Varies*"
    fieldYesText = "Yes"
    fieldNoText = "No"
    fieldOnText = "On"
    fieldOffText = "Off"

    QWidget* widgetMain = new QWidget(this)

    QWidget* widgetSelection = new QWidget(this)
    QHBoxLayout* hboxLayoutSelection = new QHBoxLayout(this)
    hboxLayoutSelection.addWidget(createComboBoxSelected())
    hboxLayoutSelection.addWidget(createToolButtonQSelect())
    hboxLayoutSelection.addWidget(createToolButtonPickAdd())
    widgetSelection.setLayout(hboxLayoutSelection)

    for (i=1; i<OBJ_TYPE_UNKNOWN-OBJ_TYPE_BASE; i++) {
        groupBoxGeometry[i] = createGroupBoxGeometry(i+OBJ_TYPE_BASE)
    }

    QScrollArea* scrollProperties = new QScrollArea(this)
    QWidget* widgetProperties = new QWidget(this)
    QVBoxLayout* vboxLayoutProperties = new QVBoxLayout(this)
    vboxLayoutProperties.addWidget(createGroupBoxGeneral())
    for (i=1; i<OBJ_TYPE_UNKNOWN-OBJ_TYPE_BASE; i++) {
        vboxLayoutProperties.addWidget(groupBoxGeometry[i+OBJ_TYPE_BASE])
    }
    vboxLayoutProperties.addWidget(createGroupBoxMiscArc())
    vboxLayoutProperties.addWidget(createGroupBoxMiscImage())
    vboxLayoutProperties.addWidget(createGroupBoxMiscPath())
    vboxLayoutProperties.addWidget(createGroupBoxMiscPolyline())
    vboxLayoutProperties.addWidget(createGroupBoxTextTextSingle())
    vboxLayoutProperties.addWidget(createGroupBoxMiscTextSingle())
    vboxLayoutProperties.addStretch(1)
    widgetProperties.setLayout(vboxLayoutProperties)
    scrollProperties.setWidget(widgetProperties)
    scrollProperties.setWidgetResizable(1)

    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(this)
    vboxLayoutMain.addWidget(widgetSelection)
    vboxLayoutMain.addWidget(scrollProperties)
    widgetMain.setLayout(vboxLayoutMain)

    setWidget(widgetMain)
    setWindowTitle(tr("Properties"))
    setAllowedAreas(Qt::LeftDockWidgetArea | Qt::RightDockWidgetArea)

    hideAllGroups()

    connect(signalMapper, SIGNAL(mapped(QObject*)), this, SLOT(fieldEdited(QObject*)))

    focusWidget = widgetToFocus
    this.installEventFilter(this)

PropertyEditor::~PropertyEditor():
}

def PropertyEditor::eventFilter(QObject *obj, QEvent *event):
    if(event.type() == QEvent::KeyPress)
    {
        QKeyEvent* pressedKey = (QKeyEvent*)event
        int key = pressedKey.key()
        switch(key)
        {
            case Qt::Key_Escape:
                if(focusWidget)
                    focusWidget.setFocus(Qt::OtherFocusReason)
                return 1
                break
            default:
                pressedKey.ignore()
        }
    }
    return QObject::eventFilter(obj, event)

QComboBox* PropertyEditor::createComboBoxSelected():
    comboBoxSelected = new QComboBox(this)
    comboBoxSelected.addItem(tr("No Selection"))
    return comboBoxSelected

QToolButton* PropertyEditor::createToolButtonQSelect():
    toolButtonQSelect = new QToolButton(this)
    toolButtonQSelect.setIcon(loadIcon(quickselect_xpm))
    toolButtonQSelect.setIconSize(QSize(iconSize, iconSize))
    toolButtonQSelect.setText("QSelect")
    toolButtonQSelect.setToolTip("QSelect"); #TODO: Better Description
    toolButtonQSelect.setToolButtonStyle(Qt::ToolButtonIconOnly)
    return toolButtonQSelect

QToolButton* PropertyEditor::createToolButtonPickAdd():
    #TODO: Set as PickAdd or PickNew based on settings
    toolButtonPickAdd = new QToolButton(this)
    updatePickAddModeButton(pickAdd)
    connect(toolButtonPickAdd, SIGNAL(clicked(int)), this, SLOT(togglePickAddMode()))
    return toolButtonPickAdd

def PropertyEditor::updatePickAddModeButton(int pickAddMode):
    pickAdd = pickAddMode
    if (pickAdd) {
        toolButtonPickAdd.setIcon(loadIcon(pickadd_xpm))
        toolButtonPickAdd.setIconSize(QSize(iconSize, iconSize))
        toolButtonPickAdd.setText("PickAdd")
        toolButtonPickAdd.setToolTip("PickAdd Mode - Add to current selection.\nClick to switch to PickNew Mode.")
        toolButtonPickAdd.setToolButtonStyle(Qt::ToolButtonIconOnly)
    }
    else {
        toolButtonPickAdd.setIcon(loadIcon(picknew_xpm))
        toolButtonPickAdd.setIconSize(QSize(iconSize, iconSize))
        toolButtonPickAdd.setText("PickNew")
        toolButtonPickAdd.setToolTip("PickNew Mode - Replace current selection.\nClick to switch to PickAdd Mode.")
        toolButtonPickAdd.setToolButtonStyle(Qt::ToolButtonIconOnly)

def PropertyEditor::togglePickAddMode():
    emit pickAddModeToggled()

def PropertyEditor::setSelectedItems(QList<QGraphicsItem*> itemList):
    selectedItemList = itemList
    #Hide all the groups initially, then decide which ones to show
    hideAllGroups()
    comboBoxSelected.clear()

    if(itemList.isEmpty())
    {
        comboBoxSelected.addItem(tr("No Selection"))
        return
    }

    QSet<int> typeSet

    int numObjects[31], i

    int numAll = itemList.size()
    for (i=0; i<31; i++) {
        numObjects[i] = 0
    }
    int numTypes = 0

    foreach (QGraphicsItem* item, itemList) {
        if(!item) continue

        int objType = item.type()
        typeSet.insert(objType)

        if (objType > OBJ_TYPE_BASE and objType < OBJ_TYPE_UNKNOWN) {
            if (numObjects[objType-OBJ_TYPE_BASE] == 0) {
                numTypes++
            numObjects[objType-OBJ_TYPE_BASE]++
        else {
            numObjects[OBJ_TYPE_UNKNOWN-OBJ_TYPE_BASE]++

    # ==================================================
    #  Populate the selection comboBox
    # ==================================================
    if (numTypes > 1) {
        comboBoxSelected.addItem(tr("Varies") + " (" + QString().setNum(numAll) + ")")
        connect(comboBoxSelected, SIGNAL(currentIndexChanged(int)), this, SLOT(showOneType(int)))

    for (i=0; i<31; i++) {
        if (numObjects[i] > 0) {
            QString comboBoxStr = tr(obj_names[i])
                + " (" + QString().setNum(numObjects[i]) + ")"
            comboBoxSelected.addItem(comboBoxStr, OBJ_TYPE_BASE+i)

    # ==================================================
    # Load Data into the fields
    # ==================================================

    # Clear fields first so if the selected data varies, the comparison is simple
    clearAllFields()

    foreach(QGraphicsItem* item, itemList) {
        if(!item) continue

        # TODO: load data into the General field

        int objType = item.type()
        switch (objType) {
        case OBJ_TYPE_ARC:
            {
            ArcObject* obj = static_cast<ArcObject*>(item)
            if (obj) {
                QPointF p = obj.objectCenter()
                updateLineEditNumIfVaries(lineEdit[ARC_CENTER_X], p.x(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_CENTER_Y], -p.y(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_RADIUS], obj.objectRadius(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_START_ANGLE], obj.objectStartAngle(), 1)
                updateLineEditNumIfVaries(lineEdit[ARC_END_ANGLE], obj.objectEndAngle(), 1)
                updateLineEditNumIfVaries(lineEdit[ARC_START_X], obj.objectStartPoint().x(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_START_Y], -obj.objectStartPoint().y(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_END_X], obj.objectEndPoint().x(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_END_Y], -obj.objectEndPoint().y(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_AREA], obj.objectArea(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_LENGTH], obj.objectArcLength(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_CHORD], obj.objectChord(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_INC_ANGLE], obj.objectIncludedAngle(), 1)
                updateComboBoxintIfVaries(comboBox[ARC_CLOCKWISE], obj.objectClockwise(), 1)
            }
            }
            break
        case OBJ_TYPE_BLOCK:
            {
            #TODO: load block data
            }
            break
        case OBJ_TYPE_CIRCLE:
            {
            CircleObject* obj = static_cast<CircleObject*>(item)
            if (obj) {
                QPointF p = obj.objectCenter()
                updateLineEditNumIfVaries(lineEdit[CIRCLE_CENTER_X], p.x(), 0)
                updateLineEditNumIfVaries(lineEdit[CIRCLE_CENTER_Y], -p.y(), 0)
                updateLineEditNumIfVaries(lineEdit[CIRCLE_RADIUS], obj.objectRadius(), 0)
                updateLineEditNumIfVaries(lineEdit[CIRCLE_DIAMETER], obj.objectDiameter(), 0)
                updateLineEditNumIfVaries(lineEdit[CIRCLE_AREA], obj.objectArea(), 0)
                updateLineEditNumIfVaries(lineEdit[CIRCLE_CIRCUMFERENCE], obj.objectCircumference(), 0)
            }
            }
            break
        case OBJ_TYPE_DIMALIGNED:
            {
            # TODO: load aligned dimension data
            }
            break
        case OBJ_TYPE_DIMANGULAR:
            {
            # TODO: load angular dimension data
            }
            break
        case OBJ_TYPE_DIMARCLENGTH:
            {
            # TODO: load arclength dimension data
            }
            break
        case OBJ_TYPE_DIMDIAMETER:
            {
            # TODO: load diameter dimension data
            }
            break
        case OBJ_TYPE_DIMLEADER:
            {
            # TODO: load leader dimension data
            }
            break
        case OBJ_TYPE_DIMLINEAR:
            {
            # TODO: load linear dimension data
            }
            break
        case OBJ_TYPE_DIMORDINATE:
            {
            # TODO: load ordinate dimension data
            }
            break
        case OBJ_TYPE_DIMRADIUS:
            {
            # TODO: load radius dimension data
            }
            break
        case OBJ_TYPE_ELLIPSE:
            {
            EllipseObject* obj = static_cast<EllipseObject*>(item)
            if (obj) {
                QPointF p = obj.objectCenter()
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_CENTER_X], p.x(), 0)
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_CENTER_Y], -p.y(), 0)
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_RADIUS_MAJOR], obj.objectRadiusMajor(), 0)
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_RADIUS_MINOR], obj.objectRadiusMinor(), 0)
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_DIAMETER_MAJOR], obj.objectDiameterMajor(), 0)
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_DIAMETER_MINOR], obj.objectDiameterMinor(), 0)
            }
            }
            break
        case OBJ_TYPE_IMAGE:
            {
            #TODO: load image data
            }
            break
        case OBJ_TYPE_INFINITELINE:
            {
            # TODO: load infinite line data
            }
            break
        case OBJ_TYPE_LINE:
            {
            LineObject* obj = static_cast<LineObject*>(item)
            if (obj) {
                updateLineEditNumIfVaries(lineEdit[LINE_START_X], obj.objectEndPoint1().x(), 0)
                updateLineEditNumIfVaries(lineEdit[LINE_START_Y], -obj.objectEndPoint1().y(), 0)
                updateLineEditNumIfVaries(lineEdit[LINE_END_X], obj.objectEndPoint2().x(), 0)
                updateLineEditNumIfVaries(lineEdit[LINE_END_Y], -obj.objectEndPoint2().y(), 0)
                updateLineEditNumIfVaries(lineEdit[LINE_DELTA_X], obj.objectDeltaX(), 0)
                updateLineEditNumIfVaries(lineEdit[LINE_DELTA_Y], -obj.objectDeltaY(), 0)
                updateLineEditNumIfVaries(lineEdit[LINE_ANGLE], obj.objectAngle(), 1)
                updateLineEditNumIfVaries(lineEdit[LINE_LENGTH], obj.objectLength(), 0)
            }
            }
            break
        case OBJ_TYPE_PATH:
        {
            #TODO: load path data
        }
            break
        case OBJ_TYPE_POINT:
            {
            PointObject* obj = static_cast<PointObject*>(item)
            if (obj) {
                updateLineEditNumIfVaries(lineEdit[POINT_X], obj.objectX(), 0)
                updateLineEditNumIfVaries(lineEdit[POINT_Y], -obj.objectY(), 0)
            }
            }
            break
        case OBJ_TYPE_POLYGON:
            {
            #TODO: load polygon data
            }
            break
        case OBJ_TYPE_POLYLINE:
            {
            #TODO: load polyline data
            }
            break
        case OBJ_TYPE_RAY:
            {
            #TODO: load ray data
            }
            break
        case OBJ_TYPE_RECTANGLE:
            {
            RectObject* obj = static_cast<RectObject*>(item)
            if(obj) {
                QPointF corn1 = obj.objectTopLeft()
                QPointF corn2 = obj.objectTopRight()
                QPointF corn3 = obj.objectBottomLeft()
                QPointF corn4 = obj.objectBottomRight()

                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_X1], corn1.x(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_Y1], -corn1.y(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_X2], corn2.x(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_Y2], -corn2.y(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_X3], corn3.x(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_Y3], -corn3.y(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_X4], corn4.x(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_Y4], -corn4.y(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_WIDTH], obj.objectWidth(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_HEIGHT], -obj.objectHeight(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_AREA], obj.objectArea(), 0)
            }
            }
            break
        case OBJ_TYPE_TEXTMULTI:
            {
            # TODO: load multiline text data
            }
            break
        case OBJ_TYPE_TEXTSINGLE:
            {
            TextSingleObject* obj = static_cast<TextSingleObject*>(item)
            if (obj) {
                updateLineEditStrIfVaries(lineEditTextSingleContents, obj.objText)
                updateFontComboBoxStrIfVaries(comboBoxTextSingleFont, obj.objTextFont)
                updateComboBoxStrIfVaries(comboBoxTextSingleJustify, obj.objTextJustify, obj.objectTextJustifyList())
                updateLineEditNumIfVaries(lineEditTextSingleHeight, obj.obj_text.size, 0)
                updateLineEditNumIfVaries(lineEditTextSingleRotation, -obj.rotation(), 1)
                updateLineEditNumIfVaries(lineEditTextSingleX, obj.objectX(), 0)
                updateLineEditNumIfVaries(lineEditTextSingleY, -obj.objectY(), 0)
                updateComboBoxintIfVaries(comboBoxTextSingleBackward, obj.obj_text.backward, 1)
                updateComboBoxintIfVaries(comboBoxTextSingleUpsideDown, obj.obj_text.upsidedown, 1)
            }
            }
            break
        default:
            break
        }
    }

    #==================================================
    # Only show fields if all objects are the same type
    #==================================================
    if (numTypes == 1) {
        foreach (int objType, typeSet) {
            showGroups(objType)
        }
    }
}

def PropertyEditor::updateLineEditStrIfVaries(QLineEdit* lineEdit, const QString& str):
    fieldOldText = lineEdit.text()
    fieldNewText = str

    if     (fieldOldText.isEmpty())       lineEdit.setText(fieldNewText)
    elif(fieldOldText != fieldNewText) lineEdit.setText(fieldVariesText)

def PropertyEditor::updateLineEditNumIfVaries(QLineEdit* lineEdit, num, int useAnglePrecision):
    int precision = 0
    if(useAnglePrecision) precision = precisionAngle
    else                  precision = precisionLength

    fieldOldText = lineEdit.text()
    fieldNewText.setNum(num, 'f', precision)

    #Prevent negative zero :D
    QString negativeZero = "-0."
    for(int i = 0; i < precision; ++i)
        negativeZero.append('0')
    if(fieldNewText == negativeZero)
        fieldNewText = negativeZero.replace("-", "")

    if     (fieldOldText.isEmpty())       lineEdit.setText(fieldNewText)
    elif(fieldOldText != fieldNewText) lineEdit.setText(fieldVariesText)

def PropertyEditor::updateFontComboBoxStrIfVaries(QFontComboBox* fontComboBox, const QString& str):
    fieldOldText = fontComboBox.property("FontFamily").toString()
    fieldNewText = str
    #debug_message("old: %d %s, new: %d %s", oldIndex, qPrintable(fontComboBox.currentText()), newIndex, qPrintable(str));
    if(fieldOldText.isEmpty())
    {
        fontComboBox.setCurrentFont(QFont(fieldNewText))
        fontComboBox.setProperty("FontFamily", fieldNewText)
    }
    elif(fieldOldText != fieldNewText)
    {
        if(fontComboBox.findText(fieldVariesText) == -1) #Prevent multiple entries
            fontComboBox.addItem(fieldVariesText)
        fontComboBox.setCurrentIndex(fontComboBox.findText(fieldVariesText))
    }
}

def PropertyEditor::updateComboBoxStrIfVaries(QComboBox* comboBox, const QString& str, const QStringList& strList):
    fieldOldText = comboBox.currentText()
    fieldNewText = str

    if(fieldOldText.isEmpty())
    {
        foreach(QString s, strList)
        {
            comboBox.addItem(s, s)
        }
        comboBox.setCurrentIndex(comboBox.findText(fieldNewText))
    }
    elif(fieldOldText != fieldNewText)
    {
        if(comboBox.findText(fieldVariesText) == -1) #Prevent multiple entries
            comboBox.addItem(fieldVariesText)
        comboBox.setCurrentIndex(comboBox.findText(fieldVariesText))
    }
}

def PropertyEditor::updateComboBoxintIfVaries(QComboBox* comboBox, int val, int yesOrNoText):
    fieldOldText = comboBox.currentText()
    if(yesOrNoText)
    {
        if(val) fieldNewText = fieldYesText
        else    fieldNewText = fieldNoText
    }
    else
    {
        if(val) fieldNewText = fieldOnText
        else    fieldNewText = fieldOffText

    if(fieldOldText.isEmpty()) {
        if (yesOrNoText) {
            comboBox.addItem(fieldYesText, 1)
            comboBox.addItem(fieldNoText, 0)
        }
        else {
            comboBox.addItem(fieldOnText, 1)
            comboBox.addItem(fieldOffText, 0)
        }
        comboBox.setCurrentIndex(comboBox.findText(fieldNewText))
    }
    elif(fieldOldText != fieldNewText) {
        # Prevent multiple entries
        if(comboBox.findText(fieldVariesText) == -1) {
            comboBox.addItem(fieldVariesText)
        }
        comboBox.setCurrentIndex(comboBox.findText(fieldVariesText))

def PropertyEditor::showGroups(int objType):
    if (objType>=OBJ_TYPE_BASE and objType<OBJ_TYPE_UNKNOWN) {
        groupBoxGeometry[objType-OBJ_TYPE_BASE].show()
    }
    if (objType == OBJ_TYPE_ARC) {
        groupBoxMiscArc.show()
    }
    elif(objType == OBJ_TYPE_IMAGE) {
        groupBoxMiscImage.show()
    }
    elif(objType == OBJ_TYPE_PATH) {
        groupBoxMiscPath.show()
    }
    elif(objType == OBJ_TYPE_POLYLINE) {
        groupBoxMiscPolyline.show()
    }
    elif(objType == OBJ_TYPE_TEXTSINGLE) {
        groupBoxTextTextSingle.show()
        groupBoxMiscTextSingle.show()
    }
}

def PropertyEditor::showOneType(int index):
    hideAllGroups()
    showGroups(comboBoxSelected.itemData(index).toInt())

def PropertyEditor::hideAllGroups():
    int i
    # NOTE: General group will never be hidden
    for (i=1; i<OBJ_TYPE_UNKNOWN-OBJ_TYPE_BASE; i++) {
        groupBoxGeometry[i].hide()
    }
    groupBoxMiscArc.hide()
    groupBoxMiscImage.hide()
    groupBoxMiscPath.hide()
    groupBoxMiscPolyline.hide()
    groupBoxTextTextSingle.hide()
    groupBoxMiscTextSingle.hide()

def PropertyEditor::clearAllFields():
    int i
    for (i=0; i<COMBOBOX_PROPERTY_EDITORS; i++) {
        comboBox[i].clear()
    }
    for (i=0; i<LINEEDIT_PROPERTY_EDITORS; i++) {
        lineEdit[i].clear()
    }

    # Text Single
    comboBoxTextSingleFont.removeItem(comboBoxTextSingleFont.findText(fieldVariesText))
    # NOTE: Do not clear comboBoxTextSingleFont
    comboBoxTextSingleFont.setProperty("FontFamily", "")

QGroupBox* PropertyEditor::createGroupBoxGeneral():
    groupBoxGeneral = new QGroupBox(tr("General"), this)

    toolButtonGeneralLayer = createToolButton("blank", tr("Layer"));      #TODO: use proper icon
    toolButtonGeneralColor = createToolButton("blank", tr("Color"));      #TODO: use proper icon
    toolButtonGeneralLineType = createToolButton("blank", tr("LineType"));   #TODO: use proper icon
    toolButtonGeneralLineWeight = createToolButton("blank", tr("LineWeight")); #TODO: use proper icon

    comboBoxGeneralLayer = createComboBox(0)
    comboBoxGeneralColor = createComboBox(0)
    comboBoxGeneralLineType = createComboBox(0)
    comboBoxGeneralLineWeight = createComboBox(0)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonGeneralLayer, comboBoxGeneralLayer)
    formLayout.addRow(toolButtonGeneralColor, comboBoxGeneralColor)
    formLayout.addRow(toolButtonGeneralLineType, comboBoxGeneralLineType)
    formLayout.addRow(toolButtonGeneralLineWeight, comboBoxGeneralLineWeight)
    groupBoxGeneral.setLayout(formLayout)

    return groupBoxGeneral

def PropertyEditor::createGroupBoxMiscArc():
    groupBoxMiscArc = new QGroupBox(tr("Misc"), this)

    toolButtonArcClockwise = createToolButton("blank", tr("Clockwise")); #TODO: use proper icon

    comboBoxArcClockwise = createComboBox(1)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonArcClockwise, comboBoxArcClockwise)
    groupBoxMiscArc.setLayout(formLayout)

    return groupBoxMiscArc

def PropertyEditor::createGroupBoxGeometry(int objType):
    int i
    QGroupBox *gb = new QGroupBox(tr("Geometry"), this)

    # TODO: use proper icons
    QFormLayout* formLayout = new QFormLayout(this)
    #
    for (i=0; property_editors[i].object != OBJ_TYPE_UNKNOWN; i++) {
        if (property_editors[i].object == objType) {
            int index = property_editors[i].id
            toolButton[index] = createToolButton(property_editors[i].icon, tr(property_editors[i].label));
            lineEdit[index] = createLineEdit(property_editors[i].type, property_editors[i].read_only)
            formLayout.addRow(toolButton[index], lineEdit[index])
            mapSignal(lineEdit[index], property_editors[i].signal, objType)

    gb.setLayout(formLayout)

    return gb

def PropertyEditor::createGroupBoxMiscImage():
    groupBoxMiscImage = new QGroupBox(tr("Misc"), this)

    # TODO: use proper icon
    toolButtonImageName = createToolButton("blank", tr("Name"));
    toolButtonImagePath = createToolButton("blank", tr("Path"));

    lineEditImageName = createLineEdit("double", 1)
    lineEditImagePath = createLineEdit("double", 1)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonImageName, lineEditImageName)
    formLayout.addRow(toolButtonImagePath, lineEditImagePath)
    groupBoxMiscImage.setLayout(formLayout)

    return groupBoxMiscImage

QGroupBox* PropertyEditor::createGroupBoxMiscPath():
    groupBoxMiscPath = new QGroupBox(tr("Misc"), this)

    toolButtonPathClosed = createToolButton("blank", tr("Closed")); #TODO: use proper icon

    comboBoxPathClosed = createComboBox(0)

    #TODO: mapSignal for paths

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonPathClosed, comboBoxPathClosed)
    groupBoxMiscPath.setLayout(formLayout)

    return groupBoxMiscPath

QGroupBox* PropertyEditor::createGroupBoxMiscPolyline():
    groupBoxMiscPolyline = new QGroupBox(tr("Misc"), this)

    toolButtonPolylineClosed = createToolButton("blank", tr("Closed")); #TODO: use proper icon

    comboBoxPolylineClosed = createComboBox(0)

    #TODO: mapSignal for polylines

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonPolylineClosed, comboBoxPolylineClosed)
    groupBoxMiscPolyline.setLayout(formLayout)

    return groupBoxMiscPolyline

QGroupBox* PropertyEditor::createGroupBoxTextTextSingle():
    groupBoxTextTextSingle = new QGroupBox(tr("Text"), this)

    # TODO: use proper icons
    toolButtonTextSingleContents = createToolButton("blank", tr("Contents"))
    toolButtonTextSingleFont = createToolButton("blank", tr("Font"))
    toolButtonTextSingleJustify = createToolButton("blank", tr("Justify"))
    toolButtonTextSingleHeight = createToolButton("blank", tr("Height"))
    toolButtonTextSingleRotation = createToolButton("blank", tr("Rotation"))

    lineEditTextSingleContents = createLineEdit("string", 0)
    comboBoxTextSingleFont = createFontComboBox(0)
    comboBoxTextSingleJustify = createComboBox(0)
    lineEditTextSingleHeight = createLineEdit("double", 0)
    lineEditTextSingleRotation = createLineEdit("double", 0)

    mapSignal(lineEditTextSingleContents, "lineEditTextSingleContents", OBJ_TYPE_TEXTSINGLE)
    mapSignal(comboBoxTextSingleFont, "comboBoxTextSingleFont", OBJ_TYPE_TEXTSINGLE)
    mapSignal(comboBoxTextSingleJustify, "comboBoxTextSingleJustify", OBJ_TYPE_TEXTSINGLE)
    mapSignal(lineEditTextSingleHeight, "lineEditTextSingleHeight", OBJ_TYPE_TEXTSINGLE)
    mapSignal(lineEditTextSingleRotation, "lineEditTextSingleRotation", OBJ_TYPE_TEXTSINGLE)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonTextSingleContents, lineEditTextSingleContents)
    formLayout.addRow(toolButtonTextSingleFont, comboBoxTextSingleFont)
    formLayout.addRow(toolButtonTextSingleJustify, comboBoxTextSingleJustify)
    formLayout.addRow(toolButtonTextSingleHeight, lineEditTextSingleHeight)
    formLayout.addRow(toolButtonTextSingleRotation, lineEditTextSingleRotation)
    groupBoxTextTextSingle.setLayout(formLayout)

    return groupBoxTextTextSingle

QGroupBox* PropertyEditor::createGroupBoxMiscTextSingle():
    groupBoxMiscTextSingle = new QGroupBox(tr("Misc"), this)

    toolButtonTextSingleBackward = createToolButton("blank", tr("Backward"));   #TODO: use proper icon
    toolButtonTextSingleUpsideDown = createToolButton("blank", tr("UpsideDown")); #TODO: use proper icon

    comboBoxTextSingleBackward = createComboBox(0)
    comboBoxTextSingleUpsideDown = createComboBox(0)

    mapSignal(comboBoxTextSingleBackward, "comboBoxTextSingleBackward", OBJ_TYPE_TEXTSINGLE)
    mapSignal(comboBoxTextSingleUpsideDown, "comboBoxTextSingleUpsideDown", OBJ_TYPE_TEXTSINGLE)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonTextSingleBackward, comboBoxTextSingleBackward)
    formLayout.addRow(toolButtonTextSingleUpsideDown, comboBoxTextSingleUpsideDown)
    groupBoxMiscTextSingle.setLayout(formLayout)

    return groupBoxMiscTextSingle

QToolButton* PropertyEditor::createToolButton(const QString& iconName, const QString& txt):
    QToolButton* tb = new QToolButton(this)
    tb.setIcon(loadIcon(blank_xpm))
    tb.setIconSize(QSize(iconSize, iconSize))
    tb.setText(txt)
    tb.setToolButtonStyle(propertyEditorButtonStyle)
    tb.setStyleSheet("border:none;")
    return tb

QLineEdit* PropertyEditor::createLineEdit(const QString& validatorType, int readOnly):
    QLineEdit* le = new QLineEdit(this)
    if (validatorType == "int") {
        le.setValidator(new QIntValidator(le))
    }
    elif (validatorType == "double") {
        le.setValidator(new QDoubleValidator(le))
    }
    le.setReadOnly(readOnly)
    return le

QComboBox* PropertyEditor::createComboBox(int disable):
    QComboBox* cb = new QComboBox(this)
    cb.setDisabled(disable)
    return cb

QFontComboBox* PropertyEditor::createFontComboBox(int disable):
    QFontComboBox* fcb = new QFontComboBox(this)
    fcb.setDisabled(disable)
    return fcb

def PropertyEditor::mapSignal(QObject* fieldObj, const QString& name, QVariant value):
    fieldObj.setObjectName(name)
    fieldObj.setProperty(qPrintable(name), value)

    if (name.startsWith("lineEdit")) {
        connect(fieldObj, SIGNAL(editingFinished()), signalMapper, SLOT(map()))
    }
    elif (name.startsWith("comboBox")) {
        connect(fieldObj, SIGNAL(activated(const QString&)), signalMapper, SLOT(map()))
    }

    signalMapper.setMapping(fieldObj, fieldObj)

def PropertyEditor::fieldEdited(QObject* fieldObj):
    ArcObject*  tempArcObj
    CircleObject*   tempCircleObj
    EllipseObject*  tempEllipseObj
    ImageObject*    tempImageObj
    LineObject* tempLineObj
    PathObject* tempPathObj
    PointObject*    tempPointObj
    PolygonObject*  tempPolygonObj
    PolylineObject* tempPolylineObj
    RectObject* tempRectObj
    TextSingleObject*   tempTextSingleObj

    static int blockSignals = 0
    if(blockSignals) return

    debug_message("==========Field was Edited==========")
    QString objName = fieldObj.objectName()
    int objType = fieldObj.property(qPrintable(objName)).toInt()

    foreach(QGraphicsItem* item, selectedItemList):
        if(item.type() != objType) continue

        switch(objType):
            case OBJ_TYPE_ARC:
                if(objName == "lineEditArcCenterX") {
                    tempArcObj = static_cast<ArcObject*>(item)
                    if (tempArcObj) {
                        QPointF p = tempArcObj.objectCenter()
                        p.setX(lineEdit[ARC_CENTER_X].text().toDouble())
                        tempArcObj.setPos(p)

                if(objName == "lineEditArcCenterY") {
                    tempArcObj = static_cast<ArcObject*>(item)
                    if (tempArcObj) {
                        QPointF p = tempArcObj.objectCenter()
                        p.setY(lineEdit[ARC_CENTER_Y].text().toDouble())
                        tempArcObj.setPos(p)

                if(objName == "lineEditArcRadius") {
                    tempArcObj = static_cast<ArcObject*>(item)
                    if (tempArcObj) {
                        tempArcObj.setObjectRadius(lineEdit[ARC_RADIUS].text().toDouble())

                if(objName == "lineEditArcStartAngle") {
                    tempArcObj = static_cast<ArcObject*>(item)
                    if (tempArcObj) {
                        tempArcObj.setObjectStartAngle(lineEdit[ARC_START_ANGLE].text().toDouble())

                if(objName == "lineEditArcEndAngle") {
                    tempArcObj = static_cast<ArcObject*>(item)
                    if (tempArcObj) {
                        tempArcObj.setObjectEndAngle(lineEdit[ARC_END_ANGLE].text().toDouble())

                break
            case OBJ_TYPE_BLOCK: #TODO: field editing
                break
            case OBJ_TYPE_CIRCLE:
                if(objName == "lineEditCircleCenterX") {
                    tempCircleObj = static_cast<CircleObject*>(item)
                    if (tempCircleObj) {
                        QPointF p = tempCircleObj.objectCenter()
                        p.setX(lineEdit[CIRCLE_CENTER_X].text().toDouble())
                        tempCircleObj.setPos(p)

                if(objName == "lineEditCircleCenterY") {
                    tempCircleObj = static_cast<CircleObject*>(item)
                    if (tempCircleObj) {
                        QPointF p = tempCircleObj.objectCenter()
                        p.setY(lineEdit[CIRCLE_CENTER_Y].text().toDouble())
                        tempCircleObj.setPos(p)

                if(objName == "lineEditCircleRadius") {
                    tempCircleObj = static_cast<CircleObject*>(item)
                    if (tempCircleObj) {
                        tempCircleObj.setObjectRadius(lineEdit[CIRCLE_RADIUS].text().toDouble())

                if(objName == "lineEditCircleDiameter") {
                    tempCircleObj = static_cast<CircleObject*>(item)
                    if (tempCircleObj) {
                        tempCircleObj.setObjectDiameter(lineEdit[CIRCLE_DIAMETER].text().toDouble())

                if(objName == "lineEditCircleArea") {
                    tempCircleObj = static_cast<CircleObject*>(item)
                    if(tempCircleObj) { tempCircleObj.setObjectArea(lineEdit[CIRCLE_AREA].text().toDouble()); }
                }
                if(objName == "lineEditCircleCircumference") {
                    tempCircleObj = static_cast<CircleObject*>(item)
                    if (tempCircleObj) {
                        tempCircleObj.setObjectCircumference(lineEdit[CIRCLE_CIRCUMFERENCE].text().toDouble())

                break
            case OBJ_TYPE_DIMALIGNED: #TODO: field editing
                break
            case OBJ_TYPE_DIMANGULAR: #TODO: field editing
                break
            case OBJ_TYPE_DIMARCLENGTH: #TODO: field editing
                break
            case OBJ_TYPE_DIMDIAMETER: #TODO: field editing
                break
            case OBJ_TYPE_DIMLEADER: #TODO: field editing
                break
            case OBJ_TYPE_DIMLINEAR: #TODO: field editing
                break
            case OBJ_TYPE_DIMORDINATE: #TODO: field editing
                break
            case OBJ_TYPE_DIMRADIUS: #TODO: field editing
                break
            case OBJ_TYPE_ELLIPSE:
                if(objName == "lineEditEllipseCenterX") {
                    tempEllipseObj = static_cast<EllipseObject*>(item)
                    if (tempEllipseObj) {
                        QPointF p = tempCircleObj.objectCenter()
                        p.setX(lineEdit[ELLIPSE_CENTER_X].text().toDouble())
                        tempCircleObj.setPos(p)

                if(objName == "lineEditEllipseCenterY") {
                    tempEllipseObj = static_cast<EllipseObject*>(item)
                    if (tempEllipseObj) {
                        QPointF p = tempCircleObj.objectCenter()
                        p.setY(lineEdit[ELLIPSE_CENTER_Y].text().toDouble())
                        tempCircleObj.setPos(p)

                if(objName == "lineEditEllipseRadiusMajor") {
                    tempEllipseObj = static_cast<EllipseObject*>(item)
                    if (tempEllipseObj) {
                        tempEllipseObj.setObjectRadiusMajor(lineEdit[ELLIPSE_RADIUS_MAJOR].text().toDouble())

                if(objName == "lineEditEllipseRadiusMinor") {
                    tempEllipseObj = static_cast<EllipseObject*>(item)
                    if (tempEllipseObj) {
                        tempEllipseObj.setObjectRadiusMinor(lineEdit[ELLIPSE_RADIUS_MINOR].text().toDouble())

                if(objName == "lineEditEllipseDiameterMajor") {
                    tempEllipseObj = static_cast<EllipseObject*>(item)
                    if (tempEllipseObj) {
                        tempEllipseObj.setObjectDiameterMajor(lineEdit[ELLIPSE_DIAMETER_MAJOR].text().toDouble())

                if(objName == "lineEditEllipseDiameterMinor") {
                    tempEllipseObj = static_cast<EllipseObject*>(item)
                    if (tempEllipseObj) {
                        tempEllipseObj.setObjectDiameterMinor(lineEdit[ELLIPSE_DIAMETER_MINOR].text().toDouble())

                break
            case OBJ_TYPE_IMAGE: #TODO: field editing
                break
            case OBJ_TYPE_INFINITELINE: #TODO: field editing
                break
            case OBJ_TYPE_LINE:
                if(objName == "lineEditLineStartX") {
                    tempLineObj = static_cast<LineObject*>(item)
                    if (tempLineObj) {
                        tempLineObj.setObjectX1(lineEdit[LINE_START_X].text().toDouble())
                    }
                }
                if(objName == "lineEditLineStartY") {
                    tempLineObj = static_cast<LineObject*>(item)
                    if (tempLineObj) {
                        tempLineObj.setObjectY1(-lineEdit[LINE_START_Y].text().toDouble())
                    }
                }
                if(objName == "lineEditLineEndX") {
                    tempLineObj = static_cast<LineObject*>(item)
                    if (tempLineObj) {
                        tempLineObj.setObjectX2(lineEdit[LINE_END_X].text().toDouble())
                    }
                }
                if(objName == "lineEditLineEndY") {
                    tempLineObj = static_cast<LineObject*>(item)
                    if (tempLineObj) {
                        tempLineObj.setObjectY2(-lineEdit[LINE_END_Y].text().toDouble())
                    }
                }
                break
            case OBJ_TYPE_PATH: #TODO: field editing
                break
            case OBJ_TYPE_POINT:
                if(objName == "lineEditPointX") {
                    tempPointObj = static_cast<PointObject*>(item)
                    if (tempPointObj) {
                        tempPointObj.setObjectX(lineEdit[POINT_X].text().toDouble())
                    }
                }
                if(objName == "lineEditPointY") {
                    tempPointObj = static_cast<PointObject*>(item)
                    if (tempPointObj) {
                        tempPointObj.setObjectY(-lineEdit[POINT_Y].text().toDouble())
                    }
                }
                break
            case OBJ_TYPE_POLYGON: #TODO: field editing
                break
            case OBJ_TYPE_POLYLINE: #TODO: field editing
                break
            case OBJ_TYPE_RAY: #TODO: field editing
                break
            case OBJ_TYPE_RECTANGLE: #TODO: field editing
                break
            case OBJ_TYPE_TEXTMULTI: #TODO: field editing
                break
            case OBJ_TYPE_TEXTSINGLE: #TODO: field editing
                if(objName == "lineEditTextSingleContents") {
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if (tempTextSingleObj) {
                        tempTextSingleObj.setObjectText(lineEditTextSingleContents.text())
                    }
                }
                if(objName == "comboBoxTextSingleFont") {
                    if(comboBoxTextSingleFont.currentText() == fieldVariesText) { break; }
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if(tempTextSingleObj) { tempTextSingleObj.setObjectTextFont(comboBoxTextSingleFont.currentFont().family()); } }
                if (objName == "comboBoxTextSingleJustify") {
                    if (comboBoxTextSingleJustify.currentText() == fieldVariesText) {
                        break
                    }
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if (tempTextSingleObj) {
                        tempTextSingleObj.setObjectTextJustify(comboBoxTextSingleJustify.itemData(comboBoxTextSingleJustify.currentIndex()).toString())
                    }
                }
                if(objName == "lineEditTextSingleHeight") {
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if (tempTextSingleObj) {
                        tempTextSingleObj.setObjectTextSize(lineEditTextSingleHeight.text().toDouble())
                    }
                }
                if(objName == "lineEditTextSingleRotation") {
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if (tempTextSingleObj) {
                        tempTextSingleObj.setRotation(-lineEditTextSingleRotation.text().toDouble())
                    }
                }
                if(objName == "lineEditTextSingleX") {
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if(tempTextSingleObj) { tempTextSingleObj.setObjectX(lineEditTextSingleX.text().toDouble()); } }
                if(objName == "lineEditTextSingleY") {
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if(tempTextSingleObj) { tempTextSingleObj.setObjectY(lineEditTextSingleY.text().toDouble()); } }
                if(objName == "comboBoxTextSingleBackward") {
                    if(comboBoxTextSingleBackward.currentText() == fieldVariesText) { break; }
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if(tempTextSingleObj) { tempTextSingleObj.setObjectTextBackward(comboBoxTextSingleBackward.itemData(comboBoxTextSingleBackward.currentIndex()).toBool()); } }
                if(objName == "comboBoxTextSingleUpsideDown") {
                    if(comboBoxTextSingleUpsideDown.currentText() == fieldVariesText) { break; }
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if(tempTextSingleObj) { tempTextSingleObj.setObjectTextUpsideDown(comboBoxTextSingleUpsideDown.itemData(comboBoxTextSingleUpsideDown.currentIndex()).toBool()); } }
                break
            default:
                break

    # Block this slot from running twice since calling setSelectedItems will trigger it
    blockSignals = 1

    QWidget* widget = QApplication::focusWidget()
    # Update so all fields have fresh data
    # TODO: Improve this

    setSelectedItems(selectedItemList)
    hideAllGroups()
    showGroups(objType)

    if(widget) widget.setFocus(Qt::OtherFocusReason)

    blockSignals = 0


def MainWindow::stub_testing():
    QMessageBox::warning(this, tr("Testing Feature"), tr("<b>This feature is in testing.</b>"))

def MainWindow::checkForUpdates():
    debug_message("checkForUpdates()")
    #TODO: Check website for new versions, commands, etc...
}

def MainWindow::selectAll():
    debug_message("selectAll()")
    View* gview = activeView()
    if(gview) { gview.selectAll(); }
}

QString MainWindow::platformString():
    #TODO: Append QSysInfo to string where applicable.
    QString os

#if defined(__unix__) or defined(__linux__)
    struct utsname unameData
    uname(&unameData)
    os = QString(unameData.sysname)
#else
    # Get windows version.
    os = QString("Windows")
#endif
    debug_message("Platform: %s", qPrintable(os))
    return os

def MainWindow::designDetails():
    QGraphicsScene* scene = activeScene()
    if(scene)
    {
        EmbDetailsDialog dialog(scene, this)
        dialog.exec()
    }
}

def MainWindow::whatsThisContextHelp():
    debug_message("whatsThisContextHelp()")
    QWhatsThis::enterWhatsThisMode()

def MainWindow::print():
    debug_message("print()")
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea.activeSubWindow())
    if mdiWin: mdiWin.print();

def MainWindow::tipOfTheDay():
    debug_message("tipOfTheDay()")

    QString appDir = qApp.applicationDirPath()
    wizardTipOfTheDay = new QDialog()
    QToolButton *button1 = new QToolButton(wizardTipOfTheDay)
    QToolButton *button2 = new QToolButton(wizardTipOfTheDay)
    QToolButton *button3 = new QToolButton(wizardTipOfTheDay)

    ImageWidget* imgBanner = new ImageWidget(appDir + "/images/did-you-know.png", wizardTipOfTheDay)

    QCheckBox* checkBoxTipOfTheDay = new QCheckBox(tr("&Show tips on startup"), wizardTipOfTheDay)
    checkBoxTipOfTheDay.setChecked(settings.general_tip_of_the_day)
    connect(checkBoxTipOfTheDay, SIGNAL(stateChanged(int)), this, SLOT(checkBoxTipOfTheDayStateChanged(int)))

    if (strlen(tips[settings.general_current_tip])==0) {
        settings.general_current_tip = 0
    }
    labelTipOfTheDay = new QLabel(tips[settings.general_current_tip], wizardTipOfTheDay)
    labelTipOfTheDay.setWordWrap(1)

    button1.setText("&Previous")
    button2.setText("&Next")
    button3.setText("&Close")
    connect(button1, SIGNAL(triggered()), wizardTipOfTheDay, SLOT(wizardTipOfTheDay.close()))
    connect(button2, SIGNAL(triggered()), wizardTipOfTheDay, SLOT(wizardTipOfTheDay.close()))
    connect(button3, SIGNAL(triggered()), wizardTipOfTheDay, SLOT(wizardTipOfTheDay.close()))

    QVBoxLayout* layout = new QVBoxLayout(wizardTipOfTheDay)
    layout.addWidget(imgBanner)
    layout.addStrut(1)
    layout.addWidget(labelTipOfTheDay)
    layout.addStretch(1)
    layout.addWidget(checkBoxTipOfTheDay)
    layout.addStrut(1)
    layout.addWidget(button1)
    layout.addStrut(1)
    layout.addWidget(button2)
    layout.addStrut(1)
    layout.addWidget(button3)

    wizardTipOfTheDay.setLayout(layout)
    wizardTipOfTheDay.setWindowTitle("Tip of the Day")
    wizardTipOfTheDay.setMinimumSize(550, 400)
    wizardTipOfTheDay.exec()

def MainWindow::buttonTipOfTheDayClicked(int button):
    #
    debug_message("buttonTipOfTheDayClicked(%d)", button)
    if(button == QWizard::CustomButton1)
    {
        if(settings.general_current_tip > 0)
            settings.general_current_tip--
        else
            settings.general_current_tip = listTipOfTheDay.size()-1
        labelTipOfTheDay.setText(listTipOfTheDay.value(settings.general_current_tip))
    }
    elif(button == QWizard::CustomButton2)
    {
        settings.general_current_tip++
        if(settings.general_current_tip >= listTipOfTheDay.size())
            settings.general_current_tip = 0
        labelTipOfTheDay.setText(listTipOfTheDay.value(settings.general_current_tip))
    }
    elif(button == QWizard::CustomButton3)
        wizardTipOfTheDay.close()



def MainWindow::help():
    debug_message("help()")

    # display in a custom widget instead
    # Open the HTML Help in the default browser
    QUrl helpURL("file:///" + qApp.applicationDirPath() + "/help/doc-index.html")
    QDesktopServices::openUrl(helpURL)

    #TODO: This is how to start an external program. Use this elsewhere...
    #QString program = "firefox";
    #QStringList arguments;
    #arguments << "help/commands.html";
    #QProcess *myProcess = new QProcess(this);
    #myProcess.start(program, arguments);


def MainWindow::actions():
    " this wrapper connects the signal to the C-style actuator "
    char call[100]
    QObject *obj = sender()
    caller = obj.objectName()
    for i in range(len(action_list.keys()):
        if caller == action_list[i].abbreviation:
            call[0] = (char)i
            call[1] = 0
            actuator(call)
            return

def main_undo():
    debug_message("undo()")
    if (undo_history_position > 0) {
        char *last = undo_history[undo_history_position]
        undo_history_position--
        printf("undo_history_position = %d\n", undo_history_position)
        printf("undo_history_length = %d\n", undo_history_length)

        # Create the reverse action from the last action and apply with
         * the main actuator.

        switch (last[0]) {
        case ACTION_donothing:
        default:
            debug_message("The last action has no undo candidate.")
            break
        }
        actuator(last)
    }
}

def main_redo():
    char undo_call[100]
    debug_message("redo()")
    if (undo_history_position < undo_history_length) {
        undo_history_position++
        printf("undo_history_position = %d\n", undo_history_position)
        printf("undo_history_length = %d\n", undo_history_length)
        strcpy(undo_call, undo_history[undo_history_position])
        # set reverse flag
        strcat(undo_call, " -r")
        actuator(undo_call)

int MainWindow::isShiftPressed():
    return settings.shiftKeyPressedState

def MainWindow::setShiftPressed():
    settings.shiftKeyPressedState = 1

def MainWindow::setShiftReleased():
    settings.shiftKeyPressedState = 0

# Icons
def MainWindow::iconResize(int iconSize):
    this.setIconSize(QSize(iconSize, iconSize))
    layerSelector.     setIconSize(QSize(iconSize*4, iconSize))
    colorSelector.     setIconSize(QSize(iconSize, iconSize))
    linetypeSelector.  setIconSize(QSize(iconSize*4, iconSize))
    lineweightSelector.setIconSize(QSize(iconSize*4, iconSize))
    #set the minimum combobox width so the text is always readable
    layerSelector.     setMinimumWidth(iconSize*4)
    colorSelector.     setMinimumWidth(iconSize*2)
    linetypeSelector.  setMinimumWidth(iconSize*4)
    lineweightSelector.setMinimumWidth(iconSize*4)

    # TODO: low-priority:
     * open app with iconSize set to 128. resize the icons to a smaller size.

    settings.general_icon_size = iconSize

MdiWindow* MainWindow::activeMdiWindow():
    debug_message("activeMdiWindow()")
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea.activeSubWindow())
    return mdiWin

View* MainWindow::activeView():
    debug_message("activeView()")
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea.activeSubWindow())
    if mdiWin:
        View* v = mdiWin.getView()
        return v
    return 0

QGraphicsScene* MainWindow::activeScene():
    debug_message("activeScene()")
    mdiWin = qobject_cast<MdiWindow*>(mdiArea.activeSubWindow())
    if mdiWin:
        return mdiWin.getScene()
    return 0

def MainWindow::updateAllViewScrollBars(int val):
    QList<QMdiSubWindow*> windowList = mdiArea.subWindowList()
    for(int i = 0; i < windowList.count(); ++i):
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i))
        if(mdiWin) { mdiWin.showViewScrollBars(val); }


def MainWindow::updateAllViewCrossHairColors(unsigned int color):
    QList<QMdiSubWindow*> windowList = mdiArea.subWindowList()
    for(int i = 0; i < windowList.count(); ++i)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i))
        if(mdiWin) { mdiWin.setViewCrossHairColor(color); }

def MainWindow::updateAllViewBackgroundColors(unsigned int color):
    QList<QMdiSubWindow*> windowList = mdiArea.subWindowList()
    for(int i = 0; i < windowList.count(); ++i)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i))
        if(mdiWin) { mdiWin.setViewBackgroundColor(color); }

def MainWindow::updateAllViewSelectBoxColors(unsigned int colorL, unsigned int fillL, unsigned int colorR, unsigned int fillR, int alpha):
    QList<QMdiSubWindow*> windowList = mdiArea.subWindowList()
    for(int i = 0; i < windowList.count(); ++i)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i))
        if(mdiWin) { mdiWin.setViewSelectBoxColors(colorL, fillL, colorR, fillR, alpha); }

def MainWindow::updateAllViewGridColors(unsigned int color):
    QList<QMdiSubWindow*> windowList = mdiArea.subWindowList()
    for(int i = 0; i < windowList.count(); ++i)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i))
        if(mdiWin) { mdiWin.setViewGridColor(color); }

def MainWindow::updateAllViewRulerColors(unsigned int color):
    QList<QMdiSubWindow*> windowList = mdiArea.subWindowList()
    for(int i = 0; i < windowList.count(); ++i)
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i))
        if(mdiWin) { mdiWin.setViewRulerColor(color); }

def MainWindow::updatePickAddMode(int val):
    settings.selection_mode_pickadd = val
    dockPropEdit.updatePickAddModeButton(val)

def MainWindow::pickAddModeToggled():
    int val = !settings.selection_mode_pickadd
    updatePickAddMode(val)

def MainWindow::layerSelectorIndexChanged(int index):
    debug_message("layerSelectorIndexChanged(%d)", index)

def MainWindow::colorSelectorIndexChanged(int index):
    debug_message("colorSelectorIndexChanged(%d)", index)

    QComboBox* comboBox = qobject_cast<QComboBox*>(sender())
    unsigned int newColor
    if(comboBox)
    {
        bool ok = 0
        #TODO: Handle ByLayer and ByBlock and Other...
        newColor = comboBox.itemData(index).toUInt(&ok)
        if(!ok)
            QMessageBox::warning(this, tr("Color Selector Conversion Error"), tr("<b>An error has occurred while changing colors.</b>"))
    }
    else
        QMessageBox::warning(this, tr("Color Selector Pointer Error"), tr("<b>An error has occurred while changing colors.</b>"))

    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea.activeSubWindow())
    if(mdiWin) { mdiWin.currentColorChanged(newColor); }
}

def MainWindow::linetypeSelectorIndexChanged(int index):
    debug_message("linetypeSelectorIndexChanged(%d)", index)

def MainWindow::lineweightSelectorIndexChanged(int index):
    debug_message("lineweightSelectorIndexChanged(%d)", index)

def MainWindow::textFontSelectorCurrentFontChanged(const QFont& font):
    debug_message("textFontSelectorCurrentFontChanged()")
    textFontSelector.setCurrentFont(QFont(font.family()))
    strcpy(settings.text_font, font.family().toLocal8Bit().constData())

def MainWindow::textSizeSelectorIndexChanged(int index):
    debug_message("textSizeSelectorIndexChanged(%d)", index)
    settings.text_style.size = fabs(textSizeSelector.itemData(index).toReal()); #TODO: check that the toReal() conversion is ok
}

QString MainWindow::textFont():
    return settings.text_font

def MainWindow::setTextSize(num):
    settings.text_style.size = fabs(num)
    int index = textSizeSelector.findText("Custom", Qt::MatchContains)
    if(index != -1)
        textSizeSelector.removeItem(index)
    textSizeSelector.addItem("Custom " + QString().setNum(num, 'f', 2) + " pt", num)
    index = textSizeSelector.findText("Custom", Qt::MatchContains)
    if(index != -1)
        textSizeSelector.setCurrentIndex(index)

QString MainWindow::getCurrentLayer():
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea.activeSubWindow())
    if(mdiWin) { return mdiWin.getCurrentLayer(); }
    return "0"

unsigned int MainWindow::getCurrentColor():
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea.activeSubWindow())
    if(mdiWin) { return mdiWin.getCurrentColor(); }
    return 0; #TODO: return color ByLayer

QString MainWindow::getCurrentLineType():
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea.activeSubWindow())
    if(mdiWin) { return mdiWin.getCurrentLineType(); }
    return "ByLayer"

QString MainWindow::getCurrentLineWeight():
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea.activeSubWindow())
    if(mdiWin) { return mdiWin.getCurrentLineWeight(); }
    return "ByLayer"

def MainWindow::deletePressed():
    debug_message("deletePressed()")
    QApplication::setOverrideCursor(Qt::WaitCursor)
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea.activeSubWindow())
    if(mdiWin) { mdiWin.deletePressed(); }
    QApplication::restoreOverrideCursor()

def MainWindow::escapePressed():
    debug_message("escapePressed()")
    QApplication::setOverrideCursor(Qt::WaitCursor)
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea.activeSubWindow())
    if(mdiWin) { mdiWin.escapePressed(); }
    QApplication::restoreOverrideCursor()

    gview = activeView()
    if gview:
        gview.clearRubberRoom()
        gview.previewOff()
        gview.disableMoveRapidFire()

def toggleGrid():
    debug_message("toggleGrid()")
    status_bar[STATUS_GRID].toggle()

def toggleRuler():
    debug_message("toggleRuler()")
    status_bar[STATUS_RULER].toggle()

def toggleLwt():
    debug_message("toggleLwt()")
    status_bar[STATUS_LWT].toggle()

def MainWindow::enableMoveRapidFire():
    View* gview = activeView()
    if (gview) gview.enableMoveRapidFire()

def MainWindow::disableMoveRapidFire():
    View* gview = activeView()
    if(gview) gview.disableMoveRapidFire()

def MainWindow::nativeAddTextSingle(const QString& str, x, y, rot, int fill, int rubberMode):
    View* gview = activeView()
    QGraphicsScene* gscene = gview.scene()
    if(gview and gscene)
    {
        TextSingleObject* obj = new TextSingleObject(str, x, -y, getCurrentColor())
        obj.objTextFont = settings.text_font
        obj.obj_text = settings.text_style
        obj.setObjectText(obj.objText)
        obj.setRotation(-rot)
        #TODO: single line text fill
        obj.setObjectRubberMode(rubberMode)
        if (rubberMode) {
            gview.addToRubberRoom(obj)
            gscene.addItem(obj)
            gscene.update()

def MainWindow::nativeAddLine(x1, y1, x2, y2, rot, int rubberMode):
    View* gview = activeView()
    QGraphicsScene* gscene = gview.scene()
    if(gview and gscene)
    {
        LineObject* obj = new LineObject(x1, -y1, x2, -y2, getCurrentColor())
        obj.setRotation(-rot)
        obj.setObjectRubberMode(rubberMode)
        if rubberMode:
            gview.addToRubberRoom(obj)
            gscene.addItem(obj)
            gscene.update()


def MainWindow::nativeAddRectangle(x, y, w, h, rot, int fill, int rubberMode):
    View* gview = activeView()
    QGraphicsScene* gscene = gview.scene()
    if(gview and gscene)
    {
        RectObject* obj = new RectObject(x, -y, w, -h, getCurrentColor())
        obj.setRotation(-rot)
        obj.setObjectRubberMode(rubberMode)
        #TODO: rect fill
        if (rubberMode) {
            gview.addToRubberRoom(obj)
            gscene.addItem(obj)
            gscene.update()

def MainWindow::nativeAddArc(startX, startY, midX, midY, endX, endY, int rubberMode):
    View* gview = activeView()
    QGraphicsScene* scene = activeScene()
    if(gview and scene)
    {
        ArcObject* arcObj = new ArcObject(startX, -startY, midX, -midY, endX, -endY, getCurrentColor())
        arcObj.setObjectRubberMode(rubberMode)
        if(rubberMode) gview.addToRubberRoom(arcObj)
        scene.addItem(arcObj)
        scene.update()

def MainWindow::nativeAddCircle(centerX, centerY, radius, int fill, int rubberMode):
    View* gview = activeView()
    QGraphicsScene* gscene = gview.scene()
    if (gview and gscene) {
        CircleObject* obj = new CircleObject(centerX, -centerY, radius, getCurrentColor())
        obj.setObjectRubberMode(rubberMode)
        #TODO: circle fill
        if rubberMode:
            gview.addToRubberRoom(obj)
            gscene.addItem(obj)
            gscene.update()


def MainWindow::nativeAddEllipse(centerX, centerY, width, height, rot, int fill, int rubberMode):
    View* gview = activeView()
    QGraphicsScene* gscene = gview.scene()
    if (gview and gscene) {
        EllipseObject* obj = new EllipseObject(centerX, -centerY, width, height, getCurrentColor())
        obj.setRotation(-rot)
        obj.setObjectRubberMode(rubberMode)
        #TODO: ellipse fill
        if rubberMode:
            gview.addToRubberRoom(obj)
            gscene.addItem(obj)
            gscene.update()


def MainWindow::nativeAddPoint(x, y):
    gview = activeView()
    if gview:
        obj = new PointObject(x, -y, getCurrentColor())


#NOTE: This native is different than the rest in that the Y+ is down (scripters need not worry about this)
def MainWindow::nativeAddPolygon(startX, startY, const QPainterPath& p, rubberMode):
    gview = activeView()
    QGraphicsScene* gscene = gview.scene()
    if (gview and gscene) {
        PolygonObject* obj = new PolygonObject(startX, startY, p, getCurrentColor())
        obj.setObjectRubberMode(rubberMode)
        if(rubberMode)
            gview.addToRubberRoom(obj)
            gscene.addItem(obj)
            gscene.update()
        else:


#NOTE: This native is different than the rest in that the Y+ is down (scripters need not worry about this)
def MainWindow::nativeAddPolyline(startX, startY, const QPainterPath& p, rubberMode):
    gview = activeView()
    QGraphicsScene* gscene = gview.scene()
    if(gview and gscene)
        PolylineObject* obj = new PolylineObject(startX, startY, p, getCurrentColor())
        obj.setObjectRubberMode(rubberMode)
        if(rubberMode)
            gview.addToRubberRoom(obj)
            gscene.addItem(obj)
            gscene.update()
        else:


def MainWindow::nativeAddDimLeader(x1, y1, x2, y2, rot, rubberMode):
    View* gview = activeView()
    QGraphicsScene* gscene = gview.scene()
    if(gview and gscene) {
        DimLeaderObject* obj = new DimLeaderObject(x1, -y1, x2, -y2, getCurrentColor())
        obj.setRotation(-rot)
        obj.setObjectRubberMode(rubberMode)
        if(rubberMode)
        {
            gview.addToRubberRoom(obj)
            gscene.addItem(obj)
            gscene.update()

MainWindow::nativeCalculateAngle(x1, y1, x2, y2):
    return QLineF(x1, -y1, x2, -y2).angle()

MainWindow::nativeCalculateDistance(x1, y1, x2, y2):
    return QLineF(x1, y1, x2, y2).length()

def MainWindow::fill_menu(menu_id):
    i
    debug_message("MainWindow creating %s", menu_label[menu_id])
    menuBar().addMenu(menu[menu_id])
    for (i=0; menus[menu_id][i]>=-1; i++) {
        if (menus[menu_id][i] >= 0) {
            menu[menu_id].addAction(actionHash.value(menus[menu_id][i]))
        }
        else {
            menu[menu_id].addSeparator()

# nativePerpendicularDistance
    This is currently causing a bug and is going to be replaced with a libembroidery function.
    QLineF line(x1, y1, x2, y2)
    QLineF norm = line.normalVector()
    dx = px-x1
    dy = py-y1
    norm.translate(dx, dy)
    QPointF iPoint
    norm.intersects(line, &iPoint)
    return QLineF(px, py, iPoint.x(), iPoint.y()).length()


MainWindow::MainWindow() : QMainWindow(0):
    char current_path[1000]
    i

    QString appDir = qApp.applicationDirPath()
    readSettings()

    for (i=0; i<nFolders; i++) {
        app_dir(current_path, i)
        if (!file_exists) {
            QMessageBox::critical(this, tr("Path Error"), tr("Cannot locate: ") + current_path)
        }
    }

    QString lang = settings.general_language
    qDebug("language: %s", qPrintable(lang))
    if(lang == "system")
        lang = QLocale::system().languageToString(QLocale::system().language()).toLower()

    #Load translations for the Embroidermodder 2 GUI
    QTranslator translatorEmb
    app_dir(current_path, translations_folder)
    translatorEmb.load(QString(current_path) + "/embroidermodder2_" + lang)
    qApp.installTranslator(&translatorEmb)

    #Load translations for the commands
    QTranslator translatorCmd
    translatorCmd.load(QDir::toNativeSeparators(QString(current_path) + lang + "/commands_" + lang))
    qApp.installTranslator(&translatorCmd)

    #Load translations provided by Qt - this covers dialog buttons and other common things.
    QTranslator translatorQt
    translatorQt.load("qt_" + QLocale::system().name(), QLibraryInfo::location(QLibraryInfo::TranslationsPath)); #TODO: ensure this always loads, ship a copy of this with the app
    qApp.installTranslator(&translatorQt)

    #Init
    mainWin = this
    for (i=0; i<N_MENUS; i++) {
        menu[i] = new QMenu(tr(menu_label[i]), this)
    }
    for (i=0; i<N_TOOLBARS; i++) {
        toolbar[i] = addToolBar(tr(toolbar_label[i]))
    }
    #Selectors
    layerSelector = new QComboBox(this)
    colorSelector = new QComboBox(this)
    linetypeSelector = new QComboBox(this)
    lineweightSelector = new QComboBox(this)
    textFontSelector = new QFontComboBox(this)
    textSizeSelector = new QComboBox(this)

    numOfDocs = 0
    docIndex = 0

    settings.shiftKeyPressedState = 0

    setWindowIcon(loadIcon(app_xpm))
    setMinimumSize(800, 480); #Require Minimum WVGA

    loadFormats()

    #create the mdiArea
    QFrame* vbox = new QFrame(this)
    QVBoxLayout* layout = new QVBoxLayout(vbox)
    layout.setContentsMargins(QMargins())
    vbox.setFrameStyle(QFrame::StyledPanel | QFrame::Sunken)
    mdiArea = new MdiArea(this, vbox)
    mdiArea.useBackgroundLogo(settings.general_mdi_bg_use_logo)
    mdiArea.useBackgroundTexture(settings.general_mdi_bg_use_texture)
    mdiArea.useBackgroundColor(settings.general_mdi_bg_use_color)
    mdiArea.setBackgroundLogo(settings.general_mdi_bg_logo)
    mdiArea.setBackgroundTexture(settings.general_mdi_bg_texture)
    mdiArea.setBackgroundColor(QColor(settings.general_mdi_bg_color))
    mdiArea.setViewMode(QMdiArea::TabbedView)
    mdiArea.setHorizontalScrollBarPolicy(Qt::ScrollBarAsNeeded)
    mdiArea.setVerticalScrollBarPolicy(Qt::ScrollBarAsNeeded)
    mdiArea.setActivationOrder(QMdiArea::ActivationHistoryOrder)
    layout.addWidget(mdiArea)
    setCentralWidget(vbox)

    #setDockOptions(QMainWindow::AnimatedDocks | QMainWindow::AllowTabbedDocks | QMainWindow::VerticalTabs);
    # TODO: Load these from settings
    # tabifyDockWidget(dockPropEdit, dockUndoEdit);
    # TODO: load this from settings

    statusbar = new StatusBar(this, this)
    this.setStatusBar(statusbar)

    debug_message("Creating All Actions...")
    QString appName = QApplication::applicationName()

    for (i=0; action_list[i].abbreviation[0]; i++) {
        QAction *ACTION = new QAction(loadIcon((*)action_list[i].icon), action_list[i].menu_name, this)
        # TODO: Set What's This Context Help to statusTip for now so there is some infos there.
        # Make custom What's This Context Help popup with more descriptive help than just
        # the status bar/tip one liner(short but not real long) with a hyperlink in the custom popup
        # at the bottom to open full help file description. Ex: like wxPython AGW's SuperToolTip.
        # TODO: Finish All Commands ... <.<

        #
        if(icon == "windowcascade") {
            connect(ACTION, SIGNAL(triggered()), mdiArea, SLOT(cascade()))
        }
        elif(icon == "windowtile") {
            connect(ACTION, SIGNAL(triggered()), mdiArea, SLOT(tile()))
        }
        elif(icon == "windowclose") {
            ACTION.setShortcut(QKeySequence::Close)
            connect(ACTION, SIGNAL(triggered()), this, SLOT(onCloseWindow()))
        }
        elif(icon == "windowcloseall") {
            connect(ACTION, SIGNAL(triggered()), mdiArea, SLOT(closeAllSubWindows()))
        }
        elif(icon == "windownext") {
            connect(ACTION, SIGNAL(triggered()), mdiArea, SLOT(activateNextSubWindow()))
        }
        elif(icon == "windowprevious") {
            connect(ACTION, SIGNAL(triggered()), mdiArea, SLOT(activatePreviousSubWindow()))
        }
        elif(icon == "textbold" or icon == "textitalic"
            or icon == "textunderline" or icon == "textstrikeout"
            or icon == "textoverline") {
            ACTION.setCheckable(1)
        }


        if (strlen(action_list[i].shortcut)>0) {
            ACTION.setShortcut(QKeySequence(action_list[i].shortcut))
        }
        ACTION.setStatusTip(action_list[i].description)
        ACTION.setObjectName(action_list[i].abbreviation)
        ACTION.setWhatsThis(action_list[i].description)
        connect(ACTION, SIGNAL(triggered()), this, SLOT(actions()))
        actionHash.insert(i, ACTION)
    }

    actionHash.value(ACTION_windowclose).setEnabled(numOfDocs > 0)
    actionHash.value(ACTION_designdetails).setEnabled(numOfDocs > 0)

    # ----

    debug_message("MainWindow createAllMenus()")

    debug_message("MainWindow createFileMenu()")
    menuBar().addMenu(menu[FILE_MENU])
    menu[FILE_MENU].addAction(actionHash.value(ACTION_new))
    menu[FILE_MENU].addSeparator()
    menu[FILE_MENU].addAction(actionHash.value(ACTION_open))

    menu[FILE_MENU].addMenu(menu[RECENT_MENU])
    connect(menu[RECENT_MENU], SIGNAL(aboutToShow()), this, SLOT(recentMenuAboutToShow()))
    # Do not allow the Recent Menu to be torn off. It's a pain in the ass to maintain.
    menu[RECENT_MENU].setTearOffEnabled(0)

    menu[FILE_MENU].addSeparator()
    menu[FILE_MENU].addAction(actionHash.value(ACTION_save))
    menu[FILE_MENU].addAction(actionHash.value(ACTION_saveas))
    menu[FILE_MENU].addSeparator()
    menu[FILE_MENU].addAction(actionHash.value(ACTION_print))
    menu[FILE_MENU].addSeparator()
    menu[FILE_MENU].addAction(actionHash.value(ACTION_windowclose))
    menu[FILE_MENU].addSeparator()
    menu[FILE_MENU].addAction(actionHash.value(ACTION_designdetails))
    menu[FILE_MENU].addSeparator()

    menu[FILE_MENU].addAction(actionHash.value(ACTION_exit))
    menu[FILE_MENU].setTearOffEnabled(0)

    # ----

    debug_message("MainWindow createmenu[EDIT_MENU]()")
    menuBar().addMenu(menu[EDIT_MENU])
    menu[EDIT_MENU].addAction(actionHash.value(ACTION_undo))
    menu[EDIT_MENU].addAction(actionHash.value(ACTION_redo))
    menu[EDIT_MENU].addSeparator()
    menu[EDIT_MENU].addAction(actionHash.value(ACTION_cut))
    menu[EDIT_MENU].addAction(actionHash.value(ACTION_copy))
    menu[EDIT_MENU].addAction(actionHash.value(ACTION_paste))
    menu[EDIT_MENU].addSeparator()
    menu[EDIT_MENU].setTearOffEnabled(1)

    # ----

    debug_message("MainWindow createmenu[VIEW_MENU]()")

    menuBar().addMenu(menu[VIEW_MENU])
    menu[VIEW_MENU].addSeparator()
    menu[VIEW_MENU].addMenu(menu[ZOOM_MENU])
    menu[ZOOM_MENU].setIcon(loadIcon(zoom_xpm))
    menu[ZOOM_MENU].addAction(actionHash.value(ACTION_zoomrealtime))
    menu[ZOOM_MENU].addAction(actionHash.value(ACTION_zoomprevious))
    menu[ZOOM_MENU].addSeparator()
    menu[ZOOM_MENU].addAction(actionHash.value(ACTION_zoomwindow))
    menu[ZOOM_MENU].addAction(actionHash.value(ACTION_zoomdynamic))
    menu[ZOOM_MENU].addAction(actionHash.value(ACTION_zoomscale))
    menu[ZOOM_MENU].addAction(actionHash.value(ACTION_zoomcenter))
    menu[ZOOM_MENU].addSeparator()
    menu[ZOOM_MENU].addAction(actionHash.value(ACTION_zoomin))
    menu[ZOOM_MENU].addAction(actionHash.value(ACTION_zoomout))
    menu[ZOOM_MENU].addSeparator()
    menu[ZOOM_MENU].addAction(actionHash.value(ACTION_zoomselected))
    menu[ZOOM_MENU].addAction(actionHash.value(ACTION_zoomall))
    menu[ZOOM_MENU].addAction(actionHash.value(ACTION_zoomextents))
    menu[VIEW_MENU].addMenu(menu[PAN_MENU])
    menu[PAN_MENU].setIcon(loadIcon(pan_xpm))
    menu[PAN_MENU].addAction(actionHash.value(ACTION_panrealtime))
    menu[PAN_MENU].addAction(actionHash.value(ACTION_panpoint))
    menu[PAN_MENU].addSeparator()
    menu[PAN_MENU].addAction(actionHash.value(ACTION_panleft))
    menu[PAN_MENU].addAction(actionHash.value(ACTION_panright))
    menu[PAN_MENU].addAction(actionHash.value(ACTION_panup))
    menu[PAN_MENU].addAction(actionHash.value(ACTION_pandown))
    menu[VIEW_MENU].addSeparator()
    menu[VIEW_MENU].addAction(actionHash.value(ACTION_day))
    menu[VIEW_MENU].addAction(actionHash.value(ACTION_night))
    menu[VIEW_MENU].addSeparator()

    menu[VIEW_MENU].setTearOffEnabled(1)
    menu[ZOOM_MENU].setTearOffEnabled(1)
    menu[PAN_MENU].setTearOffEnabled(1)

    # ----

    debug_message("MainWindow createSettingsMenu()")
    menuBar().addMenu(menu[SETTINGS_MENU])
    menu[SETTINGS_MENU].addAction(actionHash.value(ACTION_settingsdialog))
    menu[SETTINGS_MENU].addSeparator()
    menu[SETTINGS_MENU].setTearOffEnabled(1)

    # ----

    debug_message("MainWindow createWindowMenu()")
    menuBar().addMenu(menu[WINDOW_MENU])
    connect(menu[WINDOW_MENU], SIGNAL(aboutToShow()), this, SLOT(windowMenuAboutToShow()))
    #Do not allow the Window Menu to be torn off. It's a pain in the ass to maintain.
    menu[WINDOW_MENU].setTearOffEnabled(0)

    # ----

    debug_message("MainWindow createHelpMenu()")
    menuBar().addMenu(menu[HELP_MENU])
    menu[HELP_MENU].addAction(actionHash.value(ACTION_help))
    menu[HELP_MENU].addSeparator()
    menu[HELP_MENU].addAction(actionHash.value(ACTION_changelog))
    menu[HELP_MENU].addSeparator()
    menu[HELP_MENU].addAction(actionHash.value(ACTION_tipoftheday))
    menu[HELP_MENU].addSeparator()
    menu[HELP_MENU].addAction(actionHash.value(ACTION_about))
    menu[HELP_MENU].addSeparator()
    menu[HELP_MENU].addAction(actionHash.value(ACTION_whatsthis))
    menu[HELP_MENU].setTearOffEnabled(1)

    # ----

    debug_message("MainWindow createAllToolbars()")

    for (i=0; i<N_TOOLBARS; i++) {
        j
        char message[100]
        sprintf(message, "MainWindow creating %s\n", toolbar_label[i])
        debug_message(message)

        toolbar[i].setObjectName(toolbar_label[i])

        for (j=0; toolbars[i][j]!=-2; j++) {
            if (toolbars[i][j] >= 0) {
                toolbar[i].addAction(actionHash.value(toolbars[i][j]))
            }
            else {
                toolbar[i].addSeparator()
            }
        }

        connect(toolbar[i], SIGNAL(topLevelChanged(int)), this, SLOT(floatingChangedToolBar(int)))
    }

    # ---------

    debug_message("MainWindow createLayerToolbar()")

    toolbar[TOOLBAR_LAYER].setObjectName("toolbarLayer")
    toolbar[TOOLBAR_LAYER].addAction(actionHash.value(ACTION_makelayercurrent))
    toolbar[TOOLBAR_LAYER].addAction(actionHash.value(ACTION_layers))

    #NOTE: Qt4.7 wont load icons without an extension...
    #TODO: Create layer pixmaps by concatenating several icons
    layerSelector.addItem(loadIcon(linetypebylayer_xpm), "0")
    layerSelector.addItem(loadIcon(linetypebylayer_xpm), "1")
    layerSelector.addItem(loadIcon(linetypebylayer_xpm), "2")
    layerSelector.addItem(loadIcon(linetypebylayer_xpm), "3")
    layerSelector.addItem(loadIcon(linetypebylayer_xpm), "4")
    layerSelector.addItem(loadIcon(linetypebylayer_xpm), "5")
    layerSelector.addItem(loadIcon(linetypebylayer_xpm), "6")
    layerSelector.addItem(loadIcon(linetypebylayer_xpm), "7")
    layerSelector.addItem(loadIcon(linetypebylayer_xpm), "8")
    layerSelector.addItem(loadIcon(linetypebylayer_xpm), "9")
    toolbar[TOOLBAR_LAYER].addWidget(layerSelector)
    connect(layerSelector, SIGNAL(currentIndexChanged(int)), this, SLOT(layerSelectorIndexChanged(int)))

    toolbar[TOOLBAR_LAYER].addAction(actionHash.value(ACTION_layerprevious))

    connect(toolbar[TOOLBAR_LAYER], SIGNAL(topLevelChanged(int)), this, SLOT(floatingChangedToolBar(int)))

    # ------

    debug_message("MainWindow createPropertiesToolbar()")

    toolbar[TOOLBAR_PROPERTIES].setObjectName("toolbarProperties")

    colorSelector.setFocusProxy(menu[FILE_MENU])
    #NOTE: Qt4.7 wont load icons without an extension...
    colorSelector.addItem(loadIcon(colorbylayer_xpm), "ByLayer")
    colorSelector.addItem(loadIcon(colorbyblock_xpm), "ByBlock")
    colorSelector.addItem(loadIcon(colorred_xpm), tr("Red"), qRgb(255, 0, 0))
    colorSelector.addItem(loadIcon(coloryellow_xpm), tr("Yellow"), qRgb(255,255, 0))
    colorSelector.addItem(loadIcon(colorgreen_xpm), tr("Green"), qRgb(0, 255, 0))
    colorSelector.addItem(loadIcon(colorcyan_xpm), tr("Cyan"), qRgb(  0,255,255))
    colorSelector.addItem(loadIcon(colorblue_xpm), tr("Blue"), qRgb(  0, 0,255))
    colorSelector.addItem(loadIcon(colormagenta_xpm), tr("Magenta"), qRgb(255, 0,255))
    colorSelector.addItem(loadIcon(colorwhite_xpm), tr("White"), qRgb(255,255,255))
    colorSelector.addItem(loadIcon(colorother_xpm), tr("Other..."))
    toolbar[TOOLBAR_PROPERTIES].addWidget(colorSelector)
    connect(colorSelector, SIGNAL(currentIndexChanged(int)), this, SLOT(colorSelectorIndexChanged(int)))

    toolbar[TOOLBAR_PROPERTIES].addSeparator()
    linetypeSelector.setFocusProxy(menu[FILE_MENU])
    #NOTE: Qt4.7 wont load icons without an extension...
    linetypeSelector.addItem(loadIcon(linetypebylayer_xpm), "ByLayer")
    linetypeSelector.addItem(loadIcon(linetypebyblock_xpm), "ByBlock")
    linetypeSelector.addItem(loadIcon(linetypecontinuous_xpm), "Continuous")
    linetypeSelector.addItem(loadIcon(linetypehidden_xpm), "Hidden")
    linetypeSelector.addItem(loadIcon(linetypecenter_xpm), "Center")
    linetypeSelector.addItem(loadIcon(linetypeother_xpm), "Other...")
    toolbar[TOOLBAR_PROPERTIES].addWidget(linetypeSelector)
    connect(linetypeSelector, SIGNAL(currentIndexChanged(int)), this, SLOT(linetypeSelectorIndexChanged(int)))

    toolbar[TOOLBAR_PROPERTIES].addSeparator()
    lineweightSelector.setFocusProxy(menu[FILE_MENU])
    #NOTE: Qt4.7 wont load icons without an extension...
    lineweightSelector.addItem(loadIcon(lineweightbylayer_xpm), "ByLayer", -2.00)
    lineweightSelector.addItem(loadIcon(lineweightbyblock_xpm), "ByBlock", -1.00)
    lineweightSelector.addItem(loadIcon(lineweightdefault_xpm), "Default", 0.00)
    # TODO: Thread weight is weird. See http://en.wikipedia.org/wiki/Thread_(yarn)#Weight
    lineweightSelector.addItem(loadIcon(lineweight01_xpm), "0.00 mm", 0.00)
    lineweightSelector.addItem(loadIcon(lineweight02_xpm), "0.05 mm", 0.05)
    lineweightSelector.addItem(loadIcon(lineweight03_xpm), "0.15 mm", 0.15)
    lineweightSelector.addItem(loadIcon(lineweight04_xpm), "0.20 mm", 0.20)
    lineweightSelector.addItem(loadIcon(lineweight05_xpm), "0.25 mm", 0.25)
    lineweightSelector.addItem(loadIcon(lineweight06_xpm), "0.30 mm", 0.30)
    lineweightSelector.addItem(loadIcon(lineweight07_xpm), "0.35 mm", 0.35)
    lineweightSelector.addItem(loadIcon(lineweight08_xpm), "0.40 mm", 0.40)
    lineweightSelector.addItem(loadIcon(lineweight09_xpm), "0.45 mm", 0.45)
    lineweightSelector.addItem(loadIcon(lineweight10_xpm), "0.50 mm", 0.50)
    lineweightSelector.addItem(loadIcon(lineweight11_xpm), "0.55 mm", 0.55)
    lineweightSelector.addItem(loadIcon(lineweight12_xpm), "0.60 mm", 0.60)
    lineweightSelector.addItem(loadIcon(lineweight13_xpm), "0.65 mm", 0.65)
    lineweightSelector.addItem(loadIcon(lineweight14_xpm), "0.70 mm", 0.70)
    lineweightSelector.addItem(loadIcon(lineweight15_xpm), "0.75 mm", 0.75)
    lineweightSelector.addItem(loadIcon(lineweight16_xpm), "0.80 mm", 0.80)
    lineweightSelector.addItem(loadIcon(lineweight17_xpm), "0.85 mm", 0.85)
    lineweightSelector.addItem(loadIcon(lineweight18_xpm), "0.90 mm", 0.90)
    lineweightSelector.addItem(loadIcon(lineweight19_xpm), "0.95 mm", 0.95)
    lineweightSelector.addItem(loadIcon(lineweight20_xpm), "1.00 mm", 1.00)
    lineweightSelector.addItem(loadIcon(lineweight21_xpm), "1.05 mm", 1.05)
    lineweightSelector.addItem(loadIcon(lineweight22_xpm), "1.10 mm", 1.10)
    lineweightSelector.addItem(loadIcon(lineweight23_xpm), "1.15 mm", 1.15)
    lineweightSelector.addItem(loadIcon(lineweight24_xpm), "1.20 mm", 1.20)
    lineweightSelector.setMinimumContentsLength(8)
    # Prevent dropdown text readability being squish...d.
    toolbar[TOOLBAR_PROPERTIES].addWidget(lineweightSelector)
    connect(lineweightSelector, SIGNAL(currentIndexChanged(int)), this, SLOT(lineweightSelectorIndexChanged(int)))

    connect(toolbar[TOOLBAR_PROPERTIES], SIGNAL(topLevelChanged(int)), this, SLOT(floatingChangedToolBar(int)))

    # ------

    debug_message("MainWindow createTextToolbar()")

    toolbar[TOOLBAR_TEXT].setObjectName("toolbarText")

    toolbar[TOOLBAR_TEXT].addWidget(textFontSelector)
    textFontSelector.setCurrentFont(QFont(settings.text_font))
    connect(textFontSelector, SIGNAL(currentFontChanged(const QFont&)), this, SLOT(textFontSelectorCurrentFontChanged(const QFont&)))

# TODO: SEGFAULTING FOR SOME REASON
    toolbar[TOOLBAR_TEXT].addAction(actionHash.value(ACTION_textbold))
    actionHash.value(ACTION_textbold).setChecked(settings.text_style_bold)
    toolbar[TOOLBAR_TEXT].addAction(actionHash.value(ACTION_textitalic))
    actionHash.value(ACTION_textitalic).setChecked(settings.text_style_italic)
    toolbar[TOOLBAR_TEXT].addAction(actionHash.value(ACTION_textunderline))
    actionHash.value(ACTION_textunderline).setChecked(settings.text_style_underline)
    toolbar[TOOLBAR_TEXT].addAction(actionHash.value(ACTION_textstrikeout))
    actionHash.value(ACTION_textstrikeout).setChecked(settings.text_style_strikeout)
    toolbar[TOOLBAR_TEXT].addAction(actionHash.value(ACTION_textoverline))
    actionHash.value(ACTION_textoverline).setChecked(settings.text_style_overline)

    textSizeSelector.setFocusProxy(menu[FILE_MENU])
    textSizeSelector.addItem("6 pt", 6)
    textSizeSelector.addItem("8 pt", 8)
    textSizeSelector.addItem("9 pt", 9)
    textSizeSelector.addItem("10 pt", 10)
    textSizeSelector.addItem("11 pt", 11)
    textSizeSelector.addItem("12 pt", 12)
    textSizeSelector.addItem("14 pt", 14)
    textSizeSelector.addItem("18 pt", 18)
    textSizeSelector.addItem("24 pt", 24)
    textSizeSelector.addItem("30 pt", 30)
    textSizeSelector.addItem("36 pt", 36)
    textSizeSelector.addItem("48 pt", 48)
    textSizeSelector.addItem("60 pt", 60)
    textSizeSelector.addItem("72 pt", 72)
    setTextSize(settings.text_size)
    toolbar[TOOLBAR_TEXT].addWidget(textSizeSelector)
    connect(textSizeSelector, SIGNAL(currentIndexChanged(int)), this, SLOT(textSizeSelectorIndexChanged(int)))


    connect(toolbar[TOOLBAR_TEXT], SIGNAL(topLevelChanged(int)), this, SLOT(floatingChangedToolBar(int)))

    # -----

    # Horizontal
    toolbar[TOOLBAR_VIEW].setOrientation(Qt::Horizontal)
    toolbar[TOOLBAR_ZOOM].setOrientation(Qt::Horizontal)
    toolbar[TOOLBAR_LAYER].setOrientation(Qt::Horizontal)
    toolbar[TOOLBAR_PROPERTIES].setOrientation(Qt::Horizontal)
    toolbar[TOOLBAR_TEXT].setOrientation(Qt::Horizontal)
    # Top
    addToolBarBreak(Qt::TopToolBarArea)
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_FILE])
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_EDIT])
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_HELP])
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_ICON])
    addToolBarBreak(Qt::TopToolBarArea)
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_ZOOM])
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_PAN])
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_VIEW])
    addToolBarBreak(Qt::TopToolBarArea)
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_LAYER])
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_PROPERTIES])
    addToolBarBreak(Qt::TopToolBarArea)
    addToolBar(Qt::TopToolBarArea, toolbar[TOOLBAR_TEXT])

    #zoomToolBar.setToolButtonStyle(Qt::ToolButtonTextOnly);
    # ----

    iconResize(settings.general_icon_size)
    updateMenuToolbarStatusbar()

    # Show date in statusbar after it has been updated
     * TODO: Switch to ISO dates.

    QDate date = QDate::currentDate()
    QString datestr = date.toString("MMMM d, yyyy")
    statusbar.showMessage(datestr)

    showNormal()

    if (settings.general_tip_of_the_day) {
        tipOfTheDay()
    }
}

MainWindow::~MainWindow():
    debug_message("MainWindow::Destructor()")

    #Prevent memory leaks by deleting any unpasted objects
    qDeleteAll(cutCopyObjectList.begin(), cutCopyObjectList.end())
    cutCopyObjectList.clear()

def MainWindow::recentMenuAboutToShow():
    debug_message("MainWindow::recentMenuAboutToShow()")
    menu[RECENT_MENU].clear()

    QFileInfo recentFileInfo
    QString recentValue
    for(i = 0; i < opensave_recent_list_of_files.size(); ++i)
    {
        #If less than the max amount of entries add to menu
        if(i < settings.opensave_recent_max_files)
        {
            recentFileInfo = QFileInfo(opensave_recent_list_of_files.at(i))
            if(recentFileInfo.exists() and validFileFormat(recentFileInfo.fileName()))
            {
                recentValue.setNum(i+1)
                QAction* rAction
                if     (recentValue.toInt() >= 1 and recentValue.toInt() <= 9) rAction = new QAction("&" + recentValue + " " + recentFileInfo.fileName(), this)
                elif(recentValue.toInt() == 10)                            rAction = new QAction("1&0 "                  + recentFileInfo.fileName(), this)
                else                                                          rAction = new QAction(      recentValue + " " + recentFileInfo.fileName(), this)
                rAction.setCheckable(0)
                rAction.setData(opensave_recent_list_of_files.at(i))
                menu[RECENT_MENU].addAction(rAction)
                connect(rAction, SIGNAL(triggered()), this, SLOT(openrecentfile()))

    #Ensure the list only has max amount of entries
    while(opensave_recent_list_of_files.size() > settings.opensave_recent_max_files) {
        opensave_recent_list_of_files.removeLast()


def MainWindow::windowMenuAboutToShow():
    debug_message("MainWindow::windowMenuAboutToShow()")
    menu[WINDOW_MENU].clear()
    menu[WINDOW_MENU].addAction(actionHash.value(ACTION_windowclose))
    menu[WINDOW_MENU].addAction(actionHash.value(ACTION_windowcloseall))
    menu[WINDOW_MENU].addSeparator()
    menu[WINDOW_MENU].addAction(actionHash.value(ACTION_windowcascade))
    menu[WINDOW_MENU].addAction(actionHash.value(ACTION_windowtile))
    menu[WINDOW_MENU].addSeparator()
    menu[WINDOW_MENU].addAction(actionHash.value(ACTION_windownext))
    menu[WINDOW_MENU].addAction(actionHash.value(ACTION_windowprevious))

    menu[WINDOW_MENU].addSeparator()
    QList<QMdiSubWindow*> windows = mdiArea.subWindowList()
    for(i = 0; i < windows.count(); ++i)
    {
        QAction* aAction = new QAction(windows.at(i).windowTitle(), this)
        aAction.setCheckable(1)
        aAction.setData(i)
        menu[WINDOW_MENU].addAction(aAction)
        connect(aAction, SIGNAL(toggled(int)), this, SLOT(windowMenuActivated(int)))
        aAction.setChecked(mdiArea.activeSubWindow() == windows.at(i))
    }
}

def MainWindow::windowMenuActivated(checked):
    debug_message("MainWindow::windowMenuActivated()")
    QAction* aSender = qobject_cast<QAction*>(sender())
    if(!aSender)
        return
    QWidget* w = mdiArea.subWindowList().at(aSender.data().toInt())
    if(w and checked)
        w.setFocus()

def MainWindow::newFile():
    debug_message("MainWindow::newFile()")
    docIndex++
    numOfDocs++
    MdiWindow* mdiWin = new MdiWindow(docIndex, mainWin, mdiArea, Qt::SubWindow)
    connect(mdiWin, SIGNAL(sendCloseMdiWin(MdiWindow*)), this, SLOT(onCloseMdiWin(MdiWindow*)))
    connect(mdiArea, SIGNAL(subWindowActivated(QMdiSubWindow*)), this, SLOT(onWindowActivated(QMdiSubWindow*)))

    updateMenuToolbarStatusbar()
    windowMenuAboutToShow()

    View* v = mdiWin.getView()
    if(v)
    {
        v.recalculateLimits()
        v.zoomExtents()
    }
}

def MainWindow::openFile(recent, const QString& recentFile):
    debug_message("MainWindow::openFile()")

    QApplication::setOverrideCursor(Qt::ArrowCursor)

    QStringList files
    preview = settings.opensave_open_thumbnail
    openFilesPath = settings.opensave_recent_directory

    #Check to see if this from the recent files list
    if(recent)
    {
        files.append(recentFile)
        openFilesSelected(files)
    }
    elif(!preview)
    {
        #TODO: set getOpenFileNames' selectedFilter parameter from settings.opensave_open_format
        files = QFileDialog::getOpenFileNames(this, tr("Open"), openFilesPath, formatFilterOpen)
        openFilesSelected(files)
    }
    elif(preview)
    {
        PreviewDialog* openDialog = new PreviewDialog(this, tr("Open w/Preview"), openFilesPath, formatFilterOpen)
        #TODO: set openDialog.selectNameFilter(const QString& filter) from settings.opensave_open_format
        connect(openDialog, SIGNAL(filesSelected(const QStringList&)), this, SLOT(openFilesSelected(const QStringList&)))
        openDialog.exec()
    }

    QApplication::restoreOverrideCursor()

def MainWindow::openFilesSelected(const QStringList& filesToOpen):
    doOnce = 1

    if(filesToOpen.count())
    {
        for(i = 0; i < filesToOpen.count(); i++)
        {
            if(!validFileFormat(filesToOpen[i]))
                continue

            QMdiSubWindow* existing = findMdiWindow(filesToOpen[i])
            if(existing)
            {
                mdiArea.setActiveSubWindow(existing)
                continue
            }

            #The docIndex doesn't need increased as it is only used for unnamed files
            numOfDocs++
            MdiWindow* mdiWin = new MdiWindow(docIndex, mainWin, mdiArea, Qt::SubWindow)
            connect(mdiWin, SIGNAL(sendCloseMdiWin(MdiWindow*)), this, SLOT(onCloseMdiWin(MdiWindow*)))
            connect(mdiArea, SIGNAL(subWindowActivated(QMdiSubWindow*)), this, SLOT(onWindowActivated(QMdiSubWindow*)))

            # Make sure the toolbars/etc... are shown before doing their zoomExtents
            if (doOnce) {
                updateMenuToolbarStatusbar()
                doOnce = 0
            }

            if (mdiWin.loadFile(filesToOpen.at(i))) {
                statusbar.showMessage(tr("File(s) loaded"), 2000)
                mdiWin.show()
                mdiWin.showMaximized()
                #Prevent duplicate entries in the recent files list
                if(!opensave_recent_list_of_files.contains(filesToOpen.at(i), Qt::CaseInsensitive)) {
                    opensave_recent_list_of_files.prepend(filesToOpen.at(i))
                }
                #Move the recent file to the top of the list
                else {
                    opensave_recent_list_of_files.removeAll(filesToOpen.at(i))
                    opensave_recent_list_of_files.prepend(filesToOpen.at(i))
                }
                strcpy(settings.opensave_recent_directory, QFileInfo(filesToOpen.at(i)).absolutePath().toLocal8Bit().constData())

                View* v = mdiWin.getView()
                if (v) {
                    v.recalculateLimits()
                    v.zoomExtents()
                }
            }
            else {
                mdiWin.close()

    windowMenuAboutToShow()

def MainWindow::openrecentfile():
    debug_message("MainWindow::openrecentfile()")

    #Check to see if this from the recent files list
    QAction* recentSender = qobject_cast<QAction*>(sender())
    if (recentSender) {
        openFile(1, recentSender.data().toString())
    }
}

def MainWindow::savefile():
    debug_message("MainWindow::savefile()")

def MainWindow::saveasfile():
    debug_message("MainWindow::saveasfile()")
    # need to find the activeSubWindow before it loses focus to the FileDialog
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea.activeSubWindow())
    if(!mdiWin)
        return

    QString file
    openFilesPath = settings.opensave_recent_directory
    file = QFileDialog::getSaveFileName(this, tr("Save As"), openFilesPath, formatFilterSave)

    mdiWin.saveFile(file)

QMdiSubWindow* MainWindow::findMdiWindow(const QString& fileName):
    debug_message("MainWindow::findMdiWindow(%s)", qPrintable(fileName))
    QString canonicalFilePath = QFileInfo(fileName).canonicalFilePath()

    foreach(QMdiSubWindow* subWindow, mdiArea.subWindowList()):
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(subWindow)
        if(mdiWin):
            if(mdiWin.getCurrentFile() == canonicalFilePath):
                return subWindow

    return 0

def MainWindow::closeEvent(QCloseEvent* event):
    mdiArea.closeAllSubWindows()
    writeSettings()
    event.accept()

def MainWindow::onCloseWindow():
    debug_message("MainWindow::onCloseWindow()")
    mdiWin = qobject_cast<MdiWindow*>(mdiArea.activeSubWindow())
    if mdiWin:
        onCloseMdiWin(mdiWin)

def MainWindow::onCloseMdiWin(MdiWindow* theMdiWin):
    debug_message("MainWindow::onCloseMdiWin()")
    numOfDocs--

    keepMaximized
    if(theMdiWin) { keepMaximized = theMdiWin.isMaximized(); }

    mdiArea.removeSubWindow(theMdiWin)
    theMdiWin.deleteLater()

    updateMenuToolbarStatusbar()
    windowMenuAboutToShow()

    if(keepMaximized)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea.activeSubWindow())
        if(mdiWin) { mdiWin.showMaximized(); }
    }
}

def MainWindow::onWindowActivated(QMdiSubWindow* w):
    debug_message("MainWindow::onWindowActivated()")
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(w)
    if(mdiWin) { mdiWin.onWindowActivated(); }
}

def MainWindow::resizeEvent(QResizeEvent* e):
    debug_message("MainWindow::resizeEvent()")
    QMainWindow::resizeEvent(e)
    statusBar().setSizeGripEnabled(!isMaximized())

QAction* MainWindow::getFileSeparator():
    debug_message("MainWindow::getFileSeparator()")
    return myFileSeparator

def MainWindow::updateMenuToolbarStatusbar():
    i
    debug_message("MainWindow::updateMenuToolbarStatusbar()")

    actionHash.value(ACTION_print).setEnabled(numOfDocs > 0)
    actionHash.value(ACTION_windowclose).setEnabled(numOfDocs > 0)
    actionHash.value(ACTION_designdetails).setEnabled(numOfDocs > 0)

    if (numOfDocs) {
        i
        #Toolbars
        for (i=0; i<N_TOOLBARS; i++) {
            toolbar[i].show()
        }

        foreach(QToolBar* tb, toolbarHash)
        {
            tb.show()
        }

        #DockWidgets
        #
        dockPropEdit.show()
        dockUndoEdit.show()


        #Menus
        menuBar().clear()
        menuBar().addMenu(menu[FILE_MENU])
        menuBar().addMenu(menu[EDIT_MENU])
        menuBar().addMenu(menu[VIEW_MENU])

        foreach(QMenu* menu_, menuHash)
        {
            menuBar().addMenu(menu_)
        }

        menuBar().addMenu(menu[SETTINGS_MENU])
        menuBar().addMenu(menu[WINDOW_MENU])
        menuBar().addMenu(menu[HELP_MENU])

        menu[WINDOW_MENU].setEnabled(1)

        # Statusbar
        statusbar.clearMessage()
        statusBarMouseCoord.show()
        status_bar[STATUS_SNAP].show()
        status_bar[STATUS_GRID].show()
        status_bar[STATUS_RULER].show()
        status_bar[STATUS_ORTHO].show()
        status_bar[STATUS_POLAR].show()
        status_bar[STATUS_QSNAP].show()
        status_bar[STATUS_QTRACK].show()
        status_bar[STATUS_LWT].show()
    }
    else
    {
        # Toolbars
        toolbar[TOOLBAR_VIEW].hide()
        toolbar[TOOLBAR_ZOOM].hide()
        toolbar[TOOLBAR_PAN].hide()
        toolbar[TOOLBAR_ICON].hide()
        toolbar[TOOLBAR_HELP].hide()
        toolbar[TOOLBAR_LAYER].hide()
        toolbar[TOOLBAR_TEXT].hide()
        toolbar[TOOLBAR_PROPERTIES].hide()
        foreach(QToolBar* tb, toolbarHash)
        {
            tb.hide()
        }

        #DockWidgets
        #
        dockPropEdit.hide()
        dockUndoEdit.hide()


        #Menus
        menuBar().clear()
        menuBar().addMenu(menu[FILE_MENU])
        menuBar().addMenu(menu[EDIT_MENU])
        menuBar().addMenu(menu[SETTINGS_MENU])
        menuBar().addMenu(menu[WINDOW_MENU])
        menuBar().addMenu(menu[HELP_MENU])

        menu[WINDOW_MENU].setEnabled(0)

        #Statusbar
        statusbar.clearMessage()
        statusBarMouseCoord.hide()
        for (i=0; i<N_STATUS; i++:
            status_bar[i].hide()


MainWindow::validFileFormat(const QString& fileName):
    if(fileName.length() == 0) {
        return 0
    }
    fname
    fname = qPrintable(fileName)
    if (emb_identify_format(fname) >= 0) {
        return 1
    }
    return 0

def MainWindow::loadFormats():
    char stable, unstable
    QString supportedReaders = "All Supported Files ("
    QString individualReaders = "All Files (*);;"
    QString supportedWriters = "All Supported Files ("
    QString individualWriters = "All Files (*);;"
    QString supportedStr
    QString individualStr

    #TODO: Stable Only (Settings Option)
    #stable = 'S'; unstable = 'S';

    #Stable + Unstable
    stable = 'S'; unstable = 'U'

    const char* extension = 0
    const char* description = 0
    char readerState
    char writerState

    EmbFormatList* curFormat = 0
    for(i=0; i < numberOfFormats; i++)
    {
        extension = formatTable[i].extension
        description = formatTable[i].description
        readerState = formatTable[i].reader_state
        writerState = formatTable[i].writer_state

        QString upperExt = QString(extension).toUpper()
        supportedStr = "*" + upperExt + " "
        individualStr = upperExt.replace(".", "") + " - " + description + " (*" + extension + ");;"
        if(readerState == stable or readerState == unstable)
        {
            #Exclude color file formats from open dialogs
            if(upperExt != "COL" and upperExt != "EDR" and upperExt != "INF" and upperExt != "RGB")
            {
                supportedReaders.append(supportedStr)
                individualReaders.append(individualStr)
            }
        }
        if(writerState == stable or writerState == unstable)
        {
            supportedWriters.append(supportedStr)
            individualWriters.append(individualStr)

    supportedReaders.append(");;")
    supportedWriters.append(");;")

    formatFilterOpen = supportedReaders + individualReaders
    formatFilterSave = supportedWriters + individualWriters

    #TODO: Fixup custom filter
    #
    QString custom = settings.custom_filter
    if(custom.contains("supported", Qt::CaseInsensitive))
        custom = ""; //This will hide it
    elif(!custom.contains("*", Qt::CaseInsensitive))
        custom = ""; //This will hide it
    else
        custom = "Custom Filter(" + custom + ");;"

    return tr(qPrintable(custom + supported + all))


def MainWindow::closeToolBar(QAction* action):
    if (action.objectName() == "toolbarclose") {
        QToolBar* tb = qobject_cast<QToolBar*>(sender())
        if(tb)
        {
            debug_message("%s closed.", qPrintable(tb.objectName()))
            tb.hide()


def MainWindow::floatingChangedToolBar(isFloating):
    QToolBar* tb = qobject_cast<QToolBar*>(sender())
    if(tb)
    {
        if(isFloating)
        {
            #
            //TODO: Determine best suited close button on various platforms.
            QStyle::SP_DockWidgetCloseButton
            QStyle::SP_TitleBarCloseButton
            QStyle::SP_DialogCloseButton

            QAction *ACTION = new QAction(tb.style().standardIcon(QStyle::SP_DialogCloseButton), "Close", this)
            ACTION.setStatusTip("Close the " + tb.windowTitle() + " Toolbar")
            ACTION.setObjectName("toolbarclose")
            tb.addAction(ACTION)
            connect(tb, SIGNAL(actionTriggered(QAction*)), this, SLOT(closeToolBar(QAction*)))
        }
        else
        {
            QList<QAction*> actList = tb.actions()
            for(i = 0; i < actList.size(); ++i)
            {
                QAction* ACTION = actList.value(i)
                if(ACTION.objectName() == "toolbarclose")
                {
                    tb.removeAction(ACTION)
                    disconnect(tb, SIGNAL(actionTriggered(QAction*)), this, SLOT(closeToolBar(QAction*)))
                    delete ACTION


EmbDetailsDialog::EmbDetailsDialog(QGraphicsScene* theScene, QWidget* parent) : QDialog(parent):
    setMinimumSize(750,550)

    getInfo()
    mainWidget = createMainWidget()

    buttonBox = new QDialogButtonBox(QDialogButtonBox::Ok)
    connect(buttonBox, SIGNAL(accepted()), this, SLOT(accept()))

    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(this)
    vboxLayoutMain.addWidget(mainWidget)
    vboxLayoutMain.addWidget(buttonBox)
    setLayout(vboxLayoutMain)

    setWindowTitle(tr("Embroidery Design Details"))

    QApplication::setOverrideCursor(Qt::ArrowCursor)

EmbDetailsDialog::~EmbDetailsDialog():
    QApplication::restoreOverrideCursor()

def EmbDetailsDialog::getInfo():
    #TODO: generate a temporary pattern from the scene data.

    #TODO: grab this information from the pattern
    stitchesTotal = 5; #TODO: embStitchList_count(pattern.stitchList, TOTAL);
    stitchesReal = 4; #TODO: embStitchList_count(pattern.stitchList, NORMAL);
    stitchesJump = 3; #TODO: embStitchList_count(pattern.stitchList, JUMP);
    stitchesTrim = 2; #TODO: embStitchList_count(pattern.stitchList, TRIM);
    colorTotal = 1; #TODO: embThreadList_count(pattern.threadList, TOTAL);
    colorChanges = 0; #TODO: embThreadList_count(pattern.threadList, CHANGES);

    boundingRect.setRect(0, 0, 50, 100); #TODO: embPattern_calcBoundingBox(pattern);
}

extern char *details_label_text[]

QWidget* EmbDetailsDialog::createMainWidget():
    QWidget* widget = new QWidget(this)

    #Misc
    QGroupBox* groupBoxMisc = new QGroupBox(tr("General Information"), widget)

    QLabel* labels[12]
    QLabel* fields[12]

    i
    for (i=0; i<12; i++) {
        labels[i] = new QLabel(tr(details_label_text[i]), this)
    }

    fields[0] = new QLabel(QString::number(stitchesTotal), this)
    fields[1] = new QLabel(QString::number(stitchesReal), this)
    fields[2] = new QLabel(QString::number(stitchesJump), this)
    fields[3] = new QLabel(QString::number(stitchesTrim), this)
    fields[4] = new QLabel(QString::number(colorTotal), this)
    fields[5] = new QLabel(QString::number(colorChanges), this)
    fields[6] = new QLabel(QString::number(boundingRect.left()) + " mm", this)
    fields[7] = new QLabel(QString::number(boundingRect.top()) + " mm", this)
    fields[8] = new QLabel(QString::number(boundingRect.right()) + " mm", this)
    fields[9] = new QLabel(QString::number(boundingRect.bottom()) + " mm", this)
    fields[10] = new QLabel(QString::number(boundingRect.width()) + " mm", this)
    fields[11] = new QLabel(QString::number(boundingRect.height()) + " mm", this)

    QGridLayout* gridLayoutMisc = new QGridLayout(groupBoxMisc)
    for (i=0; i<12; i++) {
        gridLayoutMisc.addWidget(labels[i], i, 0, Qt::AlignLeft)
        gridLayoutMisc.addWidget(fields[i], i, 1, Qt::AlignLeft)
    }
    gridLayoutMisc.setColumnStretch(1,1)
    groupBoxMisc.setLayout(gridLayoutMisc)

    # TODO: Color Histogram

    #Stitch Distribution
    #QGroupBox* groupBoxDist = new QGroupBox(tr("Stitch Distribution"), widget);

    # TODO: Stitch Distribution Histogram

    #Widget Layout
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget)
    vboxLayoutMain.addWidget(groupBoxMisc)
    #vboxLayoutMain.addWidget(groupBoxDist);
    vboxLayoutMain.addStretch(1)
    widget.setLayout(vboxLayoutMain)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea.setWidgetResizable(1)
    scrollArea.setWidget(widget)
    return scrollArea

bool Application::event(QEvent *event):
    switch (event.type()) {
    case QEvent::FileOpen:
        if (_mainWin) {
            _mainWin.openFilesSelected(QStringList(static_cast<QFileOpenEvent *>(event).file()))
            return 1
        }
        # Fall through
    default:
        return QApplication::event(event)
    }
}

ImageWidget::ImageWidget(const QString &filename, QWidget* parent) : QWidget(parent):
    debug_message("ImageWidget Constructor")

    img.load(filename)

    setMinimumWidth(img.width())
    setMinimumHeight(img.height())
    setMaximumWidth(img.width())
    setMaximumHeight(img.height())

    this.show()

ImageWidget::load(const QString &fileName):
    img.load(fileName)
    return 1

ImageWidget::save(const QString &fileName):
    img.save(fileName, "PNG")
    return 1

ImageWidget::~ImageWidget():
    debug_message("ImageWidget Destructor")

def ImageWidget::paintEvent(QPaintEvent*):
    QPainter painter(this)
    painter.setViewport(0, 0, width(), height())
    painter.setWindow(0, 0, width(), height())
    painter.drawImage(0, 0, img)


LayerManager::LayerManager(MainWindow* mw, QWidget* parent) : QDialog(parent):
    layerModel = new QStandardItemModel(0, 8, this)

    layerModelSorted = new QSortFilterProxyModel
    layerModelSorted.setDynamicSortFilter(1)
    layerModelSorted.setSourceModel(layerModel)

    treeView = new QTreeView
    treeView.setRootIsDecorated(0)
    treeView.setAlternatingRowColors(1)
    treeView.setModel(layerModelSorted)
    treeView.setSortingEnabled(1)
    treeView.sortByColumn(0, Qt::AscendingOrder)

    QVBoxLayout *mainLayout = new QVBoxLayout
    mainLayout.addWidget(treeView)
    setLayout(mainLayout)

    setWindowTitle(tr("Layer Manager"))
    setMinimumSize(750, 550)

    layerModel.setHeaderData(0, Qt::Horizontal, tr("Name"))
    layerModel.setHeaderData(1, Qt::Horizontal, tr("Visible"))
    layerModel.setHeaderData(2, Qt::Horizontal, tr("Frozen"))
    layerModel.setHeaderData(3, Qt::Horizontal, tr("Z Value"))
    layerModel.setHeaderData(4, Qt::Horizontal, tr("Color"))
    layerModel.setHeaderData(5, Qt::Horizontal, tr("Linetype"))
    layerModel.setHeaderData(6, Qt::Horizontal, tr("Lineweight"))
    layerModel.setHeaderData(7, Qt::Horizontal, tr("Print"))

    addLayer("0", 1, 0, 0.0, qRgb(0,0,0), "Continuous", "Default", 1)
    addLayer("1", 1, 0, 1.0, qRgb(0,0,0), "Continuous", "Default", 1)
    addLayer("2", 1, 0, 2.0, qRgb(0,0,0), "Continuous", "Default", 1)
    addLayer("3", 1, 0, 3.0, qRgb(0,0,0), "Continuous", "Default", 1)
    addLayer("4", 1, 0, 4.0, qRgb(0,0,0), "Continuous", "Default", 1)
    addLayer("5", 1, 0, 5.0, qRgb(0,0,0), "Continuous", "Default", 1)
    addLayer("6", 1, 0, 6.0, qRgb(0,0,0), "Continuous", "Default", 1)
    addLayer("7", 1, 0, 7.0, qRgb(0,0,0), "Continuous", "Default", 1)
    addLayer("8", 1, 0, 8.0, qRgb(0,0,0), "Continuous", "Default", 1)
    addLayer("9", 1, 0, 9.0, qRgb(0,0,0), "Continuous", "Default", 1)

    for(i = 0; i < layerModel.columnCount(); ++i)
        treeView.resizeColumnToContents(i)

    QApplication::setOverrideCursor(Qt::ArrowCursor)

LayerManager::~LayerManager():
    QApplication::restoreOverrideCursor()

def LayerManager::addLayer(const QString& name,
                            const visible,
                            const frozen,
                            const zValue,
                            const unsigned color,
                            const QString& lineType,
                            const QString& lineWeight,
                            const print):
    layerModel.insertRow(0)
    layerModel.setData(layerModel.index(0, 0), name)
    layerModel.setData(layerModel.index(0, 1), visible)
    layerModel.setData(layerModel.index(0, 2), frozen)
    layerModel.setData(layerModel.index(0, 3), zValue)

    QPixmap colorPix(QSize(16,16))
    colorPix.fill(QColor(color))
    layerModel.itemFromIndex(layerModel.index(0, 4)).setIcon(QIcon(colorPix))
    layerModel.setData(layerModel.index(0, 4), QColor(color))

    layerModel.setData(layerModel.index(0, 5), lineType)
    layerModel.setData(layerModel.index(0, 6), lineWeight)
    layerModel.setData(layerModel.index(0, 7), print)

old_main(argc, char *argv[]):
#if defined(Q_OS_MAC)
    Application app(argc, argv)
#else
    QApplication app(argc, argv)
#endif
    app.setApplicationName(_appName_)
    app.setApplicationVersion(_appVer_)

    QStringList filesToOpen

    for (i = 1; i < argc; i++) {
        if (!strcmp(argv[i], "-d") or !strcmp(argv[i], "--debug")) {  }
        elif(!strcmp(argv[i], "-h") or !strcmp(argv[i], "--help")   ) { usage(); }
        elif(!strcmp(argv[i], "-v") or !strcmp(argv[i], "--version")) { version(); }
        elif(QFile::exists(argv[i]) and MainWindow::validFileFormat(argv[i])) {
            filesToOpen << argv[i]
        }
    }

    if(exitApp)
        return 1

    _mainWin = new MainWindow()
#if defined(Q_OS_MAC)
    app.setMainWin(_mainWin)
#endif

    QObject::connect(&app, SIGNAL(lastWindowClosed()), _mainWin, SLOT(quit()))

    _mainWin.setWindowTitle(app.applicationName() + " " + app.applicationVersion())
    _mainWin.show()

    #NOTE: If openFilesSelected() is called from within the mainWin constructor, slot commands wont work and the window menu will be screwed
    if(!filesToOpen.isEmpty())
        _mainWin.openFilesSelected(filesToOpen)

    return app.exec()

MdiArea::MdiArea(MainWindow* mw, QWidget *parent) : QMdiArea(parent), mainWin(mw):
    setTabsClosable(1)

    useLogo = 0
    useTexture = 0
    useColor = 0

MdiArea::~MdiArea():
}

def MdiArea::useBackgroundLogo(use):
    useLogo = use
    forceRepaint()

def MdiArea::useBackgroundTexture(use):
    useTexture = use
    forceRepaint()

def MdiArea::useBackgroundColor(use):
    useColor = use
    forceRepaint()

def MdiArea::setBackgroundLogo(const QString& fileName):
    bgLogo.load(fileName)

    forceRepaint()

def MdiArea::setBackgroundTexture(const QString& fileName):
    bgTexture.load(fileName)

    forceRepaint()

def MdiArea::setBackgroundColor(const QColor& color):
    if(!color.isValid())
        bgColor = background().color()
    else
        bgColor = color

    forceRepaint()

def MdiArea::mouseDoubleClickEvent(QMouseEvent* #e):
    mainWin.openFile()

def MdiArea::paintEvent(QPaintEvent* #e):
    QWidget* vport = viewport()
    QRect rect = vport.rect()

    QPainter painter(vport)
    painter.setRenderHint(QPainter::SmoothPixmapTransform)

    #Always fill with a solid color first
    if(useColor) painter.fillRect(rect, bgColor)
    else         painter.fillRect(rect, background())

    #Then overlay the texture
    if(useTexture)
    {
        QBrush bgBrush(bgTexture)
        painter.fillRect(rect, bgBrush)
    }

    #Overlay the logo last
    if(useLogo)
    {
        #Center the pixmap
        dx = (rect.width()-bgLogo.width())/2
        dy = (rect.height()-bgLogo.height())/2
        painter.drawPixmap(dx, dy, bgLogo.width(), bgLogo.height(), bgLogo)
    }
}

def MdiArea::cascade():
    cascadeSubWindows()
    zoomExtentsAllSubWindows()

def MdiArea::tile():
    tileSubWindows()
    zoomExtentsAllSubWindows()

def MdiArea::zoomExtentsAllSubWindows():
    foreach(QMdiSubWindow* window, subWindowList())
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(window)
        if(mdiWin)
        {
            View* v = mdiWin.getView()
            if(v)
            {
                v.recalculateLimits()
                v.zoomExtents()
            }
        }
    }
}

def MdiArea::forceRepaint():
    # HACK: Take that QMdiArea!
    QSize hack = size()
    resize(hack + QSize(1,1))
    resize(hack)

MdiWindow::MdiWindow(const theIndex, MainWindow* mw, QMdiArea* parent, Qt::WindowFlags wflags) : QMdiSubWindow(parent, wflags):
    mainWin = mw
    mdiArea = parent

    myIndex = theIndex

    fileWasLoaded = 0

    setAttribute(Qt::WA_DeleteOnClose)

    QString aName
    curFile = aName.asprintf("Untitled%d.dst", myIndex)
    this.setWindowTitle(curFile)

    this.setWindowIcon(QIcon("icons/app.png"))

    gscene = new QGraphicsScene(0,0,0,0, this)
    gview = new View(mainWin, gscene, this)

    setWidget(gview)

    #
     * WARNING:
     * DO NOT SET THE QMDISUBWINDOW (this) FOCUSPROXY TO THE PROMPT
     * AS IT WILL CAUSE THE WINDOW MENU TO NOT SWITCH WINDOWS PROPERLY!
     * ALTHOUGH IT SEEMS THAT SETTING INTERNAL WIDGETS FOCUSPROXY IS OK.

#    gview.setFocusProxy(mainWin.prompt);

    resize(sizeHint())

    curLayer = "0"
    curColor = 0; #TODO: color ByLayer
    curLineType = "ByLayer"
    curLineWeight = "ByLayer"

    # Due to strange Qt4.2.3 feature the child window icon is not drawn
    # in the main menu if showMaximized() is called for a non-visible child window
    # Therefore calling show() first...
    show()
    showMaximized()

    setFocusPolicy(Qt::WheelFocus)
    setFocus()

    onWindowActivated()

MdiWindow::~MdiWindow():
    debug_message("MdiWindow Destructor()")

MdiWindow::saveFile(const QString &fileName):
    debug_message("SaveObject save(%s)", qPrintable(fileName))

    # TODO: Before saving to a stitch only format, Embroidermodder needs
     *       to calculate the optimal path to minimize jump stitches. Also
     *       based upon which layer needs to be stitched first,
     *       the path to the next object needs to be hidden beneath fills
     *       that will come later. When finding the optimal path, we need
     *       to take into account the color of the thread, as we do not want
     *       to try to hide dark colored stitches beneath light colored fills.

    formatType = EMBFORMAT_UNSUPPORTED
    writeSuccessful = 0
    i

    formatType = emb_identify_format((char*)qPrintable(fileName))
    if (formatType == EMBFORMAT_UNSUPPORTED) {
        return 0
    }

    EmbPattern* pattern = 0

    pattern = embPattern_create()
    if(!pattern) { debug_message("Could not allocate memory for embroidery pattern"); }

    # Write
    writer = emb_identify_format((char*)qPrintable(fileName))
    if (writer<0) {
        debug_message("Unsupported write file type: %s", qPrintable(fileName))
    }
    else {
        foreach(QGraphicsItem* item, _mainWin.activeScene().items(Qt::AscendingOrder))
        {
            objType = item.data(OBJ_TYPE).toInt()

            if (objType == OBJ_TYPE_ARC) {
                # addArc
            }
            elif (objType == OBJ_TYPE_BLOCK) {
                # addBlock(pattern, item);
            }
            elif(objType == OBJ_TYPE_CIRCLE) {
                CircleObject* obj = static_cast<CircleObject*>(item)
                if (obj) {
                    if (formatType == EMBFORMAT_STITCHONLY) {
                        QPainterPath path = obj.objectSavePath()
            toPolyline(pattern, obj.objectCenter(), path.simplified(), "0", obj.objectColor(), "CONTINUOUS", "BYLAYER"); #TODO: proper layer/lineType/lineWeight //TODO: Improve precision, replace simplified
        }
        else {
            QPointF p = obj.objectCenter()
            r = obj.objectRadius()
            embPattern_addCircleObjectAbs(pattern, (double)p.x(), (double)p.y(), (double)r)
        }
    }
            }
            elif(objType == OBJ_TYPE_DIMALIGNED) {
                # addDimAligned(pattern, item);
            }
            elif(objType == OBJ_TYPE_DIMANGULAR) {
                # addDimAngular(pattern, item);
            }
            elif(objType == OBJ_TYPE_DIMARCLENGTH) {
                # addDimArcLength(pattern, item);
            }
            elif(objType == OBJ_TYPE_DIMDIAMETER) {
                # addDimDiameter(pattern, item);
            }
            elif(objType == OBJ_TYPE_DIMLEADER) {
                # addDimLeader(pattern, item);
            }
            elif(objType == OBJ_TYPE_DIMLINEAR) {
                # addDimLinear(pattern, item);
            }
            elif(objType == OBJ_TYPE_DIMORDINATE)  {
                # addDimOrdinate(pattern, item);
            }
            elif(objType == OBJ_TYPE_DIMRADIUS)    {
                # addDimRadius(pattern, item);
            }
            elif(objType == OBJ_TYPE_ELLIPSE) {
    EllipseObject* obj = static_cast<EllipseObject*>(item)
    if(obj)
    {
        if(formatType == EMBFORMAT_STITCHONLY)
        {
            QPainterPath path = obj.objectSavePath()
            toPolyline(pattern, obj.objectCenter(), path.simplified(), "0", obj.objectColor(), "CONTINUOUS", "BYLAYER"); #TODO: proper layer/lineType/lineWeight //TODO: Improve precision, replace simplified
        }
        else
        {
            #TODO: ellipse rotation
            embPattern_addEllipseObjectAbs(pattern, (double)obj.objectCenter().x(), (double)obj.objectCenter().y(), (double)obj.objectWidth()/2.0, (double)obj.objectHeight()/2.0)
        }
    }
            }
            elif(objType == OBJ_TYPE_ELLIPSEARC)   { # addEllipseArc(pattern, item);   }
            elif(objType == OBJ_TYPE_GRID)         { # addGrid(pattern, item);         }
            elif(objType == OBJ_TYPE_HATCH)        { # addHatch(pattern, item);        }
            elif(objType == OBJ_TYPE_IMAGE)        { # addImage(pattern, item);        }
            elif(objType == OBJ_TYPE_INFINITELINE) { # addInfiniteLine(pattern, item);  }
            elif(objType == OBJ_TYPE_LINE)         {
    LineObject* obj = static_cast<LineObject*>(item)
    if(obj)
    {
        if(formatType == EMBFORMAT_STITCHONLY)
        {
            toPolyline(pattern, obj.objectEndPoint1(), obj.objectSavePath(), "0", obj.objectColor(), "CONTINUOUS", "BYLAYER"); #TODO: proper layer/lineType/lineWeight
        }
        else
        {
            embPattern_addLineObjectAbs(pattern, (double)obj.objectX1(), (double)obj.objectY1(), (double)obj.objectX2(), (double)obj.objectY2())
        }
    }
      }
            elif (objType == OBJ_TYPE_PATH) {
    #TODO: Reimplement addPolyline() using the libembroidery C API
    #
    debug_message("addPolyline()")
    QGraphicsPathItem* polylineItem = (QGraphicsPathItem*)item
    if(polylineItem)
    {
        QPainterPath path = polylineItem.path()
        QPointF pos = polylineItem.pos()
        startX = pos.x()
        startY = pos.y()

        QPainterPath::Element element
        QPainterPath::Element P1
        QPainterPath::Element P2
        QPainterPath::Element P3
        QPainterPath::Element P4

        for(i = 0; i < path.elementCount()-1; ++i)
        {
            element = path.elementAt(i)
            if(element.isMoveTo())
            {
                pattern.AddStitchAbs((element.x + startX), -(element.y + startY), TRIM)
            }
            elif(element.isLineTo())
            {
                pattern.AddStitchAbs((element.x + startX), -(element.y + startY), NORMAL)
            }
            elif(element.isCurveTo())
            {
                P1 = path.elementAt(i-1); // start point
                P2 = path.elementAt(i);   // control point
                P3 = path.elementAt(i+1); // control point
                P4 = path.elementAt(i+2); // end point

                pattern.AddStitchAbs(P4.x, -P4.y, NORMAL); //TODO: This is temporary
                //TODO: Curved Polyline segments are always arcs
            }
        }
        pattern.AddStitchRel(0, 0, STOP)
        QColor c= polylineItem.pen().color()
        pattern.AddColor(c.red(), c.green(), c.blue(), "", "")
    }

            }
            elif(objType == OBJ_TYPE_POINT)        {
    PointObject* obj = static_cast<PointObject*>(item)
    if(obj)
    {
        if(formatType == EMBFORMAT_STITCHONLY)
        {
            toPolyline(pattern, obj.objectPos(), obj.objectSavePath(), "0", obj.objectColor(), "CONTINUOUS", "BYLAYER"); #TODO: proper layer/lineType/lineWeight
        }
        else
        {
            embPattern_addPointObjectAbs(pattern, (double)obj.objectX(), (double)obj.objectY())
        }
    }
             }
            elif(objType == OBJ_TYPE_POLYGON) {
    PolygonObject* obj = static_cast<PolygonObject*>(item)
    if(obj)
    {
        toPolyline(pattern, obj.objectPos(), obj.objectSavePath(), "0", obj.objectColor(), "CONTINUOUS", "BYLAYER"); #TODO: proper layer/lineType/lineWeight
    }
            }
            elif(objType == OBJ_TYPE_POLYLINE) {
                PolylineObject* obj = static_cast<PolylineObject*>(item)
                if (obj)  {
                    toPolyline(pattern, obj.objectPos(), obj.objectSavePath(), "0", obj.objectColor(), "CONTINUOUS", "BYLAYER"); #TODO: proper layer/lineType/lineWeight
                }
            }
            elif(objType == OBJ_TYPE_RAY) {
                # addRay(pattern, item);
            }
            elif(objType == OBJ_TYPE_RECTANGLE) {
    RectObject* obj = static_cast<RectObject*>(item)
    if(obj)
    {
        if(formatType == EMBFORMAT_STITCHONLY)
        {
            toPolyline(pattern, obj.objectPos(), obj.objectSavePath(), "0", obj.objectColor(), "CONTINUOUS", "BYLAYER"); #TODO: proper layer/lineType/lineWeight
        }
        else
        {
            #TODO: Review this at some point
            QPointF topLeft = obj.objectTopLeft()
            embPattern_addRectObjectAbs(pattern, (double)topLeft.x(), (double)topLeft.y(), (double)obj.objectWidth(), (double)obj.objectHeight())
        }
    }
            }
            elif(objType == OBJ_TYPE_SLOT) {
            }
            elif(objType == OBJ_TYPE_SPLINE)       {
    #TODO: abstract bezier into geom-bezier... cubicBezierMagic(P1, P2, P3, P4, 0.0, 1.0, tPoints);
    }
            elif(objType == OBJ_TYPE_TEXTMULTI)    {
    #TODO: saving polygons, polylines and paths must be stable before we go here.
       }
            elif (objType == OBJ_TYPE_TEXTSINGLE) {
    #TODO: saving polygons, polylines and paths must be stable before we go here.

    #TODO: This needs to work like a path, not a polyline. Improve this
    TextSingleObject* obj = static_cast<TextSingleObject*>(item)
    if(obj)
    {
        if(formatType == EMBFORMAT_STITCHONLY)
        {
            QList<QPainterPath> pathList = obj.objectSavePathList()
            foreach(QPainterPath path, pathList)
            {
                toPolyline(pattern, obj.objectPos(), path.simplified(), "0", obj.objectColor(), "CONTINUOUS", "BYLAYER"); #TODO: proper layer/lineType/lineWeight //TODO: Improve precision, replace simplified
            }
        }
        else
        {

        }
    }  }
        }

        #TODO: handle EMBFORMAT_STCHANDOBJ also
        if(formatType == EMBFORMAT_STITCHONLY)
            embPattern_movePolylinesToStitchList(pattern); #TODO: handle all objects like this

        writeSuccessful = embPattern_writeAuto(pattern, qPrintable(fileName))
        if(!writeSuccessful) { debug_message("Writing file %s was unsuccessful", qPrintable(fileName)); }
    }

    #TODO: check the embLog for errors and if any exist, report them.
    embPattern_free(pattern)

    return writeSuccessful

MdiWindow::loadFile(const QString &fileName):
    debug_message("MdiWindow loadFile()")

    unsigned tmpColor = getCurrentColor()

    QFile file(fileName)
    if(!file.open(QFile::ReadOnly | QFile::Text))
    {
        QMessageBox::warning(this, tr("Error reading file"),
                             tr("Cannot read file %1:\n%2.")
                             .arg(fileName)
                             .arg(file.errorString()))
        return 0
    }

    QApplication::setOverrideCursor(Qt::WaitCursor)

    QString ext = fileExtension(fileName)
    debug_message("ext: %s", qPrintable(ext))

    # Read
    EmbPattern* p = embPattern_create()
    if (!p) {
        printf("Could not allocate memory for embroidery pattern\n")
        exit(1)
    }
    if (!embPattern_readAuto(p, qPrintable(fileName))) {
        debug_message("Reading file was unsuccessful: %s\n", qPrintable(fileName))
        QApplication::restoreOverrideCursor()
        QMessageBox::warning(this, tr("Error reading pattern"), tr("Reading file was unsuccessful: ") + fileName)
    }
    else:
        embPattern_moveStitchListToPolylines(p); #TODO: Test more
        stitchCount = p.stitchList.count
        QPainterPath path

        if p.circles:
            for i in range(p.circles.count):
                EmbCircle c = p.circles.circle[i].circle
                EmbColor thisColor = p.circles.circle[i].color
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b))
                # NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed.
                mainWin.nativeAddCircle(c.center.x, c.center.y, c.radius, 0, OBJ_RUBBER_OFF); #TODO: fill

        if p.ellipses:
            for (i = 0; i < p.ellipses.count; i++) {
                EmbEllipse e = p.ellipses.ellipse[i].ellipse
                EmbColor thisColor = p.ellipses.ellipse[i].color
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b))
                # NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed.
                mainWin.nativeAddEllipse(e.centerX, e.centerY, e.radiusX, e.radiusY, 0, 0, OBJ_RUBBER_OFF); #TODO: rotation and fill

        if (p.lines) {
            for (i = 0; i < p.lines.count; i++) {
                EmbLine li = p.lines.line[i].line
                EmbColor thisColor = p.lines.line[i].color
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b))
                # NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed.
                mainWin.nativeAddLine(li.start.x, li.start.y, li.end.x, li.end.y, 0, OBJ_RUBBER_OFF); #TODO: rotation

        if (p.paths) {
            # TODO: This is unfinished. It needs more work
            for (i=0; i < p.paths.count; i++) {
                EmbArray* curPointList = p.paths.path[i].pointList
                QPainterPath pathPath
                EmbColor thisColor = p.paths.path[i].color
                if (curPointList.count > 0) {
                    EmbVector pp = curPointList[0].point.point
                    pathPath.moveTo(pp.x, -pp.y); #NOTE: Qt Y+ is down and libembroidery Y+ is up, so inverting the Y is needed.
                }
                for (j = 1; j < curPointList.count; j++) {
                    EmbVector pp = curPointList[j].point.point
                    pathPath.lineTo(pp.x, -pp.y); #NOTE: Qt Y+ is down and libembroidery Y+ is up, so inverting the Y is needed.
                }
                QPen loadPen(qRgb(thisColor.r, thisColor.g, thisColor.b))
                loadPen.setWidthF(0.35)
                loadPen.setCapStyle(Qt::RoundCap)
                loadPen.setJoinStyle(Qt::RoundJoin)

                PathObject* obj = new PathObject(0,0, pathPath, loadPen.color().rgb())
                obj.setObjectRubberMode(OBJ_RUBBER_OFF)
                _mainWin.activeScene().addItem(obj)
            }
        }
        if (p.points) {
            for (i = 0; i < p.points.count; i++) {
                EmbVector po = p.points.point[i].point
                EmbColor thisColor = p.points.point[i].color
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b))
                # NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed.
                mainWin.nativeAddPoint(po.x, po.y)
            }
        }
        if (p.polygons) {
            for (i = 0; i < p.polygons.count; i++) {
                EmbArray *curPointList = p.polygons.polygon[i].pointList
                QPainterPath polygonPath
                firstPo= 0
                startX = 0, startY = 0
                x = 0, y = 0
                EmbColor thisColor = p.polygons.polygon[i].color
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b))
                for (j=0; j<curPointList.count; j++) {
                    EmbVector pp = curPointList.point[j].point
                    x = pp.x
                    y = -pp.y; #NOTE: Qt Y+ is down and libembroidery Y+ is up, so inverting the Y is needed.

                    if (firstPoint) {
                        polygonPath.lineTo(x,y)
                    } else {
                        polygonPath.moveTo(x,y)
                        firstPo= 1
                        startX = x
                        startY = y
                    }
                }
                polygonPath.translate(-startX, -startY)
                mainWin.nativeAddPolygon(startX, startY, polygonPath, OBJ_RUBBER_OFF)
            }
        }
        # NOTE: Polylines should only contain NORMAL stitches.
        if (p.polylines) {
            for (i=0; i<p.polylines.count; i++) {
                EmbArray* curPointList = p.polylines.polyline[i].pointList
                QPainterPath polylinePath
                firstPo= 0
                startX = 0, startY = 0
                x = 0, y = 0
                EmbColor thisColor = p.polylines.polyline[i].color
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b))
                for (j=0; j<curPointList.count; j++) {
                    EmbVector pp = curPointList.point[j].point
                    x = pp.x
                    y = -pp.y; #NOTE: Qt Y+ is down and libembroidery Y+ is up, so inverting the Y is needed.
                    if (firstPoint) {
                        polylinePath.lineTo(x,y)
                    } else {
                        polylinePath.moveTo(x,y)
                        firstPo= 1
                        startX = x
                        startY = y
                    }
                }

                polylinePath.translate(-startX, -startY)
                mainWin.nativeAddPolyline(startX, startY, polylinePath, OBJ_RUBBER_OFF)
            }
        }
        if (p.rects) {
            for (i=0; i<p.rects.count; i++) {
                EmbRect r = p.rects.rect[i].rect
                EmbColor thisColor = p.rects.rect[i].color
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b))
                #NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed.
                mainWin.nativeAddRectangle(embRect_x(r), embRect_y(r), embRect_width(r), embRect_height(r), 0, 0, OBJ_RUBBER_OFF); #TODO: rotation and fill
            }
        }
        setCurrentFile(fileName)
        mainWin.statusbar.showMessage("File loaded.")
        QString stitches
        stitches.setNum(stitchCount)

        if(settings.grid_load_from_file) {
            #TODO: Josh, provide me a hoop size and/or grid spacing from the pattern.
        }
        QApplication::restoreOverrideCursor()
    }
    embPattern_free(p)

    # Clear the undo stack so it is not possible to undo past this point.
    undo_history_length = 0

    setCurrentColor(tmpColor)
    return 1

def MdiWindow::print():
    #
    QPrintDialog dialog(&printer, this)
    if (dialog.exec() == QDialog::Accepted) {
        QPainter painter(&printer)
        if (settings.printing_disable_bg) {
            // Save current bg
            QBrush brush = gview.backgroundBrush()
            // Save ink by not printing the bg at all
            gview.setBackgroundBrush(Qt::NoBrush)
            // Print, fitting the viewport contents into a full page
            gview.render(&painter)
            // Restore the bg
            gview.setBackgroundBrush(brush)
        } else {
            // Print, fitting the viewport contents into a full page
            gview.render(&painter)
        }



# TODO: Save a Brother PEL image (An 8bpp, 130x113 pixel monochromatic? bitmap image) Why 8bpp when only 1bpp is needed?

# TODO: Should BMC be limited to ~32KB or is this a mix up with Bitmap Cache?
# TODO: Is there/should there be other embedded data in the bitmap besides the image itself?
# NOTE: Can save a Singer BMC image (An 8bpp, 130x113 pixel colored bitmap image)
def MdiWindow::saveBMC():
    # TODO: figure out how to center the image, right now it just plops it to the left side.
    QImage img(150, 150, QImage::Format_ARGB32_Premultiplied)
    img.fill(qRgb(255,255,255))
    QRectF extents = gscene.itemsBoundingRect()

    QPainter painter(&img)
    QRectF targetRect(0,0,150,150)
    if (settings.printing_disable_bg) { #TODO: Make BMC background into it's own setting?
        QBrush brush = gscene.backgroundBrush()
        gscene.setBackgroundBrush(Qt::NoBrush)
        gscene.update()
        gscene.render(&painter, targetRect, extents, Qt::KeepAspectRatio)
        gscene.setBackgroundBrush(brush)
    } else {
        gscene.update()
        gscene.render(&painter, targetRect, extents, Qt::KeepAspectRatio)
    }
    img.convertToFormat(QImage::Format_Indexed8, Qt::ThresholdDither|Qt::AvoidDither).save("test.bmc", "BMP")

def MdiWindow::setCurrentFile(const QString &fileName):
    curFile = QFileInfo(fileName).canonicalFilePath()
    setWindowModified(0)
    setWindowTitle(getShortCurrentFile())

QString MdiWindow::getShortCurrentFile():
    return QFileInfo(curFile).fileName()

QString MdiWindow::fileExtension(const QString& fileName):
    return QFileInfo(fileName).suffix().toLower()

def MdiWindow::closeEvent(QCloseEvent* #e):
    debug_message("MdiWindow closeEvent()")
    emit sendCloseMdiWin(this)

def MdiWindow::onWindowActivated():
    debug_message("MdiWindow onWindowActivated()")
    status_bar[STATUS_SNAP].setChecked(gscene.property("ENABLE_SNAP").toBool())
    status_bar[STATUS_GRID].setChecked(gscene.property("ENABLE_GRID").toBool())
    status_bar[STATUS_RULER].setChecked(gscene.property("ENABLE_RULER").toBool())
    status_bar[STATUS_ORTHO].setChecked(gscene.property("ENABLE_ORTHO").toBool())
    status_bar[STATUS_POLAR].setChecked(gscene.property("ENABLE_POLAR").toBool())
    status_bar[STATUS_QSNAP].setChecked(gscene.property("ENABLE_QSNAP").toBool())
    status_bar[STATUS_QTRACK].setChecked(gscene.property("ENABLE_QTRACK").toBool())
    status_bar[STATUS_LWT].setChecked(gscene.property("ENABLE_LWT").toBool())
    #mainWin.prompt.setHistory(promptHistory);
}

QSize MdiWindow::sizeHint() const:
    debug_message("MdiWindow sizeHint()")
    return QSize(450, 300)

def MdiWindow::currentLayerChanged(const QString& layer):
    curLayer = layer

def MdiWindow::currentColorChanged(const unsigned int& color):
    curColor = color

def MdiWindow::currentLinetypeChanged(const QString& type):
    curLineType = type

def MdiWindow::currentLineweightChanged(const QString& weight):
    curLineWeight = weight

def MdiWindow::updateColorLinetypeLineweight():
}

def MdiWindow::deletePressed():
    gview.deletePressed()

def MdiWindow::escapePressed():
    gview.escapePressed()

def MdiWindow::showViewScrollBars(val):
    gview.showScrollBars(val)

def MdiWindow::setViewCrossHairColor(unsigned color):
    gview.setCrossHairColor(color)

def MdiWindow::setViewBackgroundColor(unsigned color):
    gview.setBackgroundColor(color)

def MdiWindow::setViewSelectBoxColors(unsigned colorL, unsigned fillL, unsigned colorR, unsigned fillR, alpha):
    gview.setSelectBoxColors(colorL, fillL, colorR, fillR, alpha)

def MdiWindow::setViewGridColor(unsigned color):
    gview.setGridColor(color)

def MdiWindow::setViewRulerColor(unsigned color):
    gview.setRulerColor(color)

PreviewDialog::PreviewDialog(QWidget* parent,
                             const QString& caption,
                             const QString& dir,
                             const QString& filter) : QFileDialog(parent, caption, dir, filter):
    debug_message("PreviewDialog Constructor")

    #TODO: get actual thumbnail image from file, lets also use a size of 128x128 for now...
    #TODO: make thumbnail size adjustable thru settings dialog
    imgWidget = new ImageWidget("icons/default/nopreview.png", this)

    QLayout* lay = layout()
    if(qobject_cast<QGridLayout*>(lay))
    {
        QGridLayout* grid = qobject_cast<QGridLayout*>(lay)
        grid.addWidget(imgWidget, 0, grid.columnCount(), grid.rowCount(), 1)
    }

    setModal(1)
    setOption(QFileDialog::DontUseNativeDialog)
    setViewMode(QFileDialog::Detail)
    setFileMode(QFileDialog::ExistingFiles)

    #TODO: connect the currentChanged signal to update the preview imgWidget.
}

PreviewDialog::~PreviewDialog():
    debug_message("PreviewDialog Destructor")

SelectBox::SelectBox(Shape s, QWidget* parent) : QRubberBand(s, parent):
    #Default values
    setColors(QColor(Qt::darkGreen), QColor(Qt::green), QColor(Qt::darkBlue), QColor(Qt::blue), 32)

def SelectBox::setDirection(dir):
    if(!dir) { dirPen = leftPen;  dirBrush = leftBrush;  }
    else     { dirPen = rightPen; dirBrush = rightBrush; }
    boxDir = dir

def SelectBox::setColors(const QColor& colorL, const QColor& fillL, const QColor& colorR, const QColor& fillR, newAlpha):
    debug_message("SelectBox setColors()")
    alpha = newAlpha

    leftPenColor = colorL; #TODO: allow customization
    leftBrushColor = to_emb_color(QColor(fillL.red(), fillL.green(), fillL.blue(), alpha))
    rightPenColor = colorR; #TODO: allow customization
    rightBrushColor = QColor(fillR.red(), fillR.green(), fillR.blue(), alpha)

    leftPen.setColor(leftPenColor)
    leftPen.setStyle(Qt::DashLine)
    leftBrush.setStyle(Qt::SolidPattern)
    leftBrush.setColor(to_qcolor(leftBrushColor))

    rightPen.setColor(rightPenColor)
    rightPen.setStyle(Qt::SolidLine)
    rightBrush.setStyle(Qt::SolidPattern)
    rightBrush.setColor(rightBrushColor)

    if(!boxDir) { dirPen = leftPen;  dirBrush = leftBrush;  }
    else        { dirPen = rightPen; dirBrush = rightBrush; }

    forceRepaint()

def SelectBox::paintEvent(QPaintEvent*):
    QPainter painter(this)
    painter.setPen(dirPen)
    painter.fillRect(0,0,width()-1, height()-1, dirBrush)
    painter.drawRect(0,0,width()-1, height()-1)

def SelectBox::forceRepaint():
    #HACK: Take that QRubberBand!
    QSize hack = size()
    resize(hack + QSize(1,1))
    resize(hack)

StatusBarButton::StatusBarButton(QString buttonText, MainWindow* mw, StatusBar* statbar, QWidget *parent) : QToolButton(parent):
    statusbar = statbar

    this.setObjectName("StatusBarButton" + buttonText)

    this.setText(buttonText)
    this.setAutoRaise(1)
    this.setCheckable(1)

    if (objectName() == "StatusBarButtonSNAP") {
        connect(this, SIGNAL(toggled(int)), this, SLOT(toggleSnap(int)))
    }
    elif (objectName() == "StatusBarButtonGRID") {
        connect(this, SIGNAL(toggled(int)), this, SLOT(toggleGrid(int)))
    }
    elif(objectName() == "StatusBarButtonRULER") {
        connect(this, SIGNAL(toggled(int)), this, SLOT(toggleRuler(int)))
    }
    elif(objectName() == "StatusBarButtonORTHO")  { connect(this, SIGNAL(toggled(int)), this, SLOT(toggleOrtho(int))); }
    elif(objectName() == "StatusBarButtonPOLAR")  { connect(this, SIGNAL(toggled(int)), this, SLOT(togglePolar(int))); }
    elif(objectName() == "StatusBarButtonQSNAP")  { connect(this, SIGNAL(toggled(int)), this, SLOT(toggleQSnap(int))); }
    elif(objectName() == "StatusBarButtonQTRACK") { connect(this, SIGNAL(toggled(int)), this, SLOT(toggleQTrack(int))); }
    elif(objectName() == "StatusBarButtonLWT")    { connect(this, SIGNAL(toggled(int)), this, SLOT(toggleLwt(int))); }
}

def StatusBarButton::contextMenuEvent(QContextMenuEvent *event):
    QApplication::setOverrideCursor(Qt::ArrowCursor)
    QMenu menu_(this)
    if (objectName() == "StatusBarButtonSNAP") {
        QAction* settingsSnapAction = new QAction(loadIcon(gridsnapsettings_xpm), "&Settings...", &menu_)
        connect(settingsSnapAction, SIGNAL(triggered()), this, SLOT(settingsSnap()))
        menu_.addAction(settingsSnapAction)
    }
    elif (objectName() == "StatusBarButtonGRID") {
        QAction* settingsGridAction = new QAction(loadIcon(gridsettings_xpm), "&Settings...", &menu_)
        connect(settingsGridAction, SIGNAL(triggered()), this, SLOT(settingsGrid()))
        menu_.addAction(settingsGridAction)
    }
    elif (objectName() == "StatusBarButtonRULER") {
        QAction* settingsRulerAction = new QAction(QIcon("icons/rulersettings.png"), "&Settings...", &menu_)
        connect(settingsRulerAction, SIGNAL(triggered()), this, SLOT(settingsRuler()))
        menu_.addAction(settingsRulerAction)
    }
    elif (objectName() == "StatusBarButtonORTHO") {
        QAction* settingsOrthoAction = new QAction(QIcon("icons/orthosettings.png"), "&Settings...", &menu_)
        connect(settingsOrthoAction, SIGNAL(triggered()), this, SLOT(settingsOrtho()))
        menu_.addAction(settingsOrthoAction)
    }
    elif (objectName() == "StatusBarButtonPOLAR") {
        QAction* settingsPolarAction = new QAction(QIcon("icons/polarsettings.png"), "&Settings...", &menu_)
        connect(settingsPolarAction, SIGNAL(triggered()), this, SLOT(settingsPolar()))
        menu_.addAction(settingsPolarAction)
    }
    elif(objectName() == "StatusBarButtonQSNAP")
    {
        QAction* settingsQSnapAction = new QAction(QIcon("icons/qsnapsettings.png"), "&Settings...", &menu_)
        connect(settingsQSnapAction, SIGNAL(triggered()), this, SLOT(settingsQSnap()))
        menu_.addAction(settingsQSnapAction)
    }
    elif(objectName() == "StatusBarButtonQTRACK")
    {
        QAction* settingsQTrackAction = new QAction(QIcon("icons/qtracksettings.png"), "&Settings...", &menu_)
        connect(settingsQTrackAction, SIGNAL(triggered()), this, SLOT(settingsQTrack()))
        menu_.addAction(settingsQTrackAction)
    }
    elif(objectName() == "StatusBarButtonLWT") {
        View* gview = _mainWin.activeView()
        if gview:
            QAction* enableRealAction = new QAction(QIcon("icons/realrender.png"), "&RealRender On", &menu_)
            enableRealAction.setEnabled(!gview.isRealEnabled())
            connect(enableRealAction, SIGNAL(triggered()), this, SLOT(enableReal()))
            menu_.addAction(enableRealAction)

            QAction* disableRealAction = new QAction(QIcon("icons/realrender.png"), "&RealRender Off", &menu_)
            disableRealAction.setEnabled(gview.isRealEnabled())
            connect(disableRealAction, SIGNAL(triggered()), this, SLOT(disableReal()))
            menu_.addAction(disableRealAction)
        }

        QAction* settingsLwtAction = new QAction(loadIcon(lineweightsettings_xpm), "&Settings...", &menu_)
        connect(settingsLwtAction, SIGNAL(triggered()), this, SLOT(settingsLwt()))
        menu_.addAction(settingsLwtAction)
    }
    menu_.exec(event.globalPos())
    QApplication::restoreOverrideCursor()
    statusbar.clearMessage()

StatusBar::StatusBar(MainWindow* mw, QWidget *parent) : QStatusBar(parent):
    i
    this.setObjectName("StatusBar")

    for (i=0; i<N_STATUS; i++) {
        status_bar[i] = new StatusBarButton(status_bar_label[i], _mainWin, this, this)
    }
    statusBarMouseCoord = new QLabel(this)

    statusBarMouseCoord.setMinimumWidth(300); # Must fit this text always
    statusBarMouseCoord.setMaximumWidth(300); # "+1.2345E+99, +1.2345E+99, +1.2345E+99"

    this.addWidget(statusBarMouseCoord)
    for (i=0; i<N_STATUS; i++) {
        this.addWidget(status_bar[i])

def StatusBar::setMouseCoord(x, y):
    # TODO: set format from settings (Architectural, Decimal, Engineering, Fractional, Scientific)

    # Decimal
    statusBarMouseCoord.setText(QString().setNum(x, 'F', 4) + ", "
        + QString().setNum(y, 'F', 4));
        #TODO: use precision from unit settings

    # Scientific
    # statusBarMouseCoord.setText(QString().setNum(x, 'E', 4)
         + ", " + QString().setNum(y, 'E', 4));
    # TODO: use precision from unit settings


def main_about():
    debug_message("main_about()")

    #TODO: QTabWidget for about dialog
    #QApplication::setOverrideCursor(Qt::ArrowCursor)
    debug_message("about()")
    QString appDir = qApp.applicationDirPath()
    QString title = "About Embroidermodder 2"

    QDialog dialog(_mainWin)
    ImageWidget img(appDir + "/images/logo-small.png")
    QLabel text(QString("Embroidermodder ") + QString(_appVer_) + "\n\n" +
        _mainWin.tr("http://embroidermodder.org") +
        "\n\n" +
        _mainWin.tr("Available Platforms: GNU/Linux, Windows, Mac OSX, Raspberry Pi") +
        "\n\n" +
         _mainWin.tr("Embroidery formats by Josh Varga.") +
         "\n" +
        _mainWin.tr("User Interface by Jonathan Greig and Robin Swift.") +
        "\n\n" +
         _mainWin.tr("Free under the zlib/libpng license.")
         #if defined(BUILD_GIT_HASH)
         + "\n\n" +
         _mainWin.tr("Build Hash: ") + qPrintable(BUILD_GIT_HASH)
          #endif
    )
    text.setWordWrap(1)

    QDialogButtonBox buttonbox(Qt::Horizontal, &dialog)
    QPushButton button(&dialog)
    button.setText("Oh, Yeah!")
    buttonbox.addButton(&button, QDialogButtonBox::AcceptRole)
    buttonbox.setCenterButtons(1)
    _mainWin.connect(&buttonbox, SIGNAL(accepted()), &dialog, SLOT(accept()))

    QVBoxLayout layout
    layout.setAlignment(Qt::AlignCenter)
    layout.addWidget(&img)
    layout.addWidget(&text)
    layout.addWidget(&buttonbox)

    dialog.setWindowTitle(title)
    dialog.setMinimumWidth(img.minimumWidth()+30)
    dialog.setMinimumHeight(img.minimumHeight()+50)
    dialog.setLayout(&layout)
    dialog.exec()
    QApplication::restoreOverrideCursor()


def actuator(call):
    undo_history_position++
    # an action has been taken, we are at the current head of the stack
    undo_history_length = undo_history_position
    strcpy(undo_history[undo_history_position], call)
    id = call[0]
    if (id < 0)
        id += 256

    if (id < N_ACTIONS)
        action_list[id].function()

# New for toolbars: modify and draw. Inquiry toolbar?
 *
 * TODO: associate the property editor with the function callbacks using
 * a function pointer.


# property_editor_row property_editors[] = {
#
QGroupBox* PropertyEditor::createGroupBoxGeometryCircle():
    groupBoxGeometryCircle = new QGroupBox(tr("Geometry"), this)

    toolButtonCircleCenterX = createToolButton("blank", tr("Center X"))
    toolButtonCircleCenterY = createToolButton("blank", tr("Center Y"))
    toolButtonCircleRadius = createToolButton("blank", tr("Radius"))
    toolButtonCircleDiameter = createToolButton("blank", tr("Diameter"))
    toolButtonCircleArea = createToolButton("blank", tr("Area"))
    toolButtonCircleCircumference = createToolButton("blank",
        tr("Circumference"))

    lineEditCircleCenterX = createLineEdit("double", 0)
    lineEditCircleCenterY = createLineEdit("double", 0)
    lineEditCircleRadius = createLineEdit("double", 0)
    lineEditCircleDiameter = createLineEdit("double", 0)
    lineEditCircleArea = createLineEdit("double", 0)
    lineEditCircleCircumference = createLineEdit("double", 0)

    mapSignal(lineEditCircleCenterX, "lineEditCircleCenterX", OBJ_TYPE_CIRCLE)
    mapSignal(lineEditCircleCenterY, "lineEditCircleCenterY", OBJ_TYPE_CIRCLE)
    mapSignal(lineEditCircleRadius, "lineEditCircleRadius", OBJ_TYPE_CIRCLE)
    mapSignal(lineEditCircleDiameter, "lineEditCircleDiameter", "CIRCLE")
    mapSignal(lineEditCircleArea, "lineEditCircleArea", OBJ_TYPE_CIRCLE)
    mapSignal(lineEditCircleCircumference, "lineEditCircleCircumference",
        OBJ_TYPE_CIRCLE)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonCircleCenterX, lineEditCircleCenterX)
    formLayout.addRow(toolButtonCircleCenterY, lineEditCircleCenterY)
    formLayout.addRow(toolButtonCircleRadius, lineEditCircleRadius)
    formLayout.addRow(toolButtonCircleDiameter, lineEditCircleDiameter)
    formLayout.addRow(toolButtonCircleArea, lineEditCircleArea)
    formLayout.addRow(toolButtonCircleCircumference,
        lineEditCircleCircumference)
    groupBoxGeometryCircle.setLayout(formLayout)

    return groupBoxGeometryCircle

QGroupBox* PropertyEditor::createGroupBoxGeometryImage():
    groupBoxGeometryImage = new QGroupBox(tr("Geometry"), this)

    toolButtonImageX = createToolButton("blank", tr("Position X"))
    toolButtonImageY = createToolButton("blank", tr("Position Y"))
    toolButtonImageWidth = createToolButton("blank", tr("Width"))
    toolButtonImageHeight = createToolButton("blank", tr("Height"))

    lineEditImageX = createLineEdit("double", 0)
    lineEditImageY = createLineEdit("double", 0)
    lineEditImageWidth = createLineEdit("double", 0)
    lineEditImageHeight = createLineEdit("double", 0)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonImageX, lineEditImageX)
    formLayout.addRow(toolButtonImageY, lineEditImageY)
    formLayout.addRow(toolButtonImageWidth, lineEditImageWidth)
    formLayout.addRow(toolButtonImageHeight, lineEditImageHeight)
    groupBoxGeometryImage.setLayout(formLayout)

    return groupBoxGeometryImage

QGroupBox* PropertyEditor::createGroupBoxMiscImage():
    groupBoxMiscImage = new QGroupBox(tr("Misc"), this)

    toolButtonImageName = createToolButton("blank", tr("Name"))
    toolButtonImagePath = createToolButton("blank", tr("Path"))

    lineEditImageName = createLineEdit("double", 1)
    lineEditImagePath = createLineEdit("double", 1)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonImageName, lineEditImageName)
    formLayout.addRow(toolButtonImagePath, lineEditImagePath)
    groupBoxMiscImage.setLayout(formLayout)

    return groupBoxMiscImage

QGroupBox* PropertyEditor::createGroupBoxGeometryInfiniteLine():
    groupBoxGeometryInfiniteLine = new QGroupBox(tr("Geometry"), this)

    toolButtonInfiniteLineX1 = createToolButton("blank", tr("Start X"))
    toolButtonInfiniteLineY1 = createToolButton("blank", tr("Start Y"))
    toolButtonInfiniteLineX2 = createToolButton("blank", tr("2nd X"))
    toolButtonInfiniteLineY2 = createToolButton("blank", tr("2nd Y"))
    toolButtonInfiniteLineVectorX = createToolButton("blank", tr("Vector X"))
    toolButtonInfiniteLineVectorY = createToolButton("blank", tr("Vector Y"))

    lineEditInfiniteLineX1 = createLineEdit("double", 0)
    lineEditInfiniteLineY1 = createLineEdit("double", 0)
    lineEditInfiniteLineX2 = createLineEdit("double", 0)
    lineEditInfiniteLineY2 = createLineEdit("double", 0)
    lineEditInfiniteLineVectorX = createLineEdit("double", 1)
    lineEditInfiniteLineVectorY = createLineEdit("double", 1)

    //TODO: mapSignal for infinite lines

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonInfiniteLineX1, lineEditInfiniteLineX1)
    formLayout.addRow(toolButtonInfiniteLineY1, lineEditInfiniteLineY1)
    formLayout.addRow(toolButtonInfiniteLineX2, lineEditInfiniteLineX2)
    formLayout.addRow(toolButtonInfiniteLineY2, lineEditInfiniteLineY2)
    formLayout.addRow(toolButtonInfiniteLineVectorX,
        lineEditInfiniteLineVectorX)
    formLayout.addRow(toolButtonInfiniteLineVectorY,
        lineEditInfiniteLineVectorY)
    groupBoxGeometryInfiniteLine.setLayout(formLayout)

    return groupBoxGeometryInfiniteLine

QGroupBox* PropertyEditor::createGroupBoxGeometryLine():
    groupBoxGeometryLine = new QGroupBox(tr("Geometry"), this)

    toolButtonLineStartX = createToolButton("blank", tr("Start X"))
    toolButtonLineStartY = createToolButton("blank", tr("Start Y"))
    toolButtonLineEndX = createToolButton("blank", tr("End X"))
    toolButtonLineEndY = createToolButton("blank", tr("End Y"))
    toolButtonLineDeltaX = createToolButton("blank", tr("Delta X"))
    toolButtonLineDeltaY = createToolButton("blank", tr("Delta Y"))
    toolButtonLineAngle = createToolButton("blank", tr("Angle"))
    toolButtonLineLength = createToolButton("blank", tr("Length"))

    lineEditLineStartX = createLineEdit("double", 0)
    lineEditLineStartY = createLineEdit("double", 0)
    lineEditLineEndX = createLineEdit("double", 0)
    lineEditLineEndY = createLineEdit("double", 0)
    lineEditLineDeltaX = createLineEdit("double", 1)
    lineEditLineDeltaY = createLineEdit("double", 1)
    lineEditLineAngle = createLineEdit("double", 1)
    lineEditLineLength = createLineEdit("double", 1)

    mapSignal(lineEditLineStartX, "lineEditLineStartX", OBJ_TYPE_LINE)
    mapSignal(lineEditLineStartY, "lineEditLineStartY", OBJ_TYPE_LINE)
    mapSignal(lineEditLineEndX, "lineEditLineEndX", OBJ_TYPE_LINE)
    mapSignal(lineEditLineEndY, "lineEditLineEndY", OBJ_TYPE_LINE)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonLineStartX, lineEditLineStartX)
    formLayout.addRow(toolButtonLineStartY, lineEditLineStartY)
    formLayout.addRow(toolButtonLineEndX, lineEditLineEndX)
    formLayout.addRow(toolButtonLineEndY, lineEditLineEndY)
    formLayout.addRow(toolButtonLineDeltaX, lineEditLineDeltaX)
    formLayout.addRow(toolButtonLineDeltaY, lineEditLineDeltaY)
    formLayout.addRow(toolButtonLineAngle, lineEditLineAngle)
    formLayout.addRow(toolButtonLineLength, lineEditLineLength)
    groupBoxGeometryLine.setLayout(formLayout)

    return groupBoxGeometryLine

QGroupBox* PropertyEditor::createGroupBoxGeometryPath():
    groupBoxGeometryPath = new QGroupBox(tr("Geometry"), this)

    toolButtonPathVertexNum = createToolButton("blank", tr("Vertex #"))
    toolButtonPathVertexX = createToolButton("blank", tr("Vertex X"))
    toolButtonPathVertexY = createToolButton("blank", tr("Vertex Y"))
    toolButtonPathArea = createToolButton("blank", tr("Area"))
    toolButtonPathLength = createToolButton("blank", tr("Length"))

    comboBoxPathVertexNum = createComboBox(0)
    lineEditPathVertexX = createLineEdit("double", 0)
    lineEditPathVertexY = createLineEdit("double", 0)
    lineEditPathArea = createLineEdit("double", 1)
    lineEditPathLength = createLineEdit("double", 1)

    //TODO: mapSignal for paths

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonPathVertexNum, comboBoxPathVertexNum)
    formLayout.addRow(toolButtonPathVertexX, lineEditPathVertexX)
    formLayout.addRow(toolButtonPathVertexY, lineEditPathVertexY)
    formLayout.addRow(toolButtonPathArea, lineEditPathArea)
    formLayout.addRow(toolButtonPathLength, lineEditPathLength)
    groupBoxGeometryPath.setLayout(formLayout)

    return groupBoxGeometryPath

QGroupBox* PropertyEditor::createGroupBoxMiscPath():
    groupBoxMiscPath = new QGroupBox(tr("Misc"), this)

    toolButtonPathClosed = createToolButton("blank", tr("Closed"))

    comboBoxPathClosed = createComboBox(0)

    //TODO: mapSignal for paths

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonPathClosed, comboBoxPathClosed)
    groupBoxMiscPath.setLayout(formLayout)

    return groupBoxMiscPath


QGroupBox* PropertyEditor::createGroupBoxGeometryPolygon():
    groupBoxGeometryPolygon = new QGroupBox(tr("Geometry"), this)

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
        0, "blank", "Vertex Radius", LINE_EDIT_MODE,
        "lineEditPolygonVertexRadius"
    }

    toolButtonPolygonRadiusSide = createToolButton("blank",
        tr("Side Radius"))
    toolButtonPolygonDiameterVertex = createToolButton("blank",
        tr("Vertex Diameter"))
    toolButtonPolygonDiameterSide = createToolButton("blank",
       tr("Side Diameter"))
    toolButtonPolygonInteriorAngle = createToolButton("blank",
       tr("Interior Angle"))

    lineEditPolygonRadiusSide = createLineEdit("double", 0)
    lineEditPolygonDiameterVertex = createLineEdit("double", 0)
    lineEditPolygonDiameterSide = createLineEdit("double", 0)
    lineEditPolygonInteriorAngle = createLineEdit("double", 1)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonPolygonRadiusSide,
        lineEditPolygonRadiusSide)
    formLayout.addRow(toolButtonPolygonDiameterVertex,
        lineEditPolygonDiameterVertex)
    formLayout.addRow(toolButtonPolygonDiameterSide,
        lineEditPolygonDiameterSide)
    formLayout.addRow(toolButtonPolygonInteriorAngle,
        lineEditPolygonInteriorAngle)
    groupBoxGeometryPolygon.setLayout(formLayout)

    return groupBoxGeometryPolygon

QGroupBox* PropertyEditor::createGroupBoxGeometryPolyline():
    groupBoxGeometryPolyline = new QGroupBox(tr("Geometry"), this)

    toolButtonPolylineVertexNum = createToolButton("blank", tr("Vertex #"))
    toolButtonPolylineVertexX = createToolButton("blank", tr("Vertex X"))
    toolButtonPolylineVertexY = createToolButton("blank", tr("Vertex Y"))
    toolButtonPolylineArea = createToolButton("blank", tr("Area"))
    toolButtonPolylineLength = createToolButton("blank", tr("Length"))

    comboBoxPolylineVertexNum = createComboBox(0)
    lineEditPolylineVertexX = createLineEdit("double", 0)
    lineEditPolylineVertexY = createLineEdit("double", 0)
    lineEditPolylineArea = createLineEdit("double", 1)
    lineEditPolylineLength = createLineEdit("double", 1)

    //TODO: mapSignal for polylines

    QFormLayout* formLayout = new QFormLayout(this)
    "comboBoxPolylineVertexNum"
    "lineEditPolylineVertexX"
    "lineEditPolylineVertexY"
    "lineEditPolylineArea"
    "lineEditPolylineLength"
    groupBoxGeometryPolyline.setLayout(formLayout)

    return groupBoxGeometryPolyline

QGroupBox* PropertyEditor::createGroupBoxGeometryRay():
    toolButtonRayX2 = createToolButton()
    toolButtonRayY2 = createToolButton("blank", tr("2nd Y"))
    toolButtonRayVectorX = createToolButton("blank", tr("Vector X"))
    toolButtonRayVectorY = createToolButton("blank", tr("Vector Y"))

    "blank", "Start X", 0, "lineEditRayX1"
    "blank", "Start Y", 0, "lineEditRayY1"
    "blank", "2nd X", 0, "lineEditRayX2"
    "blank", "2nd Y", 0, "lineEditRayY2"
    "blank", "Vector X", 1, "lineEditRayVectorX"
    1, "lineEditRayVectorY"
}

QGroupBox* PropertyEditor::createGroupBoxGeometryTextMulti():
    groupBoxGeometryTextMulti = new QGroupBox(tr("Geometry"), this)

    toolButtonTextMultiX = createToolButton("blank", tr("Position X"))
    toolButtonTextMultiY = createToolButton("blank", tr("Position Y"))

    lineEditTextMultiX = createLineEdit("double", 0)
    lineEditTextMultiY = createLineEdit("double", 0)


    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonTextMultiX, lineEditTextMultiX)
    formLayout.addRow(toolButtonTextMultiY, lineEditTextMultiY)
    groupBoxGeometryTextMulti.setLayout(formLayout)

    return groupBoxGeometryTextMulti

QGroupBox* PropertyEditor::createGroupBoxTextTextSingle():
    groupBoxTextTextSingle = new QGroupBox(tr("Text"), this)

    {
        "blank",
        "Contents",
        "toolButtonTextSingleContents"
    },
    toolButtonTextSingleFont = createToolButton("blank", tr("Font"))
    toolButtonTextSingleJustify = createToolButton("blank", tr("Justify"))
    toolButtonTextSingleHeight = createToolButton("blank", tr("Height"))
    toolButtonTextSingleRotation = createToolButton("blank", tr("Rotation"))

    lineEditTextSingleContents = createLineEdit("string", 0)
    comboBoxTextSingleFont = createFontComboBox(0)
    comboBoxTextSingleJustify = createComboBox(0)
    lineEditTextSingleHeight = createLineEdit("double", 0)
    lineEditTextSingleRotation = createLineEdit("double", 0)

    mapSignal(lineEditTextSingleContents,
       "lineEditTextSingleContents", OBJ_TYPE_TEXTSINGLE)
    mapSignal(comboBoxTextSingleFont,
        "comboBoxTextSingleFont", OBJ_TYPE_TEXTSINGLE)
    mapSignal(comboBoxTextSingleJustify,
        "comboBoxTextSingleJustify", OBJ_TYPE_TEXTSINGLE)
    mapSignal(lineEditTextSingleHeight,
        "lineEditTextSingleHeight", OBJ_TYPE_TEXTSINGLE)
    mapSignal(lineEditTextSingleRotation,
        "lineEditTextSingleRotation", OBJ_TYPE_TEXTSINGLE)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonTextSingleContents,
        lineEditTextSingleContents)
    formLayout.addRow(toolButtonTextSingleFont,
        comboBoxTextSingleFont)
    formLayout.addRow(toolButtonTextSingleJustify,
        comboBoxTextSingleJustify)
    formLayout.addRow(toolButtonTextSingleHeight,
        lineEditTextSingleHeight)
    formLayout.addRow(toolButtonTextSingleRotation,
        lineEditTextSingleRotation)
    groupBoxTextTextSingle.setLayout(formLayout)

    return groupBoxTextTextSingle

QGroupBox* PropertyEditor::createGroupBoxGeometryTextSingle():
    groupBoxGeometryTextSingle = new QGroupBox(tr("Geometry"), this)

    toolButtonTextSingleX = createToolButton("blank", tr("Position X"))
    toolButtonTextSingleY = createToolButton("blank", tr("Position Y"))

    lineEditTextSingleX = createLineEdit("double", 0)
    lineEditTextSingleY = createLineEdit("double", 0)

    mapSignal(lineEditTextSingleX, "lineEditTextSingleX", OBJ_TYPE_TEXTSINGLE)
    mapSignal(lineEditTextSingleY, "lineEditTextSingleY", OBJ_TYPE_TEXTSINGLE)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonTextSingleX, lineEditTextSingleX)
    formLayout.addRow(toolButtonTextSingleY, lineEditTextSingleY)
    groupBoxGeometryTextSingle.setLayout(formLayout)

    return groupBoxGeometryTextSingle

QGroupBox* PropertyEditor::createGroupBoxMiscTextSingle():
    groupBoxMiscTextSingle = new QGroupBox(tr("Misc"), this)

    toolButtonTextSingleBackward = createToolButton("blank",
        tr("Backward"))
    toolButtonTextSingleUpsideDown = createToolButton("blank",
        tr("UpsideDown"))

    comboBoxTextSingleBackward = createComboBox(0)
    comboBoxTextSingleUpsideDown = createComboBox(0)

    mapSignal(comboBoxTextSingleBackward,
        "comboBoxTextSingleBackward", OBJ_TYPE_TEXTSINGLE)
    mapSignal(comboBoxTextSingleUpsideDown,
        "comboBoxTextSingleUpsideDown", OBJ_TYPE_TEXTSINGLE)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout.addRow(toolButtonTextSingleBackward,
        comboBoxTextSingleBackward)
    formLayout.addRow(toolButtonTextSingleUpsideDown,
        comboBoxTextSingleUpsideDown)
    groupBoxMiscTextSingle.setLayout(formLayout)

    return groupBoxMiscTextSingle

