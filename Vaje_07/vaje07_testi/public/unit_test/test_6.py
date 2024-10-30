'''nakupovalna_kosara'''
import unittest
from trgovina import *

seznam = ['jogurt', 'mleko', 'jogurt', 'jogurt', 'piškoti']

test_case = unittest.TestCase()
test_case.assertEqual(nakupovalna_kosara(seznam), {'jogurt': 3, 'mleko': 1, 'piškoti': 1})
