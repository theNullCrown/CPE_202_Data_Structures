# Name: Allie Blaising 

from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        return ((type(other) == TreeNode)
                and self.key == other.key
                and self.data == other.data
                and self.left == other.left
                and self.right == other.right
                )

    def __repr__(self):
        return ("TreeNode({!r}, {!r}, {!r}, {!r})".format(self.key, self.data, self.left, self.right))

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        return self.root == None # If self.root is None then we know that there is nothing in 
        # the tree

    def search(self, key): 
        if self.root != None: # While there are still nodes to check, then we can call self.search_helper 
        # on the next node 
            return self.search_helper(key, self.root) # Return the result of looking for this node 
            # at the root of the tree
        else: 
            return False 

    def search_helper(self, key, current_node): 
        if key == current_node.key: 
            return True 
        elif key < current_node.key and current_node.left != None: 
            return self.search_helper(key, current_node.left)
        elif key > current_node.key and current_node.right != None: 
            return self.search_helper(key, current_node.right)
        return False 


    def insert(self, key, data=None):
        if self.root == None:  # If there is no root, then create a new TreeNode with key and data (None) and set  
        # as root 
            self.root = TreeNode(key, data)
        else: # If there is at least one root: 
            current = self.root # Initiate current to self.root 
            inserted = False 
            while not inserted: # While we haven't found the location of the last node we are going to inser, i.e. the 
            # last node, in either right or left direction depending on key value, then we keep going through the below 
            # conditional structure: 
                if key < current.key: # If key < current.key then we know we're going to look left first 
                    if current.left != None: # If there is a left child, then we move to that left child, making 
                    # current the next left child and returning to beginning of while loop 
                        current = current.left 
                    else: # If there is no left child, i.e., we've reached the end of the last line, then we 
                    # make a new node and true inserted True 
                        current.left = TreeNode(key, data)
                        inserted = True
                elif key > current.key: # If key > current.key then we know we're going to look right first 
                    if current.right != None: 
                        current = current.right # If there is a right child left to traverse, then change current, to 
                        # next right child 
                    else: 
                        current.right = TreeNode(key, data) # If we've reached the last right child node, then we  
                        # can create a new node and assign it to the current.right, i.e. make current that didn't have a 
                        # a child, now have a child 
                        inserted = True # Conditional to break out of the loop 
                else: 
                    current.key = key # Condition to check if the key has already been inserted, if current.key is already 
                    # equal to key, then inserted is True because it was already apart of the list 
                    inserted = True  



    def find_min(self): 
        if self.root != None: 
            current = self.root  
            while current.left != None: # The min key is always going to be the last left child, so we are going 
            # to traverse through every left child, until the current node's left child is none at which point 
            # we know we've reached the end of the list. 
                current = current.left 
            return (current.key, current.data) # Return key and data is tuple form 
        else: 
            return None # If there is just one node, then we want to return None, nothing to traverse to look for min 



    def find_max(self): 
        if self.root != None: 
            current = self.root 
            while current.right != None: # Same as above, but with right child now 
                current = current.right
            return (current.key, current.data)
        else: 
            return None


    def tree_height(self):
        if self.root != None: # If tree is not empty then feed self.root (top node) into 
        # tree_height_helper function 
            return self.tree_height_helper(self.root, 0)
        else: 
            return None # If empty case return None 


    def tree_height_helper(self, current_node, current_height): 
        if current_node == None: # Checks empty condition 
            return current_height 
        else: 
            left_height = self.tree_height_helper(current_node.left, current_height)  
            right_height = self.tree_height_helper(current_node.right, current_height)
            return max(left_height, right_height)

        # return the height of the tree
        # returns None if tree is empty

    def inorder_list(self): 
        inorder_list = []
        current = self.root
        return self.inorder_list_helper(current, inorder_list)


    def inorder_list_helper(self, current, inorder_list): 
        if current is None: 
            return 
        if current.left: 
            self.inorder_list_helper(current.left, inorder_list) 
        inorder_list.append(current.key)
        if current.right:
            self.inorder_list_helper(current.right, inorder_list)
        return inorder_list

## self.root
        # return Python list of BST keys representing in-order traversal of BST
       # pass

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        preorder_list = []
        current = self.root 
        self.preorder_list_helper(current, preorder_list)
        return preorder_list


    def preorder_list_helper(self, current, preorder_list): 
        if current is None: 
            return 
        preorder_list.append(current.key)
        if current.left: 
            self.preorder_list_helper(current.left, preorder_list)
        if current.right: 
            self.preorder_list_helper(current.right, preorder_list) 
        return 


    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) 
        temp_list = []
        q.enqueue(self.root)
        while not q.is_empty(): 
            output_node = q.dequeue() 
            if output_node.left != None: 
                q.enqueue(output_node.left) 
            if output_node.right != None: 
                q.enqueue(output_node.right)
            temp_list.append(output_node.key)
        return temp_list


        
