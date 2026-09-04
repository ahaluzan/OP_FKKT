import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

result = pH(0.0025)
expected = 2.6020599913279625
test_case.assertAlmostEqual(result, expected, places=5)