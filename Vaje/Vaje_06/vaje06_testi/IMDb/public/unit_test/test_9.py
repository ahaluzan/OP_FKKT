import unittest
from IMDb import *

test_case = unittest.TestCase()
serije = []
expected = 0
result = povprecna_ocena(serije)

test_case.assertAlmostEqual(expected, result, 2)