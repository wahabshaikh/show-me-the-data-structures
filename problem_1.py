from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity=0):
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

        try:
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
        except:
            print("INVALID: Setting to cache with capacity 0")        

''' Test Case 1 '''
print("\nTest Case 1")
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)

print(our_cache.get(1))
# Expected output: 1

print(our_cache.get(9))
# Expected output: -1

our_cache.set(6, 6)

print(our_cache.get(2)) # 2 is the LRU element
# Expected output: -1

print(our_cache.get(6)) # 6 replaced 2 in the cache
# Expected output: 6


''' Test case 2 '''
print("\nTest Case 2: Empty cache")
our_cache = LRU_Cache()

our_cache.set(1, 1)
# Expected output: INVALID: Setting to cache with capacity 0

print(our_cache.get(1))
# Expected output: -1


''' Test Case 3 '''
print("\nTest Case 3: Large cache")
our_cache = LRU_Cache(1000)

for i in range(10000):
    our_cache.set(i, i)

print(our_cache.get(8999))
# Expected output: -1

print(our_cache.get(9000))
# Expected output: 9000

print(our_cache.get(10000))
# Expected output: -1
