"3. naloga"
import unittest
import naloge
import variables

test_case = unittest.TestCase()

actual = naloge.statistika(variables.slovar_izdelek5)

test_case.assertIsInstance(actual, dict, "Funkcija ne vraca slovarja.")
