'''stevilo_besed'''
import unittest
from knjiga import *



test_case = unittest.TestCase()
test_case.assertEqual(stevilo_besed('OliverTwist.txt'), 158041)
