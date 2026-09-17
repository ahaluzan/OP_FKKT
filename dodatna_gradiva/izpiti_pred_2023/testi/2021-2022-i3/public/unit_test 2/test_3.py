import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = PREBERI_PODATKE[0][1]
actual = izpit.preberi_podatke(*PREBERI_PODATKE[0][0])

test_case.assertEqual(len(actual), len(expected), "Napacno stevilo prebranih meritev")
