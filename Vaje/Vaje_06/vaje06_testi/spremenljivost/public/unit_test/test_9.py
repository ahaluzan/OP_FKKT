import unittest
from spremenljivost import *

test_case = unittest.TestCase()
seznam = [8, 2, 12, 4, -5]
seznam_original = seznam.copy()
result = unikaten_seznam(seznam)
expected = [8, 2, 12, 4, -5]
test_case.assertEqual(expected, result)
test_case.assertEqual(seznam_original, seznam, msg='The original list must not be modified!')