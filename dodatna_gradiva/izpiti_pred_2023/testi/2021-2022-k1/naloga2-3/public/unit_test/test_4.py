'''v_visine'''
import unittest

from naloge import *

test_case = unittest.TestCase()
expected = [('1/1/2022', 's', 25.0, -5), ('2/1/2022', 's', 25.0, -5), ('3/1/2022', None, 0, -5),
            ('4/1/2022', 's', 2.875, -0.5), ('5/1/2022', 'd', 10, -0.5)]
arg = [('1/1/2022', 's', 10, -5), ('2/1/2022', 's', 10, -5), ('3/1/2022', None, 0, -5), ('4/1/2022', 's', 2.5, -0.5),
       ('5/1/2022', 'd', 10, -0.5)]
result = v_visine(arg)
test_case.assertEqual(expected, result)
