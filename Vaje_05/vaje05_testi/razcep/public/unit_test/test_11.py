import unittest
from razcep import *

test_case = unittest.TestCase()
test_case.assertEqual(razcep_na_prafaktorje(1944), [[2, 3], [3, 5]])