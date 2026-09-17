'''v_slovar'''
import unittest

from kolokvij import *

test_case = unittest.TestCase()
data = [('AUS', 2017, 94.8),
        ('AUS', 2018, 94.6),
        ('DNK', 2017, 95.0),
        ('DNK', 2018, 96.0),
        ('FRA', 2017, 96.1),
        ('FRA', 2018, 96.3),
        ('SVN', 2017, 94.0),
        ('SVN', 2018, 93.0)]

expected = {'AUS': [(2017, 94.8), (2018, 94.6)],
            'DNK': [(2017, 95.0), (2018, 96.0)],
            'FRA': [(2017, 96.1), (2018, 96.3)],
            'SVN': [(2017, 94.0), (2018, 93.0)]}

actual = v_slovar(data)
test_case.assertEqual(type(expected), type(actual))
