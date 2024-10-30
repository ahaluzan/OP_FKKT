import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

result = minimum([3, 2, 2, 8])
expected = 2
test_case.assertEqual(result, expected)