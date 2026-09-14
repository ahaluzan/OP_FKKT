import unittest

import naloga
from .TEST_DATA import *

test_case = unittest.TestCase()

poskusi, resitve = naloga.preberi_podatke(DATA_FILE_1)

test_case.assertEqual(resitve, SOLUTIONS, "Prebrane rešitve niso pravilne")
test_case.assertEqual(poskusi, ATTEMPTS, "Prebrani odgovor niso pravilni")
