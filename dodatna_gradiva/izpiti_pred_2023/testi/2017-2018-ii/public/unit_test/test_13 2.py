import unittest
from izpit import *

test_case = unittest.TestCase()

podatki = {'HUBER Daniel': 181.6,
 'EISENBICHLER Markus': 199.2,
 'KRANJEC Robert': 208.5,
 'NAGLIC Tomaz': 187.9,
 'KASAI Noriaki': 186.2,
 'AMMANN Simon': 195.0,
 'BICKNER Kevin': 199.9,
 'STJERNEN Andreas': 203.5,
 'FREITAG Richard': 210.5,
 'HULA Stefan': 191.6,
 'KORNILOV Denis': 193.0,
 'GRANERUD Halvor Egner': 157.5,
 'SCHLIERENZAUER Gregor': 168.4,
 'FORFANG Johann Andre': 219.3,
 'WOLNY Jakub': 152.8,
 'KUBACKI Dawid': 194.9,
 'PASCHKE Pius': 183.6,
 'KOBAYASHI Junshiro': 199.3,
 'LEYHE Stephan': 193.7,
 'WANK Andreas': 185.0,
 'FANNEMEL Anders': 209.6,
 'KRAFT Stefan': 211.2,
 'JOHANSSON Robert': 205.4,
 'JELAR Ziga': 186.4,
 'STOCH Kamil': 217.6,
 'KOBAYASHI Ryoyu': 192.4,
 'TEPES Jurij': 197.6,
 'PREVC Peter': 181.9,
 'PAVLOVCIC Bor': 181.4}

test_case.assertEqual(mesto(podatki, 'TEPES Jurij'), 12)

