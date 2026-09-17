import unittest

import naloga
from .TEST_DATA import *

test_case = unittest.TestCase()

poskusi, resitve = naloga.preberi_podatke(DATA_FILE_1)

test_case.assertEqual(len(resitve), len(SOLUTIONS), "Število odgovorov v rešitvah se ne ujema")

for (actual_key, actual_values), (expected_key, expected_values) in zip(poskusi.items(), ATTEMPTS.items()):
    test_case.assertEqual(len(actual_values), len(expected_values),
                          "Število odgovorov za študenta %s je napačno" % expected_key)
