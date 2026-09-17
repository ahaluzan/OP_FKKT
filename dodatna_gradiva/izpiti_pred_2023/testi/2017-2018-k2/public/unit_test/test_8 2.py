
import unittest
from kolokvij import *

test_case = unittest.TestCase()

podatki = ['CE L1-83T',
 'CE NR-006',
 'LJ MI-788',
 'MB DK-299',
 'CE DL-030',
 'MS FM-169',
 'LJ LF-920',
 'CE C3-125',
 'CE GZ-587',
 'LJ MI-788',
 'CE MN-800',
 'CE MR-622',
 'CE EF-111',
 'CE AD-035',
 'MB H5-77C',
 'MB LL-251',
 'MS KU-636',
 'LJ LF-920']

resitev = {'MS': {'FM-169', 'KU-636'},
 'MB': {'DK-299', 'H5-77C', 'LL-251'},
 'LJ': {'LF-920', 'MI-788'},
 'CE': {'AD-035',  'C3-125',  'DL-030',  'EF-111',  'GZ-587',  'L1-83T',  'MN-800',  'MR-622',  'NR-006'}}


test_case.assertEqual(zdruzi_obmocja(podatki), resitev)
