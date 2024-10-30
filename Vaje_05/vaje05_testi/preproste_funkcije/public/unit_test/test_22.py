'''prekrivajoca_seznama'''
import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

test_case.assertTrue(prekrivajoca_seznama(['Ana', 'Peter', 'Miha'], ['Matej', 'Eva', 'Ana']), msg="prekrivajoca_seznama(['Ana', 'Peter', 'Miha'], ['Matej', 'Eva', 'Ana']) -> True")