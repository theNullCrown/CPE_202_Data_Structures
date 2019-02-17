
## Name: Allie Blaising 

import unittest
from queue_array import *

class TestLab3(unittest.TestCase):
    def test_queue(self):
        q = Queue(5)

    def test_empty(self): 
        q = Queue(5)
        self.assertEqual(q.is_empty(), True)

    def test_full(self): 
        q = Queue(5)
        self.assertEqual(q.is_full(), False)

    def test_size(self): 
        q = Queue(5)
        q.enqueue('thing')
        q.enqueue('test')
        self.assertEqual(q.items, ['thing', 'test', None, None, None])
        self.assertEqual(q.dequeue(), 'thing')
        self.assertEqual(q.size(), 1)

    def test_enqueue(self): 
        q = Queue(5)
        q.enqueue('thing')
        q.enqueue('test')
        self.assertEqual(q.items, ['thing', 'test', None, None, None])
        q.enqueue('thing')
        q.enqueue('thing')
        q.enqueue('thing')
        with self.assertRaises(IndexError):
            q.enqueue('thing_not')

    def test_dequeue(self): 
        q = Queue(3)
        q.enqueue('thing')
        q.enqueue('test')
        q.dequeue()
        q.dequeue()
        self.assertEqual(q.items, [None,None, None])


# enqueue full 

## model stack tests 

if __name__ == '__main__': 
    unittest.main()
