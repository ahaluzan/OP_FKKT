import unittest
import naloge

test_case = unittest.TestCase()

kms = [5, 7, 3, 9, 23, 1, 8, 25, 30, 14]
mins = [26, 40, 15, 67, 135, 4, 70, 120, 150, 60]

expected = [8.75, 5.61, 4.0]
actual = naloge.povprecni_tempo(kms, mins)

test_case.assertEqual(expected, actual, "Napaka v funkciji.")