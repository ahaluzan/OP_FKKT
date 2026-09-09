import unittest
import naloge

test_case = unittest.TestCase()

podatki = [('T-Series Bhakti Sagar', 72.6, 29140, 37185631965, 'IN'),
    ('Set India', 180.0, 148727, 172709029653, 'IN'),
    ('Katy Perry', 45.6, 170, 27616850074, 'US')]

expected = {'IN': [('T-Series Bhakti Sagar', 29140, 72.6, 37185631965),
    ('Set India', 148727, 180.0, 172709029653)],
    'US': [('Katy Perry', 170, 45.6, 27616850074)]}

actual = naloge.po_drzavah(podatki)

test_case.assertEqual(expected, actual, "Napacna vsebina slovarja.")