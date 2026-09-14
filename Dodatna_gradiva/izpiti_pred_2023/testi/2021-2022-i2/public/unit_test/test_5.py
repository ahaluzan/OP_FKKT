import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = DATA3
actual = izpit.preberi_vreme('weather_LJ_2021.csv')

test_case.assertEqual(actual, expected)
