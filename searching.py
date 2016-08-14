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


if __name__ == '__main__':
    unittest.main()   # pragma: no cover
