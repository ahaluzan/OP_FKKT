import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

del VOTES["Pulp Fiction"]
del VOTES["Schindler's List"]
del VOTES["Matrix"]

actual = izpit.najboljsi_film(VOTES)
expected = "The godfather"

test_case.assertEqual(expected, actual)
