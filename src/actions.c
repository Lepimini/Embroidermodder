/* Embroidermodder 2.
 * ------------------------------------------------------------
 * Copyright 2021 The Embroidermodder Team
 * Embroidermodder 2 is Open Source Software.
 * See LICENSE.txt for licensing terms.
 * ------------------------------------------------------------
 * This file is for the functions, not the data, of embroidermodder 2.
 */

#include "embroidermodder.h"

#include <string.h>
#include <stdlib.h>

void icon16(void)
{
    debug_message("icon16()");
}

void icon24(void)
{
    debug_message("icon24()");
}

void icon32(void)
{
    debug_message("icon32()");
}

void icon48(void)
{
    debug_message("icon48()");
}

void icon64(void)
{
    debug_message("icon64()");
}

void icon128(void)
{
    debug_message("icon128()");
}

void newFile(void)
{
    debug_message("newFile()");
}

void openFile(void)
{
    debug_message("openFile()");
}

void saveFile(void)
{
    debug_message("saveFile()");
}

void main_print(void)
{
    debug_message("print()");
}

void main_exit(void)
{
    debug_message("main_exit()");
    exit(0);
}

void saveAsFile(void)
{

}

void whatsthisContextHelp(void)
{

}

void makeLayerCurrent(void)
{

}

void layerSelector(void)
{

}

void main_about(void)
{
    /*TODO: QTabWidget for about dialog*/
    /*QApplication::setOverrideCursor(Qt::ArrowCursor);
    debug_message("about()");
    QString appDir = qApp->applicationDirPath();
    QString title = "About Embroidermodder 2";

    QDialog dialog(_mainWin);
    ImageWidget img(appDir + "/images/logo-small.png");
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
                          );
    text.setWordWrap(1);

    QDialogButtonBox buttonbox(Qt::Horizontal, &dialog);
    QPushButton button(&dialog);
    button.setText("Oh, Yeah!");
    buttonbox.addButton(&button, QDialogButtonBox::AcceptRole);
    buttonbox.setCenterButtons(1);
    _mainWin->connect(&buttonbox, SIGNAL(accepted()), &dialog, SLOT(accept()));

    QVBoxLayout layout;
    layout.setAlignment(Qt::AlignCenter);
    layout.addWidget(&img);
    layout.addWidget(&text);
    layout.addWidget(&buttonbox);

    dialog.setWindowTitle(title);
    dialog.setMinimumWidth(img.minimumWidth()+30);
    dialog.setMinimumHeight(img.minimumHeight()+50);
    dialog.setLayout(&layout);
    dialog.exec();
    QApplication::restoreOverrideCursor();
    */
}

void main_help(void)
{

}

void settingsDialog(void)
{

}

void designDetails(void)
{

}

void main_cut(void)
{
    debug_message("cut()");
    /*
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->cut();
    }
    */
}

void main_copy(void)
{
    debug_message("copy()");
    /*
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->copy();
    }
    */
}

void main_paste(void)
{
    debug_message("main_paste()");
    /*
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->paste();
    }
    */
}


void main_redo(void)
{
    debug_message("copy()");
    /*
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->copy();
    }
    */
}

void main_undo(void)
{
    debug_message("main_paste()");
    /*
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->paste();
    }
    */
}

void tipOfTheDay(void)
{

}

void changelog(void)
{
    debug_message("changelog()");

    /* display in a custom widget instead */
    /*
    QUrl changelogURL("help/changelog.html");
    QDesktopServices::openUrl(changelogURL);
    */
}

void showAllLayers(void)
{

}

void freezeAllLayers(void)
{

}

void thawAllLayers(void)
{

}

void lockAllLayers(void)
{

}

void unlockAllLayers(void)
{

}

void hideAllLayers(void)
{

}

void lineWeightSelector(void)
{

}

void lineTypeSelector(void)
{

}

void colorSelector(void)
{

}

void windowClose(void)
{

}

void windowTile(void)
{

}

void windowCloseAll(void)
{

}

void windowCascade(void)
{

}

void windowNext(void)
{

}

void windowPrevious(void)
{

}

void textItalic(void)
{
    settings.text_style.italic = !settings.text_style.italic;
}

void textBold(void)
{
    settings.text_style.bold = !settings.text_style.bold;
}

void textStrikeout(void)
{
    settings.text_style.strikeout = !settings.text_style.strikeout;
}

void textUnderline(void)
{
    settings.text_style.underline = !settings.text_style.underline;
}

void textOverline(void)
{
    settings.text_style.overline = !settings.text_style.overline;
}


void makeLayerActive(void)
{
    debug_message("makeLayerActive()");
    debug_message("Implement makeLayerActive.");
}

