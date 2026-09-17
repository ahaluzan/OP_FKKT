import unittest
import kolokvij
import numpy as np
import pickle

n = 50
drzave = pickle.load(open("public/data/drzave" + str(n) + ".p", "rb"))
meje = pickle.load(open("public/data/meje" + str(n) + ".p", "rb"))

par_drzav = (drzave[0], drzave[n//2])

test_case = unittest.TestCase()
test_case.assertAlmostEqual(np.float64(kolokvij.dolzina_meje(meje, drzave, par_drzav)), np.float64(394.31227901875212))

