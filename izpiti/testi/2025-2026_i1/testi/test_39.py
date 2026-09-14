import unittest
import naloge

test_case = unittest.TestCase()

podatki = [(28, 'UK', 'Beginner', 9, 4.5, 52, 49, 5),
 (43, 'Indonesia', 'Intermediate', 15, 8.2, 62, 30, 5),
 (29, 'USA', 'Beginner', 6, 7.8, 54, 31, 7),
 (40, 'India', 'Advanced', 7, 6.9, 59, 38, 6),
 (52, 'UK', 'Beginner', 2, 4.4, 62, 36, 5),
 (30, 'Germany', 'Intermediate', 3, 10.4, 48, 36, 7),
 (18, 'Pakistan', 'Beginner', 5, 10.6, 46, 34, 5),
 (16, 'UK', 'Beginner', 7, 10.1, 54, 40, 5),
 (44, 'India', 'Beginner', 10, 8.5, 69, 38, 8),
 (28, 'Germany', 'Intermediate', 3, 5.3, 68, 32, 8),
 (21, 'Indonesia', 'Beginner', 15, 11.2, 53, 29, 5),
 (39, 'India', 'Beginner', 1, 4.9, 72, 47, 5),
 (33, 'Pakistan', 'Beginner', 12, 7.4, 60, 34, 5),
 (36, 'Pakistan', 'Advanced', 12, 3.6, 57, 48, 6)]

expected = "UK"

actual = naloge.po_izkusnjah(podatki, "Beginner")

test_case.assertEqual(expected, actual, "Napačno vračanje funkcije.")