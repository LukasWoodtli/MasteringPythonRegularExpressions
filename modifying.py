import unittest

import re


class ModifyingTests(unittest.TestCase):

    def test_split(self):
        result = re.split(r'\n', 'Beautiful is better than ugly.\nExplicit is better than implicit')
        self.assertEqual(['Beautiful is better than ugly.','Explicit is better than implicit'], result)


if __name__ == '__main__':
    unittest.main()   # pragma: no cover
