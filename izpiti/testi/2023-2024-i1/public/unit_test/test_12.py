import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

sez = []

actual = naloge.statistika_strani(sez)
expected = {'min': -1, 'max': -1, 'avg': 'ni podatkov'}

test_case.assertEqual(actual, expected, 'Napaka pri praznem seznamu.')
