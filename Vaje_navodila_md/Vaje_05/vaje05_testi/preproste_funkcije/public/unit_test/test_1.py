'''minimum'''
import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

result = minimum([23, 42, 87, 34, 1, -3, 2])
expected = -3
test_case.assertEqual(result, expected)