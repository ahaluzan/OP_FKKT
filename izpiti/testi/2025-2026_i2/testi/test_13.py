import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = 'Neveljaven indeks.'

actual = naloge.pripravi_slovar(variables.shop10, 15, 1)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije v primeru neveljavnega indeksa kljuca. Preverite tudi tipkarske napake.")