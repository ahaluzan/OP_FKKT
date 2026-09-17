'''obdobja_za_izlete'''
import unittest

from .TEST_DATA import *
import izpit

test_case = unittest.TestCase()


dates = READS[0]
actual = izpit.obdobja_za_izlete(dates)
expected = OBDOBJA_IZLETI
test_case.assertEqual(len(actual), len(expected), "Stevilo obdobij ni pravilno")

