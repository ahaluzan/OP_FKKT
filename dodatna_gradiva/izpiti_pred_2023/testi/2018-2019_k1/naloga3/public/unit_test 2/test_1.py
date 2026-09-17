'''pretvori'''
import unittest
from naloga3 import *


test_case = unittest.TestCase()
test_case.assertAlmostEqual(pretvori(14, 30, 0, 'E'), 14.5)
