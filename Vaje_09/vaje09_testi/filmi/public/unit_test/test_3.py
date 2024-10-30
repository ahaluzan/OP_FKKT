'''v_slovar'''
import unittest
from filmi import *

test_case = unittest.TestCase()
expected = {'Romantična drama': ['Titanic'], 'Kriminalka': ['The Godfather'],
                       'Akcija': ['Gladiator', 'Saving Private Ryan'], 'Drama': ["Schindler's List", 'Casablanca'],
                       'Komedija': ['Forrest Gump'], 'Glasbena biografija': ['The Sound of Music']}

test_case.assertEqual(v_slovar('podatki/filmi.txt'), expected)