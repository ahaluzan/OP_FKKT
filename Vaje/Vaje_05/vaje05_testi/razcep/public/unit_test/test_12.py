import unittest
from razcep import *

test_case = unittest.TestCase()
test_case.assertEqual(razcep_na_prafaktorje(10948), [[2, 2], [7, 1], [17, 1], [23, 1]])