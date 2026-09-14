import unittest

from kolokvij import *

test_case = unittest.TestCase()
data = [('AUS', 2017, 94.8),
        ('AUT', 2017, 90.0),
        ('BEL', 2017, 98.0),
        ('CAN', 2017, 91.0),
        ('CZE', 2017, 96.0),
        ('DNK', 2017, 95.0),
        ('FIN', 2017, 89.0),
        ('FRA', 2017, 96.1),
        ('DEU', 2017, 93.0),
        ('GRC', 2017, 99.0)]
expected = {
    'AUS': {'min': 94.8, 'max': 94.8, 'avg': 94.8},
    'AUT': {'min': 90.0, 'max': 90.0, 'avg': 90.0},
    'BEL': {'min': 98.0, 'max': 98.0, 'avg': 98.0},
    'CAN': {'min': 91.0, 'max': 91.0, 'avg': 91.0},
    'CZE': {'min': 96.0, 'max': 96.0, 'avg': 96.0},
    'DNK': {'min': 95.0, 'max': 95.0, 'avg': 95.0},
    'FIN': {'min': 89.0, 'max': 89.0, 'avg': 89.0},
    'FRA': {'min': 96.1, 'max': 96.1, 'avg': 96.1},
    'DEU': {'min': 93.0, 'max': 93.0, 'avg': 93.0},
    'GRC': {'min': 99.0, 'max': 99.0, 'avg': 99.0}}

actual = statistika(data)
test_case.assertEqual(expected, actual)
