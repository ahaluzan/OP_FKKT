'''povprecna_dolzina'''
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

for genre in GENRES.keys():
    actual = round(izpit.povprecna_dolzina(READ, genre), 2)
    expected = GENRES[genre]

    test_case.assertEqual(actual, expected, "Napačna vrednost za žanr '%s'" % genre)
