import unittest
from trgovina import *

seznam = ['jogurt', 'moka', 'moka', 'moka', 'hrenovka', 'makaroni', 'mleko', 'hrenovka', 'jogurt', 'moka', 'moka',
          'moka', 'makaroni', 'jogurt', 'piškoti', 'hrenovka', 'makaroni', 'hrenovka']

test_case = unittest.TestCase()
test_case.assertEqual(nakupovalna_kosara(seznam),
                      {'jogurt': 3, 'mleko': 1, 'makaroni': 3, 'piškoti': 1, 'hrenovka': 4, 'moka': 6})