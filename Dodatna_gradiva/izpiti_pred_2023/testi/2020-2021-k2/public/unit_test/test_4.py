import unittest

from kolokvij import *

test_case = unittest.TestCase()
expected = [('AUS', 2017, 94.8),
            ('AUT', 2017, 90.0),
            ('BEL', 2017, 98.0),
            ('CAN', 2017, 91.0),
            ('CZE', 2017, 96.0)]
actual = preberi_podatke('cep2.txt')
test_case.assertEqual(expected, actual)
