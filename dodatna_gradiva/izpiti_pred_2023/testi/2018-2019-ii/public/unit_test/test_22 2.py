import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

test_case.assertLessEqual(izpit.najmanj_pogosta_stevila(READS[0]), 39)
