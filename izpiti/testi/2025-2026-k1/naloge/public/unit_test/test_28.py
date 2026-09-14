import unittest
import naloge

test_case = unittest.TestCase()

cilj = 10
zacetna_razdalja = 0.1

expected = 49
actual = naloge.priprave(cilj, zacetna_razdalja)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")