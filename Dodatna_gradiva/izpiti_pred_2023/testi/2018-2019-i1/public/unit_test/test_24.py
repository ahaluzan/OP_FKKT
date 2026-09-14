import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

del VOTES["Pulp Fiction"]
del VOTES["Schindler's List"]

actual = izpit.najboljsi_film(VOTES)
expected = "Matrix"

test_case.assertEqual(expected, actual)
