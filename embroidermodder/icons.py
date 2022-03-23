#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENSE for licensing terms.

    ------------------------------------------------------------

    All the imports needed to make the xpms available.
"""

import tempfile
import tkinter as tk
import pkg_resources
from PIL import Image, ImageDraw

def load_image(path):
    r"""
    For safe packaging, and to reduce the risk of program
    crashing errors the resources are loaded via a temporary
    file.
    """
    file_data = pkg_resources.resource_string(__name__, path)
    file = tempfile.NamedTemporaryFile()
    file.write(file_data)
    return tk.PhotoImage(file=file.name)

def draw_icon(code):
    r"""
    Would work on lists like this:

    "about": [
        "arc 0 0 128 128 1 -1 black 3",
        "arc 0 0 128 128 -2 2 black 3",
        "arc 20 20 108 108 40 -40 black 3"
    ]
    """
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
