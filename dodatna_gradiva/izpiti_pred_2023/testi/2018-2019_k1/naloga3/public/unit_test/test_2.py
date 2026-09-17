import unittest
from naloga3 import *


test_case = unittest.TestCase()
test_case.assertAlmostEqual(pretvori(14, 28, 8, 'E'), 14.46888888888889, 4)
