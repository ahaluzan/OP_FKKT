import unittest
from naloga3 import *

test_case = unittest.TestCase()
expected = '13.1.2020'
result = najhujsi_dan([("11.1.2020",0), ("12.1.2020", 0), ("13.1.2020", 1)])
test_case.assertEqual(expected, result)