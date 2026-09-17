import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = DATUMI_TEST[1]

actual = izpit.pretvori_datum(*case[0])
expected = case[1]

test_case.assertEqual(actual, expected, "Napacno pretvorjen datum")
