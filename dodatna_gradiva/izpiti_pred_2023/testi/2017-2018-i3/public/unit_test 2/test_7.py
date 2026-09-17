import unittest
from izpit import *

test_case = unittest.TestCase()
expected = 20
test_case.assertEqual(razlika_v_mesecih((-215, 9), (-213, 5)), expected)