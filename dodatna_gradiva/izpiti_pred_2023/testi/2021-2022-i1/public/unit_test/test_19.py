import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = OBREMENJENI_DNEVI[3][1]
actual = izpit.obremenjeni_dnevi(*OBREMENJENI_DNEVI[3][0])

test_case.assertEqual(actual, expected)
