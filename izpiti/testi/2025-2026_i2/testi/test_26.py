import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = None 

actual = naloge.najvec_vrednosti({"Shoes":[], "T-Shirt":[]})

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije")