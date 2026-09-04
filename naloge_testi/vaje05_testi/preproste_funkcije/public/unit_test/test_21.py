import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

result = pH(0.000000000046)
expected = 10.337242168318426
test_case.assertAlmostEqual(result, expected, places=5)