import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()
actual = izpit.statistika_vplacil(READS[1])
expected = STATS[1]

# Prebrani igralci
test_case.assertEqual(actual.keys(), expected.keys())
