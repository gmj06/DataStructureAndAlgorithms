import sys
import heapq
import collections
import os

class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return other.freq > self.freq


class Huffman_coding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}
        self.root = None

    def build_frequency_dict(self, text):
        """ Building frequency dictionary with sorted values from low to high """
        freq_dict = {}

        for char in text:
            if not char in freq_dict:
                freq_dict[char] = 0
            freq_dict[char] += 1
        sorted_freq_tuple = sorted(freq_dict.items(), key = lambda key_value: (key_value[1], key_value[0]))
        return collections.OrderedDict(sorted_freq_tuple)
        

    def build_heap(self, freq_dict):
        """ Building PriorityQueue of frequency dictionary """
        for key in freq_dict:
            new_node = HeapNode(key, freq_dict[key])
            self.heap.append(new_node)

    def merge_nodes(self):
        """ Build tree by merging two small frequencies at every point in time """
        while len(self.heap) > 1:
            left_node = heapq.heappop(self.heap)
            right_node = heapq.heappop(self.heap)
            merge_node = HeapNode(None, left_node.freq + right_node.freq)
            merge_node.left = left_node
            merge_node.right = right_node
            heapq.heappush(self.heap, merge_node)


    def build_Huffman_tree_helper(self, root, current_code):
        """ Heper function to build Binary Tree """
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.build_Huffman_tree_helper(root.left, current_code + "0")
        self.build_Huffman_tree_helper(root.right, current_code + "1")

    def build_Huffman_tree(self):
        """ Build the Binary Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. """
        self.root = heapq.heappop(self.heap)
        current_code = ""
        self.build_Huffman_tree_helper(self.root, current_code)

    def get_encoded_text(self, text):
        """ Encoding the given text using the generated codes array """
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        return encoded_text

    def get_decoded_text(self, encoded_text):
        """ Extra method to decode the given encoded text using reverse_mapping dictionary """
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit

            if current_code in self.reverse_mapping:
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text

    def get_root(self):
        """ Property to get Huffman Tree root """
        return self.root

    def compress(self, text):
        """ Compressing the given text using Huffman Class methods/functions"""
        if text == "":
            return

        freq_dict = self.build_frequency_dict(text)
        self.build_heap(freq_dict)
        self.merge_nodes()
        self.build_Huffman_tree()
        encoded_text = self.get_encoded_text(text)
        return encoded_text

         

    def decompress(self, encoded_data, tree_root):
        """ Decompressing the given compressed/encoded text using Huffman Class methods/functions"""
        if encoded_data == "" or tree_root is None:
            return

        decoded_text = ""; 
        current_node = tree_root; 
        for data in encoded_data:
            if (data == '0'): 
                current_node = current_node.left; 
            else:
                current_node = current_node.right; 
        
            # reached leaf node 
            if (current_node.left is None and current_node.right is None):
                decoded_text += current_node.char
                current_node = tree_root

        return decoded_text

        


def huffman_encoding(data):
    """ Encoding the given data using Huffman_coding class """
    coding = Huffman_coding()
    return coding.compress(data), coding.get_root()

def huffman_decoding(data,tree):
    """ Decoding the given encoded data using Huffman_coding class """
    coding = Huffman_coding()
    return coding.decompress(data, tree)
    

if __name__ == "__main__":
    codes = {}

    print(" --- Test Case 1 --- ")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    print(" --- Test Case 2 --- ")
    a_great_sentence2 = "DataStructure and Algorithm Nanodegree in UDACITY!!!"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence2)))
    print ("The content of the data is: {}\n".format(a_great_sentence2))

    encoded_data2, tree2 = huffman_encoding(a_great_sentence2)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data2, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data2))

    decoded_data2 = huffman_decoding(encoded_data2, tree2)
   
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data2)))
    print ("The content of the decoded data is: {}\n".format(decoded_data2))

    print(" --- Test Case 3 --- ")
    a_great_sentence3 = ""
    
    # As per documentation (https://docs.python.org/3/library/sys.html), getsizeof() calls the object’s __sizeof__ method and adds an additional garbage collector overhead if the object is managed by the garbage collector.
    # Hence, even though given data is empty string, the below line gives you the size 
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence3)))
    print ("The content of the data is: {}\n".format(a_great_sentence3))

    encoded_data3, tree3 = huffman_encoding(a_great_sentence3)

    # This line throws a "TypeError: int() can't convert non-string with explicit base"
    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data3, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data3))

    decoded_data3 = huffman_decoding(encoded_data3, tree3)
   
    # As per documentation (https://docs.python.org/3/library/sys.html), getsizeof() calls the object’s __sizeof__ method and adds an additional garbage collector overhead if the object is managed by the garbage collector.
    # Hence, even though given data is empty string, the below line gives you the size  
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data3)))
    print ("The content of the decoded data is: {}\n".format(decoded_data3))

    print(" --- Test Case 4 --- ")
    a_great_sentence4 = "Empty Tree Node Testing"
    
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence4)))
    print ("The content of the data is: {}\n".format(a_great_sentence4))

    encoded_data4, tree4 = huffman_encoding(a_great_sentence4)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data4, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data4))

    decoded_data4 = huffman_decoding(encoded_data4, None)
   
    # As per documentation (https://docs.python.org/4/library/sys.html), getsizeof() calls the object’s __sizeof__ method and adds an additional garbage collector overhead if the object is managed by the garbage collector.
    # Hence, even though given data is empty string, the below line gives you the size  
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data4)))
    print ("The content of the decoded data is: {}\n".format(decoded_data4))

