import unittest
from metode import *

test_case = unittest.TestCase()
result = aa_besede('Anja je v trgovini kupila ananas in jabolka.')
expected = {'ananas', 'Anja', 'jabolka'}
test_case.assertEqual(result, expected)