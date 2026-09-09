import unittest
import naloge

test_case = unittest.TestCase()

podatki = [('Forest', 'Productivity', 4.7, 340816, True, 2021, 'Everyone'),
 ('Calm', 'Health & Fitness', 4.3, 402349, True, 2021, 'Everyone'),
 ('TED', 'Education', 4.6, 208571, True, 2020, 'Everyone 10+'),
 ('Skillshare', 'Education', 4.5, 46058, True, 2021, 'Everyone'),
 ('Asana', 'Business', 4.5, 34128, True, 2021, 'Everyone')]

expected = [i[0] for i in podatki]

actual = [i[0] for i in naloge.preberi_podatke("data/apps_imena.txt")]

test_case.assertEqual(expected, actual, "Neustrezno krajsanje naslovov.")