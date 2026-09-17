import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = NAJSTAREJSI[2]
actual = izpit.najstarejsi(*case[0])
expected = case[1]

test_case.assertEquals(actual, expected)
