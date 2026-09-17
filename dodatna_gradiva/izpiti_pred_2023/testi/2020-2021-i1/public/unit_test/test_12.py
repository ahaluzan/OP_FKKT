import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DATA

podatki1 = [('USA', 'Americas', 22645757, 377446, 331341050),  
('Slovenia', 'Europe', 141587, 3171, 2078989),  ('Gibraltar', 'Europe', 3240, 16, 33689),  
('Monaco', 'Europe', 1092, 7, 39290)]

actual = izpit.primerov_na_regijo(podatki1)
#expected = case

for k, v in actual.items():
    test_case.assertIsInstance(k, str, "Napacen tip kljuca")
    test_case.assertIsInstance(v, float, "Napacen tip vrednosti")
