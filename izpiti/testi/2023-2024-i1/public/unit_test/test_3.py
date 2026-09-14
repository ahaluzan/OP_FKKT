import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = naloge.preberi_podatke("goodread_simple2.csv")
expected = [('Rainbow Rowell',
  'Eleanor & Park',
  'standalone',
  4.05,
  328,
  ['Young Adult', 'Romance', 'Contemporary']),
 ('William Shakespeare',
  'Romeo and Juliet',
  'standalone',
  3.75,
  301,
  ['Classics', 'Plays', 'Fiction']),
 ('Dan Brown',
  'Angels & Demons',
  'Robert Langdon',
  3.9,
  736,
  ['Fiction', 'Mystery', 'Thriller']),
 ('Cassandra Clare',
  'City of Bones',
  'The Mortal Instruments',
  4.1,
  485,
  ['Fantasy', 'Young Adult', 'Paranormal'])]

test_case.assertEqual(actual, expected, "Branje datoteke z imenom goodread_simple2.csv je napacno. Pazi na manjkajoca imena zbirk!")
