'''preberi'''
import unittest
from filmi import *

test_case = unittest.TestCase()
expected = "The Godfather;9.2;Kriminalka;1972\n\
Schindler's List;8.9;Drama;1993\n\
Casablanca;8.6;Drama;1942\n\
Forrest Gump;8.8;Komedija;1994\n\
The Sound of Music;8.0;Glasbena biografija;1965\n\
Gladiator;8.5;Akcija;2000\n\
Titanic;7.7;Romantična drama;1997\n\
Saving Private Ryan;8.6;Akcija;1998"

test_case.assertEqual(preberi('podatki/filmi.txt'), expected)