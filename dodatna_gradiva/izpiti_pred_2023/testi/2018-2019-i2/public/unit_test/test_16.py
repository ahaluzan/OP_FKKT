'''najvec_padavin'''
import unittest

import izpit

test_case = unittest.TestCase()

test_case.assertTrue(isinstance(izpit.najvec_padavin([]), float), "Funkcija ne vraca pravega tipa podatkov")
