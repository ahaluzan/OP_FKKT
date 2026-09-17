import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

for genre in GENRES.keys():
    actual = izpit.povprecna_dolzina(READ, genre)
    expected = GENRES[genre]

    test_case.assertEqual(actual, expected, "Napačna vrednost za žanr '%s'" % genre)
