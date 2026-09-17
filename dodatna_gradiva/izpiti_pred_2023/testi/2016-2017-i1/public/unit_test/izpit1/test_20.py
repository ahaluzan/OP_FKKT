import unittest
import izpit1


datoteka = 'public/data/rezultati500.csv'
slovar = {'Japonska': [1579, 1642], 'Norveška': [1821, 1867], 'Španija': [1517, 1441], 'Egipt': [1927, 1844], 'Slovenija': [1972, 2051], 'Brazilija': [1983, 2029], 'Tunizija': [1945, 1963], 'Francija': [1788, 1749], 'Makedonija': [1528, 1460], 'Islandija': [1657, 1657], 'Katar': [1963, 1993], 'Poljska': [1737, 1780], 'Angola': [1836, 1797], 'Rusija': [2060, 2040]}

test_case = unittest.TestCase()
test_case.assertEqual(izpit1.preberi(datoteka), slovar)

