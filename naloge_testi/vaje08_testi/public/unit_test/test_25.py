import unittest
from metode import *

test_case = unittest.TestCase()
test_case.assertEqual(ponavljajoci_znaki('Ljubljanica'), {('j', 2), ('a', 2)})