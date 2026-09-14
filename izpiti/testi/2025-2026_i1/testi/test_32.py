import unittest
import naloge

test_case = unittest.TestCase()

podatki = []

expected = ""

actual = naloge.po_izkusnjah(podatki, "Beginner")

test_case.assertEqual(expected, actual, "Napačno vračanje funkcije v primeru praznega seznama.")