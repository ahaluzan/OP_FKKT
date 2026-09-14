import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = ['skupno', 'samo_m', 'samo_f']

actual = list(naloge.po_spolu(variables.slovar_spol5).keys())

test_case.assertCountEqual(expected, actual, "Napacni kljuci v slovarju.")
