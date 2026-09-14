import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.preberi_filme(DATA_FILE)
expected = READ

for act, exp in zip(actual, expected):
    test_case.assertEqual(act[2], exp[2], "Napačno leto za film '%s'" % exp[0])
