'''preberi_podatke'''
import unittest
from kolokvij import *

test_case = unittest.TestCase()
test_case.assertEqual(preberi_podatke("public/data/tomacevo.txt"),
['LJ MI-788',
 'LJ LF-920',
 'LJ JT-154',
 'KR ZF-406',
 'LJ 007-CL',
 'LJ KV-288',
 'KR N7-177',
 'LJ P3-07F',
 'LJ MI-788']
)
