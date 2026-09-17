
import unittest
from kolokvij import *

test_case = unittest.TestCase()
test_case.assertEqual(preberi_podatke("public/data/pp_vic.txt"),
['LJ MI-788',
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
)
