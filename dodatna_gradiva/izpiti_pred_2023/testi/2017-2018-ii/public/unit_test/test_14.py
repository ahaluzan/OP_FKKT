import unittest
from izpit import *

test_case = unittest.TestCase()

podatki = {'HUBER Daniel': 180.9,
 'WELLINGER Andreas': 205.0,
 'TAKEUCHI Taku': 170.6,
 'HAYBOECK Michael': 197.9,
 'KRAFT Stefan': 231.4,
 'EISENBICHLER Markus': 217.6,
 'TANDE Daniel Andre': 233.3,
 'KOBAYASHI Ryoyu': 203.6,
 'AMMANN Simon': 215.6,
 'KASAI Noriaki': 198.5,
 'SEMENIC Anze': 204.7,
 'STJERNEN Andreas': 219.6,
 'FREITAG Richard': 217.9,
 'BARTOL Tilen': 205.5,
 'HULA Stefan': 215.5,
 'GEIGER Karl': 221.1,
 'GRANERUD Halvor Egner': 196.4,
 'KOT Maciej': 202.6,
 'FORFANG Johann Andre': 227.0,
 'KUBACKI Dawid': 199.0,
 'PASCHKE Pius': 177.2,
 'KOBAYASHI Junshiro': 227.1,
 'LEYHE Stephan': 181.3,
 'AIGNER Clemens': 173.3,
 'PREVC Peter': 220.2,
 'JOHANSSON Robert': 231.9,
 'STOCH Kamil': 247.1,
 'ZYLA Piotr': 188.1,
 'FANNEMEL Anders': 220.2,
 'DAMJAN Jernej': 194.6}

test_case.assertEqual(mesto(podatki, 'PREVC Peter'), 8)

