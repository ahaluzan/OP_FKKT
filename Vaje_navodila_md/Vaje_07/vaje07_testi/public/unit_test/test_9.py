'''cena'''
import unittest
from trgovina import *

zaloga = {'mleko': [0.86, 128], 'hrenovka': [1.99, 28], 'jogurt': [0.49, 56], 'sok': [1.79, 104],
          'moka': [1.39, 99], 'paradižnik': [0.23, 35], 'gorgonzola': [2.69, 32], 'makaroni': [1.89, 67],
          'kruh': [2.19, 43], 'piškoti': [2.99, 73], 'jajce': [0.1, 103]}

slovar_nakupov =  {'jogurt': 3, 'mleko': 1, 'piškoti': 1}

test_case = unittest.TestCase()
test_case.assertEqual(round(cena(zaloga, slovar_nakupov), 2), 5.32)
