import unittest
from preproste_funkcije import *

test_case = unittest.TestCase()

test_case.assertFalse(prekrivajoca_seznama([1, 2, 3, 4, 5], [30, 33]), msg='prekrivajoca_seznama([1, 2, 3, 4, 5], [30, 33]) -> False')
test_case.assertTrue(prekrivajoca_seznama([7486, 4087, -4345, -8861, -2463, -2771, 4171, 4179, -700, 2816, 2255, 9504, -4560, -8701, -4697, -6573, 9737, 4613, 6097, 2646, 6336, 3335, 400, 9930, 5872, 3560, 2214, 693, 8512, 8856, 8740, 6056, -4472, -2075, 624, -7673, -2895, 3079, -4207, -8737, -231, 2846, 2539, 4414, 5985, -8339, -8281, -6742, 604, 9653, -916, 1519, -902, 6140, -5568, 2282, -5796, -8150, -2703, -8734, -6484, -5863, 4510, 5706, 1247, -6667, -5270, -6919, 1246, 9311, 7408, 8882, -8886, -8991, 6264, -2846, -8053, 8839, -3713, -6449, -2559, 2971, 2356, 3606, 2340, -1868, -356, 4227, -7318, 9325, -7716, 4582, -2592, -176, -1129, -2852, 9865, 8390, -5248, 3254, 3844, -2915, -36, -1355, 1051, 9132, 4936, 509, 1830, -3, -3132, 7728, 9901, -7834, 3834, -5491, 110, 2769, 6029, -2532, 3437, -9925, 1484, 7216, 1282, -8645, -3526, -3169, 9169, 4121, -5317, -2655, 218, -2847, 8018, 6557, 2595, 2300, 9856, 142, 4264, -7221, 6273, 5147, 3521, -5515, 119, -7456, 6100, -699, -1454, 212, 1587, 7622, -7799, 1237, -1023, -8788, 7283, 3389, 2339, -8813, 9998, 4717, -7456, 2577], [-9745, 2760, -3904, 2062, 4597, -6126, -8644, -5210, 9926, 2794, -370, -2803, -3491, -5339, 3911, 852, 8389, -2548, -3755, 3519, 5698, -6646, 2713, -2352, 591, 8954, -9311, -1826, 1607, 1367, -681, -4791, -6498, -9510, -8351, -9728, -7416, -1384, 8632, 2558, -9480, -6702, 6739, -5160, 6527, 7518, -2820, 3440, -3261, -2253, 4001, -8318, -4853, -9226, 1683, -3998, 5256, -9427, -5323, -8205, 8737, -2335, -1642, -5278, 7411, -4687, -8188, 5885, 1135, -9314, 6692, 8007, 8950, -6002, 1535, 4315, 9150, 6991, -1195, 8940, -1286, -5998, 4789, -4744, -8213, -5014, 8300, 2878, -1581, 8239, -1446, -8696, 9842, -4869, 9117, 8206, -3606, -372, -2334, -3970, -8852, 2264, 3731, -5370, 9577, -4540, -3780, -2237, 7240, 2179, -7991, 7547, 7548, 182, -9307, -477, -1436, 3190, -7504, -7467, -1168, -7255, 3908, 6326, -2173, 2939, -3565, 4384, 6576, -1350, 3489, -5292, -8646, -8989, 8482, 7873, -2356, -2820, -3687, -6413, -3451, -1818, 8734, 7835, 8478, 2021, 5757, 7585, -5919, -713, 9227, 4957, -4350, -5302, 935, 3723, 6700, -3041, -9272, -7734, -7640, -2401, 489, -6904, 4886, 1714, -4115, -1767, -1973, -1263, -6800, 4889, 1553, -9389, 1321, -9367, -6786, 2339, -2782, 407, 8021, -2785, -387, -2153, 2338, 8449, 3653, -850, 6858, -4907, -9519, -2095, 4676, -4680, 1599, -1880, -3516, -621, -1511, -957, -4196, -8870, -3120, 807, -3816, -5089, 9714, 9980, -2544, 5329, 4703, -6016, 7972, -50, -322, -2174, -8943, -1630, -4583, 439, 2945, 9481, 3629, -5929, 6174, -7124, -4340, -7626, 1371, 5983, 1936, -2155, -1781, -3168, 8437, -2832, -3947, 334, 1765, -1449, 4711, 3517, -1441, 8348, 5203, -5278, -8502, 8652, -7861, -4977, 6387, -752, 488, -5096, 2497, 9017, -9051, -276, -6658, 3770, 4732, 8043, -5849, -1381, 6252, 8982, 4879, 1851, 6786, -6662, -6434, 5173, -945, 314, -9971, -6109, 8345, -6931, -8131, -1326, -1600, -6595, 5141, -8791, 3861, 6802, -5694, -1662, 2164, -7954, 3537, -4342, -9681, -6960, -6793, 1487, -144, 2248, 2620, 6357, -9379, 558, -960, 8169, 1674, -6474, 1293, -7082, 2805, -3633, 7816, -2142, -3468, 3889, -9492, -8677, -2388, -5855, -2367, 9978, -2101, 6242, 2107, -8703, -3496, 8099, 5410, 3328, -1032, -1318, 648, 968, -1087, -4104]), msg='prekrivajoca_seznama([7486, 4087, -4345, -8861, -2463, -2771, 4171, 4179, -700, 2816, 2255, 9504, -4560, -8701, -4697, -6573, 9737, 4613, 6097, 2646, 6336, 3335, 400, 9930, 5872, 3560, 2214, 693, 8512, 8856, 8740, 6056, -4472, -2075, 624, -7673, -2895, 3079, -4207, -8737, -231, 2846, 2539, 4414, 5985, -8339, -8281, -6742, 604, 9653, -916, 1519, -902, 6140, -5568, 2282, -5796, -8150, -2703, -8734, -6484, -5863, 4510, 5706, 1247, -6667, -5270, -6919, 1246, 9311, 7408, 8882, -8886, -8991, 6264, -2846, -8053, 8839, -3713, -6449, -2559, 2971, 2356, 3606, 2340, -1868, -356, 4227, -7318, 9325, -7716, 4582, -2592, -176, -1129, -2852, 9865, 8390, -5248, 3254, 3844, -2915, -36, -1355, 1051, 9132, 4936, 509, 1830, -3, -3132, 7728, 9901, -7834, 3834, -5491, 110, 2769, 6029, -2532, 3437, -9925, 1484, 7216, 1282, -8645, -3526, -3169, 9169, 4121, -5317, -2655, 218, -2847, 8018, 6557, 2595, 2300, 9856, 142, 4264, -7221, 6273, 5147, 3521, -5515, 119, -7456, 6100, -699, -1454, 212, 1587, 7622, -7799, 1237, -1023, -8788, 7283, 3389, 2339, -8813, 9998, 4717, -7456, 2577], [-9745, 2760, -3904, 2062, 4597, -6126, -8644, -5210, 9926, 2794, -370, -2803, -3491, -5339, 3911, 852, 8389, -2548, -3755, 3519, 5698, -6646, 2713, -2352, 591, 8954, -9311, -1826, 1607, 1367, -681, -4791, -6498, -9510, -8351, -9728, -7416, -1384, 8632, 2558, -9480, -6702, 6739, -5160, 6527, 7518, -2820, 3440, -3261, -2253, 4001, -8318, -4853, -9226, 1683, -3998, 5256, -9427, -5323, -8205, 8737, -2335, -1642, -5278, 7411, -4687, -8188, 5885, 1135, -9314, 6692, 8007, 8950, -6002, 1535, 4315, 9150, 6991, -1195, 8940, -1286, -5998, 4789, -4744, -8213, -5014, 8300, 2878, -1581, 8239, -1446, -8696, 9842, -4869, 9117, 8206, -3606, -372, -2334, -3970, -8852, 2264, 3731, -5370, 9577, -4540, -3780, -2237, 7240, 2179, -7991, 7547, 7548, 182, -9307, -477, -1436, 3190, -7504, -7467, -1168, -7255, 3908, 6326, -2173, 2939, -3565, 4384, 6576, -1350, 3489, -5292, -8646, -8989, 8482, 7873, -2356, -2820, -3687, -6413, -3451, -1818, 8734, 7835, 8478, 2021, 5757, 7585, -5919, -713, 9227, 4957, -4350, -5302, 935, 3723, 6700, -3041, -9272, -7734, -7640, -2401, 489, -6904, 4886, 1714, -4115, -1767, -1973, -1263, -6800, 4889, 1553, -9389, 1321, -9367, -6786, 2339, -2782, 407, 8021, -2785, -387, -2153, 2338, 8449, 3653, -850, 6858, -4907, -9519, -2095, 4676, -4680, 1599, -1880, -3516, -621, -1511, -957, -4196, -8870, -3120, 807, -3816, -5089, 9714, 9980, -2544, 5329, 4703, -6016, 7972, -50, -322, -2174, -8943, -1630, -4583, 439, 2945, 9481, 3629, -5929, 6174, -7124, -4340, -7626, 1371, 5983, 1936, -2155, -1781, -3168, 8437, -2832, -3947, 334, 1765, -1449, 4711, 3517, -1441, 8348, 5203, -5278, -8502, 8652, -7861, -4977, 6387, -752, 488, -5096, 2497, 9017, -9051, -276, -6658, 3770, 4732, 8043, -5849, -1381, 6252, 8982, 4879, 1851, 6786, -6662, -6434, 5173, -945, 314, -9971, -6109, 8345, -6931, -8131, -1326, -1600, -6595, 5141, -8791, 3861, 6802, -5694, -1662, 2164, -7954, 3537, -4342, -9681, -6960, -6793, 1487, -144, 2248, 2620, 6357, -9379, 558, -960, 8169, 1674, -6474, 1293, -7082, 2805, -3633, 7816, -2142, -3468, 3889, -9492, -8677, -2388, -5855, -2367, 9978, -2101, 6242, 2107, -8703, -3496, 8099, 5410, 3328, -1032, -1318, 648, 968, -1087, -4104]) -> True')
test_case.assertFalse(prekrivajoca_seznama([26993, -95480, 65966, -24333, 16571, 38173, -10287, 55979, -88501, -67657, -51091, -72172, 12541, -60503, 53067, 60569, 42107, 58950, 90660, -86720] , [68047, 41033, 86288, -21019, 53526, 82834, -19055, 99996, 10445, 31398, -96175, -56653, 95489, 71133, -97042, -19584, -50846, -86333, 17159, 50430, -96214, -13615, 73302, -90980, 61382, -60736, 45564, -11395, 64596, 55070]), msg='prekrivajoca_seznama([26993, -95480, 65966, -24333, 16571, 38173, -10287, 55979, -88501, -67657, -51091, -72172, 12541, -60503, 53067, 60569, 42107, 58950, 90660, -86720], [68047, 41033, 86288, -21019, 53526, 82834, -19055, 99996, 10445, 31398, -96175, -56653, 95489, 71133, -97042, -19584, -50846, -86333, 17159, 50430, -96214, -13615, 73302, -90980, 61382, -60736, 45564, -11395, 64596, 55070]) -> False')