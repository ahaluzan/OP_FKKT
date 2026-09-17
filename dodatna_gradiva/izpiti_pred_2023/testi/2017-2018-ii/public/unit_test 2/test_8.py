
import unittest
from izpit import *

test_case = unittest.TestCase()

podatki = [[2, 'JELAR Ziga', 'SLO', 218.5, (18.5, 18.5, 18.5, 18.5, 18.5), 9, 0.14],
[3, 'TEPES Jurij', 'SLO', 221.0, (18.5, 19.0, 18.0, 18.5, 18.5), 9, -0.36],
[4, 'KRANJEC Robert', 'SLO', 232.5, (18.5, 19.0, 17.5, 18.5, 18.5), 9, -0.19],
[5, 'PAVLOVCIC Bor', 'SLO', 206.0, (18.0, 18.0, 18.0, 18.0, 18.0), 9, -0.55],
[6, 'NAGLIC Tomaz', 'SLO', 213.0, (18.0, 18.0, 18.0, 18.0, 18.0), 9, -0.44],
[8, 'WANK Andreas', 'GER', 213.5, (18.0, 17.5, 18.0, 18.0, 18.0), 9, -0.24],
[9, 'HUBER Daniel', 'AUT', 214.0, (18.0, 18.0, 18.0, 18.0, 18.0), 9, -0.01],
[10, 'SCHLIERENZAUER Gregor', 'AUT', 194.0, (17.5, 17.5, 17.0, 17.0, 17.0), 9, -0.77],
[13, 'WOLNY Jakub', 'POL', 194.5, (16.0, 16.0, 16.0, 16.0, 16.0), 9, -0.04],
[14, 'PASCHKE Pius', 'GER', 218.5, (18.0, 18.0, 18.0, 17.5, 17.5), 9, 0.19],
[16, 'BICKNER Kevin', 'USA', 230.5, (18.0, 18.0, 17.5, 18.5, 19.0), 9, 0.13],
[17, 'KOBAYASHI Junshiro', 'JPN', 224.0, (18.5, 19.0, 18.5, 18.5, 18.5), 9, -0.25],
[22, 'KOBAYASHI Ryoyu', 'JPN', 211.5, (18.5, 18.0, 18.0, 18.0, 18.0), 9, -0.8],
[23, 'KORNILOV Denis', 'RUS', 222.5, (18.5, 18.5, 18.5, 19.0, 18.0), 9, 0.01],
[24, 'KUBACKI Dawid', 'POL', 220.0, (18.0, 18.5, 18.0, 18.0, 17.5), 9, -0.36],
[26, 'LEYHE Stephan', 'GER', 211.0, (18.0, 18.0, 18.0, 17.0, 18.0), 9, -0.91],
[27, 'FANNEMEL Anders', 'NOR', 233.0, (18.5, 18.5, 18.5, 18.5, 17.0), 9, -0.22],
[28, 'GRANERUD Halvor Egner', 'NOR', 191.0, (15.5, 16.0, 15.5, 15.5, 15.5), 9, -0.64],
[29, 'FORFANG Johann Andre', 'NOR', 234.5, (19.0, 19.0, 19.0, 19.0, 18.5), 9, -0.59],
[30, 'HULA Stefan', 'POL', 220.5, (18.0, 19.0, 19.0, 18.5, 18.5), 9, -0.02],
[32, 'FREITAG Richard', 'GER', 232.0, (18.0, 18.5, 17.0, 19.0, 18.5), 9, -0.37],
[33, 'STOCH Kamil', 'POL', 234.0, (19.5, 19.5, 19.5, 19.5, 19.0), 9, -0.44],
[34, 'PREVC Peter', 'SLO', 215.0, (18.0, 18.0, 18.0, 18.0, 18.5), 9, 0.05],
[35, 'EISENBICHLER Markus', 'GER', 224.0, (17.0, 17.0, 17.0, 17.5, 16.0), 9, -0.5],
[36, 'AMMANN Simon', 'SUI', 229.5, (16.0, 17.5, 16.5, 17.0, 16.0), 9, 0.04],
[37, 'KASAI Noriaki', 'JPN', 214.0, (18.0, 18.0, 18.0, 18.0, 18.0), 9, -0.27],
[38, 'KRAFT Stefan', 'AUT', 234.5, (19.0, 19.0, 19.0, 19.0, 19.5), 9, -0.12],
[39, 'JOHANSSON Robert', 'NOR', 227.5, (18.5, 18.5, 18.5, 18.5, 19.0), 9, -0.36],
[40, 'STJERNEN Andreas', 'NOR', 221.5, (18.5, 18.0, 18.0, 17.5, 18.0), 9, -0.75]]

rezultati = {'HUBER Daniel': 181.6,
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

for skok in podatki:
    test_case.assertEqual(izracun_tock(skok), rezultati[skok[1]], "Skakalec "+skok[1])

