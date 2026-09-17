'''drseca_bruto_placa'''
import unittest

from .TEST_DATA import *
import izpit

test_case = unittest.TestCase()

actual = izpit.drseca_bruto_placa(READS[1])
expected = DRSECE_POVPRECJE[1]

test_case.assertEqual(len(actual), len(expected), "Rezultat vsebuje napacno stevilo podatkov.")
