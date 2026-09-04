'''nabava'''
import unittest
from trgovina import *

jedi = {
    "palačinke": {"jajce": 3, "mleko": 1, "moka": 1},
    "šmorn": {"jajce": 3, "mleko": 1, "moka": 1},
    "hrenovke": {"hrenovka": 2, "kruh": 1},
    "makaroni": {"makaroni": 1, "paradižnik": 3, "gorgonzola": 1},
    "piškoti": {"piškoti": 1}
}

obroki = [("makaroni", 20), ("palačinke", 15), ("šmorn", 10), ("hrenovke", 5)]


test_case = unittest.TestCase()
test_case.assertEqual(nakup(jedi, obroki),
                      {'paradižnik': 60, 'gorgonzola': 20, 'moka': 25, 'kruh': 5, 'hrenovka': 10, 'jajce': 75,
                       'makaroni': 20, 'mleko': 25})
