import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.preberi_filme(EXTRA_DATA_FILE)
expected = EXTRA_READ

test_case.assertEqual(expected, actual)
