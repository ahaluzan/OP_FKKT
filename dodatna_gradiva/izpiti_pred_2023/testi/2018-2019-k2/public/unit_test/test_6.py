'''oceni_naloge'''
import unittest

import naloga

test_case = unittest.TestCase()

ATTEMPTS = {
    "a": ['a', 'a', 'a'],
}
SOLUTIONS = ['a', 'a', 'a']
CORRECTED = {
    "a": [1, 1, 1],
}

corrected = naloga.oceni_naloge(ATTEMPTS, SOLUTIONS)

test_case.assertEqual(corrected, CORRECTED, "Naloge niso ocenjene pravilno")