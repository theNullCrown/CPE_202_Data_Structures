## Name: Allie Blaising 


import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_reverse(self):
        t_list = OrderedList()
        self.assertEqual(t_list.python_list_reversed(), [])
        t_list.add(10)
        t_list.add(70)
        self.assertEqual(t_list.python_list_reversed(), [70,10])

    def test_size(self):
        t_list = OrderedList()
        self.assertEqual(t_list.size(), 0)
        t_list.add(10)
        t_list.add(9)
        t_list.add(50)
        self.assertEqual(t_list.size(), 3)


    def test_is_empty(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())

    def test_add(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(70)
        self.assertEqual(t_list.python_list(), [10,70])

    def test_remove(self):
        t_list = OrderedList()
        t_list.add(80)
        t_list.add(15)
        self.assertEqual(t_list.python_list(), [15,80])
            

    def test_index(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(9)
        t_list.add(2)
        self.assertEqual(t_list.index(10),2)
        self.assertEqual(t_list.index(9),1)
        self.assertEqual(t_list.index(2),0)
        self.assertEqual(t_list.index(15),None)


    def test_search(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(9)
        t_list.add(999)
        self.assertTrue(t_list.search(10))
        self.assertTrue(t_list.search(9))
        self.assertTrue(t_list.search(999))
        self.assertFalse(t_list.search(60))


    def test_pop(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(9)
        self.assertEqual(t_list.pop(0),9)
        t_list.add(10)
        with self.assertRaises(IndexError):
            t_list.pop(-5)
        with self.assertRaises(IndexError):
            t_list.pop(15)

    def test_python_list(self):
        t_list = OrderedList()
        self.assertEqual(t_list.python_list(), [])
        t_list.add(10)
        t_list.add(9)
        t_list.add(50)
        self.assertEqual(t_list.python_list(), [9,10, 50])






if __name__ == '__main__': 
    unittest.main()
