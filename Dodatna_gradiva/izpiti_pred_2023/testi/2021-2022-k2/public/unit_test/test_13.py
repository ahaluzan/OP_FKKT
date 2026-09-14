import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

act = naloge.manjkajoci(*N3[0][0])
exp = N3[0][1]

test_case.assertEqual(act, exp)

