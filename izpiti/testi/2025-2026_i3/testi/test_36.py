import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.po_spolu5['samo_f']

actual = naloge.po_spolu(variables.slovar_spol5)['samo_f']

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije pod kljucem 'samo_f'.")
