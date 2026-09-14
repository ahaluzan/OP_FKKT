import unittest
from naloge import *

test_case = unittest.TestCase()
expected = ''
result = komplement('TTAAGGCCaaa')
test_case.assertEqual(expected, result)
