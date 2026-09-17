import unittest

from naloge import *

test_case = unittest.TestCase()
expected = [('1/1/2022', 'd', 25.0, -5), ('2/1/2022', 'd', 25.0, -5), ('3/1/2022', None, 0, -5),
            ('4/1/2022', 'd', 2.875, -0.5), ('5/1/2022', 'd', 10, -0.5)]
arg = expected
result = v_visine(arg)
test_case.assertEqual(expected, result)
