import unittest
import izpit1

naselje = [['PNS', 'MPAI', 'MPNFA', 'IMNF', 'MHFS', 'IMNA', 'MPNFA', 'IHAP', 'IHNFS', 'IPFS'],
           ['IHNA', 'MPNAS', 'IFS', 'IMAP', 'MNFSP', 'MNH', 'IFAS', 'MPHS', 'IHSNAM', 'IPNFA'],
           ['IFAS', 'IMS', 'MPSI', 'PSFNAM', 'IPNFA', 'IHFS', 'MNFHA', 'MHAS', 'IHSP', 'IHNFP'],
           ['PSFNAM', 'PNFH', 'MNFHS', 'INFAS', 'MHNAP', 'IMNFS', 'MPNHA', 'IMP', 'IHP', 'IPMA'],
           ['IHPFAM', 'PNHS', 'IHNFA', 'IHNFS', 'HNASP', 'NAS', 'IHFAP', 'IHPFAM', 'PNFA', 'MNFS'],
           ['IPNMS', 'IMNHP', 'SMFHA', 'HNAS', 'IHSFAM', 'MPNHI', 'MNHAS', 'IHSNAP', 'IPFA', 'HNAP'],
           ['MNF', 'HNFP', 'MFAP', 'SPNHA', 'IHMAS', 'MNHA', 'NFS', 'HFSP', 'MNFH', 'IPNFS'],
           ['IMNA', 'IPNH', 'PNFA', 'NFA', 'IHPSAM', 'MHIAP', 'PNFA', 'IPNFH', 'IPNMA', 'MHS'],
           ['IHFAS', 'MPNAS', 'IMHS', 'MFA', 'IHNMA', 'IMNSP', 'IHFS', 'HNAP', 'IMNS', 'IHMP'],
           ['IPNHS', 'IHMS', 'IHNF', 'IHFM', 'NAS', 'IMHAS', 'IMHS', 'IHNA', 'IHNA', 'PHS']]


naslov1 = (5, 6)
naslov2 = (5, 7)

test_case = unittest.TestCase()
test_case.assertEqual(izpit1.sporazumevanje(naselje, naslov1, naslov2), {'N', 'H', 'A', 'S'})

