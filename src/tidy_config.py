#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENSE for licensing terms.

    ------------------------------------------------------------

    Testing and other meta scripting for Embroidermodder 2, to sit outside
    of installed folder since we don't expect non-developers to use it.

    The sort of things that would normally be covered by a Makefile are
    here, like running the build, testing and linting.
"""

from embroidermodder.config.icons import icons

def tidy_config(chunk_size=75):
    r"""
    Break up long hexdump blocks in configuration
    so they load well in editors.
    """
    output = """#!/usr/bin/env python3

r\"\"\"
    Embroidermodder 2.

    -----

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENSE for licensing terms.

    -----

    Icon hexdumps: sorry this isn't in Unix style.

    Should be replaced with readable code or files.
\"\"\"

icons = {
"""
    for i in icons:
        output += f"    \"{i}\": \"\"\"\n"
        icon = icons[i].replace("\n", "")
        length = len(icon)
        for j in range(1+length//chunk_size):
            bottom = j*chunk_size
            top = min((j+1)*chunk_size, length)
            output += icon[bottom:top] + "\n"
        output += "\"\"\",\n"

    output = output[:-2] + "}\n"

    with open("icons.py", "w", encoding="utf-8") as f:
        f.write(output)


if __name__ == "__main__":
    tidy_config()
