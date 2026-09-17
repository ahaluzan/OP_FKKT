import unittest

import naloga

test_case = unittest.TestCase()

ATTEMPTS = {
    "a": ['-', '-', '-'],
}
SOLUTIONS = ['a', 'a', 'a']
CORRECTED = {
    "a": [0, 0, 0],
}

corrected = naloga.oceni_naloge(ATTEMPTS, SOLUTIONS)

test_case.assertEqual(corrected, CORRECTED, "Naloge niso ocenjene pravilno")
