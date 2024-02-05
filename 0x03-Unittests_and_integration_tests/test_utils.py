#!/usr/bin/env python3
"""import libraries"""
import unittest
import unittest.mock
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
    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
    )
    def test_get_json(self, test_url, test_payload):
        """test get json func"""
        # Configure the mock_get to return a Mock with a json method
        configure = {'return_value.json.return_value': test_payload}
        patcher = unittest.mock.patch('utils.requests.get', **configure)
        mock = patcher.start()
        self.assertEqual(utils.get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()


if __name__ == '__main__':
    unittest.main()
