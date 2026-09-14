import unittest
import izpit1

naselje = [['MASIH', 'NFMH'],
           ['SFI', 'SMPH'],
           ['ASFH', 'MFSNH'],
           ['NAMIH', 'ASIH'],
           ['SAFI', 'AIPH'],
           ['ASFPH', 'FMH']]



test_case = unittest.TestCase()
test_case.assertEqual(izpit1.najbolj_zastopan_jezik(naselje), 'H')



