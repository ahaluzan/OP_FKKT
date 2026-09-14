import unittest
import naloge

test_case = unittest.TestCase()

kms = [5, 7, 3, 9]
mins = [25, 45, 10, 65]

expected = [7.22, 5.5, 3.33]
actual = naloge.povprecni_tempo(kms, mins)

test_case.assertEqual(expected, actual, "Napaka v funkciji.")