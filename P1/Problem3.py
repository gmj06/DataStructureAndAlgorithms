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
        """ Heper function to build Huffman Tree """
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.build_Huffman_tree_helper(root.left, current_code + "0")
        self.build_Huffman_tree_helper(root.right, current_code + "1")

    def build_Huffman_tree(self):
        """ Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. """
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
        freq_dict = self.build_frequency_dict(text)
        self.build_heap(freq_dict)
        self.merge_nodes()
        self.build_Huffman_tree()
        encoded_text = self.get_encoded_text(text)
        return encoded_text

    def decompress(self, encoded_data, tree_root):
        """ Decompressing the given compressed/encoded text using Huffman Class methods/functions"""
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
            
        return decoded_text; 


def huffman_encoding(data):
    coding = Huffman_coding()
    return coding.compress(data), coding.get_root()

def huffman_decoding(data,tree):
    coding = Huffman_coding()
    return coding.decompress(data, tree)
    

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


    a_great_sentence2 = "DataStructure and Algorithm Nanodegree in UDACITY!!!"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence2)))
    print ("The content of the data is: {}\n".format(a_great_sentence2))

    encoded_data2, tree2 = huffman_encoding(a_great_sentence2)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data2, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data2))

    decoded_data2 = huffman_decoding(encoded_data2, tree2)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data2)))
    print ("The content of the encoded data is: {}\n".format(decoded_data2))


