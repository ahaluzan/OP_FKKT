'''metode_datiranja'''
import unittest
from izpit import *

test_case = unittest.TestCase()

input = [['Vesuvius', 10048, 3, (-600, None), (None, None), 'Anthropology'], ['Vesuvius', 10050, 5, (79, 10), (79, 10), 'Historical Observations'], ['Mauna Loa', 10157, 0, (100, None), (None, None), 'Radiocarbon'],['Tambora', 16231, 7, (1812, None), (1815, 7), 'Historical Observations'], ['Pinatubo', 16867, 6, (1991, 4), (1991, 9), 'Historical Observations'], ['Kikai', 16980, 7, (-4350, None), (None, None), 'Radiocarbon'], ['Aira', 17051, 5, (1471, 11), (1476, 10), 'Historical Observations'], ['Unzendake', 17182, 2, (1996, 2), (1996, 5), 'Historical Observations'], ['Asosan', 17198, 3, (864, 11), (None, None), 'Historical Observations'], ['Kujusan', 17363, 2, (1675, 6), (None, None), 'Historical Observations'], ['Fujisan', 17419, 2, (100, None), (None, None), 'Tephrochronology'], ['Fujisan', 17452, 5, (1707, 12), (1708, 2), 'Historical Observations'], ['Shikotsu', 18610, 5, (1667, 9), (1667, 9), 'Historical Observations'], ['Shikotsu', 18612, 5, (1739, 8), (1739, 8), 'Historical Observations'], ['St. Helens', 20557, 5, (1980, 3), (1986, 10), 'Historical Observations'], ['Lengai, Ol Doinyo', 20790, 0, (2011, 6), (2014, 7), 'Historical Observations'], ['Rinjani', 20843, 7, (1257, 7), (None, None), 'Ice Core']]
expected = {'Anthropology': 1, 'Historical Observations': 12, 'Radiocarbon': 2, 'Tephrochronology': 1, 'Ice Core': 1}
test_case.assertEqual(metode_datiranja(input), expected)

