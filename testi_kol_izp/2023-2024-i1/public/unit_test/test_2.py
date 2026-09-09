import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = naloge.preberi_podatke("goodread_simple1.csv")
expected = [('Dan Brown',
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
  ['Fantasy', 'Young Adult', 'Paranormal']),
 ('Suzanne Collins',
  'Mockingjay',
  'The Hunger Games',
  4.04,
  390,
  ['Young Adult', 'Dystopia', 'Fiction'])]

test_case.assertEqual(actual, expected, "Branje datoteke z imenom goodread_simple1.csv je napacno. Pazi na stevilo zanrov v seznamu!")
