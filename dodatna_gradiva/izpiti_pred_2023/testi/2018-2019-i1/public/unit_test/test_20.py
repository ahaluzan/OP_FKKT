import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.ocene_po_filmih(EXTRA_RATINGS, EXTRA_READ)
expected = EXTRA_VOTES

for movie, votes in expected.items():
    for name, assessment in votes.items():
        test_case.assertEqual(assessment, actual[movie][name],
                              "Uporabnik '{}' je za film '{}' podal oceno '{}' in ne '{}'".format(
                                  name, movie, assessment, actual[movie][name]
                              ))

actual = izpit.ocene_po_filmih(EXTRA_RATINGS, EXTRA_READ)
expected = EXTRA_VOTES

for movie, votes in actual.items():
    for name, assessment in votes.items():
        test_case.assertIn(movie, expected, "Neznan film '%s'" % movie)
        test_case.assertIn(name, expected[movie], "Uporabnik '{}' ni ocenil filma '{}'".format(
            name, movie))
        test_case.assertEqual(assessment, expected[movie][name],
                              "Uporabnik '{}' je za film '{}' podal oceno '{}' in ne '{}'".format(
                                  name, movie, assessment, expected[movie][name]
                              ))
