import unittest
import kolokvij
import numpy as np
import pickle

n = 100
drzave = pickle.load(open("public/data/drzave" + str(n) + ".p", "rb"))
meje = pickle.load(open("public/data/meje" + str(n) + ".p", "rb"))


drzava = drzave[n//2]
mnozica = {'HT', 'CP', 'CF', 'JB', 'RD', 'XK', 'AG', 'JF', 'GE', 'SW', 'UE', 'MB', 'GB', 'XB', 'FH', 'VV', 'GS', 'VC', 'NS', 'RX', 'UB', 'FB', 'VL', 'SM', 'ED', 'ZA', 'RJ', 'BE', 'CS', 'OS', 'IP', 'OL', 'PC', 'QJ', 'BJ', 'XC', 'DJ', 'PN', 'IX', 'CR', 'CK', 'XA', 'OD', 'YV', 'CZ', 'IJ', 'NW', 'RL', 'NC', 'SH', 'FD', 'KY', 'GG', 'WW', 'IV', 'DY', 'BW', 'US', 'IR', 'OR', 'SO', 'OC', 'LV', 'QC', 'JN', 'RU', 'EH', 'PI', 'UU', 'DB', 'XM', 'DV', 'HE', 'BR', 'MT', 'SV', 'MJ', 'BI', 'BN', 'XI'}

test_case = unittest.TestCase()
test_case.assertEqual(kolokvij.sosedi(meje, drzave, drzava), mnozica)