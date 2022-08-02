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
    
    def test_max_at_end(self):
        """Testing for max integer at the end of the list"""
        n = [1, 34, 43, 3, 59]
        self.assertEqual(max_integer(n), 59)
    
    def test_max_at_beginning(self):
        """Testing for max integer at the beinning of the list"""
        n = [59, 1, 34, 43, 3]
        self.assertEqual(max_integer(n), 59)
        
    def test_max_at_middle(self):
        """Testing for max integer at the middle of the list"""
        n = [1, 34, 59, 32, 12]
        self.assertEqual(max_integer(n), 59)
    
    def test_one_negative(self):
        """Test for one negative number in the list"""
        n = [1, 32, 4, 14, -6]
        self.assertEqual(max_integer(n), 32)      
    
    def test_all_negative(self):
        """Testing for list with all negative numbers"""
        n = [-1, -34, -43, -3, -59]
        self.assertEqual(max_integer(n), -1)
        
    def test_single_item(self):
        """Test for only one list item"""
        self.assertEqual(max_integer([5]), 5)
    
    def test_non_int(self):
        """Testing for a non integer type list"""
        n = [1, 2, "Ian", 3, 7]
        self.assertRaises(TypeError)






if __name__ == "__main__":
    unittest.main()