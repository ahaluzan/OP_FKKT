import unittest
import kolokvij
import numpy as np
import pickle

n = 70
drzave = pickle.load(open("public/data/drzave" + str(n) + ".p", "rb"))
meje = pickle.load(open("public/data/meje" + str(n) + ".p", "rb"))


drzava = drzave[0]

test_case = unittest.TestCase()
test_case.assertAlmostEqual(np.float64(kolokvij.skupna_dolzina_meje(meje, drzave, drzava)), np.float64(33744.432926552567))

