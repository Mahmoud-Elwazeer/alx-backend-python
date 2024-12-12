#!/usr/bin/env python3
"""import libraries"""
import unittest
import unittest.mock
from parameterized import parameterized
import utils
from utils import memoize
from unittest.mock import patch


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


class TestClass:
    """class using for test"""
    def a_method(self):
        """method 1"""
        return 42

    @memoize
    def a_property(self):
        """property for method"""
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """class with a test_memoize method."""
    def test_memoize(self):
        """test memoize decorador"""
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            instance = TestClass()

            # Call the memoized property twice
            result1 = instance.a_property
            result2 = instance.a_property

            # Assert that the correct result is returned both times
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Assert that `a_method` was called only once
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
