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


        result = iter.next()
        self.assertEqual(27, result.start())
        self.assertEqual(31, result.end())

        result = iter.next()
        self.assertEqual(63, result.start())
        self.assertEqual(67, result.end())

    def test_substitution(self):
        pattern = re.compile(r'\d{1,3}')
        self.assertEqual(['123', '455', '678', '90'],
                         pattern.findall("The number is: 12345567890"))

        pattern = re.compile(r'\d{1,3}(?=(\d{3})+(?!\d))')
        iter = pattern.finditer('1234567890')

        result = iter.next()
        self.assertEqual(0, result.start())
        self.assertEqual(1, result.end())

        result = iter.next()
        self.assertEqual(1, result.start())
        self.assertEqual(4, result.end())

        result = iter.next()
        self.assertEqual(4, result.start())
        self.assertEqual(7, result.end())

        self.assertEqual('1,234,567,890', pattern.sub(r'\g<0>,', "1234567890"))

if __name__ == '__main__':
    unittest.main()   # pragma: no cover
