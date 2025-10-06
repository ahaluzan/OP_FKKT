import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

test_case.assertTrue(samoglasnik("A"), msg='samoglasnik("A") -> True')
test_case.assertTrue(samoglasnik("E"), msg='samoglasnik("E") -> True')
test_case.assertTrue(samoglasnik("I"), msg='samoglasnik("I") -> True')
test_case.assertTrue(samoglasnik("O"), msg='samoglasnik("O") -> True')
test_case.assertTrue(samoglasnik("U"), msg='samoglasnik("U") -> True')