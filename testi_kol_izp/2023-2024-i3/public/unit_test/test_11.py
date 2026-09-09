import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

sez = {'starosti': [],
 'goli': [],
 'rumeni_kartoni': [],
 'rdeci_kartoni': []}

actual = naloge.drzavno_povprecje(sez)
expected = {'povprecna_starost': False, 'najvec_golov': 0, 'kazni': (0, 0)}

test_case.assertEqual(list(actual.values()), list(expected.values()), "Napacno vracanje funkcije pri praznih vrednostih.")

