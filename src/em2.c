/* 
 *  Embroidermodder 2.
 *
 *  ------------------------------------------------------------
 *
 *  Copyright 2013-2022 The Embroidermodder Team
 *  Embroidermodder 2 is Open Source Software.
 *  See LICENSE for licensing terms.
 *
 *  ------------------------------------------------------------
 *
 *  Use Python's PEP7 style guide.
 *      https://peps.python.org/pep-0007/
 */

#include "em2.h"

/* Global Settings: should all be */
SDL_Window *window;
SDL_Renderer *renderer;
EmbPattern *pattern[10];
int n_patterns = 0;
/* TTF_Font *font; */
int debug_mode = 1;
char error_msg[MAX_STRING_LENGTH];
char uname_string[MAX_STRING_LENGTH];
char current_file_name[MAX_STRING_LENGTH];
WindowTab *tabs[10];
int n_tabs;
int window_x = 100;
int window_y = 100;
int window_width = 640;
int window_height = 480;
widget *widgets;
int n_widgets = 0;
int n_docs = 0;
int preview_active = 0;
int moving_active = 0;
int panning_active = 0;
int rapid_move_active = 0;
int pasting_active = 0;
int selecting_active = 0;
int zoom_window_active = 0;
int gripping_active = 0;
int general_tip_of_the_day = 0;
int ruler_metric = 1;
int display_use_open_gl = 0;
int display_renderhint_aa = 0;
int display_renderhint_text_aa = 0;
int display_renderhint_smooth_pix = 0;
int display_renderhint_high_aa = 0;
int display_renderhint_noncosmetic = 0;
int display_show_scrollbars = 1;
int display_scrollbar_widget_num = 0;
float display_zoom_scale_action_in = 0.0;
float display_zoom_scale_action_out = 0.0;
unsigned char display_selectbox_alpha = 0;
unsigned char display_crosshair_percent = 0;
double zoom_in_limit = 0.00001;
double zoom_out_limit = 10000.0;
int qsnap_mode[20];
int state[20];
int toggle_status[20];
int tab_index;
char prefix[100];
EmbVector grid_center;
EmbVector grid_size;
EmbVector grid_spacing;
float grid_size_radius;
float grid_spacing_radius;
float grid_spacing_angle;
int ruler_show_on_load;
int general_system_help_browser;
int general_check_for_updates;
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
int ruler_pixel_size = 16;
int grip_size = 16;
int pick_box_size = 16;
int crosshair_size = 16;
char *title_string = "Embroidermodder";
char *em2_version_string = "2.0.0-alpha";
int shift_key_pressed_state;
int qSnapToggle; /* ? */
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
int testing = 0;
/*
char text_font[MAX_STRING_LENGTH];
preview = settings.copy();
dialog = settings.copy();
accept = settings.copy(); */
char undo_history[MAX_UNDO_HISTORY][MAX_STRING_LENGTH];
int undo_history_length;
int undo_history_position;
int undo_history_max = 500;
int undo_history_chunk_size;
char opensave_recent_list_of_files[RECENT_FILES][MAX_STRING_LENGTH];
char opensave_custom_filter[MAX_STRING_LENGTH];
int running;
int real_render;

char welcome_message_em2[20*MAX_STRING_LENGTH];

/* Variable data */
char obj_names[MAX_OBJECTS][MAX_STRING_LENGTH];
char details_label_text[12][MAX_STRING_LENGTH];

int padding = 5;
int button_size = 25;

int dialog_setting_int[100];
double dialog_setting_double[100];

char toolbar_entries[MAX_TOOLBARS][MAX_TOOLBAR_ENTRIES][MAX_STRING_LENGTH];
char menu_entries[MAX_TOOLBARS][MAX_TOOLBAR_ENTRIES][MAX_STRING_LENGTH];
char statusbar_label[MAX_MENU_LENGTH][MAX_STRING_LENGTH];

void create_window(void);
void process_input(scheme *sc);
void main_loop(scheme *sc);
void create_widget(SDL_Rect rect, char *action_id);
int click_detection(widget *w, int x, int y);

/* Settings
 * --------
 */
Setting
grid_ruler_misc_settings[] = {
	{
		"Initially show grid when loading a file",
		INT_GRID_SHOW_ON_LOAD,
		"int",
		0,
		1,
		0,
		0,
		ALIGN_LEFT
    },
    {
		"Show the origin when the grid is enabled",
		INT_GRID_SHOW_ORIGIN,
		"int",
		0,
		1,
		1,
		0,
		ALIGN_LEFT
	},
    {
		"END",
		-1,
		-1,
		-1,
		-1,
		-1,
		-1,
		-1
	}
};

