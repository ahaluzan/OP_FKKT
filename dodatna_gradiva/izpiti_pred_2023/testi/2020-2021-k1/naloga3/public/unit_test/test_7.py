import unittest
from naloga3 import *

test_case = unittest.TestCase()
expected = '11.1.2020'
result = najhujsi_dan([("11.1.2020", 101), ("12.1.2020", 99), ("13.1.2020", 100),
                       ("14.1.2020", 99), ("15.1.2020", 99), ("16.1.2020", 100),
                       ])
test_case.assertEqual(expected, result)
