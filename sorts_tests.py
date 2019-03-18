import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10, 40, 50, 60, 80]
        comps = selection_sort(nums)
        #self.assertEqual(comps, 5)
        #self.assertEqual(nums, [10, 23])
        self.assertEqual(insertion_sort([1, 2, 3, 55, 5, 6, 8, 7, 9, 111]), 15) 

    def test_selection_sort(self):
        """Test comparisons and sorting for selection sort"""
        nums = [8,7,6,5,4,3,2,1]
        comparisons = selection_sort(nums)
        self.assertEqual(comparisons, 28)
        self.assertEqual(nums, [1,2,3,4,5,6,7,8])
        random.seed(1234) 
        # Generate 5000 random numbers from 0 to 999,999
        randoms = random.sample(range(1000000), 1000)
        randoms_answer = randoms.copy()
        randoms_answer.sort()
        comparisons = selection_sort(randoms)
        self.assertEqual(comparisons, (len(randoms) * (len(randoms) - 1)) / 2)
        self.assertEqual(randoms_answer, randoms)

if __name__ == '__main__': 
    unittest.main()
