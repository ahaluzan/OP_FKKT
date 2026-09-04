import unittest
from metode import *

test_case = unittest.TestCase()
seznam1 = ['Let It Be', 'Imagine', 'The River', 'One', 'Stand By Me']
seznam2 = ['Stairway To Heaven']

test_case.assertEqual(skupne(seznam1, seznam2), set())