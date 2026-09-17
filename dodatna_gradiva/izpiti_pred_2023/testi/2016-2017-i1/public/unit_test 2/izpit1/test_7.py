import unittest
import izpit1

naselje = [['SAF', 'AN', 'SHP'],
           ['S', 'F', 'AP'],
           ['AN', 'AFP', 'SM']]

naslov1 = (1, 0)
naslov2 = (1, 2)

test_case = unittest.TestCase()
test_case.assertEqual(izpit1.sporazumevanje(naselje, naslov1, naslov2), None)

