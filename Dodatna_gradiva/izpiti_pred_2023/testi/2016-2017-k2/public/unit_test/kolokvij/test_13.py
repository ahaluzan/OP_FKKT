import unittest
import kolokvij
import numpy as np
import pickle

n = 50
drzave = pickle.load(open("public/data/drzave" + str(n) + ".p", "rb"))
meje = pickle.load(open("public/data/meje" + str(n) + ".p", "rb"))


drzava = drzave[n//2]
mnozica = {'VP', 'OS', 'NZ', 'HD', 'AP', 'BX', 'TK', 'UA', 'QJ', 'KY', 'SP', 'SH', 'IJ', 'NR', 'LJ', 'CX', 'LS', 'MW', 'RZ', 'BS', 'NI', 'KF', 'KX', 'IC', 'AF', 'SI', 'FC', 'ST', 'HB', 'OT', 'QX', 'QD', 'KM', 'NP', 'PX', 'PO', 'QI', 'HJ'}

test_case = unittest.TestCase()
test_case.assertEqual(kolokvij.sosedi(meje, drzave, drzava), mnozica)

