'''pogosta_vozila'''
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

resitev = {'LJ MI-788'}

test_case.assertEqual(pogosta_vozila(podatki, 2), resitev)

