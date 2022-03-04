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
 * This is the heart of the program, we're working on replacing
 * the Qt reliance, so these functions and data represent the eventual core
 * of the program.
 *
 * The widget system is created here, but it is built on top of the
 * SVG system created in libembroidery. So a widget is an svg drawing,
 * with a position to draw it in relative to its parent. The widgets
 * form a tree rooted at the global variable called root.
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>
#include <sys/stat.h>
#include <math.h>

#if defined(__unix__) || defined(__linux__)
#include <pwd.h>
#include <unistd.h>
#else
#include <windows.h>
#endif

#if __APPLE__
#include <OpenGL/gl.h>
#include <OpenGL/glu.h>
#else
#include <GL/gl.h>
#include <GL/glu.h>
#endif

#include "GL/freeglut.h"

#include "embroidermodder.h"

/* FUNCTION DECLARATIONS */
void clearSelection(void);
circle_args circle_init(void);

quad make_texture(xpm_texture texture);

widget *make_widget(float width, float height);
void draw_widget(widget *w);
void free_widget(widget *w);

char * copy_ini_block(int i, char *data, char *section);
int find_ini_value(char *key, char *out);
int get_ini_int(char *key, int default_value);
float get_ini_float(char *key, float default_value);
int embClamp(int lower, int x, int upper);

void mouse_callback(int button, int state, int x, int y);

/* DATA SECTION */
int debug_mode = 1;
quad quads[N_TEXTURES];
GLuint texture[N_TEXTURES];
int interaction_mode = 0;
int run = 1;
int window_width = 640;
int window_height = 480;
float mouse[2];
int mouse_x = 0;
int mouse_y = 0;
int action_id = -1;
char undo_history[1000][100];
int undo_history_length = 0;
int undo_history_position = 0;
settings_wrapper settings, preview, dialog, accept_;
const char* _appName_ = "Embroidermodder";
const char* _appVer_ = "v2.0 alpha";
int exitApp = 0;
widget *root;
char assets_dir[1000];
char settings_fname[1000];
char settings_data[5000];
char value_out[1000];
int settings_data_length;
float aspect = 640.0/480.0;
float ui_scale = 0.1;
char new_palette_symbols[] = " .+@#$%&*=-;>,')!";
int ntextures = 0;
char user_string[100];

extern int new_palette[17*3];
extern int open_palette[17*3];

xpm_texture icon_xpm[] = {
    {
        0,
        0,
        {-1.0, 1.0},
        128,
        128,
        (char*)new_palette_symbols,
        (int*)new_palette,
        (char**)new_xpm
    },
    {
        0,
        1,
        {-1.0+0.1, 1.0},
        128,
        128,
        (char*)new_palette_symbols,
        (int*)open_palette,
        (char**)open_xpm
    }
};

/* FUNCTIONS SECTION */

int new_main(int argc, char *argv[])
{
    int window, i;
    puts("FreeGLUT3 version of Embroidermodder");
    sprintf(user_string, "User String");

    root = make_widget(1.0, 1.0);

    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(window_width, window_height);
    glutInitWindowPosition(100,100);
    window = glutCreateWindow("Embroidermodder 2");
    glClearColor (0.5, 0.5, 0.5, 0.0);

    glEnable(GL_DEPTH_TEST);
    glDepthFunc(GL_LESS);
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
    glGenTextures(N_TEXTURES, texture);
    root->left = make_widget(ui_scale, ui_scale);
    root->right = make_widget(ui_scale, ui_scale);
    root->left->texture_id = 0;
    root->right->texture_id = 1;
    for (i=0; i<2; i++) {
        quads[i] = make_texture(icon_xpm[i]);
    }
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL);
    glEnable(GL_TEXTURE_2D);
    glShadeModel(GL_FLAT);
    glutDisplayFunc(display);
    glutIdleFunc(display);
    glutKeyboardFunc(key_handler);
    glutMouseFunc(mouse_callback);
    glutMainLoop();
    
    free_widget(root);
    return 0;
}

widget *make_widget(float width, float height)
{
    widget *w = (widget *)malloc(sizeof(widget));
    w->left = 0;
    w->right = 0;
    w->width = width;
    w->height = height;
    return w;
}

void draw_widget(widget *w)
{
    if (w->left > 0) {
        draw_widget(w->left);
    }
    if (w->right > 0) {
        draw_widget(w->right);
    }
    render_quad(quads[w->texture_id]);
}

void free_widget(widget *w)
{
    if (w->left > 0) {
        free_widget(w->left);
    }
    if (w->right > 0) {
        free_widget(w->right);
    }
    free(w);
}

double sgn(double x)
{
    if (x > 0.0) return 1.0;
    else if(x < 0.0) return -1.0;
    else return 0.0;
}

double theta(double x)
{
    if (x < 0.0) return 0.0;
    else return 1.0;
}

EmbVector unit_vector(float angle)
{
    EmbVector u;
    u.x = cos(angle);
    u.y = sin(angle);
    return u;
}

EmbVector rotate_vector(EmbVector a, float angle)
{
    EmbVector rot;
    EmbVector u = unit_vector(angle);
    rot.x = a.x*u.x - a.y*u.y;
    rot.y = a.x*u.y + a.y*u.x;
    return rot;
}

EmbVector scale_vector(EmbVector a, float scale)
{
    a.x *= scale;
    a.y *= scale;
    return a;
}

EmbVector scale_and_rotate(EmbVector a, float scale, float angle)
{
    a = scale_vector(a, scale);
    a = rotate_vector(a, angle);
    return a;
}


void app_dir(char *output, int folder)
{
#if defined(__unix__) || defined(__linux__)
    char *separator = "/";

    strcpy(output, getenv("HOME"));

    /* On MacOS we set a system "HOME" manually if it is not set. */
    if (!output) {
        struct passwd* pwd = getpwuid(getuid());
        if (pwd) {
            output = pwd->pw_dir;
        }
        else {
            printf("ERROR: failed to set HOME.");
        }
    }

#else
    char *separator = "\\";

    strcpy(output, getenv("HOMEDRIVE"));
    strcat(output, getenv("HOMEPATH"));
#endif

    strcat(output, separator);
    strcat(output, ".embroidermodder2");
    strcat(output, separator);

    if (folder >= 0 && folder < nFolders) {
        strcat(output, folders[folder]);
        strcat(output, separator);
    }
}

/* UTILITY FUNCTIONS FOR ALL SYSTEMS
 * These could be moved to libembroidery.
 */
void debug_message(const char *format, ...)
{
    if (debug_mode) {
        va_list args;
        va_start(args, format);
        vprintf(format, args);
        printf("\n");
        va_end(args);
    }
}

int file_exists(char *fname)
{
    struct stat stats;
    return !stat(fname, &stats);
}

void render_quad(quad q)
{
    glBindTexture(GL_TEXTURE_2D, texture[q.texture_id]);
    glBegin(GL_QUADS);
    glTexCoord2f(0.0, 0.0);
    glVertex2f(q.left, q.top);
    glTexCoord2f(0.0, 1.0);
    glVertex2f(q.left, q.bottom);
    glTexCoord2f(1.0, 1.0);
    glVertex2f(q.right, q.bottom);
    glTexCoord2f(1.0, 0.0);
    glVertex2f(q.right, q.top);
    glEnd();
}

void menu___(int key)
{
    switch (key) {
    default:
        break;
    }
}

void display()
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    if (action_id >= 0) {
        printf("%d\n", action_id);
        action_id = -1;
    }

    draw_widget(root);

    glutSwapBuffers();
}

void key_handler(int key, int x, int y)
{
    switch (key) {
    case 27:
        exit(0);
    default:
        break;
    }
}

quad make_texture(xpm_texture t)
{
    quad output;
    unsigned char data[128*128*3];
    ntextures++;
    if (t.mode == 0) {
        /* xpm-style drawing routine */
        int a, j, k, npalette, pixel;
        npalette = strlen(t.palette_symbols);
        for (a=0; a<128; a++) {
            for (j=0; j<128; j++) {
                for (k=0; k<npalette; k++) {
                    if (t.palette_symbols[k] == t.icon[1+npalette+a][j]) {
                        break;
                    }
                }
                pixel = 3*(128*(127-a)+j);
                data[pixel+0] = t.palette[3*k+0];
                data[pixel+1] = t.palette[3*k+1];
                data[pixel+2] = t.palette[3*k+2];
            }
        }
    }
    else {
        /* svg-style drawing routine */
    
    }
    output.width = t.width;
    output.height = t.height;
    output.left = t.position.x;
    output.right = t.position.x+ui_scale;
    output.top =  t.position.y-ui_scale*aspect;
    output.bottom =  t.position.y;
    output.texture_id =  t.texture_id;
    glBindTexture(GL_TEXTURE_2D, texture[t.texture_id]);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexImage2D(GL_TEXTURE_2D, 0, 3, t.width, t.height, 0,
        GL_RGB, GL_UNSIGNED_BYTE, data);
    return output;
}

char *translate(char *a)
{
    return a;
}

void
to_lower(char *dst, char *src)
{
    int i;
    for (i=0; i<MAX_STRING_LENGTH; i++) {
        if (src[i] >= 'A' && src[i] <= 'Z') {
            dst[i] = src[i] - 'A';
        }
        else {
            dst[i] = src[i];
        }
    }
}

void usage(void)
{
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
           );
    exitApp = 1;
}

void version()
{
    fprintf(stdout, "%s %s\n", _appName_, _appVer_);
    exitApp = 1;
}

void clearSelection(void)
{

}

circle_args circle_init(void)
{
    clearSelection();
    circle_args args;
    args.mode = circle_mode_1P_RAD;
    args.x1 = MAX_DISTANCE+1.0;
    args.y1 = MAX_DISTANCE+1.0;
    args.x2 = MAX_DISTANCE+1.0;
    args.y2 = MAX_DISTANCE+1.0;
    args.x3 = MAX_DISTANCE+1.0;
    args.y3 = MAX_DISTANCE+1.0;
    /*
    setPromptPrefix(qsTr("Specify center point for circle or [3P/2P/Ttr (tan tan radius)]: "));
    */
    return args;
}

void mouse_callback(int button, int state, int x, int y)
{
    if (button==GLUT_LEFT_BUTTON) {
        if (state==GLUT_DOWN) {
            int i;
            float pos_x = x/(0.5*window_width) - 1.0;
            float pos_y = -y/(0.5*window_height) + 1.0;
            mouse_x = x;
            mouse_y = y;
            for (i=0; i<2; i++) {
                if ((quads[i].left < pos_x) && (pos_x < quads[i].right))
                if ((quads[i].top < pos_y) && (pos_y < quads[i].bottom)) {
                    action_id = i;
                    break;
                }
            }
        }
    }
}

#if 0
int circle_click(circle_args *args, float x, float y)
{
    if (args.mode == args.mode_1P_RAD) {
        if(isNaN(args.x1)) {
            args.x1 = x;
            args.y1 = y;
            args.cx = x;
            args.cy = y;
            addRubber("CIRCLE");
            setRubberMode("CIRCLE_1P_RAD");
            setRubberPoint("CIRCLE_CENTER", args.cx, args.cy);
            appendPromptHistory();
            setPromptPrefix(qsTr("Specify radius of circle or [Diameter]: "));
        }
        else {
            args.x2 = x;
            args.y2 = y;
            setRubberPoint("CIRCLE_RADIUS", args.x2, args.y2);
            vulcanize();
            appendPromptHistory();
            return;
        }
    }
    else if(args.mode == circle_mode_1P_DIA) {
        if(isNaN(args.x1)) {
            error("CIRCLE", qsTr("This should never happen."));
        }
        else {
            args.x2 = x;
            args.y2 = y;
            setRubberPoint("CIRCLE_DIAMETER", args.x2, args.y2);
            vulcanize();
            appendPromptHistory();
            return;
        }
    }
    else if(args.mode == args.mode_2P) {
        if(isNaN(args.x1)) {
            args.x1 = x;
            args.y1 = y;
            addRubber("CIRCLE");
            setRubberMode("CIRCLE_2P");
            setRubberPoint("CIRCLE_TAN1", args.x1, args.y1);
            appendPromptHistory();
            setPromptPrefix(qsTr("Specify second end point of circle's diameter: "));
        }
        else if(isNaN(args.x2)) {
            args.x2 = x;
            args.y2 = y;
            setRubberPoint("CIRCLE_TAN2", args.x2, args.y2);
            vulcanize();
            appendPromptHistory();
            return;
        }
        else {
            error("CIRCLE", qsTr("This should never happen."));
        }
    }
    else if(args.mode == args.mode_3P) {
        if(isNaN(args.x1)) {
            args.x1 = x;
            args.y1 = y;
            appendPromptHistory();
            setPromptPrefix(qsTr("Specify second point on circle: "));
        }
        else if(isNaN(args.x2)) {
            args.x2 = x;
            args.y2 = y;
            addRubber("CIRCLE");
            setRubberMode("CIRCLE_3P");
            setRubberPoint("CIRCLE_TAN1", args.x1, args.y1);
            setRubberPoint("CIRCLE_TAN2", args.x2, args.y2);
            appendPromptHistory();
            setPromptPrefix(qsTr("Specify third point on circle: "));
        }
        else if(isNaN(args.x3)) {
            args.x3 = x;
            args.y3 = y;
            setRubberPoint("CIRCLE_TAN3", args.x3, args.y3);
            vulcanize();
            appendPromptHistory();
            return;
        }
        else {
            error("CIRCLE", qsTr("This should never happen."));
        }
    }
    else if(args.mode == args.mode_TTR) {
        if (isNaN(args.x1)) {
            args.x1 = x;
            args.y1 = y;
            appendPromptHistory();
            setPromptPrefix(qsTr("Specify point on object for second tangent of circle: "));
        }
        else if (isNaN(args.x2)) {
            args.x2 = x;
            args.y2 = y;
            appendPromptHistory();
            setPromptPrefix(qsTr("Specify radius of circle: "));
        }
        else if (isNaN(args.x3)) {
            args.x3 = x;
            args.y3 = y;
            appendPromptHistory();
            setPromptPrefix(qsTr("Specify second point: "));
        }
        else {
            todo("CIRCLE", "click() for TTR");
        }
    }
    return 0;
}

