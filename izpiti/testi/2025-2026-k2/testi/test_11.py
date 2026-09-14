"v_slovar"
import unittest
import naloge

test_case = unittest.TestCase()

podatki = [(1946, 'Stylianos Kyriakides', 'Greece', 8967, 42.2),
 (1909, 'Henri Renaud', 'United States', 10416, 39.4),
 (1979, 'Joan Benoit', 'United States', 9315, 42.2),
 (1910, 'Fred S. Cameron', 'Canada', 8932, 39.4),
 (1979, 'Joan Benoit', 'United States', 9315, 42.2)]

expected = True #{'Canada', 'United States', 'Kenya', 'Greece'}

#actual = naloge.v_slovar(podatki)

actual = all(isinstance(k,str) for k in naloge.v_slovar(podatki))

test_case.assertEqual(expected, actual, "Kljuci so napacnega podatkovnega tipa.")