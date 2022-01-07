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

#include <QSettings>

extern settings_wrapper settings;

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
    }
    fclose(f);

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
    strcpy(settings.general_mdi_bg_logo, get_ini_str("MdiBGLogo", (char *)(QString(assets_dir) + "_images_logo-spirals.png").toLocal8Bit().constData()));
    strcpy(settings.general_mdi_bg_texture, get_ini_str("MdiBGTexture", (char *)(QString(assets_dir) + "_images_texture-spirals.png").toLocal8Bit().constData()));
    settings.general_mdi_bg_color = get_ini_int("MdiBGColor", qRgb(192,192,192));
    settings.general_tip_of_the_day = get_ini_int("TipOfTheDay", 1);
    settings.general_current_tip =  get_ini_int("CurrentTip", 0);
    settings.general_system_help_browser = get_ini_int("SystemHelpBrowser", 1);
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
    
    fprintf(f, "Window_PositionX=%d\r\n", _mainWin->pos().x());
    fprintf(f, "Window_PositionY=%d\r\n", _mainWin->pos().y());
    fprintf(f, "Window_Width=%d\r\n", _mainWin->size().width());
    fprintf(f, "Window_Height=%d\r\n", _mainWin->size().height());

    fclose(f);
}

QString load_setting_str(char *s, char* default_value)
{
    QSettings settings_file(QString(settings_fname), QSettings::IniFormat);
    return settings_file.value(s, default_value).toString();
}

QString load_setting_str(char *s, QString default_value)
{
    QSettings settings_file(QString(settings_fname), QSettings::IniFormat);
    return settings_file.value(s, default_value).toString();
}

int embClamp(int lower, int x, int upper)
{
    x = embMinInt(upper, x);
    x = embMaxInt(lower, x);
    return x;
}

