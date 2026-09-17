import unittest
import izpit


datoteka = 'public/data/piknik30.txt'
slovar = {'ncrue': (465, 248), 'kbcplfjo': (336, 119), 'hinpltf': (205, 42), 'ndjtfg': (123, 422), 'einlajo': (56, 407), 'cnzmsru': (312, 63), 'cgeuk': (285, 352), 'ipdmrju': (181, 370), 'nzstfgu': (348, 382), 'ehcdlztu': (470, 392), 'zasrgo': (408, 458), 'indcfo': (184, 479), 'khcasrfo': (493, 250), 'hilrju': (441, 263), 'nlamju': (494, 272), 'camjuk': (67, 435), 'oepui': (483, 35), 'amftjo': (383, 269), 'hcdztrjo': (97, 488), 'ndltfg': (133, 95), 'dlpmtfj': (59, 111), 'hciamsu': (139, 118), 'kehmfuo': (427, 75), 'ipsrjfu': (169, 25), 'bpmtrgk': (349, 91), 'eplmrftk': (457, 40), 'hcmruk': (159, 280), 'bhpasj': (391, 173), 'hdlzmsu': (243, 481), 'behamsgo': (136, 12)}


test_case = unittest.TestCase()
test_case.assertEqual(izpit.preberi(datoteka), slovar)