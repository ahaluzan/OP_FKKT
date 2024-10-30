import unittest
from trgovina import *

zaloga = {}

test_case = unittest.TestCase()
test_case.assertEqual(stevilo_izdelkov(zaloga), 0)
