import unittest

from .TEST_DATA import *
import izpit

test_case = unittest.TestCase()


dates = READS[0]
actual = izpit.obdobja_za_izlete(dates)
expected = OBDOBJA_IZLETI

test_case.assertEqual(len(actual), len(expected), "Stevilo obdobij ni pravilno")

for (a_start, a_end), (exp_start, exp_end) in zip(actual, expected):
    test_case.assertEqual(a_end, exp_end, "Konca obdobij za izlet se ne skladata.")

