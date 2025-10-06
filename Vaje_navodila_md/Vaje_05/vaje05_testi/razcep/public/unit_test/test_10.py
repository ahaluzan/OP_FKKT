'''razcep_na_prafaktorje'''
import unittest
from razcep import *

test_case = unittest.TestCase()
test_case.assertEqual(razcep_na_prafaktorje(252), [[2, 2], [3, 2], [7, 1]])
