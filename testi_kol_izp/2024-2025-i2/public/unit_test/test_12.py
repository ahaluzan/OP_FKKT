import unittest
import naloge

test_case = unittest.TestCase()

slovar = { 'Education': [('SkyView Lite', 'Everyone', 4.4, True), ('TED', 'Everyone 10+', 4.6, True)]}

expected = {'Education': 4.5}

actual = naloge.povprecje_po_kategorijah(slovar)

test_case.assertEqual(expected, actual, "Napacna vsebina slovarja.")