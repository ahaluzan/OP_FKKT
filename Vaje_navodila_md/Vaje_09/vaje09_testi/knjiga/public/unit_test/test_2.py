'''razlicni_znaki'''
import unittest
from knjiga import *



test_case = unittest.TestCase()
test_case.assertEqual(razlicni_znaki('OliverTwist.txt'), 70)
