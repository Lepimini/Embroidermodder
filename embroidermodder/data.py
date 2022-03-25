#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENCE for licensing terms.

    ------------------------------------------------------------

    Load JSON and PNG files.
"""

import os
from pathlib import Path
import json
import importlib.resources as res
import tkinter as tk

application_folder = str(Path.home()) + os.sep + ".embroidermodder2"


def load_image(path):
    r"""
    For safe packaging, and to reduce the risk of program
    crashing errors the resources are loaded into the
    application folder each time the program boots.
    """
    file_data = res.read_binary("embroidermodder", path)
    a = application_folder + os.sep + path
    f = open(a, "wb")
    f.write(file_data)
    f.close()
    return tk.PhotoImage(file=a)


def draw_icon(code):
    r"""
    Would work on lists like this:

    "about": [
        "arc 0 0 128 128 1 -1 black 3",
        "arc 0 0 128 128 -2 2 black 3",
        "arc 20 20 108 108 40 -40 black 3"
    ]
    out = Image.new("RGB", (128, 128), (255, 255, 255))
    draw = ImageDraw.Draw(out)
    for line in code:
        cmd = line.split(" ")
        if cmd[0] == "arc":
            box = (int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4]))
            start = int(cmd[5])
            end = int(cmd[6])
            draw.arc(box, start, end, fill=cmd[7], width=int(cmd[8]))
    return out
    """
    return "This function is overridden."


def load_data(path):
    r"""
    These are loaded from the Python package first, then
    any that contradict them in the users system override.
    """
    file_data = res.read_text("embroidermodder", path)
    d = json.loads(file_data)
    if not os.path.isdir(application_folder):
        os.mkdir(application_folder)

    fname = application_folder + os.sep + path

    if os.path.isfile(fname):
        with open(fname, "r") as f:
            user_data = json.loads(f.read())
            for k in user_data.keys():
                d[k] = user_data[k]
    else:
        with open(fname, "w") as f:
            f.write(json.dumps(d, indent=4))

    return d


layout = load_data("layout.json")
settings = load_data("config.json")
