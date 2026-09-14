import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = RES2
actual = izpit.lepi_dnevi(DATA2)

test_case.assertEqual(actual, expected)
