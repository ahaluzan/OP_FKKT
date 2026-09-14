import unittest
import naloge

test_case = unittest.TestCase()

cilj = 12
zacetna_razdalja = 11

expected = 1
actual = naloge.priprave(cilj, zacetna_razdalja)

test_case.assertEqual(expected, actual, "Nepravilno vracanje stevila treningov, ko je cilj dosezen v enem tednu.")