import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

for args, res in PRIMERJAVE_TEST_2:
    test_case.assertEquals(izpit.starejsi(*args), res, "%s mora biti %s %s" % (
        args[0],
        "manjsi ali enak" if res else "vecji",
        args[1]))
