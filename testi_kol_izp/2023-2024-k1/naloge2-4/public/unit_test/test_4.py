'''kvaliteta'''
import unittest
from naloge import *

test_case = unittest.TestCase()
expected = [('AAA', 4.97), ('TTT', 9.98), ('C', 4.23)]
result = kvaliteta(["AAA", "TTT", "C"],  [10, 15, 5], [50.325235, 33.444, 15.4])
test_case.assertEqual(expected, result)
