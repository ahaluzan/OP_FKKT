import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.statistika5.values()

actual = naloge.statistika(variables.slovar_izdelek5).values()

test_case.assertCountEqual(expected, actual, "Napacne vrednosti v slovarju.")
