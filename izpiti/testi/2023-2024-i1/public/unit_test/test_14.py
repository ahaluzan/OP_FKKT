import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

sez = [('J.K. Rowling', 'Harry Potter and the Deathly Hallows', 'Harry Potter', 4.62, 759, []),
       ('J.K. Rowling', "Harry Potter and the Sorcerer's Stone", 'Harry Potter', 4.47, 309, []),
       ('Louis Sachar', 'Holes', 'Holes', 3.97, 233, []),              
       ('Stephenie Meyer', 'Twilight', 'The Twilight Saga', 3.6, 501, [])]

act = naloge.zbirke(sez)
exp = ['Harry Potter', 'Holes', 'The Twilight Saga']

test_case.assertEqual(type(act), type(exp), "Napacen podatkovni tip.")
test_case.assertEqual(act, exp, "Pazi pri ponovitvah iste zbirke.")

