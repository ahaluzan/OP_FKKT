import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

case = TEST_VAC3

podatki = [('USA', 'Americas', 22645757, 377446, 331341050),
 ('Slovenia', 'Europe', 141587, 3171, 2078989),
 ('Spain', 'Europe', 2137220, 52683, None)]

actual = izpit.cepljenje(podatki, [], 2*10**6)
expected = case

test_case.assertEquals(actual, [])
