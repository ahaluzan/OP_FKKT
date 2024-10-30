import unittest
from trgovina import *

zaloga = {'mleko': [0.86, 128], 'hrenovka': [1.99, 28], 'jogurt': [0.49, 56], 'sok': [1.79, 104],
          'moka': [1.39, 99], 'paradižnik': [0.23, 35], 'gorgonzola': [2.69, 32], 'makaroni': [1.89, 67],
          'kruh': [2.19, 43], 'piškoti': [2.99, 73], 'jajce': [0.1, 103]}

slovar_nakupov =  {'jogurt': 3, 'mleko': 1, 'makaroni': 3, 'piškoti': 1, 'hrenovka': 4, 'moka': 6}


test_case = unittest.TestCase()
popravek = blagajna(zaloga, slovar_nakupov)
test_case.assertEqual(round(popravek, 2), 27.29)
test_case.assertEqual(zaloga,
                      {'mleko': [0.86, 127], 'hrenovka': [1.99, 24], 'moka': [1.39, 93], 'sok': [1.79, 104],
                       'makaroni': [1.89, 64], 'kruh': [2.19, 43], 'jogurt': [0.49, 53], 'paradižnik': [0.23, 35],
                       'piškoti': [2.99, 72], 'gorgonzola': [2.69, 32], 'jajce': [0.1, 103]})