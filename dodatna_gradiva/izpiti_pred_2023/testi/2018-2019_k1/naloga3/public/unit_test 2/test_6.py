'''razdalja'''
import unittest
from naloga3 import *


test_case = unittest.TestCase()
test_case.assertAlmostEqual(razdalja([46.0, 15.0], [46.0, 14.0], 6371), 77.24197923618823, 2)
