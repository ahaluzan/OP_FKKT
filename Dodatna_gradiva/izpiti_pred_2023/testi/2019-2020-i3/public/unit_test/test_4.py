import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DATA

actual = izpit.preberi_podatke("infections_small.txt")
expected = case

for act, exp in zip(actual, expected):
    for i, (act_c, exp_c) in enumerate(zip(act, exp)):
        test_case.assertEqual(
            type(act_c),
            type(exp_c),
            "Stolpec na poziciji %i mora biti tipa %s in ne %s"
            % (i, type(exp_c), type(act_c)),
        )
