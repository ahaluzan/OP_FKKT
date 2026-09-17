import unittest
from naloga2 import *

test_case = unittest.TestCase()
expected = False
result = povprecje_interval([-1, -1, -1, -1],1,4)
test_case.assertEqual(expected, result)