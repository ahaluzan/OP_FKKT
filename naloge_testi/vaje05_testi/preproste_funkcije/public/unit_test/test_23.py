import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

test_case.assertTrue(prekrivajoca_seznama(['Anja', 'Peter', 'Miha'], ['Ana', 'Peter', 'Miha']), msg="prekrivajoca_seznama(['Anja', 'Peter', 'Miha'], ['Ana', 'Peter', 'Miha']) -> True")
test_case.assertFalse(prekrivajoca_seznama(['Ana', 'Peter', 'Miha', 'Tina', 'Sašo'], ['Maša', 'Marko', 'Petra', 'Tanja', 'Anja', 'Katarina']), msg="prekrivajoca_seznama(['Ana', 'Peter', 'Miha', 'Tina', 'Sašo'], ['Maša', 'Marko', 'Petra', 'Tanja', 'Anja', 'Katarina']) -> False")