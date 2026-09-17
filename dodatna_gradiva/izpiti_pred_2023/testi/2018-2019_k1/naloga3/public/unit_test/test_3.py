import unittest
from naloga3 import *


test_case = unittest.TestCase()
test_case.assertAlmostEqual(pretvori(46, 3, 3, 'N'), 46.05083333333333, 6)
