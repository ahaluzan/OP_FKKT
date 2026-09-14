import unittest
import naloge

test_case = unittest.TestCase()

podatki2 = [('Central and Eastern Europe', 'Poland', False, 1.246, 1.047, 0.691, 0.452, 0.055), 
            ('Western Europe', 'Switzerland', 7.509, 1.527, False, 0.863, 0.586, 0.412), 
            ('Central and Eastern Europe', 'Latvia', False, 1.218, 0.95, 0.64, 0.28, 0.089), 
            ('Central and Eastern Europe', 'Slovakia', False, 1.28, 1.083, False, 0.234, 0.029), 
            ('Latin America and Caribbean', 'Nicaragua', 5.992, 0.694, 0.895, 0.652, 0.466, False)]

expected = {'Western Europe': [('Switzerland', 7.509)], 
            'Latin America and Caribbean': [('Nicaragua', 5.992)]}

actual = naloge.v_slovar(podatki2)

test_case.assertEqual(expected, actual, "Vsebina slovarja ni pravilna v primeru, ko podatki vsebujejo False.")
