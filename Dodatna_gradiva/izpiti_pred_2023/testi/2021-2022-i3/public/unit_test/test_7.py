import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = PO_LETIH[0][1]
actual = izpit.po_letih(*PO_LETIH[0][0])

for (act_k, act_v), (exp_k, exp_v) in zip(expected.items(), actual.items()):
    for (act_kk, act_vv), (exp_kk, exp_vv) in zip(exp_v.items(), act_v.items()):
        test_case.assertIsInstance(act_kk, type(exp_kk), "Kljuci v slovarju so napacnega tipa")
        test_case.assertIsInstance(act_vv, type(exp_vv), "Vrednosti v slovarju so napacnega tipa")
