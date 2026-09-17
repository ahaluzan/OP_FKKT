import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_COVID

pop = {'Slovenia': 2078989, 'Monaco': 39290, 'Gibraltar': 33689}
actual = izpit.preberi_covid("covid1.csv", pop)
expected = case

for v, tv in zip(actual, expected):
    test_case.assertEqual(type(v[4]), type(tv[4]), "Vrednost v seznamu je napacnega tipa.")