int circle_prompt(circle_args args, char *str)
{
    if (args.mode == args.mode_1P_RAD) {
        if (isNaN(args.x1)) {
            /* TODO: Probably should add additional qsTr calls here. */
            if (!strcmp(str, "2P")) {
                args.mode = args.mode_2P;
                setPromptPrefix(qsTr("Specify first end point of circle's diameter: "));
            }
            /* TODO: Probably should add additional qsTr calls here. */
            else if (!strcmp(str, "3P")) {
                args.mode = args.mode_3P;
                setPromptPrefix(qsTr("Specify first point of circle: "));
            }
            /* TODO: Probably should add additional qsTr calls here. */
            else if (!strcmp(str, "T") || !strcmp(str, "TTR")) {
                args.mode = args.mode_TTR;
                setPromptPrefix(qsTr("Specify point on object for first tangent of circle: "));
            }
            else {
                var strList = str.split(",");
                if (isNaN(strList[0]) || isNaN(strList[1])) {
                    alert(qsTr("Point or option keyword required."));
                    setPromptPrefix(qsTr("Specify center point for circle or [3P/2P/Ttr (tan tan radius)]: "));
                }
                else {
                    args.x1 = Number(strList[0]);
                    args.y1 = Number(strList[1]);
                    args.cx = args.x1;
                    args.cy = args.y1;
                    addRubber("CIRCLE");
                    setRubberMode("CIRCLE_1P_RAD");
                    setRubberPoint("CIRCLE_CENTER", args.cx, args.cy);
                    setPromptPrefix(qsTr("Specify radius of circle or [Diameter]: "));
                }
            }
        }
        else {
            /* TODO: Probably should add additional qsTr calls here. */
            if (!strcmp(str, "D") || !strcmp(str, "DIAMETER")) {
                args.mode = circle_mode_1P_DIA;
                setRubberMode("CIRCLE_1P_DIA");
                setPromptPrefix(qsTr("Specify diameter of circle: "));
            }
            else {
                float num = Number(str);
                if (isNaN(num)) {
                    alert(qsTr("Requires numeric radius, point on circumference, or \"D\"."));
                    setPromptPrefix(qsTr("Specify radius of circle or [Diameter]: "));
                }
                else {
                    args.rad = num;
                    args.x2 = args.x1 + args.rad;
                    args.y2 = args.y1;
                    setRubberPoint("CIRCLE_RADIUS", args.x2, args.y2);
                    vulcanize();
                    return;
                }
            }
        }
    }
    else if (args.mode == circle_mode_1P_DIA) {
        if (isNaN(args.x1)) {
            error("CIRCLE", qsTr("This should never happen."));
        }
        if (isNaN(args.x2)) {
            var num = Number(str);
            if(isNaN(num))
            {
                alert(qsTr("Requires numeric distance or second point."));
                setPromptPrefix(qsTr("Specify diameter of circle: "));
            }
            else
            {
                args.dia = num;
                args.x2 = args.x1 + args.dia;
                args.y2 = args.y1;
                setRubberPoint("CIRCLE_DIAMETER", args.x2, args.y2);
                vulcanize();
                return;
            }
        }
        else
        {
            error("CIRCLE", qsTr("This should never happen."));
        }
    }
    else if(args.mode == args.mode_2P)
    {
        if(isNaN(args.x1))
        {
            var strList = str.split(",");
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(qsTr("Invalid point."));
                setPromptPrefix(qsTr("Specify first end point of circle's diameter: "));
            }
            else
            {
                args.x1 = Number(strList[0]);
                args.y1 = Number(strList[1]);
                addRubber("CIRCLE");
                setRubberMode("CIRCLE_2P");
                setRubberPoint("CIRCLE_TAN1", args.x1, args.y1);
                setPromptPrefix(qsTr("Specify second end point of circle's diameter: "));
            }
        }
        else if(isNaN(args.x2))
        {
            var strList = str.split(",");
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(qsTr("Invalid point."));
                setPromptPrefix(qsTr("Specify second end point of circle's diameter: "));
            }
            else
            {
                args.x2 = Number(strList[0]);
                args.y2 = Number(strList[1]);
                setRubberPoint("CIRCLE_TAN2", args.x2, args.y2);
                vulcanize();
                return;
            }
        }
        else
        {
            error("CIRCLE", qsTr("This should never happen."));
        }
    }
    else if(args.mode == args.mode_3P)
    {
        if(isNaN(args.x1))
        {
            var strList = str.split(",");
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(qsTr("Invalid point."));
                setPromptPrefix(qsTr("Specify first point of circle: "));
            }
            else
            {
                args.x1 = Number(strList[0]);
                args.y1 = Number(strList[1]);
                setPromptPrefix(qsTr("Specify second point of circle: "));
            }
        }
        else if(isNaN(args.x2))
        {
            var strList = str.split(",");
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(qsTr("Invalid point."));
                setPromptPrefix(qsTr("Specify second point of circle: "));
            }
            else
            {
                args.x2 = Number(strList[0]);
                args.y2 = Number(strList[1]);
                addRubber("CIRCLE");
                setRubberMode("CIRCLE_3P");
                setRubberPoint("CIRCLE_TAN1", args.x1, args.y1);
                setRubberPoint("CIRCLE_TAN2", args.x2, args.y2);
                setPromptPrefix(qsTr("Specify third point of circle: "));
            }
        }
        else if(isNaN(args.x3)) {
            var strList = str.split(",");
            if (isNaN(strList[0]) || isNaN(strList[1])) {
                alert(qsTr("Invalid point."));
                setPromptPrefix(qsTr("Specify third point of circle: "));
            }
            else {                
                args.x3 = Number(strList[0]);
                args.y3 = Number(strList[1]);
                setRubberPoint("CIRCLE_TAN3", args.x3, args.y3);
                vulcanize();
                return;
            }
        }
        else
        {
            error("CIRCLE", qsTr("This should never happen."));
        }
        
    }
    else if(args.mode == args.mode_TTR) {
        todo("CIRCLE", "prompt() for TTR");
    }
    return 0;
}

/* -------------------------------------------------------------------------------- */

EmbLine line_init(void)
{
    EmbLine line;
    clearSelection();
    args.x1 = MAX_DISTANCE+1.0;
    args.y1 = MAX_DISTANCE+1.0;
    args.x2 = MAX_DISTANCE+1.0;
    args.y2 = MAX_DISTANCE+1.0;
    setPromptPrefix(qsTr("Specify first point: "));
    return line;
}

int line_click(float x, float y)
{
    if(isNaN(args.x1))
    {
        args.x1 = x;
        args.y1 = y;
        addRubber("LINE");
        setRubberMode("LINE");
        setRubberPoint("LINE_START", args.x1, args.y1);
        appendPromptHistory();
        setPromptPrefix(qsTr("Specify second point: "));
    }
    else
    {
        appendPromptHistory();
        args.x2 = x;
        args.y2 = y;
        reportDistance();
        return;
    }
}

int prompt(str)
{
    var strList = str.split(",");
    if (isNaN(args.x1)) {
        if (isNaN(strList[0]) || isNaN(strList[1])) {
            alert(qsTr("Requires numeric distance or two points."));
            setPromptPrefix(qsTr("Specify first point: "));
        }
        else {
            args.x1 = Number(strList[0]);
            args.y1 = Number(strList[1]);
            addRubber("LINE");
            setRubberMode("LINE");
            setRubberPoint("LINE_START", args.x1, args.y1);
            setPromptPrefix(qsTr("Specify second point: "));
        }
    }
    else
    {
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(qsTr("Requires numeric distance or two points."));
            setPromptPrefix(qsTr("Specify second point: "));
        }
        else
        {
            args.x2 = Number(strList[0]);
            args.y2 = Number(strList[1]);
            reportDistance();
            return;
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

int reportDistance(void)
{
    var dx = args.x2 - args.x1;
    var dy = args.y2 - args.y1;

    var dist = calculateDistance(args.x1,args.y1,args.x2, args.y2);
    var angle = calculateAngle(args.x1,args.y1,args.x2, args.y2);

    setPromptPrefix(qsTr("Distance") + " = " + dist.toString() + ", " + qsTr("Angle") + " = " + angle.toString());
    appendPromptHistory();
    setPromptPrefix(qsTr("Delta X") + " = " + dx.toString() + ", " + qsTr("Delta Y") + " = " + dy.toString());
    appendPromptHistory();
}

/* ---------------------------------------------------------------------- */

dolphin_args dolphin_init(void)
{
    dolphin_args args;
    clearSelection();
    args.numPoints = 512; /*Default //TODO: min:64 max:8192*/
    args.cx = MAX_DISTANCE+1.0;
    args.cy = MAX_DISTANCE+1.0;
    args.sx = 0.04; /*Default*/
    args.sy = 0.04; /*Default*/
    args.mode = DOLPHIN_MODE_NUM_POINTS;


    addRubber("POLYGON");
    setRubberMode("POLYGON");
    updateDolphin(args, args.numPoints, args.sx, args.sy);
    spareRubber("POLYGON");
    return args;
}
#endif

#define basis_func(A, B, C, D, E) (A/B)*sin(C*t+(D/E))

int dolphin_update(dolphin_args args, int numPts, float xScale, float yScale)
{
    int i;

    for (i=0; i<=numPts; i++) {
        float t, xx, yy;
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
        5/16*sin(59*t+32/39);

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
        34/25*sin(54*t+37/26);

        /*
        setRubberPoint("POLYGON_POINT_" + i.toString(), xx*xScale, yy*yScale);
        */
    }

    /*
    setRubberText("POLYGON_NUM_POINTS", numPts.toString()); */
    return 0;
}

#if 0

/* ---------------------------------------------------------------------- */

ellipse_args ellipse_init(void)
{
    ellipse_args args;
    clearSelection();
    args.mode = ELLIPSE_MAJORDIAMETER_MINORRADIUS;
    args.point1 = {NaN, NaN};
    args.point2 = {NaN, NaN};
    args.point3 = {NaN, NaN};
    setPromptPrefix(qsTr("Specify first axis start point or [Center]: "));
    return args;
}

int ellipse_click(EmbVector point)
{
    if (args.mode == ELLIPSE_MAJORDIAMETER_MINORRADIUS) {
        if (isNaN(args.x1)) {
            args.point1 = point;
            addRubber("ELLIPSE");
            setRubberMode("ELLIPSE_LINE");
            setRubberPoint("ELLIPSE_LINE_POINT1", args.x1, args.y1);
            appendPromptHistory();
            setPromptPrefix(qsTr("Specify first axis end point: "));
        }
        else if (isNaN(args.x2)) {
            args.point2 = point;
            args.cx = (args.x1 + args.x2)/2.0;
            args.cy = (args.y1 + args.y2)/2.0;
            args.width = calculateDistance(args.x1, args.y1, args.x2, args.y2);
            args.rot = calculateAngle(args.x1, args.y1, args.x2, args.y2);
            setRubberMode("ELLIPSE_MAJORDIAMETER_MINORRADIUS");
            setRubberPoint("ELLIPSE_AXIS1_POINT1", args.x1, args.y1);
            setRubberPoint("ELLIPSE_AXIS1_POINT2", args.x2, args.y2);
            setRubberPoint("ELLIPSE_CENTER", args.cx, args.cy);
            setRubberPoint("ELLIPSE_WIDTH", args.width, 0);
            setRubberPoint("ELLIPSE_ROT", args.rot, 0);
            appendPromptHistory();
            setPromptPrefix(qsTr("Specify second axis end point or [Rotation]: "));
        }
        else if (isNaN(args.x3)) {
            args.x3 = x;
            args.y3 = y;
            args.height = perpendicularDistance(args.x3, args.y3, args.x1, args.y1, args.x2, args.y2)*2.0;
            setRubberPoint("ELLIPSE_AXIS2_POINT2", args.x3, args.y3);
            vulcanize();
            appendPromptHistory();
            return;
        }
        else {
            error("ELLIPSE", qsTr("This should never happen."));
        }
    }
    else if (args.mode == ELLIPSE_MAJORRADIUS_MINORRADIUS) {
        if (isNaN(args.x1)) {
            args.x1 = x;
            args.y1 = y;
            args.cx = args.x1;
            args.cy = args.y1;
            addRubber("ELLIPSE");
            setRubberMode("ELLIPSE_LINE");
            setRubberPoint("ELLIPSE_LINE_POINT1", args.x1, args.y1);
            setRubberPoint("ELLIPSE_CENTER", args.cx, args.cy);
            appendPromptHistory();
            setPromptPrefix(qsTr("Specify first axis end point: "));
        }
        else if(isNaN(args.x2)) {
            args.x2 = x;
            args.y2 = y;
            args.width = calculateDistance(args.cx, args.cy, args.x2, args.y2)*2.0;
            args.rot = calculateAngle(args.x1, args.y1, args.x2, args.y2);
            setRubberMode("ELLIPSE_MAJORRADIUS_MINORRADIUS");
            setRubberPoint("ELLIPSE_AXIS1_POINT2", args.x2, args.y2);
            setRubberPoint("ELLIPSE_WIDTH", args.width, 0);
            setRubberPoint("ELLIPSE_ROT", args.rot, 0);
            appendPromptHistory();
            setPromptPrefix(qsTr("Specify second axis end point or [Rotation]: "));
        }
        else if(isNaN(args.x3)) {
            args.x3 = x;
            args.y3 = y;
            args.height = perpendicularDistance(args.x3, args.y3, args.cx, args.cy, args.x2, args.y2)*2.0;
            setRubberPoint("ELLIPSE_AXIS2_POINT2", args.x3, args.y3);
            vulcanize();
            appendPromptHistory();
            return;
        }
        else {
            error("ELLIPSE", qsTr("This should never happen."));
        }
    }
    else if(args.mode == args.mode_ELLIPSE_ROTATION) {
        if (isNaN(args.x1)) {
            error("ELLIPSE", qsTr("This should never happen."));
        }
        else if (isNaN(args.x2)) {
            error("ELLIPSE", qsTr("This should never happen."));
        }
        else if(isNaN(args.x3)) {
            var angle = calculateAngle(args.cx, args.cy, x, y);
            args.height = cos(angle*embConstantPi/180.0)*args.width;
            addEllipse(args.cx, args.cy, args.width, args.height, args.rot, false);
            appendPromptHistory();
            return;
        }
    }
}

int ellipse_prompt(str)
{
    if(args.mode == args.mode_MAJORDIAMETER_MINORRADIUS)
    {
        if(isNaN(args.x1))
        {
            if(str == "C" || str == "CENTER") /*TODO: Probably should add additional qsTr calls here.*/
            {
                args.mode = args.mode_MAJORRADIUS_MINORRADIUS;
                setPromptPrefix(qsTr("Specify center point: "));
            }
            else
            {
                var strList = str.split(",");
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(qsTr("Point or option keyword required."));
                    setPromptPrefix(qsTr("Specify first axis start point or [Center]: "));
                }
                else
                {
                    args.x1 = Number(strList[0]);
                    args.y1 = Number(strList[1]);
                    addRubber("ELLIPSE");
                    setRubberMode("ELLIPSE_LINE");
                    setRubberPoint("ELLIPSE_LINE_POINT1", args.x1, args.y1);
                    setPromptPrefix(qsTr("Specify first axis end point: "));
                }
            }
        }
        else if(isNaN(args.x2))
        {
            var strList = str.split(",");
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(qsTr("Invalid point."));
                setPromptPrefix(qsTr("Specify first axis end point: "));
            }
            else
            {
                args.x2 = Number(strList[0]);
                args.y2 = Number(strList[1]);
                args.cx = (args.x1 + args.x2)/2.0;
                args.cy = (args.y1 + args.y2)/2.0;
                args.width = calculateDistance(args.x1, args.y1, args.x2, args.y2);
                args.rot = calculateAngle(args.x1, args.y1, args.x2, args.y2);
                setRubberMode("ELLIPSE_MAJORDIAMETER_MINORRADIUS");
                setRubberPoint("ELLIPSE_AXIS1_POINT1", args.x1, args.y1);
                setRubberPoint("ELLIPSE_AXIS1_POINT2", args.x2, args.y2);
                setRubberPoint("ELLIPSE_CENTER", args.cx, args.cy);
                setRubberPoint("ELLIPSE_WIDTH", args.width, 0);
                setRubberPoint("ELLIPSE_ROT", args.rot, 0);
                setPromptPrefix(qsTr("Specify second axis end point or [Rotation]: "));
            }
        }
        else if(isNaN(args.x3))
        {
            if(str == "R" || str == "ROTATION") /*TODO: Probably should add additional qsTr calls here.*/
            {
                args.mode = args.mode_ELLIPSE_ROTATION;
                setPromptPrefix(qsTr("Specify rotation: "));
            }
            else
            {
                var strList = str.split(",");
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(qsTr("Point or option keyword required."));
                    setPromptPrefix(qsTr("Specify second axis end point or [Rotation]: "));
                }
                else
                {
                    args.x3 = Number(strList[0]);
                    args.y3 = Number(strList[1]);
                    args.height = perpendicularDistance(args.x3, args.y3, args.x1, args.y1, args.x2, args.y2)*2.0;
                    setRubberPoint("ELLIPSE_AXIS2_POINT2", args.x3, args.y3);
                    vulcanize();
                    return;
                }
            }
        }
    }
    else if(args.mode == args.mode_MAJORRADIUS_MINORRADIUS)
    {
        if(isNaN(args.x1))
        {
            var strList = str.split(",");
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(qsTr("Invalid point."));
                setPromptPrefix(qsTr("Specify center point: "));
            }
            else
            {
                args.x1 = Number(strList[0]);
                args.y1 = Number(strList[1]);
                args.cx = args.x1;
                args.cy = args.y1;
                addRubber("ELLIPSE");
                setRubberMode("ELLIPSE_LINE");
                setRubberPoint("ELLIPSE_LINE_POINT1", args.x1, args.y1);
                setRubberPoint("ELLIPSE_CENTER", args.cx, args.cy);
                setPromptPrefix(qsTr("Specify first axis end point: "));
            }
        }
        else if(isNaN(args.x2))
        {
            var strList = str.split(",");
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(qsTr("Invalid point."));
                setPromptPrefix(qsTr("Specify first axis end point: "));
            }
            else
            {
                args.x2 = Number(strList[0]);
                args.y2 = Number(strList[1]);
                args.width = calculateDistance(args.x1, args.y1, args.x2, args.y2)*2.0;
                args.rot = calculateAngle(args.x1, args.y1, args.x2, args.y2);
                setRubberMode("ELLIPSE_MAJORRADIUS_MINORRADIUS");
                setRubberPoint("ELLIPSE_AXIS1_POINT2", args.x2, args.y2);
                setRubberPoint("ELLIPSE_WIDTH", args.width, 0);
                setRubberPoint("ELLIPSE_ROT", args.rot, 0);
                setPromptPrefix(qsTr("Specify second axis end point or [Rotation]: "));
            }
        }
        else if(isNaN(args.x3))
        {
            if(str == "R" || str == "ROTATION") /*TODO: Probably should add additional qsTr calls here.*/
            {
                args.mode = args.mode_ELLIPSE_ROTATION;
                setPromptPrefix(qsTr("Specify ellipse rotation: "));
            }
            else
            {
                var strList = str.split(",");
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(qsTr("Point or option keyword required."));
                    setPromptPrefix(qsTr("Specify second axis end point or [Rotation]: "));
                }
                else
                {
                    args.x3 = Number(strList[0]);
                    args.y3 = Number(strList[1]);
                    args.height = perpendicularDistance(args.x3, args.y3, args.x1, args.y1, args.x2, args.y2)*2.0;
                    setRubberPoint("ELLIPSE_AXIS2_POINT2", args.x3, args.y3);
                    vulcanize();
                    return;
                }
            }
        }
    }
    else if(args.mode == args.mode_ELLIPSE_ROTATION)
    {
        if(isNaN(args.x1))
        {
            error("ELLIPSE", qsTr("This should never happen."));
        }
        else if(isNaN(args.x2))
        {
            error("ELLIPSE", qsTr("This should never happen."));
        }
        else if(isNaN(args.x3))
        {
            if(isNaN(str))
            {
                alert(qsTr("Invalid angle. Input a numeric angle or pick a point."));
                setPromptPrefix(qsTr("Specify rotation: "));
            }
            else
            {
                var angle = Number(str);
                args.height = cos(angle*embConstantPi/180.0)*args.width;
                addEllipse(args.cx, args.cy, args.width, args.height, args.rot, false);
                return;
            }
        }
    }
}

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.numPoints = 512; /*Default //TODO: min:64 max:8192*/
args.cx;
args.cy;
args.sx = 1.0;
args.sy = 1.0;
args.numPoints;
args.mode;

