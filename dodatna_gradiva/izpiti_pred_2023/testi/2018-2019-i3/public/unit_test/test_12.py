import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.drseca_bruto_placa(READS[1])
expected = DRSECE_POVPRECJE[1]

for act, exp in zip(actual, expected):
    test_case.assertEqual(len(act), len(exp), "Posamezen zapis ima napačno število komponent")
