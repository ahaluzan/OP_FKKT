"""moski_zenske"""
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = TEST_SPOL[0]
actual = izpit.moski_zenske(arg)

test_case.assertIsInstance(actual, type(expected))
