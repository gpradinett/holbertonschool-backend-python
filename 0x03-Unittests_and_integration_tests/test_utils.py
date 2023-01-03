#!/usr/bin/python
"""
Familiarize yourself with the utils.access_nested_map
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    A class for testing utils.access_nested_map method
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, mapp, path, expected):
        """Sucess testing for access_nested_map method
        """
        self.assertEqual(access_nested_map(mapp, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, mapp, path, error):
        """Testing failure of utils.access_nested_map method
        """
        with self.assertRaises(KeyError):
            try:
                access_nested_map(mapp, path)
            except KeyError as e:
                self.assertEqual(e.args[0], error)
                raise
