'''jeziki'''
import unittest
import izpit1

naselje = [['SAF', 'AN', 'SHP'],
           ['S', 'F', 'AP'],
           ['AN', 'AFP', 'SM']]

ulica = 1

hisna_stevilka = 1

test_case = unittest.TestCase()
test_case.assertEqual(izpit1.jeziki(naselje, ulica, hisna_stevilka), {'F'})

