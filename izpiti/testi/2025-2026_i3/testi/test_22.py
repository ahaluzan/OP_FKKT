import unittest
import naloge
import variables

test_case = unittest.TestCase()

actual = naloge.statistika(variables.slovar_izdelek5)

test_case.assertTrue(all(isinstance(k, str) for k in actual.keys()), "Kljuci niso pravilnega podatkovnega tipa (str).")
