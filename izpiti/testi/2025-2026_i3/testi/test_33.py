import unittest
import naloge
import variables

test_case = unittest.TestCase()

actual = naloge.po_spolu(variables.slovar_spol5)

test_case.assertTrue(all(isinstance(v, set) for v in actual.values()), "Vrednosti v slovarju niso mnozice.")
