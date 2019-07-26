import collections

class LRU_Cache(object):

    def __init__(self, capacity=0):
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
        try:
            if key in self.cache_dict:
                self.cache_dict.pop(key)
            else:
                if len(self.cache_dict) >= self.capacity:
                    self.cache_dict.popitem(last=False) # As last = False, we will get least accessed item (FIFO order)

            self.cache_dict[key] = value        
        except KeyError:
            print("Please create the LRU_Cache object with capacity greater than 0")



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
