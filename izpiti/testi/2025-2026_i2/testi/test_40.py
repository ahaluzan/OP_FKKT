import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = {'Backpack', 'Boots', 'Jewelry', 'Scarf', 'Shoes'}

actual = naloge.po_spolih(variables.shop20, nacin="m")

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije v nacinu 'm'.")