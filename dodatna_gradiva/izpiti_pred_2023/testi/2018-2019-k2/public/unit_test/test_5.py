import unittest

import naloga
from .TEST_DATA import *

test_case = unittest.TestCase()

poskusi, resitve = naloga.preberi_podatke(DATA_FILE_2)

test_case.assertEqual(len(poskusi), 30, "Študentov je 30")
test_case.assertEqual(len(resitve), 13, "Vsak izpit ima 13 odgovorov")
