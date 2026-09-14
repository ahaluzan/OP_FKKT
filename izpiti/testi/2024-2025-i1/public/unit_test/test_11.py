import unittest
import naloge

test_case = unittest.TestCase()

podatki = [('Material Girl', 'Madonna', 1984, 58, 0.775, 0.051, 0.616, 240),
           ('Right As Rain', 'Adele', 2008, 54, 0.842, 0.089, 0.679, 197),
           ('Hometown Glory', 'Adele', 2008, 61, 0.436, 0.102, 0.336, 271),
           ('Sweet Emotion', 'Aerosmith', 1975, 75, 0.379, 0.104, 0.76, 274),
           ('Party', 'Alan Silvestri', 1991, 1, 0.469, 0.121, 0.383, 337),
           ('Canyons', 'Avicii', 2013, 35, 0.663, 0.613, 0.682, 449),
           ('California King Bed', 'Rihanna', 2010, 48, 0.475, 0.121, 0.577, 251),
           ('Man Down', 'Rihanna', 2010, 42, 0.465, 0.049, 0.909, 267),
           ('The Scientist', 'Coldplay', 2024, 1, 0.557, 0.11, 0.442, 309)]

expected = {'Madonna': 0.78, 'Coldplay': 0.56, 'Queen': 0}

actual = naloge.tocke(podatki, ["Madonna", "Coldplay", "Queen"])

test_case.assertEqual(expected, actual, "Napacna vsebina slovarja, ko izbranega izvajalca iz seznama ni v podatkih.")