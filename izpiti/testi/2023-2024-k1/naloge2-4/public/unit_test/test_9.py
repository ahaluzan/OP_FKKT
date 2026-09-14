import unittest
from naloge import *

test_case = unittest.TestCase()
expected = 'C'
result = naj_DNA([('AAA', 1), ('TTT', 9.98), ('C', 100)]) 
test_case.assertEqual(expected, result)
