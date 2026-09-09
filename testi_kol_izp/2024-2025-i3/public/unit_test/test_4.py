import unittest
import naloge

test_case = unittest.TestCase()

expected = [('5-Minute Crafts', 81.1, 7391, 27907581110, 'US'),
    ('UR.Cristiano', 71.7, 80, 721228815, 'PT'),
    ('Alfredo Larin', 46.0, 1831, 39518875780, 'SV'),
    ('MrBeast', 336.0, 838, 66853633536, 'US'),
    ('Stokes Twins', 102.0, 335, 16139307959, 'US')]

actual = naloge.preberi_podatke("data/youtube5.txt")

test_case.assertEqual(expected, actual, "Napacna vsebina seznama.")

