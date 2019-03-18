# Name: Allie Blaising 


class MaxHeap:

    def __init__(self, capacity=50):
        self.heap_list = [0]*(capacity + 1) 
        self.current_size = 0
        self.capacity = capacity
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""


    def enqueue(self, item):
        if not self.is_full(): 
            self.current_size += 1
            self.heap_list[self.current_size] = item # Append before making sure that appended number aligns with heap property 
            self.perc_up(self.current_size)
            return True 
        return False 
        # For max heap, largest value is always @ the start 
        """inserts "item" into the heap, returns true if successful, false if there is no room in the heap"""


    def peek(self):
        if not self.is_empty(): 
            return self.heap_list[1]
        return None 
        """returns max without changing the heap, returns None if the heap is empty"""

    def dequeue(self):
        if not self.is_empty(): 
            max_element = self.heap_list[1]
            self.heap_list[1] = self.heap_list[self.current_size]
            self.current_size -= 1
            self.perc_down(1)
            return max_element
        return None 

        """returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty"""


    def contents(self):
        if not self.is_empty(): 
            return self.heap_list[1:self.current_size + 1]
        else:  
            None
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""


    def build_heap(self, alist):
        if len(alist) > (self.get_capacity()):
            self.heap_list = [0]*(len(alist) + 1) 
            self.capacity = len(alist)
        for i in range(len(alist)): 
            self.heap_list[i + 1] = alist[i]
        self.current_size = len(alist)
        i = len(alist) // 2
        while (i > 0):
            self.perc_down(i)
            i -= 1

        """Discards the items in the current heap and builds a heap from 
        the items in alist using the bottom up method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""


    def is_empty(self):
        return self.current_size == 0 
        """returns True if the heap is empty, false otherwise"""


    def is_full(self):
        return self.current_size == self.capacity
        """returns True if the heap is full, false otherwise"""

        
    def get_capacity(self):
        return (self.capacity)
        """this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold"""
    
    
    def get_size(self):
        return self.current_size
        """the actual number of elements in the heap, not the capacity"""

    def find_max_child(self, i): 
        if (i * 2) + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[(i * 2) + 1]:
                return (i * 2) + 1
            else:
                return i * 2 

        
    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.find_max_child(i)
            if self.heap_list[i] < self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc


        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""

        
    def perc_up(self, i):
        parent = i // 2
        if i <= 1:
            return
        elif parent != 0 and self.heap_list[i] > self.heap_list[parent]:
            self.heap_list[i], self.heap_list[parent] = self.heap_list[parent], self.heap_list[i]
            self.perc_up(parent)

        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""


    def heap_sort_ascending(self, alist):
        new_heap = MaxHeap(len(alist))
        new_heap.build_heap(alist)
        while new_heap.current_size > 0:
            max_item = new_heap.dequeue()
            alist.remove(max_item)
            alist.insert(0 , max_item)

        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate alist to put the items in ascending order"""


