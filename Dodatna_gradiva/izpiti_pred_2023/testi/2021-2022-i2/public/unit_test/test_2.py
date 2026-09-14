import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = DATA1
actual = izpit.preberi_vreme('weather_KP_small.csv')

test_case.assertEqual(len(actual), len(expected), "Napacno stevilo prebranih meritev")
