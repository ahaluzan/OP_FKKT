import unittest

import izpit
from .TEST_DATA import *
from .utils import *

test_case = unittest.TestCase()

actual = izpit.preberi_podatke(DATA_FILES[0])
expected = READS[0]

compare_read_data(actual, expected, test_case)
