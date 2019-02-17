import unittest
from binary_search_tree import *
 
# Allie Blaising 

class TestLab4(unittest.TestCase):

    def is_empty_test(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertFalse(bst.is_empty())

    def search_test(self): 
        bst = BinarySearchTree()
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertFalse(bst.search(14))
        bst.insert(188, 'stuff')
        self.assertTrue(bst.search(188))


    def insert_test(self): 
        bst = BinarySearchTree()
        bst.insert(10, 'other')
        bst.insert(20, 'other 2')

    def find_min_test(self): 
        bst = BinarySearchTree() 
        bst.insert(10, 'other')
        bst.insert(12, 'other')
        bst.insert(13, 'other')
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(5, 'other')
        self.assertEqual(bst.find_min(), (5, 'other'))


    def find_max_test(self): 
        bst = BinarySearchTree() 
        bst.insert(10, 'other')
        bst.insert(12, 'other')
        bst.insert(13, 'other')
        self.assertEqual(bst.find_max(), (13, 'other'))
        bst.insert(40, 'other')
        self.assertEqual(bst.find_max(), (40, 'other'))

    def find_tree_height_test(self):
        bst = BinarySearchTree() 
        bst.insert(10, 'other')
        bst.insert(12, 'other')
        bst.insert(13, 'other')
        self.assertEqual(bst.tree_height(), 3)
        bst.insert(13, 'other')
        bst.insert(13, 'other')
        self.assertEqual(bst.tree_height(), 5)

    def test_pre_order(self): 
        bst = BinarySearchTree() 
        bst.insert(50, 'other')
        bst.insert(60, 'other')
        bst.insert(40, 'other')
        bst.insert(70,'test')
        bst.insert(45,'test')
        bst.insert(30,'test')
        self.assertEqual(bst.preorder_list(), [50, 40, 30, 45, 60, 70])


    def test_extra(self):
        bst = BinarySearchTree()
        bst.insert(50, 'other')
        bst.insert(60, 'other')
        bst.insert(40, 'other')
        bst.insert(70,'test')
        bst.insert(45,'test')
        bst.insert(30,'test')
        self.assertEqual(bst.inorder_list(),[30, 40, 45, 50, 60, 70])



def add(self, item):



if __name__ == '__main__': 
    unittest.main()