void layerManager(void)
{
    debug_message("layerManager()");
    debug_message("Implement layerManager.");
    /*LayerManager layman( _mainWin,  _mainWin);
    layman.exec();
    */
}

void layerPrevious(void)
{
    debug_message("layerPrevious()");
    debug_message("Implement layerPrevious.");
}

void zoomRealtime(void)
{
    debug_message("zoomRealtime()");
    debug_message("Implement zoomRealtime.");
}

void zoomPrevious(void)
{
    debug_message("zoomPrevious()");
    debug_message("Implement zoomPrevious.");
}

void zoomWindow(void)
{
    debug_message("zoomWindow()");
    /*View* gview = _mainWin->activeView();
    if (gview) {
        gview->zoomWindow();
    }
    */
}

void zoomDynamic(void)
{
    debug_message("zoomDynamic()");
    debug_message("Implement zoomDynamic.");
}

void zoomScale(void)
{
    debug_message("zoomScale()");
    debug_message("Implement zoomScale.");
}

void zoomCenter(void)
{
    debug_message("zoomCenter()");
    debug_message("Implement zoomCenter.");
}

void zoomIn(void)
{
    debug_message("zoomIn()");
}

void zoomOut(void)
{
    debug_message("zoomOut()");
}

void zoomSelected(void)
{
    debug_message("zoomSelected()");
}

void zoomAll(void)
{
    debug_message("zoomAll()");
    debug_message("Implement zoomAll.");
}

void zoomExtents(void)
{
    debug_message("zoomExtents()");
}

void panrealtime(void)
{
    debug_message("panrealtime()");
}

void panpoint(void)
{
    debug_message("panpoint()");
}

void panLeft(void)
{
    debug_message("panLeft()");
}

void panRight(void)
{
    debug_message("panRight()");
}

void panUp(void)
{
    debug_message("panUp()");
}

void panDown(void)
{
    debug_message("panDown()");
}

void dayVision(void)
{
    #if 0
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->setBackgroundColor(qRgb(255,255,255)); /*TODO: Make day vision color settings.*/
        gview->setCrossHairColor(qRgb(0,0,0));        /*TODO: Make day vision color settings.*/
        gview->setGridColor(qRgb(0,0,0));             /*TODO: Make day vision color settings.*/
    }
    #endif
}

void nightVision(void)
{
    #if 0
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->setBackgroundColor(qRgb(0,0,0)); /* TODO: Make night vision color settings. */
        gview->setCrossHairColor(qRgb(255,255,255)); /*TODO: Make night vision color settings.*/
        gview->setGridColor(qRgb(255,255,255));      /*TODO: Make night vision color settings.*/
    }
    #endif
}

void doNothing(void)
{
    /* This function intentionally does nothing. */
    debug_message("doNothing()");
}


void actuator(char *call)
{
    int id;
    undo_history_position++;
    /* an action has been taken, we are at the current head of the stack */
    undo_history_length = undo_history_position;
    strcpy(undo_history[undo_history_position], call);
    id = call[0];
    if (id < 0) {
        id += 256;
    }
    if (id < N_ACTIONS) {
        action_list[id].function();
    }
}

/* --------------------------------------------------------------- */

void get_n_ints(const char *command, int *out, int n);
void get_n_floats(const char *command, float *out, int n);

/* This is similar to using an svg path, we can blend these systems
 * later. */
 #if 0
QPixmap *draw_pixmap(const char *description)
{
    char *ptr;
    int int_buffer[4];
    QPixmap *icon;
    QPainter *painter;
    QPen pen;
    get_n_ints(description, int_buffer, 2);
    icon = new QPixmap(int_buffer[0], int_buffer[1]);
    painter = new QPainter(icon);
    pen.setWidth(10);
    for (ptr=(char*)description; *ptr; ptr++) {
        /* Other functions we can use are eraseRect, drawArc etc. https://doc.qt.io/qt-5/qpainter.html */
        if (strncmp(ptr, "rect", 4)==0) {
            pen.setColor(QColor(QRgb(0x000000)));
            painter->setPen(pen);
            get_n_ints(ptr+5, int_buffer, 4);
            painter->fillRect(int_buffer[0], int_buffer[1],
                int_buffer[2], int_buffer[3], Qt::SolidPattern); 
        }
    }
    return icon;
}

QIcon loadIcon(const char **icon)
{
    /* so we can experiment with different icon generation methods */
    if (icon[0][0] == 'C') {
        return QIcon(*draw_pixmap(icon[0]+2));
    }
    return QIcon(QPixmap(icon));
}

