import unittest

from naloge import *

test_case = unittest.TestCase()
expected = 100.0
result = v_cm(10.0, -35)
test_case.assertAlmostEqual(expected, result, 5)
