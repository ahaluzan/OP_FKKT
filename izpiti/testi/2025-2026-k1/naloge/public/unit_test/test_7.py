import unittest
import naloge

test_case = unittest.TestCase()

kms = [5, 42.2]
mins = [25, 240]

expected = []
actual = naloge.povprecni_tempo(kms, mins)

test_case.assertEqual(expected, actual, "Neustrezno obravnavanje prekratkih seznamov.")