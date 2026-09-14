import unittest
import naloge

test_case = unittest.TestCase()

kms = [5, 10, 21.1, 42.2]
mins = [25, 50, 240]

expected = []
actual = naloge.povprecni_tempo(kms, mins)

test_case.assertEqual(len(expected), len(actual), "Napacno vracanje pri razlicni dolzini seznamov.")
