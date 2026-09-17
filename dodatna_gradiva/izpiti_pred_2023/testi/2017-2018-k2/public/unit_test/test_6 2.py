'''zdruzi_obmocja'''
import unittest
from kolokvij import *

test_case = unittest.TestCase()

podatki = ['LJ MI-788',
 'LJ LF-920',
 'LJ JT-154',
 'KR ZF-406',
 'LJ 007-CL',
 'LJ KV-288',
 'KR N7-177',
 'LJ P3-07F',
 'LJ MI-788']

resitev = {'KR': {'N7-177', 'ZF-406'},
 'LJ': {'007-CL', 'JT-154', 'KV-288', 'LF-920', 'MI-788', 'P3-07F'}}

test_case.assertEqual(zdruzi_obmocja(podatki), resitev)