/*enums*/
args.mode_NUM_POINTS = 0;
args.mode_STYLE      = 1;
args.mode_XSCALE     = 2;
args.mode_YSCALE     = 3;

int init()
{
    clearSelection();
    args.cx = MAX_DISTANCE+1.0;
    args.cy = MAX_DISTANCE+1.0;
    args.mode = args.mode_NUM_POINTS;

    /*Heart4: 10.0 / 512*/
    /*Heart5: 1.0 / 512*/

    addRubber("POLYGON");
    setRubberMode("POLYGON");
    updateHeart("HEART5", args.numPoints, args.sx, args.sy);
    spareRubber("POLYGON");
    return;
}

int updateHeart(style, numPts, xScale, yScale)
{
    var i;
    var t;
    var xx = MAX_DISTANCE+1.0;
    var yy = MAX_DISTANCE+1.0;
    var two_pi = 2*embConstantPi;

    for(i = 0; i <= numPts; i++)
    {
        t = two_pi/numPts*i; 

        if(style == "HEART4")
        {
            xx = cos(t)*((sin(t)*sqrt(abs(cos(t))))/(sin(t)+7/5) - 2*sin(t) + 2);
            yy = sin(t)*((sin(t)*sqrt(abs(cos(t))))/(sin(t)+7/5) - 2*sin(t) + 2);
        }
        else if(style == "HEART5")
        {
            xx = 16*pow(sin(t), 3);
            yy = 13*cos(t) - 5*cos(2*t) - 2*cos(3*t) - cos(4*t);
        }

        setRubberPoint("POLYGON_POINT_" + i.toString(), xx*xScale, yy*yScale);
    }

    setRubberText("POLYGON_NUM_POINTS", numPts.toString());
}

--------------------------------------------------------------------------------


/*Command: Line*/

var global = {}; /*Required*/
args.firstRun;
args.firstX;
args.firstY;
args.prevX;
args.prevY;

int init()
{
    clearSelection();
    args.firstRun = true;
    args.firstX = MAX_DISTANCE+1.0;
    args.firstY = MAX_DISTANCE+1.0;
    args.prevX = MAX_DISTANCE+1.0;
    args.prevY = MAX_DISTANCE+1.0;
    setPromptPrefix(qsTr("Specify first point: "));
}

int click(x, y)
{
    if(args.firstRun)
    {
        args.firstRun = false;
        args.firstX = x;
        args.firstY = y;
        args.prevX = x;
        args.prevY = y;
        addRubber("LINE");
        setRubberMode("LINE");
        setRubberPoint("LINE_START", args.firstX, args.firstY);
        appendPromptHistory();
        setPromptPrefix(qsTr("Specify next point or [Undo]: "));
    }
    else
    {
        setRubberPoint("LINE_END", x, y);
        vulcanize();
        addRubber("LINE");
        setRubberMode("LINE");
        setRubberPoint("LINE_START", x, y);
        appendPromptHistory();
        args.prevX = x;
        args.prevY = y;
    }
}

int prompt(str)
{
    if(args.firstRun)
    {
        var strList = str.split(",");
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(qsTr("Invalid point."));
            setPromptPrefix(qsTr("Specify first point: "));
        }
        else
        {
            args.firstRun = false;
            args.firstX = Number(strList[0]);
            args.firstY = Number(strList[1]);
            args.prevX = args.firstX;
            args.prevY = args.firstY;
            addRubber("LINE");
            setRubberMode("LINE");
            setRubberPoint("LINE_START", args.firstX, args.firstY);
            setPromptPrefix(qsTr("Specify next point or [Undo]: "));
        }
    }
    else
    {
        if(str == "U" || str == "UNDO") /*TODO: Probably should add additional qsTr calls here.*/
        {
            todo("LINE", "prompt() for UNDO");
        }
        else
        {
            var strList = str.split(",");
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(qsTr("Point or option keyword required."));
                setPromptPrefix(qsTr("Specify next point or [Undo]: "));
            }
            else
            {
                var x = Number(strList[0]);
                var y = Number(strList[1]);
                setRubberPoint("LINE_END", x, y);
                vulcanize();
                addRubber("LINE");
                setRubberMode("LINE");
                setRubberPoint("LINE_START", x, y);
                args.prevX = x;
                args.prevY = y;
                setPromptPrefix(qsTr("Specify next point or [Undo]: "));
            }
        }
    }
}

--------------------------------------------------------------------------------

int init()
{
    clearSelection();
    setPromptPrefix(qsTr("Specify point: "));
}

int click(x, y)
{
    appendPromptHistory();
    setPromptPrefix("X = " + x.toString() + ", Y = " + y.toString());
    appendPromptHistory();
    return;
}

int prompt(str)
{
    var strList = str.split(",");
    if(isNaN(strList[0]) || isNaN(strList[1]))
    {
        alert(qsTr("Invalid point."));
        setPromptPrefix(qsTr("Specify point: "));
    }
    else
    {
        appendPromptHistory();
        setPromptPrefix("X = " + strList[0].toString() + ", Y = " + strList[1].toString());
        appendPromptHistory();
        return;
    }
}

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.firstRun;
args.baseX;
args.baseY;
args.destX;
args.destY;
args.deltaX;
args.deltaY;

int init()
{
    args.firstRun = true;
    args.baseX  = MAX_DISTANCE+1.0;
    args.baseY  = MAX_DISTANCE+1.0;
    args.destX  = MAX_DISTANCE+1.0;
    args.destY  = MAX_DISTANCE+1.0;
    args.deltaX = MAX_DISTANCE+1.0;
    args.deltaY = MAX_DISTANCE+1.0;

    if(numSelected() <= 0)
    {
        /*TODO: Prompt to select objects if nothing is preselected*/
        alert(qsTr("Preselect objects before invoking the move command."));
        return;
        messageBox("information", qsTr("Move Preselect"), qsTr("Preselect objects before invoking the move command."));
    }
    else
    {
        setPromptPrefix(qsTr("Specify base point: "));
    }
}

int click(x, y)
{
    if(args.firstRun)
    {
        args.firstRun = false;
        args.baseX = x;
        args.baseY = y;
        addRubber("LINE");
        setRubberMode("LINE");
        setRubberPoint("LINE_START", args.baseX, args.baseY);
        previewOn("SELECTED", "MOVE", args.baseX, args.baseY, 0);
        appendPromptHistory();
        setPromptPrefix(qsTr("Specify destination point: "));
    }
    else
    {
        args.destX = x;
        args.destY = y;
        args.deltaX = args.destX - args.baseX;
        args.deltaY = args.destY - args.baseY;
        moveSelected(args.deltaX, args.deltaY);
        previewOff();
        return;
    }
}

int prompt(str)
{
    if(args.firstRun)
    {
        var strList = str.split(",");
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(qsTr("Invalid point."));
            setPromptPrefix(qsTr("Specify base point: "));
        }
        else
        {
            args.firstRun = false;
            args.baseX = Number(strList[0]);
            args.baseY = Number(strList[1]);
            addRubber("LINE");
            setRubberMode("LINE");
            setRubberPoint("LINE_START", args.baseX, args.baseY);
            previewOn("SELECTED", "MOVE", args.baseX, args.baseY, 0);
            setPromptPrefix(qsTr("Specify destination point: "));
        }
    }
    else
    {
        var strList = str.split(",");
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(qsTr("Invalid point."));
            setPromptPrefix(qsTr("Specify destination point: "));
        }
        else
        {
            args.destX = Number(strList[0]);
            args.destY = Number(strList[1]);
            args.deltaX = args.destX - args.baseX;
            args.deltaY = args.destY - args.baseY;
            moveSelected(args.deltaX, args.deltaY);
            previewOff();
            return;
        }
    }
}

--------------------------------------------------------------------------------

/*TODO: The path command is currently broken*/

var global = {}; /*Required*/
args.firstRun;
args.firstX;
args.firstY;
args.prevX;
args.prevY;

int init()
{
    clearSelection();
    args.firstRun = true;
    args.firstX = MAX_DISTANCE+1.0;
    args.firstY = MAX_DISTANCE+1.0;
    args.prevX = MAX_DISTANCE+1.0;
    args.prevY = MAX_DISTANCE+1.0;
    setPromptPrefix(qsTr("Specify start point: "));
}

int click(x, y)
{
    if(args.firstRun)
    {
        args.firstRun = false;
        args.firstX = x;
        args.firstY = y;
        args.prevX = x;
        args.prevY = y;
        addPath(x,y);
        appendPromptHistory();
        setPromptPrefix(qsTr("Specify next point or [Arc/Undo]: "));
    }
    else
    {
        appendPromptHistory();
        appendLineToPath(x,y);
        args.prevX = x;
        args.prevY = y;
    }
}

int prompt(str)
{
    if(str == "A" || str == "ARC")/*TODO: Probably should add additional qsTr calls here.*/
    {
        todo("PATH", "prompt() for ARC");
    }
    else if(str == "U" || str == "UNDO") /*TODO: Probably should add additional qsTr calls here.*/
    {
        todo("PATH", "prompt() for UNDO");
    }
    else
    {
        var strList = str.split(",");
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(qsTr("Point or option keyword required."));
            setPromptPrefix(qsTr("Specify next point or [Arc/Undo]: "));
        }
        else
        {
            var x = Number(strList[0]);
            var y = Number(strList[1]);
            if(args.firstRun)
            {
                args.firstRun = false;
                args.firstX = x;
                args.firstY = y;
                args.prevX = x;
                args.prevY = y;
                addPath(x,y);
                setPromptPrefix(qsTr("Specify next point or [Arc/Undo]: "));
            }
            else
            {
                appendLineToPath(x,y);
                args.prevX = x;
                args.prevY = y;
            }
        }
    }
}

int init()
{
    clearSelection();
    reportPlatform();
    return;
}

int reportPlatform()
{
    setPromptPrefix(qsTr("Platform") + " = " + platformString());
    appendPromptHistory();
}

/* ------------------------------------------------------------------------- */

var global = {}; /*Required*/
args.firstRun;

int point_init()
{
    clearSelection();
    args.firstRun = true;
    setPromptPrefix("TODO: Current point settings: PDMODE=?  PDSIZE=?"); /*TODO: qsTr needed here when complete*/
    appendPromptHistory();
    setPromptPrefix(qsTr("Specify first point: "));
}

int point_click(x, y)
{
    if(args.firstRun) {
        args.firstRun = false;
        appendPromptHistory();
        setPromptPrefix(qsTr("Specify next point: "));
        addPoint(x,y);
    }
    else {
        appendPromptHistory();
        addPoint(x,y);
    }
}

int prompt(str)
{
    if (args.firstRun) {
        if(str == "M" || str == "MODE") {
            /*TODO: Probably should add additional qsTr calls here.*/
            todo("POINT", "prompt() for PDMODE");
        }
        else if(str == "S" || str == "SIZE") {
            /*TODO: Probably should add additional qsTr calls here.*/
            todo("POINT", "prompt() for PDSIZE");
        }
        var strList = str.split(",");
        if (isNaN(strList[0]) || isNaN(strList[1])) {
            alert(qsTr("Invalid point."));
            setPromptPrefix(qsTr("Specify first point: "));
        }
        else
        {
            args.firstRun = false;
            var x = Number(strList[0]);
            var y = Number(strList[1]);
            setPromptPrefix(qsTr("Specify next point: "));
            addPoint(x,y);
        }
    }
    else
    {
        var strList = str.split(",");
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(qsTr("Invalid point."));
            setPromptPrefix(qsTr("Specify next point: "));
        }
        else
        {
            var x = Number(strList[0]);
            var y = Number(strList[1]);
            setPromptPrefix(qsTr("Specify next point: "));
            addPoint(x,y);
        }
    }
}

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.centerX;
args.centerY;
args.sideX1;
args.sideY1;
args.sideX2;
args.sideY2;
args.pointIX;
args.pointIY;
args.pointCX;
args.pointCY;
args.polyType = "Inscribed"; /*Default*/
args.numSides = 4;           /*Default*/
args.mode;


int init()
{
    clearSelection();
    args.center.x = MAX_DISTANCE+1.0;
    args.center.y = MAX_DISTANCE+1.0;
    args.sideX1  = MAX_DISTANCE+1.0;
    args.sideY1  = MAX_DISTANCE+1.0;
    args.sideX2  = MAX_DISTANCE+1.0;
    args.sideY2  = MAX_DISTANCE+1.0;
    args.pointIX = MAX_DISTANCE+1.0;
    args.pointIY = MAX_DISTANCE+1.0;
    args.pointCX = MAX_DISTANCE+1.0;
    args.pointCY = MAX_DISTANCE+1.0;
    args.mode = #define POLYGON_NUM_SIDES;
    setPromptPrefix(qsTr("Enter number of sides") + " {" + args.numSides.toString() + "}: ");
}

int click(x, y)
{
    if (args.mode == POLYGON_NUM_SIDES) {
        /*Do nothing, the prompt controls this.*/
    }
    else if (args.mode == POLYGON_CENTER_PT) {
        args.centerX = x;
        args.centerY = y;
        args.mode = args.mode_POLYTYPE;
        appendPromptHistory();
        setPromptPrefix(qsTr("Specify polygon type [Inscribed in circle/Circumscribed around circle]") + " {" + args.polyType + "}: ");
    }
    else if(args.mode == args.mode_POLYTYPE)
    {
        /*Do nothing, the prompt controls this.*/
    }
    else if(args.mode == args.mode_INSCRIBE)
    {
        args.pointIX = x;
        args.pointIY = y;
        setRubberPoint("POLYGON_INSCRIBE_POINT", args.pointIX, args.pointIY);
        vulcanize();
        appendPromptHistory();
        return;
    }
    else if(args.mode == args.mode_CIRCUMSCRIBE)
    {
        args.pointCX = x;
        args.pointCY = y;
        setRubberPoint("POLYGON_CIRCUMSCRIBE_POINT", args.pointCX, args.pointCY);
        vulcanize();
        appendPromptHistory();
        return;
    }
    else if(args.mode == args.mode_DISTANCE)
    {
        /*Do nothing, the prompt controls this.*/
    }
    else if(args.mode == args.mode_SIDE_LEN)
    {
        todo("POLYGON", "Sidelength mode");
    }
}

