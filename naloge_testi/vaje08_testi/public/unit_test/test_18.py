import unittest
from metode import *

test_case = unittest.TestCase()
seznam1 = []
seznam2 = ['Imagine', 'Stairway To Heaven', 'One', 'Imagine']

test_case.assertEqual(repertuar(seznam1, seznam2),
                      {'Imagine', 'Stairway To Heaven', 'One', 'Imagine'})
