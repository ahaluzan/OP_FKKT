import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = OBDELAJ_DATUME[0][1]
actual = izpit.obdelaj_datume(*OBDELAJ_DATUME[0][0])

test_case.assertEqual(actual, expected)
