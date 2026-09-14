'''povprecne_mesecne_place'''
import unittest

import izpit

test_case = unittest.TestCase()

test_case.assertTrue(isinstance(izpit.povprecne_mesecne_place([]), dict), "Funkcija ne vraca pravega tipa podatkov")
