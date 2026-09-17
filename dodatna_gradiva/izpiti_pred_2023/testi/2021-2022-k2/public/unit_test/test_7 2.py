import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

a1, a2 = naloge.v_slovarja(N1_DATA)
e1, e2 = N2_DATA

test_case.assertIsInstance(a1, type(e1), "Prvi del terke ni pravega tipa")
test_case.assertIsInstance(a2, type(e2), "Drugi del terke ni pravega tipa")

for act, exp in zip(sorted(list(a1.keys())), sorted(list(e1.keys()))):
    test_case.assertIsInstance(act, type(exp), "Kljuci prvega slovarja so napacnega tipa")

for act, exp in zip(sorted(list(a1.values())), sorted(list(e1.values()))):
    test_case.assertIsInstance(act, type(exp), "Vrednosti prvega slovarja so napacnega tipa")

    for a, e in zip(act, exp):
        test_case.assertIsInstance(a, type(e), "Vrednosti prvega slovarja so napacnega tipa")

for act, exp in zip(sorted(list(a2.keys())), sorted(list(e2.keys()))):
    test_case.assertIsInstance(act, type(exp), "Kljuci drugega slovarja so napacnega tipa")

for act, exp in zip(sorted(list(a2.values())), sorted(list(e2.values()))):
    test_case.assertIsInstance(act, type(exp), "Vrednosti drugega slovarja so napacnega tipa")

    for a, e in zip(act, exp):
        test_case.assertIsInstance(a, type(e), "Vrednosti drugega slovarja so napacnega tipa")

        for a_, e_ in zip(a, e):
            test_case.assertIsInstance(a_, type(e_), "Vrednosti drugega slovarja so napacnega tipa")