int prompt(str)
{
    if(args.mode == args.mode_NUM_SIDES)
    {
        if(str == "" && args.numSides >= 3 && args.numSides <= 1024)
        {
            setPromptPrefix(qsTr("Specify center point or [Sidelength]: "));
            args.mode = args.mode_CENTER_PT;
        }
        else
        {
            var tmp = Number(str);
            if(isNaN(tmp) || !isInt(tmp) || tmp < 3 || tmp > 1024)
            {
                alert(qsTr("Requires an integer between 3 and 1024."));
                setPromptPrefix(qsTr("Enter number of sides") + " {" + args.numSides.toString() + "}: ");
            }
            else
            {
                args.numSides = tmp;
                setPromptPrefix(qsTr("Specify center point or [Sidelength]: "));
                args.mode = args.mode_CENTER_PT;
            }
        }
    }
    else if(args.mode == args.mode_CENTER_PT)
    {
        if(str == "S" || str == "SIDELENGTH") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SIDE_LEN;
            setPromptPrefix(qsTr("Specify start point: "));
        }
        else
        {
            var strList = str.split(",");
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(qsTr("Point or option keyword required."));
                setPromptPrefix(qsTr("Specify center point or [Sidelength]: "));
            }
            else
            {
                args.centerX = Number(strList[0]);
                args.centerY = Number(strList[1]);
                args.mode = args.mode_POLYTYPE;
                setPromptPrefix(qsTr("Specify polygon type [Inscribed in circle/Circumscribed around circle]") + " {" + args.polyType + "}: ");
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
            args.mode = args.mode_INSCRIBE;
            args.polyType = "Inscribed";
            setPromptPrefix(qsTr("Specify polygon corner point or [Distance]: "));
            addRubber("POLYGON");
            setRubberMode("POLYGON_INSCRIBE");
            setRubberPoint("POLYGON_CENTER", args.centerX, args.centerY);
            setRubberPoint("POLYGON_NUM_SIDES", args.numSides, 0);
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
            args.mode = args.mode_CIRCUMSCRIBE;
            args.polyType = "Circumscribed";
            setPromptPrefix(qsTr("Specify polygon side point or [Distance]: "));
            addRubber("POLYGON");
            setRubberMode("POLYGON_CIRCUMSCRIBE");
            setRubberPoint("POLYGON_CENTER", args.centerX, args.centerY);
            setRubberPoint("POLYGON_NUM_SIDES", args.numSides, 0);
        }
        else if(str == "")
        {
            if(args.polyType == "Inscribed")
            {
                args.mode = args.mode_INSCRIBE;
                setPromptPrefix(qsTr("Specify polygon corner point or [Distance]: "));
                addRubber("POLYGON");
                setRubberMode("POLYGON_INSCRIBE");
                setRubberPoint("POLYGON_CENTER", args.centerX, args.centerY);
                setRubberPoint("POLYGON_NUM_SIDES", args.numSides, 0);
            }
            else if(args.polyType == "Circumscribed")
            {
                args.mode = args.mode_CIRCUMSCRIBE;
                setPromptPrefix(qsTr("Specify polygon side point or [Distance]: "));
                addRubber("POLYGON");
                setRubberMode("POLYGON_CIRCUMSCRIBE");
                setRubberPoint("POLYGON_CENTER", args.centerX, args.centerY);
                setRubberPoint("POLYGON_NUM_SIDES", args.numSides, 0);
            }
            else
            {
                error("POLYGON", qsTr("Polygon type is not Inscribed or Circumscribed."));
            }
        }
        else
        {
            alert(qsTr("Invalid option keyword."));
            setPromptPrefix(qsTr("Specify polygon type [Inscribed in circle/Circumscribed around circle]") + " {" + args.polyType + "}: ");
        }
    }
    else if(args.mode == args.mode_INSCRIBE)
    {
        if(str == "D" || str == "DISTANCE") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_DISTANCE;
            setPromptPrefix(qsTr("Specify distance: "));
        }
        else
        {
            var strList = str.split(",");
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(qsTr("Point or option keyword required."));
                setPromptPrefix(qsTr("Specify polygon corner point or [Distance]: "));
            }
            else
            {
                args.pointIX = Number(strList[0]);
                args.pointIY = Number(strList[1]);
                setRubberPoint("POLYGON_INSCRIBE_POINT", args.pointIX, args.pointIY);
                vulcanize();
                return;
            }
        }
    }
    else if(args.mode == args.mode_CIRCUMSCRIBE)
    {
        if(str == "D" || str == "DISTANCE") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_DISTANCE;
            setPromptPrefix(qsTr("Specify distance: "));
        }
        else
        {
            var strList = str.split(",");
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(qsTr("Point or option keyword required."));
                setPromptPrefix(qsTr("Specify polygon side point or [Distance]: "));
            }
            else
            {
                args.pointCX = Number(strList[0]);
                args.pointCY = Number(strList[1]);
                setRubberPoint("POLYGON_CIRCUMSCRIBE_POINT", args.pointCX, args.pointCY);
                vulcanize();
                return;
            }
        }
    }
    else if(args.mode == args.mode_DISTANCE)
    {
        if(isNaN(str))
        {
            alert(qsTr("Requires valid numeric distance."));
            setPromptPrefix(qsTr("Specify distance: "));
        }
        else
        {
            if(args.polyType == "Inscribed")
            {
                args.pointIX = args.centerX;
                args.pointIY = args.centerY + Number(str);
                setRubberPoint("POLYGON_INSCRIBE_POINT", args.pointIX, args.pointIY);
                vulcanize();
                return;
            }
            else if(args.polyType == "Circumscribed")
            {
                args.pointCX = args.centerX;
                args.pointCY = args.centerY + Number(str);
                setRubberPoint("POLYGON_CIRCUMSCRIBE_POINT", args.pointCX, args.pointCY);
                vulcanize();
                return;
            }
            else
            {
                error("POLYGON", qsTr("Polygon type is not Inscribed or Circumscribed."));
            }
        }
    }
    else if(args.mode == args.mode_SIDE_LEN)
    {
        todo("POLYGON", "Sidelength mode");
    }
}

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.firstRun;
args.firstX;
args.firstY;
args.prevX;
args.prevY;
args.num;

int init()
{
    clearSelection();
    args.firstRun = true;
    args.firstX = MAX_DISTANCE+1.0;
    args.firstY = MAX_DISTANCE+1.0;
    args.prevX = MAX_DISTANCE+1.0;
    args.prevY = MAX_DISTANCE+1.0;
    args.num = 0;
    setPromptPrefix(qsTr("Specify first point: "));
}

int click(x, y)
{
    if(args.firstRun)
    {
        args.firstRun = false;
        args.firstX = x;
        args.firstY = y;
        args.prevX = x;
        args.prevY = y;
        addRubber("POLYLINE");
        setRubberMode("POLYLINE");
        setRubberPoint("POLYLINE_POINT_0", args.firstX, args.firstY);
        appendPromptHistory();
        setPromptPrefix(qsTr("Specify next point or [Undo]: "));
    }
    else
    {
        args.num++;
        setRubberPoint("POLYLINE_POINT_" + args.num.toString(), x, y);
        setRubberText("POLYLINE_NUM_POINTS", args.num.toString());
        spareRubber("POLYLINE");
        appendPromptHistory();
        args.prevX = x;
        args.prevY = y;
    }
}

int prompt(str)
{
    if(args.firstRun)
    {
        var strList = str.split(",");
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(qsTr("Invalid point."));
            setPromptPrefix(qsTr("Specify first point: "));
        }
        else
        {
            args.firstRun = false;
            args.firstX = Number(strList[0]);
            args.firstY = Number(strList[1]);
            args.prevX = args.firstX;
            args.prevY = args.firstY;
            addRubber("POLYLINE");
            setRubberMode("POLYLINE");
            setRubberPoint("POLYLINE_POINT_0", args.firstX, args.firstY);
            setPromptPrefix(qsTr("Specify next point or [Undo]: "));
        }
    }
    else
    {
        if(str == "U" || str == "UNDO") /*TODO: Probably should add additional qsTr calls here.*/
        {
            todo("POLYLINE", "prompt() for UNDO");
        }
        else
        {
            var strList = str.split(",");
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(qsTr("Point or option keyword required."));
                setPromptPrefix(qsTr("Specify next point or [Undo]: "));
            }
            else
            {
                var x = Number(strList[0]);
                var y = Number(strList[1]);
                args.num++;
                setRubberPoint("POLYLINE_POINT_" + args.num.toString(), x, y);
                setRubberText("POLYLINE_NUM_POINTS", args.num.toString());
                spareRubber("POLYLINE");
                args.prevX = x;
                args.prevY = y;
                setPromptPrefix(qsTr("Specify next point or [Undo]: "));
            }
        }
    }
}

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.x1;
args.y1;
args.x2;
args.y2;

/*TODO: Adding the text is not complete yet.*/

int init()
{
    clearSelection();
    args.x1 = MAX_DISTANCE+1.0;
    args.y1 = MAX_DISTANCE+1.0;
    args.x2 = MAX_DISTANCE+1.0;
    args.y2 = MAX_DISTANCE+1.0;
    setPromptPrefix(qsTr("Specify first point: "));
}

int click(x, y)
{
    if(isNaN(args.x1))
    {
        args.x1 = x;
        args.y1 = y;
        addRubber("DIMLEADER");
        setRubberMode("DIMLEADER_LINE");
        setRubberPoint("DIMLEADER_LINE_START", args.x1, args.y1);
        appendPromptHistory();
        setPromptPrefix(qsTr("Specify second point: "));
    }
    else
    {
        args.x2 = x;
        args.y2 = y;
        setRubberPoint("DIMLEADER_LINE_END", args.x2, args.y2);
        vulcanize();
        appendPromptHistory();
        return;
    }
}

int prompt(str)
{
    var strList = str.split(",");
    if(isNaN(args.x1))
    {
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(qsTr("Requires two points."));
            setPromptPrefix(qsTr("Specify first point: "));
        }
        else
        {
            args.x1 = Number(strList[0]);
            args.y1 = Number(strList[1]);
            addRubber("DIMLEADER");
            setRubberMode("DIMLEADER_LINE");
            setRubberPoint("DIMLEADER_LINE_START", args.x1, args.y1);
            setPromptPrefix(qsTr("Specify second point: "));
        }
    }
    else
    {
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(qsTr("Requires two points."));
            setPromptPrefix(qsTr("Specify second point: "));
        }
        else
        {
            args.x2 = Number(strList[0]);
            args.y2 = Number(strList[1]);
            setRubberPoint("DIMLEADER_LINE_END", args.x2, args.y2);
            vulcanize();
            return;
        }
    }
}
--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.newRect;
args.x1;
args.y1;
args.x2;
args.y2;

int init()
{
    clearSelection();
    args.newRect = true;
    args.x1 = MAX_DISTANCE+1.0;
    args.y1 = MAX_DISTANCE+1.0;
    args.x2 = MAX_DISTANCE+1.0;
    args.y2 = MAX_DISTANCE+1.0;
    setPromptPrefix(qsTr("Specify first corner point or [Chamfer/Fillet]: "));
}

int click(x, y)
{
    if(args.newRect)
    {
        args.newRect = false;
        args.x1 = x;
        args.y1 = y;
        addRubber("RECTANGLE");
        setRubberMode("RECTANGLE");
        setRubberPoint("RECTANGLE_START", x, y);
        setPromptPrefix(qsTr("Specify other corner point or [Dimensions]: "));
    }
    else
    {
        args.newRect = true;
        args.x2 = x;
        args.y2 = y;
        setRubberPoint("RECTANGLE_END", x, y);
        vulcanize();
        return;
    }
}

int prompt(str)
{
    if(str == "C" || str == "CHAMFER") /*TODO: Probably should add additional qsTr calls here.*/
    {
        todo("RECTANGLE", "prompt() for CHAMFER");
    }
    else if(str == "D" || str == "DIMENSIONS") /*TODO: Probably should add additional qsTr calls here.*/
    {
        todo("RECTANGLE", "prompt() for DIMENSIONS");
    }
    else if(str == "F" || str == "FILLET") /*TODO: Probably should add additional qsTr calls here.*/
    {
        todo("RECTANGLE", "prompt() for FILLET");
    }
    else
    {
        var strList = str.split(",");
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(qsTr("Invalid point."));
            setPromptPrefix(qsTr("Specify first point: "));
        }
        else
        {
            var x = Number(strList[0]);
            var y = Number(strList[1]);
            if(args.newRect)
            {
                args.newRect = false;
                args.x1 = x;
                args.y1 = y;
                addRubber("RECTANGLE");
                setRubberMode("RECTANGLE");
                setRubberPoint("RECTANGLE_START", x, y);
                setPromptPrefix(qsTr("Specify other corner point or [Dimensions]: "));
            }
            else
            {
                args.newRect = true;
                args.x2 = x;
                args.y2 = y;
                setRubberPoint("RECTANGLE_END", x, y);
                vulcanize();
                return;
            }
        }
    }
}

---------------------------------------------------------------------------------

var global = {}; /*Required*/
args.mode;

/*enums*/
args.mode_BACKGROUND = 0;
args.mode_CROSSHAIR  = 1;
args.mode_GRID       = 2;

int init()
{
    clearSelection();
    args.mode = args.mode_BACKGROUND;
    setPromptPrefix(qsTr("Enter RED,GREEN,BLUE values for background or [Crosshair/Grid]: "));
}

int prompt(str)
{
    if(args.mode == args.mode_BACKGROUND)
    {
        if(str == "C" || str == "CROSSHAIR") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_CROSSHAIR;
            setPromptPrefix(qsTr("Specify crosshair color: "));
        }
        else if(str == "G" || str == "GRID") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_GRID;
            setPromptPrefix(qsTr("Specify grid color: "));
        }
        else
        {
            var strList = str.split(",");
            var r = Number(strList[0]);
            var g = Number(strList[1]);
            var b = Number(strList[2]);
            if(!validRGB(r,g,b))
            {
                alert(qsTr("Invalid color. R,G,B values must be in the range of 0-255."));
                setPromptPrefix(qsTr("Specify background color: "));
            }
            else
            {
                setBackgroundColor(r,g,b);
                return;
            }
        }
    }
    else if(args.mode == args.mode_CROSSHAIR)
    {
        var strList = str.split(",");
        var r = Number(strList[0]);
        var g = Number(strList[1]);
        var b = Number(strList[2]);
        if(!validRGB(r,g,b))
        {
            alert(qsTr("Invalid color. R,G,B values must be in the range of 0-255."));
            setPromptPrefix(qsTr("Specify crosshair color: "));
        }
        else
        {
            setCrossHairColor(r,g,b);
            return;
        }
    }
    else if(args.mode == args.mode_GRID)
    {
        var strList = str.split(",");
        var r = Number(strList[0]);
        var g = Number(strList[1]);
        var b = Number(strList[2]);
        if(!validRGB(r,g,b))
        {
            alert(qsTr("Invalid color. R,G,B values must be in the range of 0-255."));
            setPromptPrefix(qsTr("Specify grid color: "));
        }
        else
        {
            setGridColor(r,g,b);
            return;
        }
    }
}

int validRGB(r, g, b)
{
    if(isNaN(r)) return false;
    if(isNaN(g)) return false;
    if(isNaN(b)) return false;
    if(r < 0 || r > 255) return false;
    if(g < 0 || g > 255) return false;
    if(b < 0 || b > 255) return false;
    return true;
}

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.firstRun;
args.baseX;
args.baseY;
args.destX;
args.destY;
args.angle;

args.baseRX;
args.baseRY;
args.destRX;
args.destRY;
args.angleRef;
args.angleNew;

args.mode;

/*enums*/
args.mode_NORMAL    = 0;
args.mode_REFERENCE = 1;

int init()
{
    args.mode = args.mode_NORMAL;
    args.firstRun = true;
    args.baseX = MAX_DISTANCE+1.0;
    args.baseY = MAX_DISTANCE+1.0;
    args.destX = MAX_DISTANCE+1.0;
    args.destY = MAX_DISTANCE+1.0;
    args.angle = MAX_DISTANCE+1.0;

    args.baseRX   = MAX_DISTANCE+1.0;
    args.baseRY   = MAX_DISTANCE+1.0;
    args.destRX   = MAX_DISTANCE+1.0;
    args.destRY   = MAX_DISTANCE+1.0;
    args.angleRef = MAX_DISTANCE+1.0;
    args.angleNew = MAX_DISTANCE+1.0;

    if(numSelected() <= 0)
    {
        /*TODO: Prompt to select objects if nothing is preselected*/
        alert(qsTr("Preselect objects before invoking the rotate command."));
        return;
        messageBox("information", qsTr("Rotate Preselect"), qsTr("Preselect objects before invoking the rotate command."));
    }
    else
    {
        setPromptPrefix(qsTr("Specify base point: "));
    }
}

