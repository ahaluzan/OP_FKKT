import unittest
from naloge import *

test_case = unittest.TestCase()
expected = 'AAUUCC'
result = komplement("TTAAGG", RNA=True)
test_case.assertEqual(expected, result)
