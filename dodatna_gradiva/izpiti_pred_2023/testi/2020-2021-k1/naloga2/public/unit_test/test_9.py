import unittest
from naloga2 import *

test_case = unittest.TestCase()
expected = False
result = povprecje_interval([3, 5, -1, -1, 7],3,4)
test_case.assertEqual(expected, result)