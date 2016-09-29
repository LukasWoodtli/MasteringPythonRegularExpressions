import unittest

import re


class MatchObjectTests(unittest.TestCase):
    # A MatchObject is returned every time when following functions are called:
    # - match
    # - search
    # - finditer
    def test_group(self):
        pattern = re.compile(r"(\w+) (\w+)")
        match = pattern.search("Hello world")

        self.assertEqual("Hello world", match.group())

        self.assertEqual("Hello world", match.group(0))

        self.assertEqual("Hello", match.group(1))

        self.assertEqual("world", match.group(2))

        with self.assertRaises(IndexError):
             match.group(3)
            
        self.assertEqual(("Hello world", "world"), match.group(0, 2))


    def test_group_named(self):
        pattern = re.compile(r"(?P<first>\w+) (?P<second>\w+)")
        match = pattern.search("Hello world")

        self.assertEqual("Hello", match.group('first'))
        self.assertEqual("Hello", match.group(1))

        self.assertEqual(("Hello world", "Hello", "world"), match.group(0, 'first', 2))

    def test_groups(self):
        pattern = re.compile(r"(\w+) (\w+)")
        match = pattern.search("Hello world")

        self.assertEqual(("Hello", "world"), match.groups())

    def test_groups_not_matching(self):
        pattern = re.compile(r"(\w+) (\w+)?")
        match = pattern.search("Hello ")

        self.assertEqual(("Hello", "mundo"), match.groups("mundo"))
        self.assertEqual(("Hello", None), match.groups())

    def test_groupdict(self):
        pattern = re.compile(r"(?P<first>\w+) (?P<second>\w+)")
        result = pattern.search("Hello world")
        self.assertEqual({'first' : 'Hello', 'second' : 'world'},
                         result.groupdict())

    def test_start_end(self):
        pattern = re.compile(r"(?P<first>\w+) (?P<second>\w+)")
        result = pattern.search("Hello world")
        self.assertEqual({'first' : 'Hello', 'second' : 'world'},
                         result.groupdict())

    def test_start_end_span(self):
        pattern = re.compile(r"(?P<first>\w+) (?P<second>\w+)?")
        match = pattern.search("Hello ")
        self.assertEqual(0, match.start(1))
        self.assertEqual(-1, match.start(2))

        self.assertEqual(5, match.end(1))

        self.assertEqual((0, 5), match.span(1))


    def test_expand(self):
        text = "imagine a new *world*, a magic *world*"
        match = re.search(r"\*(.*?)\*", text)
        self.assertEqual('<b>world<\\b>', match.expand(r"<b>\g<1><\\b>"))

if __name__ == '__main__':
    unittest.main()   # pragma: no cover

