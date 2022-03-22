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

from .data import *
from .config import *

"""
#
TODO: ACTION_spellcheck 
TODO: ACTION_quickselect 
*/

DOLPHIN_NUM_POINTS                 0
DOLPHIN_XSCALE                     1
DOLPHIN_YSCALE                     2

ELLIPSE_MAJORDIAMETER_MINORRADIUS  0
ELLIPSE_MAJORRADIUS_MINORRADIUS    1
ELLIPSE_ROTATION                   2

POLYGON_NUM_SIDES                  0
POLYGON_CENTER_PT                  1
POLYGON_POLYTYPE                   2
POLYGON_INSCRIBE                   3
POLYGON_CIRCUMSCRIBE               4
POLYGON_DISTANCE                   5
POLYGON_SIDE_LEN                   6

TREBLE_CLEF_MODE_NUM_POINTS        0
TREBLE_CLEF_MODE_XSCALE            1
TREBLE_CLEF_MODE_YSCALE            2


typedef struct Text_Properties 
    float size
    float angle
    int bold
    int italic
    int underline
    int overline
    int strikeout
    int backward
    int upsidedown
} text_properties


typedef struct circle_args_ 
    float x1
    float y1
    float x2
    float y2
    float x3
    float y3
    float rad
    float dia
    float cx
    float cy
    int mode
} circle_args

typedef struct dolphin_args_ 
    int numPoints
    float cx
    float cy
    float sx
    float sy
    int mode
} dolphin_args

typedef struct ellipse_args_ 
    float x1
    float y1
    float x2
    float y2
    float x3
    float y3
    float cx
    float cy
    float width
    float height
    float rot
    int mode
} ellipse_args

typedef struct user_quad__ 
    int flag
    float left
    float right
    float top
    float bottom
    float red
    float green
    float blue
} user_quad_

typedef struct treble_clef_ 
    int num_points
    double cx
    double cy
    double sx
    double sy
    int mode
} treble_clef

# C Data for embroidermodder

extern int *toolbars[], *menus = ""

extern action action_list = ""

extern int undo_history_length, undo_history_position
actions_strings[], *tips[], *toolbar_label[], *folders[],
    *menu_label[], *settings_tab_label[], *status_bar_label[], *obj_names[],
    *symbol_list[], * _appName_, * _appVer_
extern char undo_history[1000][100]
extern int exitApp
extern settings_wrapper settings, preview, dialog, accept_
origin_string = ""

extern widget *root
extern int debug_mode

# C functions for embroidermodder

def to_lower(char *, char *)
def usage()
def version()
def debug_message(format, ...)
def app_dir(char *string, int folder)
int file_exists(char *fname)
int new_main(int argc, char *argv[])
double radians(double)
double degrees(double)
double sgn(double x)
double theta(double x)
def key_handler(int c, int x, int y)
# void render_quadlist(quad *qlist); */
def menu___(int key)
def display()
char *translate(char *a)

def comboBoxScrollBarWidgetCurrentIndexChanged(int)
def checkBoxTipOfTheDayStateChanged(int)
def checkBoxUseOpenGLStateChanged(int)
def checkBoxRenderHintAAStateChanged(int)
def checkBoxRenderHintTextAAStateChanged(int)
def checkBoxRenderHintSmoothPixStateChanged(int)
def checkBoxRenderHintHighAAStateChanged(int)
def checkBoxRenderHintNonCosmeticStateChanged(int)
def spinBoxZoomScaleInValueChanged(double)
def spinBoxZoomScaleOutValueChanged(double)
def checkBoxDisableBGStateChanged(int)
def spinBoxGridCenterXValueChanged(double)
def spinBoxGridCenterYValueChanged(double)
def spinBoxGridSizeXValueChanged(double)
def spinBoxGridSizeYValueChanged(double)
def spinBoxGridSpacingXValueChanged(double)
def spinBoxGridSpacingYValueChanged(double)
def spinBoxGridSizeRadiusValueChanged(double)
def spinBoxGridSpacingRadiusValueChanged(double)
def spinBoxGridSpacingAngleValueChanged(double)
def checkBoxRulerShowOnLoadStateChanged(int)
def checkBoxQSnapEndPointStateChanged(int)
def checkBoxQSnapMidPointStateChanged(int)
def checkBoxQSnapCenterStateChanged(int)
def checkBoxQSnapNodeStateChanged(int)
def checkBoxQSnapQuadrantStateChanged(int)
def checkBoxQSnapIntersectionStateChanged(int)
def checkBoxQSnapExtensionStateChanged(int)
def checkBoxQSnapInsertionStateChanged(int)
def checkBoxQSnapPerpendicularStateChanged(int)
def checkBoxQSnapTangentStateChanged(int)
def checkBoxQSnapNearestStateChanged(int)
def checkBoxQSnapApparentStateChanged(int)
def checkBoxQSnapParallelStateChanged(int)
def spinBoxRecentMaxFilesValueChanged(int)
def spinBoxTrimDstNumJumpsValueChanged(int)
def checkBoxGridShowOnLoadStateChanged(int)
def checkBoxGridShowOriginStateChanged(int)
def checkBoxSelectionModePickFirstStateChanged(int)
def checkBoxSelectionModePickAddStateChanged(int)
def checkBoxSelectionModePickDragStateChanged(int)
def sliderSelectionGripSizeValueChanged(int)
def sliderSelectionPickBoxSizeValueChanged(int)
def spinBoxRulerPixelSizeValueChanged(double)

def settingsSnap()
def settingsGrid()
def settingsRuler()
def settingsOrtho()
def settingsPolar()
def settingsQSnap()
def settingsQTrack()
def settingsLwt()
def toggleSnap(int on)
def toggleGrid(int on)
def toggleRuler(int on)
def toggleOrtho(int on)
def togglePolar(int on)
def toggleQSnap(int on)
def toggleQTrack(int on)
def toggleLwt(int on)
def enableLwt()
def disableLwt()
def enableReal()
def disableReal()

def actuator(char *call)

EmbVector unit_vector(float angle)
EmbVector rotate_vector(EmbVector a, float angle)
EmbVector scale_vector(EmbVector a, float scale)
EmbVector scale_and_rotate(EmbVector a, float scale, float angle)

def main_print()
    debug_message("print()")

def whatsthisContextHelp():

def makeLayerCurrent():

def layerSelector():


def designDetails():


def main_cut():
    debug_message("cut()")
    gview = _mainWin->activeView()
    if gview:
        gview->cut()


def main_copy()
    debug_message("copy()")
    gview = _mainWin->activeView()
    if gview:
        gview->copy()


def main_paste():
    debug_message("main_paste()")
    View* gview = _mainWin->activeView()
    if (gview) {
        gview->paste()


def main_redo():
    debug_message("copy()")
    View* gview = _mainWin->activeView()
    if (gview) {
        gview->copy()


def main_undo():
    debug_message("main_paste()")
    View* gview = _mainWin->activeView()
    if gview:
        gview->paste()


def tipOfTheDay():
    debug_message("main_paste()")


def changelog():
    debug_message("changelog()")

    # display in a custom widget instead
    #
    # QUrl changelogURL("help/changelog.html")
    # QDesktopServices::openUrl(changelogURL)


def show_all_layers():


def freezeAllLayers():


}

def thawAllLayers()

}

def lockAllLayers()

}

def unlockAllLayers()

}

def hideAllLayers()

}

def lineWeightSelector()

}

def lineTypeSelector()

}

def colorSelector()

}

def windowClose()

}

def windowTile()

}

def windowCloseAll()

}

def windowCascade():
    debug_message(".")


def windowNext():
    debug_message(".")


def windowPrevious():
    debug_message(".")


def textItalic():
    settings["text_style_italic"] = not settings.text_style.italic

def textBold():
    settings["text_style_bold"] = not settings.text_style.bold

def textStrikeout():
    settings.text_style.strikeout = not settings.text_style.strikeout

def textUnderline():
    settings.text_style.underline = !settings.text_style.underline

def textOverline():
    settings.text_style.overline = !settings.text_style.overline


def makeLayerActive()
    debug_message("makeLayerActive()")
    debug_message("Implement makeLayerActive.")

def layerManager():
    debug_message("layerManager()")
    debug_message("Implement layerManager.")
    /*LayerManager layman( _mainWin,  _mainWin)
    layman.exec()


def layerPrevious():
    debug_message("layerPrevious()")
    debug_message("Implement layerPrevious.")


def zoomRealtime():
    debug_message("zoomRealtime()")
    debug_message("Implement zoomRealtime.")


def zoomPrevious():
    debug_message("zoomPrevious()")
    debug_message("Implement zoomPrevious.")


def zoomWindow():
    debug_message("zoomWindow()")
    /*View* gview = _mainWin->activeView()
    if (gview) {
        gview->zoomWindow()



def zoomDynamic():
    debug_message("zoomDynamic()")
    debug_message("Implement zoomDynamic.")

def zoomScale():
    debug_message("zoomScale()")
    debug_message("Implement zoomScale.")

def zoomCenter():
    debug_message("zoomCenter()")
    debug_message("Implement zoomCenter.")

def zoomIn():
    debug_message("zoomIn()")

def zoomOut():
    debug_message("zoomOut()")

def zoomSelected():
    debug_message("zoomSelected()")

def zoomAll():
    debug_message("zoomAll()")
    debug_message("Implement zoomAll.")

def zoomExtents():
    debug_message("zoomExtents()")

def panrealtime():
    debug_message("panrealtime()")

def panpoint():
    debug_message("panpoint()")

def panLeft():
    debug_message("panLeft()")

def panRight():
    debug_message("panRight()")

def panUp():
    debug_message("panUp()")

def panDown():
    debug_message("panDown()")

def dayVision():
    #if 0
    View* gview = _mainWin->activeView()
    if (gview) {
        gview->setBackgroundColor(qRgb(255,255,255)); /*TODO: Make day vision color settings.*/
        gview->setCrossHairColor(qRgb(0,0,0));        /*TODO: Make day vision color settings.*/
        gview->setGridColor(qRgb(0,0,0));             /*TODO: Make day vision color settings.*/
    }
    #endif
}

def nightVision():
    #if 0
    View* gview = _mainWin->activeView()
    if (gview) {
        gview->setBackgroundColor(qRgb(0,0,0)); /* TODO: Make night vision color settings. */
        gview->setCrossHairColor(qRgb(255,255,255)); /*TODO: Make night vision color settings.*/
        gview->setGridColor(qRgb(255,255,255));      /*TODO: Make night vision color settings.*/
    }
    #endif
}

def doNothing():
    /* This function intentionally does nothing. */
    debug_message("doNothing()")


def actuator(char *call):
    int id
    undo_history_position++
    /* an action has been taken, we are at the current head of the stack */
    undo_history_length = undo_history_position
    strcpy(undo_history[undo_history_position], call)
    id = call[0]
    if (id < 0) {
        id += 256
    }
    if (id < N_ACTIONS) {
        action_list[id].function()
    }
}


def get_n_ints(command, int *out, int n)
def get_n_floats(command, float *out, int n)

/* This is similar to using an svg path, we can blend these systems
 * later. */
 #if 0
QPixmap *draw_pixmap(description):
    char *ptr
    int int_buffer[4]
    QPixmap *icon
    QPainter *painter
    QPen pen
    get_n_ints(description, int_buffer, 2)
    icon = new QPixmap(int_buffer[0], int_buffer[1])
    painter = new QPainter(icon)
    pen.setWidth(10)
    for (ptr=(char*)description; *ptr; ptr++) {
        /* Other functions we can use are eraseRect, drawArc etc. https://doc.qt.io/qt-5/qpainter.html */
        if (strncmp(ptr, "rect", 4)==0) {
            pen.setColor(QColor(QRgb(0x000000)))
            painter->setPen(pen)
            get_n_ints(ptr+5, int_buffer, 4)
            painter->fillRect(int_buffer[0], int_buffer[1],
                int_buffer[2], int_buffer[3], Qt::SolidPattern); 
        }
    }
    return icon

QIcon loadIcon(*icon):
    /* so we can experiment with different icon generation methods */
    if (icon[0][0] == 'C') {
        return QIcon(*draw_pixmap(icon[0]+2))
    }
    return QIcon(QPixmap(icon))

#endif
def get_n_ints(command, int *out, int n):
    int i
    char modifyable[100]
    strcpy(modifyable, command)
    char *rest = (char*)modifyable
    for (i=0; i<n; i++) {
        char *tok = strtok_r(rest, " ", &rest)
        out[i] = atoi(tok)
    }
}

def get_n_floats(command, float *out, int n):
    int i
    char modifyable[100]
    strcpy(modifyable, command)
    char *rest = (char*)modifyable
    for (i=0; i<n; i++) {
        char *tok = strtok_r(rest, " ", &rest)
        out[i] = atof(tok)
    }
}

#if 0
def add_to_path(QPainterPath *path, command, float pos[2], float scale[2]):
    int j
    float out[10]
    for (j=0; j<strlen(command); j++) {
        switch (command[j]) {
        case 'M':
            get_n_floats(command+j+2, out, 2)
            path->moveTo(pos[0]+out[0]*scale[0], pos[1]+out[1]*scale[1])
            break
        case 'L':
            get_n_floats(command+j+2, out, 2)
            path->lineTo(pos[0]+out[0]*scale[0], pos[1]+out[1]*scale[1])
            break
        case 'A':
            get_n_floats(command+j+2, out, 6)
            path->arcTo(pos[0]+out[0]*scale[0], pos[1]+out[1]*scale[1],
                        out[2], out[3], out[4], out[5])
            break
        case 'a':
            get_n_floats(command+j+2, out, 5)
            path->arcMoveTo(pos[0]+out[0]*scale[0], pos[1]+out[1]*scale[1],
                        out[2]*scale[0], out[3]*scale[1],
                        out[4])
            break
        case 'E':
            get_n_floats(command+j+2, out, 4)
            path->addEllipse(
                QPointF(pos[0]+out[0]*scale[0],  pos[1]+out[1]*scale[1]),
                out[2]*scale[0], out[3]*scale[1])
            break
        case 'Z':
            path->closeSubpath()
            break
        default:
            break
        }
    }
}

def add_list_to_path(QPainterPath *path, commands[], float pos[2], float scale[2]):
    for (int i=0; origin_string[i][0]; i++) {
        add_to_path(path, origin_string[i], pos, scale)
    }
}

/*NOTE: This function should be used to interpret various object types and save them as polylines for stitchOnly formats.*/
def toPolyline(EmbPattern* pattern, const QPointF& objPos, const QPainterPath& objPath, const QString& layer, const QColor& color, const QString& lineType, const QString& lineWeight):
    float startX = objPos.x()
    float startY = objPos.y()
    EmbArray* pointList = embArray_create(EMB_POINT)
    QPainterPath::Element element
    for(int i = 0; i < objPath.elementCount(); ++i)
    {
        element = objPath.elementAt(i)
        EmbPointObject a
        a.point.x = element.x + startX
        a.point.y = -(element.y + startY)
        embArray_addPoint(pointList, &a)
    }
    EmbPolylineObject* polyObject
    polyObject = (EmbPolylineObject *) malloc(sizeof(EmbPolylineObject))
    polyObject->pointList = pointList
    polyObject->color = embColor_make(color.red(), color.green(), color.blue())
    polyObject->lineType = 1; /*TODO: proper lineType*/
    embPattern_addPolylineObjectAbs(pattern, polyObject)
#endif
"""

def settingsSnap():
    debug_message("stub")

def settingsGrid():
    debug_message("stub")

def settingsRuler():
    debug_message("stub")

def settingsOrtho():
    debug_message("stub")

def settingsPolar():
    debug_message("stub")

def settingsQSnap():
    debug_message("stub")

def settingsQTrack():
    debug_message("stub")

def settingsLwt():
    debug_message("stub")

def toggleSnap(on):
    debug_message("StatusBarButton toggleSnap()")

def toggleGrid(on):
    debug_message("StatusBarButton toggleGrid()")

def toggleRuler(on):
    debug_message("StatusBarButton toggleRuler()")

def toggleOrtho(on):
    debug_message("StatusBarButton toggleOrtho()")

def togglePolar(on):
    debug_message("StatusBarButton togglePolar()")

def toggleQSnap(on):
    debug_message("StatusBarButton toggleQSnap()")

def toggleQTrack(on):
    debug_message("StatusBarButton toggleQTrack()")

def toggleLwt(on):
    debug_message("StatusBarButton toggleLwt()")

def enableLwt():
    debug_message("StatusBarButton enableLwt()")

def disableLwt():
    debug_message("StatusBarButton disableLwt()")

def enableReal():
    debug_message("StatusBarButton enableReal()")

def disableReal():
    debug_message("StatusBarButton disableReal()")

"""
N_TEXTURES = 20

/* FUNCTION DECLARATIONS */
def clearSelection()
circle_args circle_init()

def make_texture(widget *w, char** icon, EmbVector position)

widget *make_widget(float width, float height)
def draw_widget(widget *w)
def free_widget(widget *w)

char * copy_ini_block(int i, char *data, char *section)
int find_ini_value(char *key, char *out)
int get_ini_int(char *key, int default_value)
float get_ini_float(char *key, float default_value)
int embClamp(int lower, int x, int upper)

def mouse_callback(int button, int state, int x, int y)

/* DATA SECTION */
int debug_mode = 1
GLuint texture[N_TEXTURES]
int interaction_mode = 0
int run = 1
int window_width = 640
int window_height = 480
float mouse[2]
int mouse_x = 0
int mouse_y = 0
int action_id = -1
char undo_history[1000][100]
int undo_history_length = 0
int undo_history_position = 0
settings_wrapper settings, preview, dialog, accept_
const char* _appName_ = "Embroidermodder"
const char* _appVer_ = "v2.0 alpha"
int exitApp = 0
widget *root
char assets_dir[1000]
char settings_fname[1000]
char settings_data[5000]
char value_out[1000]
int settings_data_length
float aspect = 640.0/480.0
float ui_scale = 0.1
char palette_symbols[] = " .+@#$%&*=-;>,')!"
int ntextures = 0
char user_string[100]
int ui_palette[17*3] = {
    0, 0, 0,
    0, 0, 0,
    0, 0, 0,
    0x3b, 0x3c, 0x34,
    0x3f, 0x44, 0x3e,
    0x66, 0x6f, 0x67,
    0x8f, 0x94, 0x8e,
    0xc1, 0xbb, 0xbe,
    0xc3, 0xc0, 0xc4,
    0xc3, 0xc0, 0xc4,
    0xc3, 0xc0, 0xc4,
    0xde, 0xe4, 0xe0,
    0xde, 0xe4, 0xe0,
    0xe7, 0xeb, 0xe6,
    0xe7, 0xeb, 0xe6,
    0xe7, 0xeb, 0xe6,
    0xe7, 0xeb, 0xe6,
]


def app_dir(output, folder):
#if defined(__unix__) || defined(__linux__)
    char *separator = "/"

    output = getenv("HOME")

    /* On MacOS we set a system "HOME" manually if it is not set. */
    if !output:
        struct passwd* pwd = getpwuid(getuid())
        if pwd:
            output = pwd->pw_dir
        else:
            printf("ERROR: failed to set HOME.")

#else
    separator = "\\"

    output = getenv("HOMEDRIVE") + getenv("HOMEPATH")
#endif

    output += separator + ".embroidermodder2" + separator

    if folder >= 0 and folder < nFolders:
        output += folders[folder] + separator


int file_exists(char *fname):
    struct stat stats
    return !stat(fname, &stats)

def menu___(int key):
    switch (key) {
    default:
        break


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if (action_id >= 0) {
        printf("%d\n", action_id)
        action_id = -1

    draw_widget(root)

    glutSwapBuffers()

def key_handler(int key, int x, int y):
    switch (key) {
    case 27:
        exit(0)
    default:
        break


def make_texture(widget *output, char **icon, EmbVector position):
    unsigned char data[128*128*3]
    /* xpm-style drawing routine */
    int a, j, k, npalette, pixel
    npalette = strlen(palette_symbols)
    for (a=0; a<128; a++) {
        for (j=0; j<128; j++) {
            for (k=0; k<npalette; k++) {
                if (palette_symbols[k] == icon[1+npalette+a][j]) {
                    break

            pixel = 3*(128*(127-a)+j)
            data[pixel+0] = ui_palette[3*k+0]
            data[pixel+1] = ui_palette[3*k+1]
            data[pixel+2] = ui_palette[3*k+2]

    output->width = ui_scale
    output->height = ui_scale
    output->left = position.x
    output->right = position.x+ui_scale
    output->top = position.y-ui_scale*aspect
    output->bottom = position.y
    output->texture_id = ntextures
    glBindTexture(GL_TEXTURE_2D, texture[ntextures])
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, 128, 128, 0,
        GL_RGB, GL_UNSIGNED_BYTE, data)
    ntextures++


def usage():
    fprintf(stderr,
  " ___ _____ ___  ___   __  _ ___  ___ ___   _____  __  ___  ___  ___ ___    ___ " "\n"
  "| __|     | _ \\| _ \\ /  \\| |   \\| __| _ \\ |     |/  \\|   \\|   \\| __| _ \\  |__ \\" "\n"
  "| __| | | | _ <|   /| () | | |) | __|   / | | | | () | |) | |) | __|   /  / __/" "\n"
  "|___|_|_|_|___/|_|\\_\\\\__/|_|___/|___|_|\\_\\|_|_|_|\\__/|___/|___/|___|_|\\_\\ |___|" "\n"
  " _____________________________________________________________________________ " "\n"
  "|                                                                             | "  "\n"
  "|                   http://embroidermodder.github.io                          | "  "\n"
  "|_____________________________________________________________________________| "  "\n"
  " " "\n"
  "Usage: embroidermodder [options] files ..."  "\n"
   /*80CHARS======================================================================MAX*/
  "Options:"  "\n"
  "  -d, --debug      Print lots of debugging information." "\n"
  "  -h, --help       Print this message and exit." "\n"
  "  -v, --version    Print the version number of embroidermodder and exit."  "\n"
  "\n"
           )
    exitApp = 1

def version():
    fprintf(stdout, "%s %s\n", _appName_, _appVer_)
    exitApp = 1

def clearSelection():

}

circle_args circle_init():
    clearSelection()
    circle_args args
    args.mode = circle_mode_1P_RAD
    args.x1 = MAX_DISTANCE+1.0
    args.y1 = MAX_DISTANCE+1.0
    args.x2 = MAX_DISTANCE+1.0
    args.y2 = MAX_DISTANCE+1.0
    args.x3 = MAX_DISTANCE+1.0
    args.y3 = MAX_DISTANCE+1.0
    /*
    setPromptPrefix(translate("Specify center point for circle or [3P/2P/Ttr (tan tan radius)]: "))
    */
    return args

def mouse_callback(int button, int state, int x, int y):
    if (button==GLUT_LEFT_BUTTON) {
        if (state==GLUT_DOWN) {
            int i
            float pos_x = x/(0.5*window_width) - 1.0
            float pos_y = -y/(0.5*window_height) + 1.0
            mouse_x = x
            mouse_y = y
            for (i=0; i<2; i++) {
                widget *leaf = root->leaves[i]
                if ((leaf->left < pos_x) && (pos_x < leaf->right))
                if ((leaf->top < pos_y) && (pos_y < leaf->bottom)) {
                    action_id = i
                    break
                }
            }
        }
    }
}

#if 0
int circle_click(circle_args *args, float x, float y):
    if (args.mode == args.mode_1P_RAD) {
        if(isNaN(args.x1)) {
            args.x1 = x
            args.y1 = y
            args.cx = x
            args.cy = y
            addRubber("CIRCLE")
            setRubberMode("CIRCLE_1P_RAD")
            setRubberPoint("CIRCLE_CENTER", args.cx, args.cy)
            appendPromptHistory()
            setPromptPrefix(translate("Specify radius of circle or [Diameter]: "))
        }
        else {
            args.x2 = x
            args.y2 = y
            setRubberPoint("CIRCLE_RADIUS", args.x2, args.y2)
            vulcanize()
            appendPromptHistory()
            return
        }
    }
    else if(args.mode == circle_mode_1P_DIA) {
        if(isNaN(args.x1)) {
            error("CIRCLE", translate("This should never happen."))
        }
        else {
            args.x2 = x
            args.y2 = y
            setRubberPoint("CIRCLE_DIAMETER", args.x2, args.y2)
            vulcanize()
            appendPromptHistory()
            return
        }
    }
    else if(args.mode == args.mode_2P) {
        if(isNaN(args.x1)) {
            args.x1 = x
            args.y1 = y
            addRubber("CIRCLE")
            setRubberMode("CIRCLE_2P")
            setRubberPoint("CIRCLE_TAN1", args.x1, args.y1)
            appendPromptHistory()
            setPromptPrefix(translate("Specify second end point of circle's diameter: "))
        }
        else if(isNaN(args.x2)) {
            args.x2 = x
            args.y2 = y
            setRubberPoint("CIRCLE_TAN2", args.x2, args.y2)
            vulcanize()
            appendPromptHistory()
            return
        }
        else {
            error("CIRCLE", translate("This should never happen."))
        }
    }
    else if(args.mode == args.mode_3P) {
        if(isNaN(args.x1)) {
            args.x1 = x
            args.y1 = y
            appendPromptHistory()
            setPromptPrefix(translate("Specify second point on circle: "))
        }
        else if(isNaN(args.x2)) {
            args.x2 = x
            args.y2 = y
            addRubber("CIRCLE")
            setRubberMode("CIRCLE_3P")
            setRubberPoint("CIRCLE_TAN1", args.x1, args.y1)
            setRubberPoint("CIRCLE_TAN2", args.x2, args.y2)
            appendPromptHistory()
            setPromptPrefix(translate("Specify third point on circle: "))
        }
        else if(isNaN(args.x3)) {
            args.x3 = x
            args.y3 = y
            setRubberPoint("CIRCLE_TAN3", args.x3, args.y3)
            vulcanize()
            appendPromptHistory()
            return
        }
        else {
            error("CIRCLE", translate("This should never happen."))
        }
    }
    else if(args.mode == args.mode_TTR) {
        if (isNaN(args.x1)) {
            args.x1 = x
            args.y1 = y
            appendPromptHistory()
            setPromptPrefix(translate("Specify point on object for second tangent of circle: "))
        }
        else if (isNaN(args.x2)) {
            args.x2 = x
            args.y2 = y
            appendPromptHistory()
            setPromptPrefix(translate("Specify radius of circle: "))
        }
        else if (isNaN(args.x3)) {
            args.x3 = x
            args.y3 = y
            appendPromptHistory()
            setPromptPrefix(translate("Specify second point: "))
        }
        else {
            todo("CIRCLE", "click() for TTR")
        }
    }
    return 0

int circle_prompt(circle_args args, char *str):
    if (args.mode == args.mode_1P_RAD) {
        if (isNaN(args.x1)) {
            /* TODO: Probably should add additional qsTr calls here. */
            if (!strcmp(str, "2P")) {
                args.mode = args.mode_2P
                setPromptPrefix(translate("Specify first end point of circle's diameter: "))
            }
            /* TODO: Probably should add additional qsTr calls here. */
            else if (!strcmp(str, "3P")) {
                args.mode = args.mode_3P
                setPromptPrefix(translate("Specify first point of circle: "))
            }
            /* TODO: Probably should add additional qsTr calls here. */
            else if (!strcmp(str, "T") || !strcmp(str, "TTR")) {
                args.mode = args.mode_TTR
                setPromptPrefix(translate("Specify point on object for first tangent of circle: "))
            }
            else {
                var strList = str.split(",")
                if (isNaN(strList[0]) || isNaN(strList[1])) {
                    alert(translate("Point or option keyword required."))
                    setPromptPrefix(translate("Specify center point for circle or [3P/2P/Ttr (tan tan radius)]: "))
                }
                else {
                    args.x1 = Number(strList[0])
                    args.y1 = Number(strList[1])
                    args.cx = args.x1
                    args.cy = args.y1
                    addRubber("CIRCLE")
                    setRubberMode("CIRCLE_1P_RAD")
                    setRubberPoint("CIRCLE_CENTER", args.cx, args.cy)
                    setPromptPrefix(translate("Specify radius of circle or [Diameter]: "))
                }
            }
        }
        else {
            /* TODO: Probably should add additional qsTr calls here. */
            if (!strcmp(str, "D") || !strcmp(str, "DIAMETER")) {
                args.mode = circle_mode_1P_DIA
                setRubberMode("CIRCLE_1P_DIA")
                setPromptPrefix(translate("Specify diameter of circle: "))
            }
            else {
                float num = Number(str)
                if (isNaN(num)) {
                    alert(translate("Requires numeric radius, point on circumference, or \"D\"."))
                    setPromptPrefix(translate("Specify radius of circle or [Diameter]: "))
                }
                else {
                    args.rad = num
                    args.x2 = args.x1 + args.rad
                    args.y2 = args.y1
                    setRubberPoint("CIRCLE_RADIUS", args.x2, args.y2)
                    vulcanize()
                    return
                }
            }
        }
    }
    else if (args.mode == circle_mode_1P_DIA) {
        if (isNaN(args.x1)) {
            error("CIRCLE", translate("This should never happen."))
        }
        if (isNaN(args.x2)) {
            var num = Number(str)
            if(isNaN(num))
            {
                alert(translate("Requires numeric distance or second point."))
                setPromptPrefix(translate("Specify diameter of circle: "))
            }
            else
            {
                args.dia = num
                args.x2 = args.x1 + args.dia
                args.y2 = args.y1
                setRubberPoint("CIRCLE_DIAMETER", args.x2, args.y2)
                vulcanize()
                return
            }
        }
        else
        {
            error("CIRCLE", translate("This should never happen."))
        }
    }
    else if(args.mode == args.mode_2P)
    {
        if(isNaN(args.x1))
        {
            var strList = str.split(",")
            if(isNaN(strList[0]) || isNaN(strList[1])):
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify first end point of circle's diameter: "))
            else:
                args.x1 = Number(strList[0])
                args.y1 = Number(strList[1])
                addRubber("CIRCLE")
                setRubberMode("CIRCLE_2P")
                setRubberPoint("CIRCLE_TAN1", args.x1, args.y1)
                setPromptPrefix(translate("Specify second end point of circle's diameter: "))
        elif(isNaN(args.x2)):
            strList = str.split(",")
            if isNaN(strList[0]) or isNaN(strList[1]):
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify second end point of circle's diameter: "))
            else:
                args.x2 = Number(strList[0])
                args.y2 = Number(strList[1])
                setRubberPoint("CIRCLE_TAN2", args.x2, args.y2)
                vulcanize()
                return
        else:
            error("CIRCLE", translate("This should never happen."))

    else if(args.mode == args.mode_3P):
        if(isNaN(args.x1)):
            var strList = str.split(",")
            if(isNaN(strList[0]) || isNaN(strList[1])):
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify first point of circle: "))
            else:
                args.x1 = Number(strList[0])
                args.y1 = Number(strList[1])
                setPromptPrefix(translate("Specify second point of circle: "))

        elif(isNaN(args.x2)):
        {
            var strList = str.split(",")
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify second point of circle: "))
            }
            else
            {
                args.x2 = Number(strList[0])
                args.y2 = Number(strList[1])
                addRubber("CIRCLE")
                setRubberMode("CIRCLE_3P")
                setRubberPoint("CIRCLE_TAN1", args.x1, args.y1)
                setRubberPoint("CIRCLE_TAN2", args.x2, args.y2)
                setPromptPrefix(translate("Specify third point of circle: "))
            }
        }
        else if(isNaN(args.x3)) {
            var strList = str.split(",")
            if (isNaN(strList[0]) || isNaN(strList[1])) {
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify third point of circle: "))
            }
            else {                
                args.x3 = Number(strList[0])
                args.y3 = Number(strList[1])
                setRubberPoint("CIRCLE_TAN3", args.x3, args.y3)
                vulcanize()
                return
            }
        }
        else
        {
            error("CIRCLE", translate("This should never happen."))
        }
        
    }
    else if(args.mode == args.mode_TTR) {
        todo("CIRCLE", "prompt() for TTR")
    }
    return 0

class line():
    def __init__(self):
        clearSelection()
        self.x1 = MAX_DISTANCE+1.0
        self.y1 = MAX_DISTANCE+1.0
        self.x2 = MAX_DISTANCE+1.0
        self.y2 = MAX_DISTANCE+1.0
        setPromptPrefix(translate("Specify first point: "))

    def click(x, y):
        if isNaN(self.x1):
            self.x1 = x
            self.y1 = y
            addRubber("LINE")
            setRubberMode("LINE")
            setRubberPoint("LINE_START", args.x1, args.y1)
            appendPromptHistory()
            setPromptPrefix(translate("Specify second point: "))
        else:
            appendPromptHistory()
            self.x2 = x
            self.y2 = y
            reportDistance()

int prompt(str):
    var strList = str.split(",")
    if (isNaN(args.x1)) {
        if (isNaN(strList[0]) || isNaN(strList[1])) {
            alert(translate("Requires numeric distance or two points."))
            setPromptPrefix(translate("Specify first point: "))
        }
        else {
            args.x1 = Number(strList[0])
            args.y1 = Number(strList[1])
            addRubber("LINE")
            setRubberMode("LINE")
            setRubberPoint("LINE_START", args.x1, args.y1)
            setPromptPrefix(translate("Specify second point: "))
        }
    }
    else
    {
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(translate("Requires numeric distance or two points."))
            setPromptPrefix(translate("Specify second point: "))
        }
        else
        {
            args.x2 = Number(strList[0])
            args.y2 = Number(strList[1])
            reportDistance()
            return
        }
    }
}

/* Cartesian Coordinate System reported:
 *
 *               (+)
 *               90
 *               |
 *      (-) 180__|__0 (+)
 *               |
 *              270
 *              (-)
 */

int reportDistance():
    var dx = args.x2 - args.x1
    var dy = args.y2 - args.y1

    var dist = calculateDistance(args.x1,args.y1,args.x2, args.y2)
    var angle = calculateAngle(args.x1,args.y1,args.x2, args.y2)

    setPromptPrefix(translate("Distance") + " = " + dist.toString() + ", " + translate("Angle") + " = " + angle.toString())
    appendPromptHistory()
    setPromptPrefix(translate("Delta X") + " = " + dx.toString() + ", " + translate("Delta Y") + " = " + dy.toString())
    appendPromptHistory()

/* ---------------------------------------------------------------------- */

dolphin_args dolphin_init():
    dolphin_args args
    clearSelection()
    args.numPoints = 512; /*Default //TODO: min:64 max:8192*/
    args.cx = MAX_DISTANCE+1.0
    args.cy = MAX_DISTANCE+1.0
    args.sx = 0.04; /*Default*/
    args.sy = 0.04; /*Default*/
    args.mode = DOLPHIN_MODE_NUM_POINTS


    addRubber("POLYGON")
    setRubberMode("POLYGON")
    updateDolphin(args, args.numPoints, args.sx, args.sy)
    spareRubber("POLYGON")
    return args
#endif

def basis_func(A, B, C, D, E):
    return (A/B)*math.sin(C*t+(D/E))

int dolphin_update(dolphin_args args, int numPts, float xScale, float yScale):
    int i

    for (i=0; i<=numPts; i++) {
        float t, xx, yy
        t = (2*embConstantPi)/numPts*i; 

        xx = basis_func(4, 23, -58, 62, 33)+
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
        5/16*sin(59*t+32/39)

        yy = 5/11*sin(163/37-59*t)+
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
        34/25*sin(54*t+37/26)

        /*
        setRubberPoint("POLYGON_POINT_" + i.toString(), xx*xScale, yy*yScale)
        */
    }

    /*
    setRubberText("POLYGON_NUM_POINTS", numPts.toString()); */
    return 0

#if 0

/* ---------------------------------------------------------------------- */

ellipse_args ellipse_init():
    ellipse_args args
    clearSelection()
    args.mode = ELLIPSE_MAJORDIAMETER_MINORRADIUS
    args.point1 = {NaN, NaN]
    args.point2 = {NaN, NaN]
    args.point3 = {NaN, NaN]
    setPromptPrefix(translate("Specify first axis start point or [Center]: "))
    return args

int ellipse_click(EmbVector point):
    if (args.mode == ELLIPSE_MAJORDIAMETER_MINORRADIUS) {
        if (isNaN(args.x1)) {
            args.point1 = point
            addRubber("ELLIPSE")
            setRubberMode("ELLIPSE_LINE")
            setRubberPoint("ELLIPSE_LINE_POINT1", args.x1, args.y1)
            appendPromptHistory()
            setPromptPrefix(translate("Specify first axis end point: "))
        }
        else if (isNaN(args.x2)) {
            args.point2 = point
            args.cx = (args.x1 + args.x2)/2.0
            args.cy = (args.y1 + args.y2)/2.0
            args.width = calculateDistance(args.x1, args.y1, args.x2, args.y2)
            args.rot = calculateAngle(args.x1, args.y1, args.x2, args.y2)
            setRubberMode("ELLIPSE_MAJORDIAMETER_MINORRADIUS")
            setRubberPoint("ELLIPSE_AXIS1_POINT1", args.x1, args.y1)
            setRubberPoint("ELLIPSE_AXIS1_POINT2", args.x2, args.y2)
            setRubberPoint("ELLIPSE_CENTER", args.cx, args.cy)
            setRubberPoint("ELLIPSE_WIDTH", args.width, 0)
            setRubberPoint("ELLIPSE_ROT", args.rot, 0)
            appendPromptHistory()
            setPromptPrefix(translate("Specify second axis end point or [Rotation]: "))
        }
        else if (isNaN(args.x3)) {
            args.x3 = x
            args.y3 = y
            args.height = perpendicularDistance(args.x3, args.y3, args.x1, args.y1, args.x2, args.y2)*2.0
            setRubberPoint("ELLIPSE_AXIS2_POINT2", args.x3, args.y3)
            vulcanize()
            appendPromptHistory()
            return
        }
        else {
            error("ELLIPSE", translate("This should never happen."))
        }
    }
    else if (args.mode == ELLIPSE_MAJORRADIUS_MINORRADIUS) {
        if (isNaN(args.x1)) {
            args.x1 = x
            args.y1 = y
            args.cx = args.x1
            args.cy = args.y1
            addRubber("ELLIPSE")
            setRubberMode("ELLIPSE_LINE")
            setRubberPoint("ELLIPSE_LINE_POINT1", args.x1, args.y1)
            setRubberPoint("ELLIPSE_CENTER", args.cx, args.cy)
            appendPromptHistory()
            setPromptPrefix(translate("Specify first axis end point: "))
        }
        else if(isNaN(args.x2)) {
            args.x2 = x
            args.y2 = y
            args.width = calculateDistance(args.cx, args.cy, args.x2, args.y2)*2.0
            args.rot = calculateAngle(args.x1, args.y1, args.x2, args.y2)
            setRubberMode("ELLIPSE_MAJORRADIUS_MINORRADIUS")
            setRubberPoint("ELLIPSE_AXIS1_POINT2", args.x2, args.y2)
            setRubberPoint("ELLIPSE_WIDTH", args.width, 0)
            setRubberPoint("ELLIPSE_ROT", args.rot, 0)
            appendPromptHistory()
            setPromptPrefix(translate("Specify second axis end point or [Rotation]: "))
        }
        else if(isNaN(args.x3)) {
            args.x3 = x
            args.y3 = y
            args.height = perpendicularDistance(args.x3, args.y3, args.cx, args.cy, args.x2, args.y2)*2.0
            setRubberPoint("ELLIPSE_AXIS2_POINT2", args.x3, args.y3)
            vulcanize()
            appendPromptHistory()
            return
        }
        else {
            error("ELLIPSE", translate("This should never happen."))
        }
    }
    else if(args.mode == args.mode_ELLIPSE_ROTATION) {
        if (isNaN(args.x1)) {
            error("ELLIPSE", translate("This should never happen."))
        }
        else if (isNaN(args.x2)) {
            error("ELLIPSE", translate("This should never happen."))
        }
        else if(isNaN(args.x3)) {
            var angle = calculateAngle(args.cx, args.cy, x, y)
            args.height = cos(angle*embConstantPi/180.0)*args.width
            addEllipse(args.cx, args.cy, args.width, args.height, args.rot, false)
            appendPromptHistory()
            return
        }
    }
}

int ellipse_prompt(str):
    if(args.mode == args.mode_MAJORDIAMETER_MINORRADIUS)
    {
        if(isNaN(args.x1))
        {
            if(str == "C" || str == "CENTER") /*TODO: Probably should add additional qsTr calls here.*/
            {
                args.mode = args.mode_MAJORRADIUS_MINORRADIUS
                setPromptPrefix(translate("Specify center point: "))
            }
            else
            {
                var strList = str.split(",")
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(translate("Point or option keyword required."))
                    setPromptPrefix(translate("Specify first axis start point or [Center]: "))
                }
                else
                {
                    args.x1 = Number(strList[0])
                    args.y1 = Number(strList[1])
                    addRubber("ELLIPSE")
                    setRubberMode("ELLIPSE_LINE")
                    setRubberPoint("ELLIPSE_LINE_POINT1", args.x1, args.y1)
                    setPromptPrefix(translate("Specify first axis end point: "))
                }
            }
        }
        else if(isNaN(args.x2))
        {
            var strList = str.split(",")
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify first axis end point: "))
            }
            else
            {
                args.x2 = Number(strList[0])
                args.y2 = Number(strList[1])
                args.cx = (args.x1 + args.x2)/2.0
                args.cy = (args.y1 + args.y2)/2.0
                args.width = calculateDistance(args.x1, args.y1, args.x2, args.y2)
                args.rot = calculateAngle(args.x1, args.y1, args.x2, args.y2)
                setRubberMode("ELLIPSE_MAJORDIAMETER_MINORRADIUS")
                setRubberPoint("ELLIPSE_AXIS1_POINT1", args.x1, args.y1)
                setRubberPoint("ELLIPSE_AXIS1_POINT2", args.x2, args.y2)
                setRubberPoint("ELLIPSE_CENTER", args.cx, args.cy)
                setRubberPoint("ELLIPSE_WIDTH", args.width, 0)
                setRubberPoint("ELLIPSE_ROT", args.rot, 0)
                setPromptPrefix(translate("Specify second axis end point or [Rotation]: "))
            }
        }
        else if(isNaN(args.x3))
        {
            if(str == "R" || str == "ROTATION") /*TODO: Probably should add additional qsTr calls here.*/
            {
                args.mode = args.mode_ELLIPSE_ROTATION
                setPromptPrefix(translate("Specify rotation: "))
            }
            else
            {
                var strList = str.split(",")
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(translate("Point or option keyword required."))
                    setPromptPrefix(translate("Specify second axis end point or [Rotation]: "))
                }
                else
                {
                    args.x3 = Number(strList[0])
                    args.y3 = Number(strList[1])
                    args.height = perpendicularDistance(args.x3, args.y3, args.x1, args.y1, args.x2, args.y2)*2.0
                    setRubberPoint("ELLIPSE_AXIS2_POINT2", args.x3, args.y3)
                    vulcanize()
                    return
                }
            }
        }
    }
    else if(args.mode == args.mode_MAJORRADIUS_MINORRADIUS)
    {
        if(isNaN(args.x1))
        {
            var strList = str.split(",")
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify center point: "))
            }
            else
            {
                args.x1 = Number(strList[0])
                args.y1 = Number(strList[1])
                args.cx = args.x1
                args.cy = args.y1
                addRubber("ELLIPSE")
                setRubberMode("ELLIPSE_LINE")
                setRubberPoint("ELLIPSE_LINE_POINT1", args.x1, args.y1)
                setRubberPoint("ELLIPSE_CENTER", args.cx, args.cy)
                setPromptPrefix(translate("Specify first axis end point: "))
            }
        }
        else if(isNaN(args.x2))
        {
            var strList = str.split(",")
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify first axis end point: "))
            }
            else
            {
                args.x2 = Number(strList[0])
                args.y2 = Number(strList[1])
                args.width = calculateDistance(args.x1, args.y1, args.x2, args.y2)*2.0
                args.rot = calculateAngle(args.x1, args.y1, args.x2, args.y2)
                setRubberMode("ELLIPSE_MAJORRADIUS_MINORRADIUS")
                setRubberPoint("ELLIPSE_AXIS1_POINT2", args.x2, args.y2)
                setRubberPoint("ELLIPSE_WIDTH", args.width, 0)
                setRubberPoint("ELLIPSE_ROT", args.rot, 0)
                setPromptPrefix(translate("Specify second axis end point or [Rotation]: "))
            }
        }
        else if(isNaN(args.x3))
        {
            if(str == "R" || str == "ROTATION") /*TODO: Probably should add additional qsTr calls here.*/
            {
                args.mode = args.mode_ELLIPSE_ROTATION
                setPromptPrefix(translate("Specify ellipse rotation: "))
            }
            else
            {
                var strList = str.split(",")
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(translate("Point or option keyword required."))
                    setPromptPrefix(translate("Specify second axis end point or [Rotation]: "))
                }
                else
                {
                    args.x3 = Number(strList[0])
                    args.y3 = Number(strList[1])
                    args.height = perpendicularDistance(args.x3, args.y3, args.x1, args.y1, args.x2, args.y2)*2.0
                    setRubberPoint("ELLIPSE_AXIS2_POINT2", args.x3, args.y3)
                    vulcanize()
                    return
                }
            }
        }
    }
    else if(args.mode == args.mode_ELLIPSE_ROTATION)
    {
        if(isNaN(args.x1))
        {
            error("ELLIPSE", translate("This should never happen."))
        }
        else if(isNaN(args.x2))
        {
            error("ELLIPSE", translate("This should never happen."))
        }
        else if(isNaN(args.x3))
        {
            if(isNaN(str))
            {
                alert(translate("Invalid angle. Input a numeric angle or pick a point."))
                setPromptPrefix(translate("Specify rotation: "))
            }
            else
            {
                var angle = Number(str)
                args.height = cos(angle*embConstantPi/180.0)*args.width
                addEllipse(args.cx, args.cy, args.width, args.height, args.rot, false)
                return
            }
        }
    }
}

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.numPoints = 512; /*Default //TODO: min:64 max:8192*/
args.cx
args.cy
args.sx = 1.0
args.sy = 1.0
args.numPoints
args.mode

/*enums*/
args.mode_NUM_POINTS = 0
args.mode_STYLE      = 1
args.mode_XSCALE     = 2
args.mode_YSCALE     = 3

int init():
    clearSelection()
    args.cx = MAX_DISTANCE+1.0
    args.cy = MAX_DISTANCE+1.0
    args.mode = args.mode_NUM_POINTS

    /*Heart4: 10.0 / 512*/
    /*Heart5: 1.0 / 512*/

    addRubber("POLYGON")
    setRubberMode("POLYGON")
    updateHeart("HEART5", args.numPoints, args.sx, args.sy)
    spareRubber("POLYGON")
    return

int updateHeart(style, numPts, xScale, yScale):
    var i
    var t
    var xx = MAX_DISTANCE+1.0
    var yy = MAX_DISTANCE+1.0
    var two_pi = 2*embConstantPi

    for(i = 0; i <= numPts; i++)
    {
        t = two_pi/numPts*i; 

        if(style == "HEART4")
        {
            xx = cos(t)*((sin(t)*sqrt(abs(cos(t))))/(sin(t)+7/5) - 2*sin(t) + 2)
            yy = sin(t)*((sin(t)*sqrt(abs(cos(t))))/(sin(t)+7/5) - 2*sin(t) + 2)
        }
        else if(style == "HEART5")
        {
            xx = 16*pow(sin(t), 3)
            yy = 13*cos(t) - 5*cos(2*t) - 2*cos(3*t) - cos(4*t)
        }

        setRubberPoint("POLYGON_POINT_" + i.toString(), xx*xScale, yy*yScale)
    }

    setRubberText("POLYGON_NUM_POINTS", numPts.toString())

--------------------------------------------------------------------------------


/*Command: Line*/

var global = {}; /*Required*/
args.firstRun
args.firstX
args.firstY
args.prevX
args.prevY

int init():
    clearSelection()
    args.firstRun = true
    args.firstX = MAX_DISTANCE+1.0
    args.firstY = MAX_DISTANCE+1.0
    args.prevX = MAX_DISTANCE+1.0
    args.prevY = MAX_DISTANCE+1.0
    setPromptPrefix(translate("Specify first point: "))

int click(x, y):
    if(args.firstRun)
    {
        args.firstRun = false
        args.firstX = x
        args.firstY = y
        args.prevX = x
        args.prevY = y
        addRubber("LINE")
        setRubberMode("LINE")
        setRubberPoint("LINE_START", args.firstX, args.firstY)
        appendPromptHistory()
        setPromptPrefix(translate("Specify next point or [Undo]: "))
    }
    else
    {
        setRubberPoint("LINE_END", x, y)
        vulcanize()
        addRubber("LINE")
        setRubberMode("LINE")
        setRubberPoint("LINE_START", x, y)
        appendPromptHistory()
        args.prevX = x
        args.prevY = y
    }
}

int prompt(str):
    if(args.firstRun)
    {
        var strList = str.split(",")
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(translate("Invalid point."))
            setPromptPrefix(translate("Specify first point: "))
        }
        else
        {
            args.firstRun = false
            args.firstX = Number(strList[0])
            args.firstY = Number(strList[1])
            args.prevX = args.firstX
            args.prevY = args.firstY
            addRubber("LINE")
            setRubberMode("LINE")
            setRubberPoint("LINE_START", args.firstX, args.firstY)
            setPromptPrefix(translate("Specify next point or [Undo]: "))
        }
    }
    else
    {
        if(str == "U" || str == "UNDO") /*TODO: Probably should add additional qsTr calls here.*/
        {
            todo("LINE", "prompt() for UNDO")
        }
        else
        {
            var strList = str.split(",")
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(translate("Point or option keyword required."))
                setPromptPrefix(translate("Specify next point or [Undo]: "))
            }
            else
            {
                var x = Number(strList[0])
                var y = Number(strList[1])
                setRubberPoint("LINE_END", x, y)
                vulcanize()
                addRubber("LINE")
                setRubberMode("LINE")
                setRubberPoint("LINE_START", x, y)
                args.prevX = x
                args.prevY = y
                setPromptPrefix(translate("Specify next point or [Undo]: "))
            }
        }
    }
}

--------------------------------------------------------------------------------

int init():
    clearSelection()
    setPromptPrefix(translate("Specify point: "))

int click(x, y):
    appendPromptHistory()
    setPromptPrefix("X = " + x.toString() + ", Y = " + y.toString())
    appendPromptHistory()
    return

int prompt(str):
    var strList = str.split(",")
    if(isNaN(strList[0]) || isNaN(strList[1]))
    {
        alert(translate("Invalid point."))
        setPromptPrefix(translate("Specify point: "))
    }
    else
    {
        appendPromptHistory()
        setPromptPrefix("X = " + strList[0].toString() + ", Y = " + strList[1].toString())
        appendPromptHistory()
        return
    }
}

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.firstRun
args.baseX
args.baseY
args.destX
args.destY
args.deltaX
args.deltaY

int init():
    args.firstRun = true
    args.baseX  = MAX_DISTANCE+1.0
    args.baseY  = MAX_DISTANCE+1.0
    args.destX  = MAX_DISTANCE+1.0
    args.destY  = MAX_DISTANCE+1.0
    args.deltaX = MAX_DISTANCE+1.0
    args.deltaY = MAX_DISTANCE+1.0

    if(numSelected() <= 0)
    {
        /*TODO: Prompt to select objects if nothing is preselected*/
        alert(translate("Preselect objects before invoking the move command."))
        return
        messageBox("information", translate("Move Preselect"), translate("Preselect objects before invoking the move command."))
    }
    else
    {
        setPromptPrefix(translate("Specify base point: "))
    }
}

int click(x, y):
    if(args.firstRun)
    {
        args.firstRun = false
        args.baseX = x
        args.baseY = y
        addRubber("LINE")
        setRubberMode("LINE")
        setRubberPoint("LINE_START", args.baseX, args.baseY)
        previewOn("SELECTED", "MOVE", args.baseX, args.baseY, 0)
        appendPromptHistory()
        setPromptPrefix(translate("Specify destination point: "))
    }
    else
    {
        args.destX = x
        args.destY = y
        args.deltaX = args.destX - args.baseX
        args.deltaY = args.destY - args.baseY
        moveSelected(args.deltaX, args.deltaY)
        previewOff()
        return
    }
}

int prompt(str):
    if(args.firstRun)
    {
        var strList = str.split(",")
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(translate("Invalid point."))
            setPromptPrefix(translate("Specify base point: "))
        }
        else
        {
            args.firstRun = false
            args.baseX = Number(strList[0])
            args.baseY = Number(strList[1])
            addRubber("LINE")
            setRubberMode("LINE")
            setRubberPoint("LINE_START", args.baseX, args.baseY)
            previewOn("SELECTED", "MOVE", args.baseX, args.baseY, 0)
            setPromptPrefix(translate("Specify destination point: "))
        }
    }
    else
    {
        var strList = str.split(",")
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(translate("Invalid point."))
            setPromptPrefix(translate("Specify destination point: "))
        }
        else
        {
            args.destX = Number(strList[0])
            args.destY = Number(strList[1])
            args.deltaX = args.destX - args.baseX
            args.deltaY = args.destY - args.baseY
            moveSelected(args.deltaX, args.deltaY)
            previewOff()
            return
        }
    }
}

--------------------------------------------------------------------------------

/*TODO: The path command is currently broken*/

var global = {}; /*Required*/
args.firstRun
args.firstX
args.firstY
args.prevX
args.prevY

int init():
    clearSelection()
    args.firstRun = true
    args.firstX = MAX_DISTANCE+1.0
    args.firstY = MAX_DISTANCE+1.0
    args.prevX = MAX_DISTANCE+1.0
    args.prevY = MAX_DISTANCE+1.0
    setPromptPrefix(translate("Specify start point: "))

int click(x, y):
    if(args.firstRun)
    {
        args.firstRun = false
        args.firstX = x
        args.firstY = y
        args.prevX = x
        args.prevY = y
        addPath(x,y)
        appendPromptHistory()
        setPromptPrefix(translate("Specify next point or [Arc/Undo]: "))
    }
    else
    {
        appendPromptHistory()
        appendLineToPath(x,y)
        args.prevX = x
        args.prevY = y
    }
}

int prompt(str):
    if(str == "A" || str == "ARC")/*TODO: Probably should add additional qsTr calls here.*/
    {
        todo("PATH", "prompt() for ARC")
    }
    else if(str == "U" || str == "UNDO") /*TODO: Probably should add additional qsTr calls here.*/
    {
        todo("PATH", "prompt() for UNDO")
    }
    else
    {
        var strList = str.split(",")
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(translate("Point or option keyword required."))
            setPromptPrefix(translate("Specify next point or [Arc/Undo]: "))
        }
        else
        {
            var x = Number(strList[0])
            var y = Number(strList[1])
            if(args.firstRun)
            {
                args.firstRun = false
                args.firstX = x
                args.firstY = y
                args.prevX = x
                args.prevY = y
                addPath(x,y)
                setPromptPrefix(translate("Specify next point or [Arc/Undo]: "))
            }
            else
            {
                appendLineToPath(x,y)
                args.prevX = x
                args.prevY = y
            }
        }
    }
}

int init():
    clearSelection()
    reportPlatform()
    return

int reportPlatform():
    setPromptPrefix(translate("Platform") + " = " + platformString())
    appendPromptHistory()

/* ------------------------------------------------------------------------- */

var global = {}; /*Required*/
args.firstRun

int point_init():
    clearSelection()
    args.firstRun = true
    setPromptPrefix("TODO: Current point settings: PDMODE=?  PDSIZE=?"); /*TODO: qsTr needed here when complete*/
    appendPromptHistory()
    setPromptPrefix(translate("Specify first point: "))

int point_click(x, y):
    if(args.firstRun) {
        args.firstRun = false
        appendPromptHistory()
        setPromptPrefix(translate("Specify next point: "))
        addPoint(x,y)
    }
    else {
        appendPromptHistory()
        addPoint(x,y)
    }
}

int prompt(str):
    if (args.firstRun) {
        if(str == "M" || str == "MODE") {
            /*TODO: Probably should add additional qsTr calls here.*/
            todo("POINT", "prompt() for PDMODE")
        }
        else if(str == "S" || str == "SIZE") {
            /*TODO: Probably should add additional qsTr calls here.*/
            todo("POINT", "prompt() for PDSIZE")
        }
        var strList = str.split(",")
        if (isNaN(strList[0]) || isNaN(strList[1])) {
            alert(translate("Invalid point."))
            setPromptPrefix(translate("Specify first point: "))
        }
        else
        {
            args.firstRun = false
            var x = Number(strList[0])
            var y = Number(strList[1])
            setPromptPrefix(translate("Specify next point: "))
            addPoint(x,y)
        }
    }
    else
    {
        var strList = str.split(",")
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(translate("Invalid point."))
            setPromptPrefix(translate("Specify next point: "))
        }
        else
        {
            var x = Number(strList[0])
            var y = Number(strList[1])
            setPromptPrefix(translate("Specify next point: "))
            addPoint(x,y)
        }
    }

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.centerX
args.centerY
args.sideX1
args.sideY1
args.sideX2
args.sideY2
args.pointIX
args.pointIY
args.pointCX
args.pointCY
args.polyType = "Inscribed"; /*Default*/
args.numSides = 4;           /*Default*/
args.mode


int init():
    clearSelection()
    args.center.x = MAX_DISTANCE+1.0
    args.center.y = MAX_DISTANCE+1.0
    args.sideX1  = MAX_DISTANCE+1.0
    args.sideY1  = MAX_DISTANCE+1.0
    args.sideX2  = MAX_DISTANCE+1.0
    args.sideY2  = MAX_DISTANCE+1.0
    args.pointIX = MAX_DISTANCE+1.0
    args.pointIY = MAX_DISTANCE+1.0
    args.pointCX = MAX_DISTANCE+1.0
    args.pointCY = MAX_DISTANCE+1.0
    args.mode = #define POLYGON_NUM_SIDES
    setPromptPrefix(translate("Enter number of sides") + " {" + args.numSides.toString() + "}: ")

int click(x, y):
    if (args.mode == POLYGON_NUM_SIDES) {
        /*Do nothing, the prompt controls this.*/
    }
    else if (args.mode == POLYGON_CENTER_PT) {
        args.centerX = x
        args.centerY = y
        args.mode = args.mode_POLYTYPE
        appendPromptHistory()
        setPromptPrefix(translate("Specify polygon type [Inscribed in circle/Circumscribed around circle]") + " {" + args.polyType + "}: ")
    }
    else if(args.mode == args.mode_POLYTYPE)
    {
        /*Do nothing, the prompt controls this.*/
    }
    else if(args.mode == args.mode_INSCRIBE)
    {
        args.pointIX = x
        args.pointIY = y
        setRubberPoint("POLYGON_INSCRIBE_POINT", args.pointIX, args.pointIY)
        vulcanize()
        appendPromptHistory()
        return
    }
    else if(args.mode == args.mode_CIRCUMSCRIBE)
    {
        args.pointCX = x
        args.pointCY = y
        setRubberPoint("POLYGON_CIRCUMSCRIBE_POINT", args.pointCX, args.pointCY)
        vulcanize()
        appendPromptHistory()
        return
    }
    else if(args.mode == args.mode_DISTANCE)
    {
        /*Do nothing, the prompt controls this.*/
    }
    else if(args.mode == args.mode_SIDE_LEN)
    {
        todo("POLYGON", "Sidelength mode")
    }

int prompt(str):
    if(args.mode == args.mode_NUM_SIDES)
    {
        if(str == "" && args.numSides >= 3 && args.numSides <= 1024)
        {
            setPromptPrefix(translate("Specify center point or [Sidelength]: "))
            args.mode = args.mode_CENTER_PT
        }
        else
        {
            var tmp = Number(str)
            if(isNaN(tmp) || !isInt(tmp) || tmp < 3 || tmp > 1024)
            {
                alert(translate("Requires an integer between 3 and 1024."))
                setPromptPrefix(translate("Enter number of sides") + " {" + args.numSides.toString() + "}: ")
            }
            else
            {
                args.numSides = tmp
                setPromptPrefix(translate("Specify center point or [Sidelength]: "))
                args.mode = args.mode_CENTER_PT
            }
        }
    }
    else if(args.mode == args.mode_CENTER_PT)
    {
        if(str == "S" || str == "SIDELENGTH") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SIDE_LEN
            setPromptPrefix(translate("Specify start point: "))
        }
        else
        {
            var strList = str.split(",")
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(translate("Point or option keyword required."))
                setPromptPrefix(translate("Specify center point or [Sidelength]: "))
            }
            else
            {
                args.centerX = Number(strList[0])
                args.centerY = Number(strList[1])
                args.mode = args.mode_POLYTYPE
                setPromptPrefix(translate("Specify polygon type [Inscribed in circle/Circumscribed around circle]") + " {" + args.polyType + "}: ")
            }
        }
    }
    else if(args.mode == args.mode_POLYTYPE)
    {
        if(str == "I"        ||
           str == "IN"       ||
           str == "INS"      ||
           str == "INSC"     ||
           str == "INSCR"    ||
           str == "INSCRI"   ||
           str == "INSCRIB"  ||
           str == "INSCRIBE" ||
           str == "INSCRIBED") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_INSCRIBE
            args.polyType = "Inscribed"
            setPromptPrefix(translate("Specify polygon corner point or [Distance]: "))
            addRubber("POLYGON")
            setRubberMode("POLYGON_INSCRIBE")
            setRubberPoint("POLYGON_CENTER", args.centerX, args.centerY)
            setRubberPoint("POLYGON_NUM_SIDES", args.numSides, 0)
        }
        else if(str == "C"            ||
                str == "CI"           ||
                str == "CIR"          ||
                str == "CIRC"         ||
                str == "CIRCU"        ||
                str == "CIRCUM"       ||
                str == "CIRCUMS"      ||
                str == "CIRCUMSC"     ||
                str == "CIRCUMSCR"    ||
                str == "CIRCUMSCRI"   ||
                str == "CIRCUMSCRIB"  ||
                str == "CIRCUMSCRIBE" ||
                str == "CIRCUMSCRIBED") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_CIRCUMSCRIBE
            args.polyType = "Circumscribed"
            setPromptPrefix(translate("Specify polygon side point or [Distance]: "))
            addRubber("POLYGON")
            setRubberMode("POLYGON_CIRCUMSCRIBE")
            setRubberPoint("POLYGON_CENTER", args.centerX, args.centerY)
            setRubberPoint("POLYGON_NUM_SIDES", args.numSides, 0)
        }
        else if(str == "")
        {
            if(args.polyType == "Inscribed")
            {
                args.mode = args.mode_INSCRIBE
                setPromptPrefix(translate("Specify polygon corner point or [Distance]: "))
                addRubber("POLYGON")
                setRubberMode("POLYGON_INSCRIBE")
                setRubberPoint("POLYGON_CENTER", args.centerX, args.centerY)
                setRubberPoint("POLYGON_NUM_SIDES", args.numSides, 0)
            }
            else if(args.polyType == "Circumscribed")
            {
                args.mode = args.mode_CIRCUMSCRIBE
                setPromptPrefix(translate("Specify polygon side point or [Distance]: "))
                addRubber("POLYGON")
                setRubberMode("POLYGON_CIRCUMSCRIBE")
                setRubberPoint("POLYGON_CENTER", args.centerX, args.centerY)
                setRubberPoint("POLYGON_NUM_SIDES", args.numSides, 0)
            }
            else
            {
                error("POLYGON", translate("Polygon type is not Inscribed or Circumscribed."))
            }
        }
        else
        {
            alert(translate("Invalid option keyword."))
            setPromptPrefix(translate("Specify polygon type [Inscribed in circle/Circumscribed around circle]") + " {" + args.polyType + "}: ")
        }
    }
    else if(args.mode == args.mode_INSCRIBE)
    {
        if(str == "D" || str == "DISTANCE") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_DISTANCE
            setPromptPrefix(translate("Specify distance: "))
        }
        else
        {
            var strList = str.split(",")
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(translate("Point or option keyword required."))
                setPromptPrefix(translate("Specify polygon corner point or [Distance]: "))
            }
            else
            {
                args.pointIX = Number(strList[0])
                args.pointIY = Number(strList[1])
                setRubberPoint("POLYGON_INSCRIBE_POINT", args.pointIX, args.pointIY)
                vulcanize()
                return
            }
        }
    }
    else if(args.mode == args.mode_CIRCUMSCRIBE)
    {
        if(str == "D" || str == "DISTANCE") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_DISTANCE
            setPromptPrefix(translate("Specify distance: "))
        }
        else:
            var strList = str.split(",")
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(translate("Point or option keyword required."))
                setPromptPrefix(translate("Specify polygon side point or [Distance]: "))
            }
            else:
                args.pointCX = Number(strList[0])
                args.pointCY = Number(strList[1])
                setRubberPoint("POLYGON_CIRCUMSCRIBE_POINT", args.pointCX, args.pointCY)
                vulcanize()
                return

    else if(args.mode == args.mode_DISTANCE)
    {
        if(isNaN(str))
        {
            alert(translate("Requires valid numeric distance."))
            setPromptPrefix(translate("Specify distance: "))
        }
        else
        {
            if(args.polyType == "Inscribed")
            {
                args.pointIX = args.centerX
                args.pointIY = args.centerY + Number(str)
                setRubberPoint("POLYGON_INSCRIBE_POINT", args.pointIX, args.pointIY)
                vulcanize()
                return
            }
            else if(args.polyType == "Circumscribed")
            {
                args.pointCX = args.centerX
                args.pointCY = args.centerY + Number(str)
                setRubberPoint("POLYGON_CIRCUMSCRIBE_POINT", args.pointCX, args.pointCY)
                vulcanize()
                return
            }
            else
            {
                error("POLYGON", translate("Polygon type is not Inscribed or Circumscribed."))
            }
        }
    }
    else if(args.mode == args.mode_SIDE_LEN)
    {
        todo("POLYGON", "Sidelength mode")
    }

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.firstRun
args.firstX
args.firstY
args.prevX
args.prevY
args.num

int init():
    clearSelection()
    args.firstRun = true
    args.firstX = MAX_DISTANCE+1.0
    args.firstY = MAX_DISTANCE+1.0
    args.prevX = MAX_DISTANCE+1.0
    args.prevY = MAX_DISTANCE+1.0
    args.num = 0
    setPromptPrefix(translate("Specify first point: "))

int click(x, y):
    if(args.firstRun)
    {
        args.firstRun = false
        args.firstX = x
        args.firstY = y
        args.prevX = x
        args.prevY = y
        addRubber("POLYLINE")
        setRubberMode("POLYLINE")
        setRubberPoint("POLYLINE_POINT_0", args.firstX, args.firstY)
        appendPromptHistory()
        setPromptPrefix(translate("Specify next point or [Undo]: "))
    }
    else
    {
        args.num++
        setRubberPoint("POLYLINE_POINT_" + args.num.toString(), x, y)
        setRubberText("POLYLINE_NUM_POINTS", args.num.toString())
        spareRubber("POLYLINE")
        appendPromptHistory()
        args.prevX = x
        args.prevY = y
    }

int prompt(str):
    if(args.firstRun)
    {
        var strList = str.split(",")
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(translate("Invalid point."))
            setPromptPrefix(translate("Specify first point: "))
        }
        else
        {
            args.firstRun = false
            args.firstX = Number(strList[0])
            args.firstY = Number(strList[1])
            args.prevX = args.firstX
            args.prevY = args.firstY
            addRubber("POLYLINE")
            setRubberMode("POLYLINE")
            setRubberPoint("POLYLINE_POINT_0", args.firstX, args.firstY)
            setPromptPrefix(translate("Specify next point or [Undo]: "))
        }
    }
    else
    {
        if(str == "U" || str == "UNDO") /*TODO: Probably should add additional qsTr calls here.*/
        {
            todo("POLYLINE", "prompt() for UNDO")
        }
        else
        {
            var strList = str.split(",")
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(translate("Point or option keyword required."))
                setPromptPrefix(translate("Specify next point or [Undo]: "))
            }
            else
            {
                var x = Number(strList[0])
                var y = Number(strList[1])
                args.num++
                setRubberPoint("POLYLINE_POINT_" + args.num.toString(), x, y)
                setRubberText("POLYLINE_NUM_POINTS", args.num.toString())
                spareRubber("POLYLINE")
                args.prevX = x
                args.prevY = y
                setPromptPrefix(translate("Specify next point or [Undo]: "))
            }
        }
    }

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.x1
args.y1
args.x2
args.y2

/*TODO: Adding the text is not complete yet.*/

int init():
    clearSelection()
    args.x1 = MAX_DISTANCE+1.0
    args.y1 = MAX_DISTANCE+1.0
    args.x2 = MAX_DISTANCE+1.0
    args.y2 = MAX_DISTANCE+1.0
    setPromptPrefix(translate("Specify first point: "))

int click(x, y):
    if(isNaN(args.x1))
    {
        args.x1 = x
        args.y1 = y
        addRubber("DIMLEADER")
        setRubberMode("DIMLEADER_LINE")
        setRubberPoint("DIMLEADER_LINE_START", args.x1, args.y1)
        appendPromptHistory()
        setPromptPrefix(translate("Specify second point: "))
    }
    else
    {
        args.x2 = x
        args.y2 = y
        setRubberPoint("DIMLEADER_LINE_END", args.x2, args.y2)
        vulcanize()
        appendPromptHistory()
        return
    }

int prompt(str):
    var strList = str.split(",")
    if(isNaN(args.x1))
    {
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(translate("Requires two points."))
            setPromptPrefix(translate("Specify first point: "))
        }
        else
        {
            args.x1 = Number(strList[0])
            args.y1 = Number(strList[1])
            addRubber("DIMLEADER")
            setRubberMode("DIMLEADER_LINE")
            setRubberPoint("DIMLEADER_LINE_START", args.x1, args.y1)
            setPromptPrefix(translate("Specify second point: "))
        }
    }
    else
    {
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(translate("Requires two points."))
            setPromptPrefix(translate("Specify second point: "))
        }
        else
        {
            args.x2 = Number(strList[0])
            args.y2 = Number(strList[1])
            setRubberPoint("DIMLEADER_LINE_END", args.x2, args.y2)
            vulcanize()
            return
        }
    }
--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.newRect
args.x1
args.y1
args.x2
args.y2

int init():
    clearSelection()
    args.newRect = true
    args.x1 = MAX_DISTANCE+1.0
    args.y1 = MAX_DISTANCE+1.0
    args.x2 = MAX_DISTANCE+1.0
    args.y2 = MAX_DISTANCE+1.0
    setPromptPrefix(translate("Specify first corner point or [Chamfer/Fillet]: "))

int click(x, y):
    if(args.newRect)
    {
        args.newRect = false
        args.x1 = x
        args.y1 = y
        addRubber("RECTANGLE")
        setRubberMode("RECTANGLE")
        setRubberPoint("RECTANGLE_START", x, y)
        setPromptPrefix(translate("Specify other corner point or [Dimensions]: "))
    }
    else
    {
        args.newRect = true
        args.x2 = x
        args.y2 = y
        setRubberPoint("RECTANGLE_END", x, y)
        vulcanize()
        return
    }

int prompt(str):
    if(str == "C" || str == "CHAMFER") /*TODO: Probably should add additional qsTr calls here.*/
    {
        todo("RECTANGLE", "prompt() for CHAMFER")
    }
    else if(str == "D" || str == "DIMENSIONS") /*TODO: Probably should add additional qsTr calls here.*/
    {
        todo("RECTANGLE", "prompt() for DIMENSIONS")
    }
    else if(str == "F" || str == "FILLET") /*TODO: Probably should add additional qsTr calls here.*/
    {
        todo("RECTANGLE", "prompt() for FILLET")
    }
    else
    {
        var strList = str.split(",")
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(translate("Invalid point."))
            setPromptPrefix(translate("Specify first point: "))
        }
        else
        {
            var x = Number(strList[0])
            var y = Number(strList[1])
            if(args.newRect)
            {
                args.newRect = false
                args.x1 = x
                args.y1 = y
                addRubber("RECTANGLE")
                setRubberMode("RECTANGLE")
                setRubberPoint("RECTANGLE_START", x, y)
                setPromptPrefix(translate("Specify other corner point or [Dimensions]: "))
            }
            else
            {
                args.newRect = true
                args.x2 = x
                args.y2 = y
                setRubberPoint("RECTANGLE_END", x, y)
                vulcanize()
                return
            }
        }
    }

---------------------------------------------------------------------------------

var global = {}; /*Required*/
args.mode

/*enums*/
args.mode_BACKGROUND = 0
args.mode_CROSSHAIR  = 1
args.mode_GRID       = 2

int init():
    clearSelection()
    args.mode = args.mode_BACKGROUND
    setPromptPrefix(translate("Enter RED,GREEN,BLUE values for background or [Crosshair/Grid]: "))

int prompt(str):
    if(args.mode == args.mode_BACKGROUND)
    {
        if(str == "C" || str == "CROSSHAIR") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_CROSSHAIR
            setPromptPrefix(translate("Specify crosshair color: "))
        }
        else if(str == "G" || str == "GRID") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_GRID
            setPromptPrefix(translate("Specify grid color: "))
        }
        else
        {
            var strList = str.split(",")
            var r = Number(strList[0])
            var g = Number(strList[1])
            var b = Number(strList[2])
            if(!validRGB(r,g,b))
            {
                alert(translate("Invalid color. R,G,B values must be in the range of 0-255."))
                setPromptPrefix(translate("Specify background color: "))
            }
            else
            {
                setBackgroundColor(r,g,b)
                return
            }
        }
    }
    else if(args.mode == args.mode_CROSSHAIR)
    {
        var strList = str.split(",")
        var r = Number(strList[0])
        var g = Number(strList[1])
        var b = Number(strList[2])
        if(!validRGB(r,g,b))
        {
            alert(translate("Invalid color. R,G,B values must be in the range of 0-255."))
            setPromptPrefix(translate("Specify crosshair color: "))
        }
        else
        {
            setCrossHairColor(r,g,b)
            return
        }
    }
    else if(args.mode == args.mode_GRID)
    {
        var strList = str.split(",")
        var r = Number(strList[0])
        var g = Number(strList[1])
        var b = Number(strList[2])
        if(!validRGB(r,g,b))
        {
            alert(translate("Invalid color. R,G,B values must be in the range of 0-255."))
            setPromptPrefix(translate("Specify grid color: "))
        }
        else
        {
            setGridColor(r,g,b)
            return
        }
    }

int validRGB(r, g, b):
    if(isNaN(r)) return false
    if(isNaN(g)) return false
    if(isNaN(b)) return false
    if(r < 0 || r > 255) return false
    if(g < 0 || g > 255) return false
    if(b < 0 || b > 255) return false
    return true

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.firstRun
args.baseX
args.baseY
args.destX
args.destY
args.angle

args.baseRX
args.baseRY
args.destRX
args.destRY
args.angleRef
args.angleNew

args.mode

/*enums*/
args.mode_NORMAL    = 0
args.mode_REFERENCE = 1

int init():
    args.mode = args.mode_NORMAL
    args.firstRun = true
    args.baseX = MAX_DISTANCE+1.0
    args.baseY = MAX_DISTANCE+1.0
    args.destX = MAX_DISTANCE+1.0
    args.destY = MAX_DISTANCE+1.0
    args.angle = MAX_DISTANCE+1.0

    args.baseRX   = MAX_DISTANCE+1.0
    args.baseRY   = MAX_DISTANCE+1.0
    args.destRX   = MAX_DISTANCE+1.0
    args.destRY   = MAX_DISTANCE+1.0
    args.angleRef = MAX_DISTANCE+1.0
    args.angleNew = MAX_DISTANCE+1.0

    if(numSelected() <= 0)
    {
        /*TODO: Prompt to select objects if nothing is preselected*/
        alert(translate("Preselect objects before invoking the rotate command."))
        return
        messageBox("information", translate("Rotate Preselect"), translate("Preselect objects before invoking the rotate command."))
    }
    else
    {
        setPromptPrefix(translate("Specify base point: "))
    }

int click(x, y):
    if(args.mode == args.mode_NORMAL)
    {
        if(args.firstRun)
        {
            args.firstRun = false
            args.baseX = x
            args.baseY = y
            addRubber("LINE")
            setRubberMode("LINE")
            setRubberPoint("LINE_START", args.baseX, args.baseY)
            previewOn("SELECTED", "ROTATE", args.baseX, args.baseY, 0)
            appendPromptHistory()
            setPromptPrefix(translate("Specify rotation angle or [Reference]: "))
        }
        else
        {
            args.destX = x
            args.destY = y
            args.angle = calculateAngle(args.baseX, args.baseY, args.destX, args.destY)
            appendPromptHistory()
            rotateSelected(args.baseX, args.baseY, args.angle)
            previewOff()
            return
        }
    }
    else if(args.mode == args.mode_REFERENCE)
    {
        if(isNaN(args.baseRX))
        {
            args.baseRX = x
            args.baseRY = y
            appendPromptHistory()
            addRubber("LINE")
            setRubberMode("LINE")
            setRubberPoint("LINE_START", args.baseRX, args.baseRY)
            setPromptPrefix(translate("Specify second point: "))
        }
        else if(isNaN(args.destRX))
        {
            args.destRX = x
            args.destRY = y
            args.angleRef = calculateAngle(args.baseRX, args.baseRY, args.destRX, args.destRY)
            setRubberPoint("LINE_START", args.baseX, args.baseY)
            previewOn("SELECTED", "ROTATE", args.baseX, args.baseY, args.angleRef)
            appendPromptHistory()
            setPromptPrefix(translate("Specify the new angle: "))
        }
        else if(isNaN(args.angleNew))
        {
            args.angleNew = calculateAngle(args.baseX, args.baseY, x, y)
            rotateSelected(args.baseX, args.baseY, args.angleNew - args.angleRef)
            previewOff()
            return
        }
    }

int prompt(str):
    if(args.mode == args.mode_NORMAL)
    {
        if(args.firstRun)
        {
            var strList = str.split(",")
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify base point: "))
            }
            else
            {
                args.firstRun = false
                args.baseX = Number(strList[0])
                args.baseY = Number(strList[1])
                addRubber("LINE")
                setRubberMode("LINE")
                setRubberPoint("LINE_START", args.baseX, args.baseY)
                previewOn("SELECTED", "ROTATE", args.baseX, args.baseY, 0)
                setPromptPrefix(translate("Specify rotation angle or [Reference]: "))
            }
        }
        else
        {
            if(str == "R" || str == "REFERENCE") /*TODO: Probably should add additional qsTr calls here.*/
            {
                args.mode = args.mode_REFERENCE
                setPromptPrefix(translate("Specify the reference angle") + " {0.00}: ")
                clearRubber()
                previewOff()
            }
            else
            {
                if(isNaN(str))
                {
                    alert(translate("Requires valid numeric angle, second point, or option keyword."))
                    setPromptPrefix(translate("Specify rotation angle or [Reference]: "))
                }
                else
                {
                    args.angle = Number(str)
                    rotateSelected(args.baseX, args.baseY, args.angle)
                    previewOff()
                    return
                }
            }
        }
    }
    else if(args.mode == args.mode_REFERENCE)
    {
        if(isNaN(args.baseRX))
        {
            if(isNaN(str))
            {
                var strList = str.split(",")
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(translate("Requires valid numeric angle or two points."))
                    setPromptPrefix(translate("Specify the reference angle") + " {0.00}: ")
                }
                else
                {
                    args.baseRX = Number(strList[0])
                    args.baseRY = Number(strList[1])
                    addRubber("LINE")
                    setRubberMode("LINE")
                    setRubberPoint("LINE_START", args.baseRX, args.baseRY)
                    setPromptPrefix(translate("Specify second point: "))
                }
            }
            else
            {
                /*The base and dest values are only set here to advance the command.*/
                args.baseRX = 0.0
                args.baseRY = 0.0
                args.destRX = 0.0
                args.destRY = 0.0
                /*The reference angle is what we will use later.*/
                args.angleRef = Number(str)
                addRubber("LINE")
                setRubberMode("LINE")
                setRubberPoint("LINE_START", args.baseX, args.baseY)
                previewOn("SELECTED", "ROTATE", args.baseX, args.baseY, args.angleRef)
                setPromptPrefix(translate("Specify the new angle: "))
            }
        }
        else if(isNaN(args.destRX))
        {
            if(isNaN(str))
            {
                var strList = str.split(",")
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(translate("Requires valid numeric angle or two points."))
                    setPromptPrefix(translate("Specify second point: "))
                }
                else
                {
                    args.destRX = Number(strList[0])
                    args.destRY = Number(strList[1])
                    args.angleRef = calculateAngle(args.baseRX, args.baseRY, args.destRX, args.destRY)
                    previewOn("SELECTED", "ROTATE", args.baseX, args.baseY, args.angleRef)
                    setRubberPoint("LINE_START", args.baseX, args.baseY)
                    setPromptPrefix(translate("Specify the new angle: "))
                }
            }
            else
            {
                /*The base and dest values are only set here to advance the command.*/
                args.baseRX = 0.0
                args.baseRY = 0.0
                args.destRX = 0.0
                args.destRY = 0.0
                /*The reference angle is what we will use later.*/
                args.angleRef = Number(str)
                previewOn("SELECTED", "ROTATE", args.baseX, args.baseY, args.angleRef)
                setPromptPrefix(translate("Specify the new angle: "))
            }
        }
        else if(isNaN(args.angleNew))
        {
            if(isNaN(str))
            {
                var strList = str.split(",")
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(translate("Requires valid numeric angle or second point."))
                    setPromptPrefix(translate("Specify the new angle: "))
                }
                else
                {
                    var x = Number(strList[0])
                    var y = Number(strList[1])
                    args.angleNew = calculateAngle(args.baseX, args.baseY, x, y)
                    rotateSelected(args.baseX, args.baseY, args.angleNew - args.angleRef)
                    previewOff()
                    return
                }
            }
            else
            {
                args.angleNew = Number(str)
                rotateSelected(args.baseX, args.baseY, args.angleNew - args.angleRef)
                previewOff()
                return
            }
        }
    }

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.test1
args.test2

int init():
    /*Report number of pre-selected objects*/
    setPromptPrefix("Number of Objects Selected: " + numSelected().toString())
    appendPromptHistory()
    
    mirrorSelected(0,0,0,1)
    
    /*selectAll();*/
    /*rotateSelected(0,0,90);*/
    
    /*Polyline & Polygon Testing*/
    
    var offsetX = 0.0
    var offsetY = 0.0
    
    var polylineArray = []
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
    
    var polygonArray = []
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

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.firstRun
args.baseX
args.baseY
args.destX
args.destY
args.factor

args.baseRX
args.baseRY
args.destRX
args.destRY
args.factorRef
args.factorNew

args.mode

/*enums*/
args.mode_NORMAL    = 0
args.mode_REFERENCE = 1

int __init__():
    args.mode = args.mode_NORMAL
    args.firstRun = true
    args.baseX  = MAX_DISTANCE+1.0
    args.baseY  = MAX_DISTANCE+1.0
    args.destX  = MAX_DISTANCE+1.0
    args.destY  = MAX_DISTANCE+1.0
    args.factor = MAX_DISTANCE+1.0

    args.baseRX    = MAX_DISTANCE+1.0
    args.baseRY    = MAX_DISTANCE+1.0
    args.destRX    = MAX_DISTANCE+1.0
    args.destRY    = MAX_DISTANCE+1.0
    args.factorRef = MAX_DISTANCE+1.0
    args.factorNew = MAX_DISTANCE+1.0

    if(numSelected() <= 0)
    {
        /*TODO: Prompt to select objects if nothing is preselected*/
        alert(translate("Preselect objects before invoking the scale command."))
        return
        messageBox("information", translate("Scale Preselect"), translate("Preselect objects before invoking the scale command."))
    }
    else
    {
        setPromptPrefix(translate("Specify base point: "))
    }

int click(x, y):
    if(args.mode == args.mode_NORMAL)
    {
        if(args.firstRun)
        {
            args.firstRun = false
            args.baseX = x
            args.baseY = y
            addRubber("LINE")
            setRubberMode("LINE")
            setRubberPoint("LINE_START", args.baseX, args.baseY)
            previewOn("SELECTED", "SCALE", args.baseX, args.baseY, 1)
            appendPromptHistory()
            setPromptPrefix(translate("Specify scale factor or [Reference]: "))
        }
        else
        {
            args.destX = x
            args.destY = y
            args.factor = calculateDistance(args.baseX, args.baseY, args.destX, args.destY)
            appendPromptHistory()
            scaleSelected(args.baseX, args.baseY, args.factor)
            previewOff()
            return
        }
    }
    else if(args.mode == args.mode_REFERENCE)
    {
        if(isNaN(args.baseRX))
        {
            args.baseRX = x
            args.baseRY = y
            appendPromptHistory()
            addRubber("LINE")
            setRubberMode("LINE")
            setRubberPoint("LINE_START", args.baseRX, args.baseRY)
            setPromptPrefix(translate("Specify second point: "))
        }
        else if(isNaN(args.destRX))
        {
            args.destRX = x
            args.destRY = y
            args.factorRef = calculateDistance(args.baseRX, args.baseRY, args.destRX, args.destRY)
            if(args.factorRef <= 0.0)
            {
                args.destRX    = MAX_DISTANCE+1.0
                args.destRY    = MAX_DISTANCE+1.0
                args.factorRef = MAX_DISTANCE+1.0
                alert(translate("Value must be positive and nonzero."))
                setPromptPrefix(translate("Specify second point: "))
            }
            else
            {
                appendPromptHistory()
                setRubberPoint("LINE_START", args.baseX, args.baseY)
                previewOn("SELECTED", "SCALE", args.baseX, args.baseY, args.factorRef)
                setPromptPrefix(translate("Specify new length: "))
            }
        }
        else if(isNaN(args.factorNew))
        {
            args.factorNew = calculateDistance(args.baseX, args.baseY, x, y)
            if(args.factorNew <= 0.0)
            {
                args.factorNew = MAX_DISTANCE+1.0
                alert(translate("Value must be positive and nonzero."))
                setPromptPrefix(translate("Specify new length: "))
            }
            else
            {
                appendPromptHistory()
                scaleSelected(args.baseX, args.baseY, args.factorNew/args.factorRef)
                previewOff()
                return
            }
        }
    }

int prompt(str):
    if(args.mode == args.mode_NORMAL)
    {
        if(args.firstRun)
        {
            var strList = str.split(",")
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(translate("Invalid point."))
                setPromptPrefix(translate("Specify base point: "))
            }
            else
            {
                args.firstRun = false
                args.baseX = Number(strList[0])
                args.baseY = Number(strList[1])
                addRubber("LINE")
                setRubberMode("LINE")
                setRubberPoint("LINE_START", args.baseX, args.baseY)
                previewOn("SELECTED", "SCALE", args.baseX, args.baseY, 1)
                setPromptPrefix(translate("Specify scale factor or [Reference]: "))
            }
        }
        else
        {
            if(str == "R" || str == "REFERENCE") /*TODO: Probably should add additional qsTr calls here.*/
            {
                args.mode = args.mode_REFERENCE
                setPromptPrefix(translate("Specify reference length") + " {1}: ")
                clearRubber()
                previewOff()
            }
            else
            {
                if(isNaN(str))
                {
                    alert(translate("Requires valid numeric distance, second point, or option keyword."))
                    setPromptPrefix(translate("Specify scale factor or [Reference]: "))
                }
                else
                {
                    args.factor = Number(str)
                    scaleSelected(args.baseX, args.baseY, args.factor)
                    previewOff()
                    return
                }
            }
        }
    }
    else if(args.mode == args.mode_REFERENCE)
    {
        if(isNaN(args.baseRX))
        {
            if(isNaN(str))
            {
                var strList = str.split(",")
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(translate("Requires valid numeric distance or two points."))
                    setPromptPrefix(translate("Specify reference length") + " {1}: ")
                }
                else
                {
                    args.baseRX = Number(strList[0])
                    args.baseRY = Number(strList[1])
                    addRubber("LINE")
                    setRubberMode("LINE")
                    setRubberPoint("LINE_START", args.baseRX, args.baseRY)
                    setPromptPrefix(translate("Specify second point: "))
                }
            }
            else
            {
                /*The base and dest values are only set here to advance the command.*/
                args.baseRX = 0.0
                args.baseRY = 0.0
                args.destRX = 0.0
                args.destRY = 0.0
                /*The reference length is what we will use later.*/
                args.factorRef = Number(str)
                if(args.factorRef <= 0.0)
                {
                    args.baseRX    = MAX_DISTANCE+1.0
                    args.baseRY    = MAX_DISTANCE+1.0
                    args.destRX    = MAX_DISTANCE+1.0
                    args.destRY    = MAX_DISTANCE+1.0
                    args.factorRef = MAX_DISTANCE+1.0
                    alert(translate("Value must be positive and nonzero."))
                    setPromptPrefix(translate("Specify reference length") + " {1}: ")
                }
                else
                {
                    addRubber("LINE")
                    setRubberMode("LINE")
                    setRubberPoint("LINE_START", args.baseX, args.baseY)
                    previewOn("SELECTED", "SCALE", args.baseX, args.baseY, args.factorRef)
                    setPromptPrefix(translate("Specify new length: "))
                }
            }
        }
        else if(isNaN(args.destRX))
        {
            if(isNaN(str))
            {
                var strList = str.split(",")
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(translate("Requires valid numeric distance or two points."))
                    setPromptPrefix(translate("Specify second point: "))
                }
                else
                {
                    args.destRX = Number(strList[0])
                    args.destRY = Number(strList[1])
                    args.factorRef = calculateDistance(args.baseRX, args.baseRY, args.destRX, args.destRY)
                    if(args.factorRef <= 0.0)
                    {
                        args.destRX    = MAX_DISTANCE+1.0
                        args.destRY    = MAX_DISTANCE+1.0
                        args.factorRef = MAX_DISTANCE+1.0
                        alert(translate("Value must be positive and nonzero."))
                        setPromptPrefix(translate("Specify second point: "))
                    }
                    else
                    {
                        setRubberPoint("LINE_START", args.baseX, args.baseY)
                        previewOn("SELECTED", "SCALE", args.baseX, args.baseY, args.factorRef)
                        setPromptPrefix(translate("Specify new length: "))
                    }
                }
            }
            else
            {
                /*The base and dest values are only set here to advance the command.*/
                args.baseRX = 0.0
                args.baseRY = 0.0
                args.destRX = 0.0
                args.destRY = 0.0
                /*The reference length is what we will use later.*/
                args.factorRef = Number(str)
                if(args.factorRef <= 0.0)
                {
                    args.destRX    = MAX_DISTANCE+1.0
                    args.destRY    = MAX_DISTANCE+1.0
                    args.factorRef = MAX_DISTANCE+1.0
                    alert(translate("Value must be positive and nonzero."))
                    setPromptPrefix(translate("Specify second point: "))
                }
                else
                {
                    setRubberPoint("LINE_START", args.baseX, args.baseY)
                    previewOn("SELECTED", "SCALE", args.baseX, args.baseY, args.factorRef)
                    setPromptPrefix(translate("Specify new length: "))
                }
            }
        }
        else if(isNaN(args.factorNew))
        {
            if(isNaN(str))
            {
                var strList = str.split(",")
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(translate("Requires valid numeric distance or second point."))
                    setPromptPrefix(translate("Specify new length: "))
                }
                else
                {
                    var x = Number(strList[0])
                    var y = Number(strList[1])
                    args.factorNew = calculateDistance(args.baseX, args.baseY, x, y)
                    if(args.factorNew <= 0.0)
                    {
                        args.factorNew = MAX_DISTANCE+1.0
                        alert(translate("Value must be positive and nonzero."))
                        setPromptPrefix(translate("Specify new length: "))
                    }
                    else
                    {
                        scaleSelected(args.baseX, args.baseY, args.factorNew/args.factorRef)
                        previewOff()
                        return
                    }
                }
            }
            else
            {
                args.factorNew = Number(str)
                if(args.factorNew <= 0.0)
                {
                    args.factorNew = MAX_DISTANCE+1.0
                    alert(translate("Value must be positive and nonzero."))
                    setPromptPrefix(translate("Specify new length: "))
                }
                else
                {
                    scaleSelected(args.baseX, args.baseY, args.factorNew/args.factorRef)
                    previewOff()
                    return
                }
            }
        }
    }

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.text
args.textX
args.textY
args.textJustify
args.textFont
args.textHeight
args.textRotation
args.mode

/*enums*/
args.mode_JUSTIFY = 0
args.mode_SETFONT = 1
args.mode_SETGEOM = 2
args.mode_RAPID   = 3

int init():
    clearSelection()
    args.text = ""
    args.textX = MAX_DISTANCE+1.0
    args.textY = MAX_DISTANCE+1.0
    args.textJustify = "Left"
    args.textFont = textFont()
    args.textHeight = MAX_DISTANCE+1.0
    args.textRotation = MAX_DISTANCE+1.0
    args.mode = args.mode_SETGEOM
    setPromptPrefix(translate("Current font: ") + "{" + args.textFont + "} " + translate("Text height: ") + "{" +  textSize() + "}")
    appendPromptHistory()
    setPromptPrefix(translate("Specify start point of text or [Justify/Setfont]: "))

int click(x, y):
    if(args.mode == args.mode_SETGEOM)
    {
        if(isNaN(args.textX))
        {
            args.textX = x
            args.textY = y
            addRubber("LINE")
            setRubberMode("LINE")
            setRubberPoint("LINE_START", args.textX, args.textY)
            appendPromptHistory()
            setPromptPrefix(translate("Specify text height") + " {" + textSize() + "}: ")
        }
        else if(isNaN(args.textHeight))
        {
            args.textHeight = calculateDistance(args.textX, args.textY, x, y)
            setTextSize(args.textHeight)
            appendPromptHistory()
            setPromptPrefix(translate("Specify text angle") + " {" + textAngle() + "}: ")
        }
        else if(isNaN(args.textRotation))
        {
            args.textRotation = calculateAngle(args.textX, args.textY, x, y)
            setTextAngle(args.textRotation)
            appendPromptHistory()
            setPromptPrefix(translate("Enter text: "))
            args.mode = args.mode_RAPID
            enablePromptRapidFire()
            clearRubber()
            addRubber("TEXTSINGLE")
            setRubberMode("TEXTSINGLE")
            setRubberPoint("TEXT_POINT", args.textX, args.textY)
            setRubberPoint("TEXT_HEIGHT_ROTATION", args.textHeight, args.textRotation)
            setRubberText("TEXT_FONT", args.textFont)
            setRubberText("TEXT_JUSTIFY", args.textJustify)
            setRubberText("TEXT_RAPID", args.text)
        }
        else
        {
            /*Do nothing, as we are in rapidFire mode now.*/
        }
    }

int prompt(str):
    if(args.mode == args.mode_JUSTIFY)
    {
        if(str == "C" || str == "CENTER") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM
            args.textJustify = "Center"
            setRubberText("TEXT_JUSTIFY", args.textJustify)
            setPromptPrefix(translate("Specify center point of text or [Justify/Setfont]: "))
        }
        else if(str == "R" || str == "RIGHT") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM
            args.textJustify = "Right"
            setRubberText("TEXT_JUSTIFY", args.textJustify)
            setPromptPrefix(translate("Specify right-end point of text or [Justify/Setfont]: "))
        }
        else if(str == "A" || str == "ALIGN") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM
            args.textJustify = "Aligned"
            setRubberText("TEXT_JUSTIFY", args.textJustify)
            setPromptPrefix(translate("Specify start point of text or [Justify/Setfont]: "))
        }
        else if(str == "M" || str == "MIDDLE") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM
            args.textJustify = "Middle"
            setRubberText("TEXT_JUSTIFY", args.textJustify)
            setPromptPrefix(translate("Specify middle point of text or [Justify/Setfont]: "))
        }
        else if(str == "F" || str == "FIT") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM
            args.textJustify = "Fit"
            setRubberText("TEXT_JUSTIFY", args.textJustify)
            setPromptPrefix(translate("Specify start point of text or [Justify/Setfont]: "))
        }
        else if(str == "TL" || str == "TOPLEFT") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM
            args.textJustify = "Top Left"
            setRubberText("TEXT_JUSTIFY", args.textJustify)
            setPromptPrefix(translate("Specify top-left point of text or [Justify/Setfont]: "))
        }
        else if(str == "TC" || str == "TOPCENTER") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM
            args.textJustify = "Top Center"
            setRubberText("TEXT_JUSTIFY", args.textJustify)
            setPromptPrefix(translate("Specify top-center point of text or [Justify/Setfont]: "))
        }
        else if(str == "TR" || str == "TOPRIGHT") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM
            args.textJustify = "Top Right"
            setRubberText("TEXT_JUSTIFY", args.textJustify)
            setPromptPrefix(translate("Specify top-right point of text or [Justify/Setfont]: "))
        }
        else if(str == "ML" || str == "MIDDLELEFT") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM
            args.textJustify = "Middle Left"
            setRubberText("TEXT_JUSTIFY", args.textJustify)
            setPromptPrefix(translate("Specify middle-left point of text or [Justify/Setfont]: "))
        }
        else if(str == "MC" || str == "MIDDLECENTER") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM
            args.textJustify = "Middle Center"
            setRubberText("TEXT_JUSTIFY", args.textJustify)
            setPromptPrefix(translate("Specify middle-center point of text or [Justify/Setfont]: "))
        }
        else if(str == "MR" || str == "MIDDLERIGHT") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM
            args.textJustify = "Middle Right"
            setRubberText("TEXT_JUSTIFY", args.textJustify)
            setPromptPrefix(translate("Specify middle-right point of text or [Justify/Setfont]: "))
        }
        else if(str == "BL" || str == "BOTTOMLEFT") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM
            args.textJustify = "Bottom Left"
            setRubberText("TEXT_JUSTIFY", args.textJustify)
            setPromptPrefix(translate("Specify bottom-left point of text or [Justify/Setfont]: "))
        }
        else if(str == "BC" || str == "BOTTOMCENTER") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM
            args.textJustify = "Bottom Center"
            setRubberText("TEXT_JUSTIFY", args.textJustify)
            setPromptPrefix(translate("Specify bottom-center point of text or [Justify/Setfont]: "))
        }
        else if(str == "BR" || str == "BOTTOMRIGHT") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM
            args.textJustify = "Bottom Right"
            setRubberText("TEXT_JUSTIFY", args.textJustify)
            setPromptPrefix(translate("Specify bottom-right point of text or [Justify/Setfont]: "))
        }
        else
        {
            alert(translate("Invalid option keyword."))
            setPromptPrefix(translate("Text Justification Options [Center/Right/Align/Middle/Fit/TL/TC/TR/ML/MC/MR/BL/BC/BR]: "))
        }
    }
    else if(args.mode == args.mode_SETFONT)
    {
        args.mode = args.mode_SETGEOM
        args.textFont = str
        setRubberText("TEXT_FONT", args.textFont)
        setTextFont(args.textFont)
        setPromptPrefix(translate("Specify start point of text or [Justify/Setfont]: "))
    }
    else if(args.mode == args.mode_SETGEOM)
    {
        if(isNaN(args.textX))
        {
            if(str == "J" || str == "JUSTIFY") /*TODO: Probably should add additional qsTr calls here.*/
            {
                args.mode = args.mode_JUSTIFY
                setPromptPrefix(translate("Text Justification Options [Center/Right/Align/Middle/Fit/TL/TC/TR/ML/MC/MR/BL/BC/BR]: "))
            }
            else if(str == "S" || str == "SETFONT") /*TODO: Probably should add additional qsTr calls here.*/
            {
                args.mode = args.mode_SETFONT
                setPromptPrefix(translate("Specify font name: "))
            }
            else
            {
                var strList = str.split(",")
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(translate("Point or option keyword required."))
                    setPromptPrefix(translate("Specify start point of text or [Justify/Setfont]: "))
                }
                else
                {
                    args.textX = Number(strList[0])
                    args.textY = Number(strList[1])
                    addRubber("LINE")
                    setRubberMode("LINE")
                    setRubberPoint("LINE_START", args.textX, args.textY)
                    setPromptPrefix(translate("Specify text height") + " {" + textSize() + "}: ")
                }
            }
        }
        else if(isNaN(args.textHeight))
        {
            if(str == "")
            {
                args.textHeight = textSize()
                setPromptPrefix(translate("Specify text angle") + " {" + textAngle() + "}: ")
            }
            else if(isNaN(str))
            {
                alert(translate("Requires valid numeric distance or second point."))
                setPromptPrefix(translate("Specify text height") + " {" + textSize() + "}: ")
            }
            else
            {
                args.textHeight = Number(str)
                setTextSize(args.textHeight)
                setPromptPrefix(translate("Specify text angle") + " {" + textAngle() + "}: ")
            }
        }
        else if(isNaN(args.textRotation))
        {
            if(str == "")
            {
                args.textRotation = textAngle()
                setPromptPrefix(translate("Enter text: "))
                args.mode = args.mode_RAPID
                enablePromptRapidFire()
                clearRubber()
                addRubber("TEXTSINGLE")
                setRubberMode("TEXTSINGLE")
                setRubberPoint("TEXT_POINT", args.textX, args.textY)
                setRubberPoint("TEXT_HEIGHT_ROTATION", args.textHeight, args.textRotation)
                setRubberText("TEXT_FONT", args.textFont)
                setRubberText("TEXT_JUSTIFY", args.textJustify)
                setRubberText("TEXT_RAPID", args.text)
            }
            else if(isNaN(str))
            {
                alert(translate("Requires valid numeric angle or second point."))
                setPromptPrefix(translate("Specify text angle") + " {" + textAngle() + "}: ")
            }
            else
            {
                args.textRotation = Number(str)
                setTextAngle(args.textRotation)
                setPromptPrefix(translate("Enter text: "))
                args.mode = args.mode_RAPID
                enablePromptRapidFire()
                clearRubber()
                addRubber("TEXTSINGLE")
                setRubberMode("TEXTSINGLE")
                setRubberPoint("TEXT_POINT", args.textX, args.textY)
                setRubberPoint("TEXT_HEIGHT_ROTATION", args.textHeight, args.textRotation)
                setRubberText("TEXT_FONT", args.textFont)
                setRubberText("TEXT_JUSTIFY", args.textJustify)
                setRubberText("TEXT_RAPID", args.text)
            }
        }
        else
        {
            /*Do nothing, as we are in rapidFire mode now.*/
        }
    }
    else if(args.mode == args.mode_RAPID)
    {
        if(str == "RAPID_ENTER")
        {
            if(args.text == "")
            {
                return
            }
            else
            {
                vulcanize()
                return; /*TODO: Rather than ending the command, calculate where the next line would be and modify the x/y to the new point*/
            }
        }
        else
        {
            args.text = str
            setRubberText("TEXT_RAPID", args.text)
        }
    }

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.numPoints = 2048; /*Default //TODO: min:64 max:8192*/
args.cx
args.cy
args.sx = 0.04; /*Default*/
args.sy = 0.04; /*Default*/
args.numPoints
args.mode

/*enums*/
args.mode_NUM_POINTS = 0
args.mode_XSCALE     = 1
args.mode_YSCALE     = 2

int init():
    clearSelection()
    args.cx = MAX_DISTANCE+1.0
    args.cy = MAX_DISTANCE+1.0
    args.mode = args.mode_NUM_POINTS

    addRubber("POLYGON")
    setRubberMode("POLYGON")
    updateSnowflake(args.numPoints, args.sx, args.sy)
    spareRubber("POLYGON")
    return

int updateSnowflake(numPts, xScale, yScale):
    var i
    var t
    var xx = MAX_DISTANCE+1.0
    var yy = MAX_DISTANCE+1.0
    var two_pi = 2*embConstantPi

    for(i = 0; i <= numPts; i++)
    {
        t = two_pi/numPts*i; 

/*Snowflake Curve with t [0,2pi]*/

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

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.numPoints = 5; /*Default*/
args.cx
args.cy
args.x1
args.y1
args.x2
args.y2
args.mode

/*enums*/
args.mode_NUM_POINTS = 0
args.mode_CENTER_PT  = 1
args.mode_RAD_OUTER  = 2
args.mode_RAD_INNER  = 3

int init():
    clearSelection()
    args.cx       = MAX_DISTANCE+1.0
    args.cy       = MAX_DISTANCE+1.0
    args.x1       = MAX_DISTANCE+1.0
    args.y1       = MAX_DISTANCE+1.0
    args.x2       = MAX_DISTANCE+1.0
    args.y2       = MAX_DISTANCE+1.0
    args.mode = args.mode_NUM_POINTS
    setPromptPrefix(translate("Enter number of star points") + " {" + args.numPoints.toString() + "}: ")

int click(x, y):
    if(args.mode == args.mode_NUM_POINTS)
    {
        /*Do nothing, the prompt controls this.*/
    }
    else if(args.mode == args.mode_CENTER_PT)
    {
        args.cx = x
        args.cy = y
        args.mode = args.mode_RAD_OUTER
        setPromptPrefix(translate("Specify outer radius of star: "))
        addRubber("POLYGON")
        setRubberMode("POLYGON")
        updateStar(args.cx, args.cy)
        enableMoveRapidFire()
    }
    else if(args.mode == args.mode_RAD_OUTER)
    {
        args.x1 = x
        args.y1 = y
        args.mode = args.mode_RAD_INNER
        setPromptPrefix(translate("Specify inner radius of star: "))
        updateStar(args.x1, args.y1)
    }
    else if(args.mode == args.mode_RAD_INNER)
    {
        args.x2 = x
        args.y2 = y
        disableMoveRapidFire()
        updateStar(args.x2, args.y2)
        spareRubber("POLYGON")
        return
    }

int move(x, y):
    if(args.mode == args.mode_NUM_POINTS)
    {
        /*Do nothing, the prompt controls this.*/
    }
    else if(args.mode == args.mode_CENTER_PT)
    {
        /*Do nothing, prompt and click controls this.*/
    }
    else if(args.mode == args.mode_RAD_OUTER)
    {
        updateStar(x, y)
    }
    else if(args.mode == args.mode_RAD_INNER)
    {
        updateStar(x, y)
    }

int prompt(str):
    if(args.mode == args.mode_NUM_POINTS)
    {
        if(str == "" && args.numPoints >= 3 && args.numPoints <= 1024)
        {
            setPromptPrefix(translate("Specify center point: "))
            args.mode = args.mode_CENTER_PT
        }
        else
        {
            var tmp = Number(str)
            if(isNaN(tmp) || !isInt(tmp) || tmp < 3 || tmp > 1024)
            {
                alert(translate("Requires an integer between 3 and 1024."))
                setPromptPrefix(translate("Enter number of star points") + " {" + args.numPoints.toString() + "}: ")
            }
            else
            {
                args.numPoints = tmp
                setPromptPrefix(translate("Specify center point: "))
                args.mode = args.mode_CENTER_PT
            }
        }
    }
    else if(args.mode == args.mode_CENTER_PT)
    {
        var strList = str.split(",")
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(translate("Invalid point."))
            setPromptPrefix(translate("Specify center point: "))
        }
        else:
            args.cx = Number(strList[0])
            args.cy = Number(strList[1])
            args.mode = args.mode_RAD_OUTER
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
            args.x1 = Number(strList[0])
            args.y1 = Number(strList[1])
            args.mode = args.mode_RAD_INNER
            setPromptPrefix(translate("Specify inner radius of star: "))
            updateStar(qsnapX(), qsnapY())

    else if(args.mode == args.mode_RAD_INNER)
    {
        var strList = str.split(",")
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(translate("Invalid point."))
            setPromptPrefix(translate("Specify inner radius of star: "))
        }
        else
        {
            args.x2 = Number(strList[0])
            args.y2 = Number(strList[1])
            disableMoveRapidFire()
            updateStar(args.x2, args.y2)
            spareRubber("POLYGON")
            return
        }
    }

int updateStar(x, y):
    var distOuter
    var distInner
    var angOuter

    if(args.mode == args.mode_RAD_OUTER)
    {
        angOuter = calculateAngle(args.cx, args.cy, x, y)
        distOuter = calculateDistance(args.cx, args.cy, x, y)
        distInner = distOuter/2.0
    }
    else if(args.mode == args.mode_RAD_INNER)
    {
        angOuter = calculateAngle(args.cx, args.cy, args.x1, args.y1)
        distOuter = calculateDistance(args.cx, args.cy, args.x1, args.y1)
        distInner = calculateDistance(args.cx, args.cy, x, y)
    }

    /*Calculate the Star Points*/
    var angInc = 360.0/(args.numPoints*2)
    var odd = true
    for(var i = 0; i < args.numPoints*2; i++)
    {
        var xx
        var yy
        if(odd)
        {
            xx = distOuter*cos((angOuter+(angInc*i))*embConstantPi/180.0)
            yy = distOuter*sin((angOuter+(angInc*i))*embConstantPi/180.0)
        }
        else
        {
            xx = distInner*cos((angOuter+(angInc*i))*embConstantPi/180.0)
            yy = distInner*sin((angOuter+(angInc*i))*embConstantPi/180.0)
        }
        odd = !odd
        setRubberPoint("POLYGON_POINT_" + i.toString(), args.cx + xx, args.cy + yy)
    }
    setRubberText("POLYGON_NUM_POINTS", (args.numPoints*2 - 1).toString())

    "menu-name": "None",
    "menu-position": 0,
    "toolbar-name": "None",
    "toolbar-position": 0,
    "tooltip": "&SysWindows",
    "statustip": "Arrange the windows:  SYSWINDOWS",
    "alias": "WINDOWS, SYSWINDOWS"

/*Command: SysWindows*/

int init():
    clearSelection()
    setPromptPrefix(translate("Enter an option [Cascade/Tile]: "))

int prompt(str):
    if(str == "C" || str == "CASCADE") /*TODO: Probably should add additional qsTr calls here.*/
    {
        windowCascade()
        return
    }
    else if(str == "T" || str == "TILE") /*TODO: Probably should add additional qsTr calls here.*/
    {
        windowTile()
        return
    }
    else
    {
        alert(translate("Invalid option keyword."))
        setPromptPrefix(translate("Enter an option [Cascade/Tile]: "))
    }

/* ----------------------------------------------------------------------- */

def treble_clef_init():
    treble_clef global
    clearSelection()
    args.cx = MAX_DISTANCE+1.0
    args.cy = MAX_DISTANCE+1.0
    args.numPoints = 1024; /*Default //TODO: min:64 max:8192*/
    args.sx = 0.04; /*Default*/
    args.sy = 0.04; /*Default*/
    args.mode = TREBLE_CLEF_MODE_NUM_POINTS

    addRubber("POLYGON")
    setRubberMode("POLYGON")
    updateClef(args.numPoints, args.sx, args.sy)
    spareRubber("POLYGON")
    return

def treble_clef_updateClef(int numPts, double xScale, double yScale):
    int i

    for (i=0; i<=numPts; i++) {
        double t, xx, yy
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
    }

    setRubberText("POLYGON_NUM_POINTS", numPts.toString())

        for (j=0; j<dolphin_curve_basis_ints; j++) {
            float coef = dolphin_curve_x[5*j]/(1.0*dolphin_curve_x[5*j+1])
            float offset = dolphin_curve_x[5*j+2]/(1.0*dolphin_curve_x[5*j+3])
            float t_mult = dophin_curve_x[5*j+4]
            xx += coef * sin(offset + t_mult * t)
        }
        
        for (j=0; j<dolphin_curve_basis_ints; j++) {
            float coef = dolphin_curve_y[5*j]/(1.0*dolphin_curve_y[5*j+1])
            float offset = dolphin_curve_y[5*j+2]/(1.0*dolphin_curve_y[5*j+3])
            float t_mult = dophin_curve_y[5*j+4]
            yy += coef * sin(offset + t_mult * t)
        }
#endif

unsigned int rgb(unsigned char red, unsigned char green, unsigned char blue):
    return blue + green*256 + blue*256*256

int find_ini_value(char *key, char *out):
    int i
    for (i=0; i<settings_data_length; i++) {
        if (settings_data[i] == '\n' || settings_data[i] == '\r') {
            if (!strncmp(settings_data+i+1, key, strlen(key))) {
                int j
                strcpy(out, settings_data+i+2+strlen(key))
                for (j=0; j<strlen(out); j++) {
                    if (out[j] == '\n' || out[j] == '\r') {
                        out[j] = 0
                        break
                    }
                }
                return 1
            }
        }
    }
    return 0

int get_ini_int(char *key, int default_value):
    int r
    r = find_ini_value(key, value_out)
    if (r) {
        return atoi(value_out)
    }
    return default_value

float get_ini_float(char *key, float default_value):
    int r
    r = find_ini_value(key, value_out)
    if (r) {
        return atof(value_out)
    }
    return default_value

char * get_ini_str(char *key, char *default_value):
    int r
    r = find_ini_value(key, value_out)
    if (r) {
        return value_out
    }
    return default_value

int load_settings():
    FILE *f
    app_dir(assets_dir, 0)
    strcpy(settings_fname, assets_dir)
    strcat(settings_fname, "settings.ini")

    puts("Loading settings...")

    /* Step zero: load all of the ini file into a char buffer. */
    f = fopen(settings_fname, "rb")
    if (!f) {
        puts("No settings file found, probably the first run on this system.")
        return 1
    }
    else {
        fseek(f, 0, SEEK_END)
        settings_data_length = ftell(f)
        fseek(f, 0, SEEK_SET)
        fread(settings_data, 1, settings_data_length, f)
        fclose(f)
    }

    settings_data_length = 0

    settings.window_width = get_ini_int("Window_Width", 640)
    settings.window_height = get_ini_int("Window_Height", 480)
    settings.window_width = embClamp(640, settings.window_width, 10000)
    settings.window_height = embClamp(480, settings.window_height, 10000)
    settings.window_x = get_ini_int("Window_PositionX", 0)
    settings.window_y = get_ini_int("Window_PositionY", 0)
    settings.window_x = embClamp(0, settings.window_x, 1000)
    settings.window_y = embClamp(0, settings.window_y, 1000)

    strcpy(settings.general_language, get_ini_str("Language", "default"))
    strcpy(settings.general_icon_theme, get_ini_str("IconTheme", "default"))
    settings.general_icon_size = get_ini_int("IconSize", 16)
    settings.general_mdi_bg_use_logo = get_ini_int("MdiBGUseLogo", 1)
    settings.general_mdi_bg_use_texture = get_ini_int("MdiBGUseTexture", 1)
    settings.general_mdi_bg_use_color = get_ini_int("MdiBGUseColor", 1)
    char default_str[200]
    sprintf(default_str, "%s/images/logo-spirals.png", assets_dir)
    strcpy(settings.general_mdi_bg_logo, get_ini_str("MdiBGLogo", default_str))
    sprintf(default_str, "%s/images/texture-spirals.png", assets_dir)
    strcpy(settings.general_mdi_bg_texture, get_ini_str("MdiBGTexture", default_str))
    settings.general_mdi_bg_color = get_ini_int("MdiBGColor", rgb(192,192,192))
    settings.general_tip_of_the_day = get_ini_int("TipOfTheDay", 1)
    settings.general_current_tip =  get_ini_int("CurrentTip", 0)
    settings.general_system_help_browser = get_ini_int("SystemHelpBrowser", 1)

    /* Display */
    settings.display_use_opengl = get_ini_int("Display_UseOpenGL", 0)
    settings.display_renderhint_aa = get_ini_int("Display_RenderHintAntiAlias", 0)
    settings.display_renderhint_text_aa = get_ini_int("Display_RenderHintTextAntiAlias", 0)
    settings.display_renderhint_smooth_pix = get_ini_int("Display_RenderHintSmoothPixmap", 0)
    settings.display_renderhint_high_aa = get_ini_int("Display_RenderHintHighQualityAntiAlias", 0)
    settings.display_renderhint_noncosmetic = get_ini_int("Display_RenderHintNonCosmetic", 0)
    settings.display_show_scrollbars = get_ini_int("Display_ShowScrollBars", 1)
    settings.display_scrollbar_widget_num = get_ini_int("Display_ScrollBarWidgetNum", 0)
    settings.display_crosshair_color = get_ini_int("Display_CrossHairColor", rgb(  0, 0, 0))
    settings.display_bg_color = get_ini_int("Display_BackgroundColor", rgb(235,235,235))
    settings.display_selectbox_left_color = get_ini_int("Display_SelectBoxLeftColor", rgb(  0,128, 0))
    settings.display_selectbox_left_fill = get_ini_int("Display_SelectBoxLeftFill", rgb(  0,255, 0))
    settings.display_selectbox_right_color = get_ini_int("Display_SelectBoxRightColor", rgb(  0, 0,128))
    settings.display_selectbox_right_fill = get_ini_int("Display_SelectBoxRightFill", rgb(  0, 0,255))
    settings.display_selectbox_alpha = get_ini_int("Display_SelectBoxAlpha", 32)
    settings.display_zoomscale_in = get_ini_float("Display_ZoomScaleIn", 2.0)
    settings.display_zoomscale_out = get_ini_float("Display_ZoomScaleOut", 0.5)
    settings.display_crosshair_percent = get_ini_int("Display_CrossHairPercent", 5)
    strcpy(settings.display_units, get_ini_str("Display_Units", "mm"))

    /* OpenSave */
    /* opensave_custom_filter = QString(get_ini_str("OpenSave_CustomFilter", "supported")); */
    strcpy(settings.opensave_open_format, get_ini_str("OpenSave_OpenFormat", "*.*"))
    settings.opensave_open_thumbnail = get_ini_int("OpenSave_OpenThumbnail", 0)
    strcpy(settings.opensave_save_format, get_ini_str("OpenSave_SaveFormat", "*.*"))
    settings.opensave_save_thumbnail = get_ini_int("OpenSave_SaveThumbnail", 0)

    /* Recent */
    settings.opensave_recent_max_files = get_ini_int("OpenSave_RecentMax", 10)
    /* opensave_recent_list_of_files = get_ini_str("OpenSave_RecentFiles", ""); */
    sprintf(default_str, "%s/samples", assets_dir)
    strcpy(settings.opensave_recent_directory, get_ini_str("OpenSave_RecentDirectory", default_str))

    /* Trimming */
    settings.opensave_trim_dst_num_jumps = get_ini_int("OpenSave_TrimDstNumJumps", 5)

    /* Printing
    settings.printing_default_device = settings_file.value("Printing_DefaultDevice", "").toString()
    settings.printing_use_last_device = settings_file.value("Printing_UseLastDevice", 0)
    settings.printing_disable_bg = settings_file.value("Printing_DisableBG", 1); */
    /* Grid */
    settings.grid_show_on_load = get_ini_int("Grid_ShowOnLoad", 1)
    settings.grid_show_origin = get_ini_int("Grid_ShowOrigin", 1)
    settings.grid_color_match_crosshair = get_ini_int("Grid_ColorMatchCrossHair", 1)
    settings.grid_color = get_ini_int("Grid_Color", rgb(0, 0, 0))
    settings.grid_load_from_file = get_ini_int("Grid_LoadFromFile", 1)
    strcpy(settings.grid_type, get_ini_str("Grid_Type", "Rectangular"))
    settings.grid_center_on_origin = get_ini_int("Grid_CenterOnOrigin", 1)
    settings.grid_center.x = get_ini_float("Grid_CenterX", 0.0)
    settings.grid_center.y = get_ini_float("Grid_CenterY", 0.0)
    settings.grid_size.x = get_ini_float("Grid_SizeX", 100.0)
    settings.grid_size.y = get_ini_float("Grid_SizeY", 100.0)
    settings.grid_spacing.x = get_ini_float("Grid_SpacingX", 25.0)
    settings.grid_spacing.y = get_ini_float("Grid_SpacingY", 25.0)
    settings.grid_size_radius = get_ini_float("Grid_SizeRadius", 50.0)
    settings.grid_spacing_radius = get_ini_float("Grid_SpacingRadius", 25.0)
    settings.grid_spacing_angle = get_ini_float("Grid_SpacingAngle", 45.0)

    /* Ruler */
    settings.ruler_show_on_load = get_ini_int("Ruler_ShowOnLoad", 1)
    settings.ruler_metric = get_ini_int("Ruler_Metric", 1)
    settings.ruler_color = get_ini_int("Ruler_Color", rgb(210,210, 50))
    settings.ruler_pixel_size = get_ini_int("Ruler_PixelSize", 20)

    /* Quick Snap */
    settings.qsnap_enabled = get_ini_int("QuickSnap_Enabled", 1)
    settings.qsnap_locator_color = get_ini_int("QuickSnap_LocatorColor", rgb(255,255, 0))
    settings.qsnap_locator_size = get_ini_int("QuickSnap_LocatorSize", 4)
    settings.qsnap_aperture_size = get_ini_int("QuickSnap_ApertureSize", 10)
    settings.qsnap_endpoint = get_ini_int("QuickSnap_EndPoint", 1)
    settings.qsnap_midpoint = get_ini_int("QuickSnap_MidPoint", 1)
    settings.qsnap_center = get_ini_int("QuickSnap_Center", 1)
    settings.qsnap_node = get_ini_int("QuickSnap_Node", 1)
    settings.qsnap_quadrant = get_ini_int("QuickSnap_Quadrant", 1)
    settings.qsnap_intersection = get_ini_int("QuickSnap_Intersection", 1)
    settings.qsnap_extension = get_ini_int("QuickSnap_Extension", 1)
    settings.qsnap_insertion = get_ini_int("QuickSnap_Insertion", 0)
    settings.qsnap_perpendicular = get_ini_int("QuickSnap_Perpendicular", 1)
    settings.qsnap_tangent = get_ini_int("QuickSnap_Tangent", 1)
    settings.qsnap_nearest = get_ini_int("QuickSnap_Nearest", 0)
    settings.qsnap_apparent = get_ini_int("QuickSnap_Apparent", 0)
    settings.qsnap_parallel = get_ini_int("QuickSnap_Parallel", 0)

    /* LineWeight */
    settings.lwt_show_lwt = get_ini_int("LineWeight_ShowLineWeight", 0)
    settings.lwt_real_render = get_ini_int("LineWeight_RealRender", 1)
    settings.lwt_default_lwt = get_ini_int("LineWeight_DefaultLineWeight", 0)

    /* Selection */
    settings.selection_mode_pickfirst = get_ini_int("Selection_PickFirst", 1)
    settings.selection_mode_pickadd = get_ini_int("Selection_PickAdd", 1)
    settings.selection_mode_pickdrag = get_ini_int("Selection_PickDrag", 0)
    settings.selection_coolgrip_color = get_ini_int("Selection_CoolGripColor", rgb(  0, 0,255))
    settings.selection_hotgrip_color = get_ini_int("Selection_HotGripColor", rgb(255, 0, 0))
    settings.selection_grip_size = get_ini_int("Selection_GripSize", 4)
    settings.selection_pickbox_size = get_ini_int("Selection_PickBoxSize", 4)

    /* Text */
    strcpy(settings.text_font, get_ini_str("Text_Font", "Arial"))
    settings.text_style.size = get_ini_int("Text_Size", 12)
    settings.text_style.angle = get_ini_int("Text_Angle", 0)
    settings.text_style.bold = get_ini_int("Text_StyleBold", 0)
    settings.text_style.italic = get_ini_int("Text_StyleItalic", 0)
    settings.text_style.underline = get_ini_int("Text_StyleUnderline", 0)
    settings.text_style.strikeout = get_ini_int("Text_StyleStrikeOut", 0)
    settings.text_style.overline = get_ini_int("Text_StyleOverline", 0)

    return 0

int save_settings():
    FILE *f
    app_dir(assets_dir, 0)
    strcpy(settings_fname, assets_dir)
    /* This file needs to be read from the users home directory
     * to ensure it is writable. */
    strcat(settings_fname, "settings.ini")
    f = fopen(settings_fname, "rb")
    if (!f) {
        puts("Cannot create settings file.")
        return 1
    }
    
    fprintf(f, "Window_PositionX=%d\r\n", settings.window_x)
    fprintf(f, "Window_PositionY=%d\r\n", settings.window_y)
    fprintf(f, "Window_Width=%d\r\n", settings.window_width)
    fprintf(f, "Window_Height=%d\r\n", settings.window_height)

    /* General */
    /* fprintf(f, "LayoutState=%s\r\n", to_c_str(_mainWin->layoutState)); */
    fprintf(f, "Language=%s\r\n", settings.general_language)
    fprintf(f, "IconTheme=%s\r\n", settings.general_icon_theme)
    fprintf(f, "IconSize=%d\r\n", settings.general_icon_size)
    fprintf(f, "MdiBGUseLogo=%d\r\n", settings.general_mdi_bg_use_logo)
    fprintf(f, "MdiBGUseTexture=%d\r\n", settings.general_mdi_bg_use_texture)
    fprintf(f, "MdiBGUseColor=%d\r\n", settings.general_mdi_bg_use_color)
    fprintf(f, "MdiBGLogo=%s\r\n", settings.general_mdi_bg_logo)
    fprintf(f, "MdiBGTexture=%s\r\n", settings.general_mdi_bg_texture)
    fprintf(f, "MdiBGColor=%d\r\n", settings.general_mdi_bg_color)
    fprintf(f, "TipOfTheDay=%d\r\n", settings.general_tip_of_the_day)
    fprintf(f, "CurrentTip=%d\r\n", settings.general_current_tip + 1)
    fprintf(f, "SystemHelpBrowser=%d\r\n", settings.general_system_help_browser)

    /* Display */
    fprintf(f, "Display_UseOpenGL=%d\r\n", settings.display_use_opengl)
    fprintf(f, "Display_RenderHintAntiAlias=%d\r\n", settings.display_renderhint_aa)
    fprintf(f, "Display_RenderHintTextAntiAlias=%d\r\n", settings.display_renderhint_text_aa)
    fprintf(f, "Display_RenderHintSmoothPixmap=%d\r\n", settings.display_renderhint_smooth_pix)
    fprintf(f, "Display_RenderHintHighQualityAntiAlias=%d\r\n", settings.display_renderhint_high_aa)
    fprintf(f, "Display_RenderHintNonCosmetic=%d\r\n", settings.display_renderhint_noncosmetic)
    fprintf(f, "Display_ShowScrollBars=%d\r\n", settings.display_show_scrollbars)
    fprintf(f, "Display_ScrollBarWidgetNum=%d\r\n", settings.display_scrollbar_widget_num)
    fprintf(f, "Display_CrossHairColor=%d\r\n", settings.display_crosshair_color)
    fprintf(f, "Display_BackgroundColor=%d\r\n", settings.display_bg_color)
    fprintf(f, "Display_SelectBoxLeftColor=%d\r\n", settings.display_selectbox_left_color)
    fprintf(f, "Display_SelectBoxLeftFill=%d\r\n", settings.display_selectbox_left_fill)
    fprintf(f, "Display_SelectBoxRightColor=%d\r\n", settings.display_selectbox_right_color)
    fprintf(f, "Display_SelectBoxRightFill=%d\r\n", settings.display_selectbox_right_fill)
    fprintf(f, "Display_SelectBoxAlpha=%d\r\n", settings.display_selectbox_alpha)
    fprintf(f, "Display_ZoomScaleIn=%f\r\n", settings.display_zoomscale_in)
    fprintf(f, "Display_ZoomScaleOut=%f\r\n", settings.display_zoomscale_out)
    fprintf(f, "Display_CrossHairPercent=%d\r\n", settings.display_crosshair_percent)
    fprintf(f, "Display_Units=%s\r\n", settings.display_units)
    /* OpenSave
    fprintf(f, "OpenSave_CustomFilter=%s\r\n", to_c_str(opensave_custom_filter)); */
    fprintf(f, "OpenSave_OpenFormat=%s\r\n", settings.opensave_open_format)
    fprintf(f, "OpenSave_OpenThumbnail=%d\r\n", settings.opensave_open_thumbnail)
    fprintf(f, "OpenSave_SaveFormat=%s\r\n", settings.opensave_save_format)
    fprintf(f, "OpenSave_SaveThumbnail=%d\r\n", settings.opensave_save_thumbnail)
    //Recent
    fprintf(f, "OpenSave_RecentMax=%d\r\n", settings.opensave_recent_max_files)
    /* fprintf(f, "OpenSave_RecentFiles=%d\r\n", opensave_recent_list_of_files); */
    fprintf(f, "OpenSave_RecentDirectory=%s\r\n", settings.opensave_recent_directory)
    /* Trimming */
    fprintf(f, "OpenSave_TrimDstNumJumps=%d\r\n", settings.opensave_trim_dst_num_jumps)
    /* Printing */
    fprintf(f, "Printing_DefaultDevice=%s\r\n", settings.printing_default_device)
    fprintf(f, "Printing_UseLastDevice=%d\r\n", settings.printing_use_last_device)
    fprintf(f, "Printing_DisableBG=%d\r\n", settings.printing_disable_bg)
    /* Grid */
    fprintf(f, "Grid_ShowOnLoad=%d\r\n", settings.grid_show_on_load)
    fprintf(f, "Grid_ShowOrigin=%d\r\n", settings.grid_show_origin)
    fprintf(f, "Grid_ColorMatchCrossHair=%d\r\n", settings.grid_color_match_crosshair)
    fprintf(f, "Grid_Color=%d\r\n", settings.grid_color)
    fprintf(f, "Grid_LoadFromFile=%d\r\n", settings.grid_load_from_file)
    fprintf(f, "Grid_Type=%s\r\n", settings.grid_type)
    fprintf(f, "Grid_CenterOnOrigin=%d\r\n", settings.grid_center_on_origin)
    fprintf(f, "Grid_CenterX=%f\r\n", settings.grid_center.x)
    fprintf(f, "Grid_CenterY=%f\r\n", settings.grid_center.y)
    fprintf(f, "Grid_SizeX=%f\r\n", settings.grid_size.x)
    fprintf(f, "Grid_SizeY=%f\r\n", settings.grid_size.y)
    fprintf(f, "Grid_SpacingX=%f\r\n", settings.grid_spacing.x)
    fprintf(f, "Grid_SpacingY=%f\r\n", settings.grid_spacing.y)
    fprintf(f, "Grid_SizeRadius=%f\r\n", settings.grid_size_radius)
    fprintf(f, "Grid_SpacingRadius=%f\r\n", settings.grid_spacing_radius)
    fprintf(f, "Grid_SpacingAngle=%f\r\n", settings.grid_spacing_angle)
    //Ruler
    fprintf(f, "Ruler_ShowOnLoad=%d\r\n", settings.ruler_show_on_load)
    fprintf(f, "Ruler_Metric=%d\r\n", settings.ruler_metric)
    fprintf(f, "Ruler_Color=%d\r\n", settings.ruler_color)
    fprintf(f, "Ruler_PixelSize=%d\r\n", settings.ruler_pixel_size)
    //Quick Snap
    fprintf(f, "QuickSnap_Enabled=%d\r\n", settings.qsnap_enabled)
    fprintf(f, "QuickSnap_LocatorColor=%d\r\n", settings.qsnap_locator_color)
    fprintf(f, "QuickSnap_LocatorSize=%d\r\n", settings.qsnap_locator_size)
    fprintf(f, "QuickSnap_ApertureSize=%d\r\n", settings.qsnap_aperture_size)
    fprintf(f, "QuickSnap_EndPoint=%d\r\n", settings.qsnap_endpoint)
    fprintf(f, "QuickSnap_MidPoint=%d\r\n", settings.qsnap_midpoint)
    fprintf(f, "QuickSnap_Center=%d\r\n", settings.qsnap_center)
    fprintf(f, "QuickSnap_Node=%d\r\n", settings.qsnap_node)
    fprintf(f, "QuickSnap_Quadrant=%d\r\n", settings.qsnap_quadrant)
    fprintf(f, "QuickSnap_Intersection=%d\r\n", settings.qsnap_intersection)
    fprintf(f, "QuickSnap_Extension=%d\r\n", settings.qsnap_extension)
    fprintf(f, "QuickSnap_Insertion=%d\r\n", settings.qsnap_insertion)
    fprintf(f, "QuickSnap_Perpendicular=%d\r\n", settings.qsnap_perpendicular)
    fprintf(f, "QuickSnap_Tangent=%d\r\n", settings.qsnap_tangent)
    fprintf(f, "QuickSnap_Nearest=%d\r\n", settings.qsnap_nearest)
    fprintf(f, "QuickSnap_Apparent=%d\r\n", settings.qsnap_apparent)
    fprintf(f, "QuickSnap_Parallel=%d\r\n", settings.qsnap_parallel)
    //LineWeight
    fprintf(f, "LineWeight_ShowLineWeight=%d\r\n", settings.lwt_show_lwt)
    fprintf(f, "LineWeight_RealRender=%d\r\n", settings.lwt_real_render)
    fprintf(f, "LineWeight_DefaultLineWeight=%f\r\n", settings.lwt_default_lwt)

    /* Selection */
    fprintf(f, "Selection_PickFirst=%d\r\n", settings.selection_mode_pickfirst)
    fprintf(f, "Selection_PickAdd=%d\r\n", settings.selection_mode_pickadd)
    fprintf(f, "Selection_PickDrag=%d\r\n", settings.selection_mode_pickdrag)
    fprintf(f, "Selection_CoolGripColor=%d\r\n", settings.selection_coolgrip_color)
    fprintf(f, "Selection_HotGripColor=%d\r\n", settings.selection_hotgrip_color)
    fprintf(f, "Selection_GripSize=%d\r\n", settings.selection_grip_size)
    fprintf(f, "Selection_PickBoxSize=%d\r\n", settings.selection_pickbox_size)

    /* Text */
    fprintf(f, "Text_Font=%s\r\n", settings.text_font)
    fprintf(f, "Text_Size=%f\r\n", settings.text_style.size)
    fprintf(f, "Text_Angle=%f\r\n", settings.text_style.angle)
    fprintf(f, "Text_StyleBold=%d\r\n", settings.text_style.bold)
    fprintf(f, "Text_StyleItalic=%d\r\n", settings.text_style.italic)
    fprintf(f, "Text_StyleUnderline=%d\r\n", settings.text_style.underline)
    fprintf(f, "Text_StyleStrikeOut=%d\r\n", settings.text_style.strikeout)
    fprintf(f, "Text_StyleOverline=%d\r\n", settings.text_style.overline)

    fclose(f)
    return 0

int embClamp(int lower, int x, int upper):
    x = embMinInt(upper, x)
    x = embMaxInt(lower, x)
    return x

def checkBoxTipOfTheDayStateChanged(int checked):
    dialog.general_tip_of_the_day = checked

def checkBoxUseOpenGLStateChanged(int checked):
    dialog.display_use_opengl = checked

def checkBoxRenderHintAAStateChanged(int checked):
    dialog.display_renderhint_aa = checked

def checkBoxRenderHintTextAAStateChanged(int checked):
    dialog.display_renderhint_text_aa = checked

def checkBoxRenderHintSmoothPixStateChanged(int checked):
    dialog.display_renderhint_smooth_pix = checked

def checkBoxRenderHintHighAAStateChanged(int checked):
    dialog.display_renderhint_high_aa = checked

def checkBoxRenderHintNonCosmeticStateChanged(int checked):
    dialog.display_renderhint_noncosmetic = checked

def comboBoxScrollBarWidgetCurrentIndexChanged(int index):
    dialog.display_scrollbar_widget_num = index

def spinBoxZoomScaleInValueChanged(double value):
    dialog.display_zoomscale_in = value

def spinBoxZoomScaleOutValueChanged(value):
    dialog.display_zoomscale_out = value

def checkBoxDisableBGStateChanged(checked):
    dialog.printing_disable_bg = checked

def spinBoxRecentMaxFilesValueChanged(value):
    dialog.opensave_recent_max_files = value

def spinBoxTrimDstNumJumpsValueChanged(value):
    dialog.opensave_trim_dst_num_jumps = value

def checkBoxGridShowOnLoadStateChanged(int checked):
    dialog.grid_show_on_load = checked

def checkBoxGridShowOriginStateChanged(int checked):
    dialog.grid_show_origin = checked

def spinBoxRulerPixelSizeValueChanged(double value):
    dialog.ruler_pixel_size = value

def checkBoxQSnapEndPointStateChanged(int checked):
    dialog.qsnap_endpoint = checked

def checkBoxQSnapMidPointStateChanged(int checked):
    dialog.qsnap_midpoint = checked

def checkBoxQSnapCenterStateChanged(int checked):
    dialog.qsnap_center = checked

def checkBoxQSnapNodeStateChanged(int checked):
    dialog.qsnap_node = checked

def checkBoxQSnapQuadrantStateChanged(int checked):
    dialog.qsnap_quadrant = checked

def checkBoxQSnapIntersectionStateChanged(int checked):
    dialog.qsnap_intersection = checked

def checkBoxQSnapExtensionStateChanged(int checked):
    dialog.qsnap_extension = checked

def checkBoxQSnapInsertionStateChanged(int checked):
    dialog.qsnap_insertion = checked

def checkBoxQSnapPerpendicularStateChanged(int checked):
    dialog.qsnap_perpendicular = checked

def checkBoxQSnapTangentStateChanged(int checked):
    dialog.qsnap_tangent = checked

def checkBoxQSnapNearestStateChanged(int checked):
    dialog.qsnap_nearest = checked

def checkBoxQSnapApparentStateChanged(int checked):
    dialog.qsnap_apparent = checked

def checkBoxQSnapParallelStateChanged(int checked):
    dialog.qsnap_parallel = checked
"""

dialog = {}

def checkBoxSelectionModePickFirstStateChanged(checked):
    dialog["selection_mode_pickfirst"] = checked

def checkBoxSelectionModePickAddStateChanged(checked):
    dialog["selection_mode_pickadd"] = checked

def checkBoxSelectionModePickDragStateChanged(checked):
    dialog["selection_mode_pickdrag"] = checked

def sliderSelectionGripSizeValueChanged(value):
    dialog["selection_grip_size"] = value

"""
def sliderSelectionPickBoxSizeValueChanged(value):
    dialog.selection_pickbox_size = value

def spinBoxGridCenterXValueChanged(double value):
    dialog.grid_center.x = value

def spinBoxGridCenterYValueChanged(double value):
    dialog.grid_center.y = value

def spinBoxGridSizeXValueChanged(double value):
    dialog.grid_size.x = value

def spinBoxGridSizeYValueChanged(double value):
    dialog.grid_size.y = value

def spinBoxGridSpacingXValueChanged(double value):
    dialog.grid_spacing.x = value

def spinBoxGridSpacingYValueChanged(double value):
    dialog.grid_spacing.y = value

def spinBoxGridSizeRadiusValueChanged(double value):
    dialog.grid_size_radius = value

def spinBoxGridSpacingRadiusValueChanged(double value):
    dialog.grid_spacing_radius = value

def spinBoxGridSpacingAngleValueChanged(double value):
    dialog.grid_spacing_angle = value

def checkBoxRulerShowOnLoadStateChanged(int checked):
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

def add_to_path(QPainterPath *path, command, float pos[2], float scale[2])
def add_list_to_path(QPainterPath *path, commands[], float pos[2], float scale[2])

/* Class based code */
class LayerManager : public QDialog:
    Q_OBJECT

public:
    LayerManager(MainWindow* mw, QWidget *parent = 0)
    ~LayerManager()

    void addLayer(const QString& name,
  const int visible,
  const int frozen,
  const float zValue,
  const unsigned int color,
  const QString& lineType,
  const QString& lineWeight,
  const int print)

    QStandardItemModel*    layerModel
    QSortFilterProxyModel* layerModelSorted
    QTreeView* treeView
]

/* On Mac, if the user drops a file on the app's Dock icon, or uses Open As, then this is how the app actually opens the file.*/
class Application : public QApplication:
    Q_OBJECT
public:
    Application(int argc, char **argv)
    void setMainWin(MainWindow* mainWin) { _mainWin = mainWin; }
protected:
    virtual bool event(QEvent *e)
]

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

    /* QPrinter   printer; */

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

    void useBackgroundLogo(int use)
    void useBackgroundTexture(int use)
    void useBackgroundColor(int use)

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
    void windowMenuActivated(int checked/*int id*/ )

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
    /* Help Menu*/
    void tipOfTheDay()
    void buttonTipOfTheDayClicked(int)
    void help();
    void whatsThisContextHelp()

    void selectAll()

    void closeToolBar(QAction*)
    void floatingChangedToolBar(int)

    /* Icons*/
    void iconResize(int iconSize)

    /*Selectors*/
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

    /* Standard Slots*/
    int isShiftPressed()
    void setShiftPressed()
    void setShiftReleased()

    void deletePressed()
    void escapePressed()

    void setTextSize(float num)

    void nativeAddArc(float, float, float, float, float, float, int rubberMode)
    void nativeAddCircle(float centerX, float centerY, float radius, int fill, int rubberMode)
    void nativeAddLine(float, float, float, float, float, int rubberMode)
    void nativeAddEllipse(float centerX, float centerY, float width, float height, float rot, int fill, int rubberMode)
    void nativeAddPoint(float x, float y)
    void nativeAddPolygon(float startX, float startY, const QPainterPath& p, int rubberMode)
    void nativeAddTextSingle(const QString& str, float x, float y, float rot, int fill, int rubberMode)
    void nativeAddPolyline(float startX, float startY, const QPainterPath& p, int rubberMode)
    void nativeAddRectangle(float x, float y, float w, float h, float rot, int fill, int rubberMode)
    void nativeAddDimLeader(float x1, float y1, float x2, float y2, float rot, int rubberMode)
    
    float nativeCalculateAngle(float x1, float y1, float x2, float y2)
    float nativeCalculateDistance(float x1, float y1, float x2, float y2)
    float nativePerpendicularDistance(float px, float py, float x1, float y1, float x2, float y2)

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

    /*Helper functions*/
    QToolButton*   createToolButton(const QString& iconName, const QString& txt)
    QLineEdit* createLineEdit(const QString& validatorType = QString(), int readOnly = false)
    QComboBox* createComboBox(int disable = false)
    QFontComboBox* createFontComboBox(int disable = false)


    void updateLineEditStrIfVaries(QLineEdit* lineEdit, const QString& str)
    void updateLineEditNumIfVaries(QLineEdit* lineEdit, float num, int useAnglePrecision)
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

    /*TODO: Alphabetic/Categorized TabWidget*/

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

    /* Functions */
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

    void setMouseCoord(float x, float y)

]

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

/*Used when checking if fields vary*/
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

/*
 * WARNING
 * -------
 * DO NOT enable QGraphicsItem::ItemIsMovable. If it is enabled,
 * and the item is double clicked, the scene will erratically move the item while zooming.
 * All movement has to be handled explicitly by us, not by the scene.
 */


def MainWindow::readSettings():
    debug_message("Reading Settings...")

    /* This file needs to be read from the users home directory to ensure it is writable. */
    QPoint pos(settings.window_x, settings.window_y)
    QSize size(settings.window_width, settings.window_height)

    /*
    layoutState = settings_file.value("LayoutState").toByteArray()
    if(!restoreState(layoutState))
    {
        debug_message("LayoutState NOT restored! Setting Default Layout...")
        //someToolBar->setVisible(1)
    }
    */

    load_settings()

    move(pos)
    resize(size)

def MainWindow::writeSettings():
    debug_message("Writing Settings...")

    settings.window_x = _mainWin->pos().x()
    settings.window_y = _mainWin->pos().y()
    settings.window_width = _mainWin->size().width()
    settings.window_height = _mainWin->size().height()

    save_settings()

def MainWindow::settingsDialog(const QString& showTab):
    Settings_Dialog dialog_(this, showTab, this)
    dialog_.exec()

View::View(MainWindow* mw, QGraphicsScene* theScene, QWidget* parent) : QGraphicsView(theScene, parent):
    mainWin = mw
    gscene = theScene

    setFrameShape(QFrame::NoFrame)

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
    setViewportUpdateMode(QGraphicsView::FullViewportUpdate)

    panDistance = 10; /*TODO: should there be a setting for this???*/

    setCursor(Qt::BlankCursor)
    horizontalScrollBar()->setCursor(Qt::ArrowCursor)
    verticalScrollBar()->setCursor(Qt::ArrowCursor)
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
    toggleReal(1); /*TODO: load this from file, else settings with default being 1*/

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

    /* Randomize the hot grip location initially so it's not located at (0,0). */
    srand(1234)

    sceneGripPoint = QPointF((rand()%1000)*0.1, (rand()%1000)*0.1)

    gripBaseObj = 0
    tempBaseObj = 0

    selectBox = new SelectBox(QRubberBand::Rectangle, this)
    selectBox->setColors(QColor(settings.display_selectbox_left_color),
                         QColor(settings.display_selectbox_left_fill),
                         QColor(settings.display_selectbox_right_color),
                         QColor(settings.display_selectbox_right_fill),
                         settings.display_selectbox_alpha)

    showScrollBars(settings.display_show_scrollbars)
    setCornerButton()

    installEventFilter(this)

    setMouseTracking(1)
    setBackgroundColor(settings.display_bg_color)
    /*TODO: wrap this with a setBackgroundPixmap() function: setBackgroundBrush(QPixmap("images/canvas));*/

    connect(gscene, SIGNAL(selectionChanged()), this, SLOT(selectionChanged()))

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
            }
        }
    }

    /*==================================================*/
    /*Draw the crosshair*/
    /*==================================================*/

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
                    }
                }
            }
            /*End SelectBox Code*/
        }

        if (settings.pastingActive) {
            QList<QGraphicsItem*> itemList = pasteObjectItemGroup->childItems()
            gscene->destroyItemGroup(pasteObjectItemGroup)
            foreach(QGraphicsItem* item, itemList) {
                gscene->removeItem(item); /*Prevent Qt Runtime Warning, QGraphicsScene::addItem: item has already been added to this scene*/
            }

            foreach(QGraphicsItem* item, itemList) {
                BaseObject* base = static_cast<BaseObject*>(item)
                if (base) {
                }
            }

            settings.pastingActive = 0
            settings.selectingActive = 0
        }
        if (settings.zoomWindowActive) {
            fitInView(path.boundingRect(), Qt::KeepAspectRatio)
            clearSelection()
        }
    }
    if (event->button() == Qt::MiddleButton) {
        panStart(event->pos())
        /*The Undo command will record the spot where the pan started.*/
        event->accept()
    }
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
    }
}

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
    }

    return 1

def View::wheelEvent(QWheelEvent* event):
    int zoomDir = event->pixelDelta().y(); /* TODO: double check this*/
    QPointF mousePoint = event->globalPos(); /* TODO: this is causing weird versioning errors, this appears to be supported on Qt5.12. */

    updateMouseCoords(mousePoint.x(), mousePoint.y())
    if (zoomDir > 0) {
    }
    else {
    }
}

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
    {
        if(itemList.at(i)->data(OBJ_TYPE) != OBJ_TYPE_NULL)
        {
            BaseObject* base = static_cast<BaseObject*>(itemList.at(i))
            if(base)
            {
            }
        }
    }
}

def View::cut():
    if(gscene->selectedItems().isEmpty())
    {
        QMessageBox::information(this, tr("Cut Preselect"), tr("Preselect objects before invoking the cut command."))
        return; /*TODO: Prompt to select objects if nothing is preselected*/
    }

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
    foreach(QGraphicsItem* item, itemList)
    {
        BaseObject* base = static_cast<BaseObject*>(item)
        if(base)
        {
        }
    }

    /*Always clear the selection after a scale*/
    gscene->clearSelection()

int View::numSelected():
    return gscene->selectedItems().size()

def View::showScrollBars(int val):
    if(val)
    {
        setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOn)
        setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOn)
    }
    else
    {
        setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff)
        setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff)
    }
}

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

Settings_Dialog::Settings_Dialog(MainWindow* mw, const QString& showTab, QWidget* parent) : QDialog(parent):
    int i
    mainWin = mw
    setMinimumSize(750,550)

    tabWidget = new QTabWidget(this)

    /*TODO: Add icons to tabs*/
    tabWidget->addTab(createTabGeneral(), tr("General"))
    tabWidget->addTab(createTabFilesPaths(), tr("Files/Paths"))
    tabWidget->addTab(createTabDisplay(), tr("Display"))
    tabWidget->addTab(createTabOpenSave(), tr("Open/Save"))
    tabWidget->addTab(createTabPrinting(), tr("Printing"))
    tabWidget->addTab(createTabSnap(), tr("Snap"))
    tabWidget->addTab(createTabGridRuler(), tr("Grid/Ruler"))
    tabWidget->addTab(createTabOrthoPolar(), tr("Ortho/Polar"))
    tabWidget->addTab(createTabQuickSnap(), tr("QuickSnap"))
    tabWidget->addTab(createTabQuickTrack(), tr("QuickTrack"))
    tabWidget->addTab(createTabLineWeight(), tr("LineWeight"))
    tabWidget->addTab(createTabSelection(), tr("Selection"))

    for (i=0; i<12; i++) {
        if (showTab == settings_tab_label[i]) {
            tabWidget->setCurrentIndex(i)
        }
    }

    buttonBox = new QDialogButtonBox(QDialogButtonBox::Ok | QDialogButtonBox::Cancel)

    connect(buttonBox, SIGNAL(accepted()), this, SLOT(acceptChanges()))
    connect(buttonBox, SIGNAL(rejected()), this, SLOT(rejectChanges()))

    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(this)
    vboxLayoutMain->addWidget(tabWidget)
    vboxLayoutMain->addWidget(buttonBox)
    setLayout(vboxLayoutMain)

    setWindowTitle(tr("Settings"))

    QApplication::setOverrideCursor(Qt::ArrowCursor)

Settings_Dialog::~Settings_Dialog():
    QApplication::restoreOverrideCursor()

QWidget* Settings_Dialog::createTabGeneral():
    QWidget* widget = new QWidget(this)

    /*Language*/
    QGroupBox* groupBoxLanguage = new QGroupBox(tr("Language"), widget)

    QLabel* labelLanguage = new QLabel(tr("Language (Requires Restart)"), groupBoxLanguage)
    QComboBox* comboBoxLanguage = new QComboBox(groupBoxLanguage)
    to_lower(dialog.general_language, settings.general_language)
    comboBoxLanguage->addItem("Default")
    comboBoxLanguage->addItem("System")
    comboBoxLanguage->insertSeparator(2)
    QDir trDir(qApp->applicationDirPath())
    trDir.cd("translations")
    foreach(QString dirName, trDir.entryList(QDir::Dirs | QDir::NoDotAndDotDot))
    {
        dirName[0] = dirName[0].toUpper()
        comboBoxLanguage->addItem(dirName)
    }
    QString current = dialog.general_language
    current[0] = current[0].toUpper()
    comboBoxLanguage->setCurrentIndex(comboBoxLanguage->findText(current))
    connect(comboBoxLanguage, SIGNAL(currentIndexChanged(const QString&)), this, SLOT(comboBoxLanguageCurrentIndexChanged(const QString&)))

    QVBoxLayout* vboxLayoutLanguage = new QVBoxLayout(groupBoxLanguage)
    vboxLayoutLanguage->addWidget(labelLanguage)
    vboxLayoutLanguage->addWidget(comboBoxLanguage)
    groupBoxLanguage->setLayout(vboxLayoutLanguage)

    /*Icons*/
    QGroupBox* groupBoxIcon = new QGroupBox(tr("Icons"), widget)

    QLabel* labelIconTheme = new QLabel(tr("Icon Theme"), groupBoxIcon)
    QComboBox* comboBoxIconTheme = new QComboBox(groupBoxIcon)
    QDir dir(qApp->applicationDirPath())
    dir.cd("icons")
    strcpy(dialog.general_icon_theme, settings.general_icon_theme)
    foreach(QString dirName, dir.entryList(QDir::Dirs | QDir::NoDotAndDotDot))
    {
        comboBoxIconTheme->addItem(loadIcon(theme_xpm), dirName)
    }
    comboBoxIconTheme->setCurrentIndex(comboBoxIconTheme->findText(dialog.general_icon_theme))
    connect(comboBoxIconTheme, SIGNAL(currentIndexChanged(const QString&)), this, SLOT(comboBoxIconThemeCurrentIndexChanged(const QString&)))

    QLabel* labelIconSize = new QLabel(tr("Icon Size"), groupBoxIcon)
    QComboBox* comboBoxIconSize = new QComboBox(groupBoxIcon)
    comboBoxIconSize->addItem(loadIcon(icon16_xpm), "Very Small", 16)
    comboBoxIconSize->addItem(loadIcon(icon24_xpm), "Small", 24)
    comboBoxIconSize->addItem(loadIcon(icon32_xpm), "Medium", 32)
    comboBoxIconSize->addItem(loadIcon(icon48_xpm), "Large", 48)
    comboBoxIconSize->addItem(loadIcon(icon64_xpm), "Very Large", 64)
    comboBoxIconSize->addItem(loadIcon(icon128_xpm), "I'm Blind", 128)
    dialog.general_icon_size = settings.general_icon_size
    comboBoxIconSize->setCurrentIndex(comboBoxIconSize->findData(dialog.general_icon_size))
    connect(comboBoxIconSize, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxIconSizeCurrentIndexChanged(int)))

    QVBoxLayout* vboxLayoutIcon = new QVBoxLayout(groupBoxIcon)
    vboxLayoutIcon->addWidget(labelIconTheme)
    vboxLayoutIcon->addWidget(comboBoxIconTheme)
    vboxLayoutIcon->addWidget(labelIconSize)
    vboxLayoutIcon->addWidget(comboBoxIconSize)
    groupBoxIcon->setLayout(vboxLayoutIcon)

    /*Mdi Background*/
    QGroupBox* groupBoxMdiBG = new QGroupBox(tr("Background"), widget)

    QCheckBox* checkBoxMdiBGUseLogo = new QCheckBox(tr("Use Logo"), groupBoxMdiBG)
    dialog.general_mdi_bg_use_logo = settings.general_mdi_bg_use_logo
    preview.general_mdi_bg_use_logo = dialog.general_mdi_bg_use_logo
    checkBoxMdiBGUseLogo->setChecked(preview.general_mdi_bg_use_logo)
    connect(checkBoxMdiBGUseLogo, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGeneralMdiBGUseLogoStateChanged(int)))

    QPushButton* buttonMdiBGLogo = new QPushButton(tr("Choose"), groupBoxMdiBG)
    buttonMdiBGLogo->setEnabled(dialog.general_mdi_bg_use_logo)
    strcpy(dialog.general_mdi_bg_logo, settings.general_mdi_bg_logo)
    strcpy(accept_.general_mdi_bg_logo, dialog.general_mdi_bg_logo)
    connect(buttonMdiBGLogo, SIGNAL(clicked()), this, SLOT(chooseGeneralMdiBackgroundLogo()))
    connect(checkBoxMdiBGUseLogo, SIGNAL(toggled(int)), buttonMdiBGLogo, SLOT(setEnabled(int)))

    QCheckBox* checkBoxMdiBGUseTexture = new QCheckBox(tr("Use Texture"), groupBoxMdiBG)
    dialog.general_mdi_bg_use_texture = settings.general_mdi_bg_use_texture
    preview.general_mdi_bg_use_texture = dialog.general_mdi_bg_use_texture
    checkBoxMdiBGUseTexture->setChecked(preview.general_mdi_bg_use_texture)
    connect(checkBoxMdiBGUseTexture, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGeneralMdiBGUseTextureStateChanged(int)))

    QPushButton* buttonMdiBGTexture = new QPushButton(tr("Choose"), groupBoxMdiBG)
    buttonMdiBGTexture->setEnabled(dialog.general_mdi_bg_use_texture)
    strcpy(dialog.general_mdi_bg_texture, settings.general_mdi_bg_texture)
    strcpy(accept_.general_mdi_bg_texture, dialog.general_mdi_bg_texture)
    connect(buttonMdiBGTexture, SIGNAL(clicked()), this, SLOT(chooseGeneralMdiBackgroundTexture()))
    connect(checkBoxMdiBGUseTexture, SIGNAL(toggled(int)), buttonMdiBGTexture, SLOT(setEnabled(int)))

    QCheckBox* checkBoxMdiBGUseColor = new QCheckBox(tr("Use Color"), groupBoxMdiBG)
    dialog.general_mdi_bg_use_color = settings.general_mdi_bg_use_color
    preview.general_mdi_bg_use_color = dialog.general_mdi_bg_use_color
    checkBoxMdiBGUseColor->setChecked(preview.general_mdi_bg_use_color)
    connect(checkBoxMdiBGUseColor, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGeneralMdiBGUseColorStateChanged(int)))

    QPushButton* buttonMdiBGColor = new QPushButton(tr("Choose"), groupBoxMdiBG)
    buttonMdiBGColor->setEnabled(dialog.general_mdi_bg_use_color)
    dialog.general_mdi_bg_color = settings.general_mdi_bg_color
    preview.general_mdi_bg_color = dialog.general_mdi_bg_color
    accept_.general_mdi_bg_color = dialog.general_mdi_bg_color
    QPixmap mdiBGPix(16,16)
    mdiBGPix.fill(QColor(preview.general_mdi_bg_color))
    buttonMdiBGColor->setIcon(QIcon(mdiBGPix))
    connect(buttonMdiBGColor, SIGNAL(clicked()), this, SLOT(chooseGeneralMdiBackgroundColor()))
    connect(checkBoxMdiBGUseColor, SIGNAL(toggled(int)), buttonMdiBGColor, SLOT(setEnabled(int)))

    QGridLayout* gridLayoutMdiBG = new QGridLayout(widget)
    gridLayoutMdiBG->addWidget(checkBoxMdiBGUseLogo, 0, 0, Qt::AlignLeft)
    gridLayoutMdiBG->addWidget(buttonMdiBGLogo, 0, 1, Qt::AlignRight)
    gridLayoutMdiBG->addWidget(checkBoxMdiBGUseTexture, 1, 0, Qt::AlignLeft)
    gridLayoutMdiBG->addWidget(buttonMdiBGTexture, 1, 1, Qt::AlignRight)
    gridLayoutMdiBG->addWidget(checkBoxMdiBGUseColor, 2, 0, Qt::AlignLeft)
    gridLayoutMdiBG->addWidget(buttonMdiBGColor, 2, 1, Qt::AlignRight)
    groupBoxMdiBG->setLayout(gridLayoutMdiBG)

    /*Tips*/
    QGroupBox* groupBoxTips = new QGroupBox(tr("Tips"), widget)

    QCheckBox* checkBoxTipOfTheDay = new QCheckBox(tr("Show Tip of the Day on startup"), groupBoxTips)
    dialog.general_tip_of_the_day = settings.general_tip_of_the_day
    checkBoxTipOfTheDay->setChecked(dialog.general_tip_of_the_day)
    connect(checkBoxTipOfTheDay, SIGNAL(stateChanged(int)), this, SLOT(checkBoxTipOfTheDayStateChanged(int)))

    QVBoxLayout* vboxLayoutTips = new QVBoxLayout(groupBoxTips)
    vboxLayoutTips->addWidget(checkBoxTipOfTheDay)
    groupBoxTips->setLayout(vboxLayoutTips)

    /*Help Browser*/
    QGroupBox* groupBoxHelpBrowser = new QGroupBox(tr("Help Browser"), widget)

    QRadioButton* radioButtonSystemHelpBrowser = new QRadioButton(tr("System"), groupBoxHelpBrowser)
    radioButtonSystemHelpBrowser->setChecked(settings.general_system_help_browser)
    QRadioButton* radioButtonCustomHelpBrowser = new QRadioButton(tr("Custom"), groupBoxHelpBrowser)
    radioButtonCustomHelpBrowser->setChecked(!settings.general_system_help_browser)
    radioButtonCustomHelpBrowser->setEnabled(0); /*TODO: finish this*/

    QVBoxLayout* vboxLayoutHelpBrowser = new QVBoxLayout(groupBoxHelpBrowser)
    vboxLayoutHelpBrowser->addWidget(radioButtonSystemHelpBrowser)
    vboxLayoutHelpBrowser->addWidget(radioButtonCustomHelpBrowser)
    groupBoxHelpBrowser->setLayout(vboxLayoutHelpBrowser)

    /*Widget Layout*/
    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(widget)
    vboxLayoutMain->addWidget(groupBoxLanguage)
    vboxLayoutMain->addWidget(groupBoxIcon)
    vboxLayoutMain->addWidget(groupBoxMdiBG)
    vboxLayoutMain->addWidget(groupBoxTips)
    vboxLayoutMain->addWidget(groupBoxHelpBrowser)
    vboxLayoutMain->addStretch(1)
    widget->setLayout(vboxLayoutMain)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea->setWidgetResizable(1)
    scrollArea->setWidget(widget)
    return scrollArea

QWidget* Settings_Dialog::createTabFilesPaths():
    QWidget* widget = new QWidget(this)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea->setWidgetResizable(1)
    scrollArea->setWidget(widget)
    return scrollArea

QWidget* Settings_Dialog::createTabDisplay():
    QWidget* widget = new QWidget(this)

    /*Rendering*/
    /*TODO: Review OpenGL and Rendering settings for future inclusion*/
    /*
    QGroupBox* groupBoxRender = new QGroupBox(tr("Rendering"), widget)

    QCheckBox* checkBoxUseOpenGL = new QCheckBox(tr("Use OpenGL"), groupBoxRender)
    dialog.display_use_opengl = settings.display_use_open_gl
    checkBoxUseOpenGL->setChecked(dialog.display_use_opengl)
    connect(checkBoxUseOpenGL, SIGNAL(stateChanged(int)), this, SLOT(checkBoxUseOpenGLStateChanged(int)))

    QCheckBox* checkBoxRenderHintAA = new QCheckBox(tr("Antialias"), groupBoxRender)
    dialog.display_renderhint_aa = settings.display_render_hint_aa
    checkBoxRenderHintAA->setChecked(dialog.display_renderhint_aa)
    connect(checkBoxRenderHintAA, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRenderHintAAStateChanged(int)))

    QCheckBox* checkBoxRenderHintTextAA = new QCheckBox(tr("Antialias Text"), groupBoxRender)
    dialog.display_renderhint_text_aa = settings.display_render_hint_text_aa
    checkBoxRenderHintTextAA->setChecked(dialog.display_renderhint_text_aa)
    connect(checkBoxRenderHintTextAA, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRenderHintTextAAStateChanged(int)))

    QCheckBox* checkBoxRenderHintSmoothPix = new QCheckBox(tr("Smooth Pixmap"), groupBoxRender)
    dialog.display_renderhint_smooth_pix = settings.display_render_hint_smooth_pix
    checkBoxRenderHintSmoothPix->setChecked(dialog.display_renderhint_smooth_pix)
    connect(checkBoxRenderHintSmoothPix, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRenderHintSmoothPixStateChanged(int)))

    QCheckBox* checkBoxRenderHintHighAA = new QCheckBox(tr("High Quality Antialiasing (OpenGL)"), groupBoxRender)
    dialog.display_renderhint_high_aa = settings.display_render_hint_high_aa
    checkBoxRenderHintHighAA->setChecked(dialog.display_renderhint_high_aa)
    connect(checkBoxRenderHintHighAA, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRenderHintHighAAStateChanged(int)))

    QCheckBox* checkBoxRenderHintNonCosmetic = new QCheckBox(tr("Non Cosmetic"), groupBoxRender)
    dialog.display_renderhint_noncosmetic = settings.display_render_hint_non_cosmetic
    checkBoxRenderHintNonCosmetic->setChecked(dialog.display_renderhint_noncosmetic)
    connect(checkBoxRenderHintNonCosmetic, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRenderHintNonCosmeticStateChanged(int)))

    QVBoxLayout* vboxLayoutRender = new QVBoxLayout(groupBoxRender)
    vboxLayoutRender->addWidget(checkBoxUseOpenGL)
    vboxLayoutRender->addWidget(checkBoxRenderHintAA)
    vboxLayoutRender->addWidget(checkBoxRenderHintTextAA)
    vboxLayoutRender->addWidget(checkBoxRenderHintSmoothPix)
    vboxLayoutRender->addWidget(checkBoxRenderHintHighAA)
    vboxLayoutRender->addWidget(checkBoxRenderHintNonCosmetic)
    groupBoxRender->setLayout(vboxLayoutRender)
    */

    /*ScrollBars*/
    QGroupBox* groupBoxScrollBars = new QGroupBox(tr("ScrollBars"), widget)

    QCheckBox* checkBoxShowScrollBars = new QCheckBox(tr("Show ScrollBars"), groupBoxScrollBars)
    dialog.display_show_scrollbars = settings.display_show_scrollbars
    preview.display_show_scrollbars = dialog.display_show_scrollbars
    checkBoxShowScrollBars->setChecked(preview.display_show_scrollbars)
    connect(checkBoxShowScrollBars, SIGNAL(stateChanged(int)), this, SLOT(checkBoxShowScrollBarsStateChanged(int)))

    QLabel* labelScrollBarWidget = new QLabel(tr("Perform action when clicking corner widget"), groupBoxScrollBars)
    QComboBox* comboBoxScrollBarWidget = new QComboBox(groupBoxScrollBars)
    dialog.display_scrollbar_widget_num = settings.display_scrollbar_widget_num
    int numActions = mainWin->actionHash.size()
    for(int i = 0; i < numActions; i++)
    {
        QAction* action = mainWin->actionHash.value(i)
        if(action) comboBoxScrollBarWidget->addItem(action->icon(), action->text().replace("&", ""))
    }
    comboBoxScrollBarWidget->setCurrentIndex(dialog.display_scrollbar_widget_num)
    connect(comboBoxScrollBarWidget, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxScrollBarWidgetCurrentIndexChanged(int)))

    QVBoxLayout* vboxLayoutScrollBars = new QVBoxLayout(groupBoxScrollBars)
    vboxLayoutScrollBars->addWidget(checkBoxShowScrollBars)
    vboxLayoutScrollBars->addWidget(labelScrollBarWidget)
    vboxLayoutScrollBars->addWidget(comboBoxScrollBarWidget)
    groupBoxScrollBars->setLayout(vboxLayoutScrollBars)

    /*Colors*/
    QGroupBox* groupBoxColor = new QGroupBox(tr("Colors"), widget)

    QLabel* labelCrossHairColor = new QLabel(tr("Crosshair Color"), groupBoxColor)
    QPushButton* buttonCrossHairColor = new QPushButton(tr("Choose"), groupBoxColor)
    dialog.display_crosshair_color = settings.display_crosshair_color
    preview.display_crosshair_color = dialog.display_crosshair_color
    accept_.display_crosshair_color = dialog.display_crosshair_color
    QPixmap crosshairPix(16,16)
    crosshairPix.fill(QColor(preview.display_crosshair_color))
    buttonCrossHairColor->setIcon(QIcon(crosshairPix))
    connect(buttonCrossHairColor, SIGNAL(clicked()), this, SLOT(chooseDisplayCrossHairColor()))

    QLabel* labelBGColor = new QLabel(tr("Background Color"), groupBoxColor)
    QPushButton* buttonBGColor = new QPushButton(tr("Choose"), groupBoxColor)
    dialog.display_bg_color = settings.display_bg_color
    preview.display_bg_color = dialog.display_bg_color
    accept_.display_bg_color = dialog.display_bg_color
    QPixmap bgPix(16,16)
    bgPix.fill(QColor(preview.display_bg_color))
    buttonBGColor->setIcon(QIcon(bgPix))
    connect(buttonBGColor, SIGNAL(clicked()), this, SLOT(chooseDisplayBackgroundColor()))

    QLabel* labelSelectBoxLeftColor = new QLabel(tr("Selection Box Color (Crossing)"), groupBoxColor)
    QPushButton* buttonSelectBoxLeftColor = new QPushButton(tr("Choose"), groupBoxColor)
    dialog.display_selectbox_left_color = settings.display_selectbox_left_color
    preview.display_selectbox_left_color = dialog.display_selectbox_left_color
    accept_.display_selectbox_left_color = dialog.display_selectbox_left_color
    QPixmap sBoxLCPix(16,16)
    sBoxLCPix.fill(QColor(preview.display_selectbox_left_color))
    buttonSelectBoxLeftColor->setIcon(QIcon(sBoxLCPix))
    connect(buttonSelectBoxLeftColor, SIGNAL(clicked()), this, SLOT(chooseDisplaySelectBoxLeftColor()))

    QLabel* labelSelectBoxLeftFill = new QLabel(tr("Selection Box Fill (Crossing)"), groupBoxColor)
    QPushButton* buttonSelectBoxLeftFill = new QPushButton(tr("Choose"), groupBoxColor)
    dialog.display_selectbox_left_fill = settings.display_selectbox_left_fill
    preview.display_selectbox_left_fill = dialog.display_selectbox_left_fill
    accept_.display_selectbox_left_fill = dialog.display_selectbox_left_fill
    QPixmap sBoxLFPix(16,16)
    sBoxLFPix.fill(QColor(preview.display_selectbox_left_fill))
    buttonSelectBoxLeftFill->setIcon(QIcon(sBoxLFPix))
    connect(buttonSelectBoxLeftFill, SIGNAL(clicked()), this, SLOT(chooseDisplaySelectBoxLeftFill()))

    QLabel* labelSelectBoxRightColor = new QLabel(tr("Selection Box Color (Window)"), groupBoxColor)
    QPushButton* buttonSelectBoxRightColor = new QPushButton(tr("Choose"), groupBoxColor)
    dialog.display_selectbox_right_color = settings.display_selectbox_right_color
    preview.display_selectbox_right_color = dialog.display_selectbox_right_color
    accept_.display_selectbox_right_color = dialog.display_selectbox_right_color
    QPixmap sBoxRCPix(16,16)
    sBoxRCPix.fill(QColor(preview.display_selectbox_right_color))
    buttonSelectBoxRightColor->setIcon(QIcon(sBoxRCPix))
    connect(buttonSelectBoxRightColor, SIGNAL(clicked()), this, SLOT(chooseDisplaySelectBoxRightColor()))

    QLabel* labelSelectBoxRightFill = new QLabel(tr("Selection Box Fill (Window)"), groupBoxColor)
    QPushButton* buttonSelectBoxRightFill = new QPushButton(tr("Choose"), groupBoxColor)
    dialog.display_selectbox_right_fill = settings.display_selectbox_right_fill
    preview.display_selectbox_right_fill = dialog.display_selectbox_right_fill
    accept_.display_selectbox_right_fill = dialog.display_selectbox_right_fill
    QPixmap sBoxRFPix(16,16)
    sBoxRFPix.fill(QColor(preview.display_selectbox_right_fill))
    buttonSelectBoxRightFill->setIcon(QIcon(sBoxRFPix))
    connect(buttonSelectBoxRightFill, SIGNAL(clicked()), this, SLOT(chooseDisplaySelectBoxRightFill()))

    QLabel* labelSelectBoxAlpha = new QLabel(tr("Selection Box Fill Alpha"), groupBoxColor)
    QSpinBox* spinBoxSelectBoxAlpha = new QSpinBox(groupBoxColor)
    spinBoxSelectBoxAlpha->setRange(0, 255)
    dialog.display_selectbox_alpha = settings.display_selectbox_alpha
    preview.display_selectbox_alpha = dialog.display_selectbox_alpha
    spinBoxSelectBoxAlpha->setValue(preview.display_selectbox_alpha)
    connect(spinBoxSelectBoxAlpha, SIGNAL(valueChanged(int)), this, SLOT(spinBoxDisplaySelectBoxAlphaValueChanged(int)))

    QGridLayout* gridLayoutColor = new QGridLayout(widget)
    gridLayoutColor->addWidget(labelCrossHairColor, 0, 0, Qt::AlignLeft)
    gridLayoutColor->addWidget(buttonCrossHairColor, 0, 1, Qt::AlignRight)
    gridLayoutColor->addWidget(labelBGColor, 1, 0, Qt::AlignLeft)
    gridLayoutColor->addWidget(buttonBGColor, 1, 1, Qt::AlignRight)
    gridLayoutColor->addWidget(labelSelectBoxLeftColor, 2, 0, Qt::AlignLeft)
    gridLayoutColor->addWidget(buttonSelectBoxLeftColor, 2, 1, Qt::AlignRight)
    gridLayoutColor->addWidget(labelSelectBoxLeftFill, 3, 0, Qt::AlignLeft)
    gridLayoutColor->addWidget(buttonSelectBoxLeftFill, 3, 1, Qt::AlignRight)
    gridLayoutColor->addWidget(labelSelectBoxRightColor, 4, 0, Qt::AlignLeft)
    gridLayoutColor->addWidget(buttonSelectBoxRightColor, 4, 1, Qt::AlignRight)
    gridLayoutColor->addWidget(labelSelectBoxRightFill, 5, 0, Qt::AlignLeft)
    gridLayoutColor->addWidget(buttonSelectBoxRightFill, 5, 1, Qt::AlignRight)
    gridLayoutColor->addWidget(labelSelectBoxAlpha, 6, 0, Qt::AlignLeft)
    gridLayoutColor->addWidget(spinBoxSelectBoxAlpha, 6, 1, Qt::AlignRight)
    groupBoxColor->setLayout(gridLayoutColor)

    /*Zoom*/
    QGroupBox* groupBoxZoom = new QGroupBox(tr("Zoom"), widget)

    QLabel* labelZoomScaleIn = new QLabel(tr("Zoom In Scale"), groupBoxZoom)
    QDoubleSpinBox* spinBoxZoomScaleIn = new QDoubleSpinBox(groupBoxZoom)
    dialog.display_zoomscale_in = settings.display_zoomscale_in
    spinBoxZoomScaleIn->setValue(dialog.display_zoomscale_in)
    spinBoxZoomScaleIn->setSingleStep(0.01)
    spinBoxZoomScaleIn->setRange(1.01, 10.00)
    connect(spinBoxZoomScaleIn, SIGNAL(valueChanged(double)), this, SLOT(spinBoxZoomScaleInValueChanged(double)))

    QLabel* labelZoomScaleOut = new QLabel(tr("Zoom Out Scale"), groupBoxZoom)
    QDoubleSpinBox* spinBoxZoomScaleOut = new QDoubleSpinBox(groupBoxZoom)
    dialog.display_zoomscale_out = settings.display_zoomscale_out
    spinBoxZoomScaleOut->setValue(dialog.display_zoomscale_out)
    spinBoxZoomScaleOut->setSingleStep(0.01)
    spinBoxZoomScaleOut->setRange(0.01, 0.99)
    connect(spinBoxZoomScaleOut, SIGNAL(valueChanged(double)), this, SLOT(spinBoxZoomScaleOutValueChanged(double)))

    QGridLayout* gridLayoutZoom = new QGridLayout(groupBoxZoom)
    gridLayoutZoom->addWidget(labelZoomScaleIn, 0, 0, Qt::AlignLeft)
    gridLayoutZoom->addWidget(spinBoxZoomScaleIn, 0, 1, Qt::AlignRight)
    gridLayoutZoom->addWidget(labelZoomScaleOut, 1, 0, Qt::AlignLeft)
    gridLayoutZoom->addWidget(spinBoxZoomScaleOut, 1, 1, Qt::AlignRight)
    groupBoxZoom->setLayout(gridLayoutZoom)

    /*Widget Layout*/
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget)
    /*vboxLayoutMain->addWidget(groupBoxRender); //TODO: Review OpenGL and Rendering settings for future inclusion*/
    vboxLayoutMain->addWidget(groupBoxScrollBars)
    vboxLayoutMain->addWidget(groupBoxColor)
    vboxLayoutMain->addWidget(groupBoxZoom)
    vboxLayoutMain->addStretch(1)
    widget->setLayout(vboxLayoutMain)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea->setWidgetResizable(1)
    scrollArea->setWidget(widget)
    return scrollArea

/* TODO: finish open/save options */
QWidget* Settings_Dialog::createTabOpenSave():
    QWidget* widget = new QWidget(this)

    /*Custom Filter*/
    QGroupBox* groupBoxCustomFilter = new QGroupBox(tr("Custom Filter"), widget)
    groupBoxCustomFilter->setEnabled(0); /*TODO: Fixup custom filter*/

    QPushButton* buttonCustomFilterSelectAll = new QPushButton(tr("Select All"), groupBoxCustomFilter)
    connect(buttonCustomFilterSelectAll, SIGNAL(clicked()), this, SLOT(buttonCustomFilterSelectAllClicked()))
    QPushButton* buttonCustomFilterClearAll = new QPushButton("Clear All", groupBoxCustomFilter)
    connect(buttonCustomFilterClearAll, SIGNAL(clicked()), this, SLOT(buttonCustomFilterClearAllClicked()))
    QGridLayout* gridLayoutCustomFilter = new QGridLayout(groupBoxCustomFilter)

    int i
    for (i=0; i<numberOfFormats; i++) {
        QCheckBox* c = new QCheckBox(formatTable[i].extension, groupBoxCustomFilter)
        c->setChecked(opensave_custom_filter.contains(QString("*") + formatTable[i].extension, Qt::CaseInsensitive))
        connect(c, SIGNAL(stateChanged(int)), this, SLOT(checkBoxCustomFilterStateChanged(int)))
        connect(this, SIGNAL(buttonCustomFilterSelectAll(int)), c, SLOT(setChecked(int)))
        connect(this, SIGNAL(buttonCustomFilterClearAll(int)), c, SLOT(setChecked(int)))
        gridLayoutCustomFilter->addWidget(c, i%10, i/10, Qt::AlignLeft)
    }

    gridLayoutCustomFilter->addWidget(buttonCustomFilterSelectAll, 0, 7, Qt::AlignLeft)
    gridLayoutCustomFilter->addWidget(buttonCustomFilterClearAll, 1, 7, Qt::AlignLeft)
    gridLayoutCustomFilter->setColumnStretch(7,1)
    groupBoxCustomFilter->setLayout(gridLayoutCustomFilter)

    if(opensave_custom_filter.contains("supported", Qt::CaseInsensitive)) buttonCustomFilterSelectAllClicked()

    /* Opening */
    QGroupBox* groupBoxOpening = new QGroupBox(tr("File Open"), widget)

    QComboBox* comboBoxOpenFormat = new QComboBox(groupBoxOpening)

    QCheckBox* checkBoxOpenThumbnail = new QCheckBox(tr("Preview Thumbnails"), groupBoxOpening)
    checkBoxOpenThumbnail->setChecked(0)

    /* TODO: Add a button to clear the recent history. */

    QLabel* labelRecentMaxFiles = new QLabel(tr("Number of recently accessed files to show"), groupBoxOpening)
    QSpinBox* spinBoxRecentMaxFiles = new QSpinBox(groupBoxOpening)
    spinBoxRecentMaxFiles->setRange(0, 10)
    dialog.opensave_recent_max_files = settings.opensave_recent_max_files
    spinBoxRecentMaxFiles->setValue(dialog.opensave_recent_max_files)
    connect(spinBoxRecentMaxFiles, SIGNAL(valueChanged(int)), this, SLOT(spinBoxRecentMaxFilesValueChanged(int)))

    QFrame* frameRecent = new QFrame(groupBoxOpening)
    QGridLayout* gridLayoutRecent = new QGridLayout(frameRecent)
    gridLayoutRecent->addWidget(labelRecentMaxFiles, 0, 0, Qt::AlignLeft)
    gridLayoutRecent->addWidget(spinBoxRecentMaxFiles, 0, 1, Qt::AlignRight)
    frameRecent->setLayout(gridLayoutRecent)

    QVBoxLayout* vboxLayoutOpening = new QVBoxLayout(groupBoxOpening)
    vboxLayoutOpening->addWidget(comboBoxOpenFormat)
    vboxLayoutOpening->addWidget(checkBoxOpenThumbnail)
    vboxLayoutOpening->addWidget(frameRecent)
    groupBoxOpening->setLayout(vboxLayoutOpening)

    /*Saving*/
    QGroupBox* groupBoxSaving = new QGroupBox(tr("File Save"), widget)

    QComboBox* comboBoxSaveFormat = new QComboBox(groupBoxSaving)

    QCheckBox* checkBoxSaveThumbnail = new QCheckBox(tr("Save Thumbnails"), groupBoxSaving)
    checkBoxSaveThumbnail->setChecked(0)

    QCheckBox* checkBoxAutoSave = new QCheckBox(tr("AutoSave"), groupBoxSaving)
    checkBoxAutoSave->setChecked(0)

    QVBoxLayout* vboxLayoutSaving = new QVBoxLayout(groupBoxSaving)
    vboxLayoutSaving->addWidget(comboBoxSaveFormat)
    vboxLayoutSaving->addWidget(checkBoxSaveThumbnail)
    vboxLayoutSaving->addWidget(checkBoxAutoSave)
    groupBoxSaving->setLayout(vboxLayoutSaving)

    /*Trimming*/
    QGroupBox* groupBoxTrim = new QGroupBox(tr("Trimming"), widget)

    QLabel* labelTrimDstNumJumps = new QLabel(tr("DST Only: Minimum number of jumps to trim"), groupBoxTrim)
    QSpinBox* spinBoxTrimDstNumJumps = new QSpinBox(groupBoxTrim)
    spinBoxTrimDstNumJumps->setRange(1, 20)
    dialog.opensave_trim_dst_num_jumps = settings.opensave_trim_dst_num_jumps
    spinBoxTrimDstNumJumps->setValue(dialog.opensave_trim_dst_num_jumps)
    connect(spinBoxTrimDstNumJumps, SIGNAL(valueChanged(int)), this, SLOT(spinBoxTrimDstNumJumpsValueChanged(int)))

    QFrame* frameTrimDstNumJumps = new QFrame(groupBoxTrim)
    QGridLayout* gridLayoutTrimDstNumJumps = new QGridLayout(frameTrimDstNumJumps)
    gridLayoutTrimDstNumJumps->addWidget(labelTrimDstNumJumps, 0, 0, Qt::AlignLeft)
    gridLayoutTrimDstNumJumps->addWidget(spinBoxTrimDstNumJumps, 0, 1, Qt::AlignRight)
    frameTrimDstNumJumps->setLayout(gridLayoutTrimDstNumJumps)

    QVBoxLayout* vboxLayoutTrim = new QVBoxLayout(groupBoxTrim)
    vboxLayoutTrim->addWidget(frameTrimDstNumJumps)
    groupBoxTrim->setLayout(vboxLayoutTrim)

    /*Widget Layout*/
    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(widget)
    vboxLayoutMain->addWidget(groupBoxCustomFilter)
    vboxLayoutMain->addWidget(groupBoxOpening)
    vboxLayoutMain->addWidget(groupBoxSaving)
    vboxLayoutMain->addWidget(groupBoxTrim)
    vboxLayoutMain->addStretch(1)
    widget->setLayout(vboxLayoutMain)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea->setWidgetResizable(1)
    scrollArea->setWidget(widget)
    return scrollArea

QWidget* Settings_Dialog::createTabPrinting():
    /*
    QWidget* widget = new QWidget(this)

    //Default Printer
    QGroupBox* groupBoxDefaultPrinter = new QGroupBox(tr("Default Printer"), widget)

    QRadioButton* radioButtonUseSame = new QRadioButton(tr("Use as default device"), groupBoxDefaultPrinter)
    radioButtonUseSame->setChecked(!settings.printing_use_last_device)
    QRadioButton* radioButtonUseLast = new QRadioButton(tr("Use last used device"), groupBoxDefaultPrinter)
    radioButtonUseLast->setChecked(settings.printing_use_last_device)

    QComboBox* comboBoxDefaultDevice = new QComboBox(groupBoxDefaultPrinter)
    QList<QPrinterInfo> listAvailPrinters = QPrinterInfo::availablePrinters()
    foreach(QPrinterInfo info, listAvailPrinters)
    {
        comboBoxDefaultDevice->addItem(loadIcon(print_xpm), info.printerName())
    }

    QVBoxLayout* vboxLayoutDefaultPrinter = new QVBoxLayout(groupBoxDefaultPrinter)
    vboxLayoutDefaultPrinter->addWidget(radioButtonUseSame)
    vboxLayoutDefaultPrinter->addWidget(comboBoxDefaultDevice)
    vboxLayoutDefaultPrinter->addWidget(radioButtonUseLast)
    groupBoxDefaultPrinter->setLayout(vboxLayoutDefaultPrinter)

    //Save Ink
    QGroupBox* groupBoxSaveInk = new QGroupBox(tr("Save Ink"), widget)

    QCheckBox* checkBoxDisableBG = new QCheckBox(tr("Disable Background"), groupBoxSaveInk)
    dialog.printing_disable_bg = settings.printing_disable_bg
    checkBoxDisableBG->setChecked(dialog.printing_disable_bg)
    connect(checkBoxDisableBG, SIGNAL(stateChanged(int)), this, SLOT(checkBoxDisableBGStateChanged(int)))

    QVBoxLayout* vboxLayoutSaveInk = new QVBoxLayout(groupBoxSaveInk)
    vboxLayoutSaveInk->addWidget(checkBoxDisableBG)
    groupBoxSaveInk->setLayout(vboxLayoutSaveInk)

    //Widget Layout
    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(widget)
    vboxLayoutMain->addWidget(groupBoxDefaultPrinter)
    vboxLayoutMain->addWidget(groupBoxSaveInk)
    vboxLayoutMain->addStretch(1)
    widget->setLayout(vboxLayoutMain)

    */
    QScrollArea* scrollArea = new QScrollArea(this)
    /*scrollArea->setWidgetResizable(1)
    scrollArea->setWidget(widget); */
    return scrollArea

QWidget* Settings_Dialog::createTabSnap():
    QWidget* widget = new QWidget(this)

    /*TODO: finish this*/

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea->setWidgetResizable(1)
    scrollArea->setWidget(widget)
    return scrollArea

QWidget* Settings_Dialog::createTabGridRuler():
    QWidget* widget = new QWidget(this)

    /*Grid Misc*/
    QGroupBox* groupBoxGridMisc = new QGroupBox(tr("Grid Misc"), widget)

    QCheckBox* checkBoxGridShowOnLoad = new QCheckBox(tr("Initially show grid when loading a file"), groupBoxGridMisc)
    dialog.grid_show_on_load = settings.grid_show_on_load
    checkBoxGridShowOnLoad->setChecked(dialog.grid_show_on_load)
    connect(checkBoxGridShowOnLoad, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGridShowOnLoadStateChanged(int)))

    QCheckBox* checkBoxGridShowOrigin = new QCheckBox(tr("Show the origin when the grid is enabled"), groupBoxGridMisc)
    dialog.grid_show_origin = settings.grid_show_origin
    checkBoxGridShowOrigin->setChecked(dialog.grid_show_origin)
    connect(checkBoxGridShowOrigin, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGridShowOriginStateChanged(int)))

    QGridLayout* gridLayoutGridMisc = new QGridLayout(widget)
    gridLayoutGridMisc->addWidget(checkBoxGridShowOnLoad, 0, 0, Qt::AlignLeft)
    gridLayoutGridMisc->addWidget(checkBoxGridShowOrigin, 1, 0, Qt::AlignLeft)
    groupBoxGridMisc->setLayout(gridLayoutGridMisc)

    /*Grid Color*/
    QGroupBox* groupBoxGridColor = new QGroupBox(tr("Grid Color"), widget)

    QCheckBox* checkBoxGridColorMatchCrossHair = new QCheckBox(tr("Match grid color to crosshair color"), groupBoxGridColor)
    dialog.grid_color_match_crosshair = settings.grid_color_match_crosshair
    checkBoxGridColorMatchCrossHair->setChecked(dialog.grid_color_match_crosshair)
    connect(checkBoxGridColorMatchCrossHair, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGridColorMatchCrossHairStateChanged(int)))

    QLabel* labelGridColor = new QLabel(tr("Grid Color"), groupBoxGridColor)
    labelGridColor->setObjectName("labelGridColor")
    QPushButton* buttonGridColor = new QPushButton(tr("Choose"), groupBoxGridColor)
    buttonGridColor->setObjectName("buttonGridColor")
    if(dialog.grid_color_match_crosshair) { dialog.grid_color = settings.display_crosshair_color; }
    else                                  { dialog.grid_color = settings.grid_color;             }
    preview.grid_color = dialog.grid_color
    accept_.grid_color = dialog.grid_color
    QPixmap gridPix(16,16)
    gridPix.fill(QColor(preview.grid_color))
    buttonGridColor->setIcon(QIcon(gridPix))
    connect(buttonGridColor, SIGNAL(clicked()), this, SLOT(chooseGridColor()))

    labelGridColor->setEnabled(!dialog.grid_color_match_crosshair)
    buttonGridColor->setEnabled(!dialog.grid_color_match_crosshair)

    QGridLayout* gridLayoutGridColor = new QGridLayout(widget)
    gridLayoutGridColor->addWidget(checkBoxGridColorMatchCrossHair, 0, 0, Qt::AlignLeft)
    gridLayoutGridColor->addWidget(labelGridColor, 1, 0, Qt::AlignLeft)
    gridLayoutGridColor->addWidget(buttonGridColor, 1, 1, Qt::AlignRight)
    groupBoxGridColor->setLayout(gridLayoutGridColor)

    /*Grid Geometry*/
    QGroupBox* groupBoxGridGeom = new QGroupBox(tr("Grid Geometry"), widget)

    QCheckBox* checkBoxGridLoadFromFile = new QCheckBox(tr("Set grid size from opened file"), groupBoxGridGeom)
    dialog.grid_load_from_file = settings.grid_load_from_file
    checkBoxGridLoadFromFile->setChecked(dialog.grid_load_from_file)
    connect(checkBoxGridLoadFromFile, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGridLoadFromFileStateChanged(int)))

    QLabel* labelGridType = new QLabel(tr("Grid Type"), groupBoxGridGeom)
    labelGridType->setObjectName("labelGridType")
    QComboBox* comboBoxGridType = new QComboBox(groupBoxGridGeom)
    comboBoxGridType->setObjectName("comboBoxGridType")
    comboBoxGridType->addItem("Rectangular")
    comboBoxGridType->addItem("Circular")
    comboBoxGridType->addItem("Isometric")
    strcpy(dialog.grid_type, settings.grid_type)
    comboBoxGridType->setCurrentIndex(comboBoxGridType->findText(dialog.grid_type))
    connect(comboBoxGridType, SIGNAL(currentIndexChanged(const QString&)), this, SLOT(comboBoxGridTypeCurrentIndexChanged(const QString&)))

    QCheckBox* checkBoxGridCenterOnOrigin = new QCheckBox(tr("Center the grid on the origin"), groupBoxGridGeom)
    checkBoxGridCenterOnOrigin->setObjectName("checkBoxGridCenterOnOrigin")
    dialog.grid_center_on_origin = settings.grid_center_on_origin
    checkBoxGridCenterOnOrigin->setChecked(dialog.grid_center_on_origin)
    connect(checkBoxGridCenterOnOrigin, SIGNAL(stateChanged(int)), this, SLOT(checkBoxGridCenterOnOriginStateChanged(int)))

    QLabel* labelGridCenterX = new QLabel(tr("Grid Center X"), groupBoxGridGeom)
    labelGridCenterX->setObjectName("labelGridCenterX")
    QDoubleSpinBox* spinBoxGridCenterX = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridCenterX->setObjectName("spinBoxGridCenterX")
    dialog.grid_center.x = settings.grid_center.x
    spinBoxGridCenterX->setSingleStep(1.000)
    spinBoxGridCenterX->setRange(-1000.000, 1000.000)
    spinBoxGridCenterX->setValue(dialog.grid_center.x)
    connect(spinBoxGridCenterX, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridCenterXValueChanged(double)))

    QLabel* labelGridCenterY = new QLabel(tr("Grid Center Y"), groupBoxGridGeom)
    labelGridCenterY->setObjectName("labelGridCenterY")
    QDoubleSpinBox* spinBoxGridCenterY = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridCenterY->setObjectName("spinBoxGridCenterY")
    dialog.grid_center.y = settings.grid_center.y
    spinBoxGridCenterY->setSingleStep(1.000)
    spinBoxGridCenterY->setRange(-1000.000, 1000.000)
    spinBoxGridCenterY->setValue(dialog.grid_center.y)
    connect(spinBoxGridCenterY, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridCenterYValueChanged(double)))

    QLabel* labelGridSizeX = new QLabel(tr("Grid Size X"), groupBoxGridGeom)
    labelGridSizeX->setObjectName("labelGridSizeX")
    QDoubleSpinBox* spinBoxGridSizeX = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridSizeX->setObjectName("spinBoxGridSizeX")
    dialog.grid_size.x = settings.grid_size.x
    spinBoxGridSizeX->setSingleStep(1.000)
    spinBoxGridSizeX->setRange(1.000, 1000.000)
    spinBoxGridSizeX->setValue(dialog.grid_size.x)
    connect(spinBoxGridSizeX, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSizeXValueChanged(double)))

    QLabel* labelGridSizeY = new QLabel(tr("Grid Size Y"), groupBoxGridGeom)
    labelGridSizeY->setObjectName("labelGridSizeY")
    QDoubleSpinBox* spinBoxGridSizeY = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridSizeY->setObjectName("spinBoxGridSizeY")
    dialog.grid_size.y = settings.grid_size.y
    spinBoxGridSizeY->setSingleStep(1.000)
    spinBoxGridSizeY->setRange(1.000, 1000.000)
    spinBoxGridSizeY->setValue(dialog.grid_size.y)
    connect(spinBoxGridSizeY, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSizeYValueChanged(double)))

    QLabel* labelGridSpacingX = new QLabel(tr("Grid Spacing X"), groupBoxGridGeom)
    labelGridSpacingX->setObjectName("labelGridSpacingX")
    QDoubleSpinBox* spinBoxGridSpacingX = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridSpacingX->setObjectName("spinBoxGridSpacingX")
    dialog.grid_spacing.x = settings.grid_spacing.x
    spinBoxGridSpacingX->setSingleStep(1.000)
    spinBoxGridSpacingX->setRange(0.001, 1000.000)
    spinBoxGridSpacingX->setValue(dialog.grid_spacing.x)
    connect(spinBoxGridSpacingX, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSpacingXValueChanged(double)))

    QLabel* labelGridSpacingY = new QLabel(tr("Grid Spacing Y"), groupBoxGridGeom)
    labelGridSpacingY->setObjectName("labelGridSpacingY")
    QDoubleSpinBox* spinBoxGridSpacingY = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridSpacingY->setObjectName("spinBoxGridSpacingY")
    dialog.grid_spacing.y = settings.grid_spacing.y
    spinBoxGridSpacingY->setSingleStep(1.000)
    spinBoxGridSpacingY->setRange(0.001, 1000.000)
    spinBoxGridSpacingY->setValue(dialog.grid_spacing.y)
    connect(spinBoxGridSpacingY, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSpacingYValueChanged(double)))

    QLabel* labelGridSizeRadius = new QLabel(tr("Grid Size Radius"), groupBoxGridGeom)
    labelGridSizeRadius->setObjectName("labelGridSizeRadius")
    QDoubleSpinBox* spinBoxGridSizeRadius = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridSizeRadius->setObjectName("spinBoxGridSizeRadius")
    dialog.grid_size_radius = settings.grid_size_radius
    spinBoxGridSizeRadius->setSingleStep(1.000)
    spinBoxGridSizeRadius->setRange(1.000, 1000.000)
    spinBoxGridSizeRadius->setValue(dialog.grid_size_radius)
    connect(spinBoxGridSizeRadius, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSizeRadiusValueChanged(double)))

    QLabel* labelGridSpacingRadius = new QLabel(tr("Grid Spacing Radius"), groupBoxGridGeom)
    labelGridSpacingRadius->setObjectName("labelGridSpacingRadius")
    QDoubleSpinBox* spinBoxGridSpacingRadius = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridSpacingRadius->setObjectName("spinBoxGridSpacingRadius")
    dialog.grid_spacing_radius = settings.grid_spacing_radius
    spinBoxGridSpacingRadius->setSingleStep(1.000)
    spinBoxGridSpacingRadius->setRange(0.001, 1000.000)
    spinBoxGridSpacingRadius->setValue(dialog.grid_spacing_radius)
    connect(spinBoxGridSpacingRadius, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSpacingRadiusValueChanged(double)))

    QLabel* labelGridSpacingAngle = new QLabel(tr("Grid Spacing Angle"), groupBoxGridGeom)
    labelGridSpacingAngle->setObjectName("labelGridSpacingAngle")
    QDoubleSpinBox* spinBoxGridSpacingAngle = new QDoubleSpinBox(groupBoxGridGeom)
    spinBoxGridSpacingAngle->setObjectName("spinBoxGridSpacingAngle")
    dialog.grid_spacing_angle = settings.grid_spacing_angle
    spinBoxGridSpacingAngle->setSingleStep(1.000)
    spinBoxGridSpacingAngle->setRange(0.001, 1000.000)
    spinBoxGridSpacingAngle->setValue(dialog.grid_spacing_angle)
    connect(spinBoxGridSpacingAngle, SIGNAL(valueChanged(double)), this, SLOT(spinBoxGridSpacingAngleValueChanged(double)))

    labelGridType->setEnabled(!dialog.grid_load_from_file)
    comboBoxGridType->setEnabled(!dialog.grid_load_from_file)
    checkBoxGridCenterOnOrigin->setEnabled(!dialog.grid_load_from_file)
    labelGridCenterX->setEnabled(!dialog.grid_load_from_file)
    spinBoxGridCenterX->setEnabled(!dialog.grid_load_from_file)
    labelGridCenterY->setEnabled(!dialog.grid_load_from_file)
    spinBoxGridCenterY->setEnabled(!dialog.grid_load_from_file)
    labelGridSizeX->setEnabled(!dialog.grid_load_from_file)
    spinBoxGridSizeX->setEnabled(!dialog.grid_load_from_file)
    labelGridSizeY->setEnabled(!dialog.grid_load_from_file)
    spinBoxGridSizeY->setEnabled(!dialog.grid_load_from_file)
    labelGridSpacingX->setEnabled(!dialog.grid_load_from_file)
    spinBoxGridSpacingX->setEnabled(!dialog.grid_load_from_file)
    labelGridSpacingY->setEnabled(!dialog.grid_load_from_file)
    spinBoxGridSpacingY->setEnabled(!dialog.grid_load_from_file)
    labelGridSizeRadius->setEnabled(!dialog.grid_load_from_file)
    spinBoxGridSizeRadius->setEnabled(!dialog.grid_load_from_file)
    labelGridSpacingRadius->setEnabled(!dialog.grid_load_from_file)
    spinBoxGridSpacingRadius->setEnabled(!dialog.grid_load_from_file)
    labelGridSpacingAngle->setEnabled(!dialog.grid_load_from_file)
    spinBoxGridSpacingAngle->setEnabled(!dialog.grid_load_from_file)

    int visibility = 0
    if(dialog.grid_type == "Circular") visibility = 1
    labelGridSizeX->setVisible(!visibility)
    spinBoxGridSizeX->setVisible(!visibility)
    labelGridSizeY->setVisible(!visibility)
    spinBoxGridSizeY->setVisible(!visibility)
    labelGridSpacingX->setVisible(!visibility)
    spinBoxGridSpacingX->setVisible(!visibility)
    labelGridSpacingY->setVisible(!visibility)
    spinBoxGridSpacingY->setVisible(!visibility)
    labelGridSizeRadius->setVisible(visibility)
    spinBoxGridSizeRadius->setVisible(visibility)
    labelGridSpacingRadius->setVisible(visibility)
    spinBoxGridSpacingRadius->setVisible(visibility)
    labelGridSpacingAngle->setVisible(visibility)
    spinBoxGridSpacingAngle->setVisible(visibility)

    QGridLayout* gridLayoutGridGeom = new QGridLayout(groupBoxGridGeom)
    gridLayoutGridGeom->addWidget(checkBoxGridLoadFromFile, 0, 0, Qt::AlignLeft)
    gridLayoutGridGeom->addWidget(labelGridType, 1, 0, Qt::AlignLeft)
    gridLayoutGridGeom->addWidget(comboBoxGridType, 1, 1, Qt::AlignRight)
    gridLayoutGridGeom->addWidget(checkBoxGridCenterOnOrigin, 2, 0, Qt::AlignLeft)
    gridLayoutGridGeom->addWidget(labelGridCenterX, 3, 0, Qt::AlignLeft)
    gridLayoutGridGeom->addWidget(spinBoxGridCenterX, 3, 1, Qt::AlignRight)
    gridLayoutGridGeom->addWidget(labelGridCenterY, 4, 0, Qt::AlignLeft)
    gridLayoutGridGeom->addWidget(spinBoxGridCenterY, 4, 1, Qt::AlignRight)
    gridLayoutGridGeom->addWidget(labelGridSizeX, 5, 0, Qt::AlignLeft)
    gridLayoutGridGeom->addWidget(spinBoxGridSizeX, 5, 1, Qt::AlignRight)
    gridLayoutGridGeom->addWidget(labelGridSizeY, 6, 0, Qt::AlignLeft)
    gridLayoutGridGeom->addWidget(spinBoxGridSizeY, 6, 1, Qt::AlignRight)
    gridLayoutGridGeom->addWidget(labelGridSpacingX, 7, 0, Qt::AlignLeft)
    gridLayoutGridGeom->addWidget(spinBoxGridSpacingX, 7, 1, Qt::AlignRight)
    gridLayoutGridGeom->addWidget(labelGridSpacingY, 8, 0, Qt::AlignLeft)
    gridLayoutGridGeom->addWidget(spinBoxGridSpacingY, 8, 1, Qt::AlignRight)
    gridLayoutGridGeom->addWidget(labelGridSizeRadius, 9, 0, Qt::AlignLeft)
    gridLayoutGridGeom->addWidget(spinBoxGridSizeRadius, 9, 1, Qt::AlignRight)
    gridLayoutGridGeom->addWidget(labelGridSpacingRadius, 10, 0, Qt::AlignLeft)
    gridLayoutGridGeom->addWidget(spinBoxGridSpacingRadius, 10, 1, Qt::AlignRight)
    gridLayoutGridGeom->addWidget(labelGridSpacingAngle, 11, 0, Qt::AlignLeft)
    gridLayoutGridGeom->addWidget(spinBoxGridSpacingAngle, 11, 1, Qt::AlignRight)
    groupBoxGridGeom->setLayout(gridLayoutGridGeom)

    /*Ruler Misc*/
    QGroupBox* groupBoxRulerMisc = new QGroupBox(tr("Ruler Misc"), widget)

    QCheckBox* checkBoxRulerShowOnLoad = new QCheckBox(tr("Initially show ruler when loading a file"), groupBoxRulerMisc)
    dialog.ruler_show_on_load = settings.ruler_show_on_load
    checkBoxRulerShowOnLoad->setChecked(dialog.ruler_show_on_load)
    connect(checkBoxRulerShowOnLoad, SIGNAL(stateChanged(int)), this, SLOT(checkBoxRulerShowOnLoadStateChanged(int)))

    QLabel* labelRulerMetric = new QLabel(tr("Ruler Units"), groupBoxRulerMisc)
    QComboBox* comboBoxRulerMetric = new QComboBox(groupBoxRulerMisc)
    comboBoxRulerMetric->addItem("Imperial", 0)
    comboBoxRulerMetric->addItem("Metric", 1)
    dialog.ruler_metric = settings.ruler_metric
    comboBoxRulerMetric->setCurrentIndex(comboBoxRulerMetric->findData(dialog.ruler_metric))
    connect(comboBoxRulerMetric, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxRulerMetricCurrentIndexChanged(int)))

    QGridLayout* gridLayoutRulerMisc = new QGridLayout(widget)
    gridLayoutRulerMisc->addWidget(checkBoxRulerShowOnLoad, 0, 0, Qt::AlignLeft)
    gridLayoutRulerMisc->addWidget(labelRulerMetric, 1, 0, Qt::AlignLeft)
    gridLayoutRulerMisc->addWidget(comboBoxRulerMetric, 1, 1, Qt::AlignRight)
    groupBoxRulerMisc->setLayout(gridLayoutRulerMisc)

    /*Ruler Color*/
    QGroupBox* groupBoxRulerColor = new QGroupBox(tr("Ruler Color"), widget)

    QLabel* labelRulerColor = new QLabel(tr("Ruler Color"), groupBoxRulerColor)
    labelRulerColor->setObjectName("labelRulerColor")
    QPushButton* buttonRulerColor = new QPushButton(tr("Choose"), groupBoxRulerColor)
    buttonRulerColor->setObjectName("buttonRulerColor")
    dialog.ruler_color = settings.ruler_color
    preview.ruler_color = dialog.ruler_color
    accept_.ruler_color = dialog.ruler_color
    QPixmap rulerPix(16,16)
    rulerPix.fill(QColor(preview.ruler_color))
    buttonRulerColor->setIcon(QIcon(rulerPix))
    connect(buttonRulerColor, SIGNAL(clicked()), this, SLOT(chooseRulerColor()))

    QGridLayout* gridLayoutRulerColor = new QGridLayout(widget)
    gridLayoutRulerColor->addWidget(labelRulerColor, 1, 0, Qt::AlignLeft)
    gridLayoutRulerColor->addWidget(buttonRulerColor, 1, 1, Qt::AlignRight)
    groupBoxRulerColor->setLayout(gridLayoutRulerColor)

    /*Ruler Geometry*/
    QGroupBox* groupBoxRulerGeom = new QGroupBox(tr("Ruler Geometry"), widget)

    QLabel* labelRulerPixelSize = new QLabel(tr("Ruler Pixel Size"), groupBoxRulerGeom)
    labelRulerPixelSize->setObjectName("labelRulerPixelSize")
    QDoubleSpinBox* spinBoxRulerPixelSize = new QDoubleSpinBox(groupBoxRulerGeom)
    spinBoxRulerPixelSize->setObjectName("spinBoxRulerPixelSize")
    dialog.ruler_pixel_size = settings.ruler_pixel_size
    spinBoxRulerPixelSize->setSingleStep(1.000)
    spinBoxRulerPixelSize->setRange(20.000, 100.000)
    spinBoxRulerPixelSize->setValue(dialog.ruler_pixel_size)
    connect(spinBoxRulerPixelSize, SIGNAL(valueChanged(double)), this, SLOT(spinBoxRulerPixelSizeValueChanged(double)))

    QGridLayout* gridLayoutRulerGeom = new QGridLayout(groupBoxRulerGeom)
    gridLayoutRulerGeom->addWidget(labelRulerPixelSize, 0, 0, Qt::AlignLeft)
    gridLayoutRulerGeom->addWidget(spinBoxRulerPixelSize, 0, 1, Qt::AlignRight)
    groupBoxRulerGeom->setLayout(gridLayoutRulerGeom)

    /*Widget Layout*/
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget)
    vboxLayoutMain->addWidget(groupBoxGridMisc)
    vboxLayoutMain->addWidget(groupBoxGridColor)
    vboxLayoutMain->addWidget(groupBoxGridGeom)
    vboxLayoutMain->addWidget(groupBoxRulerMisc)
    vboxLayoutMain->addWidget(groupBoxRulerColor)
    vboxLayoutMain->addWidget(groupBoxRulerGeom)
    vboxLayoutMain->addStretch(1)
    widget->setLayout(vboxLayoutMain)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea->setWidgetResizable(1)
    scrollArea->setWidget(widget)
    return scrollArea

QWidget* Settings_Dialog::createTabOrthoPolar():
    QWidget* widget = new QWidget(this)

    /*TODO: finish this*/

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea->setWidgetResizable(1)
    scrollArea->setWidget(widget)
    return scrollArea

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

QWidget* Settings_Dialog::createTabQuickSnap():
    QWidget* widget = new QWidget(this)

    /*QSnap Locators*/
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

    gridLayoutQSnap->addWidget(buttonQSnapSelectAll, 0, 2, Qt::AlignLeft)
    gridLayoutQSnap->addWidget(buttonQSnapClearAll, 1, 2, Qt::AlignLeft)
    gridLayoutQSnap->setColumnStretch(2,1)
    groupBoxQSnapLoc->setLayout(gridLayoutQSnap)

    /*QSnap Visual Config*/
    QGroupBox* groupBoxQSnapVisual = new QGroupBox(tr("Visual Configuration"), widget)

    QLabel* labelQSnapLocColor = new QLabel(tr("Locator Color"), groupBoxQSnapVisual)
    QComboBox* comboBoxQSnapLocColor = new QComboBox(groupBoxQSnapVisual)
    addColorsToComboBox(comboBoxQSnapLocColor)
    dialog.qsnap_locator_color = settings.qsnap_locator_color
    comboBoxQSnapLocColor->setCurrentIndex(comboBoxQSnapLocColor->findData(dialog.qsnap_locator_color))
    connect(comboBoxQSnapLocColor, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxQSnapLocatorColorCurrentIndexChanged(int)))

    QLabel* labelQSnapLocSize = new QLabel(tr("Locator Size"), groupBoxQSnapVisual)
    QSlider* sliderQSnapLocSize = new QSlider(Qt::Horizontal, groupBoxQSnapVisual)
    sliderQSnapLocSize->setRange(1,20)
    dialog.qsnap_locator_size = settings.qsnap_locator_size
    sliderQSnapLocSize->setValue(dialog.qsnap_locator_size)
    connect(sliderQSnapLocSize, SIGNAL(valueChanged(int)), this, SLOT(sliderQSnapLocatorSizeValueChanged(int)))

    QVBoxLayout* vboxLayoutQSnapVisual = new QVBoxLayout(groupBoxQSnapVisual)
    vboxLayoutQSnapVisual->addWidget(labelQSnapLocColor)
    vboxLayoutQSnapVisual->addWidget(comboBoxQSnapLocColor)
    vboxLayoutQSnapVisual->addWidget(labelQSnapLocSize)
    vboxLayoutQSnapVisual->addWidget(sliderQSnapLocSize)
    groupBoxQSnapVisual->setLayout(vboxLayoutQSnapVisual)

    /*QSnap Sensitivity Config*/
    QGroupBox* groupBoxQSnapSensitivity = new QGroupBox(tr("Sensitivity"), widget)

    QLabel* labelQSnapApertureSize = new QLabel(tr("Aperture Size"), groupBoxQSnapSensitivity)
    QSlider* sliderQSnapApertureSize = new QSlider(Qt::Horizontal, groupBoxQSnapSensitivity)
    sliderQSnapApertureSize->setRange(1,20)
    dialog.qsnap_aperture_size = settings.qsnap_aperture_size
    sliderQSnapApertureSize->setValue(dialog.qsnap_aperture_size)
    connect(sliderQSnapApertureSize, SIGNAL(valueChanged(int)), this, SLOT(sliderQSnapApertureSizeValueChanged(int)))

    QVBoxLayout* vboxLayoutQSnapSensitivity = new QVBoxLayout(groupBoxQSnapSensitivity)
    vboxLayoutQSnapSensitivity->addWidget(labelQSnapApertureSize)
    vboxLayoutQSnapSensitivity->addWidget(sliderQSnapApertureSize)
    groupBoxQSnapSensitivity->setLayout(vboxLayoutQSnapSensitivity)

    /*Widget Layout*/
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget)
    vboxLayoutMain->addWidget(groupBoxQSnapLoc)
    vboxLayoutMain->addWidget(groupBoxQSnapVisual)
    vboxLayoutMain->addWidget(groupBoxQSnapSensitivity)
    vboxLayoutMain->addStretch(1)
    widget->setLayout(vboxLayoutMain)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea->setWidgetResizable(1)
    scrollArea->setWidget(widget)
    return scrollArea

#undef make_check_box

QWidget* Settings_Dialog::createTabQuickTrack():
    QWidget* widget = new QWidget(this)

    /* TODO: finish this */

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea->setWidgetResizable(1)
    scrollArea->setWidget(widget)
    return scrollArea

QWidget* Settings_Dialog::createTabLineWeight():
    QWidget* widget = new QWidget(this)

    /* TODO: finish this */

    /* Misc */
    QGroupBox* groupBoxLwtMisc = new QGroupBox(tr("LineWeight Misc"), widget)

    QGraphicsScene* s = mainWin->activeScene()

    QCheckBox* checkBoxShowLwt = new QCheckBox(tr("Show LineWeight"), groupBoxLwtMisc)
    if (s) {
        dialog.lwt_show_lwt = s->property("ENABLE_LWT").toBool()
    }
    else {
        dialog.lwt_show_lwt = settings.lwt_show_lwt
    }
    preview.lwt_show_lwt = dialog.lwt_show_lwt
    checkBoxShowLwt->setChecked(preview.lwt_show_lwt)
    connect(checkBoxShowLwt, SIGNAL(stateChanged(int)), this, SLOT(checkBoxLwtShowLwtStateChanged(int)))

    QCheckBox* checkBoxRealRender = new QCheckBox(tr("RealRender"), groupBoxLwtMisc)
    checkBoxRealRender->setObjectName("checkBoxRealRender")
    if (s) {
        dialog.lwt_real_render = s->property("ENABLE_REAL").toBool()
    }
    else {
        dialog.lwt_real_render = settings.lwt_real_render
    }
    preview.lwt_real_render = dialog.lwt_real_render
    checkBoxRealRender->setChecked(preview.lwt_real_render)
    connect(checkBoxRealRender, SIGNAL(stateChanged(int)), this, SLOT(checkBoxLwtRealRenderStateChanged(int)))
    checkBoxRealRender->setEnabled(dialog.lwt_show_lwt)

    QLabel* labelDefaultLwt = new QLabel(tr("Default weight"), groupBoxLwtMisc)
    labelDefaultLwt->setEnabled(0); /* TODO: remove later */
    QComboBox* comboBoxDefaultLwt = new QComboBox(groupBoxLwtMisc)
    dialog.lwt_default_lwt = settings.lwt_default_lwt
    /* TODO: populate the comboBox and set the initial value */
    comboBoxDefaultLwt->addItem(QString().setNum(dialog.lwt_default_lwt, 'F', 2).append(" mm"), dialog.lwt_default_lwt)
    comboBoxDefaultLwt->setEnabled(0); /* TODO: remove later */

    QVBoxLayout* vboxLayoutLwtMisc = new QVBoxLayout(groupBoxLwtMisc)
    vboxLayoutLwtMisc->addWidget(checkBoxShowLwt)
    vboxLayoutLwtMisc->addWidget(checkBoxRealRender)
    vboxLayoutLwtMisc->addWidget(labelDefaultLwt)
    vboxLayoutLwtMisc->addWidget(comboBoxDefaultLwt)
    groupBoxLwtMisc->setLayout(vboxLayoutLwtMisc)

    /*Widget Layout*/
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget)
    vboxLayoutMain->addWidget(groupBoxLwtMisc)
    vboxLayoutMain->addStretch(1)
    widget->setLayout(vboxLayoutMain)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea->setWidgetResizable(1)
    scrollArea->setWidget(widget)
    return scrollArea

QWidget* Settings_Dialog::createTabSelection():
    QWidget* widget = new QWidget(this)

    /* Selection Modes */
    QGroupBox* groupBoxSelectionModes = new QGroupBox(tr("Modes"), widget)

    QCheckBox* checkBoxSelectionModePickFirst = new QCheckBox(tr("Allow Preselection (PickFirst)"), groupBoxSelectionModes)
    dialog.selection_mode_pickfirst = settings.selection_mode_pickfirst
    checkBoxSelectionModePickFirst->setChecked(dialog.selection_mode_pickfirst)
    checkBoxSelectionModePickFirst->setChecked(1); checkBoxSelectionModePickFirst->setEnabled(0); /* TODO: Remove this line when Post-selection is available */
    connect(checkBoxSelectionModePickFirst, SIGNAL(stateChanged(int)), this, SLOT(checkBoxSelectionModePickFirstStateChanged(int)))

    QCheckBox* checkBoxSelectionModePickAdd = new QCheckBox(tr("Add to Selection (PickAdd)"), groupBoxSelectionModes)
    dialog.selection_mode_pickadd = settings.selection_mode_pickadd
    checkBoxSelectionModePickAdd->setChecked(dialog.selection_mode_pickadd)
    connect(checkBoxSelectionModePickAdd, SIGNAL(stateChanged(int)), this, SLOT(checkBoxSelectionModePickAddStateChanged(int)))

    QCheckBox* checkBoxSelectionModePickDrag = new QCheckBox(tr("Drag to Select (PickDrag)"), groupBoxSelectionModes)
    dialog.selection_mode_pickdrag = settings.selection_mode_pickdrag
    checkBoxSelectionModePickDrag->setChecked(dialog.selection_mode_pickdrag)
    checkBoxSelectionModePickDrag->setChecked(0); checkBoxSelectionModePickDrag->setEnabled(0); /*TODO: Remove this line when this functionality is available*/
    connect(checkBoxSelectionModePickDrag, SIGNAL(stateChanged(int)), this, SLOT(checkBoxSelectionModePickDragStateChanged(int)))

    QVBoxLayout* vboxLayoutSelectionModes = new QVBoxLayout(groupBoxSelectionModes)
    vboxLayoutSelectionModes->addWidget(checkBoxSelectionModePickFirst)
    vboxLayoutSelectionModes->addWidget(checkBoxSelectionModePickAdd)
    vboxLayoutSelectionModes->addWidget(checkBoxSelectionModePickDrag)
    groupBoxSelectionModes->setLayout(vboxLayoutSelectionModes)

    /*Selection Colors*/
    QGroupBox* groupBoxSelectionColors = new QGroupBox(tr("Colors"), widget)

    QLabel* labelCoolGripColor = new QLabel(tr("Cool Grip (Unselected)"), groupBoxSelectionColors)
    QComboBox* comboBoxCoolGripColor = new QComboBox(groupBoxSelectionColors)
    addColorsToComboBox(comboBoxCoolGripColor)
    dialog.selection_coolgrip_color = settings.selection_coolgrip_color
    comboBoxCoolGripColor->setCurrentIndex(comboBoxCoolGripColor->findData(dialog.selection_coolgrip_color))
    connect(comboBoxCoolGripColor, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxSelectionCoolGripColorCurrentIndexChanged(int)))

    QLabel* labelHotGripColor = new QLabel(tr("Hot Grip (Selected)"), groupBoxSelectionColors)
    QComboBox* comboBoxHotGripColor = new QComboBox(groupBoxSelectionColors)
    addColorsToComboBox(comboBoxHotGripColor)
    dialog.selection_hotgrip_color = settings.selection_hotgrip_color
    comboBoxHotGripColor->setCurrentIndex(comboBoxHotGripColor->findData(dialog.selection_hotgrip_color))
    connect(comboBoxHotGripColor, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxSelectionHotGripColorCurrentIndexChanged(int)))

    QVBoxLayout* vboxLayoutSelectionColors = new QVBoxLayout(groupBoxSelectionColors)
    vboxLayoutSelectionColors->addWidget(labelCoolGripColor)
    vboxLayoutSelectionColors->addWidget(comboBoxCoolGripColor)
    vboxLayoutSelectionColors->addWidget(labelHotGripColor)
    vboxLayoutSelectionColors->addWidget(comboBoxHotGripColor)
    groupBoxSelectionColors->setLayout(vboxLayoutSelectionColors)

    /*Selection Sizes*/
    QGroupBox* groupBoxSelectionSizes = new QGroupBox(tr("Sizes"), widget)

    QLabel* labelSelectionGripSize = new QLabel(tr("Grip Size"), groupBoxSelectionSizes)
    QSlider* sliderSelectionGripSize = new QSlider(Qt::Horizontal, groupBoxSelectionSizes)
    sliderSelectionGripSize->setRange(1,20)
    dialog.selection_grip_size = settings.selection_grip_size
    sliderSelectionGripSize->setValue(dialog.selection_grip_size)
    connect(sliderSelectionGripSize, SIGNAL(valueChanged(int)), this, SLOT(sliderSelectionGripSizeValueChanged(int)))

    QLabel* labelSelectionPickBoxSize = new QLabel(tr("Pickbox Size"), groupBoxSelectionSizes)
    QSlider* sliderSelectionPickBoxSize = new QSlider(Qt::Horizontal, groupBoxSelectionSizes)
    sliderSelectionPickBoxSize->setRange(1,20)
    dialog.selection_pickbox_size = settings.selection_pickbox_size
    sliderSelectionPickBoxSize->setValue(dialog.selection_pickbox_size)
    connect(sliderSelectionPickBoxSize, SIGNAL(valueChanged(int)), this, SLOT(sliderSelectionPickBoxSizeValueChanged(int)))

    QVBoxLayout* vboxLayoutSelectionSizes = new QVBoxLayout(groupBoxSelectionSizes)
    vboxLayoutSelectionSizes->addWidget(labelSelectionGripSize)
    vboxLayoutSelectionSizes->addWidget(sliderSelectionGripSize)
    vboxLayoutSelectionSizes->addWidget(labelSelectionPickBoxSize)
    vboxLayoutSelectionSizes->addWidget(sliderSelectionPickBoxSize)
    groupBoxSelectionSizes->setLayout(vboxLayoutSelectionSizes)

    /*Widget Layout*/
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget)
    vboxLayoutMain->addWidget(groupBoxSelectionModes)
    vboxLayoutMain->addWidget(groupBoxSelectionColors)
    vboxLayoutMain->addWidget(groupBoxSelectionSizes)
    vboxLayoutMain->addStretch(1)
    widget->setLayout(vboxLayoutMain)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea->setWidgetResizable(1)
    scrollArea->setWidget(widget)
    return scrollArea

def Settings_Dialog::addColorsToComboBox(QComboBox* comboBox):
    comboBox->addItem(loadIcon(colorred_xpm), tr("Red"), qRgb(255, 0, 0))
    comboBox->addItem(loadIcon(coloryellow_xpm), tr("Yellow"), qRgb(255,255, 0))
    comboBox->addItem(loadIcon(colorgreen_xpm), tr("Green"), qRgb(  0,255, 0))
    comboBox->addItem(loadIcon(colorcyan_xpm), tr("Cyan"), qRgb(  0,255,255))
    comboBox->addItem(loadIcon(colorblue_xpm), tr("Blue"), qRgb(  0, 0,255))
    comboBox->addItem(loadIcon(colormagenta_xpm), tr("Magenta"), qRgb(255, 0,255))
    comboBox->addItem(loadIcon(colorwhite_xpm), tr("White"), qRgb(255,255,255))
    /* TODO: Add Other... so the user can select custom colors */
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
        dialog.general_icon_size = comboBox->itemData(index).toUInt(&ok)
        if(!ok)
            dialog.general_icon_size = 16
    }
    else
        dialog.general_icon_size = 16

def Settings_Dialog::checkBoxGeneralMdiBGUseLogoStateChanged(int checked):
    preview.general_mdi_bg_use_logo = checked
    mainWin->mdiArea->useBackgroundLogo(checked)

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

        /*Update immediately so it can be previewed*/
        mainWin->mdiArea->setBackgroundLogo(accept_.general_mdi_bg_logo)
    }
}

def Settings_Dialog::checkBoxGeneralMdiBGUseTextureStateChanged(int checked):
    preview.general_mdi_bg_use_texture = checked
    mainWin->mdiArea->useBackgroundTexture(checked)

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

        /*Update immediately so it can be previewed*/
        mainWin->mdiArea->setBackgroundTexture(accept_.general_mdi_bg_texture)
    }
}

def Settings_Dialog::checkBoxGeneralMdiBGUseColorStateChanged(int checked):
    preview.general_mdi_bg_use_color = checked
    mainWin->mdiArea->useBackgroundColor(checked)

def Settings_Dialog::chooseGeneralMdiBackgroundColor():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.general_mdi_bg_color), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentGeneralMdiBackgroundColorChanged(const QColor&)))
        colorDialog->exec()

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.general_mdi_bg_color = colorDialog->selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.general_mdi_bg_color))
            button->setIcon(QIcon(pix))
            mainWin->mdiArea->setBackgroundColor(QColor(accept_.general_mdi_bg_color))
        }
        else {
            mainWin->mdiArea->setBackgroundColor(QColor(dialog.general_mdi_bg_color))
        }
    }
}

def Settings_Dialog::currentGeneralMdiBackgroundColorChanged(const QColor& color):
    preview.general_mdi_bg_color = color.rgb()
    mainWin->mdiArea->setBackgroundColor(QColor(preview.general_mdi_bg_color))


/*
check_func(checkBoxTipOfTheDayStateChanged, general_tip_of_the_day)
check_func(checkBoxUseOpenGLStateChanged, display_use_opengl)
check_func(checkBoxRenderHintAAStateChanged, display_renderhint_aa)
check_func(checkBoxRenderHintTextAAStateChanged, display_renderhint_text_aa)
check_func(checkBoxRenderHintSmoothPixStateChanged, display_renderhint_smooth_pix)
check_func(checkBoxRenderHintHighAAStateChanged, display_renderhint_high_aa)
check_func(checkBoxRenderHintNonCosmeticStateChanged, display_renderhint_noncosmetic)
*/

def Settings_Dialog::checkBoxShowScrollBarsStateChanged(int checked):
    preview.display_show_scrollbars = checked
    mainWin->updateAllViewScrollBars(preview.display_show_scrollbars)

def Settings_Dialog::spinBoxZoomScaleInValueChanged(double value):
    dialog.display_zoomscale_in = value

def Settings_Dialog::spinBoxZoomScaleOutValueChanged(double value):
    dialog.display_zoomscale_out = value

def Settings_Dialog::checkBoxDisableBGStateChanged(int checked):
    dialog.printing_disable_bg = checked

def Settings_Dialog::chooseDisplayCrossHairColor():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_crosshair_color), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplayCrossHairColorChanged(const QColor&)))
        colorDialog->exec()

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.display_crosshair_color = colorDialog->selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.display_crosshair_color))
            button->setIcon(QIcon(pix))
            mainWin->updateAllViewCrossHairColors(accept_.display_crosshair_color)
        }
        else {
            mainWin->updateAllViewCrossHairColors(dialog.display_crosshair_color)
        }
    }
}

def Settings_Dialog::currentDisplayCrossHairColorChanged(const QColor& color):
    preview.display_crosshair_color = color.rgb()
    mainWin->updateAllViewCrossHairColors(preview.display_crosshair_color)

def Settings_Dialog::chooseDisplayBackgroundColor():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_bg_color), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplayBackgroundColorChanged(const QColor&)))
        colorDialog->exec()

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.display_bg_color = colorDialog->selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.display_bg_color))
            button->setIcon(QIcon(pix))
            mainWin->updateAllViewBackgroundColors(accept_.display_bg_color)
        }
        else {
            mainWin->updateAllViewBackgroundColors(dialog.display_bg_color)
        }
    }
}

def Settings_Dialog::currentDisplayBackgroundColorChanged(const QColor& color):
    preview.display_bg_color = color.rgb()
    mainWin->updateAllViewBackgroundColors(preview.display_bg_color)

def Settings_Dialog::chooseDisplaySelectBoxLeftColor():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if(button)
    {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_selectbox_left_color), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplaySelectBoxLeftColorChanged(const QColor&)))
        colorDialog->exec()

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.display_selectbox_left_color = colorDialog->selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.display_selectbox_left_color))
            button->setIcon(QIcon(pix))
            mainWin->updateAllViewSelectBoxColors(accept_.display_selectbox_left_color,
                accept_.display_selectbox_left_fill,
                accept_.display_selectbox_right_color,
                accept_.display_selectbox_right_fill,
                preview.display_selectbox_alpha)
        }
        else
        {
            mainWin->updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                dialog.display_selectbox_left_fill,
                dialog.display_selectbox_right_color,
                dialog.display_selectbox_right_fill,
                                                  preview.display_selectbox_alpha)
        }
    }
}

def Settings_Dialog::currentDisplaySelectBoxLeftColorChanged(const QColor& color):
    preview.display_selectbox_left_color = color.rgb()
    mainWin->updateAllViewSelectBoxColors(preview.display_selectbox_left_color,
                                          preview.display_selectbox_left_fill,
                                          preview.display_selectbox_right_color,
                                          preview.display_selectbox_right_fill,
                                          preview.display_selectbox_alpha)

def Settings_Dialog::chooseDisplaySelectBoxLeftFill():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_selectbox_left_fill), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplaySelectBoxLeftFillChanged(const QColor&)))
        colorDialog->exec()

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.display_selectbox_left_fill = colorDialog->selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.display_selectbox_left_fill))
            button->setIcon(QIcon(pix))
            mainWin->updateAllViewSelectBoxColors(
                accept_.display_selectbox_left_color,
                accept_.display_selectbox_left_fill,
                accept_.display_selectbox_right_color,
                accept_.display_selectbox_right_fill,
                preview.display_selectbox_alpha)
        }
        else {
            mainWin->updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                                                  dialog.display_selectbox_left_fill,
                                                  dialog.display_selectbox_right_color,
                                                  dialog.display_selectbox_right_fill,
                                                  preview.display_selectbox_alpha)
        }
    }
}

def Settings_Dialog::currentDisplaySelectBoxLeftFillChanged(const QColor& color):
    preview.display_selectbox_left_fill = color.rgb()
    mainWin->updateAllViewSelectBoxColors(preview.display_selectbox_left_color,
        preview.display_selectbox_left_fill,
        preview.display_selectbox_right_color,
        preview.display_selectbox_right_fill,
        preview.display_selectbox_alpha)

def Settings_Dialog::chooseDisplaySelectBoxRightColor():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_selectbox_right_color), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplaySelectBoxRightColorChanged(const QColor&)))
        colorDialog->exec()

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.display_selectbox_right_color = colorDialog->selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.display_selectbox_right_color))
            button->setIcon(QIcon(pix))
            mainWin->updateAllViewSelectBoxColors(accept_.display_selectbox_left_color,
                                                  accept_.display_selectbox_left_fill,
                                                  accept_.display_selectbox_right_color,
                                                  accept_.display_selectbox_right_fill,
                                                  preview.display_selectbox_alpha)
        }
        else {
            mainWin->updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                                                  dialog.display_selectbox_left_fill,
                                                  dialog.display_selectbox_right_color,
                                                  dialog.display_selectbox_right_fill,
                                                  preview.display_selectbox_alpha)
        }
    }
}

def Settings_Dialog::currentDisplaySelectBoxRightColorChanged(const QColor& color):
    preview.display_selectbox_right_color = color.rgb()
    mainWin->updateAllViewSelectBoxColors(preview.display_selectbox_left_color,
        preview.display_selectbox_left_fill,
        preview.display_selectbox_right_color,
        preview.display_selectbox_right_fill,
        preview.display_selectbox_alpha)

def Settings_Dialog::chooseDisplaySelectBoxRightFill():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.display_selectbox_right_fill), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentDisplaySelectBoxRightFillChanged(const QColor&)))
        colorDialog->exec()

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.display_selectbox_right_fill = colorDialog->selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.display_selectbox_right_fill))
            button->setIcon(QIcon(pix))
            mainWin->updateAllViewSelectBoxColors(accept_.display_selectbox_left_color,
                 accept_.display_selectbox_left_fill,
                 accept_.display_selectbox_right_color,
                 accept_.display_selectbox_right_fill,
                 preview.display_selectbox_alpha)
        }
        else {
            mainWin->updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                                                  dialog.display_selectbox_left_fill,
                                                  dialog.display_selectbox_right_color,
                                                  dialog.display_selectbox_right_fill,
                                                  preview.display_selectbox_alpha)
        }
    }
}

def Settings_Dialog::currentDisplaySelectBoxRightFillChanged(const QColor& color):
    preview.display_selectbox_right_fill = color.rgb()
    mainWin->updateAllViewSelectBoxColors(preview.display_selectbox_left_color,
        preview.display_selectbox_left_fill,
        preview.display_selectbox_right_color,
        preview.display_selectbox_right_fill,
        preview.display_selectbox_alpha)

def Settings_Dialog::spinBoxDisplaySelectBoxAlphaValueChanged(int value):
    preview.display_selectbox_alpha = value
    mainWin->updateAllViewSelectBoxColors(accept_.display_selectbox_left_color,
        accept_.display_selectbox_left_fill,
        accept_.display_selectbox_right_color,
        accept_.display_selectbox_right_fill,
        preview.display_selectbox_alpha)

def Settings_Dialog::checkBoxCustomFilterStateChanged(int checked):
    QCheckBox* checkBox = qobject_cast<QCheckBox*>(sender())
    if(checkBox)
    {
        QString format = checkBox->text()
        debug_message("CustomFilter: %s %d", qPrintable(format), checked)
        if(checked)
            opensave_custom_filter.append(" *." + format.toLower())
        else
            opensave_custom_filter.remove("*." + format, Qt::CaseInsensitive)
        /*dialog.opensave_custom_filter = checked; //TODO*/
    }
}

def Settings_Dialog::buttonCustomFilterSelectAllClicked():
    emit buttonCustomFilterSelectAll(1)
    opensave_custom_filter = "supported"

def Settings_Dialog::buttonCustomFilterClearAllClicked():
    emit buttonCustomFilterClearAll(0)
    opensave_custom_filter.clear()

def Settings_Dialog::checkBoxGridColorMatchCrossHairStateChanged(int checked):
    dialog.grid_color_match_crosshair = checked
    if (dialog.grid_color_match_crosshair) {
        mainWin->updateAllViewGridColors(accept_.display_crosshair_color)
    }
    else {
        mainWin->updateAllViewGridColors(accept_.grid_color)
    }

    QObject* senderObj = sender()
    if (senderObj) {
        QObject* parent = senderObj->parent()
        if (parent) {
            QLabel* labelGridColor = parent->findChild<QLabel*>("labelGridColor")
            if (labelGridColor)
                labelGridColor->setEnabled(!dialog.grid_color_match_crosshair)
            QPushButton* buttonGridColor = parent->findChild<QPushButton*>("buttonGridColor")
            if (buttonGridColor)
                buttonGridColor->setEnabled(!dialog.grid_color_match_crosshair)
        }
    }
}

def Settings_Dialog::chooseGridColor():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.grid_color), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentGridColorChanged(const QColor&)))
        colorDialog->exec()

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.grid_color = colorDialog->selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.grid_color))
            button->setIcon(QIcon(pix))
            mainWin->updateAllViewGridColors(accept_.grid_color)
        }
        else {
            mainWin->updateAllViewGridColors(dialog.grid_color)
        }
    }
}

def Settings_Dialog::currentGridColorChanged(const QColor& color):
    preview.grid_color = color.rgb()
    mainWin->updateAllViewGridColors(preview.grid_color)

def Settings_Dialog::checkBoxGridLoadFromFileStateChanged(int checked):
    dialog.grid_load_from_file = checked

    QObject* senderObj = sender()
    if (senderObj) {
        QObject* parent = senderObj->parent()
        if (parent) {
            QLabel* labelGridType = parent->findChild<QLabel*>("labelGridType")
            if(labelGridType) labelGridType->setEnabled(!dialog.grid_load_from_file)
            QComboBox* comboBoxGridType = parent->findChild<QComboBox*>("comboBoxGridType")
            if(comboBoxGridType) comboBoxGridType->setEnabled(!dialog.grid_load_from_file)
            QCheckBox* checkBoxGridCenterOnOrigin = parent->findChild<QCheckBox*>("checkBoxGridCenterOnOrigin")
            if(checkBoxGridCenterOnOrigin) checkBoxGridCenterOnOrigin->setEnabled(!dialog.grid_load_from_file)
            QLabel* labelGridCenterX = parent->findChild<QLabel*>("labelGridCenterX")
            if(labelGridCenterX) labelGridCenterX->setEnabled(!dialog.grid_load_from_file && !dialog.grid_center_on_origin)
            QDoubleSpinBox* spinBoxGridCenterX = parent->findChild<QDoubleSpinBox*>("spinBoxGridCenterX")
            if(spinBoxGridCenterX) spinBoxGridCenterX->setEnabled(!dialog.grid_load_from_file && !dialog.grid_center_on_origin)
            QLabel* labelGridCenterY = parent->findChild<QLabel*>("labelGridCenterY")
            if(labelGridCenterY) labelGridCenterY->setEnabled(!dialog.grid_load_from_file && !dialog.grid_center_on_origin)
            QDoubleSpinBox* spinBoxGridCenterY = parent->findChild<QDoubleSpinBox*>("spinBoxGridCenterY")
            if(spinBoxGridCenterY) spinBoxGridCenterY->setEnabled(!dialog.grid_load_from_file && !dialog.grid_center_on_origin)
            QLabel* labelGridSizeX = parent->findChild<QLabel*>("labelGridSizeX")
            if(labelGridSizeX) labelGridSizeX->setEnabled(!dialog.grid_load_from_file)
            QDoubleSpinBox* spinBoxGridSizeX = parent->findChild<QDoubleSpinBox*>("spinBoxGridSizeX")
            if(spinBoxGridSizeX) spinBoxGridSizeX->setEnabled(!dialog.grid_load_from_file)
            QLabel* labelGridSizeY = parent->findChild<QLabel*>("labelGridSizeY")
            if(labelGridSizeY) labelGridSizeY->setEnabled(!dialog.grid_load_from_file)
            QDoubleSpinBox* spinBoxGridSizeY = parent->findChild<QDoubleSpinBox*>("spinBoxGridSizeY")
            if(spinBoxGridSizeY) spinBoxGridSizeY->setEnabled(!dialog.grid_load_from_file)
            QLabel* labelGridSpacingX = parent->findChild<QLabel*>("labelGridSpacingX")
            if(labelGridSpacingX) labelGridSpacingX->setEnabled(!dialog.grid_load_from_file)
            QDoubleSpinBox* spinBoxGridSpacingX = parent->findChild<QDoubleSpinBox*>("spinBoxGridSpacingX")
            if(spinBoxGridSpacingX) spinBoxGridSpacingX->setEnabled(!dialog.grid_load_from_file)
            QLabel* labelGridSpacingY = parent->findChild<QLabel*>("labelGridSpacingY")
            if(labelGridSpacingY) labelGridSpacingY->setEnabled(!dialog.grid_load_from_file)
            QDoubleSpinBox* spinBoxGridSpacingY = parent->findChild<QDoubleSpinBox*>("spinBoxGridSpacingY")
            if(spinBoxGridSpacingY) spinBoxGridSpacingY->setEnabled(!dialog.grid_load_from_file)
            QLabel* labelGridSizeRadius = parent->findChild<QLabel*>("labelGridSizeRadius")
            if(labelGridSizeRadius) labelGridSizeRadius->setEnabled(!dialog.grid_load_from_file)
            QDoubleSpinBox* spinBoxGridSizeRadius = parent->findChild<QDoubleSpinBox*>("spinBoxGridSizeRadius")
            if(spinBoxGridSizeRadius) spinBoxGridSizeRadius->setEnabled(!dialog.grid_load_from_file)
            QLabel* labelGridSpacingRadius = parent->findChild<QLabel*>("labelGridSpacingRadius")
            if (labelGridSpacingRadius) {
                labelGridSpacingRadius->setEnabled(!dialog.grid_load_from_file)
            }
            QDoubleSpinBox* spinBoxGridSpacingRadius = parent->findChild<QDoubleSpinBox*>("spinBoxGridSpacingRadius")
            if (spinBoxGridSpacingRadius) {
                spinBoxGridSpacingRadius->setEnabled(!dialog.grid_load_from_file)
            }
            QLabel* labelGridSpacingAngle = parent->findChild<QLabel*>("labelGridSpacingAngle")
            if (labelGridSpacingAngle) {
                labelGridSpacingAngle->setEnabled(!dialog.grid_load_from_file)
            }
            QDoubleSpinBox* spinBoxGridSpacingAngle = parent->findChild<QDoubleSpinBox*>("spinBoxGridSpacingAngle")
            if(spinBoxGridSpacingAngle) spinBoxGridSpacingAngle->setEnabled(!dialog.grid_load_from_file)
        }
    }
}

def Settings_Dialog::comboBoxGridTypeCurrentIndexChanged(const QString& type):
    strcpy(dialog.grid_type, type.toLocal8Bit().constData())

    QObject* senderObj = sender()
    if (senderObj) {
        QObject* parent = senderObj->parent()
        if (parent) {
            int visibility = 0
            if(type == "Circular") visibility = 1

            QLabel* labelGridSizeX = parent->findChild<QLabel*>("labelGridSizeX")
            if (labelGridSizeX) {
                labelGridSizeX->setVisible(!visibility)
            }
            QDoubleSpinBox* spinBoxGridSizeX = parent->findChild<QDoubleSpinBox*>("spinBoxGridSizeX")
            if (spinBoxGridSizeX) {
                spinBoxGridSizeX->setVisible(!visibility)
            }
            QLabel* labelGridSizeY = parent->findChild<QLabel*>("labelGridSizeY")
            if (labelGridSizeY) {
                labelGridSizeY->setVisible(!visibility)
            }
            QDoubleSpinBox* spinBoxGridSizeY = parent->findChild<QDoubleSpinBox*>("spinBoxGridSizeY")
            if (spinBoxGridSizeY) {
                spinBoxGridSizeY->setVisible(!visibility)
            }
            QLabel* labelGridSpacingX = parent->findChild<QLabel*>("labelGridSpacingX")
            if(labelGridSpacingX) labelGridSpacingX->setVisible(!visibility)
            QDoubleSpinBox* spinBoxGridSpacingX = parent->findChild<QDoubleSpinBox*>("spinBoxGridSpacingX")
            if(spinBoxGridSpacingX) spinBoxGridSpacingX->setVisible(!visibility)
            QLabel* labelGridSpacingY = parent->findChild<QLabel*>("labelGridSpacingY")
            if(labelGridSpacingY) labelGridSpacingY->setVisible(!visibility)
            QDoubleSpinBox* spinBoxGridSpacingY = parent->findChild<QDoubleSpinBox*>("spinBoxGridSpacingY")
            if(spinBoxGridSpacingY) spinBoxGridSpacingY->setVisible(!visibility)
            QLabel* labelGridSizeRadius = parent->findChild<QLabel*>("labelGridSizeRadius")
            if(labelGridSizeRadius) labelGridSizeRadius->setVisible(visibility)
            QDoubleSpinBox* spinBoxGridSizeRadius = parent->findChild<QDoubleSpinBox*>("spinBoxGridSizeRadius")
            if(spinBoxGridSizeRadius) spinBoxGridSizeRadius->setVisible(visibility)
            QLabel* labelGridSpacingRadius = parent->findChild<QLabel*>("labelGridSpacingRadius")
            if(labelGridSpacingRadius) labelGridSpacingRadius->setVisible(visibility)
            QDoubleSpinBox* spinBoxGridSpacingRadius = parent->findChild<QDoubleSpinBox*>("spinBoxGridSpacingRadius")
            if(spinBoxGridSpacingRadius) spinBoxGridSpacingRadius->setVisible(visibility)
            QLabel* labelGridSpacingAngle = parent->findChild<QLabel*>("labelGridSpacingAngle")
            if(labelGridSpacingAngle) labelGridSpacingAngle->setVisible(visibility)
            QDoubleSpinBox* spinBoxGridSpacingAngle = parent->findChild<QDoubleSpinBox*>("spinBoxGridSpacingAngle")
            if(spinBoxGridSpacingAngle) spinBoxGridSpacingAngle->setVisible(visibility)
        }
    }
}

def Settings_Dialog::checkBoxGridCenterOnOriginStateChanged(int checked):
    dialog.grid_center_on_origin = checked

    QObject* senderObj = sender()
    if (senderObj) {
        QObject* parent = senderObj->parent()
        if (parent) {
            QLabel* labelGridCenterX = parent->findChild<QLabel*>("labelGridCenterX")
            if (labelGridCenterX) {
                labelGridCenterX->setEnabled(!dialog.grid_center_on_origin)
            }
            QDoubleSpinBox* spinBoxGridCenterX = parent->findChild<QDoubleSpinBox*>("spinBoxGridCenterX")
            if (spinBoxGridCenterX) {
                spinBoxGridCenterX->setEnabled(!dialog.grid_center_on_origin)
            }
            QLabel* labelGridCenterY = parent->findChild<QLabel*>("labelGridCenterY")
            if(labelGridCenterY) labelGridCenterY->setEnabled(!dialog.grid_center_on_origin)
            QDoubleSpinBox* spinBoxGridCenterY = parent->findChild<QDoubleSpinBox*>("spinBoxGridCenterY")
            if(spinBoxGridCenterY) spinBoxGridCenterY->setEnabled(!dialog.grid_center_on_origin)
        }
    }
}

def Settings_Dialog::comboBoxRulerMetricCurrentIndexChanged(int index):
    QComboBox* comboBox = qobject_cast<QComboBox*>(sender())
    if (comboBox) {
        int ok = 0
        dialog.ruler_metric = comboBox->itemData(index).toBool()
    }
    else {
        dialog.ruler_metric = 1
    }
}

def Settings_Dialog::chooseRulerColor():
    QPushButton* button = qobject_cast<QPushButton*>(sender())
    if (button) {
        QColorDialog* colorDialog = new QColorDialog(QColor(accept_.ruler_color), this)
        connect(colorDialog, SIGNAL(currentColorChanged(const QColor&)), this, SLOT(currentRulerColorChanged(const QColor&)))
        colorDialog->exec()

        if (colorDialog->result() == QDialog::Accepted) {
            accept_.ruler_color = colorDialog->selectedColor().rgb()
            QPixmap pix(16,16)
            pix.fill(QColor(accept_.ruler_color))
            button->setIcon(QIcon(pix))
            mainWin->updateAllViewRulerColors(accept_.ruler_color)
        }
        else {
            mainWin->updateAllViewRulerColors(dialog.ruler_color)
        }
    }
}

def Settings_Dialog::currentRulerColorChanged(const QColor& color):
    preview.ruler_color = color.rgb()
    mainWin->updateAllViewRulerColors(preview.ruler_color)

def Settings_Dialog::buttonQSnapSelectAllClicked():
    emit buttonQSnapSelectAll(1)

def Settings_Dialog::buttonQSnapClearAllClicked():
    emit buttonQSnapClearAll(0)

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

def Settings_Dialog::comboBoxQSnapLocatorColorCurrentIndexChanged(int index):
    /* TODO: Alert user if color matched the display bg color */
    QComboBox* comboBox = qobject_cast<QComboBox*>(sender())
    unsigned int defaultColor = qRgb(255,255,0); /* Yellow */
    if (comboBox) {
        bool ok = 0
        dialog.qsnap_locator_color = comboBox->itemData(index).toUInt(&ok)
        if(!ok)
            dialog.qsnap_locator_color = defaultColor
    }
    else {
        dialog.qsnap_locator_color = defaultColor
    }
}

def Settings_Dialog::sliderQSnapLocatorSizeValueChanged(int value):
    dialog.qsnap_locator_size = value

def Settings_Dialog::sliderQSnapApertureSizeValueChanged(int value):
    dialog.qsnap_aperture_size = value

def Settings_Dialog::checkBoxLwtShowLwtStateChanged(int checked):
    preview.lwt_show_lwt = checked
    if (preview.lwt_show_lwt) {
        enableLwt()
    }
    else {
        disableLwt()
    }

    QObject* senderObj = sender()
    if (senderObj) {
        QObject* parent = senderObj->parent()
        if (parent) {
            QCheckBox* checkBoxRealRender = parent->findChild<QCheckBox*>("checkBoxRealRender")
            if (checkBoxRealRender) {
                checkBoxRealRender->setEnabled(preview.lwt_show_lwt)
            }
        }
    }
}

def Settings_Dialog::checkBoxLwtRealRenderStateChanged(int checked):
    preview.lwt_real_render = checked
    if (preview.lwt_real_render) {
        enableReal()
    }
    else {
        disableReal()
    }
}

def Settings_Dialog::comboBoxSelectionCoolGripColorCurrentIndexChanged(int index):
    /* TODO: Alert user if color matched the display bg color */
    QComboBox* comboBox = qobject_cast<QComboBox*>(sender())
    unsigned int defaultColor = qRgb(0,0,255); /*Blue*/
    if (comboBox) {
        bool ok = 0
        dialog.selection_coolgrip_color = comboBox->itemData(index).toUInt(&ok)
        if(!ok)
            dialog.selection_coolgrip_color = defaultColor
    }
    else {
        dialog.selection_coolgrip_color = defaultColor
    }
}

def Settings_Dialog::comboBoxSelectionHotGripColorCurrentIndexChanged(int index):
    /* TODO: Alert user if color matched the display bg color */
    QComboBox* comboBox = qobject_cast<QComboBox*>(sender())
    unsigned int defaultColor = qRgb(255,0,0); /* Red */
    if (comboBox) {
        bool ok = 0
        dialog.selection_hotgrip_color = comboBox->itemData(index).toUInt(&ok)
        if (!ok) {
            dialog.selection_hotgrip_color = defaultColor
        }
    }
    else {
        dialog.selection_hotgrip_color = defaultColor
    }
}

def Settings_Dialog::acceptChanges():
    dialog.general_mdi_bg_use_logo = preview.general_mdi_bg_use_logo
    dialog.general_mdi_bg_use_texture = preview.general_mdi_bg_use_texture
    dialog.general_mdi_bg_use_color = preview.general_mdi_bg_use_color
    strcpy(dialog.general_mdi_bg_logo, accept_.general_mdi_bg_logo)
    strcpy(dialog.general_mdi_bg_texture, accept_.general_mdi_bg_texture)
    dialog.general_mdi_bg_color = accept_.general_mdi_bg_color
    dialog.display_show_scrollbars = preview.display_show_scrollbars
    dialog.display_crosshair_color = accept_.display_crosshair_color
    dialog.display_bg_color = accept_.display_bg_color
    dialog.display_selectbox_left_color = accept_.display_selectbox_left_color
    dialog.display_selectbox_left_fill = accept_.display_selectbox_left_fill
    dialog.display_selectbox_right_color = accept_.display_selectbox_right_color
    dialog.display_selectbox_right_fill = accept_.display_selectbox_right_fill
    dialog.display_selectbox_alpha = preview.display_selectbox_alpha
    if (dialog.grid_color_match_crosshair) {
        dialog.grid_color = accept_.display_crosshair_color
    }
    else {
        dialog.grid_color = accept_.grid_color
    }
    dialog.ruler_color = accept_.ruler_color
    dialog.lwt_show_lwt = preview.lwt_show_lwt
    dialog.lwt_real_render = preview.lwt_real_render

    strcpy(settings.general_language, dialog.general_language)
    strcpy(settings.general_icon_theme, dialog.general_icon_theme)
    settings.general_icon_size = dialog.general_icon_size
    settings.general_mdi_bg_use_logo = dialog.general_mdi_bg_use_logo
    settings.general_mdi_bg_use_texture = dialog.general_mdi_bg_use_texture
    settings.general_mdi_bg_use_color = dialog.general_mdi_bg_use_color
    strcpy(settings.general_mdi_bg_logo, dialog.general_mdi_bg_logo)
    strcpy(settings.general_mdi_bg_texture, dialog.general_mdi_bg_texture)
    settings.general_mdi_bg_color = dialog.general_mdi_bg_color
    settings.general_tip_of_the_day = dialog.general_tip_of_the_day
    /*TODO: settings.GeneralSystemHelpBrowser = dialog.general_system_help_browser;*/
    settings.display_use_opengl = dialog.display_use_opengl
    settings.display_renderhint_aa = dialog.display_renderhint_aa
    settings.display_renderhint_text_aa = dialog.display_renderhint_text_aa
    settings.display_renderhint_smooth_pix = dialog.display_renderhint_smooth_pix
    settings.display_renderhint_high_aa = dialog.display_renderhint_high_aa
    settings.display_renderhint_noncosmetic = dialog.display_renderhint_noncosmetic
    settings.display_show_scrollbars = dialog.display_show_scrollbars
    settings.display_scrollbar_widget_num = dialog.display_scrollbar_widget_num
    settings.display_crosshair_color = dialog.display_crosshair_color
    settings.display_bg_color = dialog.display_bg_color
    settings.display_selectbox_left_color = dialog.display_selectbox_left_color
    settings.display_selectbox_left_fill = dialog.display_selectbox_left_fill
    settings.display_selectbox_right_color = dialog.display_selectbox_right_color
    settings.display_selectbox_right_fill = dialog.display_selectbox_right_fill
    settings.display_selectbox_alpha = dialog.display_selectbox_alpha
    settings.display_zoomscale_in = dialog.display_zoomscale_in
    settings.display_zoomscale_out = dialog.display_zoomscale_out
    /*TODO: settings.DisplayCrossHairPercent(dialog.display_crosshair_percent);*/
    /*TODO: settings.DisplayUnits(dialog.display_units);*/
    /*TODO: settings.PromptSaveHistoryFilename(dialog.prompt_save_history_filename);*/
    /*TODO: settings.open_format(dialog.opensave_open_format);*/
    /*TODO: settings.open_thumbnail(dialog.opensave_open_thumbnail);*/
    /*TODO: settings.save_format = dialog.opensave_save_format);*/
    /*TODO: settings.save_thumbnail = dialog.opensave_save_thumbnail);*/
    settings.opensave_recent_max_files = dialog.opensave_recent_max_files
    settings.opensave_trim_dst_num_jumps = dialog.opensave_trim_dst_num_jumps
    /*TODO: settings.PrintingDefaultDevice = dialog.printing_default_device;*/
    /*TODO: settings.PrintingUseLastDevice = dialog.printing_use_last_device;*/
    settings.printing_disable_bg = dialog.printing_disable_bg
    settings.grid_show_on_load = dialog.grid_show_on_load
    settings.grid_show_origin = dialog.grid_show_origin
    settings.grid_color_match_crosshair = dialog.grid_color_match_crosshair
    settings.grid_color = dialog.grid_color
    /*TODO: settings.GridLoadFromFile = dialog.grid_load_from_file;*/
    strcpy(settings.grid_type, dialog.grid_type)
    settings.grid_center_on_origin = dialog.grid_center_on_origin
    settings.grid_center = dialog.grid_center
    settings.grid_size = dialog.grid_size
    settings.grid_spacing = dialog.grid_spacing
    settings.grid_size_radius = dialog.grid_size_radius
    settings.grid_spacing_radius = dialog.grid_spacing_radius
    settings.grid_spacing_angle = dialog.grid_spacing_angle
    settings.ruler_show_on_load = dialog.ruler_show_on_load
    settings.ruler_metric = dialog.ruler_metric
    settings.ruler_color = dialog.ruler_color
    settings.ruler_pixel_size = dialog.ruler_pixel_size
    /*TODO: settings.qsnap_enabled = dialog.qsnap_enabled;*/
    settings.qsnap_locator_color = dialog.qsnap_locator_color
    settings.qsnap_locator_size = dialog.qsnap_locator_size
    settings.qsnap_aperture_size = dialog.qsnap_aperture_size
    settings.qsnap_endpoint = dialog.qsnap_endpoint
    settings.qsnap_midpoint = dialog.qsnap_midpoint
    settings.qsnap_center = dialog.qsnap_center
    settings.qsnap_node = dialog.qsnap_node
    settings.qsnap_quadrant = dialog.qsnap_quadrant
    settings.qsnap_intersection = dialog.qsnap_intersection
    settings.qsnap_extension = dialog.qsnap_extension
    settings.qsnap_insertion = dialog.qsnap_insertion
    settings.qsnap_perpendicular = dialog.qsnap_perpendicular
    settings.qsnap_tangent = dialog.qsnap_tangent
    settings.qsnap_nearest = dialog.qsnap_nearest
    settings.qsnap_apparent = dialog.qsnap_apparent
    settings.qsnap_parallel = dialog.qsnap_parallel
    settings.lwt_show_lwt = dialog.lwt_show_lwt
    settings.lwt_real_render = dialog.lwt_real_render
    settings.selection_mode_pickfirst = dialog.selection_mode_pickfirst
    settings.selection_mode_pickadd = dialog.selection_mode_pickadd
    settings.selection_mode_pickdrag = dialog.selection_mode_pickdrag
    settings.selection_coolgrip_color = dialog.selection_coolgrip_color
    settings.selection_hotgrip_color = dialog.selection_hotgrip_color
    settings.selection_grip_size = dialog.selection_grip_size
    settings.selection_pickbox_size = dialog.selection_pickbox_size

    /*Make sure the user sees the changes applied immediately*/
    mainWin->mdiArea->useBackgroundLogo(dialog.general_mdi_bg_use_logo)
    mainWin->mdiArea->useBackgroundTexture(dialog.general_mdi_bg_use_texture)
    mainWin->mdiArea->useBackgroundColor(dialog.general_mdi_bg_use_color)
    mainWin->mdiArea->setBackgroundLogo(dialog.general_mdi_bg_logo)
    mainWin->mdiArea->setBackgroundTexture(dialog.general_mdi_bg_texture)
    mainWin->mdiArea->setBackgroundColor(dialog.general_mdi_bg_color)
    mainWin->iconResize(dialog.general_icon_size)
    mainWin->updateAllViewScrollBars(dialog.display_show_scrollbars)
    mainWin->updateAllViewCrossHairColors(dialog.display_crosshair_color)
    mainWin->updateAllViewBackgroundColors(dialog.display_bg_color)
    mainWin->updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                                          dialog.display_selectbox_left_fill,
                                          dialog.display_selectbox_right_color,
                                          dialog.display_selectbox_right_fill,
                                          dialog.display_selectbox_alpha)
    mainWin->updateAllViewGridColors(dialog.grid_color)
    mainWin->updateAllViewRulerColors(dialog.ruler_color)
    if (dialog.lwt_show_lwt) {
        enableLwt()
    }
    else { disableLwt(); }
    if (dialog.lwt_real_render) { enableReal(); }
    else { disableReal(); }
    mainWin->updatePickAddMode(dialog.selection_mode_pickadd)

    mainWin->writeSettings()
    accept()

def Settings_Dialog::rejectChanges():
    /*TODO: inform the user if they have changed settings*/

    /*Update the view since the user must accept the preview*/
    mainWin->mdiArea->useBackgroundLogo(dialog.general_mdi_bg_use_logo)
    mainWin->mdiArea->useBackgroundTexture(dialog.general_mdi_bg_use_texture)
    mainWin->mdiArea->useBackgroundColor(dialog.general_mdi_bg_use_color)
    mainWin->mdiArea->setBackgroundLogo(dialog.general_mdi_bg_logo)
    mainWin->mdiArea->setBackgroundTexture(dialog.general_mdi_bg_texture)
    mainWin->mdiArea->setBackgroundColor(dialog.general_mdi_bg_color)
    mainWin->updateAllViewScrollBars(dialog.display_show_scrollbars)
    mainWin->updateAllViewCrossHairColors(dialog.display_crosshair_color)
    mainWin->updateAllViewBackgroundColors(dialog.display_bg_color)
    mainWin->updateAllViewSelectBoxColors(dialog.display_selectbox_left_color,
                                          dialog.display_selectbox_left_fill,
                                          dialog.display_selectbox_right_color,
                                          dialog.display_selectbox_right_fill,
                                          dialog.display_selectbox_alpha)
    mainWin->updateAllViewGridColors(dialog.grid_color)
    mainWin->updateAllViewRulerColors(dialog.ruler_color)
    if(dialog.lwt_show_lwt) { enableLwt(); }
    else                    { disableLwt(); }
    if(dialog.lwt_real_render) { enableReal(); }
    else                       { disableReal(); }

    reject()



PropertyEditor::PropertyEditor(const QString& iconDirectory, int pickAddMode, QWidget* widgetToFocus, QWidget* parent, Qt::WindowFlags flags) : QDockWidget(parent, flags):
    int i
    iconDir = iconDirectory
    iconSize = 16
    propertyEditorButtonStyle = Qt::ToolButtonTextBesideIcon; /*TODO: Make customizable*/
    setMinimumSize(100,100)

    pickAdd = pickAddMode

    precisionAngle = 0; /*TODO: Load this from settings and provide function for updating from settings*/
    precisionLength = 4; /*TODO: Load this from settings and provide function for updating from settings*/

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
    hboxLayoutSelection->addWidget(createComboBoxSelected())
    hboxLayoutSelection->addWidget(createToolButtonQSelect())
    hboxLayoutSelection->addWidget(createToolButtonPickAdd())
    widgetSelection->setLayout(hboxLayoutSelection)

    for (i=1; i<OBJ_TYPE_UNKNOWN-OBJ_TYPE_BASE; i++) {
        groupBoxGeometry[i] = createGroupBoxGeometry(i+OBJ_TYPE_BASE)
    }

    QScrollArea* scrollProperties = new QScrollArea(this)
    QWidget* widgetProperties = new QWidget(this)
    QVBoxLayout* vboxLayoutProperties = new QVBoxLayout(this)
    vboxLayoutProperties->addWidget(createGroupBoxGeneral())
    for (i=1; i<OBJ_TYPE_UNKNOWN-OBJ_TYPE_BASE; i++) {
        vboxLayoutProperties->addWidget(groupBoxGeometry[i+OBJ_TYPE_BASE])
    }
    vboxLayoutProperties->addWidget(createGroupBoxMiscArc())
    vboxLayoutProperties->addWidget(createGroupBoxMiscImage())
    vboxLayoutProperties->addWidget(createGroupBoxMiscPath())
    vboxLayoutProperties->addWidget(createGroupBoxMiscPolyline())
    vboxLayoutProperties->addWidget(createGroupBoxTextTextSingle())
    vboxLayoutProperties->addWidget(createGroupBoxMiscTextSingle())
    vboxLayoutProperties->addStretch(1)
    widgetProperties->setLayout(vboxLayoutProperties)
    scrollProperties->setWidget(widgetProperties)
    scrollProperties->setWidgetResizable(1)

    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(this)
    vboxLayoutMain->addWidget(widgetSelection)
    vboxLayoutMain->addWidget(scrollProperties)
    widgetMain->setLayout(vboxLayoutMain)

    setWidget(widgetMain)
    setWindowTitle(tr("Properties"))
    setAllowedAreas(Qt::LeftDockWidgetArea | Qt::RightDockWidgetArea)

    hideAllGroups()

    connect(signalMapper, SIGNAL(mapped(QObject*)), this, SLOT(fieldEdited(QObject*)))

    focusWidget = widgetToFocus
    this->installEventFilter(this)

PropertyEditor::~PropertyEditor():
}

bool PropertyEditor::eventFilter(QObject *obj, QEvent *event):
    if(event->type() == QEvent::KeyPress)
    {
        QKeyEvent* pressedKey = (QKeyEvent*)event
        int key = pressedKey->key()
        switch(key)
        {
            case Qt::Key_Escape:
                if(focusWidget)
                    focusWidget->setFocus(Qt::OtherFocusReason)
                return 1
                break
            default:
                pressedKey->ignore()
        }
    }
    return QObject::eventFilter(obj, event)

QComboBox* PropertyEditor::createComboBoxSelected():
    comboBoxSelected = new QComboBox(this)
    comboBoxSelected->addItem(tr("No Selection"))
    return comboBoxSelected

QToolButton* PropertyEditor::createToolButtonQSelect():
    toolButtonQSelect = new QToolButton(this)
    toolButtonQSelect->setIcon(loadIcon(quickselect_xpm))
    toolButtonQSelect->setIconSize(QSize(iconSize, iconSize))
    toolButtonQSelect->setText("QSelect")
    toolButtonQSelect->setToolTip("QSelect"); /*TODO: Better Description*/
    toolButtonQSelect->setToolButtonStyle(Qt::ToolButtonIconOnly)
    return toolButtonQSelect

QToolButton* PropertyEditor::createToolButtonPickAdd():
    /*TODO: Set as PickAdd or PickNew based on settings*/
    toolButtonPickAdd = new QToolButton(this)
    updatePickAddModeButton(pickAdd)
    connect(toolButtonPickAdd, SIGNAL(clicked(int)), this, SLOT(togglePickAddMode()))
    return toolButtonPickAdd

def PropertyEditor::updatePickAddModeButton(int pickAddMode):
    pickAdd = pickAddMode
    if (pickAdd) {
        toolButtonPickAdd->setIcon(loadIcon(pickadd_xpm))
        toolButtonPickAdd->setIconSize(QSize(iconSize, iconSize))
        toolButtonPickAdd->setText("PickAdd")
        toolButtonPickAdd->setToolTip("PickAdd Mode - Add to current selection.\nClick to switch to PickNew Mode.")
        toolButtonPickAdd->setToolButtonStyle(Qt::ToolButtonIconOnly)
    }
    else {
        toolButtonPickAdd->setIcon(loadIcon(picknew_xpm))
        toolButtonPickAdd->setIconSize(QSize(iconSize, iconSize))
        toolButtonPickAdd->setText("PickNew")
        toolButtonPickAdd->setToolTip("PickNew Mode - Replace current selection.\nClick to switch to PickAdd Mode.")
        toolButtonPickAdd->setToolButtonStyle(Qt::ToolButtonIconOnly)
    }
}

def PropertyEditor::togglePickAddMode():
    emit pickAddModeToggled()

def PropertyEditor::setSelectedItems(QList<QGraphicsItem*> itemList):
    selectedItemList = itemList
    /*Hide all the groups initially, then decide which ones to show*/
    hideAllGroups()
    comboBoxSelected->clear()

    if(itemList.isEmpty())
    {
        comboBoxSelected->addItem(tr("No Selection"))
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

        int objType = item->type()
        typeSet.insert(objType)

        if (objType > OBJ_TYPE_BASE && objType < OBJ_TYPE_UNKNOWN) {
            if (numObjects[objType-OBJ_TYPE_BASE] == 0) {
                numTypes++
            }
            numObjects[objType-OBJ_TYPE_BASE]++
        }
        else {
            numObjects[OBJ_TYPE_UNKNOWN-OBJ_TYPE_BASE]++
        }
    }

    /*==================================================*/
    /* Populate the selection comboBox*/
    /*==================================================*/
    if (numTypes > 1) {
        comboBoxSelected->addItem(tr("Varies") + " (" + QString().setNum(numAll) + ")")
        connect(comboBoxSelected, SIGNAL(currentIndexChanged(int)), this, SLOT(showOneType(int)))
    }

    for (i=0; i<31; i++) {
        if (numObjects[i] > 0) {
            QString comboBoxStr = tr(obj_names[i])
                + " (" + QString().setNum(numObjects[i]) + ")"
            comboBoxSelected->addItem(comboBoxStr, OBJ_TYPE_BASE+i)
        }
    }

    /* ==================================================
     * Load Data into the fields
     * ================================================== */

    /* Clear fields first so if the selected data varies, the comparison is simple */
    clearAllFields()

    foreach(QGraphicsItem* item, itemList) {
        if(!item) continue

        /* TODO: load data into the General field */

        int objType = item->type()
        switch (objType) {
        case OBJ_TYPE_ARC:
            {
            ArcObject* obj = static_cast<ArcObject*>(item)
            if (obj) {
                QPointF p = obj->objectCenter()
                updateLineEditNumIfVaries(lineEdit[ARC_CENTER_X], p.x(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_CENTER_Y], -p.y(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_RADIUS], obj->objectRadius(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_START_ANGLE], obj->objectStartAngle(), 1)
                updateLineEditNumIfVaries(lineEdit[ARC_END_ANGLE], obj->objectEndAngle(), 1)
                updateLineEditNumIfVaries(lineEdit[ARC_START_X], obj->objectStartPoint().x(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_START_Y], -obj->objectStartPoint().y(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_END_X], obj->objectEndPoint().x(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_END_Y], -obj->objectEndPoint().y(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_AREA], obj->objectArea(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_LENGTH], obj->objectArcLength(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_CHORD], obj->objectChord(), 0)
                updateLineEditNumIfVaries(lineEdit[ARC_INC_ANGLE], obj->objectIncludedAngle(), 1)
                updateComboBoxintIfVaries(comboBox[ARC_CLOCKWISE], obj->objectClockwise(), 1)
            }
            }
            break
        case OBJ_TYPE_BLOCK:
            {
            /*TODO: load block data*/
            }
            break
        case OBJ_TYPE_CIRCLE:
            {
            CircleObject* obj = static_cast<CircleObject*>(item)
            if (obj) {
                QPointF p = obj->objectCenter()
                updateLineEditNumIfVaries(lineEdit[CIRCLE_CENTER_X], p.x(), 0)
                updateLineEditNumIfVaries(lineEdit[CIRCLE_CENTER_Y], -p.y(), 0)
                updateLineEditNumIfVaries(lineEdit[CIRCLE_RADIUS], obj->objectRadius(), 0)
                updateLineEditNumIfVaries(lineEdit[CIRCLE_DIAMETER], obj->objectDiameter(), 0)
                updateLineEditNumIfVaries(lineEdit[CIRCLE_AREA], obj->objectArea(), 0)
                updateLineEditNumIfVaries(lineEdit[CIRCLE_CIRCUMFERENCE], obj->objectCircumference(), 0)
            }
            }
            break
        case OBJ_TYPE_DIMALIGNED:
            {
            /* TODO: load aligned dimension data */
            }
            break
        case OBJ_TYPE_DIMANGULAR:
            {
            /* TODO: load angular dimension data */
            }
            break
        case OBJ_TYPE_DIMARCLENGTH:
            {
            /* TODO: load arclength dimension data */
            }
            break
        case OBJ_TYPE_DIMDIAMETER:
            {
            /* TODO: load diameter dimension data */
            }
            break
        case OBJ_TYPE_DIMLEADER:
            {
            /* TODO: load leader dimension data */
            }
            break
        case OBJ_TYPE_DIMLINEAR:
            {
            /* TODO: load linear dimension data */
            }
            break
        case OBJ_TYPE_DIMORDINATE:
            {
            /* TODO: load ordinate dimension data */
            }
            break
        case OBJ_TYPE_DIMRADIUS:
            {
            /* TODO: load radius dimension data */
            }
            break
        case OBJ_TYPE_ELLIPSE:
            {
            EllipseObject* obj = static_cast<EllipseObject*>(item)
            if (obj) {
                QPointF p = obj->objectCenter()
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_CENTER_X], p.x(), 0)
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_CENTER_Y], -p.y(), 0)
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_RADIUS_MAJOR], obj->objectRadiusMajor(), 0)
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_RADIUS_MINOR], obj->objectRadiusMinor(), 0)
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_DIAMETER_MAJOR], obj->objectDiameterMajor(), 0)
                updateLineEditNumIfVaries(lineEdit[ELLIPSE_DIAMETER_MINOR], obj->objectDiameterMinor(), 0)
            }
            }
            break
        case OBJ_TYPE_IMAGE:
            {
            /*TODO: load image data*/
            }
            break
        case OBJ_TYPE_INFINITELINE:
            {
            /* TODO: load infinite line data */
            }
            break
        case OBJ_TYPE_LINE:
            {
            LineObject* obj = static_cast<LineObject*>(item)
            if (obj) {
                updateLineEditNumIfVaries(lineEdit[LINE_START_X], obj->objectEndPoint1().x(), 0)
                updateLineEditNumIfVaries(lineEdit[LINE_START_Y], -obj->objectEndPoint1().y(), 0)
                updateLineEditNumIfVaries(lineEdit[LINE_END_X], obj->objectEndPoint2().x(), 0)
                updateLineEditNumIfVaries(lineEdit[LINE_END_Y], -obj->objectEndPoint2().y(), 0)
                updateLineEditNumIfVaries(lineEdit[LINE_DELTA_X], obj->objectDeltaX(), 0)
                updateLineEditNumIfVaries(lineEdit[LINE_DELTA_Y], -obj->objectDeltaY(), 0)
                updateLineEditNumIfVaries(lineEdit[LINE_ANGLE], obj->objectAngle(), 1)
                updateLineEditNumIfVaries(lineEdit[LINE_LENGTH], obj->objectLength(), 0)
            }
            }
            break
        case OBJ_TYPE_PATH:
        {
            /*TODO: load path data*/
        }
            break
        case OBJ_TYPE_POINT:
            {
            PointObject* obj = static_cast<PointObject*>(item)
            if (obj) {
                updateLineEditNumIfVaries(lineEdit[POINT_X], obj->objectX(), 0)
                updateLineEditNumIfVaries(lineEdit[POINT_Y], -obj->objectY(), 0)
            }
            }
            break
        case OBJ_TYPE_POLYGON:
            {
            /*TODO: load polygon data*/
            }
            break
        case OBJ_TYPE_POLYLINE:
            {
            /*TODO: load polyline data*/
            }
            break
        case OBJ_TYPE_RAY:
            {
            /*TODO: load ray data*/
            }
            break
        case OBJ_TYPE_RECTANGLE:
            {
            RectObject* obj = static_cast<RectObject*>(item)
            if(obj) {
                QPointF corn1 = obj->objectTopLeft()
                QPointF corn2 = obj->objectTopRight()
                QPointF corn3 = obj->objectBottomLeft()
                QPointF corn4 = obj->objectBottomRight()

                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_X1], corn1.x(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_Y1], -corn1.y(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_X2], corn2.x(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_Y2], -corn2.y(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_X3], corn3.x(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_Y3], -corn3.y(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_X4], corn4.x(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_CORNER_Y4], -corn4.y(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_WIDTH], obj->objectWidth(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_HEIGHT], -obj->objectHeight(), 0)
                updateLineEditNumIfVaries(lineEdit[RECT_AREA], obj->objectArea(), 0)
            }
            }
            break
        case OBJ_TYPE_TEXTMULTI:
            {
            /* TODO: load multiline text data */
            }
            break
        case OBJ_TYPE_TEXTSINGLE:
            {
            TextSingleObject* obj = static_cast<TextSingleObject*>(item)
            if (obj) {
                updateLineEditStrIfVaries(lineEditTextSingleContents, obj->objText)
                updateFontComboBoxStrIfVaries(comboBoxTextSingleFont, obj->objTextFont)
                updateComboBoxStrIfVaries(comboBoxTextSingleJustify, obj->objTextJustify, obj->objectTextJustifyList())
                updateLineEditNumIfVaries(lineEditTextSingleHeight, obj->obj_text.size, 0)
                updateLineEditNumIfVaries(lineEditTextSingleRotation, -obj->rotation(), 1)
                updateLineEditNumIfVaries(lineEditTextSingleX, obj->objectX(), 0)
                updateLineEditNumIfVaries(lineEditTextSingleY, -obj->objectY(), 0)
                updateComboBoxintIfVaries(comboBoxTextSingleBackward, obj->obj_text.backward, 1)
                updateComboBoxintIfVaries(comboBoxTextSingleUpsideDown, obj->obj_text.upsidedown, 1)
            }
            }
            break
        default:
            break
        }
    }

    /*==================================================*/
    /* Only show fields if all objects are the same type*/
    /*==================================================*/
    if (numTypes == 1) {
        foreach (int objType, typeSet) {
            showGroups(objType)
        }
    }
}

def PropertyEditor::updateLineEditStrIfVaries(QLineEdit* lineEdit, const QString& str):
    fieldOldText = lineEdit->text()
    fieldNewText = str

    if     (fieldOldText.isEmpty())       lineEdit->setText(fieldNewText)
    else if(fieldOldText != fieldNewText) lineEdit->setText(fieldVariesText)

def PropertyEditor::updateLineEditNumIfVaries(QLineEdit* lineEdit, float num, int useAnglePrecision):
    int precision = 0
    if(useAnglePrecision) precision = precisionAngle
    else                  precision = precisionLength

    fieldOldText = lineEdit->text()
    fieldNewText.setNum(num, 'f', precision)

    /*Prevent negative zero :D*/
    QString negativeZero = "-0."
    for(int i = 0; i < precision; ++i)
        negativeZero.append('0')
    if(fieldNewText == negativeZero)
        fieldNewText = negativeZero.replace("-", "")

    if     (fieldOldText.isEmpty())       lineEdit->setText(fieldNewText)
    else if(fieldOldText != fieldNewText) lineEdit->setText(fieldVariesText)

def PropertyEditor::updateFontComboBoxStrIfVaries(QFontComboBox* fontComboBox, const QString& str):
    fieldOldText = fontComboBox->property("FontFamily").toString()
    fieldNewText = str
    /*debug_message("old: %d %s, new: %d %s", oldIndex, qPrintable(fontComboBox->currentText()), newIndex, qPrintable(str));*/
    if(fieldOldText.isEmpty())
    {
        fontComboBox->setCurrentFont(QFont(fieldNewText))
        fontComboBox->setProperty("FontFamily", fieldNewText)
    }
    else if(fieldOldText != fieldNewText)
    {
        if(fontComboBox->findText(fieldVariesText) == -1) /*Prevent multiple entries*/
            fontComboBox->addItem(fieldVariesText)
        fontComboBox->setCurrentIndex(fontComboBox->findText(fieldVariesText))
    }
}

def PropertyEditor::updateComboBoxStrIfVaries(QComboBox* comboBox, const QString& str, const QStringList& strList):
    fieldOldText = comboBox->currentText()
    fieldNewText = str

    if(fieldOldText.isEmpty())
    {
        foreach(QString s, strList)
        {
            comboBox->addItem(s, s)
        }
        comboBox->setCurrentIndex(comboBox->findText(fieldNewText))
    }
    else if(fieldOldText != fieldNewText)
    {
        if(comboBox->findText(fieldVariesText) == -1) /*Prevent multiple entries*/
            comboBox->addItem(fieldVariesText)
        comboBox->setCurrentIndex(comboBox->findText(fieldVariesText))
    }
}

def PropertyEditor::updateComboBoxintIfVaries(QComboBox* comboBox, int val, int yesOrNoText):
    fieldOldText = comboBox->currentText()
    if(yesOrNoText)
    {
        if(val) fieldNewText = fieldYesText
        else    fieldNewText = fieldNoText
    }
    else
    {
        if(val) fieldNewText = fieldOnText
        else    fieldNewText = fieldOffText
    }

    if(fieldOldText.isEmpty()) {
        if (yesOrNoText) {
            comboBox->addItem(fieldYesText, 1)
            comboBox->addItem(fieldNoText, 0)
        }
        else {
            comboBox->addItem(fieldOnText, 1)
            comboBox->addItem(fieldOffText, 0)
        }
        comboBox->setCurrentIndex(comboBox->findText(fieldNewText))
    }
    else if(fieldOldText != fieldNewText) {
        /* Prevent multiple entries */
        if(comboBox->findText(fieldVariesText) == -1) {
            comboBox->addItem(fieldVariesText)
        }
        comboBox->setCurrentIndex(comboBox->findText(fieldVariesText))
    }
}

def PropertyEditor::showGroups(int objType):
    if (objType>=OBJ_TYPE_BASE && objType<OBJ_TYPE_UNKNOWN) {
        groupBoxGeometry[objType-OBJ_TYPE_BASE]->show()
    }
    if (objType == OBJ_TYPE_ARC) {
        groupBoxMiscArc->show()
    }
    else if(objType == OBJ_TYPE_IMAGE) {
        groupBoxMiscImage->show()
    }
    else if(objType == OBJ_TYPE_PATH) {
        groupBoxMiscPath->show()
    }
    else if(objType == OBJ_TYPE_POLYLINE) {
        groupBoxMiscPolyline->show()
    }
    else if(objType == OBJ_TYPE_TEXTSINGLE) {
        groupBoxTextTextSingle->show()
        groupBoxMiscTextSingle->show()
    }
}

def PropertyEditor::showOneType(int index):
    hideAllGroups()
    showGroups(comboBoxSelected->itemData(index).toInt())

def PropertyEditor::hideAllGroups():
    int i
    /* NOTE: General group will never be hidden */
    for (i=1; i<OBJ_TYPE_UNKNOWN-OBJ_TYPE_BASE; i++) {
        groupBoxGeometry[i]->hide()
    }
    groupBoxMiscArc->hide()
    groupBoxMiscImage->hide()
    groupBoxMiscPath->hide()
    groupBoxMiscPolyline->hide()
    groupBoxTextTextSingle->hide()
    groupBoxMiscTextSingle->hide()

def PropertyEditor::clearAllFields():
    int i
    for (i=0; i<COMBOBOX_PROPERTY_EDITORS; i++) {
        comboBox[i]->clear()
    }
    for (i=0; i<LINEEDIT_PROPERTY_EDITORS; i++) {
        lineEdit[i]->clear()
    }

    /* Text Single */
    comboBoxTextSingleFont->removeItem(comboBoxTextSingleFont->findText(fieldVariesText))
    /* NOTE: Do not clear comboBoxTextSingleFont */
    comboBoxTextSingleFont->setProperty("FontFamily", "")

QGroupBox* PropertyEditor::createGroupBoxGeneral():
    groupBoxGeneral = new QGroupBox(tr("General"), this)

    toolButtonGeneralLayer = createToolButton("blank", tr("Layer"));      /*TODO: use proper icon*/
    toolButtonGeneralColor = createToolButton("blank", tr("Color"));      /*TODO: use proper icon*/
    toolButtonGeneralLineType = createToolButton("blank", tr("LineType"));   /*TODO: use proper icon*/
    toolButtonGeneralLineWeight = createToolButton("blank", tr("LineWeight")); /*TODO: use proper icon*/

    comboBoxGeneralLayer = createComboBox(0)
    comboBoxGeneralColor = createComboBox(0)
    comboBoxGeneralLineType = createComboBox(0)
    comboBoxGeneralLineWeight = createComboBox(0)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout->addRow(toolButtonGeneralLayer, comboBoxGeneralLayer)
    formLayout->addRow(toolButtonGeneralColor, comboBoxGeneralColor)
    formLayout->addRow(toolButtonGeneralLineType, comboBoxGeneralLineType)
    formLayout->addRow(toolButtonGeneralLineWeight, comboBoxGeneralLineWeight)
    groupBoxGeneral->setLayout(formLayout)

    return groupBoxGeneral

QGroupBox* PropertyEditor::createGroupBoxMiscArc():
    groupBoxMiscArc = new QGroupBox(tr("Misc"), this)

    toolButtonArcClockwise = createToolButton("blank", tr("Clockwise")); /*TODO: use proper icon*/

    comboBoxArcClockwise = createComboBox(1)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout->addRow(toolButtonArcClockwise, comboBoxArcClockwise)
    groupBoxMiscArc->setLayout(formLayout)

    return groupBoxMiscArc

QGroupBox* PropertyEditor::createGroupBoxGeometry(int objType):
    int i
    QGroupBox *gb = new QGroupBox(tr("Geometry"), this)

    /* TODO: use proper icons */
    QFormLayout* formLayout = new QFormLayout(this)
    /*
    for (i=0; property_editors[i].object != OBJ_TYPE_UNKNOWN; i++) {
        if (property_editors[i].object == objType) {
            int index = property_editors[i].id
            toolButton[index] = createToolButton(property_editors[i].icon, tr(property_editors[i].label));       
            lineEdit[index] = createLineEdit(property_editors[i].type, property_editors[i].read_only)
            formLayout->addRow(toolButton[index], lineEdit[index])
            mapSignal(lineEdit[index], property_editors[i].signal, objType)
        }
    }
    */
    gb->setLayout(formLayout)

    return gb

QGroupBox* PropertyEditor::createGroupBoxMiscImage():
    groupBoxMiscImage = new QGroupBox(tr("Misc"), this)

    toolButtonImageName = createToolButton("blank", tr("Name")); /*TODO: use proper icon*/
    toolButtonImagePath = createToolButton("blank", tr("Path")); /*TODO: use proper icon*/

    lineEditImageName = createLineEdit("double", 1)
    lineEditImagePath = createLineEdit("double", 1)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout->addRow(toolButtonImageName, lineEditImageName)
    formLayout->addRow(toolButtonImagePath, lineEditImagePath)
    groupBoxMiscImage->setLayout(formLayout)

    return groupBoxMiscImage

QGroupBox* PropertyEditor::createGroupBoxMiscPath():
    groupBoxMiscPath = new QGroupBox(tr("Misc"), this)

    toolButtonPathClosed = createToolButton("blank", tr("Closed")); /*TODO: use proper icon*/

    comboBoxPathClosed = createComboBox(0)

    /*TODO: mapSignal for paths*/

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout->addRow(toolButtonPathClosed, comboBoxPathClosed)
    groupBoxMiscPath->setLayout(formLayout)

    return groupBoxMiscPath

QGroupBox* PropertyEditor::createGroupBoxMiscPolyline():
    groupBoxMiscPolyline = new QGroupBox(tr("Misc"), this)

    toolButtonPolylineClosed = createToolButton("blank", tr("Closed")); /*TODO: use proper icon*/

    comboBoxPolylineClosed = createComboBox(0)

    /*TODO: mapSignal for polylines*/

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout->addRow(toolButtonPolylineClosed, comboBoxPolylineClosed)
    groupBoxMiscPolyline->setLayout(formLayout)

    return groupBoxMiscPolyline

QGroupBox* PropertyEditor::createGroupBoxTextTextSingle():
    groupBoxTextTextSingle = new QGroupBox(tr("Text"), this)

    toolButtonTextSingleContents = createToolButton("blank", tr("Contents")); /*TODO: use proper icon*/
    toolButtonTextSingleFont = createToolButton("blank", tr("Font"));     /*TODO: use proper icon*/
    toolButtonTextSingleJustify = createToolButton("blank", tr("Justify"));  /*TODO: use proper icon*/
    toolButtonTextSingleHeight = createToolButton("blank", tr("Height"));   /*TODO: use proper icon*/
    toolButtonTextSingleRotation = createToolButton("blank", tr("Rotation")); /*TODO: use proper icon*/

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
    formLayout->addRow(toolButtonTextSingleContents, lineEditTextSingleContents)
    formLayout->addRow(toolButtonTextSingleFont, comboBoxTextSingleFont)
    formLayout->addRow(toolButtonTextSingleJustify, comboBoxTextSingleJustify)
    formLayout->addRow(toolButtonTextSingleHeight, lineEditTextSingleHeight)
    formLayout->addRow(toolButtonTextSingleRotation, lineEditTextSingleRotation)
    groupBoxTextTextSingle->setLayout(formLayout)

    return groupBoxTextTextSingle

QGroupBox* PropertyEditor::createGroupBoxMiscTextSingle():
    groupBoxMiscTextSingle = new QGroupBox(tr("Misc"), this)

    toolButtonTextSingleBackward = createToolButton("blank", tr("Backward"));   /*TODO: use proper icon*/
    toolButtonTextSingleUpsideDown = createToolButton("blank", tr("UpsideDown")); /*TODO: use proper icon*/

    comboBoxTextSingleBackward = createComboBox(0)
    comboBoxTextSingleUpsideDown = createComboBox(0)

    mapSignal(comboBoxTextSingleBackward, "comboBoxTextSingleBackward", OBJ_TYPE_TEXTSINGLE)
    mapSignal(comboBoxTextSingleUpsideDown, "comboBoxTextSingleUpsideDown", OBJ_TYPE_TEXTSINGLE)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout->addRow(toolButtonTextSingleBackward, comboBoxTextSingleBackward)
    formLayout->addRow(toolButtonTextSingleUpsideDown, comboBoxTextSingleUpsideDown)
    groupBoxMiscTextSingle->setLayout(formLayout)

    return groupBoxMiscTextSingle

QToolButton* PropertyEditor::createToolButton(const QString& iconName, const QString& txt):
    QToolButton* tb = new QToolButton(this)
    tb->setIcon(loadIcon(blank_xpm))
    tb->setIconSize(QSize(iconSize, iconSize))
    tb->setText(txt)
    tb->setToolButtonStyle(propertyEditorButtonStyle)
    tb->setStyleSheet("border:none;")
    return tb

QLineEdit* PropertyEditor::createLineEdit(const QString& validatorType, int readOnly):
    QLineEdit* le = new QLineEdit(this)
    if (validatorType == "int") {
        le->setValidator(new QIntValidator(le))
    }
    else if (validatorType == "double") {
        le->setValidator(new QDoubleValidator(le))
    }
    le->setReadOnly(readOnly)
    return le

QComboBox* PropertyEditor::createComboBox(int disable):
    QComboBox* cb = new QComboBox(this)
    cb->setDisabled(disable)
    return cb

QFontComboBox* PropertyEditor::createFontComboBox(int disable):
    QFontComboBox* fcb = new QFontComboBox(this)
    fcb->setDisabled(disable)
    return fcb

def PropertyEditor::mapSignal(QObject* fieldObj, const QString& name, QVariant value):
    fieldObj->setObjectName(name)
    fieldObj->setProperty(qPrintable(name), value)

    if (name.startsWith("lineEdit")) {
        connect(fieldObj, SIGNAL(editingFinished()), signalMapper, SLOT(map()))
    }
    else if (name.startsWith("comboBox")) {
        connect(fieldObj, SIGNAL(activated(const QString&)), signalMapper, SLOT(map()))
    }

    signalMapper->setMapping(fieldObj, fieldObj)

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
    QString objName = fieldObj->objectName()
    int objType = fieldObj->property(qPrintable(objName)).toInt()

    foreach(QGraphicsItem* item, selectedItemList)
    {
        if(item->type() != objType) continue

        switch(objType)
        {
            case OBJ_TYPE_ARC:
                if(objName == "lineEditArcCenterX") {
                    tempArcObj = static_cast<ArcObject*>(item)
                    if (tempArcObj) {
                        QPointF p = tempArcObj->objectCenter()
                        p.setX(lineEdit[ARC_CENTER_X]->text().toDouble())
                        tempArcObj->setPos(p)
                    }
                }
                if(objName == "lineEditArcCenterY") {
                    tempArcObj = static_cast<ArcObject*>(item)
                    if (tempArcObj) {
                        QPointF p = tempArcObj->objectCenter()
                        p.setY(lineEdit[ARC_CENTER_Y]->text().toDouble())
                        tempArcObj->setPos(p)
                    }
                }
                if(objName == "lineEditArcRadius") {
                    tempArcObj = static_cast<ArcObject*>(item)
                    if (tempArcObj) {
                        tempArcObj->setObjectRadius(lineEdit[ARC_RADIUS]->text().toDouble())
                    }
                }
                if(objName == "lineEditArcStartAngle") {
                    tempArcObj = static_cast<ArcObject*>(item)
                    if (tempArcObj) {
                        tempArcObj->setObjectStartAngle(lineEdit[ARC_START_ANGLE]->text().toDouble())
                    }
                }
                if(objName == "lineEditArcEndAngle") {
                    tempArcObj = static_cast<ArcObject*>(item)
                    if (tempArcObj) {
                        tempArcObj->setObjectEndAngle(lineEdit[ARC_END_ANGLE]->text().toDouble())
                    }
                }
                break
            case OBJ_TYPE_BLOCK: /*TODO: field editing*/
                break
            case OBJ_TYPE_CIRCLE:
                if(objName == "lineEditCircleCenterX") {
                    tempCircleObj = static_cast<CircleObject*>(item)
                    if (tempCircleObj) {
                        QPointF p = tempCircleObj->objectCenter()
                        p.setX(lineEdit[CIRCLE_CENTER_X]->text().toDouble())
                        tempCircleObj->setPos(p)
                    }
                }
                if(objName == "lineEditCircleCenterY") {
                    tempCircleObj = static_cast<CircleObject*>(item)
                    if (tempCircleObj) {
                        QPointF p = tempCircleObj->objectCenter()
                        p.setY(lineEdit[CIRCLE_CENTER_Y]->text().toDouble())
                        tempCircleObj->setPos(p)
                    }
                }
                if(objName == "lineEditCircleRadius") {
                    tempCircleObj = static_cast<CircleObject*>(item)
                    if (tempCircleObj) {
                        tempCircleObj->setObjectRadius(lineEdit[CIRCLE_RADIUS]->text().toDouble())
                    }
                }
                if(objName == "lineEditCircleDiameter") {
                    tempCircleObj = static_cast<CircleObject*>(item)
                    if (tempCircleObj) {
                        tempCircleObj->setObjectDiameter(lineEdit[CIRCLE_DIAMETER]->text().toDouble())
                    }
                }
                if(objName == "lineEditCircleArea") {
                    tempCircleObj = static_cast<CircleObject*>(item)
                    if(tempCircleObj) { tempCircleObj->setObjectArea(lineEdit[CIRCLE_AREA]->text().toDouble()); }
                }
                if(objName == "lineEditCircleCircumference") {
                    tempCircleObj = static_cast<CircleObject*>(item)
                    if (tempCircleObj) {
                        tempCircleObj->setObjectCircumference(lineEdit[CIRCLE_CIRCUMFERENCE]->text().toDouble())
                    }
                }
                break
            case OBJ_TYPE_DIMALIGNED: /*TODO: field editing*/
                break
            case OBJ_TYPE_DIMANGULAR: /*TODO: field editing*/
                break
            case OBJ_TYPE_DIMARCLENGTH: /*TODO: field editing*/
                break
            case OBJ_TYPE_DIMDIAMETER: /*TODO: field editing*/
                break
            case OBJ_TYPE_DIMLEADER: /*TODO: field editing*/
                break
            case OBJ_TYPE_DIMLINEAR: /*TODO: field editing*/
                break
            case OBJ_TYPE_DIMORDINATE: /*TODO: field editing*/
                break
            case OBJ_TYPE_DIMRADIUS: /*TODO: field editing*/
                break
            case OBJ_TYPE_ELLIPSE:
                if(objName == "lineEditEllipseCenterX") {
                    tempEllipseObj = static_cast<EllipseObject*>(item)
                    if (tempEllipseObj) {
                        QPointF p = tempCircleObj->objectCenter()
                        p.setX(lineEdit[ELLIPSE_CENTER_X]->text().toDouble())
                        tempCircleObj->setPos(p)
                    }
                }
                if(objName == "lineEditEllipseCenterY") {
                    tempEllipseObj = static_cast<EllipseObject*>(item)
                    if (tempEllipseObj) {
                        QPointF p = tempCircleObj->objectCenter()
                        p.setY(lineEdit[ELLIPSE_CENTER_Y]->text().toDouble())
                        tempCircleObj->setPos(p)
                    }
                }
                if(objName == "lineEditEllipseRadiusMajor") {
                    tempEllipseObj = static_cast<EllipseObject*>(item)
                    if (tempEllipseObj) {
                        tempEllipseObj->setObjectRadiusMajor(lineEdit[ELLIPSE_RADIUS_MAJOR]->text().toDouble())
                    }
                }
                if(objName == "lineEditEllipseRadiusMinor") {
                    tempEllipseObj = static_cast<EllipseObject*>(item)
                    if (tempEllipseObj) {
                        tempEllipseObj->setObjectRadiusMinor(lineEdit[ELLIPSE_RADIUS_MINOR]->text().toDouble())
                    }
                }
                if(objName == "lineEditEllipseDiameterMajor") {
                    tempEllipseObj = static_cast<EllipseObject*>(item)
                    if (tempEllipseObj) {
                        tempEllipseObj->setObjectDiameterMajor(lineEdit[ELLIPSE_DIAMETER_MAJOR]->text().toDouble())
                    }
                }
                if(objName == "lineEditEllipseDiameterMinor") {
                    tempEllipseObj = static_cast<EllipseObject*>(item)
                    if (tempEllipseObj) {
                        tempEllipseObj->setObjectDiameterMinor(lineEdit[ELLIPSE_DIAMETER_MINOR]->text().toDouble())
                    }
                }
                break
            case OBJ_TYPE_IMAGE: /*TODO: field editing*/
                break
            case OBJ_TYPE_INFINITELINE: /*TODO: field editing*/
                break
            case OBJ_TYPE_LINE:
                if(objName == "lineEditLineStartX") {
                    tempLineObj = static_cast<LineObject*>(item)
                    if (tempLineObj) {
                        tempLineObj->setObjectX1(lineEdit[LINE_START_X]->text().toDouble())
                    }
                }
                if(objName == "lineEditLineStartY") {
                    tempLineObj = static_cast<LineObject*>(item)
                    if (tempLineObj) {
                        tempLineObj->setObjectY1(-lineEdit[LINE_START_Y]->text().toDouble())
                    }
                }
                if(objName == "lineEditLineEndX") {
                    tempLineObj = static_cast<LineObject*>(item)
                    if (tempLineObj) {
                        tempLineObj->setObjectX2(lineEdit[LINE_END_X]->text().toDouble())
                    }
                }
                if(objName == "lineEditLineEndY") {
                    tempLineObj = static_cast<LineObject*>(item)
                    if (tempLineObj) {
                        tempLineObj->setObjectY2(-lineEdit[LINE_END_Y]->text().toDouble())
                    }
                }
                break
            case OBJ_TYPE_PATH: /*TODO: field editing*/
                break
            case OBJ_TYPE_POINT:
                if(objName == "lineEditPointX") {
                    tempPointObj = static_cast<PointObject*>(item)
                    if (tempPointObj) {
                        tempPointObj->setObjectX(lineEdit[POINT_X]->text().toDouble())
                    }
                }
                if(objName == "lineEditPointY") {
                    tempPointObj = static_cast<PointObject*>(item)
                    if (tempPointObj) {
                        tempPointObj->setObjectY(-lineEdit[POINT_Y]->text().toDouble())
                    }
                }
                break
            case OBJ_TYPE_POLYGON: /*TODO: field editing*/
                break
            case OBJ_TYPE_POLYLINE: /*TODO: field editing*/
                break
            case OBJ_TYPE_RAY: /*TODO: field editing*/
                break
            case OBJ_TYPE_RECTANGLE: /*TODO: field editing*/
                break
            case OBJ_TYPE_TEXTMULTI: /*TODO: field editing*/
                break
            case OBJ_TYPE_TEXTSINGLE: /*TODO: field editing*/
                if(objName == "lineEditTextSingleContents") {
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if (tempTextSingleObj) {
                        tempTextSingleObj->setObjectText(lineEditTextSingleContents->text())
                    }
                }
                if(objName == "comboBoxTextSingleFont") {
                    if(comboBoxTextSingleFont->currentText() == fieldVariesText) { break; }
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if(tempTextSingleObj) { tempTextSingleObj->setObjectTextFont(comboBoxTextSingleFont->currentFont().family()); } }
                if (objName == "comboBoxTextSingleJustify") {
                    if (comboBoxTextSingleJustify->currentText() == fieldVariesText) {
                        break
                    }
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if (tempTextSingleObj) {
                        tempTextSingleObj->setObjectTextJustify(comboBoxTextSingleJustify->itemData(comboBoxTextSingleJustify->currentIndex()).toString())
                    }
                }
                if(objName == "lineEditTextSingleHeight") {
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if (tempTextSingleObj) {
                        tempTextSingleObj->setObjectTextSize(lineEditTextSingleHeight->text().toDouble())
                    }
                }
                if(objName == "lineEditTextSingleRotation") {
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if (tempTextSingleObj) {
                        tempTextSingleObj->setRotation(-lineEditTextSingleRotation->text().toDouble())
                    }
                }
                if(objName == "lineEditTextSingleX") {
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if(tempTextSingleObj) { tempTextSingleObj->setObjectX(lineEditTextSingleX->text().toDouble()); } }
                if(objName == "lineEditTextSingleY") {
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if(tempTextSingleObj) { tempTextSingleObj->setObjectY(lineEditTextSingleY->text().toDouble()); } }
                if(objName == "comboBoxTextSingleBackward") {
                    if(comboBoxTextSingleBackward->currentText() == fieldVariesText) { break; }
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if(tempTextSingleObj) { tempTextSingleObj->setObjectTextBackward(comboBoxTextSingleBackward->itemData(comboBoxTextSingleBackward->currentIndex()).toBool()); } }
                if(objName == "comboBoxTextSingleUpsideDown") {
                    if(comboBoxTextSingleUpsideDown->currentText() == fieldVariesText) { break; }
                    tempTextSingleObj = static_cast<TextSingleObject*>(item)
                    if(tempTextSingleObj) { tempTextSingleObj->setObjectTextUpsideDown(comboBoxTextSingleUpsideDown->itemData(comboBoxTextSingleUpsideDown->currentIndex()).toBool()); } }
                break
            default:
                break
        }

    }

    /*Block this slot from running twice since calling setSelectedItems will trigger it*/
    blockSignals = 1

    QWidget* widget = QApplication::focusWidget()
    /* Update so all fields have fresh data
     * TODO: Improve this
     */
    setSelectedItems(selectedItemList)
    hideAllGroups()
    showGroups(objType)

    if(widget) widget->setFocus(Qt::OtherFocusReason)

    blockSignals = 0

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
    else if(minDist == startDist) return start
    else if(minDist == midDist)   return mid
    else if(minDist == endDist)   return end

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
        else if(lineWeight == OBJ_LWT_BYBLOCK)
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
    else if(rubberMode == OBJ_RUBBER_CIRCLE_1P_DIA)
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
    else if(rubberMode == OBJ_RUBBER_CIRCLE_2P)
    {
        QPointF sceneTan1Point = objectRubberPoint("CIRCLE_TAN1")
        QPointF sceneQSnapPoint = objectRubberPoint("CIRCLE_TAN2")
        QLineF sceneLine(sceneTan1Point, sceneQSnapPoint)
        setPos(sceneLine.pointAt(0.5))
        float diameter = sceneLine.length()
        setObjectDiameter(diameter)
        updatePath()
    }
    else if(rubberMode == OBJ_RUBBER_CIRCLE_3P)
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
    else if(rubberMode == OBJ_RUBBER_GRIP)
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
    else if(minDist == q0Dist)   return quad0
    else if(minDist == q90Dist)  return quad90
    else if(minDist == q180Dist) return quad180
    else if(minDist == q270Dist) return quad270

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
    else if(arrowStyle == Closed)
    {
        arrowStylePath = QPainterPath()
        arrowStylePath.moveTo(ap1)
        arrowStylePath.lineTo(ap0)
        arrowStylePath.lineTo(ap2)
        arrowStylePath.lineTo(ap1)
    }
    else if(arrowStyle == Dot)
    {
        arrowStylePath = QPainterPath()
        arrowStylePath.addEllipse(ap0, arrowStyleLength, arrowStyleLength)
    }
    else if(arrowStyle == Box)
    {
        arrowStylePath = QPainterPath()
        float side = QLineF(ap1, ap2).length()
        QRectF ar0(0, 0, side, side)
        ar0.moveCenter(ap0)
        arrowStylePath.addRect(ar0)
    }
    else if(arrowStyle == Tick)
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
    else if(rubberMode == OBJ_RUBBER_GRIP)
    {
        if(painter)
        {
            QPointF gripPoint = objectRubberPoint("GRIP_POINT")
            if     (gripPoint == objectEndPoint1()) painter->drawLine(line().p2(), mapFromScene(objectRubberPoint(QString())))
            else if(gripPoint == objectEndPoint2()) painter->drawLine(line().p1(), mapFromScene(objectRubberPoint(QString())))
            else if(gripPoint == objectMidPoint())  painter->drawLine(line().translated(mapFromScene(objectRubberPoint(QString()))-mapFromScene(gripPoint)))
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
    else if(minDist == end2Dist) return endPoint2
    else if(minDist == midDist)  return midPoint

    return scenePos()

QList<QPointF> DimLeaderObject::allGripPoints():
    QList<QPointF> gripPoints
    gripPoints << objectEndPoint1() << objectEndPoint2()
    if(curved)
        gripPoints << objectMidPoint()
    return gripPoints

def DimLeaderObject::gripEdit(const QPointF& before, const QPointF& after):
    if     (before == objectEndPoint1()) { setObjectEndPoint1(to_emb_vector(after)); }
    else if(before == objectEndPoint2()) { setObjectEndPoint2(to_emb_vector(after)); }
    else if(before == objectMidPoint())  { QPointF delta = after-before; moveBy(delta.x(), delta.y()); }
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
    else if(rubberMode == OBJ_RUBBER_ELLIPSE_MAJORDIAMETER_MINORRADIUS)
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
    else if(rubberMode == OBJ_RUBBER_ELLIPSE_MAJORRADIUS_MINORRADIUS)
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
    else if(rubberMode == OBJ_RUBBER_GRIP)
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
    else if(minDist == q0Dist)   return quad0
    else if(minDist == q90Dist)  return quad90
    else if(minDist == q180Dist) return quad180
    else if(minDist == q270Dist) return quad270

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
    else if(rubberMode == OBJ_RUBBER_GRIP)
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
    else if(minDist == ptrDist) return ptr
    else if(minDist == pblDist) return pbl
    else if(minDist == pbrDist) return pbr

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
    else if(rubberMode == OBJ_RUBBER_GRIP)
    {
        if(painter)
        {
            QPointF gripPoint = objectRubberPoint("GRIP_POINT")
            if     (gripPoint == objectEndPoint1()) painter->drawLine(line().p2(), mapFromScene(objectRubberPoint(QString())))
            else if(gripPoint == objectEndPoint2()) painter->drawLine(line().p1(), mapFromScene(objectRubberPoint(QString())))
            else if(gripPoint == objectMidPoint())  painter->drawLine(line().translated(mapFromScene(objectRubberPoint(QString()))-mapFromScene(gripPoint)))

            QLineF rubLine(mapFromScene(gripPoint), mapFromScene(objectRubberPoint(QString())))
            drawRubberLine(rubLine, painter, "VIEW_COLOR_CROSSHAIR")
        }
    }
}

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
    else if(minDist == end2Dist) return endPoint2
    else if(minDist == midDist)  return midPoint

    return scenePos()

QList<QPointF> LineObject::allGripPoints():
    QList<QPointF> gripPoints
    gripPoints << objectEndPoint1() << objectEndPoint2() << objectMidPoint()
    return gripPoints

def LineObject::gripEdit(const QPointF& before, const QPointF& after):
    if     (before == objectEndPoint1()) { setObjectEndPoint1(after.x(), after.y()); }
    else if(before == objectEndPoint2()) { setObjectEndPoint2(after.x(), after.y()); }
    else if(before == objectMidPoint())  { QPointF delta = after-before; moveBy(delta.x(), delta.y()); }
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
    }
}

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
            }
        }
    }
}

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
    else if(rubberMode == OBJ_RUBBER_POLYGON_INSCRIBE) {
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
    else if (rubberMode == OBJ_RUBBER_POLYGON_CIRCUMSCRIBE) {
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
    else if(rubberMode == OBJ_RUBBER_GRIP) {
        if(painter) {
            int elemCount = normalPath.elementCount()
            QPointF gripPoint = objectRubberPoint("GRIP_POINT")
            if(gripIndex == -1) gripIndex = findIndex(gripPoint)
            if(gripIndex == -1) return

            int m = 0
            int n = 0

            if(!gripIndex)                    { m = elemCount-1; n = 1; }
            else if(gripIndex == elemCount-1) { m = elemCount-2; n = 0; }
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
    else if(rubberMode == OBJ_RUBBER_GRIP)
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
            else if(gripIndex == elemCount-1) /*Last*/
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
    else if(rubberMode == OBJ_RUBBER_GRIP)
    {
        if(painter)
        {
            /* TODO: Make this work with rotation & scaling. */
            /*
            QPointF gripPoint = objectRubberPoint("GRIP_POINT")
            QPointF after = objectRubberPoint(QString())
            QPointF delta = after-gripPoint
            if     (gripPoint == objectTopLeft())     { painter->drawPolygon(mapFromScene(QRectF(after.x(), after.y(), objectWidth()-delta.x(), objectHeight()-delta.y()))); }
            else if(gripPoint == objectTopRight())    { painter->drawPolygon(mapFromScene(QRectF(objectTopLeft().x(), objectTopLeft().y()+delta.y(), objectWidth()+delta.x(), objectHeight()-delta.y()))); }
            else if(gripPoint == objectBottomLeft())  { painter->drawPolygon(mapFromScene(QRectF(objectTopLeft().x()+delta.x(), objectTopLeft().y(), objectWidth()-delta.x(), objectHeight()+delta.y()))); }
            else if(gripPoint == objectBottomRight()) { painter->drawPolygon(mapFromScene(QRectF(objectTopLeft().x(), objectTopLeft().y(), objectWidth()+delta.x(), objectHeight()+delta.y()))); }

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
    else if(minDist == ptrDist) return ptr
    else if(minDist == pblDist) return pbl
    else if(minDist == pbrDist) return pbr

    return scenePos()

QList<QPointF> RectObject::allGripPoints():
    QList<QPointF> gripPoints
    gripPoints << objectTopLeft() << objectTopRight() << objectBottomLeft() << objectBottomRight()
    return gripPoints

def RectObject::gripEdit(const QPointF& before, const QPointF& after):
    QPointF delta = after-before
    if     (before == objectTopLeft())     { setObjectRect(after.x(), after.y(), objectWidth()-delta.x(), objectHeight()-delta.y()); }
    else if(before == objectTopRight())    { setObjectRect(objectTopLeft().x(), objectTopLeft().y()+delta.y(), objectWidth()+delta.x(), objectHeight()-delta.y()); }
    else if(before == objectBottomLeft())  { setObjectRect(objectTopLeft().x()+delta.x(), objectTopLeft().y(), objectWidth()-delta.x(), objectHeight()+delta.y()); }
    else if(before == objectBottomRight()) { setObjectRect(objectTopLeft().x(), objectTopLeft().y(), objectWidth()+delta.x(), objectHeight()+delta.y()); }
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
            else if(element.isLineTo())
            {
                flippedPath.lineTo(horiz * element.x, vert * element.y)
            }
            else if(element.isCurveTo())
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
    else if(rubberMode == OBJ_RUBBER_GRIP) {
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
            else if (element.isLineTo()) {
                subPath.lineTo(element.x, element.y)
            }
            else if (element.isCurveTo()) {
                subPath.cubicTo(path.elementAt(i  ).x, path.elementAt(i  ).y, /*control point 1*/
                                path.elementAt(i+1).x, path.elementAt(i+1).y, /*control point 2*/
                                path.elementAt(i+2).x, path.elementAt(i+2).y); /*end point*/
            }
        }
        pathList.append(trans.map(subPath))
    }

    return pathList

def MainWindow::stub_testing():
    QMessageBox::warning(this, tr("Testing Feature"), tr("<b>This feature is in testing.</b>"))

def MainWindow::checkForUpdates():
    debug_message("checkForUpdates()")
    /*TODO: Check website for new versions, commands, etc...*/
}

def MainWindow::selectAll():
    debug_message("selectAll()")
    View* gview = activeView()
    if(gview) { gview->selectAll(); }
}

QString MainWindow::platformString():
    /*TODO: Append QSysInfo to string where applicable.*/
    QString os
    
#if defined(__unix__) || defined(__linux__)
    struct utsname unameData
    uname(&unameData)
    os = QString(unameData.sysname)
#else
    /* Get windows version. */
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
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow())
    if(mdiWin) { mdiWin->print(); }
}

def MainWindow::tipOfTheDay():
    debug_message("tipOfTheDay()")

    QString appDir = qApp->applicationDirPath()
    wizardTipOfTheDay = new QDialog()
    QToolButton *button1 = new QToolButton(wizardTipOfTheDay)
    QToolButton *button2 = new QToolButton(wizardTipOfTheDay)
    QToolButton *button3 = new QToolButton(wizardTipOfTheDay)

    ImageWidget* imgBanner = new ImageWidget(appDir + "/images/did-you-know.png", wizardTipOfTheDay)

    QCheckBox* checkBoxTipOfTheDay = new QCheckBox(tr("&Show tips on startup"), wizardTipOfTheDay)
    checkBoxTipOfTheDay->setChecked(settings.general_tip_of_the_day)
    connect(checkBoxTipOfTheDay, SIGNAL(stateChanged(int)), this, SLOT(checkBoxTipOfTheDayStateChanged(int)))

    if (strlen(tips[settings.general_current_tip])==0) {
        settings.general_current_tip = 0
    }
    labelTipOfTheDay = new QLabel(tips[settings.general_current_tip], wizardTipOfTheDay)
    labelTipOfTheDay->setWordWrap(1)

    button1->setText("&Previous")
    button2->setText("&Next")
    button3->setText("&Close")
    connect(button1, SIGNAL(triggered()), wizardTipOfTheDay, SLOT(wizardTipOfTheDay.close()))
    connect(button2, SIGNAL(triggered()), wizardTipOfTheDay, SLOT(wizardTipOfTheDay.close()))
    connect(button3, SIGNAL(triggered()), wizardTipOfTheDay, SLOT(wizardTipOfTheDay.close()))

    QVBoxLayout* layout = new QVBoxLayout(wizardTipOfTheDay)
    layout->addWidget(imgBanner)
    layout->addStrut(1)
    layout->addWidget(labelTipOfTheDay)
    layout->addStretch(1)
    layout->addWidget(checkBoxTipOfTheDay)
    layout->addStrut(1)
    layout->addWidget(button1)
    layout->addStrut(1)
    layout->addWidget(button2)
    layout->addStrut(1)
    layout->addWidget(button3)

    wizardTipOfTheDay->setLayout(layout)
    wizardTipOfTheDay->setWindowTitle("Tip of the Day")
    wizardTipOfTheDay->setMinimumSize(550, 400)
    wizardTipOfTheDay->exec()

def MainWindow::buttonTipOfTheDayClicked(int button):
    /*
    debug_message("buttonTipOfTheDayClicked(%d)", button)
    if(button == QWizard::CustomButton1)
    {
        if(settings.general_current_tip > 0)
            settings.general_current_tip--
        else
            settings.general_current_tip = listTipOfTheDay.size()-1
        labelTipOfTheDay->setText(listTipOfTheDay.value(settings.general_current_tip))
    }
    else if(button == QWizard::CustomButton2)
    {
        settings.general_current_tip++
        if(settings.general_current_tip >= listTipOfTheDay.size())
            settings.general_current_tip = 0
        labelTipOfTheDay->setText(listTipOfTheDay.value(settings.general_current_tip))
    }
    else if(button == QWizard::CustomButton3)
    {
        wizardTipOfTheDay->close()



def MainWindow::help():
    debug_message("help()")

    /* display in a custom widget instead */
    /* Open the HTML Help in the default browser
    QUrl helpURL("file:///" + qApp->applicationDirPath() + "/help/doc-index.html")
    QDesktopServices::openUrl(helpURL)
    */

    /*TODO: This is how to start an external program. Use this elsewhere...*/
    /*QString program = "firefox";*/
    /*QStringList arguments;*/
    /*arguments << "help/commands.html";*/
    /*QProcess *myProcess = new QProcess(this);*/
    /*myProcess->start(program, arguments);*/
}

/* this wrapper connects the signal to the C-style actuator */
def MainWindow::actions():
    int i
    char call[100]
    QObject *obj = sender()
    QString caller = obj->objectName()
    for (i=0; action_list[i].abbreviation[0]; i++) {
        if (caller == action_list[i].abbreviation) {
            call[0] = (char)i
            call[1] = 0
            actuator(call)
            return
        }
    }
}

def main_undo():
    debug_message("undo()")
    if (undo_history_position > 0) {
        char *last = undo_history[undo_history_position]
        undo_history_position--
        printf("undo_history_position = %d\n", undo_history_position)
        printf("undo_history_length = %d\n", undo_history_length)
        
        /* Create the reverse action from the last action and apply with
         * the main actuator.
         */
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
        /* set reverse flag */
        strcat(undo_call, " -r")
        actuator(undo_call)
    }
}

int MainWindow::isShiftPressed():
    return settings.shiftKeyPressedState

def MainWindow::setShiftPressed():
    settings.shiftKeyPressedState = 1

def MainWindow::setShiftReleased():
    settings.shiftKeyPressedState = 0

/* Icons */
def MainWindow::iconResize(int iconSize):
    this->setIconSize(QSize(iconSize, iconSize))
    layerSelector->     setIconSize(QSize(iconSize*4, iconSize))
    colorSelector->     setIconSize(QSize(iconSize, iconSize))
    linetypeSelector->  setIconSize(QSize(iconSize*4, iconSize))
    lineweightSelector->setIconSize(QSize(iconSize*4, iconSize))
    /*set the minimum combobox width so the text is always readable*/
    layerSelector->     setMinimumWidth(iconSize*4)
    colorSelector->     setMinimumWidth(iconSize*2)
    linetypeSelector->  setMinimumWidth(iconSize*4)
    lineweightSelector->setMinimumWidth(iconSize*4)

    /* TODO: low-priority:
     * open app with iconSize set to 128. resize the icons to a smaller size. */

    settings.general_icon_size = iconSize

MdiWindow* MainWindow::activeMdiWindow():
    debug_message("activeMdiWindow()")
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow())
    return mdiWin

View* MainWindow::activeView():
    debug_message("activeView()")
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow())
    if(mdiWin)
    {
        View* v = mdiWin->getView()
        return v
    }
    return 0

QGraphicsScene* MainWindow::activeScene():
    debug_message("activeScene()")
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow())
    if(mdiWin)
    {
        QGraphicsScene* s = mdiWin->getScene()
        return s
    }
    return 0

def MainWindow::updateAllViewScrollBars(int val):
    QList<QMdiSubWindow*> windowList = mdiArea->subWindowList()
    for(int i = 0; i < windowList.count(); ++i)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i))
        if(mdiWin) { mdiWin->showViewScrollBars(val); }
    }
}

def MainWindow::updateAllViewCrossHairColors(unsigned int color):
    QList<QMdiSubWindow*> windowList = mdiArea->subWindowList()
    for(int i = 0; i < windowList.count(); ++i)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i))
        if(mdiWin) { mdiWin->setViewCrossHairColor(color); }
    }
}

def MainWindow::updateAllViewBackgroundColors(unsigned int color):
    QList<QMdiSubWindow*> windowList = mdiArea->subWindowList()
    for(int i = 0; i < windowList.count(); ++i)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i))
        if(mdiWin) { mdiWin->setViewBackgroundColor(color); }
    }
}

def MainWindow::updateAllViewSelectBoxColors(unsigned int colorL, unsigned int fillL, unsigned int colorR, unsigned int fillR, int alpha):
    QList<QMdiSubWindow*> windowList = mdiArea->subWindowList()
    for(int i = 0; i < windowList.count(); ++i)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i))
        if(mdiWin) { mdiWin->setViewSelectBoxColors(colorL, fillL, colorR, fillR, alpha); }
    }
}

def MainWindow::updateAllViewGridColors(unsigned int color):
    QList<QMdiSubWindow*> windowList = mdiArea->subWindowList()
    for(int i = 0; i < windowList.count(); ++i)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i))
        if(mdiWin) { mdiWin->setViewGridColor(color); }
    }
}

def MainWindow::updateAllViewRulerColors(unsigned int color):
    QList<QMdiSubWindow*> windowList = mdiArea->subWindowList()
    for(int i = 0; i < windowList.count(); ++i)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(windowList.at(i))
        if(mdiWin) { mdiWin->setViewRulerColor(color); }
    }
}

def MainWindow::updatePickAddMode(int val):
    settings.selection_mode_pickadd = val
    dockPropEdit->updatePickAddModeButton(val)

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
        /*TODO: Handle ByLayer and ByBlock and Other...*/
        newColor = comboBox->itemData(index).toUInt(&ok)
        if(!ok)
            QMessageBox::warning(this, tr("Color Selector Conversion Error"), tr("<b>An error has occurred while changing colors.</b>"))
    }
    else
        QMessageBox::warning(this, tr("Color Selector Pointer Error"), tr("<b>An error has occurred while changing colors.</b>"))

    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow())
    if(mdiWin) { mdiWin->currentColorChanged(newColor); }
}

def MainWindow::linetypeSelectorIndexChanged(int index):
    debug_message("linetypeSelectorIndexChanged(%d)", index)

def MainWindow::lineweightSelectorIndexChanged(int index):
    debug_message("lineweightSelectorIndexChanged(%d)", index)

def MainWindow::textFontSelectorCurrentFontChanged(const QFont& font):
    debug_message("textFontSelectorCurrentFontChanged()")
    textFontSelector->setCurrentFont(QFont(font.family()))
    strcpy(settings.text_font, font.family().toLocal8Bit().constData())

def MainWindow::textSizeSelectorIndexChanged(int index):
    debug_message("textSizeSelectorIndexChanged(%d)", index)
    settings.text_style.size = fabs(textSizeSelector->itemData(index).toReal()); /*TODO: check that the toReal() conversion is ok*/
}

QString MainWindow::textFont():
    return settings.text_font

def MainWindow::setTextSize(float num):
    settings.text_style.size = fabs(num)
    int index = textSizeSelector->findText("Custom", Qt::MatchContains)
    if(index != -1)
        textSizeSelector->removeItem(index)
    textSizeSelector->addItem("Custom " + QString().setNum(num, 'f', 2) + " pt", num)
    index = textSizeSelector->findText("Custom", Qt::MatchContains)
    if(index != -1)
        textSizeSelector->setCurrentIndex(index)

QString MainWindow::getCurrentLayer():
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow())
    if(mdiWin) { return mdiWin->getCurrentLayer(); }
    return "0"

unsigned int MainWindow::getCurrentColor():
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow())
    if(mdiWin) { return mdiWin->getCurrentColor(); }
    return 0; /*TODO: return color ByLayer*/
}

QString MainWindow::getCurrentLineType():
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow())
    if(mdiWin) { return mdiWin->getCurrentLineType(); }
    return "ByLayer"

QString MainWindow::getCurrentLineWeight():
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow())
    if(mdiWin) { return mdiWin->getCurrentLineWeight(); }
    return "ByLayer"

def MainWindow::deletePressed():
    debug_message("deletePressed()")
    QApplication::setOverrideCursor(Qt::WaitCursor)
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow())
    if(mdiWin) { mdiWin->deletePressed(); }
    QApplication::restoreOverrideCursor()

def MainWindow::escapePressed():
    debug_message("escapePressed()")
    QApplication::setOverrideCursor(Qt::WaitCursor)
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow())
    if(mdiWin) { mdiWin->escapePressed(); }
    QApplication::restoreOverrideCursor()

    View* gview = activeView()
    if(gview)
    {
        gview->clearRubberRoom()
        gview->previewOff()
        gview->disableMoveRapidFire()
    }
}

def toggleGrid():
    debug_message("toggleGrid()")
    status_bar[STATUS_GRID]->toggle()

def toggleRuler():
    debug_message("toggleRuler()")
    status_bar[STATUS_RULER]->toggle()

def toggleLwt():
    debug_message("toggleLwt()")
    status_bar[STATUS_LWT]->toggle()

def MainWindow::enableMoveRapidFire():
    View* gview = activeView()
    if (gview) gview->enableMoveRapidFire()

def MainWindow::disableMoveRapidFire():
    View* gview = activeView()
    if(gview) gview->disableMoveRapidFire()

def MainWindow::nativeAddTextSingle(const QString& str, float x, float y, float rot, int fill, int rubberMode):
    View* gview = activeView()
    QGraphicsScene* gscene = gview->scene()
    if(gview && gscene)
    {
        TextSingleObject* obj = new TextSingleObject(str, x, -y, getCurrentColor())
        obj->objTextFont = settings.text_font
        obj->obj_text = settings.text_style
        obj->setObjectText(obj->objText)
        obj->setRotation(-rot)
        /*TODO: single line text fill*/
        obj->setObjectRubberMode(rubberMode)
        if (rubberMode) {
            gview->addToRubberRoom(obj)
            gscene->addItem(obj)
            gscene->update()
        }
        else {
        }
    }
}

def MainWindow::nativeAddLine(float x1, float y1, float x2, float y2, float rot, int rubberMode):
    View* gview = activeView()
    QGraphicsScene* gscene = gview->scene()
    if(gview && gscene)
    {
        LineObject* obj = new LineObject(x1, -y1, x2, -y2, getCurrentColor())
        obj->setRotation(-rot)
        obj->setObjectRubberMode(rubberMode)
        if(rubberMode)
        {
            gview->addToRubberRoom(obj)
            gscene->addItem(obj)
            gscene->update()
        }
        else
        {
        }
    }
}

def MainWindow::nativeAddRectangle(float x, float y, float w, float h, float rot, int fill, int rubberMode):
    View* gview = activeView()
    QGraphicsScene* gscene = gview->scene()
    if(gview && gscene)
    {
        RectObject* obj = new RectObject(x, -y, w, -h, getCurrentColor())
        obj->setRotation(-rot)
        obj->setObjectRubberMode(rubberMode)
        /*TODO: rect fill*/
        if (rubberMode) {
            gview->addToRubberRoom(obj)
            gscene->addItem(obj)
            gscene->update()
        }
        else {
        }
    }
}

def MainWindow::nativeAddArc(float startX, float startY, float midX, float midY, float endX, float endY, int rubberMode):
    View* gview = activeView()
    QGraphicsScene* scene = activeScene()
    if(gview && scene)
    {
        ArcObject* arcObj = new ArcObject(startX, -startY, midX, -midY, endX, -endY, getCurrentColor())
        arcObj->setObjectRubberMode(rubberMode)
        if(rubberMode) gview->addToRubberRoom(arcObj)
        scene->addItem(arcObj)
        scene->update()
    }
}

def MainWindow::nativeAddCircle(float centerX, float centerY, float radius, int fill, int rubberMode):
    View* gview = activeView()
    QGraphicsScene* gscene = gview->scene()
    if (gview && gscene) {
        CircleObject* obj = new CircleObject(centerX, -centerY, radius, getCurrentColor())
        obj->setObjectRubberMode(rubberMode)
        /*TODO: circle fill*/
        if(rubberMode)
        {
            gview->addToRubberRoom(obj)
            gscene->addItem(obj)
            gscene->update()
        }
        else
        {
        }
    }
}

def MainWindow::nativeAddEllipse(float centerX, float centerY, float width, float height, float rot, int fill, int rubberMode):
    View* gview = activeView()
    QGraphicsScene* gscene = gview->scene()
    if (gview && gscene) {
        EllipseObject* obj = new EllipseObject(centerX, -centerY, width, height, getCurrentColor())
        obj->setRotation(-rot)
        obj->setObjectRubberMode(rubberMode)
        /*TODO: ellipse fill*/
        if(rubberMode)
        {
            gview->addToRubberRoom(obj)
            gscene->addItem(obj)
            gscene->update()
        }
        else
        {
        }
    }
}

def MainWindow::nativeAddPoint(float x, float y):
    View* gview = activeView()
    if (gview) {
        PointObject* obj = new PointObject(x, -y, getCurrentColor())
    }
}

/*NOTE: This native is different than the rest in that the Y+ is down (scripters need not worry about this)*/
def MainWindow::nativeAddPolygon(float startX, float startY, const QPainterPath& p, int rubberMode):
    View* gview = activeView()
    QGraphicsScene* gscene = gview->scene()
    if (gview && gscene) {
        PolygonObject* obj = new PolygonObject(startX, startY, p, getCurrentColor())
        obj->setObjectRubberMode(rubberMode)
        if(rubberMode)
        {
            gview->addToRubberRoom(obj)
            gscene->addItem(obj)
            gscene->update()
        }
        else
        {
        }
    }
}

/*NOTE: This native is different than the rest in that the Y+ is down (scripters need not worry about this)*/
def MainWindow::nativeAddPolyline(float startX, float startY, const QPainterPath& p, int rubberMode):
    View* gview = activeView()
    QGraphicsScene* gscene = gview->scene()
    if(gview && gscene)
    {
        PolylineObject* obj = new PolylineObject(startX, startY, p, getCurrentColor())
        obj->setObjectRubberMode(rubberMode)
        if(rubberMode)
        {
            gview->addToRubberRoom(obj)
            gscene->addItem(obj)
            gscene->update()
        }
        else
        {
        }
    }
}

def MainWindow::nativeAddDimLeader(float x1, float y1, float x2, float y2, float rot, int rubberMode):
    View* gview = activeView()
    QGraphicsScene* gscene = gview->scene()
    if(gview && gscene) {
        DimLeaderObject* obj = new DimLeaderObject(x1, -y1, x2, -y2, getCurrentColor())
        obj->setRotation(-rot)
        obj->setObjectRubberMode(rubberMode)
        if(rubberMode)
        {
            gview->addToRubberRoom(obj)
            gscene->addItem(obj)
            gscene->update()
        }
        else
        {
        }
    }
}

float MainWindow::nativeCalculateAngle(float x1, float y1, float x2, float y2):
    return QLineF(x1, -y1, x2, -y2).angle()

float MainWindow::nativeCalculateDistance(float x1, float y1, float x2, float y2):
    return QLineF(x1, y1, x2, y2).length()

def MainWindow::fill_menu(int menu_id):
    int i
    debug_message("MainWindow creating %s", menu_label[menu_id])
    menuBar()->addMenu(menu[menu_id])
    for (i=0; menus[menu_id][i]>=-1; i++) {
        if (menus[menu_id][i] >= 0) {
            menu[menu_id]->addAction(actionHash.value(menus[menu_id][i]))
        }
        else {
            menu[menu_id]->addSeparator()
        }
    }
}

/* nativePerpendicularDistance
    This is currently causing a bug and is going to be replaced with a libembroidery function.
    QLineF line(x1, y1, x2, y2)
    QLineF norm = line.normalVector()
    float dx = px-x1
    float dy = py-y1
    norm.translate(dx, dy)
    QPointF iPoint
    norm.intersects(line, &iPoint)
    return QLineF(px, py, iPoint.x(), iPoint.y()).length()
*/

MainWindow::MainWindow() : QMainWindow(0):
    char current_path[1000]
    int i

    QString appDir = qApp->applicationDirPath()
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

    /*Load translations for the Embroidermodder 2 GUI*/
    QTranslator translatorEmb
    app_dir(current_path, translations_folder)
    translatorEmb.load(QString(current_path) + "/embroidermodder2_" + lang)
    qApp->installTranslator(&translatorEmb)

    /*Load translations for the commands*/
    QTranslator translatorCmd
    translatorCmd.load(QDir::toNativeSeparators(QString(current_path) + lang + "/commands_" + lang))
    qApp->installTranslator(&translatorCmd)

    /*Load translations provided by Qt - this covers dialog buttons and other common things.*/
    QTranslator translatorQt
    translatorQt.load("qt_" + QLocale::system().name(), QLibraryInfo::location(QLibraryInfo::TranslationsPath)); /*TODO: ensure this always loads, ship a copy of this with the app*/
    qApp->installTranslator(&translatorQt)

    /*Init*/
    mainWin = this
    for (i=0; i<N_MENUS; i++) {
        menu[i] = new QMenu(tr(menu_label[i]), this)
    }
    for (i=0; i<N_TOOLBARS; i++) {
        toolbar[i] = addToolBar(tr(toolbar_label[i]))
    }
    /*Selectors*/
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
    setMinimumSize(800, 480); /*Require Minimum WVGA*/

    loadFormats()

    /*create the mdiArea*/
    QFrame* vbox = new QFrame(this)
    QVBoxLayout* layout = new QVBoxLayout(vbox)
    layout->setContentsMargins(QMargins())
    vbox->setFrameStyle(QFrame::StyledPanel | QFrame::Sunken)
    mdiArea = new MdiArea(this, vbox)
    mdiArea->useBackgroundLogo(settings.general_mdi_bg_use_logo)
    mdiArea->useBackgroundTexture(settings.general_mdi_bg_use_texture)
    mdiArea->useBackgroundColor(settings.general_mdi_bg_use_color)
    mdiArea->setBackgroundLogo(settings.general_mdi_bg_logo)
    mdiArea->setBackgroundTexture(settings.general_mdi_bg_texture)
    mdiArea->setBackgroundColor(QColor(settings.general_mdi_bg_color))
    mdiArea->setViewMode(QMdiArea::TabbedView)
    mdiArea->setHorizontalScrollBarPolicy(Qt::ScrollBarAsNeeded)
    mdiArea->setVerticalScrollBarPolicy(Qt::ScrollBarAsNeeded)
    mdiArea->setActivationOrder(QMdiArea::ActivationHistoryOrder)
    layout->addWidget(mdiArea)
    setCentralWidget(vbox)

    /*setDockOptions(QMainWindow::AnimatedDocks | QMainWindow::AllowTabbedDocks | QMainWindow::VerticalTabs);*/
    /* TODO: Load these from settings */
    /* tabifyDockWidget(dockPropEdit, dockUndoEdit); */
    /* TODO: load this from settings */

    statusbar = new StatusBar(this, this)
    this->setStatusBar(statusbar)

    debug_message("Creating All Actions...")
    QString appName = QApplication::applicationName()

    for (i=0; action_list[i].abbreviation[0]; i++) {
        QAction *ACTION = new QAction(loadIcon((*)action_list[i].icon), action_list[i].menu_name, this)
        /* TODO: Set What's This Context Help to statusTip for now so there is some infos there.*/
        /* Make custom What's This Context Help popup with more descriptive help than just*/
        /* the status bar/tip one liner(short but not real long) with a hyperlink in the custom popup*/
        /* at the bottom to open full help file description. Ex: like wxPython AGW's SuperToolTip.*/
        /* TODO: Finish All Commands ... <.<*/

        /*
        if(icon == "windowcascade") {
            connect(ACTION, SIGNAL(triggered()), mdiArea, SLOT(cascade()))
        }
        else if(icon == "windowtile") {
            connect(ACTION, SIGNAL(triggered()), mdiArea, SLOT(tile()))
        }
        else if(icon == "windowclose") {
            ACTION->setShortcut(QKeySequence::Close)
            connect(ACTION, SIGNAL(triggered()), this, SLOT(onCloseWindow()))
        }
        else if(icon == "windowcloseall") {
            connect(ACTION, SIGNAL(triggered()), mdiArea, SLOT(closeAllSubWindows()))
        }
        else if(icon == "windownext") {
            connect(ACTION, SIGNAL(triggered()), mdiArea, SLOT(activateNextSubWindow()))
        }
        else if(icon == "windowprevious") {
            connect(ACTION, SIGNAL(triggered()), mdiArea, SLOT(activatePreviousSubWindow()))
        }
        else if(icon == "textbold" || icon == "textitalic"
            || icon == "textunderline" || icon == "textstrikeout"
            || icon == "textoverline") {
            ACTION->setCheckable(1)
        }
        */

        if (strlen(action_list[i].shortcut)>0) {
            ACTION->setShortcut(QKeySequence(action_list[i].shortcut))
        }
        ACTION->setStatusTip(action_list[i].description)
        ACTION->setObjectName(action_list[i].abbreviation)
        ACTION->setWhatsThis(action_list[i].description)
        connect(ACTION, SIGNAL(triggered()), this, SLOT(actions()))
        actionHash.insert(i, ACTION)
    }

    actionHash.value(ACTION_windowclose)->setEnabled(numOfDocs > 0)
    actionHash.value(ACTION_designdetails)->setEnabled(numOfDocs > 0)

    /* ---------------------------------------------------------------------- */

    debug_message("MainWindow createAllMenus()")
    
    debug_message("MainWindow createFileMenu()")
    menuBar()->addMenu(menu[FILE_MENU])
    menu[FILE_MENU]->addAction(actionHash.value(ACTION_new))
    menu[FILE_MENU]->addSeparator()
    menu[FILE_MENU]->addAction(actionHash.value(ACTION_open))

    menu[FILE_MENU]->addMenu(menu[RECENT_MENU])
    connect(menu[RECENT_MENU], SIGNAL(aboutToShow()), this, SLOT(recentMenuAboutToShow()))
    /* Do not allow the Recent Menu to be torn off. It's a pain in the ass to maintain. */
    menu[RECENT_MENU]->setTearOffEnabled(0)

    menu[FILE_MENU]->addSeparator()
    menu[FILE_MENU]->addAction(actionHash.value(ACTION_save))
    menu[FILE_MENU]->addAction(actionHash.value(ACTION_saveas))
    menu[FILE_MENU]->addSeparator()
    menu[FILE_MENU]->addAction(actionHash.value(ACTION_print))
    menu[FILE_MENU]->addSeparator()
    menu[FILE_MENU]->addAction(actionHash.value(ACTION_windowclose))
    menu[FILE_MENU]->addSeparator()
    menu[FILE_MENU]->addAction(actionHash.value(ACTION_designdetails))
    menu[FILE_MENU]->addSeparator()

    menu[FILE_MENU]->addAction(actionHash.value(ACTION_exit))
    menu[FILE_MENU]->setTearOffEnabled(0)

    /* ---------------------------------------------------------------------- */

    debug_message("MainWindow createmenu[EDIT_MENU]()")
    menuBar()->addMenu(menu[EDIT_MENU])
    menu[EDIT_MENU]->addAction(actionHash.value(ACTION_undo))
    menu[EDIT_MENU]->addAction(actionHash.value(ACTION_redo))
    menu[EDIT_MENU]->addSeparator()
    menu[EDIT_MENU]->addAction(actionHash.value(ACTION_cut))
    menu[EDIT_MENU]->addAction(actionHash.value(ACTION_copy))
    menu[EDIT_MENU]->addAction(actionHash.value(ACTION_paste))
    menu[EDIT_MENU]->addSeparator()
    menu[EDIT_MENU]->setTearOffEnabled(1)

    /* ---------------------------------------------------------------------- */

    debug_message("MainWindow createmenu[VIEW_MENU]()")

    menuBar()->addMenu(menu[VIEW_MENU])
    menu[VIEW_MENU]->addSeparator()
    menu[VIEW_MENU]->addMenu(menu[ZOOM_MENU])
    menu[ZOOM_MENU]->setIcon(loadIcon(zoom_xpm))
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomrealtime))
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomprevious))
    menu[ZOOM_MENU]->addSeparator()
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomwindow))
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomdynamic))
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomscale))
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomcenter))
    menu[ZOOM_MENU]->addSeparator()
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomin))
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomout))
    menu[ZOOM_MENU]->addSeparator()
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomselected))
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomall))
    menu[ZOOM_MENU]->addAction(actionHash.value(ACTION_zoomextents))
    menu[VIEW_MENU]->addMenu(menu[PAN_MENU])
    menu[PAN_MENU]->setIcon(loadIcon(pan_xpm))
    menu[PAN_MENU]->addAction(actionHash.value(ACTION_panrealtime))
    menu[PAN_MENU]->addAction(actionHash.value(ACTION_panpoint))
    menu[PAN_MENU]->addSeparator()
    menu[PAN_MENU]->addAction(actionHash.value(ACTION_panleft))
    menu[PAN_MENU]->addAction(actionHash.value(ACTION_panright))
    menu[PAN_MENU]->addAction(actionHash.value(ACTION_panup))
    menu[PAN_MENU]->addAction(actionHash.value(ACTION_pandown))
    menu[VIEW_MENU]->addSeparator()
    menu[VIEW_MENU]->addAction(actionHash.value(ACTION_day))
    menu[VIEW_MENU]->addAction(actionHash.value(ACTION_night))
    menu[VIEW_MENU]->addSeparator()

    menu[VIEW_MENU]->setTearOffEnabled(1)
    menu[ZOOM_MENU]->setTearOffEnabled(1)
    menu[PAN_MENU]->setTearOffEnabled(1)

    /* ---------------------------------------------------------------------- */

    debug_message("MainWindow createSettingsMenu()")
    menuBar()->addMenu(menu[SETTINGS_MENU])
    menu[SETTINGS_MENU]->addAction(actionHash.value(ACTION_settingsdialog))
    menu[SETTINGS_MENU]->addSeparator()
    menu[SETTINGS_MENU]->setTearOffEnabled(1)

    /* ---------------------------------------------------------------------- */

    debug_message("MainWindow createWindowMenu()")
    menuBar()->addMenu(menu[WINDOW_MENU])
    connect(menu[WINDOW_MENU], SIGNAL(aboutToShow()), this, SLOT(windowMenuAboutToShow()))
    /*Do not allow the Window Menu to be torn off. It's a pain in the ass to maintain.*/
    menu[WINDOW_MENU]->setTearOffEnabled(0)

    /* ---------------------------------------------------------------------- */

    debug_message("MainWindow createHelpMenu()")
    menuBar()->addMenu(menu[HELP_MENU])
    menu[HELP_MENU]->addAction(actionHash.value(ACTION_help))
    menu[HELP_MENU]->addSeparator()
    menu[HELP_MENU]->addAction(actionHash.value(ACTION_changelog))
    menu[HELP_MENU]->addSeparator()
    menu[HELP_MENU]->addAction(actionHash.value(ACTION_tipoftheday))
    menu[HELP_MENU]->addSeparator()
    menu[HELP_MENU]->addAction(actionHash.value(ACTION_about))
    menu[HELP_MENU]->addSeparator()
    menu[HELP_MENU]->addAction(actionHash.value(ACTION_whatsthis))
    menu[HELP_MENU]->setTearOffEnabled(1)

    /* ---------------------------------------------------------------------- */

    debug_message("MainWindow createAllToolbars()")

    for (i=0; i<N_TOOLBARS; i++) {
        int j
        char message[100]
        sprintf(message, "MainWindow creating %s\n", toolbar_label[i])
        debug_message(message)

        toolbar[i]->setObjectName(toolbar_label[i])

        for (j=0; toolbars[i][j]!=-2; j++) {
            if (toolbars[i][j] >= 0) {
                toolbar[i]->addAction(actionHash.value(toolbars[i][j]))
            }
            else {
                toolbar[i]->addSeparator()
            }
        }

        connect(toolbar[i], SIGNAL(topLevelChanged(int)), this, SLOT(floatingChangedToolBar(int)))
    }

    /* ---------------------------------------------------------------- */
    
    debug_message("MainWindow createLayerToolbar()")

    toolbar[TOOLBAR_LAYER]->setObjectName("toolbarLayer")
    toolbar[TOOLBAR_LAYER]->addAction(actionHash.value(ACTION_makelayercurrent))
    toolbar[TOOLBAR_LAYER]->addAction(actionHash.value(ACTION_layers))

    /*NOTE: Qt4.7 wont load icons without an extension...*/
    /*TODO: Create layer pixmaps by concatenating several icons*/
    layerSelector->addItem(loadIcon(linetypebylayer_xpm), "0")
    layerSelector->addItem(loadIcon(linetypebylayer_xpm), "1")
    layerSelector->addItem(loadIcon(linetypebylayer_xpm), "2")
    layerSelector->addItem(loadIcon(linetypebylayer_xpm), "3")
    layerSelector->addItem(loadIcon(linetypebylayer_xpm), "4")
    layerSelector->addItem(loadIcon(linetypebylayer_xpm), "5")
    layerSelector->addItem(loadIcon(linetypebylayer_xpm), "6")
    layerSelector->addItem(loadIcon(linetypebylayer_xpm), "7")
    layerSelector->addItem(loadIcon(linetypebylayer_xpm), "8")
    layerSelector->addItem(loadIcon(linetypebylayer_xpm), "9")
    toolbar[TOOLBAR_LAYER]->addWidget(layerSelector)
    connect(layerSelector, SIGNAL(currentIndexChanged(int)), this, SLOT(layerSelectorIndexChanged(int)))

    toolbar[TOOLBAR_LAYER]->addAction(actionHash.value(ACTION_layerprevious))

    connect(toolbar[TOOLBAR_LAYER], SIGNAL(topLevelChanged(int)), this, SLOT(floatingChangedToolBar(int)))
    
    /* ----------------- */

    debug_message("MainWindow createPropertiesToolbar()")

    toolbar[TOOLBAR_PROPERTIES]->setObjectName("toolbarProperties")

    colorSelector->setFocusProxy(menu[FILE_MENU])
    /*NOTE: Qt4.7 wont load icons without an extension...*/
    colorSelector->addItem(loadIcon(colorbylayer_xpm), "ByLayer")
    colorSelector->addItem(loadIcon(colorbyblock_xpm), "ByBlock")
    colorSelector->addItem(loadIcon(colorred_xpm), tr("Red"), qRgb(255, 0, 0))
    colorSelector->addItem(loadIcon(coloryellow_xpm), tr("Yellow"), qRgb(255,255, 0))
    colorSelector->addItem(loadIcon(colorgreen_xpm), tr("Green"), qRgb(0, 255, 0))
    colorSelector->addItem(loadIcon(colorcyan_xpm), tr("Cyan"), qRgb(  0,255,255))
    colorSelector->addItem(loadIcon(colorblue_xpm), tr("Blue"), qRgb(  0, 0,255))
    colorSelector->addItem(loadIcon(colormagenta_xpm), tr("Magenta"), qRgb(255, 0,255))
    colorSelector->addItem(loadIcon(colorwhite_xpm), tr("White"), qRgb(255,255,255))
    colorSelector->addItem(loadIcon(colorother_xpm), tr("Other..."))
    toolbar[TOOLBAR_PROPERTIES]->addWidget(colorSelector)
    connect(colorSelector, SIGNAL(currentIndexChanged(int)), this, SLOT(colorSelectorIndexChanged(int)))

    toolbar[TOOLBAR_PROPERTIES]->addSeparator()
    linetypeSelector->setFocusProxy(menu[FILE_MENU])
    /*NOTE: Qt4.7 wont load icons without an extension...*/
    linetypeSelector->addItem(loadIcon(linetypebylayer_xpm), "ByLayer")
    linetypeSelector->addItem(loadIcon(linetypebyblock_xpm), "ByBlock")
    linetypeSelector->addItem(loadIcon(linetypecontinuous_xpm), "Continuous")
    linetypeSelector->addItem(loadIcon(linetypehidden_xpm), "Hidden")
    linetypeSelector->addItem(loadIcon(linetypecenter_xpm), "Center")
    linetypeSelector->addItem(loadIcon(linetypeother_xpm), "Other...")
    toolbar[TOOLBAR_PROPERTIES]->addWidget(linetypeSelector)
    connect(linetypeSelector, SIGNAL(currentIndexChanged(int)), this, SLOT(linetypeSelectorIndexChanged(int)))

    toolbar[TOOLBAR_PROPERTIES]->addSeparator()
    lineweightSelector->setFocusProxy(menu[FILE_MENU])
    /*NOTE: Qt4.7 wont load icons without an extension...*/
    lineweightSelector->addItem(loadIcon(lineweightbylayer_xpm), "ByLayer", -2.00)
    lineweightSelector->addItem(loadIcon(lineweightbyblock_xpm), "ByBlock", -1.00)
    lineweightSelector->addItem(loadIcon(lineweightdefault_xpm), "Default", 0.00)
    /* TODO: Thread weight is weird. See http://en.wikipedia.org/wiki/Thread_(yarn)#Weight */
    lineweightSelector->addItem(loadIcon(lineweight01_xpm), "0.00 mm", 0.00)
    lineweightSelector->addItem(loadIcon(lineweight02_xpm), "0.05 mm", 0.05)
    lineweightSelector->addItem(loadIcon(lineweight03_xpm), "0.15 mm", 0.15)
    lineweightSelector->addItem(loadIcon(lineweight04_xpm), "0.20 mm", 0.20)
    lineweightSelector->addItem(loadIcon(lineweight05_xpm), "0.25 mm", 0.25)
    lineweightSelector->addItem(loadIcon(lineweight06_xpm), "0.30 mm", 0.30)
    lineweightSelector->addItem(loadIcon(lineweight07_xpm), "0.35 mm", 0.35)
    lineweightSelector->addItem(loadIcon(lineweight08_xpm), "0.40 mm", 0.40)
    lineweightSelector->addItem(loadIcon(lineweight09_xpm), "0.45 mm", 0.45)
    lineweightSelector->addItem(loadIcon(lineweight10_xpm), "0.50 mm", 0.50)
    lineweightSelector->addItem(loadIcon(lineweight11_xpm), "0.55 mm", 0.55)
    lineweightSelector->addItem(loadIcon(lineweight12_xpm), "0.60 mm", 0.60)
    lineweightSelector->addItem(loadIcon(lineweight13_xpm), "0.65 mm", 0.65)
    lineweightSelector->addItem(loadIcon(lineweight14_xpm), "0.70 mm", 0.70)
    lineweightSelector->addItem(loadIcon(lineweight15_xpm), "0.75 mm", 0.75)
    lineweightSelector->addItem(loadIcon(lineweight16_xpm), "0.80 mm", 0.80)
    lineweightSelector->addItem(loadIcon(lineweight17_xpm), "0.85 mm", 0.85)
    lineweightSelector->addItem(loadIcon(lineweight18_xpm), "0.90 mm", 0.90)
    lineweightSelector->addItem(loadIcon(lineweight19_xpm), "0.95 mm", 0.95)
    lineweightSelector->addItem(loadIcon(lineweight20_xpm), "1.00 mm", 1.00)
    lineweightSelector->addItem(loadIcon(lineweight21_xpm), "1.05 mm", 1.05)
    lineweightSelector->addItem(loadIcon(lineweight22_xpm), "1.10 mm", 1.10)
    lineweightSelector->addItem(loadIcon(lineweight23_xpm), "1.15 mm", 1.15)
    lineweightSelector->addItem(loadIcon(lineweight24_xpm), "1.20 mm", 1.20)
    lineweightSelector->setMinimumContentsLength(8)
    /* Prevent dropdown text readability being squish...d. */
    toolbar[TOOLBAR_PROPERTIES]->addWidget(lineweightSelector)
    connect(lineweightSelector, SIGNAL(currentIndexChanged(int)), this, SLOT(lineweightSelectorIndexChanged(int)))

    connect(toolbar[TOOLBAR_PROPERTIES], SIGNAL(topLevelChanged(int)), this, SLOT(floatingChangedToolBar(int)))

    /* ------------------------------------------------------------- */

    debug_message("MainWindow createTextToolbar()")

    toolbar[TOOLBAR_TEXT]->setObjectName("toolbarText")

    toolbar[TOOLBAR_TEXT]->addWidget(textFontSelector)
    textFontSelector->setCurrentFont(QFont(settings.text_font))
    connect(textFontSelector, SIGNAL(currentFontChanged(const QFont&)), this, SLOT(textFontSelectorCurrentFontChanged(const QFont&)))

/* TODO: SEGFAULTING FOR SOME REASON 
    toolbar[TOOLBAR_TEXT]->addAction(actionHash.value(ACTION_textbold))
    actionHash.value(ACTION_textbold)->setChecked(settings.text_style_bold)
    toolbar[TOOLBAR_TEXT]->addAction(actionHash.value(ACTION_textitalic))
    actionHash.value(ACTION_textitalic)->setChecked(settings.text_style_italic)
    toolbar[TOOLBAR_TEXT]->addAction(actionHash.value(ACTION_textunderline))
    actionHash.value(ACTION_textunderline)->setChecked(settings.text_style_underline)
    toolbar[TOOLBAR_TEXT]->addAction(actionHash.value(ACTION_textstrikeout))
    actionHash.value(ACTION_textstrikeout)->setChecked(settings.text_style_strikeout)
    toolbar[TOOLBAR_TEXT]->addAction(actionHash.value(ACTION_textoverline))
    actionHash.value(ACTION_textoverline)->setChecked(settings.text_style_overline)

    textSizeSelector->setFocusProxy(menu[FILE_MENU])
    textSizeSelector->addItem("6 pt", 6)
    textSizeSelector->addItem("8 pt", 8)
    textSizeSelector->addItem("9 pt", 9)
    textSizeSelector->addItem("10 pt", 10)
    textSizeSelector->addItem("11 pt", 11)
    textSizeSelector->addItem("12 pt", 12)
    textSizeSelector->addItem("14 pt", 14)
    textSizeSelector->addItem("18 pt", 18)
    textSizeSelector->addItem("24 pt", 24)
    textSizeSelector->addItem("30 pt", 30)
    textSizeSelector->addItem("36 pt", 36)
    textSizeSelector->addItem("48 pt", 48)
    textSizeSelector->addItem("60 pt", 60)
    textSizeSelector->addItem("72 pt", 72)
    setTextSize(settings.text_size)
    toolbar[TOOLBAR_TEXT]->addWidget(textSizeSelector)
    connect(textSizeSelector, SIGNAL(currentIndexChanged(int)), this, SLOT(textSizeSelectorIndexChanged(int)))
    */

    connect(toolbar[TOOLBAR_TEXT], SIGNAL(topLevelChanged(int)), this, SLOT(floatingChangedToolBar(int)))

    /* ------------------------------------------------------------ */

    /* Horizontal*/
    toolbar[TOOLBAR_VIEW]->setOrientation(Qt::Horizontal)
    toolbar[TOOLBAR_ZOOM]->setOrientation(Qt::Horizontal)
    toolbar[TOOLBAR_LAYER]->setOrientation(Qt::Horizontal)
    toolbar[TOOLBAR_PROPERTIES]->setOrientation(Qt::Horizontal)
    toolbar[TOOLBAR_TEXT]->setOrientation(Qt::Horizontal)
    /* Top*/
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

    /*zoomToolBar->setToolButtonStyle(Qt::ToolButtonTextOnly);*/
    /* ---------------------------------------------------------------------- */

    iconResize(settings.general_icon_size)
    updateMenuToolbarStatusbar()

    /* Show date in statusbar after it has been updated
     * TODO: Switch to ISO dates.
     */
    QDate date = QDate::currentDate()
    QString datestr = date.toString("MMMM d, yyyy")
    statusbar->showMessage(datestr)

    showNormal()

    if (settings.general_tip_of_the_day) {
        tipOfTheDay()
    }
}

MainWindow::~MainWindow():
    debug_message("MainWindow::Destructor()")

    /*Prevent memory leaks by deleting any unpasted objects*/
    qDeleteAll(cutCopyObjectList.begin(), cutCopyObjectList.end())
    cutCopyObjectList.clear()

def MainWindow::recentMenuAboutToShow():
    debug_message("MainWindow::recentMenuAboutToShow()")
    menu[RECENT_MENU]->clear()

    QFileInfo recentFileInfo
    QString recentValue
    for(int i = 0; i < opensave_recent_list_of_files.size(); ++i)
    {
        /*If less than the max amount of entries add to menu*/
        if(i < settings.opensave_recent_max_files)
        {
            recentFileInfo = QFileInfo(opensave_recent_list_of_files.at(i))
            if(recentFileInfo.exists() && validFileFormat(recentFileInfo.fileName()))
            {
                recentValue.setNum(i+1)
                QAction* rAction
                if     (recentValue.toInt() >= 1 && recentValue.toInt() <= 9) rAction = new QAction("&" + recentValue + " " + recentFileInfo.fileName(), this)
                else if(recentValue.toInt() == 10)                            rAction = new QAction("1&0 "                  + recentFileInfo.fileName(), this)
                else                                                          rAction = new QAction(      recentValue + " " + recentFileInfo.fileName(), this)
                rAction->setCheckable(0)
                rAction->setData(opensave_recent_list_of_files.at(i))
                menu[RECENT_MENU]->addAction(rAction)
                connect(rAction, SIGNAL(triggered()), this, SLOT(openrecentfile()))
            }
        }
    }
    /*Ensure the list only has max amount of entries*/
    while(opensave_recent_list_of_files.size() > settings.opensave_recent_max_files) {
        opensave_recent_list_of_files.removeLast()
    }
}

def MainWindow::windowMenuAboutToShow():
    debug_message("MainWindow::windowMenuAboutToShow()")
    menu[WINDOW_MENU]->clear()
    menu[WINDOW_MENU]->addAction(actionHash.value(ACTION_windowclose))
    menu[WINDOW_MENU]->addAction(actionHash.value(ACTION_windowcloseall))
    menu[WINDOW_MENU]->addSeparator()
    menu[WINDOW_MENU]->addAction(actionHash.value(ACTION_windowcascade))
    menu[WINDOW_MENU]->addAction(actionHash.value(ACTION_windowtile))
    menu[WINDOW_MENU]->addSeparator()
    menu[WINDOW_MENU]->addAction(actionHash.value(ACTION_windownext))
    menu[WINDOW_MENU]->addAction(actionHash.value(ACTION_windowprevious))

    menu[WINDOW_MENU]->addSeparator()
    QList<QMdiSubWindow*> windows = mdiArea->subWindowList()
    for(int i = 0; i < windows.count(); ++i)
    {
        QAction* aAction = new QAction(windows.at(i)->windowTitle(), this)
        aAction->setCheckable(1)
        aAction->setData(i)
        menu[WINDOW_MENU]->addAction(aAction)
        connect(aAction, SIGNAL(toggled(int)), this, SLOT(windowMenuActivated(int)))
        aAction->setChecked(mdiArea->activeSubWindow() == windows.at(i))
    }
}

def MainWindow::windowMenuActivated(int checked):
    debug_message("MainWindow::windowMenuActivated()")
    QAction* aSender = qobject_cast<QAction*>(sender())
    if(!aSender)
        return
    QWidget* w = mdiArea->subWindowList().at(aSender->data().toInt())
    if(w && checked)
        w->setFocus()

def MainWindow::newFile():
    debug_message("MainWindow::newFile()")
    docIndex++
    numOfDocs++
    MdiWindow* mdiWin = new MdiWindow(docIndex, mainWin, mdiArea, Qt::SubWindow)
    connect(mdiWin, SIGNAL(sendCloseMdiWin(MdiWindow*)), this, SLOT(onCloseMdiWin(MdiWindow*)))
    connect(mdiArea, SIGNAL(subWindowActivated(QMdiSubWindow*)), this, SLOT(onWindowActivated(QMdiSubWindow*)))

    updateMenuToolbarStatusbar()
    windowMenuAboutToShow()

    View* v = mdiWin->getView()
    if(v)
    {
        v->recalculateLimits()
        v->zoomExtents()
    }
}

def MainWindow::openFile(int recent, const QString& recentFile):
    debug_message("MainWindow::openFile()")

    QApplication::setOverrideCursor(Qt::ArrowCursor)

    QStringList files
    int preview = settings.opensave_open_thumbnail
    openFilesPath = settings.opensave_recent_directory

    /*Check to see if this from the recent files list*/
    if(recent)
    {
        files.append(recentFile)
        openFilesSelected(files)
    }
    else if(!preview)
    {
        /*TODO: set getOpenFileNames' selectedFilter parameter from settings.opensave_open_format*/
        files = QFileDialog::getOpenFileNames(this, tr("Open"), openFilesPath, formatFilterOpen)
        openFilesSelected(files)
    }
    else if(preview)
    {
        PreviewDialog* openDialog = new PreviewDialog(this, tr("Open w/Preview"), openFilesPath, formatFilterOpen)
        /*TODO: set openDialog->selectNameFilter(const QString& filter) from settings.opensave_open_format*/
        connect(openDialog, SIGNAL(filesSelected(const QStringList&)), this, SLOT(openFilesSelected(const QStringList&)))
        openDialog->exec()
    }

    QApplication::restoreOverrideCursor()

def MainWindow::openFilesSelected(const QStringList& filesToOpen):
    int doOnce = 1

    if(filesToOpen.count())
    {
        for(int i = 0; i < filesToOpen.count(); i++)
        {
            if(!validFileFormat(filesToOpen[i]))
                continue

            QMdiSubWindow* existing = findMdiWindow(filesToOpen[i])
            if(existing)
            {
                mdiArea->setActiveSubWindow(existing)
                continue
            }

            /*The docIndex doesn't need increased as it is only used for unnamed files*/
            numOfDocs++
            MdiWindow* mdiWin = new MdiWindow(docIndex, mainWin, mdiArea, Qt::SubWindow)
            connect(mdiWin, SIGNAL(sendCloseMdiWin(MdiWindow*)), this, SLOT(onCloseMdiWin(MdiWindow*)))
            connect(mdiArea, SIGNAL(subWindowActivated(QMdiSubWindow*)), this, SLOT(onWindowActivated(QMdiSubWindow*)))

            /* Make sure the toolbars/etc... are shown before doing their zoomExtents */
            if (doOnce) {
                updateMenuToolbarStatusbar()
                doOnce = 0
            }

            if (mdiWin->loadFile(filesToOpen.at(i))) {
                statusbar->showMessage(tr("File(s) loaded"), 2000)
                mdiWin->show()
                mdiWin->showMaximized()
                /*Prevent duplicate entries in the recent files list*/
                if(!opensave_recent_list_of_files.contains(filesToOpen.at(i), Qt::CaseInsensitive)) {
                    opensave_recent_list_of_files.prepend(filesToOpen.at(i))
                }
                /*Move the recent file to the top of the list*/
                else {
                    opensave_recent_list_of_files.removeAll(filesToOpen.at(i))
                    opensave_recent_list_of_files.prepend(filesToOpen.at(i))
                }
                strcpy(settings.opensave_recent_directory, QFileInfo(filesToOpen.at(i)).absolutePath().toLocal8Bit().constData())

                View* v = mdiWin->getView()
                if (v) {
                    v->recalculateLimits()
                    v->zoomExtents()
                }
            }
            else {
                mdiWin->close()
            }
        }
    }

    windowMenuAboutToShow()

def MainWindow::openrecentfile():
    debug_message("MainWindow::openrecentfile()")

    /*Check to see if this from the recent files list*/
    QAction* recentSender = qobject_cast<QAction*>(sender())
    if (recentSender) {
        openFile(1, recentSender->data().toString())
    }
}

def MainWindow::savefile():
    debug_message("MainWindow::savefile()")

def MainWindow::saveasfile():
    debug_message("MainWindow::saveasfile()")
    /* need to find the activeSubWindow before it loses focus to the FileDialog*/
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow())
    if(!mdiWin)
        return

    QString file
    openFilesPath = settings.opensave_recent_directory
    file = QFileDialog::getSaveFileName(this, tr("Save As"), openFilesPath, formatFilterSave)

    mdiWin->saveFile(file)

QMdiSubWindow* MainWindow::findMdiWindow(const QString& fileName):
    debug_message("MainWindow::findMdiWindow(%s)", qPrintable(fileName))
    QString canonicalFilePath = QFileInfo(fileName).canonicalFilePath()

    foreach(QMdiSubWindow* subWindow, mdiArea->subWindowList())
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(subWindow)
        if(mdiWin)
        {
            if(mdiWin->getCurrentFile() == canonicalFilePath)
            {
                return subWindow
            }
        }
    }
    return 0

def MainWindow::closeEvent(QCloseEvent* event):
    mdiArea->closeAllSubWindows()
    writeSettings()
    event->accept()

def MainWindow::onCloseWindow():
    debug_message("MainWindow::onCloseWindow()")
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow())
    if(mdiWin)
    {
        onCloseMdiWin(mdiWin)
    }
}

def MainWindow::onCloseMdiWin(MdiWindow* theMdiWin):
    debug_message("MainWindow::onCloseMdiWin()")
    numOfDocs--

    int keepMaximized
    if(theMdiWin) { keepMaximized = theMdiWin->isMaximized(); }

    mdiArea->removeSubWindow(theMdiWin)
    theMdiWin->deleteLater()

    updateMenuToolbarStatusbar()
    windowMenuAboutToShow()

    if(keepMaximized)
    {
        MdiWindow* mdiWin = qobject_cast<MdiWindow*>(mdiArea->activeSubWindow())
        if(mdiWin) { mdiWin->showMaximized(); }
    }
}

def MainWindow::onWindowActivated(QMdiSubWindow* w):
    debug_message("MainWindow::onWindowActivated()")
    MdiWindow* mdiWin = qobject_cast<MdiWindow*>(w)
    if(mdiWin) { mdiWin->onWindowActivated(); }
}

def MainWindow::resizeEvent(QResizeEvent* e):
    debug_message("MainWindow::resizeEvent()")
    QMainWindow::resizeEvent(e)
    statusBar()->setSizeGripEnabled(!isMaximized())

QAction* MainWindow::getFileSeparator():
    debug_message("MainWindow::getFileSeparator()")
    return myFileSeparator

def MainWindow::updateMenuToolbarStatusbar():
    int i
    debug_message("MainWindow::updateMenuToolbarStatusbar()")

    actionHash.value(ACTION_print)->setEnabled(numOfDocs > 0)
    actionHash.value(ACTION_windowclose)->setEnabled(numOfDocs > 0)
    actionHash.value(ACTION_designdetails)->setEnabled(numOfDocs > 0)

    if (numOfDocs) {
        int i
        /*Toolbars*/
        for (i=0; i<N_TOOLBARS; i++) {
            toolbar[i]->show()
        }

        foreach(QToolBar* tb, toolbarHash)
        {
            tb->show()
        }

        /*DockWidgets*/
        /*
        dockPropEdit->show()
        dockUndoEdit->show()
        */

        /*Menus*/
        menuBar()->clear()
        menuBar()->addMenu(menu[FILE_MENU])
        menuBar()->addMenu(menu[EDIT_MENU])
        menuBar()->addMenu(menu[VIEW_MENU])

        foreach(QMenu* menu_, menuHash)
        {
            menuBar()->addMenu(menu_)
        }

        menuBar()->addMenu(menu[SETTINGS_MENU])
        menuBar()->addMenu(menu[WINDOW_MENU])
        menuBar()->addMenu(menu[HELP_MENU])

        menu[WINDOW_MENU]->setEnabled(1)

        /* Statusbar */
        statusbar->clearMessage()
        statusBarMouseCoord->show()
        status_bar[STATUS_SNAP]->show()
        status_bar[STATUS_GRID]->show()
        status_bar[STATUS_RULER]->show()
        status_bar[STATUS_ORTHO]->show()
        status_bar[STATUS_POLAR]->show()
        status_bar[STATUS_QSNAP]->show()
        status_bar[STATUS_QTRACK]->show()
        status_bar[STATUS_LWT]->show()
    }
    else
    {
        /* Toolbars */
        toolbar[TOOLBAR_VIEW]->hide()
        toolbar[TOOLBAR_ZOOM]->hide()
        toolbar[TOOLBAR_PAN]->hide()
        toolbar[TOOLBAR_ICON]->hide()
        toolbar[TOOLBAR_HELP]->hide()
        toolbar[TOOLBAR_LAYER]->hide()
        toolbar[TOOLBAR_TEXT]->hide()
        toolbar[TOOLBAR_PROPERTIES]->hide()
        foreach(QToolBar* tb, toolbarHash)
        {
            tb->hide()
        }

        /*DockWidgets*/
        /*
        dockPropEdit->hide()
        dockUndoEdit->hide()
        */
        
        /*Menus*/
        menuBar()->clear()
        menuBar()->addMenu(menu[FILE_MENU])
        menuBar()->addMenu(menu[EDIT_MENU])
        menuBar()->addMenu(menu[SETTINGS_MENU])
        menuBar()->addMenu(menu[WINDOW_MENU])
        menuBar()->addMenu(menu[HELP_MENU])

        menu[WINDOW_MENU]->setEnabled(0)

        /*Statusbar*/
        statusbar->clearMessage()
        statusBarMouseCoord->hide()
        for (i=0; i<N_STATUS; i++) {
            status_bar[i]->hide()
        }
    }
}

int MainWindow::validFileFormat(const QString& fileName):
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

    /*TODO: Stable Only (Settings Option)*/
    /*stable = 'S'; unstable = 'S';*/

    /*Stable + Unstable*/
    stable = 'S'; unstable = 'U'

    const char* extension = 0
    const char* description = 0
    char readerState
    char writerState

    EmbFormatList* curFormat = 0
    for(int i=0; i < numberOfFormats; i++)
    {
        extension = formatTable[i].extension
        description = formatTable[i].description
        readerState = formatTable[i].reader_state
        writerState = formatTable[i].writer_state

        QString upperExt = QString(extension).toUpper()
        supportedStr = "*" + upperExt + " "
        individualStr = upperExt.replace(".", "") + " - " + description + " (*" + extension + ");;"
        if(readerState == stable || readerState == unstable)
        {
            /*Exclude color file formats from open dialogs*/
            if(upperExt != "COL" && upperExt != "EDR" && upperExt != "INF" && upperExt != "RGB")
            {
                supportedReaders.append(supportedStr)
                individualReaders.append(individualStr)
            }
        }
        if(writerState == stable || writerState == unstable)
        {
            supportedWriters.append(supportedStr)
            individualWriters.append(individualStr)
        }

    }

    supportedReaders.append(");;")
    supportedWriters.append(");;")

    formatFilterOpen = supportedReaders + individualReaders
    formatFilterSave = supportedWriters + individualWriters

    /*TODO: Fixup custom filter*/
    /*
    QString custom = settings.custom_filter
    if(custom.contains("supported", Qt::CaseInsensitive))
        custom = ""; //This will hide it
    else if(!custom.contains("*", Qt::CaseInsensitive))
        custom = ""; //This will hide it
    else
        custom = "Custom Filter(" + custom + ");;"

    return tr(qPrintable(custom + supported + all))
    */
}

def MainWindow::closeToolBar(QAction* action):
    if (action->objectName() == "toolbarclose") {
        QToolBar* tb = qobject_cast<QToolBar*>(sender())
        if(tb)
        {
            debug_message("%s closed.", qPrintable(tb->objectName()))
            tb->hide()
        }
    }
}

def MainWindow::floatingChangedToolBar(int isFloating):
    QToolBar* tb = qobject_cast<QToolBar*>(sender())
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
            QAction *ACTION = new QAction(tb->style()->standardIcon(QStyle::SP_DialogCloseButton), "Close", this)
            ACTION->setStatusTip("Close the " + tb->windowTitle() + " Toolbar")
            ACTION->setObjectName("toolbarclose")
            tb->addAction(ACTION)
            connect(tb, SIGNAL(actionTriggered(QAction*)), this, SLOT(closeToolBar(QAction*)))
        }
        else
        {
            QList<QAction*> actList = tb->actions()
            for(int i = 0; i < actList.size(); ++i)
            {
                QAction* ACTION = actList.value(i)
                if(ACTION->objectName() == "toolbarclose")
                {
                    tb->removeAction(ACTION)
                    disconnect(tb, SIGNAL(actionTriggered(QAction*)), this, SLOT(closeToolBar(QAction*)))
                    delete ACTION
                }
            }
        }
    }
}

EmbDetailsDialog::EmbDetailsDialog(QGraphicsScene* theScene, QWidget* parent) : QDialog(parent):
    setMinimumSize(750,550)

    getInfo()
    mainWidget = createMainWidget()

    buttonBox = new QDialogButtonBox(QDialogButtonBox::Ok)
    connect(buttonBox, SIGNAL(accepted()), this, SLOT(accept()))

    QVBoxLayout* vboxLayoutMain = new QVBoxLayout(this)
    vboxLayoutMain->addWidget(mainWidget)
    vboxLayoutMain->addWidget(buttonBox)
    setLayout(vboxLayoutMain)

    setWindowTitle(tr("Embroidery Design Details"))

    QApplication::setOverrideCursor(Qt::ArrowCursor)

EmbDetailsDialog::~EmbDetailsDialog():
    QApplication::restoreOverrideCursor()

def EmbDetailsDialog::getInfo():
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

extern char *details_label_text[]

QWidget* EmbDetailsDialog::createMainWidget():
    QWidget* widget = new QWidget(this)

    /*Misc*/
    QGroupBox* groupBoxMisc = new QGroupBox(tr("General Information"), widget)

    QLabel* labels[12]
    QLabel* fields[12]

    int i
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
        gridLayoutMisc->addWidget(labels[i], i, 0, Qt::AlignLeft)
        gridLayoutMisc->addWidget(fields[i], i, 1, Qt::AlignLeft)
    }
    gridLayoutMisc->setColumnStretch(1,1)
    groupBoxMisc->setLayout(gridLayoutMisc)

    /* TODO: Color Histogram */

    /*Stitch Distribution*/
    /*QGroupBox* groupBoxDist = new QGroupBox(tr("Stitch Distribution"), widget);*/

    /* TODO: Stitch Distribution Histogram */

    /*Widget Layout*/
    QVBoxLayout *vboxLayoutMain = new QVBoxLayout(widget)
    vboxLayoutMain->addWidget(groupBoxMisc)
    /*vboxLayoutMain->addWidget(groupBoxDist);*/
    vboxLayoutMain->addStretch(1)
    widget->setLayout(vboxLayoutMain)

    QScrollArea* scrollArea = new QScrollArea(this)
    scrollArea->setWidgetResizable(1)
    scrollArea->setWidget(widget)
    return scrollArea

bool Application::event(QEvent *event):
    switch (event->type()) {
    case QEvent::FileOpen:
        if (_mainWin) {
            _mainWin->openFilesSelected(QStringList(static_cast<QFileOpenEvent *>(event)->file()))
            return 1
        }
        /* Fall through*/
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

    this->show()

int ImageWidget::load(const QString &fileName):
    img.load(fileName)
    return 1

int ImageWidget::save(const QString &fileName):
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
    layerModelSorted->setDynamicSortFilter(1)
    layerModelSorted->setSourceModel(layerModel)

    treeView = new QTreeView
    treeView->setRootIsDecorated(0)
    treeView->setAlternatingRowColors(1)
    treeView->setModel(layerModelSorted)
    treeView->setSortingEnabled(1)
    treeView->sortByColumn(0, Qt::AscendingOrder)

    QVBoxLayout *mainLayout = new QVBoxLayout
    mainLayout->addWidget(treeView)
    setLayout(mainLayout)

    setWindowTitle(tr("Layer Manager"))
    setMinimumSize(750, 550)

    layerModel->setHeaderData(0, Qt::Horizontal, tr("Name"))
    layerModel->setHeaderData(1, Qt::Horizontal, tr("Visible"))
    layerModel->setHeaderData(2, Qt::Horizontal, tr("Frozen"))
    layerModel->setHeaderData(3, Qt::Horizontal, tr("Z Value"))
    layerModel->setHeaderData(4, Qt::Horizontal, tr("Color"))
    layerModel->setHeaderData(5, Qt::Horizontal, tr("Linetype"))
    layerModel->setHeaderData(6, Qt::Horizontal, tr("Lineweight"))
    layerModel->setHeaderData(7, Qt::Horizontal, tr("Print"))

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

    for(int i = 0; i < layerModel->columnCount(); ++i)
        treeView->resizeColumnToContents(i)

    QApplication::setOverrideCursor(Qt::ArrowCursor)

LayerManager::~LayerManager():
    QApplication::restoreOverrideCursor()

def LayerManager::addLayer(const QString& name,
                            const int visible,
                            const int frozen,
                            const float zValue,
                            const unsigned int color,
                            const QString& lineType,
                            const QString& lineWeight,
                            const int print):
    layerModel->insertRow(0)
    layerModel->setData(layerModel->index(0, 0), name)
    layerModel->setData(layerModel->index(0, 1), visible)
    layerModel->setData(layerModel->index(0, 2), frozen)
    layerModel->setData(layerModel->index(0, 3), zValue)

    QPixmap colorPix(QSize(16,16))
    colorPix.fill(QColor(color))
    layerModel->itemFromIndex(layerModel->index(0, 4))->setIcon(QIcon(colorPix))
    layerModel->setData(layerModel->index(0, 4), QColor(color))

    layerModel->setData(layerModel->index(0, 5), lineType)
    layerModel->setData(layerModel->index(0, 6), lineWeight)
    layerModel->setData(layerModel->index(0, 7), print)

int old_main(int argc, char *argv[]):
#if defined(Q_OS_MAC)
    Application app(argc, argv)
#else
    QApplication app(argc, argv)
#endif
    app.setApplicationName(_appName_)
    app.setApplicationVersion(_appVer_)

    QStringList filesToOpen

    for (int i = 1; i < argc; i++) {
        if (!strcmp(argv[i], "-d") || !strcmp(argv[i], "--debug")) {  }
        else if(!strcmp(argv[i], "-h") || !strcmp(argv[i], "--help")   ) { usage(); }
        else if(!strcmp(argv[i], "-v") || !strcmp(argv[i], "--version")) { version(); }
        else if(QFile::exists(argv[i]) && MainWindow::validFileFormat(argv[i])) {
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

    _mainWin->setWindowTitle(app.applicationName() + " " + app.applicationVersion())
    _mainWin->show()

    /*NOTE: If openFilesSelected() is called from within the mainWin constructor, slot commands wont work and the window menu will be screwed*/
    if(!filesToOpen.isEmpty())
        _mainWin->openFilesSelected(filesToOpen)

    return app.exec()

MdiArea::MdiArea(MainWindow* mw, QWidget *parent) : QMdiArea(parent), mainWin(mw):
    setTabsClosable(1)

    useLogo = 0
    useTexture = 0
    useColor = 0

MdiArea::~MdiArea():
}

def MdiArea::useBackgroundLogo(int use):
    useLogo = use
    forceRepaint()

def MdiArea::useBackgroundTexture(int use):
    useTexture = use
    forceRepaint()

def MdiArea::useBackgroundColor(int use):
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

def MdiArea::mouseDoubleClickEvent(QMouseEvent* /*e*/):
    mainWin->openFile()

def MdiArea::paintEvent(QPaintEvent* /*e*/):
    QWidget* vport = viewport()
    QRect rect = vport->rect()

    QPainter painter(vport)
    painter.setRenderHint(QPainter::SmoothPixmapTransform)

    /*Always fill with a solid color first*/
    if(useColor) painter.fillRect(rect, bgColor)
    else         painter.fillRect(rect, background())

    /*Then overlay the texture*/
    if(useTexture)
    {
        QBrush bgBrush(bgTexture)
        painter.fillRect(rect, bgBrush)
    }

    /*Overlay the logo last*/
    if(useLogo)
    {
        /*Center the pixmap*/
        int dx = (rect.width()-bgLogo.width())/2
        int dy = (rect.height()-bgLogo.height())/2
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
            View* v = mdiWin->getView()
            if(v)
            {
                v->recalculateLimits()
                v->zoomExtents()
            }
        }
    }
}

def MdiArea::forceRepaint():
    /* HACK: Take that QMdiArea! */
    QSize hack = size()
    resize(hack + QSize(1,1))
    resize(hack)

MdiWindow::MdiWindow(const int theIndex, MainWindow* mw, QMdiArea* parent, Qt::WindowFlags wflags) : QMdiSubWindow(parent, wflags):
    mainWin = mw
    mdiArea = parent

    myIndex = theIndex

    fileWasLoaded = 0

    setAttribute(Qt::WA_DeleteOnClose)

    QString aName
    curFile = aName.asprintf("Untitled%d.dst", myIndex)
    this->setWindowTitle(curFile)

    this->setWindowIcon(QIcon("icons/app.png"))

    gscene = new QGraphicsScene(0,0,0,0, this)
    gview = new View(mainWin, gscene, this)

    setWidget(gview)

    /*
     * WARNING:
     * DO NOT SET THE QMDISUBWINDOW (this) FOCUSPROXY TO THE PROMPT
     * AS IT WILL CAUSE THE WINDOW MENU TO NOT SWITCH WINDOWS PROPERLY!
     * ALTHOUGH IT SEEMS THAT SETTING INTERNAL WIDGETS FOCUSPROXY IS OK.
     */
/*    gview->setFocusProxy(mainWin->prompt);*/

    resize(sizeHint())

    curLayer = "0"
    curColor = 0; /*TODO: color ByLayer*/
    curLineType = "ByLayer"
    curLineWeight = "ByLayer"

    /* Due to strange Qt4.2.3 feature the child window icon is not drawn*/
    /* in the main menu if showMaximized() is called for a non-visible child window*/
    /* Therefore calling show() first...*/
    show()
    showMaximized()

    setFocusPolicy(Qt::WheelFocus)
    setFocus()

    onWindowActivated()

MdiWindow::~MdiWindow():
    debug_message("MdiWindow Destructor()")

int MdiWindow::saveFile(const QString &fileName):
    debug_message("SaveObject save(%s)", qPrintable(fileName))

    /* TODO: Before saving to a stitch only format, Embroidermodder needs
     *       to calculate the optimal path to minimize jump stitches. Also
     *       based upon which layer needs to be stitched first,
     *       the path to the next object needs to be hidden beneath fills
     *       that will come later. When finding the optimal path, we need
     *       to take into account the color of the thread, as we do not want
     *       to try to hide dark colored stitches beneath light colored fills.
     */
    int formatType = EMBFORMAT_UNSUPPORTED
    int writeSuccessful = 0
    int i

    formatType = emb_identify_format((char*)qPrintable(fileName))
    if (formatType == EMBFORMAT_UNSUPPORTED) {
        return 0
    }

    EmbPattern* pattern = 0

    pattern = embPattern_create()
    if(!pattern) { debug_message("Could not allocate memory for embroidery pattern"); }

    /* Write */
    int writer = emb_identify_format((char*)qPrintable(fileName))
    if (writer<0) {
        debug_message("Unsupported write file type: %s", qPrintable(fileName))
    }
    else {
        foreach(QGraphicsItem* item, _mainWin->activeScene()->items(Qt::AscendingOrder))
        {
            int objType = item->data(OBJ_TYPE).toInt()

            if (objType == OBJ_TYPE_ARC) {
                /* addArc */
            }
            else if (objType == OBJ_TYPE_BLOCK) {
                /* addBlock(pattern, item); */
            }
            else if(objType == OBJ_TYPE_CIRCLE) {
                CircleObject* obj = static_cast<CircleObject*>(item)
                if (obj) {
                    if (formatType == EMBFORMAT_STITCHONLY) {
                        QPainterPath path = obj->objectSavePath()
            toPolyline(pattern, obj->objectCenter(), path.simplified(), "0", obj->objectColor(), "CONTINUOUS", "BYLAYER"); /*TODO: proper layer/lineType/lineWeight //TODO: Improve precision, replace simplified*/
        }
        else {
            QPointF p = obj->objectCenter()
            float r = obj->objectRadius()
            embPattern_addCircleObjectAbs(pattern, (double)p.x(), (double)p.y(), (double)r)
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
    EllipseObject* obj = static_cast<EllipseObject*>(item)
    if(obj)
    {
        if(formatType == EMBFORMAT_STITCHONLY)
        {
            QPainterPath path = obj->objectSavePath()
            toPolyline(pattern, obj->objectCenter(), path.simplified(), "0", obj->objectColor(), "CONTINUOUS", "BYLAYER"); /*TODO: proper layer/lineType/lineWeight //TODO: Improve precision, replace simplified*/
        }
        else
        {
            /*TODO: ellipse rotation*/
            embPattern_addEllipseObjectAbs(pattern, (double)obj->objectCenter().x(), (double)obj->objectCenter().y(), (double)obj->objectWidth()/2.0, (double)obj->objectHeight()/2.0)
        }
    }
            }
            else if(objType == OBJ_TYPE_ELLIPSEARC)   { /* addEllipseArc(pattern, item);  */ }
            else if(objType == OBJ_TYPE_GRID)         { /* addGrid(pattern, item);     */    }
            else if(objType == OBJ_TYPE_HATCH)        { /* addHatch(pattern, item);       */ }
            else if(objType == OBJ_TYPE_IMAGE)        { /* addImage(pattern, item);       */ }
            else if(objType == OBJ_TYPE_INFINITELINE) { /* addInfiniteLine(pattern, item); */ }
            else if(objType == OBJ_TYPE_LINE)         { 
    LineObject* obj = static_cast<LineObject*>(item)
    if(obj)
    {
        if(formatType == EMBFORMAT_STITCHONLY)
        {
            toPolyline(pattern, obj->objectEndPoint1(), obj->objectSavePath(), "0", obj->objectColor(), "CONTINUOUS", "BYLAYER"); /*TODO: proper layer/lineType/lineWeight*/
        }
        else
        {
            embPattern_addLineObjectAbs(pattern, (double)obj->objectX1(), (double)obj->objectY1(), (double)obj->objectX2(), (double)obj->objectY2())
        }
    }
      }
            else if (objType == OBJ_TYPE_PATH) {
    /*TODO: Reimplement addPolyline() using the libembroidery C API*/
    /*
    debug_message("addPolyline()")
    QGraphicsPathItem* polylineItem = (QGraphicsPathItem*)item
    if(polylineItem)
    {
        QPainterPath path = polylineItem->path()
        QPointF pos = polylineItem->pos()
        float startX = pos.x()
        float startY = pos.y()

        QPainterPath::Element element
        QPainterPath::Element P1
        QPainterPath::Element P2
        QPainterPath::Element P3
        QPainterPath::Element P4

        for(int i = 0; i < path.elementCount()-1; ++i)
        {
            element = path.elementAt(i)
            if(element.isMoveTo())
            {
                pattern.AddStitchAbs((element.x + startX), -(element.y + startY), TRIM)
            }
            else if(element.isLineTo())
            {
                pattern.AddStitchAbs((element.x + startX), -(element.y + startY), NORMAL)
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
        pattern.AddStitchRel(0, 0, STOP)
        QColor c= polylineItem->pen().color()
        pattern.AddColor(c.red(), c.green(), c.blue(), "", "")
    }
    */
            }
            else if(objType == OBJ_TYPE_POINT)        { 
    PointObject* obj = static_cast<PointObject*>(item)
    if(obj)
    {
        if(formatType == EMBFORMAT_STITCHONLY)
        {
            toPolyline(pattern, obj->objectPos(), obj->objectSavePath(), "0", obj->objectColor(), "CONTINUOUS", "BYLAYER"); /*TODO: proper layer/lineType/lineWeight*/
        }
        else
        {
            embPattern_addPointObjectAbs(pattern, (double)obj->objectX(), (double)obj->objectY())
        }
    }
             }
            else if(objType == OBJ_TYPE_POLYGON) {
    PolygonObject* obj = static_cast<PolygonObject*>(item)
    if(obj)
    {
        toPolyline(pattern, obj->objectPos(), obj->objectSavePath(), "0", obj->objectColor(), "CONTINUOUS", "BYLAYER"); /*TODO: proper layer/lineType/lineWeight*/
    }
            }
            else if(objType == OBJ_TYPE_POLYLINE) { 
                PolylineObject* obj = static_cast<PolylineObject*>(item)
                if (obj)  {
                    toPolyline(pattern, obj->objectPos(), obj->objectSavePath(), "0", obj->objectColor(), "CONTINUOUS", "BYLAYER"); /*TODO: proper layer/lineType/lineWeight*/
                }
            }
            else if(objType == OBJ_TYPE_RAY) {
                /* addRay(pattern, item);       */
            }
            else if(objType == OBJ_TYPE_RECTANGLE) { 
    RectObject* obj = static_cast<RectObject*>(item)
    if(obj)
    {
        if(formatType == EMBFORMAT_STITCHONLY)
        {
            toPolyline(pattern, obj->objectPos(), obj->objectSavePath(), "0", obj->objectColor(), "CONTINUOUS", "BYLAYER"); /*TODO: proper layer/lineType/lineWeight*/
        }
        else
        {
            /*TODO: Review this at some point*/
            QPointF topLeft = obj->objectTopLeft()
            embPattern_addRectObjectAbs(pattern, (double)topLeft.x(), (double)topLeft.y(), (double)obj->objectWidth(), (double)obj->objectHeight())
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
    TextSingleObject* obj = static_cast<TextSingleObject*>(item)
    if(obj)
    {
        if(formatType == EMBFORMAT_STITCHONLY)
        {
            QList<QPainterPath> pathList = obj->objectSavePathList()
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

        writeSuccessful = embPattern_writeAuto(pattern, qPrintable(fileName))
        if(!writeSuccessful) { debug_message("Writing file %s was unsuccessful", qPrintable(fileName)); }
    }

    /*TODO: check the embLog for errors and if any exist, report them.*/
    embPattern_free(pattern)

    return writeSuccessful

int MdiWindow::loadFile(const QString &fileName):
    debug_message("MdiWindow loadFile()")

    unsigned int tmpColor = getCurrentColor()

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

    /* Read*/
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
    else {
        embPattern_moveStitchListToPolylines(p); /*TODO: Test more*/
        int stitchCount = p->stitchList->count
        QPainterPath path

        if (p->circles) {
            for (int i = 0; i < p->circles->count; i++) {
                EmbCircle c = p->circles->circle[i].circle
                EmbColor thisColor = p->circles->circle[i].color
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b))
                /* NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed.*/
                mainWin->nativeAddCircle(c.center.x, c.center.y, c.radius, 0, OBJ_RUBBER_OFF); /*TODO: fill*/
            }
        }
        if (p->ellipses) {
            for (int i = 0; i < p->ellipses->count; i++) {
                EmbEllipse e = p->ellipses->ellipse[i].ellipse
                EmbColor thisColor = p->ellipses->ellipse[i].color
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b))
                /* NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed. */
                mainWin->nativeAddEllipse(e.centerX, e.centerY, e.radiusX, e.radiusY, 0, 0, OBJ_RUBBER_OFF); /*TODO: rotation and fill*/
            }
        }
        if (p->lines) {
            for (int i = 0; i < p->lines->count; i++) {
                EmbLine li = p->lines->line[i].line
                EmbColor thisColor = p->lines->line[i].color
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b))
                /* NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed. */
                mainWin->nativeAddLine(li.start.x, li.start.y, li.end.x, li.end.y, 0, OBJ_RUBBER_OFF); /*TODO: rotation*/
            }
        }
        if (p->paths) {
            /* TODO: This is unfinished. It needs more work*/
            for (int i=0; i < p->paths->count; i++) {
                EmbArray* curPointList = p->paths->path[i]->pointList
                QPainterPath pathPath
                EmbColor thisColor = p->paths->path[i]->color
                if (curPointList->count > 0) {
                    EmbVector pp = curPointList[0].point->point
                    pathPath.moveTo(pp.x, -pp.y); /*NOTE: Qt Y+ is down and libembroidery Y+ is up, so inverting the Y is needed.*/
                }
                for (int j = 1; j < curPointList->count; j++) {
                    EmbVector pp = curPointList[j].point->point
                    pathPath.lineTo(pp.x, -pp.y); /*NOTE: Qt Y+ is down and libembroidery Y+ is up, so inverting the Y is needed.*/
                }
                QPen loadPen(qRgb(thisColor.r, thisColor.g, thisColor.b))
                loadPen.setWidthF(0.35)
                loadPen.setCapStyle(Qt::RoundCap)
                loadPen.setJoinStyle(Qt::RoundJoin)

                PathObject* obj = new PathObject(0,0, pathPath, loadPen.color().rgb())
                obj->setObjectRubberMode(OBJ_RUBBER_OFF)
                _mainWin->activeScene()->addItem(obj)
            }
        }
        if (p->points) {
            for (int i = 0; i < p->points->count; i++) {
                EmbVector po = p->points->point[i].point
                EmbColor thisColor = p->points->point[i].color
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b))
                /* NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed.*/
                mainWin->nativeAddPoint(po.x, po.y)
            }
        }
        if (p->polygons) {
            for (int i = 0; i < p->polygons->count; i++) {
                EmbArray *curPointList = p->polygons->polygon[i]->pointList
                QPainterPath polygonPath
                int firstPoint = 0
                float startX = 0, startY = 0
                float x = 0, y = 0
                EmbColor thisColor = p->polygons->polygon[i]->color
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b))
                for (int j=0; j<curPointList->count; j++) {
                    EmbVector pp = curPointList->point[j].point
                    x = pp.x
                    y = -pp.y; /*NOTE: Qt Y+ is down and libembroidery Y+ is up, so inverting the Y is needed.*/

                    if (firstPoint) {
                        polygonPath.lineTo(x,y)
                    } else {
                        polygonPath.moveTo(x,y)
                        firstPoint = 1
                        startX = x
                        startY = y
                    }
                }
                polygonPath.translate(-startX, -startY)
                mainWin->nativeAddPolygon(startX, startY, polygonPath, OBJ_RUBBER_OFF)
            }
        }
        /* NOTE: Polylines should only contain NORMAL stitches. */
        if (p->polylines) {
            for (int i=0; i<p->polylines->count; i++) {
                EmbArray* curPointList = p->polylines->polyline[i]->pointList
                QPainterPath polylinePath
                int firstPoint = 0
                float startX = 0, startY = 0
                float x = 0, y = 0
                EmbColor thisColor = p->polylines->polyline[i]->color
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b))
                for (int j=0; j<curPointList->count; j++) {
                    EmbVector pp = curPointList->point[j].point
                    x = pp.x
                    y = -pp.y; /*NOTE: Qt Y+ is down and libembroidery Y+ is up, so inverting the Y is needed.*/
                    if (firstPoint) {
                        polylinePath.lineTo(x,y)
                    } else {
                        polylinePath.moveTo(x,y)
                        firstPoint = 1
                        startX = x
                        startY = y
                    }
                }

                polylinePath.translate(-startX, -startY)
                mainWin->nativeAddPolyline(startX, startY, polylinePath, OBJ_RUBBER_OFF)
            }
        }
        if (p->rects) {
            for (int i=0; i<p->rects->count; i++) {
                EmbRect r = p->rects->rect[i].rect
                EmbColor thisColor = p->rects->rect[i].color
                setCurrentColor(qRgb(thisColor.r, thisColor.g, thisColor.b))
                /*NOTE: With natives, the Y+ is up and libembroidery Y+ is up, so inverting the Y is NOT needed.*/
                mainWin->nativeAddRectangle(embRect_x(r), embRect_y(r), embRect_width(r), embRect_height(r), 0, 0, OBJ_RUBBER_OFF); /*TODO: rotation and fill*/
            }
        }
        setCurrentFile(fileName)
        mainWin->statusbar->showMessage("File loaded.")
        QString stitches
        stitches.setNum(stitchCount)

        if(settings.grid_load_from_file) {
            /*TODO: Josh, provide me a hoop size and/or grid spacing from the pattern.*/
        }
        QApplication::restoreOverrideCursor()
    }
    embPattern_free(p)

    /* Clear the undo stack so it is not possible to undo past this point. */
    undo_history_length = 0

    setCurrentColor(tmpColor)
    return 1

def MdiWindow::print():
    /*
    QPrintDialog dialog(&printer, this)
    if (dialog.exec() == QDialog::Accepted) {
        QPainter painter(&printer)
        if (settings.printing_disable_bg) {
            // Save current bg
            QBrush brush = gview->backgroundBrush()
            // Save ink by not printing the bg at all
            gview->setBackgroundBrush(Qt::NoBrush)
            // Print, fitting the viewport contents into a full page
            gview->render(&painter)
            // Restore the bg
            gview->setBackgroundBrush(brush)
        } else {
            // Print, fitting the viewport contents into a full page
            gview->render(&painter)
        }



/* TODO: Save a Brother PEL image (An 8bpp, 130x113 pixel monochromatic? bitmap image) Why 8bpp when only 1bpp is needed?*/

/* TODO: Should BMC be limited to ~32KB or is this a mix up with Bitmap Cache?*/
/* TODO: Is there/should there be other embedded data in the bitmap besides the image itself?*/
/* NOTE: Can save a Singer BMC image (An 8bpp, 130x113 pixel colored bitmap image)*/
def MdiWindow::saveBMC():
    /* TODO: figure out how to center the image, right now it just plops it to the left side.*/
    QImage img(150, 150, QImage::Format_ARGB32_Premultiplied)
    img.fill(qRgb(255,255,255))
    QRectF extents = gscene->itemsBoundingRect()

    QPainter painter(&img)
    QRectF targetRect(0,0,150,150)
    if (settings.printing_disable_bg) { /*TODO: Make BMC background into it's own setting? */
        QBrush brush = gscene->backgroundBrush()
        gscene->setBackgroundBrush(Qt::NoBrush)
        gscene->update()
        gscene->render(&painter, targetRect, extents, Qt::KeepAspectRatio)
        gscene->setBackgroundBrush(brush)
    } else {
        gscene->update()
        gscene->render(&painter, targetRect, extents, Qt::KeepAspectRatio)
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

def MdiWindow::closeEvent(QCloseEvent* /*e*/):
    debug_message("MdiWindow closeEvent()")
    emit sendCloseMdiWin(this)

def MdiWindow::onWindowActivated():
    debug_message("MdiWindow onWindowActivated()")
    status_bar[STATUS_SNAP]->setChecked(gscene->property("ENABLE_SNAP").toBool())
    status_bar[STATUS_GRID]->setChecked(gscene->property("ENABLE_GRID").toBool())
    status_bar[STATUS_RULER]->setChecked(gscene->property("ENABLE_RULER").toBool())
    status_bar[STATUS_ORTHO]->setChecked(gscene->property("ENABLE_ORTHO").toBool())
    status_bar[STATUS_POLAR]->setChecked(gscene->property("ENABLE_POLAR").toBool())
    status_bar[STATUS_QSNAP]->setChecked(gscene->property("ENABLE_QSNAP").toBool())
    status_bar[STATUS_QTRACK]->setChecked(gscene->property("ENABLE_QTRACK").toBool())
    status_bar[STATUS_LWT]->setChecked(gscene->property("ENABLE_LWT").toBool())
    /*mainWin->prompt->setHistory(promptHistory);*/
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
    gview->deletePressed()

def MdiWindow::escapePressed():
    gview->escapePressed()

def MdiWindow::showViewScrollBars(int val):
    gview->showScrollBars(val)

def MdiWindow::setViewCrossHairColor(unsigned int color):
    gview->setCrossHairColor(color)

def MdiWindow::setViewBackgroundColor(unsigned int color):
    gview->setBackgroundColor(color)

def MdiWindow::setViewSelectBoxColors(unsigned int colorL, unsigned int fillL, unsigned int colorR, unsigned int fillR, int alpha):
    gview->setSelectBoxColors(colorL, fillL, colorR, fillR, alpha)

def MdiWindow::setViewGridColor(unsigned int color):
    gview->setGridColor(color)

def MdiWindow::setViewRulerColor(unsigned int color):
    gview->setRulerColor(color)

PreviewDialog::PreviewDialog(QWidget* parent,
                             const QString& caption,
                             const QString& dir,
                             const QString& filter) : QFileDialog(parent, caption, dir, filter):
    debug_message("PreviewDialog Constructor")

    /*TODO: get actual thumbnail image from file, lets also use a size of 128x128 for now...*/
    /*TODO: make thumbnail size adjustable thru settings dialog*/
    imgWidget = new ImageWidget("icons/default/nopreview.png", this)

    QLayout* lay = layout()
    if(qobject_cast<QGridLayout*>(lay))
    {
        QGridLayout* grid = qobject_cast<QGridLayout*>(lay)
        grid->addWidget(imgWidget, 0, grid->columnCount(), grid->rowCount(), 1)
    }

    setModal(1)
    setOption(QFileDialog::DontUseNativeDialog)
    setViewMode(QFileDialog::Detail)
    setFileMode(QFileDialog::ExistingFiles)

    /*TODO: connect the currentChanged signal to update the preview imgWidget.*/
}

PreviewDialog::~PreviewDialog():
    debug_message("PreviewDialog Destructor")

SelectBox::SelectBox(Shape s, QWidget* parent) : QRubberBand(s, parent):
    /*Default values*/
    setColors(QColor(Qt::darkGreen), QColor(Qt::green), QColor(Qt::darkBlue), QColor(Qt::blue), 32)

def SelectBox::setDirection(int dir):
    if(!dir) { dirPen = leftPen;  dirBrush = leftBrush;  }
    else     { dirPen = rightPen; dirBrush = rightBrush; }
    boxDir = dir

def SelectBox::setColors(const QColor& colorL, const QColor& fillL, const QColor& colorR, const QColor& fillR, int newAlpha):
    debug_message("SelectBox setColors()")
    alpha = newAlpha

    leftPenColor = colorL; /*TODO: allow customization*/
    leftBrushColor = to_emb_color(QColor(fillL.red(), fillL.green(), fillL.blue(), alpha))
    rightPenColor = colorR; /*TODO: allow customization*/
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
    /*HACK: Take that QRubberBand!*/
    QSize hack = size()
    resize(hack + QSize(1,1))
    resize(hack)

StatusBarButton::StatusBarButton(QString buttonText, MainWindow* mw, StatusBar* statbar, QWidget *parent) : QToolButton(parent):
    statusbar = statbar

    this->setObjectName("StatusBarButton" + buttonText)

    this->setText(buttonText)
    this->setAutoRaise(1)
    this->setCheckable(1)

    if (objectName() == "StatusBarButtonSNAP") {
        connect(this, SIGNAL(toggled(int)), this, SLOT(toggleSnap(int)))
    }
    else if (objectName() == "StatusBarButtonGRID") {
        connect(this, SIGNAL(toggled(int)), this, SLOT(toggleGrid(int)))
    }
    else if(objectName() == "StatusBarButtonRULER") {
        connect(this, SIGNAL(toggled(int)), this, SLOT(toggleRuler(int)))
    }
    else if(objectName() == "StatusBarButtonORTHO")  { connect(this, SIGNAL(toggled(int)), this, SLOT(toggleOrtho(int))); }
    else if(objectName() == "StatusBarButtonPOLAR")  { connect(this, SIGNAL(toggled(int)), this, SLOT(togglePolar(int))); }
    else if(objectName() == "StatusBarButtonQSNAP")  { connect(this, SIGNAL(toggled(int)), this, SLOT(toggleQSnap(int))); }
    else if(objectName() == "StatusBarButtonQTRACK") { connect(this, SIGNAL(toggled(int)), this, SLOT(toggleQTrack(int))); }
    else if(objectName() == "StatusBarButtonLWT")    { connect(this, SIGNAL(toggled(int)), this, SLOT(toggleLwt(int))); }
}

def StatusBarButton::contextMenuEvent(QContextMenuEvent *event):
    QApplication::setOverrideCursor(Qt::ArrowCursor)
    QMenu menu_(this)
    if (objectName() == "StatusBarButtonSNAP") {
        QAction* settingsSnapAction = new QAction(loadIcon(gridsnapsettings_xpm), "&Settings...", &menu_)
        connect(settingsSnapAction, SIGNAL(triggered()), this, SLOT(settingsSnap()))
        menu_.addAction(settingsSnapAction)
    }
    else if (objectName() == "StatusBarButtonGRID") {
        QAction* settingsGridAction = new QAction(loadIcon(gridsettings_xpm), "&Settings...", &menu_)
        connect(settingsGridAction, SIGNAL(triggered()), this, SLOT(settingsGrid()))
        menu_.addAction(settingsGridAction)
    }
    else if (objectName() == "StatusBarButtonRULER") {
        QAction* settingsRulerAction = new QAction(QIcon("icons/rulersettings.png"), "&Settings...", &menu_)
        connect(settingsRulerAction, SIGNAL(triggered()), this, SLOT(settingsRuler()))
        menu_.addAction(settingsRulerAction)
    }
    else if (objectName() == "StatusBarButtonORTHO") {
        QAction* settingsOrthoAction = new QAction(QIcon("icons/orthosettings.png"), "&Settings...", &menu_)
        connect(settingsOrthoAction, SIGNAL(triggered()), this, SLOT(settingsOrtho()))
        menu_.addAction(settingsOrthoAction)
    }
    else if (objectName() == "StatusBarButtonPOLAR") {
        QAction* settingsPolarAction = new QAction(QIcon("icons/polarsettings.png"), "&Settings...", &menu_)
        connect(settingsPolarAction, SIGNAL(triggered()), this, SLOT(settingsPolar()))
        menu_.addAction(settingsPolarAction)
    }
    else if(objectName() == "StatusBarButtonQSNAP")
    {
        QAction* settingsQSnapAction = new QAction(QIcon("icons/qsnapsettings.png"), "&Settings...", &menu_)
        connect(settingsQSnapAction, SIGNAL(triggered()), this, SLOT(settingsQSnap()))
        menu_.addAction(settingsQSnapAction)
    }
    else if(objectName() == "StatusBarButtonQTRACK")
    {
        QAction* settingsQTrackAction = new QAction(QIcon("icons/qtracksettings.png"), "&Settings...", &menu_)
        connect(settingsQTrackAction, SIGNAL(triggered()), this, SLOT(settingsQTrack()))
        menu_.addAction(settingsQTrackAction)
    }
    else if(objectName() == "StatusBarButtonLWT") {
        View* gview = _mainWin->activeView()
        if (gview) {
            QAction* enableRealAction = new QAction(QIcon("icons/realrender.png"), "&RealRender On", &menu_)
            enableRealAction->setEnabled(!gview->isRealEnabled())
            connect(enableRealAction, SIGNAL(triggered()), this, SLOT(enableReal()))
            menu_.addAction(enableRealAction)

            QAction* disableRealAction = new QAction(QIcon("icons/realrender.png"), "&RealRender Off", &menu_)
            disableRealAction->setEnabled(gview->isRealEnabled())
            connect(disableRealAction, SIGNAL(triggered()), this, SLOT(disableReal()))
            menu_.addAction(disableRealAction)
        }

        QAction* settingsLwtAction = new QAction(loadIcon(lineweightsettings_xpm), "&Settings...", &menu_)
        connect(settingsLwtAction, SIGNAL(triggered()), this, SLOT(settingsLwt()))
        menu_.addAction(settingsLwtAction)
    }
    menu_.exec(event->globalPos())
    QApplication::restoreOverrideCursor()
    statusbar->clearMessage()

StatusBar::StatusBar(MainWindow* mw, QWidget *parent) : QStatusBar(parent):
    int i
    this->setObjectName("StatusBar")

    for (i=0; i<N_STATUS; i++) {
        status_bar[i] = new StatusBarButton(status_bar_label[i], _mainWin, this, this)
    }
    statusBarMouseCoord = new QLabel(this)

    statusBarMouseCoord->setMinimumWidth(300); /* Must fit this text always*/
    statusBarMouseCoord->setMaximumWidth(300); /* "+1.2345E+99, +1.2345E+99, +1.2345E+99"*/

    this->addWidget(statusBarMouseCoord)
    for (i=0; i<N_STATUS; i++) {
        this->addWidget(status_bar[i])
    }
}

def StatusBar::setMouseCoord(x, y):
    # TODO: set format from settings (Architectural, Decimal, Engineering, Fractional, Scientific)

    /* Decimal */
    statusBarMouseCoord->setText(QString().setNum(x, 'F', 4) + ", " + QString().setNum(y, 'F', 4)); /*TODO: use precision from unit settings*/

    /* Scientific */
    /* statusBarMouseCoord->setText(QString().setNum(x, 'E', 4) + ", " + QString().setNum(y, 'E', 4)); */
    /* TODO: use precision from unit settings */
}
"""


def main_about():
    debug_message("main_about()")

    """
    /*TODO: QTabWidget for about dialog*/
    /*QApplication::setOverrideCursor(Qt::ArrowCursor)
    debug_message("about()")
    QString appDir = qApp->applicationDirPath()
    QString title = "About Embroidermodder 2"

    QDialog dialog(_mainWin)
    ImageWidget img(appDir + "/images/logo-small.png")
    QLabel text(QString("Embroidermodder ") + QString(_appVer_) + "\n\n" +
                          _mainWin->tr("http://embroidermodder.org") +
                          "\n\n" +
                          _mainWin->tr("Available Platforms: GNU/Linux, Windows, Mac OSX, Raspberry Pi") +
                          "\n\n" +
                          _mainWin->tr("Embroidery formats by Josh Varga.") +
                          "\n" +
                          _mainWin->tr("User Interface by Jonathan Greig and Robin Swift.") +
                          "\n\n" +
                          _mainWin->tr("Free under the zlib/libpng license.")
                          #if defined(BUILD_GIT_HASH)
                          + "\n\n" +
                          _mainWin->tr("Build Hash: ") + qPrintable(BUILD_GIT_HASH)
                          #endif
                          )
    text.setWordWrap(1)

    QDialogButtonBox buttonbox(Qt::Horizontal, &dialog)
    QPushButton button(&dialog)
    button.setText("Oh, Yeah!")
    buttonbox.addButton(&button, QDialogButtonBox::AcceptRole)
    buttonbox.setCenterButtons(1)
    _mainWin->connect(&buttonbox, SIGNAL(accepted()), &dialog, SLOT(accept()))

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


def dayVision():
    gview = _mainWin->activeView()
    if gview:
        gview->setBackgroundColor(qRgb(255,255,255))
        # TODO: Make day vision color settings.
        gview->setCrossHairColor(qRgb(0,0,0))
        gview->setGridColor(qRgb(0,0,0))


def nightVision():
    gview = _mainWin->activeView()
    if (gview) 
        gview->setBackgroundColor(qRgb(0,0,0)); /* TODO: Make night vision color settings. */
        gview->setCrossHairColor(qRgb(255,255,255)); /*TODO: Make night vision color settings.*/
        gview->setGridColor(qRgb(255,255,255));      /*TODO: Make night vision color settings.*/


def actuator(char *call):
    undo_history_position++
    /* an action has been taken, we are at the current head of the stack */
    undo_history_length = undo_history_position
    strcpy(undo_history[undo_history_position], call)
    id = call[0]
    if (id < 0) 
        id += 256
    
    if (id < N_ACTIONS) 
        action_list[id].function()

file_toolbar = [
    ACTION_new,
    ACTION_open,
    ACTION_save,
    ACTION_saveas,
    ACTION_print,
    ACTION_designdetails,
    -1,
    ACTION_help,
    -2
]


edit_toolbar = [
    ACTION_undo,
    ACTION_redo,
    -1,
    ACTION_cut,
    ACTION_copy,
    ACTION_paste,
    -2
]


view_toolbar = [
    ACTION_day,
    ACTION_night,
    -2
]


int pan_toolbar[] = {
    ACTION_panrealtime,
    ACTION_panpoint,
    -1,
    ACTION_panleft,
    ACTION_panright,
    ACTION_panup,
    ACTION_pandown,
    -2
]

int icon_toolbar[] = {
    ACTION_icon16,
    ACTION_icon24,
    ACTION_icon32,
    ACTION_icon48,
    ACTION_icon64,
    ACTION_icon128,
    -2
]

int help_toolbar[] = {
    ACTION_help,
    -1,
    ACTION_changelog,
    -1,
    ACTION_about,
    -1,
    ACTION_whatsthis,
    -2
]

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
]

int layer_toolbar[] = {
    -2
]

int text_toolbar[] = {
    -2
]

int properties_toolbar[] = {
    -2
]

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
]


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
]

int edit_menu[] = {
    ACTION_undo,
    ACTION_redo,
    -1,
    ACTION_cut,
    ACTION_copy,
    ACTION_paste,
    -2
]

int view_menu[] = {
    ACTION_day,
    ACTION_night,
    -2
]

int pan_menu[] = {
    ACTION_panrealtime,
    ACTION_panpoint,
    -1,
    ACTION_panleft,
    ACTION_panright,
    ACTION_panup,
    ACTION_pandown,
    -2
]

int icon_menu[] = {
    ACTION_icon16,
    ACTION_icon24,
    ACTION_icon32,
    ACTION_icon48,
    ACTION_icon64,
    ACTION_icon128,
    -2
]

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
]

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
]

int settings_menu[] = {
    ACTION_settingsdialog,
    -1,
    -2
]

int recent_menu[] = {
    -1,
    -2
]

int window_menu[] = {
    -1,
    -2
]

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
]

float symbol_scale = 0.01

/* Symbols use the SVG path syntax.
 *
 * In theory, we could combine the icons and symbols systems,
 * since they could be rendered once and stored as icons in Qt.
 * (Or as textures in FreeGLUT.)
 *
 * Also we want to render the patterns themselves using SVG
 * syntax, so it would save on repeated work overall.
 */
symbol_list[] = {
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
]

path_symbol icon_zero[] = {
    /* path.addEllipse(QPointF(x+0.25*xScale, y-0.50*yScale), 0.25*xScale, 0.50*yScale);*/
    M 0 -0.75
    L 0 -0.25
    A 0 -0.5 0.5 0.5 180.0 180.0
    L 0.5, -0.75
    A 0 -1.0, 0.5, 0.5, 0.0, 180.0
]

path_symbol icon_two[] = {
    {PATHS_MOVETO, 0 -0.75
    A {0.45, 1.00, 0.50, 180.00, -216.87
    L 0 0.0
    L {0.50, 0.0
]

path_symbol icon_three[] = {
    {PATHS_ARCMOVETO, 0 -0.50, 0.50, 0.50, 195.00
    A 0 -0.50, 0.50, 195.00, 255.00
    A 0 -0.50, 0.50, 270.00, 255.00
]

path_symbol icon_five[] = {
    M 50 0 L 0 0 L 0 50 L 25 50 A 0.0, -0.5 0.5 0.5 90.0 -180.0 L 0 0
]

path_symbol icon_six[] = {
    path.addEllipse(QPointF(x+0.25*xScale, y-0.25*yScale), 0.25*xScale, 0.25*yScale)
    M 0 75 L 0 25
    path.arcTo(x+0.00*xScale, y-1.00*yScale, 0.50*xScale, 0.50*yScale, 180.00, -140.00)
]

path_symbol icon_eight[] = {
    path.addEllipse(QPointF(x+0.25*xScale, y-0.25*yScale), 0.25*xScale, 0.25*yScale)
    path.addEllipse(QPointF(x+0.25*xScale, y-0.75*yScale), 0.25*xScale, 0.25*yScale)
]

path_symbol icon_nine[] = {
    path.addEllipse(QPointF(x+0.25*xScale, y-0.75*yScale), 0.25*xScale, 0.25*yScale)
    M 0.50*xScale, y-0.75*yScale)
    L x+0.50*xScale, y-0.25*yScale)
    path.arcTo(x+0.00*xScale, y-0.50*yScale, 0.50*xScale, 0.50*yScale, 0.00, -140.00)
]

#endif


/* New for toolbars: modify and draw. Inquiry toolbar?
 *
 * TODO: associate the property editor with the function callbacks using
 * a function pointer.
 */

/* property_editor_row property_editors[] = { */
/*
QGroupBox* PropertyEditor::createGroupBoxGeometryCircle():
    groupBoxGeometryCircle = new QGroupBox(tr("Geometry"), this)

    toolButtonCircleCenterX = createToolButton("blank", tr("Center X"))
    toolButtonCircleCenterY = createToolButton("blank", tr("Center Y"))
    toolButtonCircleRadius = createToolButton("blank", tr("Radius"))
    toolButtonCircleDiameter = createToolButton("blank", tr("Diameter"))
    toolButtonCircleArea = createToolButton("blank", tr("Area"))
    toolButtonCircleCircumference = createToolButton("blank", tr("Circumference"))

    lineEditCircleCenterX = createLineEdit("double", 0)
    lineEditCircleCenterY = createLineEdit("double", 0)
    lineEditCircleRadius = createLineEdit("double", 0)
    lineEditCircleDiameter = createLineEdit("double", 0)
    lineEditCircleArea = createLineEdit("double", 0)
    lineEditCircleCircumference = createLineEdit("double", 0)

    mapSignal(lineEditCircleCenterX, "lineEditCircleCenterX", OBJ_TYPE_CIRCLE)
    mapSignal(lineEditCircleCenterY, "lineEditCircleCenterY", OBJ_TYPE_CIRCLE)
    mapSignal(lineEditCircleRadius, "lineEditCircleRadius", OBJ_TYPE_CIRCLE)
    mapSignal(lineEditCircleDiameter, "lineEditCircleDiameter", OBJ_TYPE_CIRCLE)
    mapSignal(lineEditCircleArea, "lineEditCircleArea", OBJ_TYPE_CIRCLE)
    mapSignal(lineEditCircleCircumference, "lineEditCircleCircumference", OBJ_TYPE_CIRCLE)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout->addRow(toolButtonCircleCenterX, lineEditCircleCenterX)
    formLayout->addRow(toolButtonCircleCenterY, lineEditCircleCenterY)
    formLayout->addRow(toolButtonCircleRadius, lineEditCircleRadius)
    formLayout->addRow(toolButtonCircleDiameter, lineEditCircleDiameter)
    formLayout->addRow(toolButtonCircleArea, lineEditCircleArea)
    formLayout->addRow(toolButtonCircleCircumference, lineEditCircleCircumference)
    groupBoxGeometryCircle->setLayout(formLayout)

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
    formLayout->addRow(toolButtonImageX, lineEditImageX)
    formLayout->addRow(toolButtonImageY, lineEditImageY)
    formLayout->addRow(toolButtonImageWidth, lineEditImageWidth)
    formLayout->addRow(toolButtonImageHeight, lineEditImageHeight)
    groupBoxGeometryImage->setLayout(formLayout)

    return groupBoxGeometryImage

QGroupBox* PropertyEditor::createGroupBoxMiscImage():
    groupBoxMiscImage = new QGroupBox(tr("Misc"), this)

    toolButtonImageName = createToolButton("blank", tr("Name"))
    toolButtonImagePath = createToolButton("blank", tr("Path"))

    lineEditImageName = createLineEdit("double", 1)
    lineEditImagePath = createLineEdit("double", 1)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout->addRow(toolButtonImageName, lineEditImageName)
    formLayout->addRow(toolButtonImagePath, lineEditImagePath)
    groupBoxMiscImage->setLayout(formLayout)

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
    formLayout->addRow(toolButtonInfiniteLineX1, lineEditInfiniteLineX1)
    formLayout->addRow(toolButtonInfiniteLineY1, lineEditInfiniteLineY1)
    formLayout->addRow(toolButtonInfiniteLineX2, lineEditInfiniteLineX2)
    formLayout->addRow(toolButtonInfiniteLineY2, lineEditInfiniteLineY2)
    formLayout->addRow(toolButtonInfiniteLineVectorX, lineEditInfiniteLineVectorX)
    formLayout->addRow(toolButtonInfiniteLineVectorY, lineEditInfiniteLineVectorY)
    groupBoxGeometryInfiniteLine->setLayout(formLayout)

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
    formLayout->addRow(toolButtonLineStartX, lineEditLineStartX)
    formLayout->addRow(toolButtonLineStartY, lineEditLineStartY)
    formLayout->addRow(toolButtonLineEndX, lineEditLineEndX)
    formLayout->addRow(toolButtonLineEndY, lineEditLineEndY)
    formLayout->addRow(toolButtonLineDeltaX, lineEditLineDeltaX)
    formLayout->addRow(toolButtonLineDeltaY, lineEditLineDeltaY)
    formLayout->addRow(toolButtonLineAngle, lineEditLineAngle)
    formLayout->addRow(toolButtonLineLength, lineEditLineLength)
    groupBoxGeometryLine->setLayout(formLayout)

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
    formLayout->addRow(toolButtonPathVertexNum, comboBoxPathVertexNum)
    formLayout->addRow(toolButtonPathVertexX, lineEditPathVertexX)
    formLayout->addRow(toolButtonPathVertexY, lineEditPathVertexY)
    formLayout->addRow(toolButtonPathArea, lineEditPathArea)
    formLayout->addRow(toolButtonPathLength, lineEditPathLength)
    groupBoxGeometryPath->setLayout(formLayout)

    return groupBoxGeometryPath

QGroupBox* PropertyEditor::createGroupBoxMiscPath():
    groupBoxMiscPath = new QGroupBox(tr("Misc"), this)

    toolButtonPathClosed = createToolButton("blank", tr("Closed"))

    comboBoxPathClosed = createComboBox(0)

    //TODO: mapSignal for paths

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout->addRow(toolButtonPathClosed, comboBoxPathClosed)
    groupBoxMiscPath->setLayout(formLayout)

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
        0, "blank", "Vertex Radius", LINE_EDIT_MODE, "lineEditPolygonVertexRadius"
    }

    toolButtonPolygonRadiusSide = createToolButton("blank", tr("Side Radius"))
    toolButtonPolygonDiameterVertex = createToolButton("blank", tr("Vertex Diameter"))
    toolButtonPolygonDiameterSide = createToolButton("blank", tr("Side Diameter"))
    toolButtonPolygonInteriorAngle = createToolButton("blank", tr("Interior Angle"))

    lineEditPolygonRadiusSide = createLineEdit("double", 0)
    lineEditPolygonDiameterVertex = createLineEdit("double", 0)
    lineEditPolygonDiameterSide = createLineEdit("double", 0)
    lineEditPolygonInteriorAngle = createLineEdit("double", 1)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout->addRow(toolButtonPolygonRadiusSide, lineEditPolygonRadiusSide)
    formLayout->addRow(toolButtonPolygonDiameterVertex, lineEditPolygonDiameterVertex)
    formLayout->addRow(toolButtonPolygonDiameterSide, lineEditPolygonDiameterSide)
    formLayout->addRow(toolButtonPolygonInteriorAngle, lineEditPolygonInteriorAngle)
    groupBoxGeometryPolygon->setLayout(formLayout)

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
    groupBoxGeometryPolyline->setLayout(formLayout)

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
    formLayout->addRow(toolButtonTextMultiX, lineEditTextMultiX)
    formLayout->addRow(toolButtonTextMultiY, lineEditTextMultiY)
    groupBoxGeometryTextMulti->setLayout(formLayout)

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

    mapSignal(lineEditTextSingleContents, "lineEditTextSingleContents", OBJ_TYPE_TEXTSINGLE)
    mapSignal(comboBoxTextSingleFont, "comboBoxTextSingleFont", OBJ_TYPE_TEXTSINGLE)
    mapSignal(comboBoxTextSingleJustify, "comboBoxTextSingleJustify", OBJ_TYPE_TEXTSINGLE)
    mapSignal(lineEditTextSingleHeight, "lineEditTextSingleHeight", OBJ_TYPE_TEXTSINGLE)
    mapSignal(lineEditTextSingleRotation, "lineEditTextSingleRotation", OBJ_TYPE_TEXTSINGLE)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout->addRow(toolButtonTextSingleContents, lineEditTextSingleContents)
    formLayout->addRow(toolButtonTextSingleFont, comboBoxTextSingleFont)
    formLayout->addRow(toolButtonTextSingleJustify, comboBoxTextSingleJustify)
    formLayout->addRow(toolButtonTextSingleHeight, lineEditTextSingleHeight)
    formLayout->addRow(toolButtonTextSingleRotation, lineEditTextSingleRotation)
    groupBoxTextTextSingle->setLayout(formLayout)

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
    formLayout->addRow(toolButtonTextSingleX, lineEditTextSingleX)
    formLayout->addRow(toolButtonTextSingleY, lineEditTextSingleY)
    groupBoxGeometryTextSingle->setLayout(formLayout)

    return groupBoxGeometryTextSingle

QGroupBox* PropertyEditor::createGroupBoxMiscTextSingle():
    groupBoxMiscTextSingle = new QGroupBox(tr("Misc"), this)

    toolButtonTextSingleBackward = createToolButton("blank", tr("Backward"))
    toolButtonTextSingleUpsideDown = createToolButton("blank", tr("UpsideDown"))

    comboBoxTextSingleBackward = createComboBox(0)
    comboBoxTextSingleUpsideDown = createComboBox(0)

    mapSignal(comboBoxTextSingleBackward, "comboBoxTextSingleBackward", OBJ_TYPE_TEXTSINGLE)
    mapSignal(comboBoxTextSingleUpsideDown, "comboBoxTextSingleUpsideDown", OBJ_TYPE_TEXTSINGLE)

    QFormLayout* formLayout = new QFormLayout(this)
    formLayout->addRow(toolButtonTextSingleBackward, comboBoxTextSingleBackward)
    formLayout->addRow(toolButtonTextSingleUpsideDown, comboBoxTextSingleUpsideDown)
    groupBoxMiscTextSingle->setLayout(formLayout)

    return groupBoxMiscTextSingle

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
/*        ARC_LENGTH, 1, "blank", "ArcLength")
    create_lineedit_row(formLayout, ARC_CHORD, 1, "blank", "ArcChord")
    create_lineedit_row(formLayout, ARC_INC_ANGLE, 1, "blank", "ArcIncludedAngle")
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
]


    There are 4 regions managed as views, .

    We don't have a seperate window for the pop-ups like the file
    browser for opening or saving a file. Instead, a view will
    be created 
"""

