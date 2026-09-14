'''preberi_podatke'''
import unittest
from izpit import *

test_case = unittest.TestCase()
test_case.assertEqual(preberi_podatke(["public/data/slovenija.txt"]),
[['Bukovnik', None, 35, None, '1/1', 'Slovenija'],
 ['Celjska koča', None, 30, None, '2/3', 'Slovenija'],
 ['Cerkno', None, 140, None, '4/7', 'Slovenija'],
 ['Črna na Koroškem', 70, 70, 50, '1/1', 'Slovenija'],
 ['Golte', None, 115, None, '7/7', 'Slovenija'],
 ['Javornik', 60, 80, 30, '1/1', 'Slovenija'],
 ['Kope - Ribniško Pohorje', None, 80, None, '8/8', 'Slovenija'],
 ['Kranjska Gora', None, 80, None, '15/15', 'Slovenija'],
 ['Krvavec', None, 130, None, '7/13', 'Slovenija'],
 ['Mariborsko Pohorje', None, 30, None, '12/17', 'Slovenija'],
 ['Pokljuka - Goreljek', None, 180, None, '5/5', 'Slovenija'],
 ['Pokljuka - Zatrnik', 60, None, None, '2/2', 'Slovenija'],
 ['Poseka/Ravne', 30, 30, None, '1/1', 'Slovenija'],
 ['Ribniško Pohorje', None, 70, None, '3/4', 'Slovenija'],
 ['Rogla', None, 110, None, '12/12', 'Slovenija'],
 ['Rudno', None, 45, None, '1/1', 'Slovenija'],
 ['Šentjošt nad Horjulom', None, None, None, '2/2', 'Slovenija'],
 ['Soriška planina', None, 200, None, '3/5', 'Slovenija'],
 ['Trije Kralji', None, 65, None, '2/2', 'Slovenija'],
 ['Velika planina', None, 25, None, '4/4', 'Slovenija'],
 ['Vogel', None, 250, None, '4/9', 'Slovenija']]
)
