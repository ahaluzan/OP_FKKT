import unittest

from naloge import *

test_case = unittest.TestCase()
expected = 25.9
result = v_cm(10.0, -5.3)
test_case.assertAlmostEqual(expected, result, 5)
