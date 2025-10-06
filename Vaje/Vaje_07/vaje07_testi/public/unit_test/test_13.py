import unittest
from trgovina import *

zaloga = {'mleko': [0.86, 128], 'hrenovka': [1.99, 28], 'jogurt': [0.49, 56], 'sok': [1.79, 104],
          'moka': [1.39, 99], 'paradižnik': [0.23, 35], 'gorgonzola': [2.69, 32], 'makaroni': [1.89, 67],
          'kruh': [2.19, 43], 'piškoti': [2.99, 73], 'jajce': [0.1, 103]}


test_case = unittest.TestCase()
popravek = popravek_zaloge(zaloga, 'jogurt', -60)
test_case.assertEqual(popravek, None)
test_case.assertEqual(zaloga,
                      {'mleko': [0.86, 128], 'hrenovka': [1.99, 28], 'moka': [1.39, 99], 'sok': [1.79, 104],
                       'makaroni': [1.89, 67], 'kruh': [2.19, 43], 'jogurt': [0.49, 56], 'paradižnik': [0.23, 35],
                       'piškoti': [2.99, 73], 'gorgonzola': [2.69, 32], 'jajce': [0.1, 103]})