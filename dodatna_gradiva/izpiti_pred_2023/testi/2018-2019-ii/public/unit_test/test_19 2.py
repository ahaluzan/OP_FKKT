import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

test_case.assertEqual(1, izpit.prestej_sedmice(READS[0], [3, 11, 23, 26, 31, 33, 38]))
