## Name: Alllie Blaising 

import unittest

from queue_linked import * 

class TestLab3(unittest.TestCase):
    def test_queue_linked(self):
        init_queue = Node(2, Node(1, None))
        queue = Queue(5, init_queue)
        self.assertEqual(queue.front, Node(2, Node(1, None)))

    def test_empty(self): 
        init_queue = Node(2, Node(1, None))
        queue = Queue(5, init_queue)
        self.assertEqual(queue.is_empty(), False)

    def test_full(self): 
        q = Queue(5)
        q.enqueue(Node(2)) 
        self.assertEqual(q.is_full(), False)

    def test_size(self): 
        init_queue = Node(2, Node(1, None))
        queue = Queue(5, init_queue)
        self.assertEqual(queue.dequeue(), 2) 
        self.assertEqual(queue.enqueue(3), Queue(5, Node(1, Node(3, None))))  
        self.assertEqual(queue.size(), 2) 

    def test_enqueue(self): 
        init_queue = Node(2, Node(1, None))
        queue = Queue(3, init_queue)
        self.assertEqual(queue.dequeue(), 2) 
        self.assertEqual(queue.enqueue(3), Queue(3, Node(1, Node(3, None))))  

    def test_dequeue(self): 
        init_queue = Node(2, Node(1, None))
        queue = Queue(5, init_queue)
        self.assertEqual(queue.dequeue(), 2) 
        self.assertEqual(queue.enqueue(3), Queue(5, Node(1, Node(3, None))))  
        self.assertEqual(queue.size(), 2) 
        self.assertEqual(queue.dequeue(), 1) 
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.dequeue()



if __name__ == '__main__': 
    unittest.main()
