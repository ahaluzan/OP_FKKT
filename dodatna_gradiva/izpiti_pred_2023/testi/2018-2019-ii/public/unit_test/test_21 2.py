'''najmanj_pogosta_stevila'''
import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

test_case.assertGreaterEqual(izpit.najmanj_pogosta_stevila(READS[0]), 1)
