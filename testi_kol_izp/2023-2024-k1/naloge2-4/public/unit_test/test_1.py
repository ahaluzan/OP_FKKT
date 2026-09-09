'''komplement'''
import unittest
from naloge import *

test_case = unittest.TestCase()
expected = 'AATTCCGG'
result = komplement('TTAAGGCC')
test_case.assertEqual(expected, result)
