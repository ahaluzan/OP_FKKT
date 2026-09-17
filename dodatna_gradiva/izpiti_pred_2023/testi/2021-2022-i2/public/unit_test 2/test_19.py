import unittest

import izpit
from .TEST_DATA import *

test_case = unittest.TestCase()

expected = False
actual = izpit.najvec_soncnih({(16, 2, 2021): (4.4, 73.26, 9.5, 'Partially cloudy'), 
(17, 2, 2021): (7.2, 86.07, 7.2, 'Rain, Overcast')})

test_case.assertEqual(actual, expected)

