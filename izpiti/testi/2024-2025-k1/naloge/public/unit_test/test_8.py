import unittest
import naloge

test_case = unittest.TestCase()
# preverjanje vračanja pri seznamih neenake dolžine

ag = [('alice123', 'alpha001'), ('carol789', 'beta002'), ('dave321', 'gamma003')]

expected = []

actual = naloge.slaba_praksa(ag)

test_case.assertEqual(expected,actual, 'Nepravilno vracanje v primeru, ko se vsa gesla razlikujejo od uporabniskih imen.')