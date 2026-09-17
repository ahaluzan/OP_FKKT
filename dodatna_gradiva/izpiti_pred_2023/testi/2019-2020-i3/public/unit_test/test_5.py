import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DATA

actual = izpit.preberi_podatke("infections_small.txt")
expected = case

test_case.assertEquals(actual, expected)
