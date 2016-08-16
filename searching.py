import unittest

import re


class SearchingTests(unittest.TestCase):

    def test_match_and_search(self):
        pattern = re.compile(r'<HTML>')

        self.assertIsNotNone(pattern.match("<HTML><HEAD>"))

        self.assertIsNone(pattern.match(" <HTML>"))

        self.assertIsNotNone(pattern.search(" <HTML>"))

    def test_match_and_search_with_pos(self):
        pattern = re.compile(r'<HTML>')

        self.assertIsNone(pattern.match("  <HTML>"))

        self.assertIsNotNone(pattern.match("  <HTML>", 2))

        # string doesn't start at position given by *pos*
        pattern = re.compile(r'^<HTML>')

        self.assertIsNone(pattern.match("  <HTML>", 2))
        # slicing gives back a new string starting at expected pos
        self.assertIsNotNone(pattern.match("  <HTML>"[2:]))

    def test_match_and_search_with_endpos(self):
        pattern = re.compile(r'<HTML>')

        self.assertIsNone(pattern.match("<HTML>"[:2]))

        self.assertIsNone(pattern.match("<HTML>", 0, 2))

        # slicing and endpos have the same effect!
        pattern = re.compile(r'<HTML>$')
        self.assertIsNotNone(pattern.match("<HTML> ", 0, 6))
        self.assertIsNotNone(pattern.match("<HTML> "[:6]))        

        pattern = re.compile(r'^<HTML>')
        self.assertIsNotNone(pattern.match("<HTML>"))
        
        self.assertIsNone(pattern.match("  <HTML>", 2))
        
if __name__ == '__main__':
    unittest.main()   # pragma: no cover
