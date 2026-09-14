import unittest
import naloge

test_case = unittest.TestCase()

podatki = [(1946, 'Stylianos Kyriakides', 'Greece', 8967, 42.2),
 (1909, 'Henri Renaud', 'United States', 10416, 39.4),
 (1979, 'Joan Benoit', 'United States', 9315, 42.2),
 (1910, 'Fred S. Cameron', 'Canada', 8932, 39.4),
 (2001, 'Catherine Ndereba', 'Kenya', 8633, 42.2)]

expected = {(1909, 'Henri Renaud', 10416),
 (1910, 'Fred S. Cameron', 8932),
 (1946, 'Stylianos Kyriakides', 8967),
 (1979, 'Joan Benoit', 9315),
 (2001, 'Catherine Ndereba', 8633)}

actual = set(list(t for v in naloge.v_slovar(podatki).values() for t in v))

test_case.assertEqual(expected, actual, "Napacne vrednosti.")