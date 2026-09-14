"po_spolih"
import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = {'Sweater'}

actual = naloge.po_spolih(variables.shop10)

test_case.assertEqual(type(expected), type(actual), "Funkcija vraca napacen podatkovni tip.")