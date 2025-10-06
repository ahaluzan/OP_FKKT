import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

test_case.assertFalse(trikotniska_neenakost(2, 8, 2), msg='trikotniska_neenakost(2, 8, 2) -> False')