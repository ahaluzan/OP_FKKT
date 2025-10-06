'''najljubsi'''
import unittest
from filmi import *

test_case = unittest.TestCase()
from unittest import mock
import io

expected = "Ne joči, Peter"

def test_najljubsi():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: expected
    najljubsi('podatki/naj_film.txt')
    test_case.assertEqual(preberi('podatki/naj_film.txt').rstrip(), expected)
    mock.builtins.input = original_input

test_najljubsi()