void MainWindow::readSettings()
{
    debug_message("Reading Settings...");

    // This file needs to be read from the users home directory to ensure it is writable
    app_dir(assets_dir, 0);
    strcpy(settings_fname, assets_dir);
    strcat(settings_fname, "settings.ini");

    load_settings();

    QSettings settings_file(QString(assets_dir)+"settings.ini", QSettings::IniFormat);
    QPoint pos(settings.window_x, settings.window_y);
    QSize size(settings.window_width, settings.window_height);

    layoutState = settings_file.value("LayoutState").toByteArray();
    if(!restoreState(layoutState))
    {
        debug_message("LayoutState NOT restored! Setting Default Layout...");
        //someToolBar->setVisible(1);
    }

    //Display
    settings.display_use_opengl = settings_file.value("Display_UseOpenGL", 0).toBool();
    settings.display_renderhint_aa = settings_file.value("Display_RenderHintAntiAlias", 0).toBool();
    settings.display_renderhint_text_aa = settings_file.value("Display_RenderHintTextAntiAlias", 0).toBool();
    settings.display_renderhint_smooth_pix = settings_file.value("Display_RenderHintSmoothPixmap", 0).toBool();
    settings.display_renderhint_high_aa = settings_file.value("Display_RenderHintHighQualityAntiAlias", 0).toBool();
    settings.display_renderhint_noncosmetic = settings_file.value("Display_RenderHintNonCosmetic", 0).toBool();
    settings.display_show_scrollbars = settings_file.value("Display_ShowScrollBars", 1).toBool();
    settings.display_scrollbar_widget_num = settings_file.value("Display_ScrollBarWidgetNum", 0).toInt();
    settings.display_crosshair_color = settings_file.value("Display_CrossHairColor", qRgb(  0, 0, 0)).toInt();
    settings.display_bg_color = settings_file.value("Display_BackgroundColor", qRgb(235,235,235)).toInt();
    settings.display_selectbox_left_color = settings_file.value("Display_SelectBoxLeftColor", qRgb(  0,128, 0)).toInt();
    settings.display_selectbox_left_fill = settings_file.value("Display_SelectBoxLeftFill", qRgb(  0,255, 0)).toInt();
    settings.display_selectbox_right_color = settings_file.value("Display_SelectBoxRightColor", qRgb(  0, 0,128)).toInt();
    settings.display_selectbox_right_fill = settings_file.value("Display_SelectBoxRightFill", qRgb(  0, 0,255)).toInt();
    settings.display_selectbox_alpha = settings_file.value("Display_SelectBoxAlpha", 32).toInt();
    settings.display_zoomscale_in = settings_file.value("Display_ZoomScaleIn", 2.0).toFloat();
    settings.display_zoomscale_out = settings_file.value("Display_ZoomScaleOut", 0.5).toFloat();
    settings.display_crosshair_percent = settings_file.value("Display_CrossHairPercent", 5).toInt();
    strcpy(settings.display_units, settings_file.value("Display_Units", "mm").toString().toLocal8Bit().constData());
    //Prompt
    //OpenSave
    opensave_custom_filter = settings_file.value("OpenSave_CustomFilter", "supported").toString();
    strcpy(settings.opensave_open_format, settings_file.value("OpenSave_OpenFormat", "*.*").toString().toLocal8Bit().constData());
    settings.opensave_open_thumbnail = settings_file.value("OpenSave_OpenThumbnail", 0).toBool();
    strcpy(settings.opensave_save_format, settings_file.value("OpenSave_SaveFormat", "*.*").toString().toLocal8Bit().constData());
    settings.opensave_save_thumbnail = settings_file.value("OpenSave_SaveThumbnail", 0).toBool();
    //Recent
    settings.opensave_recent_max_files = settings_file.value("OpenSave_RecentMax", 10).toInt();
    opensave_recent_list_of_files = settings_file.value("OpenSave_RecentFiles")                                .toStringList();
    strcpy(settings.opensave_recent_directory, settings_file.value("OpenSave_RecentDirectory", QString(assets_dir) + "_samples").toString().toLocal8Bit().constData());
    //Trimming
    settings.opensave_trim_dst_num_jumps = settings_file.value("OpenSave_TrimDstNumJumps", 5).toInt();
    /* Printing
    settings.printing_default_device = settings_file.value("Printing_DefaultDevice", "").toString();
    settings.printing_use_last_device = settings_file.value("Printing_UseLastDevice", 0).toBool();
    settings.printing_disable_bg = settings_file.value("Printing_DisableBG", 1).toBool();
    //Grid */
    settings.grid_show_on_load = settings_file.value("Grid_ShowOnLoad", 1).toBool();
    settings.grid_show_origin = settings_file.value("Grid_ShowOrigin", 1).toBool();
    settings.grid_color_match_crosshair = settings_file.value("Grid_ColorMatchCrossHair", 1).toBool();
    int red = settings_file.value("Grid_ColorR", 0).toInt();
    int green = settings_file.value("Grid_ColorG", 0).toInt();
    int blue = settings_file.value("Grid_ColorB", 0).toInt();
    settings.grid_color = QColor(red, green, blue).rgb();
    settings.grid_load_from_file = settings_file.value("Grid_LoadFromFile", 1).toBool();
    strcpy(settings.grid_type, settings_file.value("Grid_Type", "Rectangular").toString().toLocal8Bit().constData());
    settings.grid_center_on_origin = settings_file.value("Grid_CenterOnOrigin", 1).toBool();
    settings.grid_center.x = settings_file.value("Grid_CenterX", 0.0).toFloat();
    settings.grid_center.y = settings_file.value("Grid_CenterY", 0.0).toFloat();
    settings.grid_size_x = settings_file.value("Grid_SizeX", 100.0).toFloat();
    settings.grid_size_y = settings_file.value("Grid_SizeY", 100.0).toFloat();
    settings.grid_spacing_x = settings_file.value("Grid_SpacingX", 25.0).toFloat();
    settings.grid_spacing_y = settings_file.value("Grid_SpacingY", 25.0).toFloat();
    settings.grid_size_radius = settings_file.value("Grid_SizeRadius", 50.0).toFloat();
    settings.grid_spacing_radius = settings_file.value("Grid_SpacingRadius", 25.0).toFloat();
    settings.grid_spacing_angle = settings_file.value("Grid_SpacingAngle", 45.0).toFloat();
    //Ruler
    settings.ruler_show_on_load = settings_file.value("Ruler_ShowOnLoad", 1).toBool();
    settings.ruler_metric = settings_file.value("Ruler_Metric", 1).toBool();
    settings.ruler_color = settings_file.value("Ruler_Color", qRgb(210,210, 50)).toInt();
    settings.ruler_pixel_size = settings_file.value("Ruler_PixelSize", 20).toInt();
    //Quick Snap
    settings.qsnap_enabled = settings_file.value("QuickSnap_Enabled", 1).toBool();
    settings.qsnap_locator_color = settings_file.value("QuickSnap_LocatorColor", qRgb(255,255, 0)).toInt();
    settings.qsnap_locator_size = settings_file.value("QuickSnap_LocatorSize", 4).toInt();
    settings.qsnap_aperture_size = settings_file.value("QuickSnap_ApertureSize", 10).toInt();
    settings.qsnap_endpoint = settings_file.value("QuickSnap_EndPoint", 1).toBool();
    settings.qsnap_midpoint = settings_file.value("QuickSnap_MidPoint", 1).toBool();
    settings.qsnap_center = settings_file.value("QuickSnap_Center", 1).toBool();
    settings.qsnap_node = settings_file.value("QuickSnap_Node", 1).toBool();
    settings.qsnap_quadrant = settings_file.value("QuickSnap_Quadrant", 1).toBool();
    settings.qsnap_intersection = settings_file.value("QuickSnap_Intersection", 1).toBool();
    settings.qsnap_extension = settings_file.value("QuickSnap_Extension", 1).toBool();
    settings.qsnap_insertion = settings_file.value("QuickSnap_Insertion", 0).toBool();
    settings.qsnap_perpendicular = settings_file.value("QuickSnap_Perpendicular", 1).toBool();
    settings.qsnap_tangent = settings_file.value("QuickSnap_Tangent", 1).toBool();
    settings.qsnap_nearest = settings_file.value("QuickSnap_Nearest", 0).toBool();
    settings.qsnap_apparent = settings_file.value("QuickSnap_Apparent", 0).toBool();
    settings.qsnap_parallel = settings_file.value("QuickSnap_Parallel", 0).toBool();
    //LineWeight
    settings.lwt_show_lwt = settings_file.value("LineWeight_ShowLineWeight", 0).toBool();
    settings.lwt_real_render = settings_file.value("LineWeight_RealRender", 1).toBool();
    settings.lwt_default_lwt = settings_file.value("LineWeight_DefaultLineWeight", 0).toReal();
    //Selection
    settings.selection_mode_pickfirst = settings_file.value("Selection_PickFirst", 1).toBool();
    settings.selection_mode_pickadd = settings_file.value("Selection_PickAdd", 1).toBool();
    settings.selection_mode_pickdrag = settings_file.value("Selection_PickDrag", 0).toBool();
    settings.selection_coolgrip_color = settings_file.value("Selection_CoolGripColor", qRgb(  0, 0,255)).toInt();
    settings.selection_hotgrip_color = settings_file.value("Selection_HotGripColor", qRgb(255, 0, 0)).toInt();
    settings.selection_grip_size = settings_file.value("Selection_GripSize", 4).toInt();
    settings.selection_pickbox_size = settings_file.value("Selection_PickBoxSize", 4).toInt();
    //Text
    strcpy(settings.text_font, settings_file.value("Text_Font", "Arial").toString().toLocal8Bit().constData());
    settings.text_style.size = settings_file.value("Text_Size", 12).toReal();
    settings.text_style.angle = settings_file.value("Text_Angle", 0).toReal();
    settings.text_style.bold = settings_file.value("Text_StyleBold", 0).toBool();
    settings.text_style.italic = settings_file.value("Text_StyleItalic", 0).toBool();
    settings.text_style.underline = settings_file.value("Text_StyleUnderline", 0).toBool();
    settings.text_style.strikeout = settings_file.value("Text_StyleStrikeOut", 0).toBool();
    settings.text_style.overline = settings_file.value("Text_StyleOverline", 0).toBool();

    move(pos);
    resize(size);
}

