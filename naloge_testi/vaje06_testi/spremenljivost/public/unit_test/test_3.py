import unittest
from spremenljivost import *

test_case = unittest.TestCase()
seznam = []
koreni_seznam(seznam)
expected = []
test_case.assertEqual(expected, seznam)