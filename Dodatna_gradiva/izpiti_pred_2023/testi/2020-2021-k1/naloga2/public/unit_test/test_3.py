import unittest
from naloga2 import *

test_case = unittest.TestCase()
expected = False
data = [-1, -1, -1]
result = povprecje(data)
test_case.assertEqual(expected, result)


