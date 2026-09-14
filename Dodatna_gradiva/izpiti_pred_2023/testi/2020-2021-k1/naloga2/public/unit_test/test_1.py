'''povprecje'''
import unittest
from naloga2 import *

test_case = unittest.TestCase()
expected = 5.0
data = [3, 5, -1, -1, 7]
result = povprecje(data)
test_case.assertAlmostEqual(expected, result, 5)
