cmake_minimum_required(VERSION 3.5)

project(embroidermodder VERSION 1.91.0 LANGUAGES C CXX)

set(CMAKE_C_STANDARD 90)
set(CMAKE_C_STANDARD_REQUIRED True)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_AUTOMOC ON)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -pedantic -Wall -O2")

INCLUDE(FindPkgConfig)

if(UNIX AND NOT APPLE)
    set(LINUX TRUE)
endif()

# We currently assume Apple has HOME set, which is not always
# true.
if(UNIX)
set(ASSET_DIR $ENV{HOME}/.embroidermodder2)
else()
set(ASSET_DIR %HOMEDRIVE%%HOMEPATH%\.embroidermodder2)
endif()

find_package(Qt5Widgets)
find_package(OpenGL)

# Most of Embroidermodder is assets, so we just copy a full
# tree to the user's assets folder. That way in an emergency
# everything is traceable.
#
# Trailing / means the DIRECTORY is emptied into the location
# whereas without it means append the DIRECTORY name.
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/ DESTINATION ${ASSET_DIR})

SET(FREEGLUT_SRCS
	freeglut3/include/GL/freeglut.h
	freeglut3/include/GL/freeglut_ucall.h
	freeglut3/include/GL/freeglut_ext.h
	freeglut3/include/GL/freeglut_std.h
	freeglut3/src/fg_callbacks.c
	freeglut3/src/fg_cursor.c
	freeglut3/src/fg_display.c
	freeglut3/src/fg_ext.c
	freeglut3/src/fg_font_data.c
	freeglut3/src/fg_gamemode.c
	freeglut3/src/fg_geometry.c
	freeglut3/src/fg_gl2.c
	freeglut3/src/fg_gl2.h
	freeglut3/src/fg_init.c
	freeglut3/src/fg_init.h
	freeglut3/src/fg_internal.h
	freeglut3/src/fg_callback_macros.h
	freeglut3/src/fg_input_devices.c
	freeglut3/src/fg_joystick.c
	freeglut3/src/fg_main.c
	freeglut3/src/fg_misc.c
	freeglut3/src/fg_overlay.c
	freeglut3/src/fg_spaceball.c
	freeglut3/src/fg_state.c
	freeglut3/src/fg_stroke_mono_roman.c
	freeglut3/src/fg_stroke_roman.c
	freeglut3/src/fg_structure.c
	freeglut3/src/fg_teapot.c
	freeglut3/src/fg_teapot_data.h
	freeglut3/src/fg_videoresize.c
	freeglut3/src/fg_window.c
	freeglut3/src/fg_font.c
        freeglut3/src/fg_menu.c
)

IF(WIN32)
    LIST(APPEND FREEGLUT_SRCS
	freeglut3/src/mswin/fg_cursor_mswin.c
	freeglut3/src/mswin/fg_display_mswin.c
	freeglut3/src/mswin/fg_ext_mswin.c
	freeglut3/src/mswin/fg_gamemode_mswin.c
	freeglut3/src/mswin/fg_init_mswin.c
    	freeglut3/src/mswin/fg_internal_mswin.h
    	freeglut3/src/mswin/fg_input_devices_mswin.c
    	freeglut3/src/mswin/fg_joystick_mswin.c
    	freeglut3/src/mswin/fg_main_mswin.c
    	freeglut3/src/mswin/fg_menu_mswin.c
    	freeglut3/src/mswin/fg_spaceball_mswin.c
    	freeglut3/src/mswin/fg_state_mswin.c
    	freeglut3/src/mswin/fg_structure_mswin.c
    	freeglut3/src/mswin/fg_window_mswin.c
	${CMAKE_BINARY_DIR}/freeglut.rc # generated below from freeglut.rc.in
    )

