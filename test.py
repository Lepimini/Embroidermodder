#!/usr/bin/env python3

import unittest
import embroidermodder

class TestExample(unittest.TestCase):

    def test_translate(self):
        translated = embroidermodder.translate("?")
        self.assertEqual(translated, "?")

if __name__ == '__main__':
    unittest.main()
