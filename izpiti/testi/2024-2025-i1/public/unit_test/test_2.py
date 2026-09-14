import unittest
import naloge

test_case = unittest.TestCase()

expected = [('Right As Rain', 'Adele', 2008, 54, 0.842, 0.089, 0.679, 197),
 ('One Way Street', 'Aerosmith', 1973, 41, 0.457, 0.115, 0.834, 422),
 ('Sweet Emotion', 'Aerosmith', 1975, 75, 0.379, 0.104, 0.76, 274),
 ('Party', 'Alan Silvestri', 1991, 1, 0.469, 0.121, 0.383, 337),
 ('Canyons', 'Avicii', 2013, 35, 0.663, 0.613, 0.682, 449)]

actual = naloge.preberi_podatke("data/spotify5.txt")

test_case.assertEqual(expected, actual, "Vsebina seznama ni ustrezna.")