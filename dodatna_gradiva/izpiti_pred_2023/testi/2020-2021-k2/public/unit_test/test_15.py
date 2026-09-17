import unittest

from kolokvij import *

test_case = unittest.TestCase()
data = []
expected = {}

actual = statistika(data)
test_case.assertEqual(expected, actual)
