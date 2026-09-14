import unittest
import naloge

test_case = unittest.TestCase()

st2 = [('StormCipher', '!StormCipher87'), ('CodeHawk', 'Phantom#42'), ('AstroForge', 'T1tanAstroForgeKey!'), ('NightLynx', 'Blitz$99'), ('NovaPulse', 'NovaPulseW@veCore')]

expected = ['StormCipher', 'AstroForge', 'NovaPulse']

actual = naloge.slaba_praksa(st2)

test_case.assertEqual(expected, actual, "Funkcija ne vraca pravega stevila uporabnikov.")