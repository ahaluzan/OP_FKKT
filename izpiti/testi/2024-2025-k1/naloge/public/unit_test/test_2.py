import unittest
import naloge

test_case = unittest.TestCase()

usernames = ["SkyBreaker", "CodeHawk", "AstroForge", "NightLynx", "StormCipher", "NovaPulse", "DataDrift"]
passwords = ["Cryst@l88", "Phantom#42", "T1tanKey!", "Blitz$99", "Orb1t4rY", "W@veCore", "Sp@rk2024"]

result = naloge.vault(usernames, passwords)

expected = [('SkyBreaker', 'Cryst@l88'), ('CodeHawk', 'Phantom#42'), ('AstroForge', 'T1tanKey!'), ('NightLynx', 'Blitz$99'), ('StormCipher', 'Orb1t4rY'), ('NovaPulse', 'W@veCore'), ('DataDrift', 'Sp@rk2024')]

test_case.assertEqual(len(expected), len(result), "Napacno stevilo elementov v seznamu.")
