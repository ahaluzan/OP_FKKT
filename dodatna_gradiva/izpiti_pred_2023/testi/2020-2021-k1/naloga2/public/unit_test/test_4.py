import unittest
from naloga2 import *

test_case = unittest.TestCase()
expected = 0.0
data = [0, 0, 0, 0]
result = povprecje(data)
test_case.assertAlmostEqual(expected, result, 5)