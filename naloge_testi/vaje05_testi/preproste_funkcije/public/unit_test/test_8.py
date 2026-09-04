import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

result = minimum([34000007800,34000007799])
expected = 34000007799
test_case.assertEqual(result, expected)