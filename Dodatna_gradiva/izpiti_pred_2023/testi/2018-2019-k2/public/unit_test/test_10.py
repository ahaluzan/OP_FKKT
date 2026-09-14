import unittest

import naloga
from .TEST_DATA import *

test_case = unittest.TestCase()

corrected = naloga.oceni_naloge(ATTEMPTS, SOLUTIONS)

test_case.assertEqual(corrected, CORRECTED, "Naloge niso ocenjene pravilno")