void MainWindow::writeSettings()
{
    debug_message("Writing Settings...");

    save_settings();

    QSettings settings_file(QString(settings_fname), QSettings::IniFormat);
    QString tmp;

    //General
    settings_file.setValue("LayoutState", layoutState);
    settings_file.setValue("Language", settings.general_language);
    settings_file.setValue("IconTheme", settings.general_icon_theme);
    settings_file.setValue("IconSize", tmp.setNum(settings.general_icon_size));
    settings_file.setValue("MdiBGUseLogo", settings.general_mdi_bg_use_logo);
    settings_file.setValue("MdiBGUseTexture", settings.general_mdi_bg_use_texture);
    settings_file.setValue("MdiBGUseColor", settings.general_mdi_bg_use_color);
    settings_file.setValue("MdiBGLogo", settings.general_mdi_bg_logo);
    settings_file.setValue("MdiBGTexture", settings.general_mdi_bg_texture);
    settings_file.setValue("MdiBGColor", tmp.setNum(settings.general_mdi_bg_color));
    settings_file.setValue("TipOfTheDay", settings.general_tip_of_the_day);
    settings_file.setValue("CurrentTip", tmp.setNum(settings.general_current_tip + 1));
    settings_file.setValue("SystemHelpBrowser", settings.general_system_help_browser);
    //Display
    settings_file.setValue("Display_UseOpenGL", settings.display_use_opengl);
    settings_file.setValue("Display_RenderHintAntiAlias", settings.display_renderhint_aa);
    settings_file.setValue("Display_RenderHintTextAntiAlias", settings.display_renderhint_text_aa);
    settings_file.setValue("Display_RenderHintSmoothPixmap", settings.display_renderhint_smooth_pix);
    settings_file.setValue("Display_RenderHintHighQualityAntiAlias", settings.display_renderhint_high_aa);
    settings_file.setValue("Display_RenderHintNonCosmetic", settings.display_renderhint_noncosmetic);
    settings_file.setValue("Display_ShowScrollBars", settings.display_show_scrollbars);
    settings_file.setValue("Display_ScrollBarWidgetNum", tmp.setNum(settings.display_scrollbar_widget_num));
    settings_file.setValue("Display_CrossHairColor", tmp.setNum(settings.display_crosshair_color));
    settings_file.setValue("Display_BackgroundColor", tmp.setNum(settings.display_bg_color));
    settings_file.setValue("Display_SelectBoxLeftColor", tmp.setNum(settings.display_selectbox_left_color));
    settings_file.setValue("Display_SelectBoxLeftFill", tmp.setNum(settings.display_selectbox_left_fill));
    settings_file.setValue("Display_SelectBoxRightColor", tmp.setNum(settings.display_selectbox_right_color));
    settings_file.setValue("Display_SelectBoxRightFill", tmp.setNum(settings.display_selectbox_right_fill));
    settings_file.setValue("Display_SelectBoxAlpha", tmp.setNum(settings.display_selectbox_alpha));
    settings_file.setValue("Display_ZoomScaleIn", tmp.setNum(settings.display_zoomscale_in));
    settings_file.setValue("Display_ZoomScaleOut", tmp.setNum(settings.display_zoomscale_out));
    settings_file.setValue("Display_CrossHairPercent", tmp.setNum(settings.display_crosshair_percent));
    settings_file.setValue("Display_Units", settings.display_units);
    //Prompt
    //OpenSave
    settings_file.setValue("OpenSave_CustomFilter", opensave_custom_filter);
    settings_file.setValue("OpenSave_OpenFormat", settings.opensave_open_format);
    settings_file.setValue("OpenSave_OpenThumbnail", settings.opensave_open_thumbnail);
    settings_file.setValue("OpenSave_SaveFormat", settings.opensave_save_format);
    settings_file.setValue("OpenSave_SaveThumbnail", settings.opensave_save_thumbnail);
    //Recent
    settings_file.setValue("OpenSave_RecentMax", tmp.setNum(settings.opensave_recent_max_files));
    settings_file.setValue("OpenSave_RecentFiles", opensave_recent_list_of_files);
    settings_file.setValue("OpenSave_RecentDirectory", settings.opensave_recent_directory);
    //Trimming
    settings_file.setValue("OpenSave_TrimDstNumJumps", tmp.setNum(settings.opensave_trim_dst_num_jumps));
    //Printing
    settings_file.setValue("Printing_DefaultDevice", settings.printing_default_device);
    settings_file.setValue("Printing_UseLastDevice", settings.printing_use_last_device);
    settings_file.setValue("Printing_DisableBG", settings.printing_disable_bg);
    //Grid
    settings_file.setValue("Grid_ShowOnLoad", settings.grid_show_on_load);
    settings_file.setValue("Grid_ShowOrigin", settings.grid_show_origin);
    settings_file.setValue("Grid_ColorMatchCrossHair", settings.grid_color_match_crosshair);
    settings_file.setValue("Grid_Color", tmp.setNum(settings.grid_color));
    settings_file.setValue("Grid_ColorR", QColor(settings.grid_color).red());
    settings_file.setValue("Grid_ColorG", QColor(settings.grid_color).green());
    settings_file.setValue("Grid_ColorB", QColor(settings.grid_color).blue());
    settings_file.setValue("Grid_LoadFromFile", settings.grid_load_from_file);
    settings_file.setValue("Grid_Type", settings.grid_type);
    settings_file.setValue("Grid_CenterOnOrigin", settings.grid_center_on_origin);
    settings_file.setValue("Grid_CenterX", tmp.setNum(settings.grid_center.x));
    settings_file.setValue("Grid_CenterY", tmp.setNum(settings.grid_center.y));
    settings_file.setValue("Grid_SizeX", tmp.setNum(settings.grid_size_x));
    settings_file.setValue("Grid_SizeY", tmp.setNum(settings.grid_size_y));
    settings_file.setValue("Grid_SpacingX", tmp.setNum(settings.grid_spacing_x));
    settings_file.setValue("Grid_SpacingY", tmp.setNum(settings.grid_spacing_y));
    settings_file.setValue("Grid_SizeRadius", tmp.setNum(settings.grid_size_radius));
    settings_file.setValue("Grid_SpacingRadius", tmp.setNum(settings.grid_spacing_radius));
    settings_file.setValue("Grid_SpacingAngle", tmp.setNum(settings.grid_spacing_angle));
    //Ruler
    settings_file.setValue("Ruler_ShowOnLoad", settings.ruler_show_on_load);
    settings_file.setValue("Ruler_Metric", settings.ruler_metric);
    settings_file.setValue("Ruler_Color", tmp.setNum(settings.ruler_color));
    settings_file.setValue("Ruler_PixelSize", tmp.setNum(settings.ruler_pixel_size));
    //Quick Snap
    settings_file.setValue("QuickSnap_Enabled", settings.qsnap_enabled);
    settings_file.setValue("QuickSnap_LocatorColor", tmp.setNum(settings.qsnap_locator_color));
    settings_file.setValue("QuickSnap_LocatorSize", tmp.setNum(settings.qsnap_locator_size));
    settings_file.setValue("QuickSnap_ApertureSize", tmp.setNum(settings.qsnap_aperture_size));
    settings_file.setValue("QuickSnap_EndPoint", settings.qsnap_endpoint);
    settings_file.setValue("QuickSnap_MidPoint", settings.qsnap_midpoint);
    settings_file.setValue("QuickSnap_Center", settings.qsnap_center);
    settings_file.setValue("QuickSnap_Node", settings.qsnap_node);
    settings_file.setValue("QuickSnap_Quadrant", settings.qsnap_quadrant);
    settings_file.setValue("QuickSnap_Intersection", settings.qsnap_intersection);
    settings_file.setValue("QuickSnap_Extension", settings.qsnap_extension);
    settings_file.setValue("QuickSnap_Insertion", settings.qsnap_insertion);
    settings_file.setValue("QuickSnap_Perpendicular", settings.qsnap_perpendicular);
    settings_file.setValue("QuickSnap_Tangent", settings.qsnap_tangent);
    settings_file.setValue("QuickSnap_Nearest", settings.qsnap_nearest);
    settings_file.setValue("QuickSnap_Apparent", settings.qsnap_apparent);
    settings_file.setValue("QuickSnap_Parallel", settings.qsnap_parallel);
    //LineWeight
    settings_file.setValue("LineWeight_ShowLineWeight", settings.lwt_show_lwt);
    settings_file.setValue("LineWeight_RealRender", settings.lwt_real_render);
    settings_file.setValue("LineWeight_DefaultLineWeight", tmp.setNum(settings.lwt_default_lwt));
    //Selection
    settings_file.setValue("Selection_PickFirst", settings.selection_mode_pickfirst);
    settings_file.setValue("Selection_PickAdd", settings.selection_mode_pickadd);
    settings_file.setValue("Selection_PickDrag", settings.selection_mode_pickdrag);
    settings_file.setValue("Selection_CoolGripColor", tmp.setNum(settings.selection_coolgrip_color));
    settings_file.setValue("Selection_HotGripColor", tmp.setNum(settings.selection_hotgrip_color));
    settings_file.setValue("Selection_GripSize", tmp.setNum(settings.selection_grip_size));
    settings_file.setValue("Selection_PickBoxSize", tmp.setNum(settings.selection_pickbox_size));
    //Text
    settings_file.setValue("Text_Font", settings.text_font);
    settings_file.setValue("Text_Size", tmp.setNum(settings.text_style.size));
    settings_file.setValue("Text_Angle", tmp.setNum(settings.text_style.angle));
    settings_file.setValue("Text_StyleBold", settings.text_style.bold);
    settings_file.setValue("Text_StyleItalic", settings.text_style.italic);
    settings_file.setValue("Text_StyleUnderline", settings.text_style.underline);
    settings_file.setValue("Text_StyleStrikeOut", settings.text_style.strikeout);
    settings_file.setValue("Text_StyleOverline", settings.text_style.overline);
}

void MainWindow::settingsDialog(const QString& showTab)
{
    Settings_Dialog dialog_(this, showTab, this);
    dialog_.exec();
}

