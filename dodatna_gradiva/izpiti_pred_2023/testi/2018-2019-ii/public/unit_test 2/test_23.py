import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

CASE = 0
test_case.assertIn(izpit.najmanj_pogosta_stevila(READS[CASE]), RAREST[CASE])
