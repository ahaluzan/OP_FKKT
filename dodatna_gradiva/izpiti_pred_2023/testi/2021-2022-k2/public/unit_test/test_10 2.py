import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

act = naloge.v_slovarja(N1_DATA3)
exp = N2_DATA3

test_case.assertEqual(act, exp)
