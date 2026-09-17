'''najbolj_zastopan_jezik'''
import unittest
import izpit1

naselje = [['SAF', 'AN', 'SHP'],
           ['S', 'F', 'AP'],
           ['AN', 'AFP', 'SM']]


test_case = unittest.TestCase()
test_case.assertEqual(izpit1.najbolj_zastopan_jezik(naselje), 'A')

