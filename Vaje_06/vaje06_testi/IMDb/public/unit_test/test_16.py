import unittest
from IMDb import *

test_case = unittest.TestCase()
serije = []
expected = []
result = najnovejse(serije)

test_case.assertEqual(expected, result)