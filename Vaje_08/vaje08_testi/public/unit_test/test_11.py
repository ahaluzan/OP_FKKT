'''razlicne_skladbe'''
import unittest
from metode import *

test_case = unittest.TestCase()
seznam = ['Let It Be',
           'Imagine',
           'The River',
           'One',
           'Stand By Me',
           'Imagine',
           'Stairway To Heaven',
           'One',
           'Imagine']

test_case.assertEqual(razlicne_skladbe(seznam), 6)