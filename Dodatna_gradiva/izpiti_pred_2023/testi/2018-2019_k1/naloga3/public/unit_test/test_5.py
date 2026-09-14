import unittest
from naloga3 import *


test_case = unittest.TestCase()
test_case.assertAlmostEqual(pretvori(37, 57, 25, 'S'), -37.956944444444446, 6)
