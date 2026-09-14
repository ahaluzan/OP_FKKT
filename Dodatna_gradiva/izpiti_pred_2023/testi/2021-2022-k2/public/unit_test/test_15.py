import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

act = naloge.manjkajoci(*N3[2][0])
exp = N3[2][1]

test_case.assertEqual(act, exp)
