import unittest

import naloga
from .TEST_DATA import *

test_case = unittest.TestCase()


distributed = naloga.porazdelitev_ocen(GRADED)

test_case.assertEqual(distributed, DISTRIBUTED, "Izračunana porazdelitev ocen ni pravilna")
