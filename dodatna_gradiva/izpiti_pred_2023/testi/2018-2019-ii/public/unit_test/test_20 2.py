import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

test_case.assertEqual(1, izpit.prestej_sedmice(READS[1], [6, 8, 11, 20, 23, 27, 37]))
