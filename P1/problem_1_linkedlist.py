
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return "(%s, %s)" % (self.key, self.value)


class LRU_Cache(object):
    def __init__(self, capacity=0): # given default capacity = 0
        # Initialize class variables
        self.cache = {}
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.num_caches = 0

    def get(self, key):
        """ Retrieve item from provided key. Return -1 if nonexistent. """
        if (key not in self.cache):
            value = -1
        else:    
            node = self.cache[key]
            self.remove_node(node)
            self.set_head(node)
            value = node.value

        print(f"key: {key}, value: {value}")
        return value

    def set(self, key, value):
        """ Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. """
        try:
            if key in self.cache:
                node = self.cache[key]
                node.value = value
                self.remove_node(node)
                self.set_head(node)
            else:
                new_node = Node(key, value)
                if self.num_caches == self.capacity:
                    del self.cache[self.tail.key]
                    self.remove_node(self.tail)

                if self.capacity > 0:
                    self.set_head(new_node)
                    self.cache[key] = new_node   
                else:
                    raise AttributeError("Please create the LRU_Cache object with capacity greater than 0")

        except AttributeError:
            print("Please create the LRU_Cache object with capacity greater than 0")

       
    def set_head(self, node):
        """ Set given node as head of the Doubly Linked List """
        node.next = self.head
        node.prev = None
        if self.head is not None:
            self.head.prev = node

        self.head = node
        if self.tail is None:
            self.tail = node
        
        self.num_caches += 1

    def remove_node(self, node):
        """ Remove the given node from the Doubly Linked List """
        if self.head is None:
            return
    
        """ Updating the pointers on removing the node """
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        """ Removing the tail node """
        if self.tail == node:
            self.end = node.prev
            self.end.next = None

        self.num_caches -= 1
        return node
  

# Test case 1 - with Capcaity > 0
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)
our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
our_cache.get(5)      # returns 5
our_cache.set(5, 10)
our_cache.get(5)   # after setting new value, returns 10

# Test Case 2 -- With capcaity = 0
our_cache1 = LRU_Cache(0)
our_cache1.set(1, 11) # returns - custom error message
our_cache1.set(2, 22) # returns - custom error message

our_cache1.get(1)  # return  -1 because 1 is not found in the cache

# Test Case 3 -- With capcaity < 0
our_cache2 = LRU_Cache(-1)
our_cache2.set(11, 11) # returns - custom error message
our_cache2.set(22, 22) # returns - custom error message
our_cache2.get(11)  # return  -1 because 1 is not found in the cache
our_cache2.get(55)  # return  -1 because 1 is not found in the cache

# Test Case 3 -- Without capcaity
our_cache3 = LRU_Cache() 
# Exception "TypeError: __init__() missing 1 required positional argument" 
# is handled by giving default value 0 for capacity

our_cache3.set(11, 11) # returns - custom error message
our_cache3.get(100)  # return  -1 because 1 is not found in the cache

