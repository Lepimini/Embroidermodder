/* Embroidermodder 2.
 * ------------------------------------------------------------
 * Copyright 2021 The Embroidermodder Team
 * Embroidermodder 2 is Open Source Software.
 * See LICENSE.txt for licensing terms.
 * ------------------------------------------------------------
 * This file is for the functions, not the data, of embroidermodder 2.
 */

#include "embroidermodder.h"

void settings_actuator(void)
{
    
}

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
    //TODO: QTabWidget for about dialog
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
        gview->setBackgroundColor(qRgb(255,255,255)); //TODO: Make day vision color settings.
        gview->setCrossHairColor(qRgb(0,0,0));        //TODO: Make day vision color settings.
        gview->setGridColor(qRgb(0,0,0));             //TODO: Make day vision color settings.
    }
}

void nightVision(void)
{
    View* gview = _mainWin->activeView();
    if (gview) {
        gview->setBackgroundColor(qRgb(0,0,0)); /* TODO: Make night vision color settings. */
        gview->setCrossHairColor(qRgb(255,255,255)); //TODO: Make night vision color settings.
        gview->setGridColor(qRgb(255,255,255));      //TODO: Make night vision color settings.
    }
}

void doNothing(void)
{
    /* This function intentionally does nothing. */
    debug_message("doNothing()");
}


void actuator(void)
{
    undo_history_position++;
    /* an action has been taken, we are at the current head of the stack */
    undo_history_length = undo_history_position;
    memcpy(undo_history+undo_history_position, &action, sizeof(action_call));
    if (action.id >= 0 && action.id < n_actions) {
        action_list[action.id].function();
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

QIcon loadIcon(char **s)
{
    return QIcon(QPixmap(s));
}

void add_to_path(
    QPainterPath *path, path_symbol icon[],
    float pos[2], float scale[2]
)
{
    int j;
    for (j=0; icon[j].type != PATHS_END; j++) {
        switch (icon[j].type) {
        case PATHS_MOVETO:
            path->moveTo(pos[0]+icon[j].values[0]*scale[0],
                         pos[1]+icon[j].values[1]*scale[1]);
            break;
        case PATHS_LINETO:
            path->lineTo(pos[0]+icon[j].values[0]*scale[0],
                         pos[1]+icon[j].values[1]*scale[1]);
            break;
        case PATHS_ARCTO:
            path->arcTo(pos[0]+icon[j].values[0]*scale[0],
                        pos[1]+icon[j].values[1]*scale[1],
                        icon[j].values[2],
                        icon[j].values[3],
                        icon[j].values[4],
                        icon[j].values[5]
                        );
            break;
        case PATHS_ARCMOVETO:
            path->arcMoveTo(pos[0]+icon[j].values[0]*scale[0],
                        pos[1]+icon[j].values[1]*scale[1],
                        icon[j].values[2]*scale[0],
                        icon[j].values[3]*scale[1],
                        icon[j].values[4]);
            break;
        case PATHS_ELLIPSE:
            path->addEllipse(
                QPointF(
                    pos[0]+icon[j].values[0]*scale[0],
                    pos[1]+icon[j].values[1]*scale[1]
                ),
                icon[j].values[2]*scale[0],
                icon[j].values[3]*scale[1]);
            break;
        default:
            break;
        }
    }
}

