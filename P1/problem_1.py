import collections

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache_dict = collections.OrderedDict() # this datastructure remembers the insertion order

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.cache_dict:
            value = -1
        else:
            value = self.cache_dict.pop(key)
            self.cache_dict[key] = value
            
        print("key: {} - value: {}".format(key, value))
        return value


    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache_dict:
            self.cache.pop(key)
        else:
            if len(self.cache_dict) >= self.capacity:
                self.cache_dict.popitem(last=False) # As last = False, we will get least accessed item (FIFO order)

        self.cache_dict[key] = value        


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
