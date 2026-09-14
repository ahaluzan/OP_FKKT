import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = set()
actual = izpit.lepi_dnevi({})

test_case.assertEqual(actual, expected)
