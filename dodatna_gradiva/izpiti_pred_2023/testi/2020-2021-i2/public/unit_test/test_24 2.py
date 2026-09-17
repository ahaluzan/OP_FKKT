import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

data = []
actual = izpit.najvecje_povisanje(data)
expected = TEST_MINC4

test_case.assertEqual(actual, expected)
