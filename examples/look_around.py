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

    def test_look_behind(self):
        pattern = re.compile(r'(?<=John\s)McLane')
        result = pattern.finditer("I would rather go out with John McLane than with John Smith or John Bon Jovi")

        i = result.next()
        self.assertEqual(32, i.start())
        self.assertEqual(38, i.end())

    def test_match_twitter_name(self):
        text = "Know your Big Data = 5 for $50 on eBooks and 40% off all eBooks until Friday #bigdata #hadoop @HadoopNews packtpub.com/bigdataoffers"

        pattern = re.compile(r'\B@[\w_]+')
        result = pattern.findall(text)
        self.assertEqual(['@HadoopNews'], result)

        pattern = re.compile(r'(?<=\B@)[\w_]+')
        result = pattern.findall(text)
        self.assertEqual(['HadoopNews'], result)

    def test_negative_look_behind(self):
        pattern = re.compile(r'(?<!John\s)Doe')
        result = pattern.finditer("John Doe, Calvin Doe, Hobbes Doe")

        iter = result.next()
        self.assertEqual(17, iter.start())
        self.assertEqual(20, iter.end())

        iter = result.next()
        self.assertEqual(29, iter.start())
        self.assertEqual(32, iter.end())

        # no more entries
        with self.assertRaises(StopIteration):
            iter = result.next()

    def test_look_around_and_groups(self):
        pattern = re.compile(r'\w+\s[\d-]+\s[\d:,]+\s(.*(?<!authentication\s)failed)')

        self.assertEqual([], pattern.findall("INFO 2013-09-17 12:13:44,487 authentication failed"))

        self.assertEqual(['something else failed'],
                         pattern.findall("INFO 2013-09-17 12:13:44,487 something else failed"))

# this is not possible (look-behind can match only fixed-width patterns)
# pattern = re.compile(r'?<=(John|Jonathan)\s)McLane')        

if __name__ == '__main__':
    unittest.main()   # pragma: no cover
