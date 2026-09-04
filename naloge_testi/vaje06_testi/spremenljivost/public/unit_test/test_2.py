import unittest
from spremenljivost import *

test_case = unittest.TestCase()
seznam = [400, -100, 256, -1089, 0]
koreni_seznam(seznam)

expected = [20.0, None, 16.0, None, 0.0]
test_case.assertEqual(expected, seznam)