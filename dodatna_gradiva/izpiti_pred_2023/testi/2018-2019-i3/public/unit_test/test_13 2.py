import unittest

from .TEST_DATA import *
import izpit

test_case = unittest.TestCase()

actual = izpit.drseca_bruto_placa(READS[1])
expected = DRSECE_POVPRECJE[1]

for act, exp in zip(actual, expected):
    test_case.assertIsInstance(act, tuple, "Posamezen zapis mora biti terka")
    test_case.assertIsInstance(act[0], tuple, "Datum mora biti terka")
    test_case.assertEqual(len(act[0]), len(exp[0]), "Datum mora biti terka 2 komponent")
    test_case.assertEqual(act[0], exp[0], "Datuma se ne ujemata")
    test_case.assertIsInstance(act[1], float, "Povprecna bruta placa mora biti decimalno stevilo")
