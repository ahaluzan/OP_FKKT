'''statistika_vplacil'''
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()
actual = izpit.statistika_vplacil(READS[0])
expected = STATS[0]

# Prebrani igralci
test_case.assertEqual(actual.keys(), expected.keys())
