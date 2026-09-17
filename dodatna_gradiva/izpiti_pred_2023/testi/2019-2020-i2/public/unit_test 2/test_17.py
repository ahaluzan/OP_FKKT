import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = V_DRZAVI[0]
actual = izpit.v_drzavi(*case[0])
expected = case[1]

test_case.assertEqual(len(actual), len(expected), "Stevilo igralcev v rezultatu je napacno")
