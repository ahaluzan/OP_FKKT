import unittest
import naloge

test_case = unittest.TestCase()

kms = [5, 10, 21.1, 42.2]
mins = [25, 50, 110, 240]

expected = [5.69, 5.22, 5.0]
actual = naloge.povprecni_tempo(kms, mins)

test_case.assertEqual(len(expected), len(actual), "Neustrezno stevilo elementov v seznamu.")