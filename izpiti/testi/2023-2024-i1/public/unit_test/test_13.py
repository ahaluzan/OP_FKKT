'''zbirke'''
import unittest

import naloge
from .TEST_DATA import *

test_case = unittest.TestCase()

sez = [('John Green', 'Looking for Alaska', 'standalone', 4.13, 331, [])]

act = naloge.zbirke(sez)
exp = []

test_case.assertEqual(type(act), type(exp), "Napacen podatkovni tip.")
test_case.assertEqual(act, exp, "Napacno delovanje pri 'standalone'.")

