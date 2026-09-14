import unittest
import naloge

test_case = unittest.TestCase()

expected = [(1946, 'Stylianos Kyriakides', 'Greece', 8967, 42.2),
 (1909, 'Henri Renaud', 'United States', 10416, 39.4),
 (1979, 'Joan Benoit', 'United States', 9315, 42.2),
 (1910, 'Fred S. Cameron', 'Canada', 8932, 39.4),
 (2001, 'Catherine Ndereba', 'Kenya', 8633, 42.2)]

time_exp = set([8967, 10416, 9315, 8932, 8633])

datoteka = "data/boston5.csv"

actual = naloge.preberi_podatke(datoteka)

time_act = set()
for terka in actual:
    time_act.add(terka[-2])

test_case.assertEqual(time_exp, time_act, "Napacna pretvorba casa. Preverite tudi formulo: 3600*ure + 60*minute + sekunde")