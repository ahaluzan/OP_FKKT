import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

CASE = 1

test_case.assertEqual(HITS[CASE], izpit.prestej_sedmice(READS[CASE], JACKPOTS[CASE]))
