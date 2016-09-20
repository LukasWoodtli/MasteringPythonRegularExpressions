import unittest

import re


class ModifyingTests(unittest.TestCase):

    def test_split(self):
        result = re.split(r'\n', 'Beautiful is better than ugly.\nExplicit is better than implicit')
        self.assertEqual(['Beautiful is better than ugly.','Explicit is better than implicit'], result)

    def test_split_regex(self):
        pattern = re.compile(r"\W")
        self.assertEqual(['Hello', 'world'], pattern.split("Hello world"))

        self.assertEqual([' '], pattern.findall("Hello world"))

    def test_split_regex_maxsplit(self):
        pattern = re.compile(r"\W")

        result = pattern.split('Beautiful is better than ugly', 2)
        self.assertEqual(['Beautiful', 'is', 'better than ugly'], result)

    def test_split_regex_groups(self):
        pattern = re.compile(r"(-)")
        self.assertEqual(['hello', '-', 'world'], pattern.split("hello-world"))

    def test_split_regex_match_beginning(self):
        pattern = re.compile(r"(\W)")
        result = pattern.split(" hello world")
        self.assertEqual(['', ' ', 'hello', ' ', 'world'], result)

    def test_sub(self):
        pattern = re.compile(r"[0-9]+")

        self.assertEqual('order- order- order-',
                         pattern.sub('-', 'order0 order1 order13'))

    def test_sub_leftmost(self):
        self.assertEqual('order--0', re.sub('00', '-', 'order--0'))

    def test_sub_with_match_obj(self):
        def normalize_orders(matchobj):
            if matchobj.group(1) == '-':
                return "A"
            else:
                return "B"
        self.assertEqual('A1234 B193 B123',
                         re.sub('([-|A-Z])', normalize_orders, '-1234 A193 B123'))

    def test_sub_with_back_ref(self):
        text = "imagine a new *world*, a magic *world*"
        pattern = re.compile(r'\*(.*?)\*')
        self.assertEqual("imagine a new <b>world<\\b>, a magic <b>world<\\b>",
                         pattern.sub(r"<b>\g<1><\\b>", text))

if __name__ == '__main__':
    unittest.main()   # pragma: no cover
