## Name: Allie Blaising

# Queue ADT - circular array implementation

class Queue:
    """Implements an efficient first-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity, init_items=None):
        """Creates a queue with a capacity and initializes with init_items"""
        self.capacity= capacity         # capacity of queue
        self.items = [None]*capacity    # array for queue
        self.num_items = 0              # number of items in queue
        self.front = 0                  # front index of queue (items removed from front)
        self.rear = 0                   # rear index of queue (items enter at rear)
        if init_items is not None:      # if init_items is not None, initialize queue
            if len(init_items) > capacity:
                raise IndexError
            else:
                self.num_items = len(init_items)
                self.items[:self.num_items] = init_items

    def __eq__(self, other):
        return ((type(other) == Queue)
            and self.capacity == other.capacity
            and self.get_items() == other.get_items()
            )

    def __repr__(self):
        return ("Queue({!r}, {!r})".format(self.capacity, self.get_items()))

    # get_items returns array (Python list) of items in queue
    # first item in the list will be front of queue, last item is rear of queue
    def get_items(self):
        if self.num_items == 0:
            return []
        if self.front < self.rear:
            return self.items[self.front:self.rear]
        else:
            return self.items[self.front:] + self.items[:self.rear]

# ----------------------------- #

    def is_empty(self):
        return self.num_items == 0
        """Returns true if the queue is empty and false otherwise"""

    def is_full(self):
        return self.num_items == self.capacity ## if num.items == capacity, then array queue is full 
        """Returns true if the queue is full and false otherwise"""

    def enqueue(self, item):
        if not self.is_full(): 
            self.items[self.rear] = item # replace item in the rear index with item 
            if self.rear == (self.capacity - 1): # indicates wrap around is needed, i.e. rear wraps to  
            # index 0 
                self.rear = 0 
            else: 
                self.rear += 1 # if rear index is not at capacity then we increment rear to next index # 
            self.num_items += 1 # increment num_items so we can keep track of # of items 
        else: 
            raise IndexError
        """enqueues item"""

    def dequeue(self):
        if not self.is_empty(): 
            temp = self.items[self.front] # extracts item at front index position 
            self.front = (self.front + 1) % self.capacity # if front + 1 is not beyond capacity, then we 
            # increment self.front by one 
            self.num_items -= 1 # decrement num_items 
            return temp # return item we dequeued 
        else: 
            raise IndexError

        """dequeues item"""

    def size(self):
        return self.num_items

    """Returns the number of items in the queue"""
