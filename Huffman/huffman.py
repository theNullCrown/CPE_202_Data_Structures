# Name: Allie Blaising 


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the frequency count associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __lt__(self, other):
        return comes_before(self, other) # Allows use of Python List sorting

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node



def comes_before(a, b):
    if a.freq == b.freq: # If the frequency of node A is equal to the frequency of node B then we check 
    # if A's ASCII character value is less then B's value 
        return a.char < b.char
    return a.freq < b.freq # Else, we compare the frequency of A and B nodes alone 


def combine(a, b):
    if comes_before(a, b): # Checks to see if B node is greater than A node; If it is then we know that B node will be the 
        # new right child, and A node will be the new left 
        parent = HuffmanNode(min(a.char, b.char), (a.freq + b.freq)) 
        parent.right = b
        parent.left = a
        return parent 
    else: # If B is not greater than A, then we know that B node will be the left node and A will be the greater right node
        parent = HuffmanNode(min(a.char, b.char), (a.freq + b.freq)) 
        parent.right = a
        parent.left = b
        return parent 

"""Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
The new node's frequency value will be the sum of the a and b frequencies
The new node's char value will be the lesser of the a and b char ASCII values"""

def parse_header(header_string): 
    counts = [0]*256 # Start by creating an empty python list with 256 entries initialized to zero
    header_string = header_string.split()
    for i in range(0, len(header_string), 2): 
        counts[int(header_string[i])] = header_string[int(i + 1)] # Once, we've extracted the current frequency, we want to iterate the frequency by 1 to 
    counts = [int(i) for i in counts]
        # account for the current character we just read in 
    return counts # Return python list counts of 256 entries with frequencies corresponding to occurences of characters 

"""Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file
    Returns a Python List with 256 entries - counts are initialized to zero.
    The ASCII value of the characters are used to index into this list for the frequency counts"""


"""Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""

def create_huff_tree(char_freq):
    huffs = [] # Empty list that we will 
    for char,freq in enumerate(char_freq):
        print(freq)
        # For loop w/ enumerate that allows us to keep a number associated with every pass through 
        # the items in char_freq. We do this because the count of the indices we're on translate back to the ASCII character code that 
        # we need to create a new huffman node
        if int(freq) > 0: # If the freq is > 0 then we want to create a huffman node with the frequency and character  
            huffs.append(HuffmanNode(char,freq))
    # After we've iterated through char_freq and created a list of huffman_nodes, we enter a while loop 
    while len(huffs) > 1: 
        huffs.sort() # Start by sorting list (Python will do this using the logic associated with comes_before)
        node0 = huffs.pop(0) # Once the list is sorted, we want to pop the first two items in our sorted list (and this case will be 
        # the lowest two because we've sorted the list)
        node1 = huffs.pop(0) # Pop second 
        huffs.append(combine(node0,node1)) # Combine node1 and node0 according to precedence logic in combine function and append the 
        # resulting parent node  
        # While loop will continue until our length of huffman nodes is 1, in which case we now we've completed all appropriate combinations 
        # and will just have one root parent huffman node 
    return huffs[0]


def create_code(node):
    output_array = ['']*256 # Create an array of 256 empty character strings 
    if node is not None: 
        return create_code_helper(node, '', output_array) # Call recursive function 
    return 


def create_code_helper(node, current_string, output_array): 
    if node.left == None and node.right == None: # Base case indicating that we can traverse back up to the head/root node 
        output_array[node.char] = current_string
    else: 
        if node.left != None: # If there is a left node to traverse, then we add 0 to current string 
            new_string = current_string + "0"
        # Next, we push node.left in and new string with added 0, to our recursive function 
            create_code_helper(node.left, new_string, output_array)
        if node.right != None: # If there is a right node to traverse, then we add 0 to current string 
            new_string = current_string + "1" 
            # Next, we push node.right in and new string with added 1, to our recursive function 
            create_code_helper(node.right, new_string, output_array) 
    return output_array

## Edge cases: 
# ─ If the input file consists of only one unique character, say "aaaaa", it should write just that
# character ASCII value followed by a space followed by the number of occurrences: “97 5”
# ─ In case of an empty input text file, your program should also produce an empty file. (DONE)
# ─ If an input file does not exist, your program should raise a FileNotFoundError.


def huffman_decode(encoded_file, decode_file): 
    try: 
        encoded = open(encoded_file, "r") # Open in_file and prepare to extract code from array based on the ord(char)
    except FileNotFoundError as error:
        raise FileNotFoundError
    header_string = encoded.readline()
    freq_list = parse_header(header_string) # Call count_freq that we are going to feed into create_header
    empty = True 
    for index in freq_list: 
        if index != 0: 
            empty = False 
    decode_file = open(decode_file, "w")
    if not empty: 
        output = create_header(freq_list) # Create output from create_header 
        huff_tree = create_huff_tree(output) # Create a huffman tree with frequency_list 
        encoded_seq = encoded.read_line()
        if len(encoded_seq) == 0: 
            for i in len(output): 
                out_string = ''
                if output[i] != 0: 
                    out_string += chr(out_string)*output[i]
        else: 
            out_string = ''
            root = huff_tree
            for i in range(len(encoded_seq)): 
                if encoded_seq[i] == 1: 
                    huff_tree = huff_tree.left
                    if huff_tree.right == None and huff_tree.left == None: 
                        out_string += chr(huff_tree.char)
                        huff_tree = root  
                elif encoded_seq[i] == 0: 
                    huff_tree = huff_tree.right
                    if huff_tree.right != None and huff_tree.right == None: 
                        out_string += chr(huff_tree.char)
                        huff_tree = root
    elif empty: 
        decode_file.write(" ")
        decode_file.close()


## Pseudo code: 
'''
    temp_list = ""
    while huff_tree.right != None and huff_tree.left != None: 
        if huff_tree.right: 
            huff_tree = huff_tree.right 
        if huff_tree.left: 
            huff_tree = huff_tree.left 
    temp_list += str(huff_tree.char)*huff_tree.freq

'''

def create_header(freq_list): 
    new_string = ''
    for char,freq in enumerate(freq_list): # For loop w/ enumerate that allows us to keep a number associated with every pass through 
        # the items in char_freq. We do this because the count of the indices we're on translate back to the ASCII character code that 
        # we need to create a new huffman node
        if freq > 0:
            new_string += str(char) + ' ' + str(freq) + ' ' # Separate char and freq with spaces 
    return new_string.rstrip() # Strip excess white space from the end of header 


