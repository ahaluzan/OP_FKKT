import unittest
from reakcije import *

test_case = unittest.TestCase()
results = kemijski_sistem(0.02, 0.01)
expected = 1.9990071759108727

test_case.assertAlmostEqual(results, expected, places=3)