#!/usr/bin/env python3

r"""

This file is part of Embroidermodder 2.

------------------------------------------------------------

    Copyright 2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENSE.txt for licensing terms.

------------------------------------------------------------

This file is only for metaprogramming:

    * Code style maintenence: if you do something that the compiler considers
      correct but we try not to as part of the house style this'll correct it.

    * Datablocks like configuration can be stored in as JSON and be manipulated
      by database software then converted into C structs on compilation.
      
    * Since python isn't maintained as a dependency, all the libraries called
      here are standard libraries. It should run fine on any system that can
      build the software since it's now a standard part of operating systems.
      
      Windows users may need to install Python as a new step.

This will run before compilation, chained within the build scripts.
"""

import json

f = open("src/config.json", "r")
a = json.loads(f.read())
f.close()

f = open("src/config.json", "w")
f.write(json.dumps(a, indent=4))
f.close()

f = open("src/config.c", "w")
f.write("""/* This file is part of Embroidermodder 2.
 * ------------------------------------------------------------
 * Copyright 2021 The Embroidermodder Team
 * Embroidermodder 2 is Open Source Software.
 * See LICENSE.txt for licensing terms.
 * ------------------------------------------------------------
 * This file is only for data and declarations that
 * are compiled into the source.
 */

#include "embroidermodder.h"

#include "non_json_config.c"

""")

xpm_icons = sorted([k for k in a.keys() if k[-4:] == "_xpm"])

for k in xpm_icons:
    f.write("const char *%s[];\n" % k)

s = """

const char **icons[] = {
"""
    
for k in xpm_icons:
    s += "    %s,\n" % k

s += """
};

"""

# In order to use a global palette, we use a double reference via a["macro"].             
for k in a.keys():
    if a[k]["type"] == "xpm":
        s += "const char *%s[] = {\n" % (k)
        for i in a[k]["data"]:
            for m in a["macro"]["data"].keys():
                i = i.replace(m, a["macro"]["data"][m])
            s += "    \"%s\",\n" % i
        s += "};\n\n"
    elif a[k]["type"] == "string table":
        s += "const char *%s[] = {\n" % (k)
        for i in a[k]["data"]:
            s += "    \"%s\",\n" % i
        s += "};\n\n"
f.write(s)
f.close()

