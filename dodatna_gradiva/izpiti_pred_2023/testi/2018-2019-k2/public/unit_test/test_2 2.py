import unittest

import naloga
from .TEST_DATA import *

test_case = unittest.TestCase()

poskusi, _ = naloga.preberi_podatke(DATA_FILE_1)

test_case.assertEqual(len(poskusi.keys()), len(ATTEMPTS.keys()), "Število študentov se ne ujema")