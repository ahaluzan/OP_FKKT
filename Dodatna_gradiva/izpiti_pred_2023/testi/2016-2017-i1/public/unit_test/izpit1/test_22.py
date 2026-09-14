import unittest
import izpit1



slovar = {'Brazilija': [109, 104], 'Islandija': [169, 179], 'Rusija': [119, 177], 'Španija': [109, 88], 'Slovenija': [230, 203], 'Egipt': [202, 179], 'Katar': [128, 146], 'Japonska': [176, 148], 'Angola': [166, 175], 'Tunizija': [239, 262], 'Norveška': [221, 234], 'Poljska': [249, 251], 'Francija': [149, 133], 'Makedonija': [242, 229]}
drzava = 'Slovenija'

test_case = unittest.TestCase()
test_case.assertEqual(izpit1.stevilo_zadetih_golov(slovar, drzava), 230)

