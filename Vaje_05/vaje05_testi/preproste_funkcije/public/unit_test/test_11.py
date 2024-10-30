import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

test_case.assertFalse(trikotniska_neenakost(20, 7, 5), msg='trikotniska_neenakost(20, 7, 5) -> False')