import sys
from heapq import heapify, heappop, heappush


class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency

    def get_character(self):
        return self.character

    def get_frequency(self):
        return self.frequency

    def __lt__(self, other):
        return self.frequency < other.frequency


class HuffmanTreeNode():
    def __init__(self, frequency, left, right):
        self.frequency = frequency
        self.left_child = left
        self.right_child = right
        self.left_bit = '0'
        self.right_bit = '1'

    def get_frequency(self):
        return self.frequency
    
    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_left_bit(self):
        return self.left_bit

    def get_right_bit(self):
        return self.right_bit

    def __lt__(self, other):
        return self.frequency < other.frequency


def huffman_encoding(data):
    # Handling blank strings
    if not data:
        return "", None

    # Determine the frequency of each character in the message
    char_freqs = dict()
    for char in data:
        if char not in char_freqs:
            char_freqs[char] = 1
        else:
            char_freqs[char] += 1
    
    # Build a list of nodes
    list_of_nodes = [Node(char, freq) for char, freq in char_freqs.items()]

    # Convert the list into a min heap
    min_heap = list_of_nodes
    heapify(min_heap) # O(n)

    # Build the Huffman tree
    while len(min_heap) > 1:
        # Pop-out two nodes with the minimum frequency
        left_node = heappop(min_heap)
        right_node = heappop(min_heap)
        
        # Create a new node with a frequency equal to the sum of the two nodes
        freq = left_node.get_frequency() + right_node.get_frequency()
        internal_node = HuffmanTreeNode(freq, left_node, right_node)

        # Reinsert the newly created node
        heappush(min_heap, internal_node)

    # Calculate the Huffman Code for each character
    huffman_codes = dict()
    root = min_heap[0]
    
    def calculate_huffman_code(node, code=[]):
        if isinstance(node, Node):
            if not code:
                huffman_codes[node.get_character()] = node.get_character()
            else:
                huffman_codes[node.get_character()] = "".join(code)
            return
        

        code.append(node.get_left_bit())
        calculate_huffman_code(node.get_left_child(), code)
        code.pop()

        code.append(node.get_right_bit())
        calculate_huffman_code(node.get_right_child(), code)
        code.pop()

        return

    calculate_huffman_code(root)

    # Encode the data
    encoded_data = ""
    for char in data:
        encoded_data += huffman_codes[char]

    return encoded_data, root
    

def huffman_decoding(data,tree):
    # Handle empty strings
    if not data:
        return ""

    decoded_data = ""

    # Decode the data
    node = tree
    for bit in data:    
        if isinstance(node, Node):
            decoded_data += node.get_character()
            node = tree           
        if bit == '0':
            node = node.get_left_child()
        elif bit == '1':
            node = node.get_right_child()
        else:
            return data
    else:
        decoded_data += node.get_character()

    return decoded_data


if __name__ == "__main__":
    test_cases = ["The bird is the word", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "AAA", ""]

    for i, test in enumerate(test_cases):
        print("\nTest Case: {}\n".format(i + 1))

        a_great_sentence = test

        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = huffman_encoding(a_great_sentence)

        try:
            print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        except:
            print ("The size of the decoded data is: {}\n".format(sys.getsizeof(encoded_data)))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))


# Expected Output

# Test Case: 1

# The size of the data is: 69

# The content of the data is: The bird is the word

# The size of the encoded data is: 36

# The content of the encoded data is: 1110111111101010001100110000101100101101101011111101010000111001100001

# The size of the decoded data is: 69

# The content of the encoded data is: The bird is the word


# Test Case: 2

# The size of the data is: 75

# The content of the data is: ABCDEFGHIJKLMNOPQRSTUVWXYZ

# The size of the encoded data is: 44

# The content of the encoded data is: 1010100001010011101111100111001101010110010101111101101111100000010011001100010011111111100111100010010001110100011101100001

# The size of the decoded data is: 75

# The content of the encoded data is: ABCDEFGHIJKLMNOPQRSTUVWXYZ


# Test Case: 3

# The size of the data is: 52

# The content of the data is: AAA

# The size of the decoded data is: 52

# The content of the encoded data is: AAA

# The size of the decoded data is: 52

# The content of the encoded data is: AAA


# Test Case: 4

# The size of the data is: 49

# The content of the data is: 

# The size of the decoded data is: 49

# The content of the encoded data is: 

# The size of the decoded data is: 49

# The content of the encoded data is: