import unittest
from IMDb import *

test_case = unittest.TestCase()
serije = [
    ('The Big Bang Theory', 8.4, 2007),
    ('Mr. Robot', 8.7, 2015),
    ('Humans', 8.1, 2015),
    ('Orange Is the New Black', 8.3, 2013),
    ('Dexter', 8.8, 2006),
]
expected = 8.46
result = povprecna_ocena(serije)

test_case.assertAlmostEqual(expected, result, 2)