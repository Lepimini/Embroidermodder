#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENSE for licensing terms.

    ------------------------------------------------------------

"""

import json

def triage():
    r""" In order to get statistics on the errors (i.e. find the worst
    hostspots for errors) run the source through pylint and get the
    results as json data to be processed.
    """
    print("Triage")
    with open("triage.json", "r", encoding="utf-8") as file:
        string_data = file.read()
        json_data = json.loads(string_data)
        table = {}
        for i in json_data:
            if 'path' in i.keys():
                table[i['path']] = 0
        for i in json_data:
            if 'path' in i.keys():
                table[i['path']] += 1

        print("Warnings/errors per file.")
        for i in table.items():
            print(i, table[i])

if __name__ == "__main__":
    triage()
