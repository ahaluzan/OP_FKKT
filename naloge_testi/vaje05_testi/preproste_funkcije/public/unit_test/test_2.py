import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

result = minimum([5, 4, -7, 2, 12, -3, -4, 11, 2])
expected = -7
test_case.assertEqual(result, expected)