'''kemijski_sistem_tri'''
import unittest
from reakcije import *

test_case = unittest.TestCase()
results = kemijski_sistem_tri(0.01, 0.01, 0.2, 0.01, 0.02, 0.004, 0.05, 2)
expected = (5.531399403417955, 3.37242345906273)

for i in range(len(expected)):
    test_case.assertAlmostEqual(results[i], expected[i], places=3)