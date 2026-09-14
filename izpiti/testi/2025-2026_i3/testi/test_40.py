import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.po_spolu_samo_m

actual = naloge.po_spolu(variables.slovar_spol_samo_m)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije, kadar v vhodnem slovarju manjka kljuc za enega izmed spolov.")