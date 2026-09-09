import unittest
import naloge

test_case = unittest.TestCase()

slovar = {'Casual': [('Dumb Ways To Draw', 'Teen', 3.9, True)],
    'Productivity': [('Todoist', 'Everyone', 4.5, True), ('Forest', 'Everyone', 4.7, True)]}

expected = {'Casual': 3.9, 'Productivity': 4.6}

actual = naloge.povprecje_po_kategorijah(slovar)

test_case.assertEqual(list(expected.values()), list(actual.values()), "Napacne vrednosti slovarja.")