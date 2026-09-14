import unittest
import izpit1



slovar = {'Makedonija': [869, 861], 'Francija': [661, 596], 'Rusija': [734, 694], 'Poljska': [759, 769], 'Angola': [724, 768], 'Katar': [720, 691], 'Japonska': [533, 544], 'Španija': [671, 684], 'Egipt': [910, 898], 'Brazilija': [519, 546], 'Islandija': [668, 716], 'Tunizija': [733, 671], 'Norveška': [644, 652], 'Slovenija': [668, 723]}
drzava = 'Slovenija'

test_case = unittest.TestCase()
test_case.assertEqual(izpit1.stevilo_zadetih_golov(slovar, drzava), 668)

