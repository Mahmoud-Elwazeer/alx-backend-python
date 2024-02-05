#!/usr/bin/env python3
"""import libraries"""
import unittest
from unittest.mock import MagicMock, patch
from parameterized import parameterized
import utils


class TestAccessNestedMap(unittest.TestCase):
    """class using usnittest to test access_nested_map func"""
    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(self, nested_map, path):
        """test accesdd nested map"""
        self.assertEqual(utils.access_nested_map({"a": 1}, ("a",)), 1)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test accesdd nested map exception"""
        with self.assertRaises(KeyError):
            utils.access_nested_map({}, ("a",))


class TestGetJson(unittest.TestCase):
    """class using usnittest to test get_json func"""
    @patch('requests.get')
    def test_get_json(self, mock):
        """test get json func"""
        mock.return_value = {"payload": True}

        result = utils.get_json("http://example.com")

        self.assertEqual(result, {"payload": True})


if __name__ == '__main__':
    unittest.main()
