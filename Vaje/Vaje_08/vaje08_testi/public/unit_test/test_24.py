'''ponavljajoci_znaki'''
import unittest
from metode import *

test_case = unittest.TestCase()
test_case.assertEqual(ponavljajoci_znaki('otorinolaringologija'),{('l', 2), ('i', 3), ('r', 2), ('a', 2), ('g', 2), ('o', 5), ('n', 2)})