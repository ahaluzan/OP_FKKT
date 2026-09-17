import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

act = naloge.v_slovarja(N1_DATA)
exp = N2_DATA

test_case.assertEqual(act, exp)
