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

        # string doesn't start at position given by *pos*
        pattern = re.compile(r'^<HTML>')

        self.assertIsNone(pattern.match("  <HTML>", 2))
        # slicing gives back a new string starting at expected pos
        self.assertIsNotNone(pattern.match("  <HTML>"[2:]))

    def test_match_and_search_with_endpos(self):
        pattern = re.compile(r'<HTML>')

        self.assertIsNone(pattern.match("<HTML>"[:2]))

        self.assertIsNone(pattern.match("<HTML>", 0, 2))

        # slicing and endpos have the same effect!
        pattern = re.compile(r'<HTML>$')
        self.assertIsNotNone(pattern.match("<HTML> ", 0, 6))
        self.assertIsNotNone(pattern.match("<HTML> "[:6]))        

        pattern = re.compile(r'^<HTML>')
        self.assertIsNotNone(pattern.match("<HTML>"))
        
        self.assertIsNone(pattern.match("  <HTML>", 2))
        
    def test_search(self):
        pattern = re.compile(r'world')
        
        self.assertIsNotNone(pattern.search("Hello world"))
        
        self.assertIsNone(pattern.search("hola mundo"))

    def test_search_multiline(self):
        pattern = re.compile(r'^<HTML>', re.MULTILINE)

        self.assertIsNotNone(pattern.search("<HTML>"))
        self.assertIsNone(pattern.search(" <HTML>"))
        self.assertIsNotNone(pattern.search("  \n<HTML>"))

        # with pos
        self.assertIsNotNone(pattern.search("  \n<HTML>", 3))
        self.assertIsNotNone(pattern.search("</DIV></BODY>\n<HTML>", 4))
        self.assertIsNone(pattern.search("\n<HTML>", 4))

    def test_findall(self):
        pattern = re.compile(r"\w+")
        
        self.assertEqual(["hello", "world"], pattern.findall("hello world"))
        
        
        pattern = re.compile(r"a*")
        self.assertEqual(["a","","a",""], pattern.findall("aba"))
        
        pattern = re.compile(r"a?")
        self.assertEqual(["a","","a",""], pattern.findall("aba"))
    
    def test_findall_groups(self):
        pattern = re.compile(r"(\w+) (\w+)")

        self.assertEqual([('Hello', 'world'), ('hola', 'mundo')],
                    pattern.findall("Hello world hola mundo"))
    

    def test_finditer(self):
        pattern = re.compile(r"(\w+) (\w+)")
        it = pattern.finditer("Hello world hola mundo")

        match = it.next()
        self.assertEqual(('Hello', 'world'), match.groups())
        self.assertEqual((0, 11), match.span())

        match = it.next()
        self.assertEqual(('hola', 'mundo'), match.groups())
        self.assertEqual((12, 22), match.span())

        with self.assertRaises(StopIteration):
            match = it.next()


if __name__ == '__main__':
    unittest.main()   # pragma: no cover
