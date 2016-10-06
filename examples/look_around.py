import unittest

import re


class LookAroundTests(unittest.TestCase):
    def test_look_ahead(self):
        # 'normal' pattern
        pattern = re.compile(r"fox")
        result = pattern.search("The quick brown fox jumps over the lazy dog")
        self.assertEqual(16, result.start())
        self.assertEqual(19, result.end())

        # look ahead
        pattern = re.compile(r"(?=fox)")
        result = pattern.search("The quick brown fox jumps over the lazy dog")
        self.assertEqual(16, result.start())
        self.assertEqual(16, result.end())

    def test_match_comma(self):
        pattern = re.compile(r'\w+(?=,)')
        result = pattern.findall("They were three: Felix, Victor, and Carlos.")
        self.assertEqual(['Felix', 'Victor'], result)

        # without look ahead
        pattern = re.compile(r'\w+,')
        result = pattern.findall("They were three: Felix, Victor, and Carlos.")
        self.assertEqual(['Felix,', 'Victor,'], result)

    def test_alternation(self):
        pattern = re.compile(r'\w+(?=,|\.)')
        result = pattern.findall("They were three: Felix, Victor, and Carlos.")
        self.assertEqual(['Felix', 'Victor', 'Carlos'], result)

    def test_negative_look_ahead(self):
        pattern = re.compile(r'John(?!\sSmith)')
        iter = pattern.finditer("I would rather go out with John McLane than with John Smith or John Bon Jovi")

        self.assertEqual(2, iter.size())

        result = iter.next()
        self.assertEqual(27, result.start())
        self.assertEqual(31, result.end())

        result = iter.next()
        self.assertEqual(63, result.start())
        self.assertEqual(67, result.end())


if __name__ == '__main__':
    unittest.main()   # pragma: no cover
