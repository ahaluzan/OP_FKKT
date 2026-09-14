import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = list({'Sweater'})[0]

actual = list(naloge.po_spolih(variables.shop10))[0]

test_case.assertEqual(type(expected), type(actual), "Napacen tip vsebine v mnozici.")