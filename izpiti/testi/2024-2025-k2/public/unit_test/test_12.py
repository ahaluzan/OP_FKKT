import unittest
import naloge

test_case = unittest.TestCase()

podatki = {'Western Europe': [('Norway', 7.498), ('Finland', 7.413)],
           'Central and Eastern Europe': [('Slovenia', 5.768), ('Turkmenistan', 5.658)],
           'Latin America and Caribbean': [('Peru', 5.743)]}

expected = {'Western Europe': 7.46, 
            'Central and Eastern Europe': 5.71, 
            'Latin America and Caribbean': 5.74}

actual = naloge.regijska_povprecja(podatki)

#test_case.assertEqual([str(v) for k,v in expected.items()], [str(v) for k,v in actual.items()], "Napacno zaokrozevanje.")
test_case.assertEqual([v for k,v in expected.items()], [v for k,v in actual.items()], "Napacno zaokrozevanje.")