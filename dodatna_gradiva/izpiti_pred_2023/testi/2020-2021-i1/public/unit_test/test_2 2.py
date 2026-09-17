import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_DATA

actual = izpit.preberi_populacijo("population1.csv")
#expected = case

for v in actual.values():
    test_case.assertEqual(type(v), type(25), "Vrednost v slovarju je napacnega tipa.")
