#!/usr/bin/env python3
"""import libraries"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """class using usnittest to test methdods"""
    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(self, nested_map, path):
        """test accesdd nested map"""
        self.assertEqual(access_nested_map({"a": 1}, ("a",)), 1)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test accesdd nested map exception"""
        with self.assertRaises(KeyError):
            access_nested_map({}, ("a",))


if __name__ == '__main__':
    unittest.main()
