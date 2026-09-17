import unittest

import naloga
from .TEST_DATA import *

test_case = unittest.TestCase()

graded = naloga.izracunaj_ocene(CORRECTED)

test_case.assertEqual(graded, GRADED, "Izračunane ocene niso prave")
