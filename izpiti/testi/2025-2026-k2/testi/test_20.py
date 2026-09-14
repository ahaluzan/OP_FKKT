import unittest
import naloge

test_case = unittest.TestCase()

podatki = [(1946, 'Stylianos Kyriakides', 'Greece', 8967, 42.2),
 (2010, 'Teyba Erkesso', 'Ethiopia', 8771, 42.2),
 (1909, 'Henri Renaud', 'United States', 10416, 39.4),
 (1979, 'Joan Benoit', 'United States', 9315, 42.2),
 (1910, 'Fred S. Cameron', 'Canada', 8932, 39.4),
 (2001, 'Catherine Ndereba', 'Kenya', 8633, 42.2),
 (2008, 'Dire Tune', 'Ethiopia', 8725, 42.2),
 (2009, 'Salina Kosgei', 'Kenya', 9136, 42.2),
 (2011, 'Caroline Kilel', 'Kenya', 8556, 42.2),
 (2012, 'Sharon Cherop', 'Kenya', 9110, 42.2)]

expected = {'Greece': [(1946, 'Stylianos Kyriakides', 8967)],
 'Ethiopia': [(2010, 'Teyba Erkesso', 8771), (2008, 'Dire Tune', 8725)],
 'United States': [(1979, 'Joan Benoit', 9315)],
 'Kenya': [(2001, 'Catherine Ndereba', 8633),
  (2009, 'Salina Kosgei', 9136),
  (2011, 'Caroline Kilel', 8556),
  (2012, 'Sharon Cherop', 9110)]}

actual = naloge.v_slovar(podatki, kilometri = 42.2)

test_case.assertEqual(expected, actual, "Napacna izvedba funkcije pri uporabi opcijskega argumenta.")