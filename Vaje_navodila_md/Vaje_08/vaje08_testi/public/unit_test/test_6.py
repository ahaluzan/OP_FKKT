import unittest
from metode import *

test_case = unittest.TestCase()
s = 'Kupila je jagode, maline in hruške.'

test_case.assertEqual(najdaljse_besede(s), {'maline', 'jagode', 'hruške', 'Kupila'})