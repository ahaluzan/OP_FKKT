import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = TRETJA[3]
actual = izpit.najbolj_obremenjen(arg)

test_case.assertEqual(actual, expected)