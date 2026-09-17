import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

data = [('Antarctica', -1.25), ('Italy', -0.14), ('Tonga', -0.17), ('Russia', 0.00), ('Fiji', -0.25)]
actual = izpit.najvecje_povisanje(data)
expected = TEST_MINC5

test_case.assertEqual(actual, expected)
