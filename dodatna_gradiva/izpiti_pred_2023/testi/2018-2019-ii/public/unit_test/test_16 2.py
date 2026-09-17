'''prestej_sedmice'''
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

CASE = 0

test_case.assertEqual(HITS[CASE], izpit.prestej_sedmice(READS[CASE], JACKPOTS[CASE]))
