import unittest
import naloge

test_case = unittest.TestCase()

kms = [5, 7, 3, 9, 23, 1]
mins = [26, 40, 15, 67, 135, 3]

expected = [7.44, 5.37, 3.0]
actual = naloge.povprecni_tempo(kms, mins)

test_case.assertEqual(expected, actual, "Napaka v funkciji.")