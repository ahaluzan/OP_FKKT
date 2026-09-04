import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

result = minimum([23, -42007009, -870000790, -34000007800, 1, -3, 2])
expected = -34000007800
test_case.assertEqual(result, expected)