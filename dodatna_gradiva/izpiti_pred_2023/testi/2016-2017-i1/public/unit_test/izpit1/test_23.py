import unittest
import izpit1



slovar = {'Španija': [344, 311], 'Brazilija': [332, 346], 'Angola': [345, 346], 'Tunizija': [351, 376], 'Poljska': [350, 319], 'Slovenija': [228, 272], 'Egipt': [470, 468], 'Francija': [309, 293], 'Islandija': [366, 446], 'Katar': [287, 302], 'Rusija': [368, 358], 'Makedonija': [433, 444], 'Norveška': [327, 260], 'Japonska': [321, 290]}
drzava = 'Slovenija'

test_case = unittest.TestCase()
test_case.assertEqual(izpit1.stevilo_zadetih_golov(slovar, drzava), 228)

