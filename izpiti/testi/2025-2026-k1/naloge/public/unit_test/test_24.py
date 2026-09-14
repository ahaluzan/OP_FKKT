import unittest
import naloge

test_case = unittest.TestCase()

cilj = 11
zacetna_razdalja = 3

expected = 14
actual = naloge.priprave(cilj, zacetna_razdalja)

test_case.assertEqual(expected, actual, "Napacno racunanje stevila treningov. Trenutna razdalja se povecuje za 10 % (razdalja*1.1).")