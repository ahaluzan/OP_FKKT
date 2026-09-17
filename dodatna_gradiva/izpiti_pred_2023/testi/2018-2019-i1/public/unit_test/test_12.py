import unittest

import izpit

test_case = unittest.TestCase()

RATINGS = {
    'a': [1, 1, 1, 1],
    'b': [0, 0, 0, 0],
}

actual = izpit.presek(RATINGS, 'a', 'b')
expected = []

test_case.assertEqual(actual, expected, "Neustrezen presek za uporabnika '{}' in '{}' ter ocene {}".format(
    'a', 'b', RATINGS))
