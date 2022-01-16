#!/usr/bin/env python3

r"""

This file is part of Embroidermodder 2.

------------------------------------------------------------

    Copyright 2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENSE.txt for licensing terms.

------------------------------------------------------------

This file is only for metaprogramming:

    * Code style maintenence: if you do something that the
      compiler considers correct but we try not to as part
      of the house style this'll correct it.

    * Datablocks like configuration can be stored in as
      JSON and be manipulated by database software then
      converted into C structs on compilation.

    * Enums that are maintained with defines can be corrected
      here, so say you have
      
      ```
      /* enum: sequential 30 */
      #define CONSTANT_a   3
      #define CONSTANT_c     5
      #define CONSTANT_f   2
      /* end enum */
      ```
      
      is processed to:
      
      ```
      /* enum: sequential 30 */
      #define CONSTANT_a          0
      #define CONSTANT_c          1
      #define CONSTANT_f          2
      /* end enum */
      ```
      
      the comments instruct this script to do the job.
      
      Note: we don't do enums, because of the amount of
      switch statements used in the source.
      
    * Since python isn't maintained as a dependency, all the
      libraries called here are standard libraries. It should
      run fine on any system that can build the software since
      it's now a standard part of operating systems.
      
      Windows users may need to install Python as a new step.

This will run before compilation, chained within the build
scripts.

"""

import os
import json

def process_json(s):
    r"""
    The jobs carried out by this processor are:
    
        * convert C struct data stored as JSON to C code
    """
    return s


def process_c_code(s):
    r"""
    The jobs carried out by this processor are:
    
        * check indentation is always a multiple of 4
    """
    return s

    
def process_cplusplus_code(s):
    r"""
    The jobs carried out by this processor are:
    
        * check indentation is always a multiple of 4
    """
    return s


def process_header(s):
    r"""
    The jobs carried out by this processor are:
    
        * correct define blocks
        * report the number of functions that are within
          classes: to aid the de-object orientation process
    """
    return s


for fname in os.listdir("src"):
    # configuration to code
    if fname[-4:] == ".json":
        f = open("src/"+fname, "r")
        s = f.read()
        f.close()
        s = process_json(s)
        f = open("src/"+fname[:-4]+".c", "w")
        f.write(s)
        f.close()
        continue

    # in place editing
    s = ""
    with open("src/"+fname, "r") as f:
        s = f.read()
    if fname[-2:] == ".c":
        s = process_c_code(s)
    if fname[-2:] == ".h":
        s = process_header(s)
    if fname[-4:] == ".cpp":
        s = process_cplusplus_code(s)
    with open("src/"+fname, "w") as f:
        f.write(s)


