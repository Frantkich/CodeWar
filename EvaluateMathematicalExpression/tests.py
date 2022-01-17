import unittest
from solution import calc

class Test(unittest.TestCase):
    def test_codewar(self):
        cases = (
            ("1 + 1", 2),
            ("8/16", 0.5),
            ("3 -(-1)", 4),
            ("2 + -2", 0),
            ("10- 2- -5", 13),
            ("(((10)))", 10),
            ("3 * 5", 15),
            ("-7 * -(6 / 3)", 14)
        )
        for x, y in cases:
            self.assertEqual(calc(x), y)
