'''koreni_seznam2'''
import unittest
from spremenljivost import *

test_case = unittest.TestCase()
seznam = [0, 1, 4, 9, 16, 25]
seznam_original = seznam.copy()
result = koreni_seznam2(seznam) 
expected = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
test_case.assertEqual(expected, result)
test_case.assertEqual(seznam_original, seznam, msg='The original list must not be modified!')