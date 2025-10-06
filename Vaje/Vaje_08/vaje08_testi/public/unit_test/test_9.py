import unittest
from metode import *

test_case = unittest.TestCase()
s = 'V trgovini je kupila ananas in jabolka.'

test_case.assertEqual(velike_zacetnice(s), 'V Trgovini je Kupila Ananas in Jabolka.')