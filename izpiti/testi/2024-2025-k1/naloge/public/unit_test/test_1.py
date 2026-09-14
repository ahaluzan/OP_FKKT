'''vault'''
import unittest
import naloge

test_case = unittest.TestCase()

usernames1 = ["alice123", "bob456", "carol789", "dave321", "erin654", "frank987", "grace432"]
passwords1 = ["pass123", "secure456", "mypassword789", "qwerty321", "letmein654", "trustme987", "openup432"]

expected = [('alice123', 'pass123'), ('bob456', 'secure456'), ('carol789', 'mypassword789'), ('dave321', 'qwerty321'), ('erin654', 'letmein654'), ('frank987', 'trustme987'), ('grace432', 'openup432')]

actual = naloge.vault(usernames1,passwords1)

test_case.assertEqual(type(expected[0]), type(actual[0]), "Napacen podatkovni tip v seznamu.")