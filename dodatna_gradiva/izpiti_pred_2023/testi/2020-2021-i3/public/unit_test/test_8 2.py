import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

arg, expected = DRUGA[0]
actual = izpit.skupaj_vozil(arg)

for i, elem in enumerate(expected[0]):
    test_case.assertEquals(
        type(actual[0][i]),
        type(elem),
        "V posamezni vrstici mora biti element pod indeksom %d, ki ga vraca funkcija 'skupaj_vozil', tipa %s in ne %s" % (
            i, type(elem), type(actual[0][i])),
    )
