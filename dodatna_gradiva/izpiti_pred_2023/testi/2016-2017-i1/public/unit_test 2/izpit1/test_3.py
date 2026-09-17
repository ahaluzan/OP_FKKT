import unittest
import izpit1

naselje = [['SAF', 'AN', 'SHP'],
           ['S', 'F', 'AP'],
           ['AN', 'AFP', 'SM']]

ulica = 0

hisna_stevilka = 0

test_case = unittest.TestCase()
test_case.assertEqual(izpit1.jeziki(naselje, ulica, hisna_stevilka), {'A', 'F', 'S'})

