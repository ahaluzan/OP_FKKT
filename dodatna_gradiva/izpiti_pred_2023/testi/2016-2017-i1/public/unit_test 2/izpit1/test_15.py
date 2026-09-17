import unittest
import izpit1

naselje = [['API', 'NSPM', 'NSHI', 'HAMSFI', 'NSAM', 'NMHAI', 'NAMFS', 'PSAIM', 'NMI', 'FAPI', 'NHSPI', 'NSHI', 'NHAFI', 'HPANMF', 'NPSAF', 'NPI', 'NPHAF', 'NFHPI', 'MHAPS', 'HPNMFI'],
           ['PSFM', 'NSAFI', 'NSAM', 'NHA', 'NAPI', 'NAMPI', 'NHSP', 'PAFI', 'NAPI', 'NHAFI', 'AMPI', 'HPANSF', 'NHAFI', 'SHFM', 'HPASFI', 'NSHFI', 'PHAF', 'NSAHM', 'PHAFS', 'HPANSI'],
           ['HANMSF', 'NSHAI', 'NHFI', 'HPAMSF', 'IAFM', 'FAPHM', 'NPSFM', 'HSFPM', 'NPFI', 'FAPM', 'APS', 'IHPM', 'NAFS', 'NSHPI', 'NSAPM', 'HAMPI', 'HFI', 'NSHAI', 'MHAFI', 'PHAIS'],
           ['SAHI', 'NAFI', 'HPASFI', 'NSAI', 'NSHI', 'NHSAF', 'NFSAP', 'HPNMSF', 'PHMFI', 'PIAHS', 'NSMI', 'PHFI', 'NAIS', 'NHIM', 'HPI', 'HFI', 'NFAPM', 'SAF', 'IAPS', 'PANMFI'],
           ['NAF', 'NSPM', 'PIFM', 'FHSPM', 'NFSAH', 'IHAPM', 'PHAF', 'NAHI', 'HPNMSF', 'HSAPM', 'NHAPS', 'PHAFI', 'NSMPI', 'FSMPI', 'FHPI', 'HPNSFI', 'SMFI', 'PANMFI', 'NHSPM', 'SIAFM'],
           ['FAH', 'FIHPS', 'AHMPI', 'HSAPM', 'IAFS', 'NFM', 'AIM', 'SHPI', 'NSAM', 'HAFI', 'NPIFM', 'ASMI', 'PAHM', 'NPAFM', 'NFSPM', 'NAFI', 'NFSPI', 'FHIS', 'NSHFI', 'HPANMI'],
           ['NHAIM', 'PHAFM', 'HPANFI', 'NAPI', 'NFMPI', 'PSAH', 'AHM', 'NSMFI', 'NAS', 'NSIM', 'NPHFM', 'HNMSFI', 'NFSHM', 'NHPS', 'NHAF', 'NPSH', 'SAHMI', 'NIAPM', 'PSMFI', 'NHFI'],
           ['NSPI', 'HSAIM', 'NIHFM', 'NSAPI', 'NPAFI', 'NHAFS', 'NHM', 'AFS', 'NSH', 'NHAF', 'NHAS', 'HPAMSI', 'NAMFI', 'NHSPF', 'APM', 'NFIM', 'PIAFS', 'NSFI', 'NSHPI', 'NHAFM'],
           ['NFHPM', 'SAM', 'NHM', 'NAMHI', 'NFSPM', 'PFM', 'HSAPI', 'HSFI', 'SAPI', 'NAFI', 'NFSHI', 'IM', 'HISFM', 'PAMFS', 'NAFI', 'MSAHI', 'PSAIM', 'IAPM', 'HANSFI', 'HPNMFI'],
           ['NHAPI', 'NHAFI', 'FHMPI', 'PISHM', 'NAMHI', 'PIHFM', 'HAFM', 'NSAPI', 'NASMI', 'FAMPS', 'NHSFI', 'NPHF', 'FSPI', 'NPSHM', 'NFHPS', 'PSIM', 'NHSAF', 'IHAPM', 'NPAFM', 'NSFI'],
           ['PSMFI', 'NAPM', 'NSAI', 'NPSAF', 'PANMFI', 'NSFM', 'SAFM', 'HSAPI', 'NSAPI', 'FSHIM', 'HANMFI', 'SAPI', 'NPHFM', 'HPANMS', 'HIAPM', 'NPSHI', 'NFAPI', 'HAFM', 'NAMHI', 'NAFM'],
           ['NHSAF', 'NFI', 'NSIM', 'HSAF', 'NHFM', 'ISHM', 'FSAHM', 'NFSH', 'SAM', 'FAHM', 'NHFS', 'ISPM', 'APM', 'PHFM', 'NHSP', 'NPAIM', 'NSAPM', 'HSAP', 'NSHFM', 'NHP'],
           ['NAMHI', 'HPI', 'HAFI', 'ANMSFI', 'FSPM', 'SAHI', 'NSMI', 'NSAI', 'HPAMSI', 'NHAIS', 'NFPI', 'SAPI', 'NSPI', 'AFM', 'NMHAI', 'SAFI', 'NAF', 'SFI', 'PHAFS', 'NMFI'],
           ['NHAS', 'SIHFM', 'NISPM', 'NHAPS', 'NHPI', 'NAMHS', 'HANSFI', 'NFSP', 'NHPI', 'MSAFI', 'PAFM', 'NPM', 'NSHM', 'HAPM', 'FHMPS', 'HAFPS', 'NPHAF', 'NPSFI', 'NSAPM', 'NHAFM'],
           ['FPM', 'NSAP', 'NHPS', 'NPHFI', 'HISFM', 'NFAPI', 'FSAPI', 'NHAPI', 'NAS', 'HANMSI', 'AHMFI', 'NFPI', 'NHIM', 'ISPM', 'NHAP', 'HISPM', 'NIHPM', 'NHIS', 'HANMFI', 'NSAFM'],
           ['HSMFIA', 'FIHPS', 'SMHI', 'PAFI', 'HPANFI', 'MSAPI', 'FHMPI', 'NAPI', 'NAPS', 'PHFI', 'NHAPS', 'SAFI', 'NSMPI', 'NFPI', 'AHMFI', 'NSHI', 'SMHI', 'ANMSFI', 'NSAHM', 'AFI'],
           ['FSHPI', 'NHSF', 'FSP', 'NAFI', 'NPHFM', 'NSHFI', 'HAPI', 'SHI', 'NPAFM', 'NHFM', 'HPANSF', 'HPANMI', 'SPI', 'NHAPS', 'NHAFM', 'NSAHM', 'HPANMI', 'ISFM', 'NSAMI', 'PIAFM'],
           ['NSF', 'HAMSFI', 'FHSPM', 'SHAPI', 'NSMHI', 'NAMFS', 'HAI', 'SIM', 'NHSPI', 'NHAP', 'FHAPS', 'HMFI', 'NAIM', 'NAIM', 'FHAPM', 'NHAPM', 'NAMHS', 'NHAFM', 'NHAPS', 'NFAPI'],
           ['NFIPM', 'NAPI', 'PAHS', 'PHFI', 'HPAMSI', 'NAFM', 'NPAFM', 'NSHI', 'NHFM', 'SAFI', 'HAIS', 'NAFM', 'NSHI', 'HPANFI', 'PIAFM', 'HSMPI', 'NHAM', 'SAPI', 'NFM', 'MHAPS'],
           ['FSAHM', 'NPSFM', 'NIM', 'HFS', 'FHAPS', 'NSFM', 'HSAFI', 'NSHM', 'NHAFS', 'HPANMF', 'NSAI', 'NAFS', 'AMPI', 'FSPH', 'NHAF', 'SHIM', 'PAMSFI', 'HAI', 'NHF', 'NPHFI']]




test_case = unittest.TestCase()
test_case.assertEqual(izpit1.najbolj_zastopan_jezik(naselje), 'A')



