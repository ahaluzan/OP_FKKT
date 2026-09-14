import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

data_in = [('Robert Andrich', 'Germany', 30, 5, 0, 0, 2, 0),
 ('Alexander Bah', 'Denmark', 27, 4, 0, 0, 0, 0),
 ('Jude Bellingham', 'England', 21, 7, 2, 1, 2, 0),
 ('Jacob Bruun Larsen', 'Denmark', 26, 1, 0, 0, 0, 0),
 ('Joao Cancelo', 'Portugal', 30, 4, 0, 0, 1, 0),
 ('Kingsley Coman', 'France', 28, 1, 0, 0, 0, 0),
 ('Marc Cucurella', 'Spain', 26, 6, 0, 1, 0, 0),
 ('Thomas Delaney', 'Denmark', 33, 3, 0, 0, 0, 0),
 ('Kasper Dolberg', 'Denmark', 27, 2, 0, 0, 0, 0),
 ('Joao Felix', 'Portugal', 25, 2, 0, 0, 0, 0),
 ('Youssouf Fofana', 'France', 25, 3, 0, 0, 0, 0),
 ('Conor Gallagher', 'England', 24, 5, 0, 0, 1, 0),
 ('Antoine Griezmann', 'France', 33, 6, 0, 0, 1, 0),
 ('Marc Guehi', 'England', 24, 6, 0, 1, 2, 0),
 ('Benjamin Henrichs', 'Germany', 27, 1, 0, 0, 0, 0),
 ('Pierre Hojbjerg', 'Denmark', 29, 4, 0, 0, 0, 0),
 ('Joselu', 'Spain', 34, 2, 0, 0, 0, 0),
 ("N'Golo Kante", 'France', 33, 6, 0, 0, 0, 0),
 ('Ezri Konsa', 'England', 27, 3, 0, 0, 0, 0),
 ('Aymeric Laporte', 'Spain', 30, 6, 0, 0, 0, 0),
 ('Fermin Lopez', 'Spain', 21, 1, 0, 0, 0, 0),
 ('Kylian Mbappe', 'France', 26, 5, 1, 1, 1, 0),
 ('Maximilian Mittelstadt', 'Germany', 27, 4, 0, 1, 2, 0),
 ('Jamal Musiala', 'Germany', 21, 5, 3, 0, 0, 0),
 ('Jesus Navas', 'Spain', 39, 3, 0, 0, 1, 0),
 ('Joao Neves', 'Portugal', 20, 2, 0, 0, 0, 0),
 ('Christian Norgaard', 'Denmark', 30, 3, 0, 0, 1, 0),
 ('Joao Palhinha', 'Portugal', 29, 4, 0, 0, 2, 0),
 ('Pepe', 'Portugal', 41, 4, 0, 0, 0, 0),
 ('Jordan Pickford', 'England', 30, 7, 0, 0, 0, 0),
 ('Goncalo Ramos', 'Portugal', 23, 1, 0, 0, 0, 0),
 ('Declan Rice', 'England', 25, 7, 0, 1, 0, 0),
 ('Antonio Rudiger', 'Germany', 31, 5, 0, 0, 2, 0),
 ('William Saliba', 'France', 23, 6, 0, 0, 1, 0),
 ('Kasper Schmeichel', 'Denmark', 38, 4, 0, 0, 0, 0),
 ('Antonio Silva', 'Portugal', 21, 2, 0, 0, 0, 0),
 ('Andreas Skov Olsen', 'Denmark', 25, 3, 0, 0, 0, 0),
 ('Aurelien Tchouameni', 'France', 24, 5, 0, 0, 2, 0),
 ('Ferran Torres', 'Spain', 24, 5, 1, 0, 1, 0),
 ('Dayot Upamecano', 'France', 26, 6, 0, 0, 0, 0),
 ('Daniel Vivian', 'Spain', 25, 2, 0, 0, 1, 0),
 ('Nico Williams', 'Spain', 22, 6, 2, 1, 0, 0),
 ('Lamine Yamal', 'Spain', 17, 7, 1, 4, 1, 0),
 ('Jaka Bijol', 'Slovenia', 25, 4, 0, 0, 2, 0),
 ('Vanja Drkusic', 'Slovenia', 25, 4, 0, 0, 1, 0),
 ('Jon Gorenc Stankovic', 'Slovenia', 28, 4, 0, 0, 1, 0),
 ('Zan Karnicnik', 'Slovenia', 30, 4, 1, 0, 1, 0),
 ('Jan Oblak', 'Slovenia', 31, 4, 0, 0, 0, 0),
 ('Petar Stojanovic', 'Slovenia', 29, 4, 0, 0, 1, 0)]

actual = naloge.drzavni_seznami(data_in, "Slovenia")
expected = {'starosti': [25, 25, 28, 30, 31, 29],
 'goli': [0, 0, 0, 1, 0, 0],
 'rumeni_kartoni': [2, 1, 1, 1, 0, 1],
 'rdeci_kartoni': [0, 0, 0, 0, 0, 0]}

for (exp_key, exp_val), (act_key, act_val) in zip(expected.items(), actual.items()):
    test_case.assertEqual(act_key, exp_key, "Napacen kljuc.")
    test_case.assertEqual(act_val, exp_val, "Napacna vrednost.")
