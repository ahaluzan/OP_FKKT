'''presek'''
import unittest

import izpit

test_case = unittest.TestCase()

RATINGS = {
    'a': [],
    'b': [],
}

actual = izpit.presek(RATINGS, 'a', 'b')
expected = []

test_case.assertEqual(actual, expected, "Neustrezen presek za uporabnika '{}' in '{}' ter ocene {}".format(
    'a', 'b', RATINGS))
