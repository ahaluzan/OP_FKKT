import unittest
import izpit1

naselje = [['MNFHI', 'MSNI', 'SIPHN', 'SMHI'],
           ['MPNA', 'HSPNI', 'SFPHN', 'MAPNI'],
           ['SMFHI', 'HFN', 'MPHISN', 'MIPNA'],
           ['MIFHA', 'MAISFN', 'SFPA', 'SNA'],
           ['MSPA', 'MSFNA', 'HFNA', 'MFPI'],
           ['SIFNA', 'HMNI', 'IFA', 'FPNI'],
           ['MNA', 'MNH', 'HSFN', 'NMAHI'],
           ['SMHA', 'MFHA', 'SINA', 'SIPA']]



test_case = unittest.TestCase()
test_case.assertEqual(izpit1.najbolj_zastopan_jezik(naselje), 'N')



