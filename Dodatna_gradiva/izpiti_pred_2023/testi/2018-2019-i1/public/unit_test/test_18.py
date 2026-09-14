import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.ocene_po_filmih(RATINGS, READ)
expected = VOTES

for movie, votes in expected.items():
    for name, assessment in votes.items():
        test_case.assertEqual(assessment, actual[movie][name],
                              "Uporabnik '{}' je za film '{}' podal oceno '{}' in ne '{}'".format(
                                  name, movie, assessment, actual[movie][name]
                              ))
