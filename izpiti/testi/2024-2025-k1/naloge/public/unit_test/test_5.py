'''slaba_praksa'''
import unittest
import naloge

test_case = unittest.TestCase()

st = [('StormCipher', 'Cryst@l88'), ('CodeHawk', 'Phantom#42CodeHawk'), ('AstroForge', 'T1tanKey!'), ('NightLynx', 'Blitz$99'), ('NovaPulse', 'W@veCore')]

expected = ['CodeHawk']

actual = naloge.slaba_praksa(st)

test_case.assertEqual(type(expected[0]), type(actual[0]), "Funkcija vraca napacen podatkovni tip.")

