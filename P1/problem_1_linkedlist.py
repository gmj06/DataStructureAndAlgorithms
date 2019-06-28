
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return "(%s, %s)" % (self.key, self.value)


class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.hash_map = {}
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.num_caches = 0

    def get(self, key):
        """ Retrieve item from provided key. Return -1 if nonexistent. """
        if key not in self.hash_map:
            print("-1")
            return -1

        node = self.hash_map[key]
        self.remove_node(node)
        self.set_head(node)

        print(node.value)
        return node.value

    def set(self, key, value):
        """ Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. """
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            self.remove_node(node)
            self.set_head(node)
        else:
            new_node = Node(key, value)
            if self.num_caches == self.capacity:
                del self.hash_map[self.tail.key]
                self.remove_node(self.tail)

            self.set_head(new_node)
            self.hash_map[key] = new_node
       
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
  


our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

# print("[num_caches = %s, head = %s, tail = %s]" % (str(our_cache.num_caches), str(our_cache.head), str(our_cache.tail)))
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache
# print("[num_caches = %s, head = %s, tail = %s]" % (str(our_cache.num_caches), str(our_cache.head), str(our_cache.tail)))
our_cache.set(5, 5)
# print("[num_caches = %s, head = %s, tail = %s]" % (str(our_cache.num_caches), str(our_cache.head), str(our_cache.tail)))
our_cache.set(6, 6)
# print("[num_caches = %s, head = %s, tail = %s]" % (str(our_cache.num_caches), str(our_cache.head), str(our_cache.tail)))
our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

