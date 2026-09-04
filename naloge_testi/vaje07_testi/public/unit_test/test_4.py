import unittest
from trgovina import *

zaloga = {'mleko': [0.86, 128], 'jogurt': [0.49, 56],}

test_case = unittest.TestCase()
test_case.assertEqual(stevilo_izdelkov(zaloga), 184)
