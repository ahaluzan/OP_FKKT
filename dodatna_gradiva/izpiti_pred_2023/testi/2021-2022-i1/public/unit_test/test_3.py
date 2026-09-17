import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = PREBERI_STEVEC[0][1]
actual = izpit.preberi_stevec(*PREBERI_STEVEC[0][0])

test_case.assertEqual(actual, expected)
