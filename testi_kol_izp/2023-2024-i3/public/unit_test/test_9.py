'''drzavno_povprecje'''
import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

sez = {'starosti': [28, 27, 33, 26, 26, 29, 26, 29, 23, 24, 26],
 'goli': [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
 'rumeni_kartoni': [0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 0],
 'rdeci_kartoni': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

actual = naloge.drzavno_povprecje(sez)
expected = {'povprecna_starost': 27.0, 'najvec_golov': 1, 'kazni': (6, 0)}

test_case.assertEqual(len(actual), len(expected), "Slovar ima napacno stevilo elementov.")
