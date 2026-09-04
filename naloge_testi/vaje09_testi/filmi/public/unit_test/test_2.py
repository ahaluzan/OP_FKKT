'''v_seznam'''
import unittest
from filmi import *

test_case = unittest.TestCase()
expected = [['The Godfather', 9.2, 'Kriminalka', 1972], ["Schindler's List", 8.9, 'Drama', 1993],
                       ['Casablanca', 8.6, 'Drama', 1942], ['Forrest Gump', 8.8, 'Komedija', 1994],
                       ['The Sound of Music', 8.0, 'Glasbena biografija', 1965], ['Gladiator', 8.5, 'Akcija', 2000],
                       ['Titanic', 7.7, 'Romantična drama', 1997], ['Saving Private Ryan', 8.6, 'Akcija', 1998]]

test_case.assertEqual(v_seznam('podatki/filmi.txt'), expected)