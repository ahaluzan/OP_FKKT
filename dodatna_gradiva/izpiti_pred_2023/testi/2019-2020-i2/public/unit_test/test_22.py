import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = SKUPNI[0]
actual = izpit.skupni(*case[0])
expected = case[1]

test_case.assertEqual(len(actual), len(expected), "Napacno stevilo zapisov v rezultatu")
