import unittest
from metode import *

test_case = unittest.TestCase()
seznam = ['Let It Be',
           'Let It Be',
           'Let It Be',
           'Let It Be',
           'Let It Be',
           'Let It Be',]

test_case.assertEqual(razlicne_skladbe(seznam), 1)