int click(x, y)
{
    if(args.mode == args.mode_NORMAL)
    {
        if(args.firstRun)
        {
            args.firstRun = false;
            args.baseX = x;
            args.baseY = y;
            addRubber("LINE");
            setRubberMode("LINE");
            setRubberPoint("LINE_START", args.baseX, args.baseY);
            previewOn("SELECTED", "ROTATE", args.baseX, args.baseY, 0);
            appendPromptHistory();
            setPromptPrefix(qsTr("Specify rotation angle or [Reference]: "));
        }
        else
        {
            args.destX = x;
            args.destY = y;
            args.angle = calculateAngle(args.baseX, args.baseY, args.destX, args.destY);
            appendPromptHistory();
            rotateSelected(args.baseX, args.baseY, args.angle);
            previewOff();
            return;
        }
    }
    else if(args.mode == args.mode_REFERENCE)
    {
        if(isNaN(args.baseRX))
        {
            args.baseRX = x;
            args.baseRY = y;
            appendPromptHistory();
            addRubber("LINE");
            setRubberMode("LINE");
            setRubberPoint("LINE_START", args.baseRX, args.baseRY);
            setPromptPrefix(qsTr("Specify second point: "));
        }
        else if(isNaN(args.destRX))
        {
            args.destRX = x;
            args.destRY = y;
            args.angleRef = calculateAngle(args.baseRX, args.baseRY, args.destRX, args.destRY);
            setRubberPoint("LINE_START", args.baseX, args.baseY);
            previewOn("SELECTED", "ROTATE", args.baseX, args.baseY, args.angleRef);
            appendPromptHistory();
            setPromptPrefix(qsTr("Specify the new angle: "));
        }
        else if(isNaN(args.angleNew))
        {
            args.angleNew = calculateAngle(args.baseX, args.baseY, x, y);
            rotateSelected(args.baseX, args.baseY, args.angleNew - args.angleRef);
            previewOff();
            return;
        }
    }
}

int prompt(str)
{
    if(args.mode == args.mode_NORMAL)
    {
        if(args.firstRun)
        {
            var strList = str.split(",");
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(qsTr("Invalid point."));
                setPromptPrefix(qsTr("Specify base point: "));
            }
            else
            {
                args.firstRun = false;
                args.baseX = Number(strList[0]);
                args.baseY = Number(strList[1]);
                addRubber("LINE");
                setRubberMode("LINE");
                setRubberPoint("LINE_START", args.baseX, args.baseY);
                previewOn("SELECTED", "ROTATE", args.baseX, args.baseY, 0);
                setPromptPrefix(qsTr("Specify rotation angle or [Reference]: "));
            }
        }
        else
        {
            if(str == "R" || str == "REFERENCE") /*TODO: Probably should add additional qsTr calls here.*/
            {
                args.mode = args.mode_REFERENCE;
                setPromptPrefix(qsTr("Specify the reference angle") + " {0.00}: ");
                clearRubber();
                previewOff();
            }
            else
            {
                if(isNaN(str))
                {
                    alert(qsTr("Requires valid numeric angle, second point, or option keyword."));
                    setPromptPrefix(qsTr("Specify rotation angle or [Reference]: "));
                }
                else
                {
                    args.angle = Number(str);
                    rotateSelected(args.baseX, args.baseY, args.angle);
                    previewOff();
                    return;
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
                var strList = str.split(",");
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(qsTr("Requires valid numeric angle or two points."));
                    setPromptPrefix(qsTr("Specify the reference angle") + " {0.00}: ");
                }
                else
                {
                    args.baseRX = Number(strList[0]);
                    args.baseRY = Number(strList[1]);
                    addRubber("LINE");
                    setRubberMode("LINE");
                    setRubberPoint("LINE_START", args.baseRX, args.baseRY);
                    setPromptPrefix(qsTr("Specify second point: "));
                }
            }
            else
            {
                /*The base and dest values are only set here to advance the command.*/
                args.baseRX = 0.0;
                args.baseRY = 0.0;
                args.destRX = 0.0;
                args.destRY = 0.0;
                /*The reference angle is what we will use later.*/
                args.angleRef = Number(str);
                addRubber("LINE");
                setRubberMode("LINE");
                setRubberPoint("LINE_START", args.baseX, args.baseY);
                previewOn("SELECTED", "ROTATE", args.baseX, args.baseY, args.angleRef);
                setPromptPrefix(qsTr("Specify the new angle: "));
            }
        }
        else if(isNaN(args.destRX))
        {
            if(isNaN(str))
            {
                var strList = str.split(",");
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(qsTr("Requires valid numeric angle or two points."));
                    setPromptPrefix(qsTr("Specify second point: "));
                }
                else
                {
                    args.destRX = Number(strList[0]);
                    args.destRY = Number(strList[1]);
                    args.angleRef = calculateAngle(args.baseRX, args.baseRY, args.destRX, args.destRY);
                    previewOn("SELECTED", "ROTATE", args.baseX, args.baseY, args.angleRef);
                    setRubberPoint("LINE_START", args.baseX, args.baseY);
                    setPromptPrefix(qsTr("Specify the new angle: "));
                }
            }
            else
            {
                /*The base and dest values are only set here to advance the command.*/
                args.baseRX = 0.0;
                args.baseRY = 0.0;
                args.destRX = 0.0;
                args.destRY = 0.0;
                /*The reference angle is what we will use later.*/
                args.angleRef = Number(str);
                previewOn("SELECTED", "ROTATE", args.baseX, args.baseY, args.angleRef);
                setPromptPrefix(qsTr("Specify the new angle: "));
            }
        }
        else if(isNaN(args.angleNew))
        {
            if(isNaN(str))
            {
                var strList = str.split(",");
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(qsTr("Requires valid numeric angle or second point."));
                    setPromptPrefix(qsTr("Specify the new angle: "));
                }
                else
                {
                    var x = Number(strList[0]);
                    var y = Number(strList[1]);
                    args.angleNew = calculateAngle(args.baseX, args.baseY, x, y);
                    rotateSelected(args.baseX, args.baseY, args.angleNew - args.angleRef);
                    previewOff();
                    return;
                }
            }
            else
            {
                args.angleNew = Number(str);
                rotateSelected(args.baseX, args.baseY, args.angleNew - args.angleRef);
                previewOff();
                return;
            }
        }
    }
}

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.test1;
args.test2;

int init()
{
    /*Report number of pre-selected objects*/
    setPromptPrefix("Number of Objects Selected: " + numSelected().toString());
    appendPromptHistory();
    
    mirrorSelected(0,0,0,1);
    
    /*selectAll();*/
    /*rotateSelected(0,0,90);*/
    
    /*Polyline & Polygon Testing*/
    
    var offsetX = 0.0;
    var offsetY = 0.0;
    
    var polylineArray = [];
    polylineArray.push(1.0 + offsetX);
    polylineArray.push(1.0 + offsetY);
    polylineArray.push(1.0 + offsetX);
    polylineArray.push(2.0 + offsetY);
    polylineArray.push(2.0 + offsetX);
    polylineArray.push(2.0 + offsetY);
    polylineArray.push(2.0 + offsetX);
    polylineArray.push(3.0 + offsetY);
    polylineArray.push(3.0 + offsetX);
    polylineArray.push(3.0 + offsetY);
    polylineArray.push(3.0 + offsetX);
    polylineArray.push(2.0 + offsetY);
    polylineArray.push(4.0 + offsetX);
    polylineArray.push(2.0 + offsetY);
    polylineArray.push(4.0 + offsetX);
    polylineArray.push(1.0 + offsetY);
    addPolyline(polylineArray);
    
    offsetX = 5.0;
    offsetY = 0.0;
    
    var polygonArray = [];
    polygonArray.push(1.0 + offsetX);
    polygonArray.push(1.0 + offsetY);
    polygonArray.push(1.0 + offsetX);
    polygonArray.push(2.0 + offsetY);
    polygonArray.push(2.0 + offsetX);
    polygonArray.push(2.0 + offsetY);
    polygonArray.push(2.0 + offsetX);
    polygonArray.push(3.0 + offsetY);
    polygonArray.push(3.0 + offsetX);
    polygonArray.push(3.0 + offsetY);
    polygonArray.push(3.0 + offsetX);
    polygonArray.push(2.0 + offsetY);
    polygonArray.push(4.0 + offsetX);
    polygonArray.push(2.0 + offsetY);
    polygonArray.push(4.0 + offsetX);
    polygonArray.push(1.0 + offsetY);
    addPolygon(polygonArray);
    

    return;
}

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.firstRun;
args.baseX;
args.baseY;
args.destX;
args.destY;
args.factor;

args.baseRX;
args.baseRY;
args.destRX;
args.destRY;
args.factorRef;
args.factorNew;

args.mode;

/*enums*/
args.mode_NORMAL    = 0;
args.mode_REFERENCE = 1;

int init()
{
    args.mode = args.mode_NORMAL;
    args.firstRun = true;
    args.baseX  = MAX_DISTANCE+1.0;
    args.baseY  = MAX_DISTANCE+1.0;
    args.destX  = MAX_DISTANCE+1.0;
    args.destY  = MAX_DISTANCE+1.0;
    args.factor = MAX_DISTANCE+1.0;

    args.baseRX    = MAX_DISTANCE+1.0;
    args.baseRY    = MAX_DISTANCE+1.0;
    args.destRX    = MAX_DISTANCE+1.0;
    args.destRY    = MAX_DISTANCE+1.0;
    args.factorRef = MAX_DISTANCE+1.0;
    args.factorNew = MAX_DISTANCE+1.0;

    if(numSelected() <= 0)
    {
        /*TODO: Prompt to select objects if nothing is preselected*/
        alert(qsTr("Preselect objects before invoking the scale command."));
        return;
        messageBox("information", qsTr("Scale Preselect"), qsTr("Preselect objects before invoking the scale command."));
    }
    else
    {
        setPromptPrefix(qsTr("Specify base point: "));
    }
}

int click(x, y)
{
    if(args.mode == args.mode_NORMAL)
    {
        if(args.firstRun)
        {
            args.firstRun = false;
            args.baseX = x;
            args.baseY = y;
            addRubber("LINE");
            setRubberMode("LINE");
            setRubberPoint("LINE_START", args.baseX, args.baseY);
            previewOn("SELECTED", "SCALE", args.baseX, args.baseY, 1);
            appendPromptHistory();
            setPromptPrefix(qsTr("Specify scale factor or [Reference]: "));
        }
        else
        {
            args.destX = x;
            args.destY = y;
            args.factor = calculateDistance(args.baseX, args.baseY, args.destX, args.destY);
            appendPromptHistory();
            scaleSelected(args.baseX, args.baseY, args.factor);
            previewOff();
            return;
        }
    }
    else if(args.mode == args.mode_REFERENCE)
    {
        if(isNaN(args.baseRX))
        {
            args.baseRX = x;
            args.baseRY = y;
            appendPromptHistory();
            addRubber("LINE");
            setRubberMode("LINE");
            setRubberPoint("LINE_START", args.baseRX, args.baseRY);
            setPromptPrefix(qsTr("Specify second point: "));
        }
        else if(isNaN(args.destRX))
        {
            args.destRX = x;
            args.destRY = y;
            args.factorRef = calculateDistance(args.baseRX, args.baseRY, args.destRX, args.destRY);
            if(args.factorRef <= 0.0)
            {
                args.destRX    = MAX_DISTANCE+1.0;
                args.destRY    = MAX_DISTANCE+1.0;
                args.factorRef = MAX_DISTANCE+1.0;
                alert(qsTr("Value must be positive and nonzero."));
                setPromptPrefix(qsTr("Specify second point: "));
            }
            else
            {
                appendPromptHistory();
                setRubberPoint("LINE_START", args.baseX, args.baseY);
                previewOn("SELECTED", "SCALE", args.baseX, args.baseY, args.factorRef);
                setPromptPrefix(qsTr("Specify new length: "));
            }
        }
        else if(isNaN(args.factorNew))
        {
            args.factorNew = calculateDistance(args.baseX, args.baseY, x, y);
            if(args.factorNew <= 0.0)
            {
                args.factorNew = MAX_DISTANCE+1.0;
                alert(qsTr("Value must be positive and nonzero."));
                setPromptPrefix(qsTr("Specify new length: "));
            }
            else
            {
                appendPromptHistory();
                scaleSelected(args.baseX, args.baseY, args.factorNew/args.factorRef);
                previewOff();
                return;
            }
        }
    }
}

int prompt(str)
{
    if(args.mode == args.mode_NORMAL)
    {
        if(args.firstRun)
        {
            var strList = str.split(",");
            if(isNaN(strList[0]) || isNaN(strList[1]))
            {
                alert(qsTr("Invalid point."));
                setPromptPrefix(qsTr("Specify base point: "));
            }
            else
            {
                args.firstRun = false;
                args.baseX = Number(strList[0]);
                args.baseY = Number(strList[1]);
                addRubber("LINE");
                setRubberMode("LINE");
                setRubberPoint("LINE_START", args.baseX, args.baseY);
                previewOn("SELECTED", "SCALE", args.baseX, args.baseY, 1);
                setPromptPrefix(qsTr("Specify scale factor or [Reference]: "));
            }
        }
        else
        {
            if(str == "R" || str == "REFERENCE") /*TODO: Probably should add additional qsTr calls here.*/
            {
                args.mode = args.mode_REFERENCE;
                setPromptPrefix(qsTr("Specify reference length") + " {1}: ");
                clearRubber();
                previewOff();
            }
            else
            {
                if(isNaN(str))
                {
                    alert(qsTr("Requires valid numeric distance, second point, or option keyword."));
                    setPromptPrefix(qsTr("Specify scale factor or [Reference]: "));
                }
                else
                {
                    args.factor = Number(str);
                    scaleSelected(args.baseX, args.baseY, args.factor);
                    previewOff();
                    return;
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
                var strList = str.split(",");
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(qsTr("Requires valid numeric distance or two points."));
                    setPromptPrefix(qsTr("Specify reference length") + " {1}: ");
                }
                else
                {
                    args.baseRX = Number(strList[0]);
                    args.baseRY = Number(strList[1]);
                    addRubber("LINE");
                    setRubberMode("LINE");
                    setRubberPoint("LINE_START", args.baseRX, args.baseRY);
                    setPromptPrefix(qsTr("Specify second point: "));
                }
            }
            else
            {
                /*The base and dest values are only set here to advance the command.*/
                args.baseRX = 0.0;
                args.baseRY = 0.0;
                args.destRX = 0.0;
                args.destRY = 0.0;
                /*The reference length is what we will use later.*/
                args.factorRef = Number(str);
                if(args.factorRef <= 0.0)
                {
                    args.baseRX    = MAX_DISTANCE+1.0;
                    args.baseRY    = MAX_DISTANCE+1.0;
                    args.destRX    = MAX_DISTANCE+1.0;
                    args.destRY    = MAX_DISTANCE+1.0;
                    args.factorRef = MAX_DISTANCE+1.0;
                    alert(qsTr("Value must be positive and nonzero."));
                    setPromptPrefix(qsTr("Specify reference length") + " {1}: ");
                }
                else
                {
                    addRubber("LINE");
                    setRubberMode("LINE");
                    setRubberPoint("LINE_START", args.baseX, args.baseY);
                    previewOn("SELECTED", "SCALE", args.baseX, args.baseY, args.factorRef);
                    setPromptPrefix(qsTr("Specify new length: "));
                }
            }
        }
        else if(isNaN(args.destRX))
        {
            if(isNaN(str))
            {
                var strList = str.split(",");
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(qsTr("Requires valid numeric distance or two points."));
                    setPromptPrefix(qsTr("Specify second point: "));
                }
                else
                {
                    args.destRX = Number(strList[0]);
                    args.destRY = Number(strList[1]);
                    args.factorRef = calculateDistance(args.baseRX, args.baseRY, args.destRX, args.destRY);
                    if(args.factorRef <= 0.0)
                    {
                        args.destRX    = MAX_DISTANCE+1.0;
                        args.destRY    = MAX_DISTANCE+1.0;
                        args.factorRef = MAX_DISTANCE+1.0;
                        alert(qsTr("Value must be positive and nonzero."));
                        setPromptPrefix(qsTr("Specify second point: "));
                    }
                    else
                    {
                        setRubberPoint("LINE_START", args.baseX, args.baseY);
                        previewOn("SELECTED", "SCALE", args.baseX, args.baseY, args.factorRef);
                        setPromptPrefix(qsTr("Specify new length: "));
                    }
                }
            }
            else
            {
                /*The base and dest values are only set here to advance the command.*/
                args.baseRX = 0.0;
                args.baseRY = 0.0;
                args.destRX = 0.0;
                args.destRY = 0.0;
                /*The reference length is what we will use later.*/
                args.factorRef = Number(str);
                if(args.factorRef <= 0.0)
                {
                    args.destRX    = MAX_DISTANCE+1.0;
                    args.destRY    = MAX_DISTANCE+1.0;
                    args.factorRef = MAX_DISTANCE+1.0;
                    alert(qsTr("Value must be positive and nonzero."));
                    setPromptPrefix(qsTr("Specify second point: "));
                }
                else
                {
                    setRubberPoint("LINE_START", args.baseX, args.baseY);
                    previewOn("SELECTED", "SCALE", args.baseX, args.baseY, args.factorRef);
                    setPromptPrefix(qsTr("Specify new length: "));
                }
            }
        }
        else if(isNaN(args.factorNew))
        {
            if(isNaN(str))
            {
                var strList = str.split(",");
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(qsTr("Requires valid numeric distance or second point."));
                    setPromptPrefix(qsTr("Specify new length: "));
                }
                else
                {
                    var x = Number(strList[0]);
                    var y = Number(strList[1]);
                    args.factorNew = calculateDistance(args.baseX, args.baseY, x, y);
                    if(args.factorNew <= 0.0)
                    {
                        args.factorNew = MAX_DISTANCE+1.0;
                        alert(qsTr("Value must be positive and nonzero."));
                        setPromptPrefix(qsTr("Specify new length: "));
                    }
                    else
                    {
                        scaleSelected(args.baseX, args.baseY, args.factorNew/args.factorRef);
                        previewOff();
                        return;
                    }
                }
            }
            else
            {
                args.factorNew = Number(str);
                if(args.factorNew <= 0.0)
                {
                    args.factorNew = MAX_DISTANCE+1.0;
                    alert(qsTr("Value must be positive and nonzero."));
                    setPromptPrefix(qsTr("Specify new length: "));
                }
                else
                {
                    scaleSelected(args.baseX, args.baseY, args.factorNew/args.factorRef);
                    previewOff();
                    return;
                }
            }
        }
    }
}

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.text;
args.textX;
args.textY;
args.textJustify;
args.textFont;
args.textHeight;
args.textRotation;
args.mode;

