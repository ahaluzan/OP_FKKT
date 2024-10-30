import unittest
from metode import *

test_case = unittest.TestCase()
seznam1 = []
seznam2 = []

test_case.assertEqual(repertuar(seznam1, seznam2), set())