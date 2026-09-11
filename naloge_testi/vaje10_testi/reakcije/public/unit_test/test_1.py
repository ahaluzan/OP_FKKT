'''kemijski_sistem'''
import unittest
from reakcije import *

test_case = unittest.TestCase()
results = kemijski_sistem(0.01, 0.01)
expected = 0.9990068522040796

test_case.assertAlmostEqual(results, expected, places=3)