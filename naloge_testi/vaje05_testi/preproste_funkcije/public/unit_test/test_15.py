'''samoglasniki'''
import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

test_case.assertTrue(samoglasnik("a"), msg='samoglasnik("a") -> True')
test_case.assertTrue(samoglasnik("e"), msg='samoglasnik("e") -> True')
test_case.assertTrue(samoglasnik("i"), msg='samoglasnik("i") -> True')
test_case.assertTrue(samoglasnik("o"), msg='samoglasnik("o") -> True')
test_case.assertTrue(samoglasnik("u"), msg='samoglasnik("u") -> True')