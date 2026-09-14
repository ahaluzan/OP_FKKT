import unittest
import naloge
import variables
import inspect

test_case = unittest.TestCase()

expected = True

if 'nacin' in list(inspect.signature(naloge.po_spolih).parameters.keys()):
    actual = True
else:
    actual = False

test_case.assertEqual(expected, actual, "Napacno poimenovanje opcijskega argumenta.")