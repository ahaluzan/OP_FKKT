import unittest
from metode import *

test_case = unittest.TestCase()

seznam1 = ['Imagine', 'One',]
seznam2 = ['Imagine', 'One', 'Imagine']

test_case.assertEqual(unikatna_predvajanja(seznam1, seznam2), set())