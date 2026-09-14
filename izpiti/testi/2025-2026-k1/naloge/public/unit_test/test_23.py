import unittest
import naloge

test_case = unittest.TestCase()

cilj = 11
zacetna_razdalja = 6

expected = 7
actual = naloge.priprave(cilj, zacetna_razdalja)

test_case.assertEqual(expected, actual, "Napacna vrednost. Trenutna razdalja se povecuje za 10 % (razdalja*1.1).")