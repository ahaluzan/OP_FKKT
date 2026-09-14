import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DATA

actual = izpit.primerov_na_regijo([])
expected = {}

test_case.assertEquals(actual, expected)
