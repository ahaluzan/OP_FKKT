import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = variables.slovar_izdelek5.values()

actual = naloge.v_slovar(variables.kava5).values()

test_case.assertCountEqual(expected, actual, "Napacne vrednosti v slovarju.")
