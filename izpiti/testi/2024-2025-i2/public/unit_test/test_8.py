import unittest
import naloge

test_case = unittest.TestCase()

podatki = [('Dumb Ways To Draw', 'Casual', 3.9, 50095, True, 2021, 'Teen'),
    ('SkyView Lite', 'Education', 4.4, 43828, True, 2019, 'Everyone'),
    ('Todoist', 'Productivity', 4.5, 226044, True, 2021, 'Everyone'),
    ('Forest', 'Productivity', 4.7, 340816, True, 2021, 'Everyone'),
    ('TED', 'Education', 4.6, 208571, True, 2020, 'Everyone 10+')]

expected = {'Casual': [('Dumb Ways To Draw', 'Teen', 3.9, True)],
 'Education': [('SkyView Lite', 'Everyone', 4.4, True), ('TED', 'Everyone 10+', 4.6, True)],
 'Productivity': [('Todoist', 'Everyone', 4.5, True), ('Forest', 'Everyone', 4.7, True)]}

actual = naloge.po_kategorijah(podatki, 2019)

test_case.assertEqual(expected, actual, "Napacna vsebina slovarja.")