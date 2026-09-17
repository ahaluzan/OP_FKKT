import unittest
from naloga3 import *


test_case = unittest.TestCase()
test_case.assertAlmostEqual(pretvori(123, 26, 4.5, 'W'), -123.43458333333334, 6)
