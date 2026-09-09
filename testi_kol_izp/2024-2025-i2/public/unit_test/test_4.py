import unittest
import naloge

test_case = unittest.TestCase()

expected = [('Netflix', 'Entertainment', 4.4, 11694633, True, 2021, 'Teen'),
 ('Telegram', 'Communication', 4.5, 470676, True, 2021, 'Mature 17+'),
 ('Headspace', 'Health & Fitness', 4.6, 229799, True, 2021, 'Everyone'),
 ("Simon's Cat Dash", 'Casual', 4.6, 26662, True, 2019, 'Everyone'),
 ('Slack', 'Business', 4.2, 102572, True, 2021, 'Everyone')]

actual = naloge.preberi_podatke("data/apps5.txt")

test_case.assertEqual(expected, actual, "Napacna vsebina seznama.")

