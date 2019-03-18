# Name: Allie Blaiisng 


class MyHashTable:

    def __init__(self, table_size=11):
        self.table_size = table_size
        self.hash_table = [[] for _ in range(table_size)] # List of lists implementation
        self.num_items = 0
        self.num_collisions = 0


    def hashfunction(self,key,size):
       return key % size

    def insert(self, key, value):
        hash_value = self.hashfunction(key, len(self.hash_table))
        if len(self.hash_table[hash_value]) == 0: 
            self.hash_table[hash_value].append((key, value))
            self.num_items += 1 
        elif self.hash_table[hash_value] != []: 
            found = False
            for entry in self.hash_table[hash_value]: 
                if key == entry[0]: 
                    entry = (key, value)
                    found = True
            if not found: 
                self.hash_table[hash_value].append((key, value)) 
                self.num_collisions += 1 
                self.num_items += 1
        if self.load_factor() > 1.5: 
            new_hash = MyHashTable((2*(self.table_size) + 1))
            for key_item in self.hash_table: 
                if key_item != []: 
                    for inner_key in key_item: 
                        new_hash.insert(inner_key[0], inner_key[1])
            self.hash_table = new_hash.hash_table
            self.table_size = new_hash.table_size
            # Add special test cases here 
        "Takes a key, and an item.  Keys are valid Python non-negative integers. \
        The function will insert the key-item pair into the hash table based on the \
        hash value of the key mod the table size (hash_value = key % table_size)"

    def hashfunction(self,key,size):
       return key % size

    def get_item(self, key):
        hash_value = self.hashfunction(key, (self.table_size))
        position = self.hash_table[hash_value] 
        for i in position: 
            if i[0] == key: 
                return i[1] 
        else: 
            raise LookupError


        "Takes a key and returns the item from the hash table associated with the key. \
        If no key-item pair is associated with the key, the function raises a LookupError exception."

    def remove(self, key):
        hash_value = self.hashfunction(key, (self.table_size))
        position = self.hash_table[hash_value] 
        for i in position: 
            if i[0] == key: 
                returned = i
                i = [] 
                self.num_items -= 1 
                return returned
        else: 
            raise LookupError

        "Takes a key, removes the key-item pair from the hash table and returns the key-item pair. \
        If no key-item pair is associated with the key, the function raises a LookupError exception. \
        (The key-item pair should be returned as a tuple)"

    def load_factor(self):
        return self.num_items / self.table_size
        "Returns the current load factor of the hash table"

    def size(self):
        return self.num_items
        "Returns the number of key-item pairs currently stored in the hash table"

    def collisions(self):
        return self.num_collisions
        "Returns the number of collisions that have occurred during insertions into the hash table"

