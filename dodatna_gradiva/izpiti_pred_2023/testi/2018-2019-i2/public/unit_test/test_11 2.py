'''stevilo_dni_za_izlete'''
import unittest

from .TEST_DATA import *
import izpit

test_case = unittest.TestCase()


dates = IZLETI[0][0]
expected = IZLETI[0][1]
actual = izpit.stevilo_dni_za_izlete(dates)
test_case.assertEqual(actual, expected, "Na podanih datumih (%s) je %d izletnih dni in ne %d" % (dates, expected, actual))
