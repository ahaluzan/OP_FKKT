import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = None

actual = naloge.najvec_vrednosti({})

test_case.assertEqual(expected, actual, "Napacno vracanje v primeru, da je slovar prazen. Namig: 'None' ne sme biti niz.")