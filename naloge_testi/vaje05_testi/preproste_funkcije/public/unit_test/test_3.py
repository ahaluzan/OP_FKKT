import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

result = minimum([0])
expected = 0
test_case.assertEqual(result, expected)