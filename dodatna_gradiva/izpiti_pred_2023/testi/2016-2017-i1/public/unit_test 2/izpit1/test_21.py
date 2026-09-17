'''stevilo_zadetih_golov'''
import unittest
import izpit1



slovar = {'Angola': [122, 191], 'Slovenija': [271, 253], 'Rusija': [165, 169], 'Katar': [178, 181], 'Hrvaška': [254, 233], 'Brazilija': [148, 174], 'Egipt': [157, 164], 'Francija': [283, 218], 'Argentina': [108, 137], 'Japonska': [120, 161], 'Čile': [122, 160], 'Madžarska': [202, 194], 'Tunizija': [144, 144], 'Bahrajn': [110, 152], 'Poljska': [115, 125], 'Španija': [217, 172], 'Norveška': [274, 234], 'Savdska Arabija': [123, 157], 'Danska': [182, 157], 'Belorusija': [156, 186], 'Nemčija': [179, 128], 'Švedska': [233, 166], 'Makedonija': [163, 171], 'Islandija': [153, 152]}
drzava = 'Slovenija'

test_case = unittest.TestCase()
test_case.assertEqual(izpit1.stevilo_zadetih_golov(slovar, drzava), 271)

