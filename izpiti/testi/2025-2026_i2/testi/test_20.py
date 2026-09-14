import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = {'L': ['Boots', 'T-shirt', 'Shoes', 'Shoes', 'Socks', 'Skirt', 'Jewelry'],
 'S': ['Coat', 'Handbag', 'Jeans', 'Shoes'],
 'M': ['Blouse','Sunglasses','Hat','Shirt','Shoes','Sweater','Sweater','Jeans','Hoodie'],
 'XL': ['Backpack', 'Boots']}

actual = naloge.pripravi_slovar(variables.shop30, -3, -4)

test_case.assertCountEqual(expected, actual, "Napacno vracanje funkcije.")