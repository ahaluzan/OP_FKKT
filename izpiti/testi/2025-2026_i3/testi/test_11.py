"2. naloga"
import unittest
import naloge
import variables

test_case = unittest.TestCase()

actual = naloge.v_slovar(variables.kava5)

test_case.assertIsInstance(actual, dict, "Funkcija ne vraca slovarja.")
