import unittest
from izpit import *

test_case = unittest.TestCase()
expected = 24
test_case.assertEqual(razlika_v_mesecih((-1, 12),(1,12)), expected)