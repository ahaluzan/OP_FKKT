import unittest

from kolokvij import *

test_case = unittest.TestCase()
data = []
expected = {}

actual = v_slovar(data)
test_case.assertEqual(expected, actual)
