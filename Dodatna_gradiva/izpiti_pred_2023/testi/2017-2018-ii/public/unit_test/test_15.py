import unittest
from izpit import *

test_case = unittest.TestCase()

podatki = {'HUBER Daniel': 193.4,
 'WELLINGER Andreas': 210.6,
 'TAKEUCHI Taku': 178.4,
 'HAYBOECK Michael': 189.6,
 'KRAFT Stefan': 227.4,
 'EISENBICHLER Markus': 210.2,
 'TANDE Daniel Andre': 225.1,
 'KOBAYASHI Ryoyu': 219.5,
 'AMMANN Simon': 208.3,
 'KASAI Noriaki': 196.2,
 'SEMENIC Anze': 202.9,
 'STJERNEN Andreas': 228.5,
 'FREITAG Richard': 228.7,
 'BARTOL Tilen': 199.4,
 'HULA Stefan': 208.7,
 'GEIGER Karl': 224.4,
 'GRANERUD Halvor Egner': 199.5,
 'KOT Maciej': 193.8,
 'FORFANG Johann Andre': 215.7,
 'KUBACKI Dawid': 196.0,
 'PASCHKE Pius': 179.9,
 'KOBAYASHI Junshiro': 214.8,
 'LEYHE Stephan': 167.5,
 'AIGNER Clemens': 194.3,
 'PREVC Peter': 222.6,
 'JOHANSSON Robert': 224.9,
 'STOCH Kamil': 227.1,
 'ZYLA Piotr': 178.4,
 'FANNEMEL Anders': 218.2,
 'DAMJAN Jernej': 194.6}

test_case.assertEqual(mesto(podatki, 'FREITAG Richard'), 1)
