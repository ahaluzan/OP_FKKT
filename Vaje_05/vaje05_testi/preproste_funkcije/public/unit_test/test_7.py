import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

result = minimum([870000790, 42007009, 34000007800])
expected = 42007009
test_case.assertEqual(result, expected)