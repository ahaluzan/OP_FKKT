import unittest

import izpit

test_case = unittest.TestCase()

RATINGS = {
    'a': [1, 1, 1, 1],
    'b': [1, 1, 1, 1],
}

actual = izpit.presek(RATINGS, 'a', 'b')
expected = [0, 1, 2, 3]

test_case.assertEqual(actual, expected, "Neustrezen presek za uporabnika '{}' in '{}' ter ocene {}".format(
    'a', 'b', RATINGS))
