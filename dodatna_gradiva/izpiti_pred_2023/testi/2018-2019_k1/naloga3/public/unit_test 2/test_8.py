import unittest
from naloga3 import *


test_case = unittest.TestCase()
test_case.assertAlmostEqual(razdalja([30.0, 172.0], [40.5, -175.0], 6371), 1656.786459278816, 1)