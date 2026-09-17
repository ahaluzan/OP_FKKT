'''statistika'''
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
expected = {
    'AUS': {'min': 94.6, 'max': 94.8, 'avg': 94.7},
    'DNK': {'min': 95.0, 'max': 96.0, 'avg': 95.5},
    'FRA': {'min': 96.1, 'max': 96.3, 'avg': 96.2},
    'SVN': {'min': 93.0, 'max': 94.0, 'avg': 93.5}}

actual = statistika(data)
test_case.assertEqual(len(expected), len(actual))
