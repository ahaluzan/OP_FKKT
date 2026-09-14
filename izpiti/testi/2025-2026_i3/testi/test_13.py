import unittest
import naloge
import variables

test_case = unittest.TestCase()

actual = naloge.v_slovar(variables.kava5)

dolzine = [len(terka) for seznam in actual.values() for terka in seznam]

test_case.assertTrue(all(d == 5 for d in dolzine), "Terke v vrednostih slovarja nimajo pravilnega stevila elementov.")
