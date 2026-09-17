import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = TRETJA[0]
actual = izpit.najbolj_obremenjen(arg)

test_case.assertEqual(actual, expected)
