import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.statistika10.values()

actual = naloge.statistika(variables.slovar_izdelek10).values()

test_case.assertCountEqual(expected, actual, "Napacne vrednosti v slovarju.")
