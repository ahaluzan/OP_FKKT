'''stopnje_obdavcitev'''
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.stopnje_obdavcitev(READS[1])
expected = STOPNJE_OBDAVCITEV[1]

test_case.assertEqual(len(actual), len(expected), "Rezultat ne vsebuje podatkov za vse mesece")

