import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = RAZBIJ_DATUM[0][1]
actual = izpit.razbij_datum(*RAZBIJ_DATUM[0][0])

test_case.assertEqual(actual, expected)
