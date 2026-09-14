import unittest
import naloge
import variables

test_case = unittest.TestCase()

actual = naloge.statistika(variables.slovar_izdelek5)

test_case.assertTrue(all(isinstance(v, float) for v in actual.values()), "Vrednosti niso pravilnega podatkovnega tipa (float).")
