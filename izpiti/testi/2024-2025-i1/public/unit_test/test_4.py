import unittest
import naloge

test_case = unittest.TestCase()

expected = [('Hometown Glory', 'Adele', 2008, 61, 0.436, 0.102, 0.336, 271),
 ('Melt My Heart to Sto...', 'Adele', 2008, 53, 0.353, 0.215, 0.388, 203),
 ("You'll Be Queen One ...",'Ramin Djawadi',2011,40,0.279,0.083,0.006,95),
 ('Victory Does Not Mak...','Ramin Djawadi',2011,38,0.125,0.103,0.021,96),
 ('Vigilante Shit', 'Taylor Swift', 2023, 66, 0.867, 0.118, 0.272, 164)]

actual = naloge.preberi_podatke("data/spotify_long.txt")

test_case.assertEqual(expected, actual, "Napacno obravnavanje dolgih naslovov skladb.")

