import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

actual = naloge.preberi_podatke("goodread5.csv")
expected = [('Frances Hodgson Burnett',
  'The Secret Garden',
  'standalone',
  4.13,
  331,
  ['Classics', 'Fiction', 'Childrens']),
 ('John Green',
  'Looking for Alaska',
  'standalone',
  4.02,
  221,
  ['Young Adult', 'Fiction', 'Contemporary']),
 ('Louis Sachar',
  'Holes',
  'Holes',
  3.97,
  233,
  ['Young Adult', 'Fiction', 'Childrens']),
 ('Arthur Golden',
  'Memoirs of a Geisha',
  'standalone',
  4.12,
  503,
  ['Fiction', 'Historical Fiction', 'Romance']),
 ('Stephenie Meyer',
  'Twilight',
  'The Twilight Saga',
  3.6,
  501,
  ['Young Adult', 'Fantasy', 'Romance'])]

test_case.assertEqual(actual, expected, "Branje datoteke z imenom goodread5.csv je napacno.")

