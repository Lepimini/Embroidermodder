# What is Embroidermodder ?

(UNDER MAJOR RESTRUCTURING, PLEASE WAIT FOR VERSION 2)

![Pylint score button](icons/rating.png).

Embroidermodder is a free machine embroidery application.
The newest version, Embroidermodder 2 can:

- edit and create embroidery designs
- estimate the amount of thread and machine time needed to stitch a design
- convert embroidery files to a variety of formats
- upscale or downscale designs
- run on Windows, Mac and Linux

For more information, see [our website](http://embroidermodder.org).

Embroidermodder 2 is very much a work in progress since we're doing a ground
up rewrite to an interface in Python using the GUI toolkit Tk.
The reasoning for this is detailed in the issues tab.

For a more in-depth look at what we are developing read
[`dev_notes.md`](dev_notes.md). This discusses recent changes
in a less formal way than a changelog (since this software is in
development) and covers what we are about to try.

To see what we're focussing on at the moment check this table.

| *Date* | *Event* |
|----|----|
| April-June 2022 | Finish the conversion to Python/Tk |
| July-August 2022 | Finish all the targets in the Design, or assign them to 2.1. |
| September 2022 | Bugfixing, Testing, QA. libembroidery 1.0 will be released, then updates will slow down and the Embroidermodder 2 development version will be fixed to the API of this version. |
| October 2022 | Embroidermodder 2 is officially released. |

## Run

To run the development version, without installing, you can simply run these commands from the top directory:

    $ python3 -m pip install libembroidery
    $ cd src
    $ python3 -m embroidermodder

or, on Windows:

    > py -m pip install libembroidery
    > cd src
    > py -m embroidermodder

From this point on we assume that you have Python installed as `python3` but this same advice applies.

### Run Without Install

If you're using a machine that you don't have to ability to modify
(like some office workstations) you don't need to install libembroidery for
basic functioning.

In this mode the code will be able to read and write SVG embroidery files and do all of the necessary
editing. Should you then wish to convert the result without installing anything then we plan to have
a version of the convert utility as a part of the [embroidermodder.org](https://embroidermodder.org) site.
This would be a version of libembroidery compiled and run through emscripten with a simple form for
putting files in.

## Install

### Desktop

On most sytems the command:

    python3 -m pip install embroidermodder

will install the most up-to date released version.

Currently this is the 2.0-alpha, which will have a build code of
some kind.

### Mobile

These are currently unsupported (see iMobileViewer and Mobileviewer for
iOS and Android respectively), but after the Desktop version is
released we'll work on them.

The Mobile version will share some of the UI and all of the backend,
so development of the Desktop version will help us make both.

## Build

To run the development version just use

    $ python3 -m build
    $ cd dist
    $ python3 -m pip install embroidermodder-2*whl --force-reinstall

before using the command line boot (may be currently broken,
use the next method instead)

    $ embroidermodder

If you are on a shared computer you have some ability to store user data on,
like a university or library machine with a login, then use:

    $ python3 -m embroidermodder

when your shell isn't in the `src/` directory (which will boot the local
version).

This may help if you are running tests that require the `embroidermodder`
command to be in your system `PATH` or you just want to use the
latest version before it comes out for some particular feature.

## Documentation

The documentation is in the form of the website (included in the `docs/`
directory) and the printed docs in the three files:

  * [docs/libembroidery_0.1_manual.pdf](docs/libembroidery_0.1_manual.pdf)
  * [docs/embroidermodder_1.90.0_user_manual.pdf](docs/embroidermodder_1.90.0_user_manual.pdf)
  * [docs/embroidermodder_1.90.0_developer_notes.pdf](docs/embroidermodder_1.90.0_developer_notes.pdf).

## Development

If you wish to develop with us you can chat via the contact email
on the [website](embroidermodder.org) or in the issues tab on the
[github page](https://github.com/Embroidermodder/Embroidermodder/issues).
People have been polite and friendly in these conversations and I (Robin)
have really enjoyed them.
If we do have any arguments please note we have a
[Code of Conduct](CODE_OF_CONDUCT.md) so there is a consistent policy to
enforce when dealing with these arguments.

The first thing you should try is building from source using the [build advice](#build)
above. Then read some of the [development notes](dev_notes.md) to get the general
layout of the source code and what we are currently planning.

### Testing

To find unfixed errors run the `qa_tests()` script in `scripts.py`, then
dig through the output. It's currently not worth reporting the errors, since
there are so many but if you can fix anything reported here you can submit a PR.
