import unittest
import naloge

test_case = unittest.TestCase()

podatki = [(1946, 'Stylianos Kyriakides', 'Greece', 8967, 42.2),
 (1909, 'Henri Renaud', 'United States', 10416, 39.4),
 (1979, 'Joan Benoit', 'United States', 9315, 42.2),
 (1910, 'Fred S. Cameron', 'Canada', 8932, 39.4),
 (2001, 'Catherine Ndereba', 'Kenya', 8633, 42.2)]

expected = True #{'Canada', 'United States', 'Kenya', 'Greece'}

#actual = naloge.v_slovar(podatki)

actual = all(isinstance(k,list) for k in naloge.v_slovar(podatki).values()) and all(isinstance(t,tuple) for v in naloge.v_slovar(podatki).values() for t in v)

test_case.assertEqual(expected, actual, "Vrednosti so napacnega podatkovnega tipa.")