/*enums*/
args.mode_JUSTIFY = 0;
args.mode_SETFONT = 1;
args.mode_SETGEOM = 2;
args.mode_RAPID   = 3;

int init()
{
    clearSelection();
    args.text = "";
    args.textX = MAX_DISTANCE+1.0;
    args.textY = MAX_DISTANCE+1.0;
    args.textJustify = "Left";
    args.textFont = textFont();
    args.textHeight = MAX_DISTANCE+1.0;
    args.textRotation = MAX_DISTANCE+1.0;
    args.mode = args.mode_SETGEOM;
    setPromptPrefix(qsTr("Current font: ") + "{" + args.textFont + "} " + qsTr("Text height: ") + "{" +  textSize() + "}");
    appendPromptHistory();
    setPromptPrefix(qsTr("Specify start point of text or [Justify/Setfont]: "));
}

int click(x, y)
{
    if(args.mode == args.mode_SETGEOM)
    {
        if(isNaN(args.textX))
        {
            args.textX = x;
            args.textY = y;
            addRubber("LINE");
            setRubberMode("LINE");
            setRubberPoint("LINE_START", args.textX, args.textY);
            appendPromptHistory();
            setPromptPrefix(qsTr("Specify text height") + " {" + textSize() + "}: ");
        }
        else if(isNaN(args.textHeight))
        {
            args.textHeight = calculateDistance(args.textX, args.textY, x, y);
            setTextSize(args.textHeight);
            appendPromptHistory();
            setPromptPrefix(qsTr("Specify text angle") + " {" + textAngle() + "}: ");
        }
        else if(isNaN(args.textRotation))
        {
            args.textRotation = calculateAngle(args.textX, args.textY, x, y);
            setTextAngle(args.textRotation);
            appendPromptHistory();
            setPromptPrefix(qsTr("Enter text: "));
            args.mode = args.mode_RAPID;
            enablePromptRapidFire();
            clearRubber();
            addRubber("TEXTSINGLE");
            setRubberMode("TEXTSINGLE");
            setRubberPoint("TEXT_POINT", args.textX, args.textY);
            setRubberPoint("TEXT_HEIGHT_ROTATION", args.textHeight, args.textRotation);
            setRubberText("TEXT_FONT", args.textFont);
            setRubberText("TEXT_JUSTIFY", args.textJustify);
            setRubberText("TEXT_RAPID", args.text);
        }
        else
        {
            /*Do nothing, as we are in rapidFire mode now.*/
        }
    }
}

int prompt(str)
{
    if(args.mode == args.mode_JUSTIFY)
    {
        if(str == "C" || str == "CENTER") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM;
            args.textJustify = "Center";
            setRubberText("TEXT_JUSTIFY", args.textJustify);
            setPromptPrefix(qsTr("Specify center point of text or [Justify/Setfont]: "));
        }
        else if(str == "R" || str == "RIGHT") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM;
            args.textJustify = "Right";
            setRubberText("TEXT_JUSTIFY", args.textJustify);
            setPromptPrefix(qsTr("Specify right-end point of text or [Justify/Setfont]: "));
        }
        else if(str == "A" || str == "ALIGN") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM;
            args.textJustify = "Aligned";
            setRubberText("TEXT_JUSTIFY", args.textJustify);
            setPromptPrefix(qsTr("Specify start point of text or [Justify/Setfont]: "));
        }
        else if(str == "M" || str == "MIDDLE") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM;
            args.textJustify = "Middle";
            setRubberText("TEXT_JUSTIFY", args.textJustify);
            setPromptPrefix(qsTr("Specify middle point of text or [Justify/Setfont]: "));
        }
        else if(str == "F" || str == "FIT") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM;
            args.textJustify = "Fit";
            setRubberText("TEXT_JUSTIFY", args.textJustify);
            setPromptPrefix(qsTr("Specify start point of text or [Justify/Setfont]: "));
        }
        else if(str == "TL" || str == "TOPLEFT") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM;
            args.textJustify = "Top Left";
            setRubberText("TEXT_JUSTIFY", args.textJustify);
            setPromptPrefix(qsTr("Specify top-left point of text or [Justify/Setfont]: "));
        }
        else if(str == "TC" || str == "TOPCENTER") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM;
            args.textJustify = "Top Center";
            setRubberText("TEXT_JUSTIFY", args.textJustify);
            setPromptPrefix(qsTr("Specify top-center point of text or [Justify/Setfont]: "));
        }
        else if(str == "TR" || str == "TOPRIGHT") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM;
            args.textJustify = "Top Right";
            setRubberText("TEXT_JUSTIFY", args.textJustify);
            setPromptPrefix(qsTr("Specify top-right point of text or [Justify/Setfont]: "));
        }
        else if(str == "ML" || str == "MIDDLELEFT") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM;
            args.textJustify = "Middle Left";
            setRubberText("TEXT_JUSTIFY", args.textJustify);
            setPromptPrefix(qsTr("Specify middle-left point of text or [Justify/Setfont]: "));
        }
        else if(str == "MC" || str == "MIDDLECENTER") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM;
            args.textJustify = "Middle Center";
            setRubberText("TEXT_JUSTIFY", args.textJustify);
            setPromptPrefix(qsTr("Specify middle-center point of text or [Justify/Setfont]: "));
        }
        else if(str == "MR" || str == "MIDDLERIGHT") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM;
            args.textJustify = "Middle Right";
            setRubberText("TEXT_JUSTIFY", args.textJustify);
            setPromptPrefix(qsTr("Specify middle-right point of text or [Justify/Setfont]: "));
        }
        else if(str == "BL" || str == "BOTTOMLEFT") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM;
            args.textJustify = "Bottom Left";
            setRubberText("TEXT_JUSTIFY", args.textJustify);
            setPromptPrefix(qsTr("Specify bottom-left point of text or [Justify/Setfont]: "));
        }
        else if(str == "BC" || str == "BOTTOMCENTER") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM;
            args.textJustify = "Bottom Center";
            setRubberText("TEXT_JUSTIFY", args.textJustify);
            setPromptPrefix(qsTr("Specify bottom-center point of text or [Justify/Setfont]: "));
        }
        else if(str == "BR" || str == "BOTTOMRIGHT") /*TODO: Probably should add additional qsTr calls here.*/
        {
            args.mode = args.mode_SETGEOM;
            args.textJustify = "Bottom Right";
            setRubberText("TEXT_JUSTIFY", args.textJustify);
            setPromptPrefix(qsTr("Specify bottom-right point of text or [Justify/Setfont]: "));
        }
        else
        {
            alert(qsTr("Invalid option keyword."));
            setPromptPrefix(qsTr("Text Justification Options [Center/Right/Align/Middle/Fit/TL/TC/TR/ML/MC/MR/BL/BC/BR]: "));
        }
    }
    else if(args.mode == args.mode_SETFONT)
    {
        args.mode = args.mode_SETGEOM;
        args.textFont = str;
        setRubberText("TEXT_FONT", args.textFont);
        setTextFont(args.textFont);
        setPromptPrefix(qsTr("Specify start point of text or [Justify/Setfont]: "));
    }
    else if(args.mode == args.mode_SETGEOM)
    {
        if(isNaN(args.textX))
        {
            if(str == "J" || str == "JUSTIFY") /*TODO: Probably should add additional qsTr calls here.*/
            {
                args.mode = args.mode_JUSTIFY;
                setPromptPrefix(qsTr("Text Justification Options [Center/Right/Align/Middle/Fit/TL/TC/TR/ML/MC/MR/BL/BC/BR]: "));
            }
            else if(str == "S" || str == "SETFONT") /*TODO: Probably should add additional qsTr calls here.*/
            {
                args.mode = args.mode_SETFONT;
                setPromptPrefix(qsTr("Specify font name: "));
            }
            else
            {
                var strList = str.split(",");
                if(isNaN(strList[0]) || isNaN(strList[1]))
                {
                    alert(qsTr("Point or option keyword required."));
                    setPromptPrefix(qsTr("Specify start point of text or [Justify/Setfont]: "));
                }
                else
                {
                    args.textX = Number(strList[0]);
                    args.textY = Number(strList[1]);
                    addRubber("LINE");
                    setRubberMode("LINE");
                    setRubberPoint("LINE_START", args.textX, args.textY);
                    setPromptPrefix(qsTr("Specify text height") + " {" + textSize() + "}: ");
                }
            }
        }
        else if(isNaN(args.textHeight))
        {
            if(str == "")
            {
                args.textHeight = textSize();
                setPromptPrefix(qsTr("Specify text angle") + " {" + textAngle() + "}: ");
            }
            else if(isNaN(str))
            {
                alert(qsTr("Requires valid numeric distance or second point."));
                setPromptPrefix(qsTr("Specify text height") + " {" + textSize() + "}: ");
            }
            else
            {
                args.textHeight = Number(str);
                setTextSize(args.textHeight);
                setPromptPrefix(qsTr("Specify text angle") + " {" + textAngle() + "}: ");
            }
        }
        else if(isNaN(args.textRotation))
        {
            if(str == "")
            {
                args.textRotation = textAngle();
                setPromptPrefix(qsTr("Enter text: "));
                args.mode = args.mode_RAPID;
                enablePromptRapidFire();
                clearRubber();
                addRubber("TEXTSINGLE");
                setRubberMode("TEXTSINGLE");
                setRubberPoint("TEXT_POINT", args.textX, args.textY);
                setRubberPoint("TEXT_HEIGHT_ROTATION", args.textHeight, args.textRotation);
                setRubberText("TEXT_FONT", args.textFont);
                setRubberText("TEXT_JUSTIFY", args.textJustify);
                setRubberText("TEXT_RAPID", args.text);
            }
            else if(isNaN(str))
            {
                alert(qsTr("Requires valid numeric angle or second point."));
                setPromptPrefix(qsTr("Specify text angle") + " {" + textAngle() + "}: ");
            }
            else
            {
                args.textRotation = Number(str);
                setTextAngle(args.textRotation);
                setPromptPrefix(qsTr("Enter text: "));
                args.mode = args.mode_RAPID;
                enablePromptRapidFire();
                clearRubber();
                addRubber("TEXTSINGLE");
                setRubberMode("TEXTSINGLE");
                setRubberPoint("TEXT_POINT", args.textX, args.textY);
                setRubberPoint("TEXT_HEIGHT_ROTATION", args.textHeight, args.textRotation);
                setRubberText("TEXT_FONT", args.textFont);
                setRubberText("TEXT_JUSTIFY", args.textJustify);
                setRubberText("TEXT_RAPID", args.text);
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
                return;
            }
            else
            {
                vulcanize();
                return; /*TODO: Rather than ending the command, calculate where the next line would be and modify the x/y to the new point*/
            }
        }
        else
        {
            args.text = str;
            setRubberText("TEXT_RAPID", args.text);
        }
    }
}

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.numPoints = 2048; /*Default //TODO: min:64 max:8192*/
args.cx;
args.cy;
args.sx = 0.04; /*Default*/
args.sy = 0.04; /*Default*/
args.numPoints;
args.mode;

/*enums*/
args.mode_NUM_POINTS = 0;
args.mode_XSCALE     = 1;
args.mode_YSCALE     = 2;

int init()
{
    clearSelection();
    args.cx = MAX_DISTANCE+1.0;
    args.cy = MAX_DISTANCE+1.0;
    args.mode = args.mode_NUM_POINTS;

    addRubber("POLYGON");
    setRubberMode("POLYGON");
    updateSnowflake(args.numPoints, args.sx, args.sy);
    spareRubber("POLYGON");
    return;
}

int updateSnowflake(numPts, xScale, yScale)
{
    var i;
    var t;
    var xx = MAX_DISTANCE+1.0;
    var yy = MAX_DISTANCE+1.0;
    var two_pi = 2*embConstantPi;

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
33/32*sin(312*t+1/2);

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
7/15*sin(313*t+1/3);

        setRubberPoint("POLYGON_POINT_" + i.toString(), xx*xScale, yy*yScale);
    }

    setRubberText("POLYGON_NUM_POINTS", numPts.toString());
}

--------------------------------------------------------------------------------

var global = {}; /*Required*/
args.numPoints = 5; /*Default*/
args.cx;
args.cy;
args.x1;
args.y1;
args.x2;
args.y2;
args.mode;

/*enums*/
args.mode_NUM_POINTS = 0;
args.mode_CENTER_PT  = 1;
args.mode_RAD_OUTER  = 2;
args.mode_RAD_INNER  = 3;

int init()
{
    clearSelection();
    args.cx       = MAX_DISTANCE+1.0;
    args.cy       = MAX_DISTANCE+1.0;
    args.x1       = MAX_DISTANCE+1.0;
    args.y1       = MAX_DISTANCE+1.0;
    args.x2       = MAX_DISTANCE+1.0;
    args.y2       = MAX_DISTANCE+1.0;
    args.mode = args.mode_NUM_POINTS;
    setPromptPrefix(qsTr("Enter number of star points") + " {" + args.numPoints.toString() + "}: ");
}

int click(x, y)
{
    if(args.mode == args.mode_NUM_POINTS)
    {
        /*Do nothing, the prompt controls this.*/
    }
    else if(args.mode == args.mode_CENTER_PT)
    {
        args.cx = x;
        args.cy = y;
        args.mode = args.mode_RAD_OUTER;
        setPromptPrefix(qsTr("Specify outer radius of star: "));
        addRubber("POLYGON");
        setRubberMode("POLYGON");
        updateStar(args.cx, args.cy);
        enableMoveRapidFire();
    }
    else if(args.mode == args.mode_RAD_OUTER)
    {
        args.x1 = x;
        args.y1 = y;
        args.mode = args.mode_RAD_INNER;
        setPromptPrefix(qsTr("Specify inner radius of star: "));
        updateStar(args.x1, args.y1);
    }
    else if(args.mode == args.mode_RAD_INNER)
    {
        args.x2 = x;
        args.y2 = y;
        disableMoveRapidFire();
        updateStar(args.x2, args.y2);
        spareRubber("POLYGON");
        return;
    }
}

int move(x, y)
{
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
        updateStar(x, y);
    }
    else if(args.mode == args.mode_RAD_INNER)
    {
        updateStar(x, y);
    }
}

int prompt(str)
{
    if(args.mode == args.mode_NUM_POINTS)
    {
        if(str == "" && args.numPoints >= 3 && args.numPoints <= 1024)
        {
            setPromptPrefix(qsTr("Specify center point: "));
            args.mode = args.mode_CENTER_PT;
        }
        else
        {
            var tmp = Number(str);
            if(isNaN(tmp) || !isInt(tmp) || tmp < 3 || tmp > 1024)
            {
                alert(qsTr("Requires an integer between 3 and 1024."));
                setPromptPrefix(qsTr("Enter number of star points") + " {" + args.numPoints.toString() + "}: ");
            }
            else
            {
                args.numPoints = tmp;
                setPromptPrefix(qsTr("Specify center point: "));
                args.mode = args.mode_CENTER_PT;
            }
        }
    }
    else if(args.mode == args.mode_CENTER_PT)
    {
        var strList = str.split(",");
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(qsTr("Invalid point."));
            setPromptPrefix(qsTr("Specify center point: "));
        }
        else
        {
            args.cx = Number(strList[0]);
            args.cy = Number(strList[1]);
            args.mode = args.mode_RAD_OUTER;
            setPromptPrefix(qsTr("Specify outer radius of star: "));
            addRubber("POLYGON");
            setRubberMode("POLYGON");
            updateStar(qsnapX(), qsnapY());
            enableMoveRapidFire();
        }
    }
    else if(args.mode == args.mode_RAD_OUTER)
    {
        var strList = str.split(",");
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(qsTr("Invalid point."));
            setPromptPrefix(qsTr("Specify outer radius of star: "));
        }
        else
        {
            args.x1 = Number(strList[0]);
            args.y1 = Number(strList[1]);
            args.mode = args.mode_RAD_INNER;
            setPromptPrefix(qsTr("Specify inner radius of star: "));
            updateStar(qsnapX(), qsnapY());
        }
    }
    else if(args.mode == args.mode_RAD_INNER)
    {
        var strList = str.split(",");
        if(isNaN(strList[0]) || isNaN(strList[1]))
        {
            alert(qsTr("Invalid point."));
            setPromptPrefix(qsTr("Specify inner radius of star: "));
        }
        else
        {
            args.x2 = Number(strList[0]);
            args.y2 = Number(strList[1]);
            disableMoveRapidFire();
            updateStar(args.x2, args.y2);
            spareRubber("POLYGON");
            return;
        }
    }
}

