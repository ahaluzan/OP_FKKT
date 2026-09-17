import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = izpit.kolicina_padavin(TESTNI_PODATKI_1)
expected = PADAVINE_TESTNI_1

for m, r in expected.items():
    test_case.assertIn(m, actual, "Manjkajo podatki za mesec %d" % m)
    test_case.assertEqual(r, actual[m], "Kolicina padavin za mesec %d ni prava." % m)

