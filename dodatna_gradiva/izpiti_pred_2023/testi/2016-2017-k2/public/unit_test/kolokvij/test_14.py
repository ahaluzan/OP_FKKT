import unittest
import kolokvij
import numpy as np
import pickle

n = 70
drzave = pickle.load(open("public/data/drzave" + str(n) + ".p", "rb"))
meje = pickle.load(open("public/data/meje" + str(n) + ".p", "rb"))


drzava = drzave[n//2]
mnozica = {'UK', 'CV', 'HH', 'GB', 'VJ', 'FX', 'SJ', 'DR', 'VF', 'ME', 'LQ', 'FF', 'RK', 'LS', 'ES', 'MY', 'TG', 'TQ', 'TM', 'FK', 'EP', 'BQ', 'UU', 'NN', 'VR', 'BA', 'HX', 'PA', 'LW', 'LV', 'KX', 'SP', 'WP', 'TD', 'JM', 'CR', 'FM', 'MB', 'TE', 'UW', 'IE', 'BI', 'XU', 'ZC', 'RJ', 'GY', 'WH', 'HD', 'AW', 'AH', 'CD', 'HC', 'ZP', 'SN'}

test_case = unittest.TestCase()
test_case.assertEqual(kolokvij.sosedi(meje, drzave, drzava), mnozica)