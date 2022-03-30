#!/usr/bin/env python3

import unittest
from embroidermodder import *

class TestExample(unittest.TestCase):

    def test_translate(self):
        translated = translate("?")
        self.assertEqual(translated, "?")

    def test_doNothing(self):
        " Crash test do nothing function. "
        doNothing()

    def test_newFile(self):
        " Crash test new file call. "
        newFile()

    def test_openFile(self):
        " Crash test open file call. "
        openFile()

    def test_saveFile(self):
        " Crash test save file call. "
        saveFile()

    def test_saveAsFile(self):
        " Crash test save as file call. "
        saveAsFile()

    def test_cutObject(self):
        " Crash test cut object call. "
        cutObject()

    def test_copyObject(self):
        " Crash test copy object call. "
        copyObject()

    def test_pasteObject(self):
        " Crash test paste object call. "
        pasteObject()

    def test_icon16(self):
        " Crash test set icon size to 16 call. "
        icon16()

    def test_icon24(self):
        " Crash test set icon size to 24 call. "
        icon24()

    def test_icon32(self):
        " Crash test set icon size to 32 call. "
        icon32()

    def test_icon48(self):
        " Crash test set icon size to 48 call. "
        icon48()

    def test_icon64(self):
        " Crash test set icon size to 64 call. "
        icon64()

    def test_icon128(self):
        " Crash test set icon size to 128 call. "
        icon128()


if __name__ == '__main__':
    unittest.main()
