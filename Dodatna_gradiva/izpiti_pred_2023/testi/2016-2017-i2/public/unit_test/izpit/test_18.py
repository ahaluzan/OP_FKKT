import unittest
import izpit

ime = 'Pod skalco'
slovar = {'Star maln': (156, 428), 'Logar': (322, 210), 'Gaj': (306, 139), 'Skedenj': (123, 325), 'Stara žaga': (381, 494), 'Kozolc': (298, 128), 'Gril': (35, 401), 'Ranč': (363, 402), 'Park Jasa': (378, 352), 'Rušta': (54, 35), 'Pod kačjo smreko': (50, 18), 'Pod skalco': (392, 276), 'Mala Loka': (386, 333), 'Pri Kovaču': (392, 356), 'Terra Botanica': (104, 381), 'Kleče': (432, 65), 'Kraljev hrib': (233, 363), 'Jezero': (204, 423), 'Zelenica': (426, 32), 'Kos': (18, 145), 'Vitez': (190, 235), 'Sidro': (116, 281)}


test_case = unittest.TestCase()
test_case.assertEqual(izpit.najblizji(slovar, ime), 'Mala Loka')

