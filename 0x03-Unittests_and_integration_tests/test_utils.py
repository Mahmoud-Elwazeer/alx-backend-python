#!/usr/bin/env python3
"""import libraries"""
import unittest
import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """class using usnittest to test methdods"""
    @parameterized.expand([
        nested_map={"a": 1}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a", "b")
    ])
    def test_access_nested_map(self, nested_map, path):
        """test accesdd nested map"""
        self.assertEqual(({"a": 1}, "a"), "a")

if __name__ == '__main__':
    unittest.main()
