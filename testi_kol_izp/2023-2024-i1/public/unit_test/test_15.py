import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

sez = [('Stephenie Meyer', 'Twilight', 'The Twilight Saga', 3.6, 501, []),
       ('J.K. Rowling', 'Harry Potter and the Deathly Hallows', 'Harry Potter', 4.62, 759, []),
       ('Louis Sachar', 'Holes', 'Holes', 3.97, 233, [])]

act = naloge.zbirke(sez)
exp = ['Harry Potter', 'Holes', 'The Twilight Saga']

test_case.assertEqual(type(act), type(exp), "Napacen podatkovni tip.")
test_case.assertEqual(act, exp, "Pazi pri vrstnem redu v seznamu.")

