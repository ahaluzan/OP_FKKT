import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

for genre in EXTRA_GENRE.keys():
    actual = izpit.povprecna_dolzina(EXTRA_READ, genre)
    expected = EXTRA_GENRE[genre]
    test_case.assertEqual(actual, expected, "Napačna vrednost za žanr '%s'" % genre)
