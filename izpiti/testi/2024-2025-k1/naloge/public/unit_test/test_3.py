import unittest
import naloge

test_case = unittest.TestCase()

usernames = ["StormCipher", "CodeHawk", "AstroForge", "NightLynx", "StormCipher", "NovaPulse", "CodeHawk"]
passwords = ["Cryst@l88", "Phantom#42", "T1tanKey!", "Blitz$99", "Orb1t4rY", "W@veCore", "Sp@rk2024"]

expected = [('StormCipher', 'Cryst@l88'), ('CodeHawk', 'Phantom#42'), ('AstroForge', 'T1tanKey!'), ('NightLynx', 'Blitz$99'), ('NovaPulse', 'W@veCore')]

result = naloge.vault(usernames, passwords)

test_case.assertEqual(set(expected), set(result), "Napacna kombinacija uporabniskega imena in gesla, kadar se uporabnisko ime pojavi veckrat.")