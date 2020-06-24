from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables

        self.cache = dict()
        self.capacity = capacity
        self.queue = deque() # To keep track of LRU element

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 

        if key in self.cache:
            # Send the key to the end of the queue
            self.queue.remove(key) # O(n)
            self.queue.append(key) # O(1)

            return self.cache[key]

        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 

        if key in self.cache:
            # Send the key to the end of the queue
            self.queue.remove(key) # O(n)
            self.queue.append(key) # O(1)

            # Update existing key
            self.cache[key] = value

        elif len(self.cache) < self.capacity:
            self.cache[key] = value
            self.queue.append(key) # O(1)

        else:
            # Fetch LRU element
            lru_element = self.queue.popleft() # O(1)            
            
            self.queue.append(key) # O(1)
            self.cache[key] = value

            del self.cache[lru_element] # O(1)
            

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)


''' Test case 1: Key present in the cache '''
print(our_cache.get(1))
# Expected output: 1


''' Test case 2: Key NOT present in the cache '''
print(our_cache.get(9))
# Expected output: -1


''' Test case 3: LRU element replaced in the cache '''
our_cache.set(6, 6)

print(our_cache.get(2)) # 2 is the LRU element
# Expected output: -1

print(our_cache.get(6)) # 6 replaced 2 in the cache
# Expected output: 6


