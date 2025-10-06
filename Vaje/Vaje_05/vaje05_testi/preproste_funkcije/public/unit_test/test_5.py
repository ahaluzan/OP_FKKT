import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

result = minimum([2, 3, 42, 1])
expected = 1
test_case.assertEqual(result, expected)