import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.preberi_filme(DATA_FILE)
expected = READ

for act, exp in zip(actual, expected):
    test_case.assertEqual(round(act[3], 2), exp[3], "Napačen čas trajanja za film '%s'" % exp[0])
