cmake_minimum_required(VERSION 3.5)

project(embroidermodder VERSION 1.0.0 LANGUAGES C CXX)

add_compile_options(
	-g
	-O2
#	-pedantic
#	-Wall
#	-Wextra
#	-Werror
)

add_subdirectory(extern/SDL)
add_subdirectory(extern/SDL_image)
#add_subdirectory(extern/SDL_ttf)
add_subdirectory(extern/libembroidery)
add_subdirectory(extern/TinyScheme)

add_executable(embroidermodder
	src/em2.c
	src/em2.h
	src/action_table.c
	src/edit.c
	src/zoom.c
	src/window.c
	src/text.c
	src/pan.c
	src/layer.c
)

if (WIN32)
target_link_libraries(embroidermodder PRIVATE
	embroidery
	tinyscheme
	SDL2
	SDL2_image
#	SDL2_ttf
)
else (WIN32)
target_link_libraries(embroidermodder PRIVATE
	embroidery
	tinyscheme
	SDL2
	SDL2_image
#	SDL2_ttf
	m
	dl
)
endif (WIN32)

install(
    TARGETS
       embroidermodder
    LIBRARY DESTINATION /usr/lib
    ARCHIVE DESTINATION /usr/lib
    RUNTIME DESTINATION /usr/bin
)
