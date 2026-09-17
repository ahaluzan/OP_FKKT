import unittest
from naloga3 import *


test_case = unittest.TestCase()
test_case.assertAlmostEqual(razdalja([46.0, 15.0], [47.0, 15.0], 6371), 111.19492664455889, 2)