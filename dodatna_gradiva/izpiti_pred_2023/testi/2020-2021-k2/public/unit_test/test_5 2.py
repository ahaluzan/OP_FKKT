import unittest

from kolokvij import *

test_case = unittest.TestCase()
expected = [('AUS', 2017, 94.8),
            ('AUT', 2017, 90.0),
            ('FRA', 2017, 96.1),
            ('DEU', 2017, 93.0)]
actual = preberi_podatke('cep3.txt')
test_case.assertEqual(expected, actual)
