import unittest
from IMDb import *

test_case = unittest.TestCase()
serije = [
    ('Mr. Robot', 8.7, 2015),
    ('Humans', 8.1, 2015),
    ('Dexter', 8.8, 2006),
]
expected = []
result = dolga_imena(serije)

test_case.assertEqual(expected, result)