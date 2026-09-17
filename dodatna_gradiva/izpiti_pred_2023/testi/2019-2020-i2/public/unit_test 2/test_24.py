import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = SKUPNI[1]
actual1 = izpit.skupni(*case[0])
expected1 = case[1]

actual, expected = {}, {}
for k, v in actual1.items():
    actual[frozenset(k)] = v

for k, v in expected1.items():
    expected[frozenset(k)] = v

test_case.assertEqual(actual, expected)
