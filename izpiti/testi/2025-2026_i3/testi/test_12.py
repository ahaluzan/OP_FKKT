import unittest
import naloge
import variables

test_case = unittest.TestCase()

actual = naloge.v_slovar(variables.kava5)

test_case.assertTrue(
    all(isinstance(v, list) and all(isinstance(t, tuple) for t in v) for v in actual.values()),
    "Vrednosti slovarja niso seznami terk."
)
