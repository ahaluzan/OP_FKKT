import unittest

from .TEST_DATA import *
import izpit

test_case = unittest.TestCase()


dates = READS[0][OBDOBJA_IZLETI_KONEC[0][0]:OBDOBJA_IZLETI_KONEC[0][1]]
actual = izpit.obdobja_za_izlete(dates)
expected = OBDOBJA_IZLETI_KONEC[0][2]

hint = ". Namig: kaj se zgodi, ce so zadnji dnevi v letu primerni za izlet?"

test_case.assertEqual(len(actual), len(expected),
                      "Stevilo obdobij ni pravilno%s" % (hint if len(actual) + 1 == len(expected) else ""))

for act, exp in zip(actual, expected):
    test_case.assertEqual(act, exp, "Napacen interval")
