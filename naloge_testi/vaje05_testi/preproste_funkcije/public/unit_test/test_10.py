import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

test_case.assertTrue(trikotniska_neenakost(24, 43, 50), msg='trikotniska_neenakost(24, 43, 50) -> True')