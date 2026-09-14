import unittest
from naloga3 import *

test_case = unittest.TestCase()
expected = {'11.1.2020', '13.1.2020', '12.1.2020', '14.1.2020'}
result = najhujsi_dan([("11.1.2020", 10), ("12.1.2020", 10), ("13.1.2020", 10), ("14.1.2020", 10)])
test_case.assertEqual(expected, result)
