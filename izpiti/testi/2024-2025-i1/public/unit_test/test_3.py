import unittest
import naloge

test_case = unittest.TestCase()

expected = [('The Scientist', 'Coldplay', 2024, 2, 0.557, 0.11, 0.442, 309),
 ('Ronin', 'Hans Zimmer', 2003, 37, 0.207, 0.082, 0.077, 113),
 ('Open Your Heart', 'Madonna', 1986, 51, 0.624, 0.195, 0.951, 253),
 ('Antologia', 'Shakira', 2002, 56, 0.844, 0.095, 0.465, 251),
 ('Bad Blood', 'Taylor Swift', 2024, 7, 0.656, 0.201, 0.792, 211)]

actual = naloge.preberi_podatke("data/spotify_missing.txt")

test_case.assertEqual(len(expected), len(actual), "Neustrezno obravanavanje manjkajocih podatkov.")