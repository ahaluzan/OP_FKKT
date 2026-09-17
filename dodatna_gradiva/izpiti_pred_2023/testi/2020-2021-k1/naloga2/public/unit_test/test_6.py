'''povprecje_interval'''
import unittest
from naloga2 import *

test_case = unittest.TestCase()
expected = 5.0
result = povprecje_interval([3, 5, -1, -1, 7],1,5)
test_case.assertAlmostEqual(expected, result, 5)