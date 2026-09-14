import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

sez = {'starosti': [26, 34, 30, 21, 39, 24, 25, 22, 17],
 'goli': [0, 0, 0, 0, 0, 1, 0, 2, 1],
 'rumeni_kartoni': [0, 0, 0, 0, 1, 1, 1, 0, 1],
 'rdeci_kartoni': [0, 0, 0, 0, 0, 0, 0, 0, 0]}

actual = naloge.drzavno_povprecje(sez)
expected = {'povprecna_starost': 26.44, 'najvec_golov': 2, 'kazni': (4, 0)}

test_case.assertEqual(actual, expected, 'Napaka pri branju novih podatkov.')
