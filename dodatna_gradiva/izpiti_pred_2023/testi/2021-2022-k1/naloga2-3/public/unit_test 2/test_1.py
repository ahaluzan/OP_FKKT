'''v_cm'''
import unittest

from naloge import *

test_case = unittest.TestCase()
expected = 10.0
result = v_cm(10.0, 0.3)
test_case.assertAlmostEqual(expected, result, 5)
