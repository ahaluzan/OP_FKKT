'''najstarejsi_film'''
import unittest
import kolokvij



slovar = {'France': {("Le fabuleux destin d'Amélie Poulain", 2001)}, 'Bosnia & Herzegovina': {('Ničija zemlja', 2001)}, 'Italy': {('Il buono, il brutto, il cattivo', 1966), ("C'era una volta il West", 1968)}, 'Brazil': {('Cidade de Deus', 2002)}}
drzava = 'Italy'

test_case = unittest.TestCase()
test_case.assertEqual(kolokvij.najstarejsi_filmi(slovar, drzava), {'Il buono, il brutto, il cattivo'})

