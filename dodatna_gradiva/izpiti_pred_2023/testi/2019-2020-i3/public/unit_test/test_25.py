import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = TEST_POVPRECNA_STAROST[3]
actual = izpit.povprecna_starost(arg)

test_case.assertIsNone(actual)
