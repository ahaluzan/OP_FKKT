import unittest

from .TEST_DATA import *
import izpit

test_case = unittest.TestCase()

actual = izpit.najboljse_polletje(READS[0])
expected = NAJBOLJSA_POLLETJA[0]

test_case.assertEqual(actual[0], expected[0], "Zacetni datum je napacen.")
test_case.assertEqual(actual[1], expected[1], "Koncni datum je napacen.")
test_case.assertEqual(actual[2], expected[2], "Povprecje je napacno.")
