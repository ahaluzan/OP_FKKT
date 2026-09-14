'''preberi_filme'''
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.preberi_filme(DATA_FILE)
expected = READ

test_case.assertEqual(len(actual), len(expected), "Filmov mora biti %d" % len(expected))

for act, exp in zip(actual, expected):
    test_case.assertEqual(act[:2], exp[:2])
