import unittest
import kolokvij
import numpy as np

drzave = ['SI', 'IT', 'AT', 'HR', 'HU']

meje = np.array([[None, 232, 318, 670, 102],
[232, None, 430, None, None],
[318, 430, None, None, 356],
[670, None, None, None, 355],
[102, None, 356, 355, None]], dtype = np.float)

drzava = 'SI'

test_case = unittest.TestCase()
test_case.assertAlmostEqual(np.float64(kolokvij.skupna_dolzina_meje(meje, drzave, drzava)), np.float64(1322.0))

