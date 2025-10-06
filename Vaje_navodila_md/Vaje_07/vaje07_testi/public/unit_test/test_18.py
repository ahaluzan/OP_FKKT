'''posamezna_jed'''
import unittest
from copy import deepcopy
from trgovina import *

jedi = {
    "palačinke": {"jajce": 3, "mleko": 1, "moka": 1},
    "šmorn": {"jajce": 3, "mleko": 1, "moka": 1},
    "hrenovke": {"hrenovka": 2, "kruh": 1},
    "makaroni": {"makaroni": 1, "paradižnik": 3, "gorgonzola": 1},
    "piškoti": {"piškoti": 1}
}

jedi_original = deepcopy(jedi)

test_case = unittest.TestCase()
test_case.assertEqual(posamezna_jed(jedi, 'šmorn', 4),
                      {'moka': 4, 'mleko': 4, 'jajce': 12})


test_case.assertEqual(jedi, jedi_original, msg='Slovar jedi se sme spremeniti.')
