"""naj_primer"""
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = TEST_NAJ_PRIMER[0]
actual = izpit.naj_primer(arg)

test_case.assertEquals(actual, expected)
