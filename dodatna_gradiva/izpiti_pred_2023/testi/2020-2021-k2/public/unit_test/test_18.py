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
expected = {'DNK', 'FRA'}

actual = precepljeni(data, 96)
test_case.assertEqual(expected, actual)
