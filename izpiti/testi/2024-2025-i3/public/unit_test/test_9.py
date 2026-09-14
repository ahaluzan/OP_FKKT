'''ratio'''

import unittest
import naloge

test_case = unittest.TestCase()

slovar = {'US': [('5-Minute Crafts', 7391, 81.1, 27907581110),
    ('MrBeast', 838, 336.0, 66853633536),
    ('Stokes Twins', 335, 102.0, 16139307959)],
    'PT': [('UR.Cristiano', 80, 71.7, 721228815)],
    'SV': [('Alfredo Larin', 1831, 46.0, 39518875780)]}

expected = [('5-Minute Crafts', 344.1), ('MrBeast', 199.0), ('Stokes Twins', 158.2)]

actual = naloge.ratio(slovar, "US")

test_case.assertEqual(type(expected[0]), type(actual[0]), "Napacen podatkovni tip v seznamu.")