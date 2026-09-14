import unittest

from kolokvij import *

test_case = unittest.TestCase()
data = [('DNK', 2014, 91.0),
        ('DNK', 2015, 90.0),
        ('DNK', 2016, 91.0),
        ('DNK', 2017, 95.0),
        ('DNK', 2018, 96.0),
        ('FRA', 2012, 99.0),
        ('FRA', 2013, 99.0),
        ('FRA', 2014, 98.0),
        ('FRA', 2015, 97.0),
        ('FRA', 2016, 96.7),
        ('FRA', 2017, 96.1),
        ('FRA', 2018, 96.3)]
expected = {'FRA'}

actual = precepljeni(data, 96, [2012, 2013, 2014, 2015])
test_case.assertEqual(expected, actual)
