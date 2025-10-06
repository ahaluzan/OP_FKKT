import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

test_case.assertFalse(prekrivajoca_seznama([1, 2, 3], [4, 5, 6]), msg='prekrivajoca_seznama([1, 2, 3], [4, 5, 6]) -> False')
test_case.assertTrue(prekrivajoca_seznama([8, 3, 1], [2, 4, 1]), msg='prekrivajoca_seznama([8, 3, 1], [2, 4, 1]) -> True')