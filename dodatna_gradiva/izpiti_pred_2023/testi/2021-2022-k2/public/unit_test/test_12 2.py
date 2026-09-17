import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

act = naloge.manjkajoci(*N3[2][0])
exp = N3[2][1]

for a, e in zip(sorted(act.values()), sorted(exp.values())):
    test_case.assertIsInstance(a, type(e), "Vrednosti v slovarju so napacnega tipa")

    for a_, e_ in zip(a, e):
        test_case.assertIsInstance(a_, type(e_), "Vrednosti v slovarju so napacnega tipa")
