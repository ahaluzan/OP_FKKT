import unittest
from spremenljivost import *

test_case = unittest.TestCase()
seznam = []
seznam_original = seznam.copy()
result = koreni_seznam2(seznam) 
expected = []
test_case.assertEqual(expected, result)
test_case.assertEqual(seznam_original, seznam, msg='The original list must not be modified!')