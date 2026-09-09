'''pridobi_leto'''
import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

act = naloge.pridobi_leto('23-01-1930')
exp = 1930

test_case.assertEqual(act, exp, "Napacno delovanje, ko je leto na koncu")

act = naloge.pridobi_leto('1883-03-19')
exp = 1883

test_case.assertEqual(act, exp, "Napacno delovanje, ko je leto na zacetku")
