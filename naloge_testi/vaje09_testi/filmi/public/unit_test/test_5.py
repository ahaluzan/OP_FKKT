'''zapis'''
import unittest
from filmi import *

test_case = unittest.TestCase()
expected = "Casablanca\n\
Forrest Gump\n\
Gladiator\n\
Saving Private Ryan\n\
Schindler's List\n\
The Godfather\n\
The Sound of Music\n\
Titanic\n"

zapis('podatki/filmi.txt', 'podatki/imena_filmov.txt')
test_case.assertEqual(preberi('podatki/imena_filmov.txt'), expected)