#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxIteger(unittest.TestCase):
    """Unittest class for max_integer"""
    def test_module_docstring(self):
        """Tests for module docstring"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)
        
    def test_function_docstring(self):
        """Test for max_integer function docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)
    
    def test_max_integer(self):
        """test for list passed is an empty list"""
        self.assertEqual(max_integer([]), None)
        
    









if __name__ == "__main__":
    unittest.main()