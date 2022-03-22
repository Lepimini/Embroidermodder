#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENCE for licensing terms.

    ------------------------------------------------------------

    This file is for anyone that needs access to the data of
    embroidermodder for another application without booting the program.
    
    So when you import embroidermodder as a module it uses this file.
    But if you call the module like a program:
    
        $ python3 -m embroidermodder
    
    It runs __main__.py instead. This is what the embroidermodder
    command on the command line does.
"""

import libembroidery

from .data import *
from .config import *

