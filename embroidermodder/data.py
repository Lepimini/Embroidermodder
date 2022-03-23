#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENCE for licensing terms.

    ------------------------------------------------------------

    Another attempt at a graphical user interface that runs on
    lots of machines without a complex build or fragile dependencies.

    This is a translation of some of the ideas we came up with for other
    attempts.
"""

import tempfile
import json
import pkg_resources
from .icons import load_image

def load_data(path):
    r"""
    For safe packaging, and to reduce the risk of program
    crashing errors the resources are loaded via a temporary
    file.
    """
    file_data = pkg_resources.resource_string(__name__, path)
    return json.loads(str(file_data, 'utf-8'))

layout = load_data("data/layout.json")
config = load_data("data/config.json")

