import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

test_case.assertFalse(samoglasnik("0"), msg='samoglasnik("0") -> False')
test_case.assertFalse(samoglasnik("2"), msg='samoglasnik("2") -> False')
test_case.assertFalse(samoglasnik("."), msg='samoglasnik(".") -> False')
test_case.assertFalse(samoglasnik("!"), msg='samoglasnik("!") -> False')