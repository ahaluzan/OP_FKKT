'''kemijski_sistem_dva'''
import unittest
from reakcije import *

test_case = unittest.TestCase()
results = kemijski_sistem_dva(0.01, 0.01, 0.2, 0.01, 0.02, 0.004)
expected = (12.646067803591196, 8.352742972482933)

for i in range(len(expected)):
    test_case.assertAlmostEqual(results[i], expected[i], places=3)