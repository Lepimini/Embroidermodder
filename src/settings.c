/* This file is part of Embroidermodder 2.
 * ------------------------------------------------------------
 * Copyright 2021 The Embroidermodder Team
 * Embroidermodder 2 is Open Source Software.
 * See LICENSE.txt for licensing terms.
 * ------------------------------------------------------------
 * This file is for the in-progress translation of the settings
 * system into C without dependencies.
 */

#include "embroidermodder.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char assets_dir[1000];
char settings_fname[1000];
char settings_data[5000];
char value_out[1000];
int settings_data_length;

char * copy_ini_block(int i, char *data, char *section);
int find_ini_value(char *key, char *out);
int get_ini_int(char *key, int default_value);
float get_ini_float(char *key, float default_value);
int embClamp(int lower, int x, int upper);

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

