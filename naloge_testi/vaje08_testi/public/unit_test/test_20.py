'''unikatna_predvajanja'''
import unittest
from metode import *

test_case = unittest.TestCase()
seznam1 = ['Let It Be', 'Imagine', 'The River', 'One', 'Stand By Me']
seznam2 = ['Imagine', 'Stairway To Heaven', 'One', 'Imagine']

test_case.assertEqual(unikatna_predvajanja(seznam1, seznam2),
                      {'Let It Be', 'The River', 'Stand By Me', 'Stairway To Heaven'})