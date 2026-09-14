"pripravi_slovar"
import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.slovar10

actual = naloge.pripravi_slovar(variables.shop10, 0, 1)

test_case.assertEqual(type(expected), type(actual), "Funkcija vraca napacen podatkovni tip.")