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

resitev = {'KP NU-062', 'KP P6-394', 'LJ 007-CL', 'LJ 453-UA', 'LJ AG-870', 'LJ ET-285', 'LJ JH-263', 'LJ JT-154', 'LJ KV-288', 'LJ LF-920', 'LJ LH-924', 'LJ MI-788', 'LJ P3-07F', 'LJ PB-435', 'LJ PB-699', 'P 06-697', 'PO CV-300'}

test_case.assertEqual(pogosta_vozila(podatki, 1), resitev)
