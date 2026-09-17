
import unittest
from kolokvij import *

test_case = unittest.TestCase()

podatki = ['LJ MI-788',
 'LJ LF-920',
 'LJ JT-154',
 'LJ 007-CL',
 'LJ KV-288',
 'KP P6-394',
 'P 06-697',
 'LJ 453-UA',
 'LJ LH-924',
 'LJ P3-07F',
 'PO CV-300',
 'LJ PB-699',
 'LJ AG-870',
 'LJ ET-285',
 'LJ JH-263',
 'LJ PB-435',
 'P 06-697',
 'LJ 007-CL',
 'KP NU-062']

resitev = {'KP': {'NU-062', 'P6-394'},
 'P': {'06-697'},
 'LJ': {'007-CL',  '453-UA',  'AG-870',  'ET-285',  'JH-263',  'JT-154',  'KV-288',  'LF-920',  'LH-924',  'MI-788',  'P3-07F',  'PB-435',  'PB-699'},
 'PO': {'CV-300'}}


test_case.assertEqual(zdruzi_obmocja(podatki), resitev)
