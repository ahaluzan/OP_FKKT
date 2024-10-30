import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

test_case.assertFalse(samoglasnik("f"), msg='samoglasnik("f") -> False')
test_case.assertFalse(samoglasnik("b"), msg='samoglasnik("b") -> False')
test_case.assertFalse(samoglasnik("y"), msg='samoglasnik("y") -> False')
test_case.assertFalse(samoglasnik("w"), msg='samoglasnik("w") -> False')
test_case.assertFalse(samoglasnik("C"), msg='samoglasnik("C") -> False')
test_case.assertFalse(samoglasnik("M"), msg='samoglasnik("M") -> False')
test_case.assertFalse(samoglasnik("Y"), msg='samoglasnik("Y") -> False')
test_case.assertFalse(samoglasnik("W"), msg='samoglasnik("W") -> False')