Setting
grid_ruler_color_settings[] = {
    {
		"Match grid color to crosshair color",
		INT_GRID_COLOR_MATCH_CROSSHAIR,
		"int",
		0,
		1,
		0,
		0,
		ALIGN_LEFT
	},
    {
		"END",
		-1,
		-1,
		-1,
		-1,
		-1,
		-1,
		-1
	}
};

SettingBox
grid_ruler_boxes[] = {
    {
  	    "Grid Misc",
    	grid_ruler_misc_settings
	},
    {
		"Grid Color",
		grid_ruler_color_settings
	}
};

const
SettingsTab grid_ruler_settings = {
    "Grid/Ruler",
    2,
    grid_ruler_boxes
};

int
load_scheme_file(scheme *sc, char *fname)
{
    FILE *fin;
    fin = fopen(fname, "r");
    if (!fin) {
        puts("Failed to load initiation file.");
        return 3;
    }
    scheme_load_named_file(sc, fin, fname);
    fclose(fin);
    return 0;
}

char *
load_str(scheme *sc, char *key)
{
    pointer b = scheme_apply0(sc, key);
    return scheme_string_value(b);
}

char *
load_str_from_table(scheme *sc, char *key, int i)
{
    char call[200];
    pointer b;
    sprintf(call, "(define (output) (vector-ref (%s) %d))", key, i);
    scheme_load_string(sc, call);
    return load_str(sc, "output");
}

int
load_real(scheme *sc, char *key)
{
    pointer b = scheme_apply0(sc, key);
    return scheme_rvalue(b);
}

void
create_actions(scheme *sc)
{
    int i;
    for (i=0; action_list[i].command[0] != 'E'; i++) {
        scheme_define(
            sc,
            sc->global_env,
            mk_symbol(sc, action_list[i].command),
            mk_foreign_func(sc, action_list[i].function));
    }
}

/*
 * ACTUATOR
 *
 * In order to have a complex version of saving work, with backups,
 * undo history and forks we need a good recording of what has happened.
 *
 * An action has been taken, we are at the current head of the stack.
 *
 * The action string is a (hopefully valid) lisp expression
 * that is sent to the scheme state.
 */
int
actuator(scheme *sc, char *action)
{
    undo_history_position++;
    if (undo_history_max <= undo_history_position) {
        int i;
        for (i=0; i<undo_history_max-undo_history_chunk_size; i++) {
            strcpy(undo_history[i], undo_history[i+undo_history_chunk_size]);
        }
        undo_history_position -= undo_history_chunk_size;
    }
    strcpy(undo_history[undo_history_position], action);

    printf("action: %s\n", action);
    scheme_apply0(sc, action);

    return 0;
}


/* Function definitions */
int
main(int argc, char *argv[])
{
    scheme *sc;
    int file, i;
    if (!scheme_init(&sc)) {
        puts("Could not initialise TinyScheme.");
        return 2;
    }

    if (load_scheme_file(sc, "assets/boot.scm")) {
        return 3;
    }

    puts("Booting...");
    for (i=0; strcmp("END", load_str_from_table(sc, "files-to-load", i)); i++) {
        printf("%s\n", load_str_from_table(sc, "files-to-load", i));
        char *ptr = load_str_from_table(sc, "files-to-load", i);
        load_scheme_file(sc, ptr);
    }

    create_actions(sc);

    for (i=1; i<argc; i++) {
        if (!strcmp(argv[i], "--debug") || !strcmp(argv[i], "-d")) {
            debug_mode = 1;
            printf("DEBUG MODE\n");
        }
        if (!strcmp(argv[i], "--help") || !strcmp(argv[i], "-h")) {
            puts(welcome_message_em2);
        }
        if (!strcmp(argv[i], "--version") || !strcmp(argv[i], "-v")) {
            printf("%s %s\n", load_str(sc, "title"), load_str(sc, "version"));
        }
        if (!strcmp(argv[i], "--test")) {
            testing = 1;
        }
        /* else copy to files to open 
        elif (exists(argv[i]) and valid_file_format(argv[i]) ) {
            filesToOpen += [argv[i]];
        }*/
    }

    /* 
    filesToOpen = []

    main_win.set_window_title(title + " " + version);
    */
    /* NOTE: If open_files_selected() is called from within the mainWin
     * constructor, slot commands wont work and the window menu will be
     * screwed.
     */
    /*
    if len(filesToOpen) > 0:
        main_win.open_files_selected(filesToOpen);

    return app.mainloop(); */
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        return 1;
    }

    /*
    if (TTF_Init() < 0) {
        return 2;
    }
    font = TTF_OpenFont("assets/fonts/source-sans/TTF/SourceSans3-Black.ttf", 16);
    if (font == NULL) {
        debug_message("Interface font failed to load.");
    }
    */

    create_window();

    if (load_scheme_file(sc, "assets/post-boot.scm")) {
        return 3;
    }
    /* Open tabs here */
    /*
    if (argc > 10) {
        argc = 10;
    }
    for (file=1; file<argc; file++) {
        pattern[file-1] = embPattern_create();
        embPattern_readAuto(pattern[file-1], argv[file]);
    }*/

    if (testing) {
		if (load_scheme_file(sc, "assets/testing.scm")) {
		    return 4;
		}
    }
    else {
        main_loop(sc);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    /* TTF_CloseFont(font);
    TTF_Quit(); */
    return 0;
}


