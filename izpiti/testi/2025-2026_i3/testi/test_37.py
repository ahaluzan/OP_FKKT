import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.po_spolu5

actual = naloge.po_spolu(variables.slovar_spol5)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")
