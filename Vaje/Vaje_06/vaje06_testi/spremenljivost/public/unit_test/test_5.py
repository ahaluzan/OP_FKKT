import unittest
from spremenljivost import *

test_case = unittest.TestCase()
seznam = [400, -100, 256, -1089, 0]
seznam_original = seznam.copy()
result = koreni_seznam2(seznam) 
expected = [20.0, None, 16.0, None, 0.0]
test_case.assertEqual(expected, result)
test_case.assertEqual(seznam_original, seznam, msg='The original list must not be modified!')