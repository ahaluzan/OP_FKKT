import unittest
import naloga3

test_case = unittest.TestCase()
test_case.assertEqual(naloga3.lucasova_stevila(10000), [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364, 2207, 3571, 5778, 9349])
