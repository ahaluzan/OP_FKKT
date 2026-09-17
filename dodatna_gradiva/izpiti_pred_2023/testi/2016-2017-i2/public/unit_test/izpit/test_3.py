import unittest
import izpit


datoteka = 'public/data/piknik50.txt'
slovar = {'ojbltc': (218, 379), 'jmibgduf': (87, 293), 'omshtkc': (189, 224), 'oabnrtez': (388, 121), 'ishgekc': (449, 445), 'ojbhduk': (404, 283), 'jmpgrtf': (246, 216), 'jmsgdrz': (161, 30), 'isndlc': (172, 437), 'sbgdzue': (52, 317), 'ompzre': (484, 10), 'jmnztk': (103, 481), 'pndzkf': (273, 183), 'manhdekc': (372, 66), 'ilafu': (164, 21), 'oisnrze': (4, 302), 'jmasrc': (382, 383), 'miasngdu': (4, 472), 'jmpastec': (490, 203), 'iabsnt': (472, 247), 'oiblzk': (118, 286), 'jpngdte': (68, 490), 'jpasglk': (264, 94), 'angdzk': (464, 350), 'jmsgru': (80, 98), 'jgdlute': (124, 192), 'bhdtec': (250, 133), 'jmisnhec': (56, 488), 'igdlztc': (385, 433), 'onhrzu': (381, 167), 'adlrtek': (461, 181), 'jipablru': (243, 411), 'mibhdzt': (476, 251), 'ohzteu': (288, 90), 'mhgruec': (146, 48), 'pisbdlec': (350, 218), 'kgjnh': (6, 72), 'mpbsdzc': (415, 245), 'paztef': (18, 98), 'bhglzuc': (274, 34), 'isnhdzu': (374, 61), 'jmastekc': (356, 400), 'jpuekf': (116, 466), 'abngdzt': (228, 486), 'omishtu': (466, 454), 'ikjrm': (90, 212), 'abshrte': (74, 90), 'jnrtzu': (274, 206), 'ojgruek': (307, 444), 'omshgze': (228, 24)}

test_case = unittest.TestCase()
test_case.assertEqual(izpit.preberi(datoteka), slovar)