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

void icon16(void)
{
    debug_message("icon16()");
    _mainWin->iconResize(16);
}

void icon24(void)
{
    debug_message("icon24()");
    _mainWin->iconResize(24);
}

void icon32(void)
{
    debug_message("icon32()");
    _mainWin->iconResize(32);
}

void icon48(void)
{
    debug_message("icon48()");
    _mainWin->iconResize(48);
}

void icon64(void)
{
    debug_message("icon64()");
    _mainWin->iconResize(64);
}

void icon128(void)
{
    debug_message("icon128()");
    _mainWin->iconResize(128);
}

void newFile(void)
{
    debug_message("newFile()");
    _mainWin->newFile();
}

void openFile(void)
{
    debug_message("openFile()");
    _mainWin->openFile();
}

void saveFile(void)
{
    debug_message("saveFile()");
    _mainWin->savefile();
}

void main_print(void)
{
    debug_message("print()");
    _mainWin->print();
}

void main_exit(void)
{
    debug_message("main_exit()");
    qApp->closeAllWindows();
    _mainWin->deleteLater();
    /* Force the MainWindow destructor to run before exiting. Makes Valgrind "still reachable" happy :) */
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
    QApplication::setOverrideCursor(Qt::ArrowCursor);
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
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->cut();
    }
}

void main_copy(void)
{
    debug_message("copy()");
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->copy();
    }
}

void main_paste(void)
{
    debug_message("main_paste()");
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->paste();
    }
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
    LayerManager layman( _mainWin,  _mainWin);
    layman.exec();
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
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->zoomWindow();
    }
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
    View* gview =  _mainWin->activeView();
    if (gview) {
        gview->zoomIn();
    }
}

void zoomOut(void)
{
    debug_message("zoomOut()");
    View* gview =  _mainWin->activeView();
    if (gview) {
        gview->zoomOut();
    }
}

void zoomSelected(void)
{
    debug_message("zoomSelected()");
    View* gview =  _mainWin->activeView();
    if (gview) {
        gview->zoomSelected();
    }
}

void zoomAll(void)
{
    debug_message("zoomAll()");
    debug_message("Implement zoomAll.");
}

void zoomExtents(void)
{
    debug_message("zoomExtents()");
    View* gview =  _mainWin->activeView();
    if (gview) {
        gview->zoomExtents();
    }
}

void panrealtime(void)
{
    debug_message("panrealtime()");
    View* gview =  _mainWin->activeView();
    if (gview) {
        gview->panRealTime();
    }
}

void panpoint(void)
{
    debug_message("panpoint()");
    View* gview =  _mainWin->activeView();
    if (gview) {
        gview->panPoint();
    }
}

void panLeft(void)
{
    debug_message("panLeft()");
    View* gview =  _mainWin->activeView();
    if (gview) {
        gview->panLeft();
    }
}

void panRight(void)
{
    debug_message("panRight()");
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->panRight();
    }
}

void panUp(void)
{
    debug_message("panUp()");
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->panUp();
    }
}

void panDown(void)
{
    debug_message("panDown()");
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->panDown();
    }
}

void dayVision(void)
{
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->setBackgroundColor(qRgb(255,255,255)); /*TODO: Make day vision color settings.*/
        gview->setCrossHairColor(qRgb(0,0,0));        /*TODO: Make day vision color settings.*/
        gview->setGridColor(qRgb(0,0,0));             /*TODO: Make day vision color settings.*/
    }
}

void nightVision(void)
{
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->setBackgroundColor(qRgb(0,0,0)); /* TODO: Make night vision color settings. */
        gview->setCrossHairColor(qRgb(255,255,255)); /*TODO: Make night vision color settings.*/
        gview->setGridColor(qRgb(255,255,255));      /*TODO: Make night vision color settings.*/
    }
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


/* Temporary interface fix
 * conversion between native (Emb) types and Qt types
 */
/* --------------------------------------------------------------- */

QPointF to_qpointf(EmbVector v)
{
    return QPointF(v.x, v.y);
}

EmbVector to_emb_vector(QPointF p)
{
    EmbVector v;
    v.x = p.x();
    v.y = p.y();
    return v;
}

