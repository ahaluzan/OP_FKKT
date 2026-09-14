import unittest
from naloge import *

test_case = unittest.TestCase()
expected = [('AAA', 1.0)]
result = kvaliteta(["AAA"], [1], [0]) 
test_case.assertEqual(expected, result)
