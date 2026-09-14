import unittest
import naloge

test_case = unittest.TestCase()

st3 = [('StormCipher', '!StormCipher87'), ('CodeHawk', 'Phantom#42'), ('AstroForge', 'T1tanAstroForgeKey!'), ('StormCipher', '!23StormCipher87'), ('NightLynx', 'Blitz$99')]

expected = ['StormCipher', 'AstroForge']
actual = naloge.slaba_praksa(st3)

test_case.assertEqual(expected, actual, 'Napacno vracanje funkcije pri veckratni ponovitvi istega uporabnika.')