'''hapax'''
import unittest
from knjiga import *



test_case = unittest.TestCase()
test_case.assertEqual(hapax('OliverTwist.txt'), 11851)
