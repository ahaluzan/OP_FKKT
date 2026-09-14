import unittest
import naloge

test_case = unittest.TestCase()

expected = [(1946, 'Stylianos Kyriakides', 'Greece', 8967, 42.2),
(1909, 'Henri Renaud', 'United States', 10416, 39.4),
(1988, 'Rosa Mota', 'Portugal', 8670, 42.2),
(1910, 'Fred S. Cameron', 'Canada', 8932, 39.4),
(2001, 'Catherine Ndereba', 'Kenya', 8633, 42.2)]

datoteka = "data/boston_miss.csv"

actual = naloge.preberi_podatke(datoteka)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije v primeru manjkajocih podatkov.")