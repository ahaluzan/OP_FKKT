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

expected = {'AUS': [(2017, 94.8)],
            'AUT': [(2017, 90.0)],
            'BEL': [(2017, 98.0)],
            'CAN': [(2017, 91.0)],
            'CZE': [(2017, 96.0)],
            'DNK': [(2017, 95.0)],
            'FIN': [(2017, 89.0)],
            'FRA': [(2017, 96.1)],
            'DEU': [(2017, 93.0)],
            'GRC': [(2017, 99.0)]}

actual = v_slovar(data)
test_case.assertEqual(expected, actual)
