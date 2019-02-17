# name: Allie Blaising 

import unittest
from stack_array import Stack
        
class TestLab2(unittest.TestCase):

    def test_init(self):
        stack = Stack(5)
        self.assertEqual(stack.items, [None]*5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self):
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5,[1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)

    def test_repr(self):
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

    def test_empty(self): 
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.is_empty(), False)
        stack = Stack(5)
        self.assertEqual(stack.is_empty(), True)

    def test_full(self): 
        stack = Stack(3, [3, 4, 5])
        self.assertEqual(stack.is_full(), True)
        stack = Stack(3, [3, 4])
        self.assertEqual(stack.is_full(), False)

    def test_push(self): 
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.push(8), Stack(5, [1, 2, 8]))

    def test_pop(self): 
        stack = Stack(5, [1, 2, 4])
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 2)
        stack = Stack(5, [9, 2, 4, "True"])
        self.assertEqual(stack.pop(), "True")

    def test_peek(self): 
        stack = Stack(80, [])
        with self.assertRaises(IndexError):
            stack.peek()
        stack = Stack(6, [1, 2, 4, 6])
        self.assertEqual(stack.peek(), 6)
        stack = Stack(9, [1, 2, 9])
        self.assertEqual(stack.peek(), 9)


    def size(self): 
        stack = Stack(6, [1, 2, 4])
        self.assertEqual(stack.size(), 3)
        stack = Stack(6, [1, 2, 8, 2, 3])
        self.assertEqual(stack.size(), 5)
        stack = Stack(7, [])
        self.assertEqual(stack.size(), 0)




if __name__ == '__main__': 
    unittest.main()
