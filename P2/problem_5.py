# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
    
    def suffixes_helper(self, suffix):
        ## Helper method to get all the suffixes from the TrieNode
        if self.is_word:
            yield suffix 
            
        for i in self.children:
            yield from self.children[i].suffixes_helper(suffix + i)
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        ## For example, if our Trie contains the words `["fun", "function", "factory"]` 
        ## and we ask for suffixes from the `f` node, we would expect to 
        ## receive `["un", "unction", "actory"]` back from `node.suffixes()`.
        suffixes_generator =  self.suffixes_helper(suffix)
        output = []
        
        for elem in suffixes_generator:
            output.append(elem)
        
        return output
        
            
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]
            
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        
        for char in prefix:
            if char not in current_node.children:   
                return
            current_node = current_node.children[char]

        return current_node
    
        

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

print(MyTrie.find('f')) 
# Case when the Trie has a TrieNode with the prefix 'f'
# Output -  TrieNode with the prefix 'f' 

print(MyTrie.find('a').suffixes()) 
# returns all the suffixes with the prefix 'a' which is ['nt', 'nthology', 'ntagonist', 'ntonym']

print(MyTrie.find('f').suffixes('bla'))
# returns all the suffixes with the prefix 'f' and prepends those with the suffix = 'bla' which is
# ['blaun', 'blaunction', 'blaactory']

print(MyTrie.find('').suffixes())
# Case when looking for siffix of empty string prefix then it returns all the words in the Trie
# Output - ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']

print(MyTrie.find('h'))
# Case when given a prefix which is not in the Trie
# Output - None

print(MyTrie.find('')== MyTrie.root)
print(MyTrie.find(''))
# Case when prefix is empty string
# Output - root of the Trie

try:
    print(MyTrie.find('g').suffixes())
except AttributeError:
    print("Please insert words into the Trie to search for suffixes.")
    
# Case when trying to get the suffixes for a prefix which is not in the Trie
# Output - AttributeError: 'NoneType' object has no attribute 'suffixes'
# Hence, given custom error