/* The main rendering loop.
 */
void
main_loop(scheme *sc)
{
    while (running) {
        process_input(sc);
        render();
        SDL_RenderPresent(renderer);
        SDL_Delay(50);
    }
}

/* Process input: main loop step 1.
 */
void
process_input(scheme *sc)
{
    int i;
    /* Get keyboard and mouse state. */
    SDL_Event event;
    while (SDL_PollEvent(&event)) {
        if (event.type == SDL_QUIT) {
            running = 0;
            continue;
        }
        if (event.type == SDL_KEYDOWN) {
            continue;
        }
        if (event.type == SDL_MOUSEBUTTONDOWN) {
            for (i=0; i<n_widgets; i++) {
                if (click_detection(&(widgets[i]),
                    event.button.x, event.button.y)) {
                    actuator(sc, widgets[i].command);
                }
            }
        }
    }
}

int
print_all_variables(void)
{
    ;
    return 1;
}

/* Renderer for patterns.
 */
int
render(void)
{
    int i;
    for (i=0; i<n_widgets; i++) {
        if (widgets[i].mode == WIDGET_MODE_BLOCK) {
            SDL_RenderCopy(renderer,
                widgets[i].texture,
                NULL,
                &widgets[i].rect);
        }
    }
    return 0;
}

int
click_detection(widget *w, int x, int y)
{
    return (w->rect.x < x)
        && (x < w->rect.x + w->rect.w)
        && (w->rect.y < y)
        && (y < w->rect.y + w->rect.h);
}

void
make_rectangle(SDL_Rect *rect, int x, int y, int w, int h)
{
    rect->x = x;
    rect->y = y;
    rect->w = w;
    rect->h = h;
}

pointer
pair_cddr(pointer args)
{
    return pair_cdr(pair_cdr(args));
}

pointer
pair_cdddr(pointer args)
{
    return pair_cdr(pair_cdr(pair_cdr(args)));
}

int
get_int_from_closure(pointer args)
{
    return (int)ivalue(pair_car(args));
}

pointer
scm_create_widget(scheme *sc, pointer args)
{
    char icon_path[2*MAX_STRING_LENGTH];
    SDL_Surface *surface;
    SDL_Rect rect;
    debug_message("Create widget.");
    if (args == sc->NIL) {
        return sc->NIL;
    }
    
    printf("%d\n", list_length(sc, args));
    
    rect.x = get_int_from_closure(args);
    printf("x: %d\n", rect.x);

    pointer arg2 = pair_cdr(args);
    rect.y = get_int_from_closure(arg2);
    printf("y: %d\n", rect.y);

    pointer arg3 = pair_cdr(arg2);
    rect.w = get_int_from_closure(arg3);
    printf("w: %d\n", rect.w);

    pointer arg4 = pair_cdr(arg3);
    rect.h = get_int_from_closure(arg4);
    printf("h: %d\n", rect.h);
    
    printf("n_widgets: %d\n", n_widgets);

    widgets[n_widgets].rect = rect;
    widgets[n_widgets].mode = WIDGET_MODE_BLOCK;

    pointer arg5 = pair_cdr(arg4);
    strcpy(widgets[n_widgets].command, string_value(pair_car(arg5)));
    
    sprintf(icon_path, "assets/icons/%s.png", widgets[n_widgets].command);
    surface = IMG_Load(icon_path);
    widgets[n_widgets].texture = SDL_CreateTextureFromSurface(renderer, surface);
    if (!widgets[n_widgets].texture) {
        debug_message("Failed to load texture.");
        debug_message(icon_path);
    }
    SDL_FreeSurface(surface);

    n_widgets++;

    return sc->NIL;
}

/* A negative action_id means it is not an actor.
 */
