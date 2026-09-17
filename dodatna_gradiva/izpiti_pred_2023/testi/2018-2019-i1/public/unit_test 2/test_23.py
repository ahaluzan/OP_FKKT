import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

del VOTES['Pulp Fiction']

actual = izpit.najboljsi_film(VOTES)
expected = "Schindler's List"

test_case.assertEqual(expected, actual)
