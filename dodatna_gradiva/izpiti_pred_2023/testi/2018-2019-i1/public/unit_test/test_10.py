import unittest

import izpit

test_case = unittest.TestCase()

genre = "comedy"
actual = izpit.povprecna_dolzina([], genre)

test_case.assertEqual(actual, 0, "Napačna vrednost za žanr '%s'" % genre)
