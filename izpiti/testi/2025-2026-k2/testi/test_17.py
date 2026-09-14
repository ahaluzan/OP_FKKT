import unittest
import naloge
import inspect

test_case = unittest.TestCase()

actual = "kilometri" in inspect.signature(naloge.v_slovar).parameters

test_case.assertEqual(True, actual, "Napacno poimenovanje opcijskega argumenta.")