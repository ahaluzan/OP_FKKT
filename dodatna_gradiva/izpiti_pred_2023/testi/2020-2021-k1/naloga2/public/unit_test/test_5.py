import unittest
from naloga2 import *

test_case = unittest.TestCase()
expected = 328.57142857142856
data = [100, 1000, 1000, 100, 0, 0, -1, 100]
result = povprecje(data)
test_case.assertAlmostEqual(expected, result, 5)