import unittest
from IMDb import *

test_case = unittest.TestCase()
serije = [
    ('Mr. Robot', 8.7, 2015),
    ('The Big Bang Theory', 8.4, 2007),
    ('Humans', 8.1, 2015),
    ('Orange Is the New Black', 8.3, 2013),
]
expected = []
result = ocene(serije)

test_case.assertEqual(expected, result)