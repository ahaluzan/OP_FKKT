'''dolzina_zasnezeno'''
import unittest
from izpit import *

test_case = unittest.TestCase()
test_case.assertEqual(dolzina_zasnezeno([0, 0, 0, 0, 0, 30, 35, 35, 35, 30, 30, 25, 20, 15, 5, 0, 0, 0, 45, 50, 70, 70, 70, 65, 80, 80, 75, 60, 45, 35, 30, 20, 15, 10, 5, 5, 5, 0, 0, 0, 0, 10, 10, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 25, 25, 20, 20, 10, 10]), 14)

