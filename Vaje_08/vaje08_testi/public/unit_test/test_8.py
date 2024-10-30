'''velike_zacetnice'''
import unittest
from metode import *

test_case = unittest.TestCase()
s = 'Univerza v Ljubljani'

test_case.assertEqual(velike_zacetnice(s), 'Univerza v Ljubljani')