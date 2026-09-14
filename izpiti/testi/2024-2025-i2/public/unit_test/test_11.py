import unittest
import naloge

test_case = unittest.TestCase()

slovar = {'Casual': [('Dumb Ways To Draw', 'Teen', 3.9, True)],
 'Education': [('SkyView Lite', 'Everyone', 4.4, True), ('TED', 'Everyone 10+', 4.6, True)],
 'Productivity': [('Todoist', 'Everyone', 4.5, True), ('Forest', 'Everyone', 4.7, True)]}

expected = {'Casual': 3.9, 'Education': 4.5, 'Productivity': 4.6}

actual = naloge.povprecje_po_kategorijah(slovar)

test_case.assertEqual(expected, actual, "Napacna vsebina slovarja.")