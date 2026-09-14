import unittest
import naloge

test_case = unittest.TestCase()

cilj = 10
zacetna_razdalja = 12

expected = "Cilj ste že dosegli."
actual = naloge.priprave(cilj, zacetna_razdalja)

test_case.assertEqual(expected, actual, "Napacno vracanje v primeru, da je cilj ze dosezen. Preverite tipkarske napake.")