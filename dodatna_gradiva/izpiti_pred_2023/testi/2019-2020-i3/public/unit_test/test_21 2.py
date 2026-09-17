"""povprecna_starost"""
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = TEST_POVPRECNA_STAROST[0]
actual = izpit.povprecna_starost(arg)

test_case.assertIsInstance(actual, type(expected))
