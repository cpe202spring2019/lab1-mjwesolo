import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """This code tests if the ValueError is raised when the list value is None
        and it also tests the function for list with non-repeating values"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([1,2,3,4]), 4)
        self.assertEqual(max_list_iter([1,2,4,3]), 4)
        self.assertEqual(max_list_iter([1,4,2,3]), 4)
        self.assertEqual(max_list_iter([4,3,2,1]), 4)
        
    def test_max_list_repeat(self):    
        """This code tests if the function works with repeated values in a list"""
        self.assertEqual(max_list_iter([4,4,2,3]), 4)
        self.assertEqual(max_list_iter([1,4,4,2]), 4)
        self.assertEqual(max_list_iter([1,2,4,4]), 4)
        self.assertEqual(max_list_iter([4,4,4,1]), 4)
        self.assertEqual(max_list_iter([1,4,4,4]), 4)
        self.assertEqual(max_list_iter([4,4,4,4]), 4)
        self.assertEqual(max_list_iter([4,3,2,2]), 4)
        self.assertEqual(max_list_iter([3,2,2,4]), 4)
        self.assertEqual(max_list_iter([2,2,3,4]), 4)
        self.assertEqual(max_list_iter([3,3,3,4]), 4)
        
        
        
        
    def test_reverse_rec(self):
        """This code tests if the reverse_rec function raises the ValueError if list value
        is None and if the rest of the function works as intended, reversing various lists"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([1,2,3]), [3,2,1])
        self.assertEqual(reverse_rec([1,2,2]), [2,2,1])
        self.assertEqual(reverse_rec([2,2,2]), [2,2,2])
        self.assertEqual(reverse_rec([2,2,1]), [1,2,2])

    def test_bin_search(self):
        """This code tests if the bin_search function raises the ValueError if a list value 
        is None and if the function is properly able to locate items in a sorted list"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(4, 0, 1, tlist)
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)
        self.assertEqual(bin_search(4, 0, high, list_val), 4)
        self.assertEqual(bin_search(0, 0, high, list_val), 0)
        self.assertEqual(bin_search(2, 0, high, list_val), 2)
        self.assertEqual(bin_search(9, 0, high, list_val), 7)
        self.assertEqual(bin_search(10, 0, high, list_val), 8)
        self.assertEqual(bin_search(-1, 0, high, list_val), None) 
        self.assertEqual(bin_search(20, 0, high, list_val), None)
        
        

if __name__ == "__main__":
        unittest.main()

    
