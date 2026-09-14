import unittest
from naloga3 import *


test_case = unittest.TestCase()
test_case.assertAlmostEqual(razdalja([7.38, -132.0], [7.39, -132.01], 6371), 1.5660251102158975, 2)