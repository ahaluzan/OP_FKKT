import unittest

from naloge import *

test_case = unittest.TestCase()
expected = set()

arg = []
result = naj_padavin(arg)
test_case.assertEqual(expected, result)