#endif
void get_n_ints(const char *command, int *out, int n)
{
    int i;
    char modifyable[100];
    strcpy(modifyable, command);
    char *rest = (char*)modifyable;
    for (i=0; i<n; i++) {
        char *tok = strtok_r(rest, " ", &rest);
        out[i] = atoi(tok);
    }
}

void get_n_floats(const char *command, float *out, int n)
{
    int i;
    char modifyable[100];
    strcpy(modifyable, command);
    char *rest = (char*)modifyable;
    for (i=0; i<n; i++) {
        char *tok = strtok_r(rest, " ", &rest);
        out[i] = atof(tok);
    }
}

#if 0
void add_to_path(QPainterPath *path, const char *command, float pos[2], float scale[2])
{
    int j;
    float out[10];
    for (j=0; j<strlen(command); j++) {
        switch (command[j]) {
        case 'M':
            get_n_floats(command+j+2, out, 2);
            path->moveTo(pos[0]+out[0]*scale[0], pos[1]+out[1]*scale[1]);
            break;
        case 'L':
            get_n_floats(command+j+2, out, 2);
            path->lineTo(pos[0]+out[0]*scale[0], pos[1]+out[1]*scale[1]);
            break;
        case 'A':
            get_n_floats(command+j+2, out, 6);
            path->arcTo(pos[0]+out[0]*scale[0], pos[1]+out[1]*scale[1],
                        out[2], out[3], out[4], out[5]);
            break;
        case 'a':
            get_n_floats(command+j+2, out, 5);
            path->arcMoveTo(pos[0]+out[0]*scale[0], pos[1]+out[1]*scale[1],
                        out[2]*scale[0], out[3]*scale[1],
                        out[4]);
            break;
        case 'E':
            get_n_floats(command+j+2, out, 4);
            path->addEllipse(
                QPointF(pos[0]+out[0]*scale[0],  pos[1]+out[1]*scale[1]),
                out[2]*scale[0], out[3]*scale[1]);
            break;
        case 'Z':
            path->closeSubpath();
            break;
        default:
            break;
        }
    }
}

void add_list_to_path(QPainterPath *path, const char *commands[], float pos[2], float scale[2])
{
    for (int i=0; origin_string[i][0]; i++) {
        add_to_path(path, origin_string[i], pos, scale);
    }
}

/*NOTE: This function should be used to interpret various object types and save them as polylines for stitchOnly formats.*/
void toPolyline(EmbPattern* pattern, const QPointF& objPos, const QPainterPath& objPath, const QString& layer, const QColor& color, const QString& lineType, const QString& lineWeight)
{
    float startX = objPos.x();
    float startY = objPos.y();
    EmbArray* pointList = embArray_create(EMB_POINT);
    QPainterPath::Element element;
    for(int i = 0; i < objPath.elementCount(); ++i)
    {
        element = objPath.elementAt(i);
        EmbPointObject a;
        a.point.x = element.x + startX;
        a.point.y = -(element.y + startY);
        embArray_addPoint(pointList, &a);
    }
    EmbPolylineObject* polyObject;
    polyObject = (EmbPolylineObject *) malloc(sizeof(EmbPolylineObject));
    polyObject->pointList = pointList;
    polyObject->color = embColor_make(color.red(), color.green(), color.blue());
    polyObject->lineType = 1; /*TODO: proper lineType*/
    embPattern_addPolylineObjectAbs(pattern, polyObject);
}
#endif

void settingsSnap()
{

}

void settingsGrid()
{

}

void settingsRuler()
{

}

void settingsOrtho()
{

}

void settingsPolar()
{

}

void settingsQSnap()
{

}

void settingsQTrack()
{

}

void settingsLwt()
{

}

void toggleSnap(int on)
{
    debug_message("StatusBarButton toggleSnap()");

}

void toggleGrid(int on)
{
    debug_message("StatusBarButton toggleGrid()");

}

void toggleRuler(int on)
{
    debug_message("StatusBarButton toggleRuler()");

}

void toggleOrtho(int on)
{
    debug_message("StatusBarButton toggleOrtho()");

}

void togglePolar(int on)
{
    debug_message("StatusBarButton togglePolar()");

}

void toggleQSnap(int on)
{
    debug_message("StatusBarButton toggleQSnap()");

}

void toggleQTrack(int on)
{
    debug_message("StatusBarButton toggleQTrack()");

}

void toggleLwt(int on)
{
    debug_message("StatusBarButton toggleLwt()");

}

void enableLwt()
{
    debug_message("StatusBarButton enableLwt()");

}

void disableLwt()
{
    debug_message("StatusBarButton disableLwt()");
}

void enableReal()
{
    debug_message("StatusBarButton enableReal()");
}

void disableReal()
{
    debug_message("StatusBarButton disableReal()");
}

