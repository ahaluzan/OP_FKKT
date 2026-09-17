'''manjkajoci'''
import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

act = naloge.manjkajoci(*N3[0][0])
exp = N3[0][1]

for a, e in zip(sorted(act.keys()), sorted(exp.keys())):
    test_case.assertIsInstance(a, type(e), "Kljuci v slovarju so napacnega tipa")

