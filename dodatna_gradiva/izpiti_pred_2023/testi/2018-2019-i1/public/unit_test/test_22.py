import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.najboljsi_film(VOTES)
expected = 'Pulp Fiction'

test_case.assertEqual(expected, actual)
