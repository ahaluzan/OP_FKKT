'''najboljsi_film'''
import unittest

import izpit

test_case = unittest.TestCase()

VOTES = {
    'Titanic': {
        'deki': 5,
        'Rak': 4,
        'ATom': 3,
        'ivek': 2,
        'miso': 1},
    'Matrix': {
        'deki': 5,
        'Janez': 5,
    }
}

actual = izpit.najboljsi_film(VOTES)
expected = 'Matrix'

test_case.assertEqual(expected, actual)