void
create_widget(SDL_Rect rect, char *action_id)
{
    char icon_path[2*MAX_STRING_LENGTH];
    int i;
    SDL_Surface *surface;
    int act = 0;
    widgets[n_widgets].rect = rect;
    widgets[n_widgets].mode = WIDGET_MODE_BLOCK;
    debug_message(action_id);
    for (i=0; action_list[i].command[0] != 'E'; i++) {
        if (!strcmp(action_id, action_list[i].command)) {
            act = i;
        }
    }
    sprintf(icon_path, "assets/icons/%s.png", action_list[act].command);
    surface = IMG_Load(icon_path);
    widgets[n_widgets].texture = SDL_CreateTextureFromSurface(renderer, surface);
    if (!widgets[n_widgets].texture) {
        debug_message("Failed to load texture.");
        debug_message(action_list[act].command);
    }
    SDL_FreeSurface(surface);
    /* By default a widget cannot perform actions. */
    strcpy(widgets[n_widgets].command, action_id);
    n_widgets++;
}

void
make_toolbar(SDL_Rect rect, char **actions)
{
    int i;
    create_widget(rect, "do_nothing");
    rect.x += padding;
    rect.y += padding;
    rect.w = button_size;
    rect.h = button_size;
    for (i=0; actions[i][0]!='E'; i++) {
        /* char *icon = action_list[index].icon; */
        /*  icon, "button_background_color", */
        create_widget(rect, actions[i]);
        rect.x += padding+button_size;
    }
}

/* Create the window: the window and renderer variables
 * are file scope.
 *
 * In order to carry the data from file to file all the project
 * scope data is stored in here.
 */
void
create_window(void)
{
    SDL_Rect rect;
    int button_size = 25;
    running = 1;
    window = SDL_CreateWindow(
        title_string, window_x, window_y, window_width, window_height,
        SDL_WINDOW_SHOWN);
    renderer = SDL_CreateRenderer(
        window, -1, SDL_RENDERER_ACCELERATED);
    n_widgets = 0;
    widgets = (widget*)malloc(sizeof(widget)*1000);
    debug_message("background");
    /* Background */
    make_rectangle(&rect, 0, 0, 640, 480);
    /*  NULL, "background_color",  */
    create_widget(rect, "do_nothing");
    /* Menubar */
    debug_message("menubar");
    make_rectangle(&rect, 0, 0, 640, 40);
    /*  NULL, "interface_color",  */
    create_widget(rect, "do_nothing");

    /* File Toolbar */
    debug_message("file");
    make_rectangle(&rect, 0, 45, padding*6+button_size*5, padding*2+button_size);
    /*
    make_toolbar(rect, (char**)toolbar_entries[0]);
    */

    /* Edit Toolbar */
    debug_message("edit");
    make_rectangle(&rect, padding*7+button_size*5, 45, padding*6+button_size*5, padding*2+button_size);
    /*
    make_toolbar(rect, (char**)toolbar_entries[1]);
    */

    /* Window Toolbar */
    make_rectangle(&rect, padding*14+button_size*10, 45, padding*7+button_size*6, padding*2+button_size);
    /*
    make_toolbar(rect, (char**)toolbar_entries[3]);
    */

    /* Statusbar */
    make_rectangle(&rect, 0, 455, 640, 25);
    /*  NULL, "interface_color", */
    create_widget(rect, "do_nothing");
}

/*
 */
void
set_prompt_prefix(char *msg)
{
    /* From an old version, when the prompt was embedded. */
    if (debug_mode) {
        FILE *file;
        file = fopen("prompt.txt", "a");
        fprintf(file, "%s\n", msg);
        fclose(file);
    }

    /* strcpy(prompt, msg); */
}


/* Write the current settings to the standard file as ini. */
void
write_settings(void)
{
    debug_message("Writing settings...");
    /* 
    settings_fname = APPLICATION_FOLDER + os.sep + "settings.json"
    json_str = json.dumps(settings, indent=4)
    if os.path.isfile(settings_fname)
        with open(settings_fname, "w", encoding="utf-8") as settings_file:
            settings_file.write(json_str)
    else:
        print("Failed to open settings file to write state.");


    settings["window_x"] = pos().x();
    settings["window_y"] = pos().y();
    settings["window_width"] = size().width();
    settings["window_height"] = size().height();
    */
}

/* .
 */
int
find_mdi_window(char *file_name)
{
    char *canonical_path;
    debug_message("find_mdi_window(fileName)");
    /*
    canonical_path = canonical_file_path(file_name);

    for (subWindow in mdi_area.sub_window_list(void)) {
        if (subWindow.getCurrentFile() == canonicalFilePath) {
            return subWindow;
        }
    }
    */
    return 0;
}

