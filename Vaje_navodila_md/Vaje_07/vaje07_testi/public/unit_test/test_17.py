import unittest
from trgovina import *

zaloga = {'mleko': [0.86, 128], 'hrenovka': [1.99, 28], 'jogurt': [0.49, 56], 'sok': [1.79, 104],
          'moka': [1.39, 99], 'paradižnik': [0.23, 35], 'gorgonzola': [2.69, 32], 'makaroni': [1.89, 67],
          'kruh': [2.19, 43], 'piškoti': [2.99, 73], 'jajce': [0.1, 103]}

jedi = {
    "palačinke": {"jajce": 3, "mleko": 1, "moka": 1},
    "šmorn": {"jajce": 3, "mleko": 1, "moka": 1},
    "hrenovke": {"hrenovka": 2, "kruh": 1},
    "makaroni": {"makaroni": 1, "paradižnik": 3, "gorgonzola": 1},
    "piškoti": {"piškoti": 1}
}


test_case = unittest.TestCase()
test_case.assertEqual(round(kuhanje(zaloga, jedi, 'makaroni'), 2), 5.27)
