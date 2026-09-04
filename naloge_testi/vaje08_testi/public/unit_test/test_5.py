import unittest
from metode import *

test_case = unittest.TestCase()
s = 'V trgovini je kupila ananas in jabolka.'

test_case.assertEqual(najdaljse_besede(s), {'trgovini'})