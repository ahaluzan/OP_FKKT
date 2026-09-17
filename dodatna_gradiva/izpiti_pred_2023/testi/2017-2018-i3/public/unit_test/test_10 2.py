import unittest
from izpit import *

test_case = unittest.TestCase()
expected = 0
test_case.assertEqual(razlika_v_mesecih((2018, 8),(2018, 8)), expected)