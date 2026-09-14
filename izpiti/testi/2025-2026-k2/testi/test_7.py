import unittest
import naloge

test_case = unittest.TestCase()

expected = [(1946, 'Stylianos Kyriakides', 'Greece', 8967, 42.2),
 (2010, 'Teyba Erkesso', 'Ethiopia', 8771, 42.2),
 (1909, 'Henri Renaud', 'United States', 10416, 39.4),
 (1979, 'Joan Benoit', 'United States', 9315, 42.2),
 (1910, 'Fred S. Cameron', 'Canada', 8932, 39.4),
 (2001, 'Catherine Ndereba', 'Kenya', 8633, 42.2),
 (2008, 'Dire Tune', 'Ethiopia', 8725, 42.2),
 (2009, 'Salina Kosgei', 'Kenya', 9136, 42.2),
 (2011, 'Caroline Kilel', 'Kenya', 8556, 42.2),
 (2012, 'Sharon Cherop', 'Kenya', 9110, 42.2)]

datoteka = "data/boston10.csv"

actual = naloge.preberi_podatke(datoteka)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")