'''naj_DNA'''
import unittest
from naloge import *

test_case = unittest.TestCase()
expected = 'TTT'
result = naj_DNA([('AAA', 4.97), ('TTT', 9.98), ('C', 4.23)]) 
test_case.assertEqual(expected, result)
