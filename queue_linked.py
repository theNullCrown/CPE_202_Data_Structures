## Name: Allie Blaising

# Linked list version of ADT Queue

# Node class for use with Queue implemented with linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data    # data held by Node
        self.next = next    # reference to next Node

    def __eq__(self, other):
        return ((type(other) == Node)
          and self.data == other.data
          and self.next == other.next
        )

    def __repr__(self):
        return ("Node({!r}, {!r})".format(self.data, self.next))

class Queue:
    """Implements an efficient Queue ADT using a linked list of Nodes"""

    def __init__(self, capacity, front=None):
        """Creates a queue with a capacity and initializes with front Node"""
        self.capacity = capacity    # capacity of queue
        self.front = front          # front Node of Queue (next item out)
        self.rear = None            # rear Node of Queue (last item in)
        self.num_items = 0          # number of items in queue
        node = front
        while node is not None:     # set number of items based on input
            self.num_items += 1
            self.rear = node        # set rear Node
            node = node.next
            if self.num_items > capacity:
                raise IndexError

    def __eq__(self, other):
        return ((type(other) == Queue)
          and self.capacity == other.capacity
          and self.front == other.front
        )

    def __repr__(self):
        return ("Queue({!r}, {!r})".format(self.capacity, self.front))

# ----------------------------- #

    def is_empty(self):
        return self.num_items == 0

        """Returns true if the queue is empty and false otherwise"""

    def is_full(self):
        return self.num_items == self.capacity
        """Returns true if the queue is full and false otherwise"""

    def enqueue(self, item):
        if self.is_full(): # can only 
        # enqueue if there is a "free entry" in our array, i.e. if num_items != capacity of queue
          raise IndexError
        if self.is_empty():  
            temp = Node(item)
            self.rear = temp # point new enqueue node to the node currently considered the rear in the gueue (i.e. at self.rear)
            self.rear = temp # change self.rear to now reference the new item 
            self.num_items += 1  # increment num_items so we can keep track of when we hit capacity after enqueue   
        else: 
            temp = Node(item)
            self.rear.next = temp 
            self.rear = temp 
            self.num_items += 1 
        return self

        """enqueues item"""

    def dequeue(self):
        if not self.is_empty(): # if there are no items in the queue then we can't dequeue anything 
            temp = self.front.data # self.front.data stores Node value e.g. 4 from Node(4) 
            self.front = self.front.next # once we extract dequeued item, we will change self.front to 
            # point to the next node in the queue with self.front.next 
            self.num_items -= 1  # decrement 
            return temp # return item dequeued 
        else: 
            raise IndexError
        """dequeues item"""

    def size(self):
        return self.num_items
        """Returns the number of items in the queue"""
