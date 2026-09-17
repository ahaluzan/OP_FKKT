import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_REGION1

podatki1 = [('USA', 'Americas', 22645757, 377446, 331341050),  
('Slovenia', 'Europe', 141587, 3171, 2078989),  ('Gibraltar', 'Europe', 3240, 16, 33689),  
('Monaco', 'Europe', 1092, 7, 39290)]

actual = izpit.primerov_na_regijo(podatki1)
expected = case

test_case.assertEquals(actual, expected)
