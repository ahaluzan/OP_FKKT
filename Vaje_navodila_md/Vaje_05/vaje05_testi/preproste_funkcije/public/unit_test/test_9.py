'''trikotniska_neenakost'''
import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

test_case.assertTrue(trikotniska_neenakost(3, 4, 5), msg='trikotniska_neenakost(3, 4, 5) -> True')