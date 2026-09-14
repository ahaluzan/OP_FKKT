'''sneg_v_mesecu'''
import unittest

from naloge import *

test_case = unittest.TestCase()
expected = 42.5
vreme = [('27/12/2021', 's', 40, -5),
         ('28/12/2021', 's', 10, -5),
         ('29/12/2021', None, 0, -5),
         ('30/12/2021', None, 0, -0.5),
         ('31/12/2021', None, 0, -0.5),
         ('1/1/2022', 's', 20, -5),
         ('2/1/2022', 's', 20, -5),
         ('3/1/2022', None, 0, -5),
         ('4/1/2022', 's', 2.5, -0.5),
         ('5/1/2022', 'd', 10, -0.5)]
result = sneg_v_mesecu(vreme, 1)
test_case.assertAlmostEqual(expected, result, 5)