int updateStar(x, y)
{
    var distOuter;
    var distInner;
    var angOuter;

    if(args.mode == args.mode_RAD_OUTER)
    {
        angOuter = calculateAngle(args.cx, args.cy, x, y);
        distOuter = calculateDistance(args.cx, args.cy, x, y);
        distInner = distOuter/2.0;
    }
    else if(args.mode == args.mode_RAD_INNER)
    {
        angOuter = calculateAngle(args.cx, args.cy, args.x1, args.y1);
        distOuter = calculateDistance(args.cx, args.cy, args.x1, args.y1);
        distInner = calculateDistance(args.cx, args.cy, x, y);
    }

    /*Calculate the Star Points*/
    var angInc = 360.0/(args.numPoints*2);
    var odd = true;
    for(var i = 0; i < args.numPoints*2; i++)
    {
        var xx;
        var yy;
        if(odd)
        {
            xx = distOuter*cos((angOuter+(angInc*i))*embConstantPi/180.0);
            yy = distOuter*sin((angOuter+(angInc*i))*embConstantPi/180.0);
        }
        else
        {
            xx = distInner*cos((angOuter+(angInc*i))*embConstantPi/180.0);
            yy = distInner*sin((angOuter+(angInc*i))*embConstantPi/180.0);
        }
        odd = !odd;
        setRubberPoint("POLYGON_POINT_" + i.toString(), args.cx + xx, args.cy + yy);
    }
    setRubberText("POLYGON_NUM_POINTS", (args.numPoints*2 - 1).toString());
}

    "menu-name": "None",
    "menu-position": 0,
    "toolbar-name": "None",
    "toolbar-position": 0,
    "tooltip": "&SysWindows",
    "statustip": "Arrange the windows:  SYSWINDOWS",
    "alias": "WINDOWS, SYSWINDOWS"

/*Command: SysWindows*/

int init()
{
    clearSelection();
    setPromptPrefix(qsTr("Enter an option [Cascade/Tile]: "));
}

int prompt(str)
{
    if(str == "C" || str == "CASCADE") /*TODO: Probably should add additional qsTr calls here.*/
    {
        windowCascade();
        return;
    }
    else if(str == "T" || str == "TILE") /*TODO: Probably should add additional qsTr calls here.*/
    {
        windowTile();
        return;
    }
    else
    {
        alert(qsTr("Invalid option keyword."));
        setPromptPrefix(qsTr("Enter an option [Cascade/Tile]: "));
    }
}

/* ----------------------------------------------------------------------- */

void treble_clef_init()
{
    treble_clef global;
    clearSelection();
    args.cx = MAX_DISTANCE+1.0;
    args.cy = MAX_DISTANCE+1.0;
    args.numPoints = 1024; /*Default //TODO: min:64 max:8192*/
    args.sx = 0.04; /*Default*/
    args.sy = 0.04; /*Default*/
    args.mode = TREBLE_CLEF_MODE_NUM_POINTS;

    addRubber("POLYGON");
    setRubberMode("POLYGON");
    updateClef(args.numPoints, args.sx, args.sy);
    spareRubber("POLYGON");
    return;
}

void treble_clef_updateClef(int numPts, double xScale, double yScale)
{
    int i;

    for (i=0; i<=numPts; i++) {
        double t, xx, yy;
        t = (16*embConstantPi)/numPts*i;

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
        theta(sqrt(sgn(sin(t/2))));

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
        theta(sqrt(sgn(sin(t/2))));

        setRubberPoint("POLYGON_POINT_" + i.toString(), xx*xScale, yy*yScale);
    }

    setRubberText("POLYGON_NUM_POINTS", numPts.toString());
}

        for (j=0; j<dolphin_curve_basis_ints; j++) {
            float coef = dolphin_curve_x[5*j]/(1.0*dolphin_curve_x[5*j+1]);
            float offset = dolphin_curve_x[5*j+2]/(1.0*dolphin_curve_x[5*j+3]);
            float t_mult = dophin_curve_x[5*j+4];
            xx += coef * sin(offset + t_mult * t);
        }
        
        for (j=0; j<dolphin_curve_basis_ints; j++) {
            float coef = dolphin_curve_y[5*j]/(1.0*dolphin_curve_y[5*j+1]);
            float offset = dolphin_curve_y[5*j+2]/(1.0*dolphin_curve_y[5*j+3]);
            float t_mult = dophin_curve_y[5*j+4];
            yy += coef * sin(offset + t_mult * t);
        }
#endif

unsigned int rgb(unsigned char red, unsigned char green, unsigned char blue)
{
    return blue + green*256 + blue*256*256;
}

int find_ini_value(char *key, char *out)
{
    int i;
    for (i=0; i<settings_data_length; i++) {
        if (settings_data[i] == '\n' || settings_data[i] == '\r') {
            if (!strncmp(settings_data+i+1, key, strlen(key))) {
                int j;
                strcpy(out, settings_data+i+2+strlen(key));
                for (j=0; j<strlen(out); j++) {
                    if (out[j] == '\n' || out[j] == '\r') {
                        out[j] = 0;
                        break;
                    }
                }
                return 1;
            }
        }
    }
    return 0;
}

int get_ini_int(char *key, int default_value)
{
    int r;
    r = find_ini_value(key, value_out);
    if (r) {
        return atoi(value_out);
    }
    return default_value;
}

float get_ini_float(char *key, float default_value)
{
    int r;
    r = find_ini_value(key, value_out);
    if (r) {
        return atof(value_out);
    }
    return default_value;
}

char * get_ini_str(char *key, char *default_value)
{
    int r;
    r = find_ini_value(key, value_out);
    if (r) {
        return value_out;
    }
    return default_value;
}

int load_settings(void)
{
    FILE *f;
    app_dir(assets_dir, 0);
    strcpy(settings_fname, assets_dir);
    strcat(settings_fname, "settings.ini");

    puts("Loading settings...");

    /* Step zero: load all of the ini file into a char buffer. */
    f = fopen(settings_fname, "rb");
    if (!f) {
        puts("No settings file found, probably the first run on this system.");
        return 1;
    }
    else {
        fseek(f, 0, SEEK_END);
        settings_data_length = ftell(f);
        fseek(f, 0, SEEK_SET);
        fread(settings_data, 1, settings_data_length, f);
        fclose(f);
    }

    settings_data_length = 0;

    settings.window_width = get_ini_int("Window_Width", 640);
    settings.window_height = get_ini_int("Window_Height", 480);
    settings.window_width = embClamp(640, settings.window_width, 10000);
    settings.window_height = embClamp(480, settings.window_height, 10000);
    settings.window_x = get_ini_int("Window_PositionX", 0);
    settings.window_y = get_ini_int("Window_PositionY", 0);
    settings.window_x = embClamp(0, settings.window_x, 1000);
    settings.window_y = embClamp(0, settings.window_y, 1000);

    strcpy(settings.general_language, get_ini_str("Language", "default"));
    strcpy(settings.general_icon_theme, get_ini_str("IconTheme", "default"));
    settings.general_icon_size = get_ini_int("IconSize", 16);
    settings.general_mdi_bg_use_logo = get_ini_int("MdiBGUseLogo", 1);
    settings.general_mdi_bg_use_texture = get_ini_int("MdiBGUseTexture", 1);
    settings.general_mdi_bg_use_color = get_ini_int("MdiBGUseColor", 1);
    char default_str[200];
    sprintf(default_str, "%s/images/logo-spirals.png", assets_dir);
    strcpy(settings.general_mdi_bg_logo, get_ini_str("MdiBGLogo", default_str));
    sprintf(default_str, "%s/images/texture-spirals.png", assets_dir);
    strcpy(settings.general_mdi_bg_texture, get_ini_str("MdiBGTexture", default_str));
    settings.general_mdi_bg_color = get_ini_int("MdiBGColor", rgb(192,192,192));
    settings.general_tip_of_the_day = get_ini_int("TipOfTheDay", 1);
    settings.general_current_tip =  get_ini_int("CurrentTip", 0);
    settings.general_system_help_browser = get_ini_int("SystemHelpBrowser", 1);

    /* Display */
    settings.display_use_opengl = get_ini_int("Display_UseOpenGL", 0);
    settings.display_renderhint_aa = get_ini_int("Display_RenderHintAntiAlias", 0);
    settings.display_renderhint_text_aa = get_ini_int("Display_RenderHintTextAntiAlias", 0);
    settings.display_renderhint_smooth_pix = get_ini_int("Display_RenderHintSmoothPixmap", 0);
    settings.display_renderhint_high_aa = get_ini_int("Display_RenderHintHighQualityAntiAlias", 0);
    settings.display_renderhint_noncosmetic = get_ini_int("Display_RenderHintNonCosmetic", 0);
    settings.display_show_scrollbars = get_ini_int("Display_ShowScrollBars", 1);
    settings.display_scrollbar_widget_num = get_ini_int("Display_ScrollBarWidgetNum", 0);
    settings.display_crosshair_color = get_ini_int("Display_CrossHairColor", rgb(  0, 0, 0));
    settings.display_bg_color = get_ini_int("Display_BackgroundColor", rgb(235,235,235));
    settings.display_selectbox_left_color = get_ini_int("Display_SelectBoxLeftColor", rgb(  0,128, 0));
    settings.display_selectbox_left_fill = get_ini_int("Display_SelectBoxLeftFill", rgb(  0,255, 0));
    settings.display_selectbox_right_color = get_ini_int("Display_SelectBoxRightColor", rgb(  0, 0,128));
    settings.display_selectbox_right_fill = get_ini_int("Display_SelectBoxRightFill", rgb(  0, 0,255));
    settings.display_selectbox_alpha = get_ini_int("Display_SelectBoxAlpha", 32);
    settings.display_zoomscale_in = get_ini_float("Display_ZoomScaleIn", 2.0);
    settings.display_zoomscale_out = get_ini_float("Display_ZoomScaleOut", 0.5);
    settings.display_crosshair_percent = get_ini_int("Display_CrossHairPercent", 5);
    strcpy(settings.display_units, get_ini_str("Display_Units", "mm"));

    /* OpenSave */
    /* opensave_custom_filter = QString(get_ini_str("OpenSave_CustomFilter", "supported")); */
    strcpy(settings.opensave_open_format, get_ini_str("OpenSave_OpenFormat", "*.*"));
    settings.opensave_open_thumbnail = get_ini_int("OpenSave_OpenThumbnail", 0);
    strcpy(settings.opensave_save_format, get_ini_str("OpenSave_SaveFormat", "*.*"));
    settings.opensave_save_thumbnail = get_ini_int("OpenSave_SaveThumbnail", 0);

    /* Recent */
    settings.opensave_recent_max_files = get_ini_int("OpenSave_RecentMax", 10);
    /* opensave_recent_list_of_files = get_ini_str("OpenSave_RecentFiles", ""); */
    sprintf(default_str, "%s/samples", assets_dir);
    strcpy(settings.opensave_recent_directory, get_ini_str("OpenSave_RecentDirectory", default_str));

    /* Trimming */
    settings.opensave_trim_dst_num_jumps = get_ini_int("OpenSave_TrimDstNumJumps", 5);

    /* Printing
    settings.printing_default_device = settings_file.value("Printing_DefaultDevice", "").toString();
    settings.printing_use_last_device = settings_file.value("Printing_UseLastDevice", 0);
    settings.printing_disable_bg = settings_file.value("Printing_DisableBG", 1); */
    /* Grid */
    settings.grid_show_on_load = get_ini_int("Grid_ShowOnLoad", 1);
    settings.grid_show_origin = get_ini_int("Grid_ShowOrigin", 1);
    settings.grid_color_match_crosshair = get_ini_int("Grid_ColorMatchCrossHair", 1);
    settings.grid_color = get_ini_int("Grid_Color", rgb(0, 0, 0));
    settings.grid_load_from_file = get_ini_int("Grid_LoadFromFile", 1);
    strcpy(settings.grid_type, get_ini_str("Grid_Type", "Rectangular"));
    settings.grid_center_on_origin = get_ini_int("Grid_CenterOnOrigin", 1);
    settings.grid_center.x = get_ini_float("Grid_CenterX", 0.0);
    settings.grid_center.y = get_ini_float("Grid_CenterY", 0.0);
    settings.grid_size.x = get_ini_float("Grid_SizeX", 100.0);
    settings.grid_size.y = get_ini_float("Grid_SizeY", 100.0);
    settings.grid_spacing.x = get_ini_float("Grid_SpacingX", 25.0);
    settings.grid_spacing.y = get_ini_float("Grid_SpacingY", 25.0);
    settings.grid_size_radius = get_ini_float("Grid_SizeRadius", 50.0);
    settings.grid_spacing_radius = get_ini_float("Grid_SpacingRadius", 25.0);
    settings.grid_spacing_angle = get_ini_float("Grid_SpacingAngle", 45.0);

    /* Ruler */
    settings.ruler_show_on_load = get_ini_int("Ruler_ShowOnLoad", 1);
    settings.ruler_metric = get_ini_int("Ruler_Metric", 1);
    settings.ruler_color = get_ini_int("Ruler_Color", rgb(210,210, 50));
    settings.ruler_pixel_size = get_ini_int("Ruler_PixelSize", 20);

    /* Quick Snap */
    settings.qsnap_enabled = get_ini_int("QuickSnap_Enabled", 1);
    settings.qsnap_locator_color = get_ini_int("QuickSnap_LocatorColor", rgb(255,255, 0));
    settings.qsnap_locator_size = get_ini_int("QuickSnap_LocatorSize", 4);
    settings.qsnap_aperture_size = get_ini_int("QuickSnap_ApertureSize", 10);
    settings.qsnap_endpoint = get_ini_int("QuickSnap_EndPoint", 1);
    settings.qsnap_midpoint = get_ini_int("QuickSnap_MidPoint", 1);
    settings.qsnap_center = get_ini_int("QuickSnap_Center", 1);
    settings.qsnap_node = get_ini_int("QuickSnap_Node", 1);
    settings.qsnap_quadrant = get_ini_int("QuickSnap_Quadrant", 1);
    settings.qsnap_intersection = get_ini_int("QuickSnap_Intersection", 1);
    settings.qsnap_extension = get_ini_int("QuickSnap_Extension", 1);
    settings.qsnap_insertion = get_ini_int("QuickSnap_Insertion", 0);
    settings.qsnap_perpendicular = get_ini_int("QuickSnap_Perpendicular", 1);
    settings.qsnap_tangent = get_ini_int("QuickSnap_Tangent", 1);
    settings.qsnap_nearest = get_ini_int("QuickSnap_Nearest", 0);
    settings.qsnap_apparent = get_ini_int("QuickSnap_Apparent", 0);
    settings.qsnap_parallel = get_ini_int("QuickSnap_Parallel", 0);

    /* LineWeight */
    settings.lwt_show_lwt = get_ini_int("LineWeight_ShowLineWeight", 0);
    settings.lwt_real_render = get_ini_int("LineWeight_RealRender", 1);
    settings.lwt_default_lwt = get_ini_int("LineWeight_DefaultLineWeight", 0);

    /* Selection */
    settings.selection_mode_pickfirst = get_ini_int("Selection_PickFirst", 1);
    settings.selection_mode_pickadd = get_ini_int("Selection_PickAdd", 1);
    settings.selection_mode_pickdrag = get_ini_int("Selection_PickDrag", 0);
    settings.selection_coolgrip_color = get_ini_int("Selection_CoolGripColor", rgb(  0, 0,255));
    settings.selection_hotgrip_color = get_ini_int("Selection_HotGripColor", rgb(255, 0, 0));
    settings.selection_grip_size = get_ini_int("Selection_GripSize", 4);
    settings.selection_pickbox_size = get_ini_int("Selection_PickBoxSize", 4);

    /* Text */
    strcpy(settings.text_font, get_ini_str("Text_Font", "Arial"));
    settings.text_style.size = get_ini_int("Text_Size", 12);
    settings.text_style.angle = get_ini_int("Text_Angle", 0);
    settings.text_style.bold = get_ini_int("Text_StyleBold", 0);
    settings.text_style.italic = get_ini_int("Text_StyleItalic", 0);
    settings.text_style.underline = get_ini_int("Text_StyleUnderline", 0);
    settings.text_style.strikeout = get_ini_int("Text_StyleStrikeOut", 0);
    settings.text_style.overline = get_ini_int("Text_StyleOverline", 0);

    return 0;
}

