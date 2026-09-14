import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.po_spolu10

actual = naloge.po_spolu(variables.slovar_spol10)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")
