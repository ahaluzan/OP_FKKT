"""najvecje_povisanje"""
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

data = [('Italy', 0.14), ('Russia', 0.16), ('Slovenia', 0.24)]
actual = izpit.najvecje_povisanje(data)
expected = TEST_MINC1

test_case.assertEqual(actual, expected)