ELSEIF(ANDROID OR BLACKBERRY)
    # BlackBerry and Android share some similar design concepts and ideas, as with many mobile devices.
    # As such, some classes can be shared between the two. XXX: Possibly rename shareable classes to
    # a more generic name. *_stub? *_mobile?
    LIST(APPEND FREEGLUT_SRCS
	freeglut3/src/android/fg_cursor_android.c
	freeglut3/src/android/fg_ext_android.c
	freeglut3/src/android/fg_gamemode_android.c
	freeglut3/src/android/fg_joystick_android.c
	freeglut3/src/android/fg_spaceball_android.c
    )
    IF(ANDROID)
	LIST(APPEND FREEGLUT_SRCS
		freeglut3/src/android/native_app_glue/android_native_app_glue.c
		freeglut3/src/android/native_app_glue/android_native_app_glue.h
		freeglut3/src/android/fg_internal_android.h
		freeglut3/src/android/fg_init_android.c
		freeglut3/src/android/fg_input_devices_android.c
		freeglut3/src/android/fg_main_android.c
		freeglut3/src/android/fg_main_android.h
		freeglut3/src/android/fg_runtime_android.c
		freeglut3/src/android/fg_state_android.c
		freeglut3/src/android/fg_structure_android.c
		freeglut3/src/android/fg_window_android.c
	)
    ELSE()
	LIST(APPEND FREEGLUT_SRCS
		freeglut3/src/blackberry/fg_internal_blackberry.h
		freeglut3/src/blackberry/fg_init_blackberry.c
		freeglut3/src/x11/fg_input_devices_x11.c
		freeglut3/src/blackberry/fg_main_blackberry.c
		freeglut3/src/blackberry/fg_state_blackberry.c
		freeglut3/src/blackberry/fg_structure_blackberry.c
		freeglut3/src/blackberry/fg_window_blackberry.c
	)
    ENDIF()

ELSE()
	# UNIX (Wayland)
	IF(FREEGLUT_WAYLAND)
	LIST(APPEND FREEGLUT_SRCS
		freeglut3/src/wayland/fg_cursor_wl.c
		freeglut3/src/wayland/fg_ext_wl.c
		freeglut3/src/wayland/fg_gamemode_wl.c
		freeglut3/src/wayland/fg_init_wl.c
		freeglut3/src/wayland/fg_internal_wl.h
		freeglut3/src/wayland/fg_input_devices_wl.c
		freeglut3/src/wayland/fg_main_wl.c
		freeglut3/src/wayland/fg_state_wl.c
		freeglut3/src/wayland/fg_structure_wl.c
		freeglut3/src/wayland/fg_window_wl.c
	# font, serial port & joystick code are agnostic
		freeglut3/src/x11/fg_glutfont_definitions_x11.c
		freeglut3/src/x11/fg_input_devices_x11.c
		freeglut3/src/x11/fg_joystick_x11.c
	)
	# UNIX (X11)
	ELSE()
	LIST(APPEND FREEGLUT_SRCS
		freeglut3/src/x11/fg_cursor_x11.c
		freeglut3/src/x11/fg_ext_x11.c
		freeglut3/src/x11/fg_gamemode_x11.c
		freeglut3/src/x11/fg_glutfont_definitions_x11.c
		freeglut3/src/x11/fg_init_x11.c
		freeglut3/src/x11/fg_internal_x11.h
		freeglut3/src/x11/fg_input_devices_x11.c
		freeglut3/src/x11/fg_joystick_x11.c
		freeglut3/src/x11/fg_main_x11.c
		freeglut3/src/x11/fg_menu_x11.c
		freeglut3/src/x11/fg_spaceball_x11.c
		freeglut3/src/x11/fg_state_x11.c
		freeglut3/src/x11/fg_structure_x11.c
		freeglut3/src/x11/fg_window_x11.c
		freeglut3/src/x11/fg_xinput_x11.c
		freeglut3/src/x11/fg_internal_x11_glx.h
		freeglut3/src/x11/fg_display_x11_glx.c
		freeglut3/src/x11/fg_state_x11_glx.c
	    	freeglut3/src/x11/fg_state_x11_glx.h
	    	freeglut3/src/x11/fg_window_x11_glx.c
	    	freeglut3/src/x11/fg_window_x11_glx.h
	)
	ENDIF()
ENDIF()

add_executable(embroidermodder
	src/main.cpp
	src/actions.cpp
	src/gui.c
	src/config.c
	src/tables.c
	src/embroidermodder.h
	libembroidery/embroidery.c
	${FREEGLUT_SRCS}
)

target_include_directories(embroidermodder PUBLIC
	${CMAKE_CURRENT_SOURCE_DIR}/libembroidery
	${CMAKE_CURRENT_SOURCE_DIR}/freeglut3/include
	${CMAKE_CURRENT_SOURCE_DIR}/freeglut3/src
	${CMAKE_CURRENT_SOURCE_DIR}/src
)

target_link_libraries(embroidermodder
	Qt5::Widgets
	GL
)

if(LINUX)
target_link_libraries(embroidermodder
	X11
)
endif()

set_target_properties(embroidermodder PROPERTIES
    MACOSX_BUNDLE_GUI_IDENTIFIER embroidermodder.embroidermodder.org
    MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
    MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
)

if(LINUX)
install(
    TARGETS
       embroidermodder
    LIBRARY DESTINATION $ENV{HOME}/.local/lib
    ARCHIVE DESTINATION $ENV{HOME}/.local/share
    RUNTIME DESTINATION $ENV{HOME}/.local/bin
)
endif()
