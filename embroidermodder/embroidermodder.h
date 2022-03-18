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
 * We're in the process of translating this common code into mostly C by
 * building a basic binary tree widget system.
 *
 * The structs are fully documented here, please read this documentation
 * before any other inside the code itself.
 */

#ifndef EMBROIDERMODDER_H
#define EMBROIDERMODDER_H

#ifdef __cplusplus
extern "C" {
#endif

#include "embroidery.h"

/*
 * Defines
 * -------
 */
#define MAX_STRING_LENGTH            500

#define TOOLBAR_FILE                   0
#define TOOLBAR_EDIT                   1
#define TOOLBAR_VIEW                   2
#define TOOLBAR_ZOOM                   3
#define TOOLBAR_PAN                    4
#define TOOLBAR_ICON                   5
#define TOOLBAR_HELP                   6
#define TOOLBAR_LAYER                  7
#define TOOLBAR_TEXT                   8
#define TOOLBAR_PROPERTIES             9
#define N_TOOLBARS                    10

#define FILE_MENU                      0
#define EDIT_MENU                      1
#define VIEW_MENU                      2
#define SETTINGS_MENU                  3
#define WINDOW_MENU                    4
#define HELP_MENU                      5
#define RECENT_MENU                    6
#define ZOOM_MENU                      7
#define PAN_MENU                       8
#define N_MENUS                        9

#define STATUS_SNAP                   0
#define STATUS_GRID                   1
#define STATUS_RULER                  2
#define STATUS_ORTHO                  3
#define STATUS_POLAR                  4
#define STATUS_QSNAP                  5
#define STATUS_QTRACK                 6
#define STATUS_LWT                    7
#define N_STATUS                      8

#define TAB_SNAP                      0
#define TAB_GRID                      1
#define TAB_RULER                     2
#define TAB_ORTHO                     3
#define TAB_POLAR                     4
#define TAB_QSNAP                     5
#define TAB_QTRACK                    6
#define TAB_LWT                       7

#define STATUS_SNAP                   0
#define STATUS_GRID                   1
#define STATUS_RULER                  2
#define STATUS_ORTHO                  3
#define STATUS_POLAR                  4
#define STATUS_QSNAP                  5
#define STATUS_QTRACK                 6
#define STATUS_LWT                    7

#define SYMBOL_zero                   0
#define SYMBOL_one                    1
#define SYMBOL_two                    2
#define SYMBOL_three                  3
#define SYMBOL_four                   4
#define SYMBOL_five                   5
#define SYMBOL_six                    6
#define SYMBOL_seven                  7
#define SYMBOL_eight                  8
#define SYMBOL_nine                   9
#define SYMBOL_minus                 10
#define SYMBOL_apostrophe            11
#define SYMBOL_quote                 12

/* LineEdits */
/* --------------------------------- */
#define ARC_CENTER_X                   0
#define ARC_CENTER_Y                   1
#define ARC_RADIUS                     2
#define ARC_START_ANGLE                3
#define ARC_END_ANGLE                  4
#define ARC_START_X                    5
#define ARC_START_Y                    6
#define ARC_END_X                      7
#define ARC_END_Y                      8
#define ARC_AREA                       9
#define ARC_LENGTH                    10
#define ARC_CHORD                     11
#define ARC_INC_ANGLE                 12
#define TEXT_SINGLE_CONTENTS          13
#define TEXT_SINGLE_HEIGHT            14
#define TEXT_SINGLE_ROTATION          15
#define TEXT_SINGLE_X                 16
#define TEXT_SINGLE_Y                 17
#define CIRCLE_CENTER_X               18
#define CIRCLE_CENTER_Y               19
#define CIRCLE_RADIUS                 20
#define CIRCLE_DIAMETER               21
#define CIRCLE_AREA                   22
#define CIRCLE_CIRCUMFERENCE          23
#define ELLIPSE_CENTER_X              24
#define ELLIPSE_CENTER_Y              25
#define ELLIPSE_RADIUS_MAJOR          26
#define ELLIPSE_RADIUS_MINOR          27
#define ELLIPSE_DIAMETER_MAJOR        28
#define ELLIPSE_DIAMETER_MINOR        29
#define IMAGE_X                       30
#define IMAGE_Y                       31
#define IMAGE_WIDTH                   32
#define IMAGE_HEIGHT                  33
#define IMAGE_NAME                    34
#define IMAGE_PATH                    35
#define INFINITE_LINE_X1              36
#define INFINITE_LINE_Y1              37
#define INFINITE_LINE_X2              38
#define INFINITE_LINE_Y2              39
#define INFINITE_LINE_VECTOR_X        40
#define INFINITE_LINE_VECTOR_Y        41
#define BLOCK_X                       42
#define BLOCK_Y                       43
#define LINE_START_X                  44
#define LINE_START_Y                  45
#define LINE_END_X                    46
#define LINE_END_Y                    47
#define LINE_DELTA_X                  48
#define LINE_DELTA_Y                  49
#define LINE_ANGLE                    50
#define LINE_LENGTH                   51
#define POLYGON_CENTER_X              52
#define POLYGON_CENTER_Y              53
#define POLYGON_RADIUS_VERTEX         54
#define POLYGON_RADIUS_SIDE           55
#define POLYGON_DIAMETER_VERTEX       56
#define POLYGON_DIAMETER_SIDE         57
#define POLYGON_INTERIOR_ANGLE        58
#define RECT_CORNER_X1                59
#define RECT_CORNER_Y1                60
#define RECT_CORNER_X2                61
#define RECT_CORNER_Y2                62
#define RECT_CORNER_X3                63
#define RECT_CORNER_Y3                64
#define RECT_CORNER_X4                65
#define RECT_CORNER_Y4                66
#define RECT_HEIGHT                   67
#define RECT_WIDTH                    68
#define RECT_AREA                     69
#define POINT_X                       70
#define POINT_Y                       71
#define LINEEDIT_PROPERTY_EDITORS     72

/* Comboboxes */
/* --------------------------------- */
#define ARC_CLOCKWISE                 0
#define GENERAL_LAYER                 1
#define GENERAL_COLOR                 2
#define GENERAL_LINE_TYPE             3
#define GENERAL_LINE_WEIGHT           4
#define TEXT_SINGLE_FONT              5
#define TEXT_SINGLE_JUSTIFY           6
#define COMBOBOX_PROPERTY_EDITORS     7

#define PROPERTY_EDITORS \
    ( LINEEDIT_PROPERTY_EDITORS + COMBOBOX_PROPERTY_EDITORS )

#define LINE_EDIT_DOUBLE               0
#define LINE_EDIT_INT                  1
#define LINE_EDIT_STR                  2
#define COMBO_BOX_TYPE                 3

/* Keys */
/* ---- */
/* value type - int: See OBJ_TYPE_VALUES */
#define OBJ_TYPE                      0
/* value type - str: See OBJ_NAME_VALUES */
#define OBJ_NAME                      1
/* value type - str: "USER", "DEFINED", "STRINGS", etc... */
#define OBJ_LAYER                     2
/* value type - int: 0-255
  TODO: Use color chart in formats/format-dxf.h for this */
#define OBJ_COLOR                     3
/*value type - int: See OBJ_LTYPE_VALUES*/
#define OBJ_LTYPE                     4
 /*value type - int: 0-27*/
#define OBJ_LWT                       5
/* value type - int: See OBJ_RUBBER_VALUES */
#define OBJ_RUBBER                    6

/* Values */
/* ------ */
/* NOTE: Allow this enum to evaluate false */
#define OBJ_TYPE_NULL                 0
/* NOTE: Values >= 65536 ensure compatibility with qgraphicsitem_cast() */
#define OBJ_TYPE_BASE            100000
#define OBJ_TYPE_ARC             100001
#define OBJ_TYPE_BLOCK           100002
#define OBJ_TYPE_CIRCLE          100003
#define OBJ_TYPE_DIMALIGNED      100004
#define OBJ_TYPE_DIMANGULAR      100005
#define OBJ_TYPE_DIMARCLENGTH    100006
#define OBJ_TYPE_DIMDIAMETER     100007
#define OBJ_TYPE_DIMLEADER       100008
#define OBJ_TYPE_DIMLINEAR       100009
#define OBJ_TYPE_DIMORDINATE     100010
#define OBJ_TYPE_DIMRADIUS       100011
#define OBJ_TYPE_ELLIPSE         100012
#define OBJ_TYPE_ELLIPSEARC      100013
#define OBJ_TYPE_RUBBER          100014
#define OBJ_TYPE_GRID            100015
#define OBJ_TYPE_HATCH           100016
#define OBJ_TYPE_IMAGE           100017
#define OBJ_TYPE_INFINITELINE    100018
#define OBJ_TYPE_LINE            100019
#define OBJ_TYPE_PATH            100020
#define OBJ_TYPE_POINT           100021
#define OBJ_TYPE_POLYGON         100022
#define OBJ_TYPE_POLYLINE        100023
#define OBJ_TYPE_RAY             100024
#define OBJ_TYPE_RECTANGLE       100025
#define OBJ_TYPE_SLOT            100026
#define OBJ_TYPE_SPLINE          100027
#define OBJ_TYPE_TEXTMULTI       100028
#define OBJ_TYPE_TEXTSINGLE      100029
#define OBJ_TYPE_UNKNOWN         100030


/* CAD Linetypes */
#define OBJ_LTYPE_CONT                0
#define OBJ_LTYPE_CENTER              1
#define OBJ_LTYPE_DOT                 2
#define OBJ_LTYPE_HIDDEN              3
#define OBJ_LTYPE_PHANTOM             4
#define OBJ_LTYPE_ZIGZAG              5
/* Embroidery Stitchtypes */
/* __________ */
#define OBJ_LTYPE_RUNNING             6
/* vvvvvvvvvv */
#define OBJ_LTYPE_SATIN               7
/* >>>>>>>>>> */
#define OBJ_LTYPE_FISHBONE            8

/* OBJ_LWT_VALUES
 * --------------
 */
#define OBJ_LWT_BYLAYER             (-2)
#define OBJ_LWT_BYBLOCK             (-1)
#define OBJ_LWT_DEFAULT                0
#define OBJ_LWT_01                     1
#define OBJ_LWT_02                     2
#define OBJ_LWT_03                     3
#define OBJ_LWT_04                     4
#define OBJ_LWT_05                     5
#define OBJ_LWT_06                     6
#define OBJ_LWT_07                     7
#define OBJ_LWT_08                     8
#define OBJ_LWT_09                     9
#define OBJ_LWT_10                    10
#define OBJ_LWT_11                    11
#define OBJ_LWT_12                    12
#define OBJ_LWT_13                    13
#define OBJ_LWT_14                    14
#define OBJ_LWT_15                    15
#define OBJ_LWT_16                    16
#define OBJ_LWT_17                    17
#define OBJ_LWT_18                    18
#define OBJ_LWT_19                    19
#define OBJ_LWT_20                    20
#define OBJ_LWT_21                    21
#define OBJ_LWT_22                    22
#define OBJ_LWT_23                    23
#define OBJ_LWT_24                    24


/* OBJ_SNAP_VALUES */
/* --------------- */
/* NOTE: Allow this enum to evaluate false */
#define OBJ_SNAP_NULL                  0
#define OBJ_SNAP_ENDPOINT              1
#define OBJ_SNAP_MIDPOINT              2
#define OBJ_SNAP_CENTER                3
#define OBJ_SNAP_NODE                  4
#define OBJ_SNAP_QUADRANT              5
#define OBJ_SNAP_INTERSECTION          6
#define OBJ_SNAP_EXTENSION             7
#define OBJ_SNAP_INSERTION             8
#define OBJ_SNAP_PERPENDICULAR         9
#define OBJ_SNAP_TANGENT              10
#define OBJ_SNAP_NEAREST              11
#define OBJ_SNAP_APPINTERSECTION      12
#define OBJ_SNAP_PARALLEL             13


/* OBJ_RUBBER_VALUES
 * -----------------
 * NOTE: Allow this enum to evaluate false and true */
#define OBJ_RUBBER_OFF                 0
#define OBJ_RUBBER_ON                  1
#define OBJ_RUBBER_CIRCLE_1P_RAD       2
#define OBJ_RUBBER_CIRCLE_1P_DIA       3
#define OBJ_RUBBER_CIRCLE_2P           4
#define OBJ_RUBBER_CIRCLE_3P           5
#define OBJ_RUBBER_CIRCLE_TTR          6
#define OBJ_RUBBER_CIRCLE_TTT          7
#define OBJ_RUBBER_DIMLEADER_LINE      8
#define OBJ_RUBBER_ELLIPSE_LINE        9
#define OBJ_RUBBER_ELLIPSE_MAJORDIAMETER_MINORRADIUS 10
#define OBJ_RUBBER_ELLIPSE_MAJORRADIUS_MINORRADIUS 11
#define OBJ_RUBBER_ELLIPSE_ROTATION   12
#define OBJ_RUBBER_GRIP               13
#define OBJ_RUBBER_LINE               14
#define OBJ_RUBBER_POLYGON            15
#define OBJ_RUBBER_POLYGON_INSCRIBE   16
#define OBJ_RUBBER_POLYGON_CIRCUMSCRIBE 17
#define OBJ_RUBBER_POLYLINE           18
#define OBJ_RUBBER_IMAGE              19
#define OBJ_RUBBER_RECTANGLE          20
#define OBJ_RUBBER_TEXTSINGLE         21


/* SPARE_RUBBER_VALUES
 * -------------------
 * NOTE: Allow this enum to evaluate false */
#define SPARE_RUBBER_OFF               0
#define SPARE_RUBBER_PATH              1
#define SPARE_RUBBER_POLYGON           2
#define SPARE_RUBBER_POLYLINE          3


/* PREVIEW_CLONE_VALUES
 * --------------------
 * NOTE: Allow this enum to evaluate false */
#define PREVIEW_CLONE_NULL            0
#define PREVIEW_CLONE_SELECTED        1
#define PREVIEW_CLONE_RUBBER          2


/* PREVIEW_MODE_VALUES
 * -------------------
 * NOTE: Allow this enum to evaluate false */
#define PREVIEW_MODE_NULL             0
#define PREVIEW_MODE_MOVE             1
#define PREVIEW_MODE_ROTATE           2
#define PREVIEW_MODE_SCALE            3


/* COMMAND ACTIONS */
/* --------------- */
#define ACTION_donothing              0
#define ACTION_new                    1
#define ACTION_open                   2
#define ACTION_save                   3
#define ACTION_saveas                 4
#define ACTION_print                  5
#define ACTION_designdetails          6
#define ACTION_exit                   7
#define ACTION_cut                    8
#define ACTION_copy                   9
#define ACTION_paste                 10
#define ACTION_undo                  11
#define ACTION_redo                  12
/* Window Menu */
#define ACTION_windowclose           13
#define ACTION_windowcloseall        14
#define ACTION_windowcascade         15
#define ACTION_windowtile            16
#define ACTION_windownext            17
#define ACTION_windowprevious        18
/* Help Menu */
#define ACTION_help                  19
#define ACTION_changelog             20
#define ACTION_tipoftheday           21
#define ACTION_about                 22
#define ACTION_whatsthis             23
/* Icons */
#define ACTION_icon16                24
#define ACTION_icon24                25
#define ACTION_icon32                26
#define ACTION_icon48                27
#define ACTION_icon64                28
#define ACTION_icon128               29
#define ACTION_settingsdialog        30
/* Layer ToolBar */
#define ACTION_makelayercurrent      31
#define ACTION_layers                32
#define ACTION_layerselector         33
#define ACTION_layerprevious         34
#define ACTION_colorselector         35
#define ACTION_linetypeselector      36
#define ACTION_lineweightselector    37
#define ACTION_hidealllayers         38
#define ACTION_showalllayers         39
#define ACTION_freezealllayers       40
#define ACTION_thawalllayers         41
#define ACTION_lockalllayers         42
#define ACTION_unlockalllayers       43
/* Text ToolBar */
#define ACTION_textbold              44
#define ACTION_textitalic            45
#define ACTION_textunderline         46
#define ACTION_textstrikeout         47
#define ACTION_textoverline          48
/* Zoom ToolBar */
#define ACTION_zoomrealtime          49
#define ACTION_zoomprevious          50
#define ACTION_zoomwindow            51
#define ACTION_zoomdynamic           52
#define ACTION_zoomscale             53
#define ACTION_zoomcenter            54
#define ACTION_zoomin                55
#define ACTION_zoomout               56
#define ACTION_zoomselected          57
#define ACTION_zoomall               58
#define ACTION_zoomextents           59
/* Pan SubMenu */
#define ACTION_panrealtime           60
#define ACTION_panpoint              61
#define ACTION_panleft               62
#define ACTION_panright              63
#define ACTION_panup                 64
#define ACTION_pandown               65
/* View */
#define ACTION_day                   66
#define ACTION_night                 67

/* Just added */
#define ACTION_trebleclef            68
#define ACTION_path                  69
#define ACTION_circle                70
#define ACTION_line                  71
#define ACTION_distance              72
#define ACTION_dolphin               73
#define ACTION_ellipse               74
#define ACTION_delete                75
#define ACTION_heart                 76
#define ACTION_locatepoint           77
#define N_ACTIONS                    78

/*
TODO: ACTION_spellcheck 
TODO: ACTION_quickselect 
*/

#define circle_mode_1P_RAD            0
#define circle_mode_1P_DIA            1
#define circle_mode_2P                2
#define circle_mode_3P                3
#define circle_mode_TTR               4

#define app_folder                    0
#define commands_folder               1
#define help_folder                   2
#define images_folder                 4
#define samples_folder                5
#define translations_folder           6
#define nFolders                      7

#define PATHS_MOVETO                  0
#define PATHS_LINETO                  1
#define PATHS_ARCTO                   2
#define PATHS_ARCMOVETO               3
#define PATHS_ELLIPSE                 4
#define PATHS_END                     5

#define PERMISSIONS_USER               0
#define PERMISSIONS_SYSTEM             1

#define MAX_DISTANCE              10000000.0

#define DOLPHIN_NUM_POINTS                 0
#define DOLPHIN_XSCALE                     1
#define DOLPHIN_YSCALE                     2

#define ELLIPSE_MAJORDIAMETER_MINORRADIUS  0
#define ELLIPSE_MAJORRADIUS_MINORRADIUS    1
#define ELLIPSE_ROTATION                   2

#define POLYGON_NUM_SIDES                  0
#define POLYGON_CENTER_PT                  1
#define POLYGON_POLYTYPE                   2
#define POLYGON_INSCRIBE                   3
#define POLYGON_CIRCUMSCRIBE               4
#define POLYGON_DISTANCE                   5
#define POLYGON_SIDE_LEN                   6

#define TREBLE_CLEF_MODE_NUM_POINTS        0
#define TREBLE_CLEF_MODE_XSCALE            1
#define TREBLE_CLEF_MODE_YSCALE            2

/*
 * TYPEDEFS
 * ========
 *
 * Action
 * -----------------------------------------------------------------------------
 *
 * OVERVIEW
 *
 * 
 * 
 * -----------------------------------------------------------------------------
 *
 * DESCRIPTION OF STRUCT CONTENTS
 *
 * object 
 *     The object flag 
 *
 * icon
 *     The icon index determines which icon from the table is associate with
 *     the action.
 *
 * (Not implemented)
 *     The permissions flag determines whether the user or the system can
 *     run this action.
 *
 *     The mode argument determines what locations in the interface
 *     the action will appear in, for example in mode MODE_TOOLBAR,
 *     the action appears in the toolbars, in MODE_TOOLBAR | MODE_LINE_EDIT_DOUBLE
 *     it also appears as a lineEdit in the property editor expecting a
 *     double as input.
 *
 * abbreviation
 *     .
 *
 * menu_name
 *     .
 *
 * description
 *     .
 *
 * shortcut
 *     .
 *
 * function
 *     The function to call, which only uses global variables, so we can take
 *     a void in, void out pointer.
 *
 * -----------------------------------------------------------------------------
 *
 * FUNCTIONS
 *
 * The action typedef is used in 
 *
 * -----------------------------------------------------------------------------
 */

typedef struct Action {
    int object;
    const char **icon;
    /* int permissions; */
    /* int mode; */
    char abbreviation[20];
    char menu_name[30];
    char description[100];
    char shortcut[20];
    void (*function)(void);
} action;

/* Widget
 * -----------------------------------------------------------------------------
 *
 * OVERVIEW
 *
 * All buttons, shortcuts, menus and regions of the windows should be widgets.
 *
 * The widgets are stored, accessed and altered via a binary tree where the
 * left side is dominant. 
 *
 * The strength of the new GUI relies heavily on this core concept. All the
 * FreeGLUT 3 calls will happen at the end of calls to the widgets.
 *
 * Perhaps the action system should be connected to this somehow?
 *
 * -----------------------------------------------------------------------------
 *
 * DESCRIPTION OF STRUCT CONTENTS
 *
 * svg_path
 *     If the widget is a button, it needs a symbol. The svg_path is the path
 *     that draws the symbol using the .
 *
 * width
 *     The width as a proportion of the total width of the parent.
 *     0.1 means 10% of the width of the parent.
 *
 * height
 *     The height as a proportion of the total width of the parent.
 *     0.1 means 10% of the width of the parent.
 *
 * n_children
 *     The number of children of this node, capped to 10 during this stage of
 *     development.
 *
 * children
 *     An array of leaf widgets, as part of the tree of widgets. Fill this entry
 *     first, then the right widget, then the left widget's left widget.
 *
 * position
 *     Relative to its parent, where should the widget go (the top left corner's
 *     offset from the top left corner).
 *
 * -----------------------------------------------------------------------------
 *
 * FUNCTIONS
 * 
 * widget *make_widget(float width, float height);
 *     Allocate the memory for the widget and initialise all the values.
 *
 * void draw_widget(widget *w);
 *     Recursively draw the widgets starting at the supplied node, so draw
 *     the window is "draw_widget(root);"
 *
 * void free_widget(widget *w);
 *     Recursively free all the widgets starting at the supplied node.
 *
 * -----------------------------------------------------------------------------
 */

typedef struct Widget_ widget;

struct Widget_ {
    int texture_id;
    EmbVector position;
    float width;
    float height;
    float left;
    float right;
    float top;
    float bottom;
    int n_leaves;
    int size;
    struct Widget_ **leaves;
};

/* Text Properties
 * ---------------
 */

typedef struct Text_Properties {
    float size;
    float angle;
    int bold;
    int italic;
    int underline;
    int overline;
    int strikeout;
    int backward;
    int upsidedown;
} text_properties;


typedef struct circle_args_ {
    float x1;
    float y1;
    float x2;
    float y2;
    float x3;
    float y3;
    float rad;
    float dia;
    float cx;
    float cy;
    int mode;
} circle_args;

typedef struct dolphin_args_ {
    int numPoints;
    float cx;
    float cy;
    float sx;
    float sy;
    int mode;
} dolphin_args;

typedef struct ellipse_args_ {
    float x1;
    float y1;
    float x2;
    float y2;
    float x3;
    float y3;
    float cx;
    float cy;
    float width;
    float height;
    float rot;
    int mode;
} ellipse_args;

typedef struct user_quad__ {
    int flag;
    float left;
    float right;
    float top;
    float bottom;
    float red;
    float green;
    float blue;
} user_quad_;

typedef struct treble_clef_ {
    int num_points;
    double cx;
    double cy;
    double sx;
    double sy;
    int mode;
} treble_clef;

/* Settings Wrapper
 * ----------------
 *
 * The settings wrapper is necessary since during altering a setting
 * the user .
 */

typedef struct Settings_wrapper {
    int window_width;
    int window_height;
    int window_x;
    int window_y;
    int general_icon_size;
    int general_mdi_bg_use_logo;
    int general_mdi_bg_use_texture;
    int general_mdi_bg_use_color;
    int qsnap_endpoint;
    int qsnap_midpoint;
    int qsnap_center;
    int qsnap_node;
    int qsnap_quadrant;
    int qsnap_intersection;
    int qsnap_extension;
    int qsnap_insertion;
    int qsnap_perpendicular;
    int qsnap_tangent;
    int qsnap_nearest;
    int qsnap_apparent;
    int qsnap_parallel;
    int grid_center_on_origin;
    EmbVector grid_center;
    EmbVector grid_size;
    EmbVector grid_spacing;
    float grid_size_radius;
    float grid_spacing_radius;
    float grid_spacing_angle;
    int ruler_show_on_load;
    int ruler_metric;
    int general_tip_of_the_day;
    int general_system_help_browser;
    int general_check_for_updates;
    int display_use_opengl;
    int display_renderhint_aa;
    int display_renderhint_text_aa;
    int display_renderhint_smooth_pix;
    int display_renderhint_high_aa;
    int display_renderhint_noncosmetic;
    int display_show_scrollbars;
    int display_scrollbar_widget_num;
    float display_zoomscale_in;
    float display_zoomscale_out;
    unsigned char display_selectbox_alpha;
    unsigned char display_crosshair_percent;
    int opensave_open_thumbnail;
    int opensave_save_thumbnail;
    unsigned char opensave_recent_max_files;
    unsigned char opensave_trim_dst_num_jumps;
    int printing_use_last_device;
    int printing_disable_bg;
    int grid_show_on_load;
    int grid_show_origin;
    int grid_color_match_crosshair;
    int grid_load_from_file;
    unsigned char ruler_pixel_size;
    int qsnap_enabled;
    unsigned char qsnap_locator_size;
    unsigned char qsnap_aperture_size;
    int lwt_show_lwt;
    int lwt_real_render;
    float lwt_default_lwt;
    int selection_mode_pickfirst;
    int selection_mode_pickadd;
    int selection_mode_pickdrag;
    unsigned char selection_grip_size;
    unsigned char selection_pickbox_size;
    text_properties text_style;

    int rulerPixelSize;
    int gripSize;
    int pickBoxSize;
    int crosshairSize;

    int shiftKeyPressedState;

    int grippingActive;
    int rapidMoveActive;
    int previewActive;
    int pastingActive;
    int movingActive;
    int selectingActive;
    int zoomWindowActive;
    int panningRealTimeActive;
    int panningPointActive;
    int panningActive;
    int qSnapActive;
    int qSnapToggle;

    int rulerMetric;

    char general_language[MAX_STRING_LENGTH];
    char general_icon_theme[MAX_STRING_LENGTH];
    char general_mdi_bg_logo[MAX_STRING_LENGTH];
    char general_mdi_bg_texture[MAX_STRING_LENGTH];
    unsigned int general_mdi_bg_color;
    unsigned short general_current_tip;
    unsigned int display_crosshair_color;
    unsigned int display_bg_color;
    unsigned int display_selectbox_left_color;
    unsigned int display_selectbox_left_fill;
    unsigned int display_selectbox_right_color;
    unsigned int display_selectbox_right_fill;
    char display_units[MAX_STRING_LENGTH];
    char opensave_open_format[MAX_STRING_LENGTH];
    char opensave_save_format[MAX_STRING_LENGTH];
    char opensave_recent_directory[MAX_STRING_LENGTH];
    char printing_default_device[MAX_STRING_LENGTH];
    unsigned int grid_color;
    unsigned int ruler_color;
    unsigned int qsnap_locator_color;
    char grid_type[MAX_STRING_LENGTH];
    unsigned int selection_coolgrip_color;
    unsigned int selection_hotgrip_color;
    char text_font[MAX_STRING_LENGTH];
} settings_wrapper;

/* C Data for embroidermodder
 * --------------------------
 */

extern int *toolbars[], *menus[];
extern action action_list[];
extern int undo_history_length, undo_history_position;
extern const char *actions_strings[], *tips[], *toolbar_label[], *folders[],
    *menu_label[], *settings_tab_label[], *status_bar_label[], *obj_names[],
    *symbol_list[], * _appName_, * _appVer_;
extern char undo_history[1000][100];
extern int exitApp;
extern settings_wrapper settings, preview, dialog, accept_;
extern const char *origin_string[];
extern widget *root;
extern int debug_mode;

extern const char *_3dviews_xpm[];
extern const char *about_xpm[];
extern const char *aligneddimension_xpm[];
extern const char *aligntext_xpm[];
extern const char *aligntextangle_xpm[];
extern const char *aligntextcenter_xpm[];
extern const char *aligntexthome_xpm[];
extern const char *aligntextleft_xpm[];
extern const char *aligntextright_xpm[];
extern const char *angulardimension_xpm[];
extern const char *app_xpm[];
extern const char *arc3points_xpm[];
extern const char *arc_xpm[];
extern const char *arccenterstartangle_xpm[];
extern const char *arccenterstartend_xpm[];
extern const char *arccenterstartlength_xpm[];
extern const char *arccontinue_xpm[];
extern const char *arcstartcenterangle_xpm[];
extern const char *arcstartcenterend_xpm[];
extern const char *arcstartcenterlength_xpm[];
extern const char *arcstartendangle_xpm[];
extern const char *arcstartenddirection_xpm[];
extern const char *arcstartendradius_xpm[];
extern const char *area_xpm[];
extern const char *array_xpm[];
extern const char *backview_xpm[];
extern const char *baselinedimension_xpm[];
extern const char *bean_xpm[];
extern const char *blank_xpm[];
extern const char *bottomview_xpm[];
extern const char *boundary_xpm[];
extern const char *break2points_xpm[];
extern const char *breakatpoint_xpm[];
extern const char *browser_xpm[];
extern const char *camera_xpm[];
extern const char *centermark_xpm[];
extern const char *chamfer_xpm[];
extern const char *changelog_xpm[];
extern const char *check_xpm[];
extern const char *circle2points_xpm[];
extern const char *circle3points_xpm[];
extern const char *circle_xpm[];
extern const char *circlecenterdiameter_xpm[];
extern const char *circlecenterradius_xpm[];
extern const char *circletantanradius_xpm[];
extern const char *circletantantan_xpm[];
extern const char *cloud_2_xpm[];
extern const char *cloud_xpm[];
extern const char *colorblue_xpm[];
extern const char *colorbyblock_xpm[];
extern const char *colorbylayer_xpm[];
extern const char *colorcyan_xpm[];
extern const char *colorgreen_xpm[];
extern const char *colormagenta_xpm[];
extern const char *colorother_xpm[];
extern const char *colorred_xpm[];
extern const char *colorselector_xpm[];
extern const char *colorwhite_xpm[];
extern const char *coloryellow_xpm[];
extern const char *constructionline_xpm[];
extern const char *continuedimension_xpm[];
extern const char *copy_xpm[];
extern const char *copyobject_xpm[];
extern const char *customize_xpm[];
extern const char *customizekeyboard_xpm[];
extern const char *customizemenus_xpm[];
extern const char *customizetoolbars_xpm[];
extern const char *cut_xpm[];
extern const char *date_xpm[];
extern const char *day_xpm[];
extern const char *designdetails_xpm[];
extern const char *diameterdimension_xpm[];
extern const char *dimensionedit_xpm[];
extern const char *dimensionstyle_xpm[];
extern const char *dimensiontextedit_xpm[];
extern const char *dimensionupdate_xpm[];
extern const char *distance_xpm[];
extern const char *dolphin_xpm[];
extern const char *donothing_xpm[];
extern const char *donut_2_xpm[];
extern const char *donut_xpm[];
extern const char *drawing2_xpm[];
extern const char *drawing_xpm[];
extern const char *ellipse_xpm[];
extern const char *ellipsearc_xpm[];
extern const char *ellipseaxisend_xpm[];
extern const char *ellipsecenter_xpm[];
extern const char *erase_xpm[];
extern const char *escape_xpm[];
extern const char *exit_xpm[];
extern const char *explode_xpm[];
extern const char *extend_xpm[];
extern const char *fillet_xpm[];
extern const char *findandreplace_xpm[];
extern const char *freezealllayers_xpm[];
extern const char *frontview_xpm[];
extern const char *gridsettings_xpm[];
extern const char *gridsnapsettings_xpm[];
extern const char *hatch_xpm[];
extern const char *heart_2_xpm[];
extern const char *heart_xpm[];
extern const char *help_2_xpm[];
extern const char *help_xpm[];
extern const char *hex_xpm[];
extern const char *hidealllayers_xpm[];
extern const char *histogram_xpm[];
extern const char *icon128_xpm[];
extern const char *icon16_xpm[];
extern const char *icon24_xpm[];
extern const char *icon32_xpm[];
extern const char *icon48_xpm[];
extern const char *icon64_xpm[];
extern const char *inquiry_xpm[];
extern const char *insertblock_xpm[];
extern const char *join_xpm[];
extern const char *justifytext_xpm[];
extern const char *layerprevious_xpm[];
extern const char *layers_xpm[];
extern const char *layerselector_xpm[];
extern const char *layertranslate_xpm[];
extern const char *leftview_xpm[];
extern const char *lengthen_xpm[];
extern const char *line_xpm[];
extern const char *lineardimension_xpm[];
extern const char *linetypebyblock_xpm[];
extern const char *linetypebylayer_xpm[];
extern const char *linetypecenter_xpm[];
extern const char *linetypecontinuous_xpm[];
extern const char *linetypehidden_xpm[];
extern const char *linetypeother_xpm[];
extern const char *linetypeselector_xpm[];
extern const char *lineweight01_xpm[];
extern const char *lineweight02_xpm[];
extern const char *lineweight03_xpm[];
extern const char *lineweight04_xpm[];
extern const char *lineweight05_xpm[];
extern const char *lineweight06_xpm[];
extern const char *lineweight07_xpm[];
extern const char *lineweight08_xpm[];
extern const char *lineweight09_xpm[];
extern const char *lineweight10_xpm[];
extern const char *lineweight11_xpm[];
extern const char *lineweight12_xpm[];
extern const char *lineweight13_xpm[];
extern const char *lineweight14_xpm[];
extern const char *lineweight15_xpm[];
extern const char *lineweight16_xpm[];
extern const char *lineweight17_xpm[];
extern const char *lineweight18_xpm[];
extern const char *lineweight19_xpm[];
extern const char *lineweight20_xpm[];
extern const char *lineweight21_xpm[];
extern const char *lineweight22_xpm[];
extern const char *lineweight23_xpm[];
extern const char *lineweight24_xpm[];
extern const char *lineweightbyblock_xpm[];
extern const char *lineweightbylayer_xpm[];
extern const char *lineweightdefault_xpm[];
extern const char *lineweightselector_xpm[];
extern const char *lineweightsettings_xpm[];
extern const char *list_xpm[];
extern const char *locatepoint_xpm[];
extern const char *locator_snaptoapparentintersection_xpm[];
extern const char *locator_snaptocenter_xpm[];
extern const char *locator_snaptoendpoint_xpm[];
extern const char *locator_snaptoextension_xpm[];
extern const char *locator_snaptoinsert_xpm[];
extern const char *locator_snaptointersection_xpm[];
extern const char *locator_snaptomidpoint_xpm[];
extern const char *locator_snaptonearest_xpm[];
extern const char *locator_snaptonode_xpm[];
extern const char *locator_snaptoparallel_xpm[];
extern const char *locator_snaptoperpendicular_xpm[];
extern const char *locator_snaptoquadrant_xpm[];
extern const char *locator_snaptotangent_xpm[];
extern const char *lockalllayers_xpm[];
extern const char *makeblock_xpm[];
extern const char *makelayercurrent_xpm[];
extern const char *mass_xpm[];
extern const char *mirror_xpm[];
extern const char *move_xpm[];
extern const char *multiline_xpm[];
extern const char *multilinetext_xpm[];
extern const char *namedviews_xpm[];
extern const char *neisometricview_xpm[];
extern const char *new_xpm[];
extern const char *night_xpm[];
extern const char *nopreview_xpm[];
extern const char *nwisometricview_xpm[];
extern const char *obliquedimensions_xpm[];
extern const char *offset_xpm[];
extern const char *open_xpm[];
extern const char *ordinatedimension_xpm[];
extern const char *orthosettings_xpm[];
extern const char *pan_xpm[];
extern const char *pandown_xpm[];
extern const char *panleft_xpm[];
extern const char *panpoint_xpm[];
extern const char *panrealtime_xpm[];
extern const char *panright_xpm[];
extern const char *panup_xpm[];
extern const char *paste_xpm[];
extern const char *path_xpm[];
extern const char *pickadd_xpm[];
extern const char *picknew_xpm[];
extern const char *plugin_xpm[];
extern const char *point_xpm[];
extern const char *pointdivide_xpm[];
extern const char *pointmeasure_xpm[];
extern const char *pointmultiple_xpm[];
extern const char *pointsingle_xpm[];
extern const char *polarsettings_xpm[];
extern const char *polygon_xpm[];
extern const char *polyline_xpm[];
extern const char *print_xpm[];
extern const char *pyscript_xpm[];
extern const char *qsnapsettings_xpm[];
extern const char *qtracksettings_xpm[];
extern const char *quickdimension_xpm[];
extern const char *quickleader_xpm[];
extern const char *quickselect_xpm[];
extern const char *radiusdimension_xpm[];
extern const char *ray_xpm[];
extern const char *rectangle_xpm[];
extern const char *redo_xpm[];
extern const char *region_xpm[];
extern const char *render_xpm[];
extern const char *rgb_xpm[];
extern const char *rightview_xpm[];
extern const char *rotate_xpm[];
extern const char *rulersettings_xpm[];
extern const char *sandbox_xpm[];
extern const char *satin_xpm[];
extern const char *save_xpm[];
extern const char *saveas_xpm[];
extern const char *scale_xpm[];
extern const char *seisometricview_xpm[];
extern const char *settingsdialog_2_xpm[];
extern const char *settingsdialog_xpm[];
extern const char *shade2dwireframe_xpm[];
extern const char *shade3dwireframe_xpm[];
extern const char *shade_xpm[];
extern const char *shadeflat_xpm[];
extern const char *shadeflatedges_xpm[];
extern const char *shadehidden_xpm[];
extern const char *shadesmooth_xpm[];
extern const char *shadesmoothedges_xpm[];
extern const char *showalllayers_xpm[];
extern const char *singlelinetext_xpm[];
extern const char *sketch_2_xpm[];
extern const char *sketch_xpm[];
extern const char *snapfrom_xpm[];
extern const char *snaptoapparentintersection_xpm[];
extern const char *snaptocenter_xpm[];
extern const char *snaptoendpoint_xpm[];
extern const char *snaptoextension_xpm[];
extern const char *snaptoinsert_xpm[];
extern const char *snaptointersection_xpm[];
extern const char *snaptomidpoint_xpm[];
extern const char *snaptonearest_xpm[];
extern const char *snaptonode_xpm[];
extern const char *snaptonone_xpm[];
extern const char *snaptoparallel_xpm[];
extern const char *snaptoperpendicular_xpm[];
extern const char *snaptoquadrant_xpm[];
extern const char *snaptotangent_xpm[];
extern const char *snowflake_2_xpm[];
extern const char *snowflake_xpm[];
extern const char *solidbox_xpm[];
extern const char *solidcheck_xpm[];
extern const char *solidclean_xpm[];
extern const char *solidcoloredges_xpm[];
extern const char *solidcolorfaces_xpm[];
extern const char *solidcone_xpm[];
extern const char *solidcopyedges_xpm[];
extern const char *solidcopyfaces_xpm[];
extern const char *solidcylinder_xpm[];
extern const char *soliddeletefaces_xpm[];
extern const char *solidextrude_xpm[];
extern const char *solidextrudefaces_xpm[];
extern const char *solidimprint_xpm[];
extern const char *solidinterfere_xpm[];
extern const char *solidintersect_xpm[];
extern const char *solidmovefaces_xpm[];
extern const char *solidoffsetfaces_xpm[];
extern const char *solidrevolve_xpm[];
extern const char *solidrotatefaces_xpm[];
extern const char *solids_xpm[];
extern const char *solidsection_xpm[];
extern const char *solidsediting_xpm[];
extern const char *solidseparate_xpm[];
extern const char *solidsetup_xpm[];
extern const char *solidsetupdrawing_xpm[];
extern const char *solidsetupprofile_xpm[];
extern const char *solidsetupview_xpm[];
extern const char *solidshell_xpm[];
extern const char *solidslice_xpm[];
extern const char *solidsphere_xpm[];
extern const char *solidsubtract_xpm[];
extern const char *solidtaperfaces_xpm[];
extern const char *solidtorus_xpm[];
extern const char *solidunion_xpm[];
extern const char *solidwedge_xpm[];
extern const char *spline_xpm[];
extern const char *star_xpm[];
extern const char *stretch_xpm[];
extern const char *stub_xpm[];
extern const char *surface2dsolid_xpm[];
extern const char *surface3dface_xpm[];
extern const char *surface3dmesh_xpm[];
extern const char *surfacebox_xpm[];
extern const char *surfacecone_xpm[];
extern const char *surfacecylinder_xpm[];
extern const char *surfacedish_xpm[];
extern const char *surfacedome_xpm[];
extern const char *surfaceedge_xpm[];
extern const char *surfaceedgesurface_xpm[];
extern const char *surfacepyramid_xpm[];
extern const char *surfacerevolvedsurface_xpm[];
extern const char *surfaceruledsurface_xpm[];
extern const char *surfaces_xpm[];
extern const char *surfacesphere_xpm[];
extern const char *surfacetabulatedsurface_xpm[];
extern const char *surfacetorus_xpm[];
extern const char *surfacewedge_xpm[];
extern const char *swisometricview_xpm[];
extern const char *temptrackingpoint_xpm[];
extern const char *text_xpm[];
extern const char *textbold_xpm[];
extern const char *textitalic_xpm[];
extern const char *textoverline_xpm[];
extern const char *textstrikeout_xpm[];
extern const char *textunderline_xpm[];
extern const char *thawalllayers_xpm[];
extern const char *theme_xpm[];
extern const char *tipoftheday_2_xpm[];
extern const char *tipoftheday_xpm[];
extern const char *tolerance_xpm[];
extern const char *topview_xpm[];
extern const char *trim_xpm[];
extern const char *undo_xpm[];
extern const char *units_xpm[];
extern const char *unlockalllayers_xpm[];
extern const char *view_xpm[];
extern const char *whatsthis_xpm[];
extern const char *wideflange_xpm[];
extern const char *windowcascade_xpm[];
extern const char *windowclose_xpm[];
extern const char *windowcloseall_xpm[];
extern const char *windownext_xpm[];
extern const char *windowprevious_xpm[];
extern const char *windowtile_xpm[];
extern const char *world_xpm[];
extern const char *zoom_xpm[];
extern const char *zoomall_xpm[];
extern const char *zoomcenter_xpm[];
extern const char *zoomdynamic_xpm[];
extern const char *zoomextents_xpm[];
extern const char *zoomin_xpm[];
extern const char *zoomout_xpm[];
extern const char *zoomprevious_xpm[];
extern const char *zoomrealtime_xpm[];
extern const char *zoomscale_xpm[];
extern const char *zoomselected_xpm[];
extern const char *zoomwindow_xpm[];

/* C functions for embroidermodder
 * -------------------------------
 */

void to_lower(char *, char *);
void usage(void);
void version(void);
void debug_message(const char *format, ...);
void app_dir(char *string, int folder);
int file_exists(char *fname);
int new_main(int argc, char *argv[]);
double radians(double);
double degrees(double);
double sgn(double x);
double theta(double x);
void key_handler(int c, int x, int y);
/* void render_quadlist(quad *qlist); */
void menu___(int key);
void display(void);
char *translate(char *a);

void newFile(void);
void openFile(void);
void saveFile(void);
void saveAsFile(void);
void tipOfTheDay(void);
void main_exit(void);
void main_cut(void);
void main_copy(void);
void main_paste(void);
void main_print(void);
void changelog(void);
void main_about(void);
void main_help(void);

void windowCascade(void);
void windowTile(void);
void windowClose(void);
void windowCloseAll(void);
void windowNext(void);
void windowPrevious(void);

void designDetails(void);
void settingsDialog(void);

void lineTypeSelector(void);
void lineWeightSelector(void);

void whatsthisContextHelp(void);

void colorSelector(void);

void layerSelector(void);
void hideAllLayers(void);
void showAllLayers(void);
void freezeAllLayers(void);
void thawAllLayers(void);
void lockAllLayers(void);
void unlockAllLayers(void);
void makeLayerCurrent(void);

/* Icon Toolbar */
void icon16(void);
void icon24(void);
void icon32(void);
void icon48(void);
void icon64(void);
void icon128(void);

void textItalic(void);
void textOverline(void);
void textStrikeout(void);
void textBold(void);

/* Layer Toolbar */
void makeLayerActive(void);
void layerManager(void);
void layerPrevious(void);

/* Zoom Toolbar */
void zoomRealtime(void);
void zoomPrevious(void);
void zoomWindow(void);
void zoomDynamic(void);
void zoomScale(void);
void zoomCenter(void);
void zoomIn(void);
void zoomOut(void);
void zoomSelected(void);
void zoomAll();
void zoomExtents();

/* Pan SubMenu */
void panrealtime();
void panpoint();
void panLeft();
void panRight();
void panUp();
void panDown();

void dayVision(void);
void nightVision(void);

void main_undo(void);
void main_redo(void);

void doNothing(void);

int load_settings(void);
int save_settings(void);

void comboBoxScrollBarWidgetCurrentIndexChanged(int);
void checkBoxTipOfTheDayStateChanged(int);
void checkBoxUseOpenGLStateChanged(int);
void checkBoxRenderHintAAStateChanged(int);
void checkBoxRenderHintTextAAStateChanged(int);
void checkBoxRenderHintSmoothPixStateChanged(int);
void checkBoxRenderHintHighAAStateChanged(int);
void checkBoxRenderHintNonCosmeticStateChanged(int);
void spinBoxZoomScaleInValueChanged(double);
void spinBoxZoomScaleOutValueChanged(double);
void checkBoxDisableBGStateChanged(int);
void spinBoxGridCenterXValueChanged(double);
void spinBoxGridCenterYValueChanged(double);
void spinBoxGridSizeXValueChanged(double);
void spinBoxGridSizeYValueChanged(double);
void spinBoxGridSpacingXValueChanged(double);
void spinBoxGridSpacingYValueChanged(double);
void spinBoxGridSizeRadiusValueChanged(double);
void spinBoxGridSpacingRadiusValueChanged(double);
void spinBoxGridSpacingAngleValueChanged(double);
void checkBoxRulerShowOnLoadStateChanged(int);
void checkBoxQSnapEndPointStateChanged(int);
void checkBoxQSnapMidPointStateChanged(int);
void checkBoxQSnapCenterStateChanged(int);
void checkBoxQSnapNodeStateChanged(int);
void checkBoxQSnapQuadrantStateChanged(int);
void checkBoxQSnapIntersectionStateChanged(int);
void checkBoxQSnapExtensionStateChanged(int);
void checkBoxQSnapInsertionStateChanged(int);
void checkBoxQSnapPerpendicularStateChanged(int);
void checkBoxQSnapTangentStateChanged(int);
void checkBoxQSnapNearestStateChanged(int);
void checkBoxQSnapApparentStateChanged(int);
void checkBoxQSnapParallelStateChanged(int);
void spinBoxRecentMaxFilesValueChanged(int);
void spinBoxTrimDstNumJumpsValueChanged(int);
void checkBoxGridShowOnLoadStateChanged(int);
void checkBoxGridShowOriginStateChanged(int);
void checkBoxSelectionModePickFirstStateChanged(int);
void checkBoxSelectionModePickAddStateChanged(int);
void checkBoxSelectionModePickDragStateChanged(int);
void sliderSelectionGripSizeValueChanged(int);
void sliderSelectionPickBoxSizeValueChanged(int);
void spinBoxRulerPixelSizeValueChanged(double);

void settingsSnap(void);
void settingsGrid(void);
void settingsRuler(void);
void settingsOrtho(void);
void settingsPolar(void);
void settingsQSnap(void);
void settingsQTrack(void);
void settingsLwt(void);
void toggleSnap(int on);
void toggleGrid(int on);
void toggleRuler(int on);
void toggleOrtho(int on);
void togglePolar(int on);
void toggleQSnap(int on);
void toggleQTrack(int on);
void toggleLwt(int on);
void enableLwt(void);
void disableLwt(void);
void enableReal(void);
void disableReal(void);

void actuator(char *call);

EmbVector unit_vector(float angle);
EmbVector rotate_vector(EmbVector a, float angle);
EmbVector scale_vector(EmbVector a, float scale);
EmbVector scale_and_rotate(EmbVector a, float scale, float angle);

#endif /* EMBROIDERMODDER_H */

