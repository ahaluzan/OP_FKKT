"4. naloga"
import unittest
import naloge
import variables

test_case = unittest.TestCase()

actual = naloge.po_spolu(variables.slovar_spol5)

test_case.assertIsInstance(actual, dict, "Funkcija ne vraca slovarja.")
