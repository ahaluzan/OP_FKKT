import unittest

from .TEST_DATA import *
import izpit

test_case = unittest.TestCase()


dates = IZLETI[1][0]
expected = IZLETI[1][1]
actual = izpit.stevilo_dni_za_izlete(dates)
test_case.assertEqual(actual, expected, "Na podanih datumih (%s) je %d izletnih dni in ne %d" % (dates, expected, actual))
