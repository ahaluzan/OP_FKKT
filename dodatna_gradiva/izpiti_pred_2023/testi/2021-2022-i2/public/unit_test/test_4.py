import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = DATA2
actual = izpit.preberi_vreme('weather_KP_2021.csv')

test_case.assertEqual(actual, expected)
