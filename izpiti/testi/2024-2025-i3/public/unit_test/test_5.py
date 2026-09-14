'''po_drzavah'''

import unittest
import naloge

test_case = unittest.TestCase()

podatki = [('5-Minute Crafts', 81.1, 7391, 27907581110, 'US'),
    ('UR.Cristiano', 71.7, 80, 721228815, 'PT'),
    ('Alfredo Larin', 46.0, 1831, 39518875780, 'SV'),
    ('MrBeast', 336.0, 838, 66853633536, 'US'),
    ('Stokes Twins', 102.0, 335, 16139307959, 'US')]

expected = {'US': [('5-Minute Crafts', 7391, 81.1, 27907581110),
    ('MrBeast', 838, 336.0, 66853633536),
    ('Stokes Twins', 335, 102.0, 16139307959)],
    'PT': [('UR.Cristiano', 80, 71.7, 721228815)],
    'SV': [('Alfredo Larin', 1831, 46.0, 39518875780)]}

actual = naloge.po_drzavah(podatki)

test_case.assertEqual(expected.keys(), actual.keys(), "Napacni kljuci slovarja.")