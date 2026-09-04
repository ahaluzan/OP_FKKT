'''fibonaccijeva_stevila'''
import unittest
from fibonacci import *

test_case = unittest.TestCase()
test_case.assertEqual(fibonaccijeva_stevila(90), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
