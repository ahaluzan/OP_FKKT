'''csv'''
import unittest
from filmi import *

test_case = unittest.TestCase()
expected = 3.1573920265780733
test_case.assertAlmostEqual(ocena_filma(3, 'podatki/ratings.csv'),  expected, 4)