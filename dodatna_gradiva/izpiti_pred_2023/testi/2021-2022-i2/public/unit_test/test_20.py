import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = False
actual = izpit.najvec_soncnih({})

test_case.assertEqual(actual, expected)
