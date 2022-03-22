#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENCE for licensing terms.

    ------------------------------------------------------------

    All the imports needed to make the xpms available.
"""

from PIL import Image, ImageDraw, ImageTk

def draw_icon(code):
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

icon_svg = {
    "about": [
        "arc 0 0 128 128 1 -1 black 3",
        "arc 0 0 128 128 -2 2 black 3",
        "arc 20 20 108 108 40 -40 black 3"
    ],
    "aligntext": [
        "rect 0 0 128 128 #f4ed04"
    ],
    "aligntextangle": [
        "rect 0 0 128 128 #f4ed04"
    ],
    "aligntextcenter": [
        "rect 0 0 128 128 #f4ed04"
    ],
    "aligntexthome": [
        "rect 0 0 128 128 #f4ed04"
    ],
    "aligntextleft": [
        "rect 0 0 128 128 #f4ed04"
    ],
    "aligntextright": [
        "rect 0 0 128 128 #f4ed04"
    ],
    "blank": [
        "rect 0 0 128 128 #000000"
    ],
    "camera": [
        "rect 0 0 128 128 #da0608"
    ],
    "colorselector": [
        "rect 0 0 128 128 #1210bd"
    ],
    "colorother": [
        "rect 0 0 128 128 #000000"
    ],
    "customizekeyboard": [
        "rect 0 0 128 128 #f4ed04"
    ],
    "customizemenus": [
        "rect 0 0 128 128 #f4ed04"
    ],
    "customizetoolbars": [
        "rect 0 0 128 128 #f4ed04"
    ],
    "customize": [
        "rect 0 0 128 128 #f4ed04"
    ],
    "date": [
        "rect 0 0 128 128 #1210bd"
    ],
    "donothing": [
        "rect 0 0 128 128 #000000"
    ],
    "escape": [
        "rect 0 0 128 128 #f4ed04"
    ],
    "freezealllayers": [
        "rect 0 0 128 128  #1210bd"
    ],
    "surfaces": [
        "rect 0 0 128 128 #f4ed04"
    ],
    "surfacetabulatedsurface": [
        "rect 0 0 128 128 #7a090b"
    ],
    "surfacetorus": [
        "rect 0 0 128 128 #7a090b"
    ],
    "surfacewedge": [
        "rect 0 0 128 128 #7a090b"
    ],
    "thawalllayers": [
        "rect 0 0 128 128 #1210bd"
    ],
    "tolerance": [
        "rect 0 0 128 128 #1210bd"
    ],
    "units": [
        "rect 0 0 128 128 #1210bd"
    ],
    "unlockalllayers": [
        "rect 0 0 128 128 #1210bd"
    ],
    "view": [
        "rect 0 0 128 128 #1210bd"
    ],
    "wideflange": [
        "rect 0 0 128 128 #0daa10"
    ]
}

icons = {}

for icon in icon_svg.keys():
    icons[icon] = draw_icon(icon_svg[icon])

"""

    "hex": ["rect 0 0 128 128  #1210bd"]
    "hidealllayers": ["rect 0 0 128 128  #1210bd"]
    "join": ["rect 0 0 128 128  #1210bd"]
    "justifytext": ["rect 0 0 128 128  #1210bd"]
    "layerselector": ["rect 0 0 128 128  #1210bd"]
    "lockalllayers" = [
        "rect 0 0 128 128 #1210bd"
    ],
    "namedviews": [
        "rect 0 0 128 128 #da0608"
    ],
    "obliquedimensions": ["rect 0 0 128 128 #f4ed04"]
    "ordinatedimension": ["rect 0 0 128 128 #1210bd"]
    "plugin": ["rect 0 0 128 128 #0daa10"]
    "render": ["rect 0 0 128 128 #f4ed04"]
    "shadeflatedges": ["rect 0 0 128 128 #f4ed04"]
    "shadeflat": ["rect 0 0 128 128 #f4ed04"]
    "shadehidden": ["rect 0 0 128 128 #f4ed04"]
    "shadesmoothedges": ["rect 0 0 128 128 #f4ed04"]
    "shadesmooth": ["rect 0 0 128 128 #f4ed04"]
    "shade": ["rect 0 0 128 128 #f4ed04"]
    "showalllayers": ["rect 0 0 128 128 #1210bd"]
    "solidcheck": ["rect 0 0 128 128 #b707a9"]
    "solidclean": ["rect 0 0 128 128 #b707a9"]
    "solidcoloredges": ["rect 0 0 128 128  #b707a9"]
    "solidcolorfaces": ["rect 0 0 128 128  #b707a9"]
    "solidcopyedges": ["rect 0 0 128 128 #b707a9"]
    "solidcopyfaces": ["rect 0 0 128 128 #b707a9"]
    "solidcylinder": ["rect 0 0 128 128 #7a7e01"]
    "soliddeletefaces": ["rect 0 0 128 128 #b707a9"]
    "solidextrudefaces": ["rect 0 0 128 128 #b707a9"]
    "solidextrude": ["rect 0 0 128 128 #7a7e01"]
    "solidimprint": ["rect 0 0 128 128 #b707a9"]
    "solidinterfere": ["rect 0 0 128 128 #7a7e01"]
    "solidmovefaces": ["rect 0 0 128 128  #b707a9"]
    "solidoffsetfaces": ["rect 0 0 128 128  #b707a9"]
    "solidrevolve": ["rect 0 0 128 128  #7a7e01"]
    "solidrotatefaces": ["rect 0 0 128 128  #b707a9"]
    "solidsection": ["rect 0 0 128 128  #7a7e01"]
    "solidsediting": ["rect 0 0 128 128  #b707a9"]
    "solidseparate": ["rect 0 0 128 128  #b707a9"]
    "solidsetupdrawing": ["rect 0 0 128 128  #7a7e01"]
    "solidsetupprofile": ["rect 0 0 128 128  #7a7e01"]
    "solidsetupview": ["rect 0 0 128 128  #7a7e01"]
    "solidsetup": ["rect 0 0 128 128 #7a7e01"]
    "solidshell": ["rect 0 0 128 128 #b707a9"]
    "solidslice": ["rect 0 0 128 128 #7a7e01"]
    "solidsphere": ["rect 0 0 128 128 #7a7e01"]
    "solids": ["rect 0 0 128 128  #f4ed04"]
    "solidtaperfaces": ["rect 0 0 128 128  #b707a9"]
    "solidtorus": ["rect 0 0 128 128  #7a7e01"]
    "solidwedge": ["rect 0 0 128 128  #7a7e01"]
    "stub": ["rect 0 0 128 128  #62b251"]
    "surface2dsolid": ["rect 0 0 128 128  #7a090b"]
    "surface3dface": ["rect 0 0 128 128  #7a090b"]
    "surface3dmesh": ["rect 0 0 128 128  #7a090b"]
    "surfacebox": ["rect 0 0 128 128  #7a090b"]
    "surfacecone": ["rect 0 0 128 128  #7a090b"]
    "surfacecylinder": ["rect 0 0 128 128  #7a090b"]
    "surfacedish": ["rect 0 0 128 128  #7a090b"]
    "surfacedome": ["rect 0 0 128 128  #7a090b"]
    "surfaceedgesurface": ["rect 0 0 128 128  #7a090b"]
    "surfaceedge": ["rect 0 0 128 128 #7a090b"],
    "surfacepyramid": ["rect 0 0 128 128 #7a090b"],
    "surfacerevolvedsurface": ["rect 0 0 128 128 #7a090b"],
    "surfaceruledsurface": ["rect 0 0 128 128 #7a090b"],
    "surfacesphere": ["rect 0 0 128 128 #7a090b"],
    """

linetypebyblock_xpm = [ "C 256 64 rect 0 30 256 35 #000000" ]
linetypebylayer_xpm = [ "C 256 64 rect 0 30 256 35 #000000" ]
linetypecenter_xpm = [ "C 256 64 rect 0 30 256 35 #000000" ]
linetypecontinuous_xpm = [ "C 256 64 rect 0 30 256 35 #000000" ]
linetypehidden_xpm = [ "C 256 64 rect 0 30 256 35 #000000" ]
linetypeother_xpm = [ "C 256 64" ]
linetypeselector_xpm = ["rect 0 0 128 128 #1210bd"]
lineweight01_xpm = [ "C 256 64 rect 0 30 256 35 #000000" ]
lineweight02_xpm = [ "C 256 64 rect 0 29 256 36 #000000" ]
lineweight03_xpm = [ "C 256 64 rect 0 28 256 37 #000000" ]
lineweight04_xpm = [ "C 256 64 rect 0 27 256 38 #000000" ]
lineweight05_xpm = [ "C 256 64 rect 0 26 256 39 #000000" ]
lineweight06_xpm = [ "C 256 64 rect 0 25 256 40 #000000" ]
lineweight07_xpm = [ "C 256 64 rect 0 24 256 41 #000000" ]
lineweight08_xpm = [ "C 256 64 rect 0 23 256 42 #000000" ]
lineweight09_xpm = [ "C 256 64 rect 0 22 256 43 #000000" ]
lineweight10_xpm = [ "C 256 64 rect 0 21 256 44 #000000" ]
lineweight11_xpm = [ "C 256 64 rect 0 20 256 45 #000000" ]
lineweight12_xpm = [ "C 256 64 rect 0 19 256 46 #000000" ]
lineweight13_xpm = [ "C 256 64 rect 0 18 256 47 #000000" ]
lineweight14_xpm = [ "C 256 64 rect 0 17 256 48 #000000" ]
lineweight15_xpm = [ "C 256 64 rect 0 16 256 49 #000000" ]
lineweight16_xpm = [ "C 256 64 rect 0 15 256 50 #000000" ]
lineweight17_xpm = [ "C 256 64 rect 0 14 256 51 #000000" ]
lineweight18_xpm = [ "C 256 64 rect 0 13 256 52 #000000" ]
lineweight19_xpm = [ "C 256 64 rect 0 12 256 53 #000000" ]
lineweight20_xpm = [ "C 256 64 rect 0 11 256 54 #000000" ]
lineweight21_xpm = [ "C 256 64 rect 0 10 256 55 #000000" ]
lineweight22_xpm = [ "C 256 64 rect 0 9 256 56 #000000" ]
lineweight23_xpm = [ "C 256 64 rect 0 8 256 57 #000000" ]
lineweight24_xpm = [ "C 256 64 rect 0 7 256 58 #000000" ]
lineweightbyblock_xpm = [ "C 256 64 rect 0 30 256 35 #000000" ]
lineweightbylayer_xpm = [ "C 256 64 rect 0 30 256 35 #000000" ]
lineweightdefault_xpm = [ "C 256 64 rect 0 30 256 35 #000000" ]
lineweightselector_xpm = [ "C 256 64 rect 0 30 256 35 #000000" ]
lineweightsettings_xpm = [ "C 256 64 rect 0 30 256 35 #000000" ]


