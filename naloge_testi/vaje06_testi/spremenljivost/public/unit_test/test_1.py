'''koreni_seznam'''
import unittest
from spremenljivost import *

test_case = unittest.TestCase()
seznam = [0, 1, 4, 9, 16, 25]
koreni_seznam(seznam)

expected = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
test_case.assertEqual(expected, seznam)