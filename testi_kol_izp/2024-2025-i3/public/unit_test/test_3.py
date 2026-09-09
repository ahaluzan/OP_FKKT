import unittest
import naloge

test_case = unittest.TestCase()

expected = [('T-Series Bhakti Sagar', 72.6, 29140, 37185631965, 'IN'),
    ('Set India', 180.0, 148727, 172709029653, 'IN'),
    ('Katy Perry', 45.6, 170, 27616850074, 'US')]

actual = naloge.preberi_podatke("data/youtube5_missing.txt")

test_case.assertEqual(len(expected), len(actual), "Neustrezno obravnavanje vrstic z manjkajocimi podatki.")