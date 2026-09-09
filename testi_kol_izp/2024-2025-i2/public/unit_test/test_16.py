import unittest
import naloge

test_case = unittest.TestCase()

podatki = [('Netflix', 'Entertainment', 4.4, 11694633, True, 2021, 'Teen'),
    ('Telegram', 'Communication', 4.5, 470676, True, 2021, 'Mature 17+'),
    ('Headspace', 'Health & Fitness', 4.6, 229799, True, 2021, 'Everyone'),
    ('TED', 'Education', 4.6, 208571, True, 2020, 'Everyone 10+'),
    ("Simon's Cat Dash", 'Casual', 4.6, 26662, True, 2019, 'Everyone'),
    ('SkyView Lite', 'Education', 4.4, 43828, True, 2019, 'Everyone'),
    ('Slack', 'Business', 4.2, 102572, True, 2021, 'Everyone')]

expected = (4.47, 26662)

actual = naloge.avg_per(podatki, 0.1)

test_case.assertEqual(actual, expected, "Napacno vracanje funkcije.")

