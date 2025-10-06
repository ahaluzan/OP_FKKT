'''najdaljse_besede'''
import unittest
from metode import *

test_case = unittest.TestCase()
s = 'Univerza v Ljubljani'

test_case.assertEqual(najdaljse_besede(s), {'Ljubljani'})