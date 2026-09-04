import unittest
from IMDb import *

test_case = unittest.TestCase()
serije = []
expected = []
result = ocene(serije)

test_case.assertEqual(expected, result)