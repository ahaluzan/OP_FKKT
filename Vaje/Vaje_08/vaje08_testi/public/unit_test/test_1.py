'''besede_aa'''
import unittest
from metode import *

test_case = unittest.TestCase()
result = aa_besede('Univerza v Ljubljani')
expected = set()
test_case.assertEqual(result, expected)