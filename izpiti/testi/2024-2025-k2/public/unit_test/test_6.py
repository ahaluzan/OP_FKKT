import unittest
import naloge

test_case = unittest.TestCase()

podatki1 = [('Western Europe', 'Norway', 7.498, 1.577, 1.127, 0.796, 0.596, 0.358), 
            ('Western Europe', 'Finland', 7.413, 1.406, 1.135, 0.811, 0.571, 0.41), 
            ('Central and Eastern Europe', 'Slovenia', 5.768, 1.299, 1.056, 0.792, 0.532, 0.036), 
            ('Latin America and Caribbean', 'Peru', 5.743, 0.996, 0.813, 0.63, 0.375, 0.053), 
            ('Central and Eastern Europe', 'Turkmenistan', 5.658, 1.08, 1.038, 0.44, 0.374, 0.285)]

expected = {'Western Europe': [('Norway', 7.498), ('Finland', 7.413)], 
            'Central and Eastern Europe': [('Slovenia', 5.768), ('Turkmenistan', 5.658)], 
            'Latin America and Caribbean': [('Peru', 5.743)]}

actual = naloge.v_slovar(podatki1)

test_case.assertEqual(expected.keys(), actual.keys(), "Kljuci slovarja se ne ujemajo.") 