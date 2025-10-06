import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

test_case.assertFalse(trikotniska_neenakost(2, 3, 8), msg='trikotniska_neenakost(2, 3, 8) -> False')