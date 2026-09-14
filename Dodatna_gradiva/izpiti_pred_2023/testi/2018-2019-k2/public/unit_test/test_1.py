'''preberi_podatke'''
import unittest

import naloga
from .TEST_DATA import *

test_case = unittest.TestCase()


prebrano = naloga.preberi_podatke(DATA_FILE_1)
test_case.assertEqual(len(prebrano), 2, "Funkcija mora vrniti terko dolžine 2")
