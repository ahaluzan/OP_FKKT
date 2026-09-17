import unittest
from naloga3 import *


test_case = unittest.TestCase()
test_case.assertAlmostEqual(razdalja([-64.7, -143.9], [-53.0, -112.0], 6371), 2211.062878945414, 1)