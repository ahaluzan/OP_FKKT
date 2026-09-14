import unittest

import naloga

test_case = unittest.TestCase()

distributed = naloga.porazdelitev_ocen({})

test_case.assertEqual(distributed, {5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, "Izračunana porazdelitev ocen ni pravilna")
