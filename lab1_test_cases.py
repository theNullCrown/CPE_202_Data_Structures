# CPE 202 Lab 1 Test Cases
## Name: Allie Blaising

import unittest
from lab1 import *


class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        tlist = [10, 9, 8 ,4, 9]
        self.assertEqual(max_list_iter(tlist),10) ## checks last 
        tlist = [9, 8, 10 ,4, 9]
        self.assertEqual(max_list_iter(tlist),10) ## checks middle 
        tlist = [5, 9, 8 ,4, 10]
        self.assertEqual(max_list_iter(tlist),10)
        tlist = [-10, -9, -1 ,-4, -9]
        self.assertEqual(max_list_iter(tlist),-1) ## checks negative orders 
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        tlist = []
        self.assertEqual(max_list_iter(tlist), None) # used to check exception for if list is empty and should return None 

    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):  # uses context manager to check exception
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([-8,2,4]), [4, 2, -8]) ## checks negatives 
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec(""),"")
        self.assertEqual(reverse_rec("abcd"),"dcba")

## odd, right in the middle

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4) 
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0) ## checks first number 
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8)  ## checks last number 
        list_val = [2, 3, 4, 5]
        self.assertEqual(bin_search(6, 0, len(list_val)-1, list_val), None) ## checks to make sure returns None is target not found 
        list_val = [2, 8, 4, 5, 9, 10, 11]
        self.assertEqual(bin_search(13, 0, len(list_val)-1, list_val), None) ## checks 
        list_val = None
        with self.assertRaises(ValueError):  # uses context manager to check exception
            bin_search(1, 0, 10, list_val) 


if __name__ == "__main__":
        unittest.main()

    
