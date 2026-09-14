import unittest
import naloge

test_case = unittest.TestCase()

cilj = 100
zacetna_razdalja = 0.5

expected = 56
actual = naloge.priprave(cilj, zacetna_razdalja)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")