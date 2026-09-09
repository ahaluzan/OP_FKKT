'''priimki'''
import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

N41_in = [(1992, 'Walcott', 'literature', 'm', '23-01-1930', 'LC'),
(1952, 'Bloch', 'physics', 'm', '23-10-1905', 'CH'),
(2005, 'Hall', 'physics', 'm', '21-08-1934', 'US'),
(1964, 'Bloch', 'medicine', 'm', '21-01-1912', 'PL'),
(2017, 'Hall', 'medicine', 'm', '03-05-1945', 'US'),
(2016, 'Thouless', 'physics', 'm', '21-09-1934', 'GB')]

act = naloge.priimki(N41_in, 'physics', 'medicine')
exp = {'Bloch', 'Hall'}

test_case.assertEqual(len(act), len(exp), "Mnozica nima ustreznega stevila elementov.")
test_case.assertEqual(act, exp)

