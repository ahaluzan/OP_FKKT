import unittest
import naloge
import variables

test_case = unittest.TestCase()

expected = 'Slovarja ni mogoce pripraviti.'

actual = naloge.pripravi_slovar([], 0, 1)

test_case.assertEqual(expected, actual, "Napacno vracanje funkcije v primeru praznega seznama. Preverite tudi tipkarske napake.")