int save_settings(void)
{
    FILE *f;
    app_dir(assets_dir, 0);
    strcpy(settings_fname, assets_dir);
    /* This file needs to be read from the users home directory
     * to ensure it is writable. */
    strcat(settings_fname, "settings.ini");
    f = fopen(settings_fname, "rb");
    if (!f) {
        puts("Cannot create settings file.");
        return 1;
    }
    
    fprintf(f, "Window_PositionX=%d\r\n", settings.window_x);
    fprintf(f, "Window_PositionY=%d\r\n", settings.window_y);
    fprintf(f, "Window_Width=%d\r\n", settings.window_width);
    fprintf(f, "Window_Height=%d\r\n", settings.window_height);

    /* General */
    /* fprintf(f, "LayoutState=%s\r\n", to_c_str(_mainWin->layoutState)); */
    fprintf(f, "Language=%s\r\n", settings.general_language);
    fprintf(f, "IconTheme=%s\r\n", settings.general_icon_theme);
    fprintf(f, "IconSize=%d\r\n", settings.general_icon_size);
    fprintf(f, "MdiBGUseLogo=%d\r\n", settings.general_mdi_bg_use_logo);
    fprintf(f, "MdiBGUseTexture=%d\r\n", settings.general_mdi_bg_use_texture);
    fprintf(f, "MdiBGUseColor=%d\r\n", settings.general_mdi_bg_use_color);
    fprintf(f, "MdiBGLogo=%s\r\n", settings.general_mdi_bg_logo);
    fprintf(f, "MdiBGTexture=%s\r\n", settings.general_mdi_bg_texture);
    fprintf(f, "MdiBGColor=%d\r\n", settings.general_mdi_bg_color);
    fprintf(f, "TipOfTheDay=%d\r\n", settings.general_tip_of_the_day);
    fprintf(f, "CurrentTip=%d\r\n", settings.general_current_tip + 1);
    fprintf(f, "SystemHelpBrowser=%d\r\n", settings.general_system_help_browser);

    /* Display */
    fprintf(f, "Display_UseOpenGL=%d\r\n", settings.display_use_opengl);
    fprintf(f, "Display_RenderHintAntiAlias=%d\r\n", settings.display_renderhint_aa);
    fprintf(f, "Display_RenderHintTextAntiAlias=%d\r\n", settings.display_renderhint_text_aa);
    fprintf(f, "Display_RenderHintSmoothPixmap=%d\r\n", settings.display_renderhint_smooth_pix);
    fprintf(f, "Display_RenderHintHighQualityAntiAlias=%d\r\n", settings.display_renderhint_high_aa);
    fprintf(f, "Display_RenderHintNonCosmetic=%d\r\n", settings.display_renderhint_noncosmetic);
    fprintf(f, "Display_ShowScrollBars=%d\r\n", settings.display_show_scrollbars);
    fprintf(f, "Display_ScrollBarWidgetNum=%d\r\n", settings.display_scrollbar_widget_num);
    fprintf(f, "Display_CrossHairColor=%d\r\n", settings.display_crosshair_color);
    fprintf(f, "Display_BackgroundColor=%d\r\n", settings.display_bg_color);
    fprintf(f, "Display_SelectBoxLeftColor=%d\r\n", settings.display_selectbox_left_color);
    fprintf(f, "Display_SelectBoxLeftFill=%d\r\n", settings.display_selectbox_left_fill);
    fprintf(f, "Display_SelectBoxRightColor=%d\r\n", settings.display_selectbox_right_color);
    fprintf(f, "Display_SelectBoxRightFill=%d\r\n", settings.display_selectbox_right_fill);
    fprintf(f, "Display_SelectBoxAlpha=%d\r\n", settings.display_selectbox_alpha);
    fprintf(f, "Display_ZoomScaleIn=%f\r\n", settings.display_zoomscale_in);
    fprintf(f, "Display_ZoomScaleOut=%f\r\n", settings.display_zoomscale_out);
    fprintf(f, "Display_CrossHairPercent=%d\r\n", settings.display_crosshair_percent);
    fprintf(f, "Display_Units=%s\r\n", settings.display_units);
    /* OpenSave
    fprintf(f, "OpenSave_CustomFilter=%s\r\n", to_c_str(opensave_custom_filter)); */
    fprintf(f, "OpenSave_OpenFormat=%s\r\n", settings.opensave_open_format);
    fprintf(f, "OpenSave_OpenThumbnail=%d\r\n", settings.opensave_open_thumbnail);
    fprintf(f, "OpenSave_SaveFormat=%s\r\n", settings.opensave_save_format);
    fprintf(f, "OpenSave_SaveThumbnail=%d\r\n", settings.opensave_save_thumbnail);
    //Recent
    fprintf(f, "OpenSave_RecentMax=%d\r\n", settings.opensave_recent_max_files);
    /* fprintf(f, "OpenSave_RecentFiles=%d\r\n", opensave_recent_list_of_files); */
    fprintf(f, "OpenSave_RecentDirectory=%s\r\n", settings.opensave_recent_directory);
    /* Trimming */
    fprintf(f, "OpenSave_TrimDstNumJumps=%d\r\n", settings.opensave_trim_dst_num_jumps);
    /* Printing */
    fprintf(f, "Printing_DefaultDevice=%s\r\n", settings.printing_default_device);
    fprintf(f, "Printing_UseLastDevice=%d\r\n", settings.printing_use_last_device);
    fprintf(f, "Printing_DisableBG=%d\r\n", settings.printing_disable_bg);
    /* Grid */
    fprintf(f, "Grid_ShowOnLoad=%d\r\n", settings.grid_show_on_load);
    fprintf(f, "Grid_ShowOrigin=%d\r\n", settings.grid_show_origin);
    fprintf(f, "Grid_ColorMatchCrossHair=%d\r\n", settings.grid_color_match_crosshair);
    fprintf(f, "Grid_Color=%d\r\n", settings.grid_color);
    fprintf(f, "Grid_LoadFromFile=%d\r\n", settings.grid_load_from_file);
    fprintf(f, "Grid_Type=%s\r\n", settings.grid_type);
    fprintf(f, "Grid_CenterOnOrigin=%d\r\n", settings.grid_center_on_origin);
    fprintf(f, "Grid_CenterX=%f\r\n", settings.grid_center.x);
    fprintf(f, "Grid_CenterY=%f\r\n", settings.grid_center.y);
    fprintf(f, "Grid_SizeX=%f\r\n", settings.grid_size.x);
    fprintf(f, "Grid_SizeY=%f\r\n", settings.grid_size.y);
    fprintf(f, "Grid_SpacingX=%f\r\n", settings.grid_spacing.x);
    fprintf(f, "Grid_SpacingY=%f\r\n", settings.grid_spacing.y);
    fprintf(f, "Grid_SizeRadius=%f\r\n", settings.grid_size_radius);
    fprintf(f, "Grid_SpacingRadius=%f\r\n", settings.grid_spacing_radius);
    fprintf(f, "Grid_SpacingAngle=%f\r\n", settings.grid_spacing_angle);
    //Ruler
    fprintf(f, "Ruler_ShowOnLoad=%d\r\n", settings.ruler_show_on_load);
    fprintf(f, "Ruler_Metric=%d\r\n", settings.ruler_metric);
    fprintf(f, "Ruler_Color=%d\r\n", settings.ruler_color);
    fprintf(f, "Ruler_PixelSize=%d\r\n", settings.ruler_pixel_size);
    //Quick Snap
    fprintf(f, "QuickSnap_Enabled=%d\r\n", settings.qsnap_enabled);
    fprintf(f, "QuickSnap_LocatorColor=%d\r\n", settings.qsnap_locator_color);
    fprintf(f, "QuickSnap_LocatorSize=%d\r\n", settings.qsnap_locator_size);
    fprintf(f, "QuickSnap_ApertureSize=%d\r\n", settings.qsnap_aperture_size);
    fprintf(f, "QuickSnap_EndPoint=%d\r\n", settings.qsnap_endpoint);
    fprintf(f, "QuickSnap_MidPoint=%d\r\n", settings.qsnap_midpoint);
    fprintf(f, "QuickSnap_Center=%d\r\n", settings.qsnap_center);
    fprintf(f, "QuickSnap_Node=%d\r\n", settings.qsnap_node);
    fprintf(f, "QuickSnap_Quadrant=%d\r\n", settings.qsnap_quadrant);
    fprintf(f, "QuickSnap_Intersection=%d\r\n", settings.qsnap_intersection);
    fprintf(f, "QuickSnap_Extension=%d\r\n", settings.qsnap_extension);
    fprintf(f, "QuickSnap_Insertion=%d\r\n", settings.qsnap_insertion);
    fprintf(f, "QuickSnap_Perpendicular=%d\r\n", settings.qsnap_perpendicular);
    fprintf(f, "QuickSnap_Tangent=%d\r\n", settings.qsnap_tangent);
    fprintf(f, "QuickSnap_Nearest=%d\r\n", settings.qsnap_nearest);
    fprintf(f, "QuickSnap_Apparent=%d\r\n", settings.qsnap_apparent);
    fprintf(f, "QuickSnap_Parallel=%d\r\n", settings.qsnap_parallel);
    //LineWeight
    fprintf(f, "LineWeight_ShowLineWeight=%d\r\n", settings.lwt_show_lwt);
    fprintf(f, "LineWeight_RealRender=%d\r\n", settings.lwt_real_render);
    fprintf(f, "LineWeight_DefaultLineWeight=%f\r\n", settings.lwt_default_lwt);

    /* Selection */
    fprintf(f, "Selection_PickFirst=%d\r\n", settings.selection_mode_pickfirst);
    fprintf(f, "Selection_PickAdd=%d\r\n", settings.selection_mode_pickadd);
    fprintf(f, "Selection_PickDrag=%d\r\n", settings.selection_mode_pickdrag);
    fprintf(f, "Selection_CoolGripColor=%d\r\n", settings.selection_coolgrip_color);
    fprintf(f, "Selection_HotGripColor=%d\r\n", settings.selection_hotgrip_color);
    fprintf(f, "Selection_GripSize=%d\r\n", settings.selection_grip_size);
    fprintf(f, "Selection_PickBoxSize=%d\r\n", settings.selection_pickbox_size);

    /* Text */
    fprintf(f, "Text_Font=%s\r\n", settings.text_font);
    fprintf(f, "Text_Size=%f\r\n", settings.text_style.size);
    fprintf(f, "Text_Angle=%f\r\n", settings.text_style.angle);
    fprintf(f, "Text_StyleBold=%d\r\n", settings.text_style.bold);
    fprintf(f, "Text_StyleItalic=%d\r\n", settings.text_style.italic);
    fprintf(f, "Text_StyleUnderline=%d\r\n", settings.text_style.underline);
    fprintf(f, "Text_StyleStrikeOut=%d\r\n", settings.text_style.strikeout);
    fprintf(f, "Text_StyleOverline=%d\r\n", settings.text_style.overline);

    fclose(f);
    return 0;
}

int embClamp(int lower, int x, int upper)
{
    x = embMinInt(upper, x);
    x = embMaxInt(lower, x);
    return x;
}

void checkBoxTipOfTheDayStateChanged(int checked)
{
    dialog.general_tip_of_the_day = checked;
}

void checkBoxUseOpenGLStateChanged(int checked)
{
    dialog.display_use_opengl = checked;
}

void checkBoxRenderHintAAStateChanged(int checked)
{
    dialog.display_renderhint_aa = checked;
}

void checkBoxRenderHintTextAAStateChanged(int checked)
{
    dialog.display_renderhint_text_aa = checked;
}

void checkBoxRenderHintSmoothPixStateChanged(int checked)
{
    dialog.display_renderhint_smooth_pix = checked;
}

void checkBoxRenderHintHighAAStateChanged(int checked)
{
    dialog.display_renderhint_high_aa = checked;
}

void checkBoxRenderHintNonCosmeticStateChanged(int checked)
{
    dialog.display_renderhint_noncosmetic = checked;
}

void comboBoxScrollBarWidgetCurrentIndexChanged(int index)
{
    dialog.display_scrollbar_widget_num = index;
}

void spinBoxZoomScaleInValueChanged(double value)
{
    dialog.display_zoomscale_in = value;
}

void spinBoxZoomScaleOutValueChanged(double value)
{
    dialog.display_zoomscale_out = value;
}

void checkBoxDisableBGStateChanged(int checked)
{
    dialog.printing_disable_bg = checked;
}

void spinBoxRecentMaxFilesValueChanged(int value)
{
    dialog.opensave_recent_max_files = value;
}

void spinBoxTrimDstNumJumpsValueChanged(int value)
{
    dialog.opensave_trim_dst_num_jumps = value;
}

void checkBoxGridShowOnLoadStateChanged(int checked)
{
    dialog.grid_show_on_load = checked;
}

void checkBoxGridShowOriginStateChanged(int checked)
{
    dialog.grid_show_origin = checked;
}


void spinBoxRulerPixelSizeValueChanged(double value)
{
    dialog.ruler_pixel_size = value;
}

void checkBoxQSnapEndPointStateChanged(int checked)
{
    dialog.qsnap_endpoint = checked;
}

void checkBoxQSnapMidPointStateChanged(int checked)
{
    dialog.qsnap_midpoint = checked;
}

void checkBoxQSnapCenterStateChanged(int checked)
{
    dialog.qsnap_center = checked;
}

void checkBoxQSnapNodeStateChanged(int checked)
{
    dialog.qsnap_node = checked;
}

void checkBoxQSnapQuadrantStateChanged(int checked)
{
    dialog.qsnap_quadrant = checked;
}

void checkBoxQSnapIntersectionStateChanged(int checked)
{
    dialog.qsnap_intersection = checked;
}

void checkBoxQSnapExtensionStateChanged(int checked)
{
    dialog.qsnap_extension = checked;
}

void checkBoxQSnapInsertionStateChanged(int checked)
{
    dialog.qsnap_insertion = checked;
}

void checkBoxQSnapPerpendicularStateChanged(int checked)
{
    dialog.qsnap_perpendicular = checked;
}

void checkBoxQSnapTangentStateChanged(int checked)
{
    dialog.qsnap_tangent = checked;
}

void checkBoxQSnapNearestStateChanged(int checked)
{
    dialog.qsnap_nearest = checked;
}

void checkBoxQSnapApparentStateChanged(int checked)
{
    dialog.qsnap_apparent = checked;
}

void checkBoxQSnapParallelStateChanged(int checked)
{
    dialog.qsnap_parallel = checked;
}

void checkBoxSelectionModePickFirstStateChanged(int checked)
{
    dialog.selection_mode_pickfirst = checked;
}

void checkBoxSelectionModePickAddStateChanged(int checked)
{
    dialog.selection_mode_pickadd = checked;
}

void checkBoxSelectionModePickDragStateChanged(int checked)
{
    dialog.selection_mode_pickdrag = checked;
}

void sliderSelectionGripSizeValueChanged(int value)
{
    dialog.selection_grip_size = value;
}

void sliderSelectionPickBoxSizeValueChanged(int value)
{
    dialog.selection_pickbox_size = value;
}

void spinBoxGridCenterXValueChanged(double value)
{
    dialog.grid_center.x = value;
}

void spinBoxGridCenterYValueChanged(double value)
{
    dialog.grid_center.y = value;
}

void spinBoxGridSizeXValueChanged(double value)
{
    dialog.grid_size.x = value;
}

void spinBoxGridSizeYValueChanged(double value)
{
    dialog.grid_size.y = value;
}

void spinBoxGridSpacingXValueChanged(double value)
{
    dialog.grid_spacing.x = value;
}

void spinBoxGridSpacingYValueChanged(double value)
{
    dialog.grid_spacing.y = value;
}

void spinBoxGridSizeRadiusValueChanged(double value)
{
    dialog.grid_size_radius = value;
}

void spinBoxGridSpacingRadiusValueChanged(double value)
{
    dialog.grid_spacing_radius = value;
}

void spinBoxGridSpacingAngleValueChanged(double value)
{
    dialog.grid_spacing_angle = value;
}

void checkBoxRulerShowOnLoadStateChanged(int checked)
{
    dialog.ruler_show_on_load = checked;
}

