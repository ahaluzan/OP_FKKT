'''najnovejse'''
import unittest
from IMDb import *

test_case = unittest.TestCase()
serije = [
    ('Friends', 9.0, 1994),
    ('Mr. Robot', 8.7, 2015),
    ('The Big Bang Theory', 8.4, 2007),
    ('Humans', 8.1, 2015),
    ('Game of Thrones', 9.5, 2011),
]
expected = ['Mr. Robot', 'Humans']
result = najnovejse(serije)

test_case.assertEqual(expected, result)