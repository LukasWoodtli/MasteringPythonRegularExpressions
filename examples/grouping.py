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


if __name__ == '__main__':
    unittest.main()   # pragma: no cover
