# coding=utf-8

import unittest

import re


class GroupingTests(unittest.TestCase):
    def test_group(self):
        self.assertIsNotNone(re.match(r"(\d-\w){2,3}", ur"1-a2-b"))

        self.assertIsNotNone(re.search(r"(ab)+c", ur"ababc"))
        self.assertIsNone(re.search(r"(ab)+c", ur"abbc"))

    def test_spain(self):
        self.assertIsNotNone(re.search(r"Espana|ol", "Espanol"))
        self.assertIsNotNone(re.search(r"Espana|ol", "Espana"))
        self.assertIsNotNone(re.search(r"Espana|ol", "ol")) # not as intended

        # cheracter classes
        self.assertIsNotNone(re.search(r"Espan[aol]", "Espanol"))
        self.assertIsNotNone(re.search(r"Espan[aol]", "Espana"))
        self.assertIsNotNone(re.search(r"Espan[aol]", "Espano")) # not as intended
        self.assertIsNotNone(re.search(r"Espan[aol]", "Espanl")) # not as intended
        self.assertIsNotNone(re.search(r"Espan[a|ol]", "Espanol"))
        self.assertIsNotNone(re.search(r"Espan[a|ol]", "Espana"))
        self.assertIsNotNone(re.search(r"Espan[a|ol]", "Espano")) # not as intended
        self.assertIsNotNone(re.search(r"Espan[a|ol]", "Espanl")) # not as intended

    def test_spain_grouping(self):
        self.assertIsNotNone(re.search(r"Espan(a|ol)", "Espana"))
        self.assertIsNotNone(re.search(r"Espan(a|ol)", "Espanol"))

        self.assertIsNone(re.search(r"Espan(a|ol)", "Espan"))
        self.assertIsNone(re.search(r"Espan(a|ol)", "Espano"))
        self.assertIsNone(re.search(r"Espan(a|ol)", "ol"))

    def test_capturing(self):
        pattern = re.compile(r"(\d+)-\w+")
        it = pattern.finditer(r"1-a\n20-baer\n34-afcr")

        match = it.next()
        self.assertEqual('1', match.group(1))

        match = it.next()
        self.assertEqual('20', match.group(1))

        match = it.next()
        self.assertEqual('34', match.group(1))


    def test_backreferences_1(self):
        pattern = re.compile(r"(\w+) \1")
        match = pattern.search(r"hello hello world")
        self.assertEqual(('hello',), match.groups())

    def test_backreferences_2(self):
        pattern = re.compile(r"(\d+)-(\w+)")
        self.assertEqual("a-1\nbear-20\nafcr-34",
                         pattern.sub(r"\2-\1", "1-a\n20-bear\n34-afcr"))

    def test_named_groups(self):
        pattern = re.compile(r"(?P<first>\w+) (?P<second>\w+)")
        match = pattern.search("Hello world")
        self.assertEqual("Hello", match.group("first"))
        self.assertEqual("world", match.group("second"))

    def test_named_backreference(self):
        pattern = re.compile(r"(?P<country>\d+)-(?P<id>\w+)")
        result = pattern.sub(r"\g<id>-\g<country>", "1-a\n20-baer\n34-afcr")
        self.assertEqual("a-1\nbaer-20\nafcr-34", result)

    def test_named_group_in_pattern(self):
        pattern = re.compile(r"(?P<word>\w+) (?P=word)")
        match = pattern.search(r"hello hello world")
        self.assertEqual(('hello',), match.groups())

    def test_non_capturing_groups(self):
        # capturing
        self.assertIsNotNone(re.search("Espan(a|ol)", "Espanol"))
        self.assertEqual(('ol',), re.search("Espan(a|ol)", "Espanol").groups())

        # non-capturing
        self.assertIsNotNone(re.search("Espan(?:a|ol)", "Espanol"))
        self.assertEqual((), re.search("Espan(?:a|ol)", "Espanol").groups())

    def test_flags_for_groups(self):
        self.assertEqual([u'\xf1'], re.findall(r"(?u)\w+", ur"ñ"))

    def test_yes_pattern_no_pattern(self):
        pattern = re.compile(r"(\d\d-)?(\w{3,4})(?(1)(-\d\d))")
        self.assertIsNotNone(pattern.match("34-erte-22"))
        self.assertIsNotNone(pattern.match("erte"))
        self.assertIsNone(pattern.match("34-erte"))

        # with no-pattern
        pattern = re.compile(r"(\d\d-)?(\w{3,4})-(?(1)(\d\d)|[a-z]{3,4})$")
        self.assertIsNotNone(pattern.match("34-erte-22"))
        self.assertIsNone(pattern.match("34-erte"))
        self.assertIsNotNone(pattern.match("erte-abcd"))

    def test_overlapping_groups(self):
        self.assertEqual(['a','a'], re.findall(r'(a|b)+', 'abaca'))
        self.assertEqual(['abba','a'], re.findall(r'(?:a|b)+', 'abbaca'))


if __name__ == '__main__':
    unittest.main()   # pragma: no cover
