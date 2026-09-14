import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

genre = "slovenska politika"
actual = izpit.povprecna_dolzina(READ, genre)

test_case.assertEqual(actual, 0, "Napačna vrednost za žanr '%s'" % genre)
