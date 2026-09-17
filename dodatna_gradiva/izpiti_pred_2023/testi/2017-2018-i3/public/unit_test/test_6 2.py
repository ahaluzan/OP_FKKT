'''razlika_v_mesecih'''
import unittest
from izpit import *

test_case = unittest.TestCase()
expected = 3
test_case.assertEqual(razlika_v_mesecih((2018, 5), (2018, 8)), expected)