QColor to_qcolor(EmbColor c)
{
    return QColor(c.r, c.g, c.b);
}

EmbColor to_emb_color(QColor c)
{
    EmbColor C;
    C.r = c.red();
    C.g = c.green();
    C.b = c.blue();
    return C;
}

/* --------------------------------------------------------------- */

/* This is similar to using an svg path, we can blend these systems
 * later. */
QPixmap *draw_pixmap(const char *description)
{
    QPixmap *icon = new QPixmap(128, 128);
    QPainter *painter = new QPainter(icon);
    QPen pen;
    pen.setWidth(10);
    /* This is the part based on description. */
    /* Other functions we can use are eraseRect, drawArc etc. https://doc.qt.io/qt-5/qpainter.html */
    if (strncmp(description, "rect", 4)==0) {
        
        pen.setColor(QColor(QRgb(0x000000)));
        painter->setPen(pen);
        painter->fillRect(0, 0, 128, 128, Qt::SolidPattern); 
    }
    return icon;
}

QIcon loadIcon(int icon_id)
{
    /* so we can experiment with different icon generation methods */
    if (icons[icon_id][0][0] == 'C') {
        return QIcon(*draw_pixmap(icons[icon_id][0]+2));
    }
    return QIcon(QPixmap(icons[icon_id]));
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

void settingsSnap()
{
    _mainWin->settingsDialog("Snap");
}

void settingsGrid()
{
    _mainWin->settingsDialog("Grid/Ruler");
}

void settingsRuler()
{
    _mainWin->settingsDialog("Grid/Ruler");
}

void settingsOrtho()
{
    _mainWin->settingsDialog("Ortho/Polar");
}

void settingsPolar()
{
    _mainWin->settingsDialog("Ortho/Polar");
}

void settingsQSnap()
{
    _mainWin->settingsDialog("QuickSnap");
}

void settingsQTrack()
{
    _mainWin->settingsDialog("QuickTrack");
}

void settingsLwt()
{
    _mainWin->settingsDialog("LineWeight");
}

void toggleSnap(int on)
{
    debug_message("StatusBarButton toggleSnap()");
    View* gview = _mainWin->activeView();
    if(gview) { gview->toggleSnap(on); }
}

void toggleGrid(int on)
{
    debug_message("StatusBarButton toggleGrid()");
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->toggleGrid(on);
    }
}

void toggleRuler(int on)
{
    debug_message("StatusBarButton toggleRuler()");
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->toggleRuler(on);
    }
}

void toggleOrtho(int on)
{
    debug_message("StatusBarButton toggleOrtho()");
    View* gview = _mainWin->activeView();
    if(gview) { gview->toggleOrtho(on); }
}

void togglePolar(int on)
{
    debug_message("StatusBarButton togglePolar()");
    View* gview = _mainWin->activeView();
    if(gview) { gview->togglePolar(on); }
}

void toggleQSnap(int on)
{
    debug_message("StatusBarButton toggleQSnap()");
    View* gview = _mainWin->activeView();
    if(gview) { gview->toggleQSnap(on); }
}

void toggleQTrack(int on)
{
    debug_message("StatusBarButton toggleQTrack()");
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->toggleQTrack(on);
    }
}

void toggleLwt(int on)
{
    debug_message("StatusBarButton toggleLwt()");
    View* gview = _mainWin->activeView();
    if(gview) { gview->toggleLwt(on); }
}

void enableLwt()
{
    debug_message("StatusBarButton enableLwt()");
    View* gview = _mainWin->activeView();
    if(gview)
    {
        if(!gview->isLwtEnabled())
            gview->toggleLwt(1);
    }
}

void disableLwt()
{
    debug_message("StatusBarButton disableLwt()");
    View* gview = _mainWin->activeView();
    if(gview)
    {
        if(gview->isLwtEnabled())
            gview->toggleLwt(0);
    }
}

void enableReal()
{
    debug_message("StatusBarButton enableReal()");
    View* gview = _mainWin->activeView();
    if(gview) { gview->toggleReal(1); }
}

void disableReal()
{
    debug_message("StatusBarButton disableReal()");
    View* gview = _mainWin->activeView();
    if(gview) { gview->toggleReal(0); }
}

