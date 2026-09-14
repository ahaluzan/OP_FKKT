import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = ("Shoes", [20])

actual = naloge.najvec_vrednosti({"Shoes":[20]})

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije.")