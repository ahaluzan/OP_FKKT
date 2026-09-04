'''pH'''
import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

result = pH(0.0000001)
expected = 7
test_case.assertAlmostEqual(result, expected, places=5)