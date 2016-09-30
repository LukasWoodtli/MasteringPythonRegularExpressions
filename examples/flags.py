import unittest

import re
import locale

class CompilationFlagsTests(unittest.TestCase):
    def test_ignorecase(self):
        pattern = re.compile(r"[a-z]+", re.I)
        self.assertIsNotNone(pattern.search("Felix"))
        self.assertIsNotNone(pattern.search("felix"))

    def test_multiline(self):
        patternString = r"^\w+\: (\w+/\w+/\w+)"
        
        pattern = re.compile(patternString)
        self.assertEqual(['12/01/2013'],
                         pattern.findall("date: 12/01/2013\ndate: 11/01/2013"))

        pattern = re.compile(patternString, re.M)
        self.assertEqual(['12/01/2013', '11/01/2013'],
                         pattern.findall("date: 12/01/2013\ndate: 11/01/2013"))
        
    def test_dotall(self):
        self.assertEqual([], re.findall("^\d(.)", "1\ne")) # \d is equal [0-9]
        self.assertEqual(['\n'], re.findall("^\d(.)", "1\ne", re.S)) # re.S is re.DOTALL

    def test_locale(self):
        chars = ''.join(chr(i) for i in xrange(256))
        str = " ".join(re.findall(r"\w", chars))
        self.assertEqual("0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z _ a b c d e f g h i j k l m n o p q r s t u v w x y z",
                         str)

# This test only works if locale ru_RU.KOI8-R is available (it's not on travis-ci)
#        locale.setlocale(locale.LC_ALL, 'ru_RU.KOI8-R')
#        str = " ".join(re.findall(r"\w", chars, re.LOCALE))
#        expected = '0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z _ a b c d e f g h i j k l m n o p q r s t u v w x y z \xa3 \xb3 \xc0 \xc1 \xc2 \xc3 \xc4 \xc5 \xc6 \xc7 \xc8 \xc9 \xca \xcb \xcc \xcd \xce \xcf \xd0 \xd1 \xd2 \xd3 \xd4 \xd5 \xd6 \xd7 \xd8 \xd9 \xda \xdb \xdc \xdd \xde \xdf \xe0 \xe1 \xe2 \xe3 \xe4 \xe5 \xe6 \xe7 \xe8 \xe9 \xea \xeb \xec \xed \xee \xef \xf0 \xf1 \xf2 \xf3 \xf4 \xf5 \xf6 \xf7 \xf8 \xf9 \xfa \xfb \xfc \xfd \xfe \xff'
 #       self.assertEqual(expected, str)


if __name__ == '__main__':
    unittest.main()   # pragma: no cover

