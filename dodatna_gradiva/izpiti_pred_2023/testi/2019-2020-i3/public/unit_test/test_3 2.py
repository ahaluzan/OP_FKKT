import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DATA

actual = izpit.preberi_podatke("infections_small.txt")
expected = case

for act, exp in zip(actual, expected):
    test_case.assertEqual(len(act), len(act), "Napacno stevilo prebranih stolpcev")
