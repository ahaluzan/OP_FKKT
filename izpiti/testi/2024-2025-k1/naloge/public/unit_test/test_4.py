import unittest
import naloge

test_case = unittest.TestCase()

usernames = ["StormCiphers", "CodeHawk", "AstroForge", "NightLynx", "StormCipher", "NovaPulse", "ACodeHawk"]
passwords = ["Cryst@l88s", "Phantom#42e", "T1tanKeyz!"]

expected = [('StormCiphers', 'Cryst@l88s'), ('CodeHawk', 'Phantom#42e'), ('AstroForge', 'T1tanKeyz!')]

result = naloge.vault(usernames, passwords)

test_case.assertEqual(len(expected), len(result), "Napacna .")

#test_case.assertEqual(expected, result)