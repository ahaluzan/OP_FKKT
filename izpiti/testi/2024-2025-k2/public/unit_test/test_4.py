import unittest
import naloge

test_case = unittest.TestCase()

expected = [('Central and Eastern Europe', 'Poland', False, 1.246, 1.047, 0.691, 0.452, 0.055), ('Sub-Saharan Africa', 'Liberia', 3.622, 0.107, 0.504, 0.232, 0.257, 0.049), ('Sub-Saharan Africa', 'Mauritius', 5.648, 1.144, 0.757, 0.662, 0.461, 0.052), ('Eastern Asia', 'Mongolia', 4.907, 0.989, 1.09, 0.555, 0.36, 0.033), ('Western Europe', 'Switzerland', 7.509, 1.527, False, 0.863, 0.586, 0.412), ('Sub-Saharan Africa', 'Zimbabwe', 4.193, 0.35, 0.715, 0.16, 0.254, 0.086), ('Southern Asia', 'India', 4.404, 0.74, 0.292, 0.451, 0.403, 0.087), ('Central and Eastern Europe', 'Latvia', 5.56, 1.218, 0.95, 0.64, 0.28, 0.089), ('Central and Eastern Europe', 'Slovakia', 6.078, 1.28, 1.083, False, 0.234, 0.029), ('Latin America and Caribbean', 'Nicaragua', 5.992, 0.694, 0.895, 0.652, 0.466, False)]

actual = naloge.preberi_podatke("sreca10.txt")

test_case.assertEqual(expected, actual, "Napacna obravnava manjkajocih podatkov.")
