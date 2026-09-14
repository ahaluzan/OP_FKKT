import unittest
import naloge

test_case = unittest.TestCase()

podatki3 = [
    ('Sub-Saharan Africa', 'Mauritania', 4.201, 0.614, 0.841, 0.286, 0.127, 0.18),
    ('North America', 'Canada', 7.404, 1.44, 1.096, 0.828, 0.574, 0.313),
    ('Sub-Saharan Africa', 'Burkina Faso', 3.739, 0.32, 0.631, 0.213, 0.334, 0.125),
    ('Latin America and Caribbean', 'Peru', 5.743, 0.996, 0.813, 0.63, 0.375, 0.053),
    ('Sub-Saharan Africa', 'Mali', 4.073, 0.313, 0.863, 0.163, 0.275, 0.136),
    ('Central and Eastern Europe', 'Lithuania', 5.813, 1.269, 1.064, 0.647, 0.189, 0.018),
    ('Western Europe', 'Denmark', 7.526, 1.442, 1.164, 0.795, 0.579, 0.445),
    ('Western Europe', 'Germany', 6.994, 1.448, 1.098, 0.815, 0.535, 0.286),
    ('Middle East and Northern Africa', 'Qatar', 6.375, 1.824, 0.88, 0.717, 0.567, 0.48),
    ('Sub-Saharan Africa', 'Sudan', 4.139, 0.631, 0.819, 0.298, 0.0, 0.1),
    ('Central and Eastern Europe', 'Hungary', 5.145, 1.241, 0.932, 0.676, 0.198, 0.045),
    ('Middle East and Northern Africa', 'Kuwait', 6.239, 1.617, 0.878, 0.636, 0.432, 0.237),
    ('Central and Eastern Europe', 'Kazakhstan', 5.919, 1.229, 0.955, 0.574, 0.405, 0.111),
    ('Central and Eastern Europe', 'Estonia', 5.517, 1.28, 1.052, 0.681, 0.415, 0.185),
    ('Western Europe', 'Iceland', 7.501, 1.427, 1.183, 0.867, 0.566, 0.15),
    ('Latin America and Caribbean', 'Haiti', 4.028, 0.341, 0.296, 0.275, 0.121, 0.145),
    ('Central and Eastern Europe', 'Serbia', 5.177, 1.034, 0.813, 0.646, 0.157, 0.043)]

expected = "Sudan"

actual = naloge.najvecje_bogastvo(podatki3, izbrana_regija="Sub-Saharan Africa")

test_case.assertEqual(expected, actual, "Napacna resitev.") 