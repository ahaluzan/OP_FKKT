import unittest
from izpit import *

test_case = unittest.TestCase()

podatki = {'HUBER Daniel': 182.7,
 'EISENBICHLER Markus': 189.0,
 'TAKEUCHI Taku': 152.1,
 'KRANJEC Robert': 185.5,
 'FETTNER Manuel': 162.4,
 'NAGLIC Tomaz': 193.9,
 'KASAI Noriaki': 206.5,
 'KOZISEK Cestmir': 165.2,
 'AMMANN Simon': 183.7,
 'BICKNER Kevin': 182.4,
 'SEMENIC Anze': 199.1,
 'STJERNEN Andreas': 200.2,
 'FREITAG Richard': 202.1,
 'HULA Stefan': 179.8,
 'KORNILOV Denis': 178.0,
 'GRANERUD Halvor Egner': 188.1,
 'KOT Maciej': 174.9,
 'SCHLIERENZAUER Gregor': 186.3,
 'FORFANG Johann Andre': 214.2,
 'WOLNY Jakub': 175.6,
 'KOBAYASHI Ryoyu': 198.7,
 'PREVC Cene': 145.9,
 'PASCHKE Pius': 175.8,
 'KOBAYASHI Junshiro': 208.2,
 'LEYHE Stephan': 184.8,
 'WANK Andreas': 183.7,
 'FANNEMEL Anders': 204.9,
 'INSAM Alex': 163.6,
 'LINDVIK Marius': 170.0,
 'KRAFT Stefan': 213.2,
 'JOHANSSON Robert': 214.7,
 'JELAR Ziga': 180.1,
 'STOCH Kamil': 219.5,
 'SATO Yukiya': 168.0,
 'KUBACKI Dawid': 203.2,
 'TEPES Jurij': 194.7,
 'LANISEK Anze': 152.0,
 'DAMJAN Jernej': 130.8,
 'PAVLOVCIC Bor': 198.3,
 'PREVC Peter': 203.3}

test_case.assertEqual(mesto(podatki, 'DAMJAN Jernej'), 40)

