import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = RES3
actual = izpit.lepi_dnevi(DATA3)

test_case.assertEqual(actual, expected)
